#!/usr/bin/env python3
"""
Activity Tracking Script for Claude Code Sessions
Hooks into VSCode extension events to track time and file interactions
"""

import sqlite3
import json
import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from fnmatch import fnmatch
from typing import Optional, Dict, Any
import uuid

# Add project root to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load configuration
CONFIG_FILE = PROJECT_ROOT / "config" / "activity-tracking-config.json"


class ActivityTracker:
    """Manages activity tracking for Claude Code sessions"""

    def __init__(self, config_path: Path = CONFIG_FILE):
        """Initialize the activity tracker"""
        self.config = self._load_config(config_path)
        self.db_path = PROJECT_ROOT / self.config['storage']['database_path']
        self.log_dir = PROJECT_ROOT / self.config['storage']['jsonl_log_dir']
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Initialize database
        self._init_database()

    def _load_config(self, config_path: Path) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}", file=sys.stderr)
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration if file not found"""
        return {
            "tracking": {"enabled": True, "idle_threshold_seconds": 300},
            "storage": {"database_path": ".tmp/activity-tracking.db", "jsonl_log_dir": ".tmp/activity-logs"},
            "department_detection": {"rules": [], "default_department": "General"},
            "summaries": {"daily_enabled": True}
        }

    def _init_database(self):
        """Initialize SQLite database with schema"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()

        # Create sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                slug TEXT,
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                total_duration_seconds INTEGER,
                git_branch TEXT,
                conversation_turns INTEGER DEFAULT 0,
                files_touched INTEGER DEFAULT 0,
                primary_department TEXT,
                status TEXT DEFAULT 'active'
            )
        ''')

        # Create activities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                timestamp TIMESTAMP,
                activity_type TEXT,
                target_file TEXT,
                department TEXT,
                duration_seconds INTEGER DEFAULT 0,
                FOREIGN KEY (session_id) REFERENCES sessions(session_id)
            )
        ''')

        # Create file_focus table for aggregated time per file
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_focus (
                focus_id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                file_path TEXT,
                department TEXT,
                total_duration_seconds INTEGER DEFAULT 0,
                interaction_count INTEGER DEFAULT 0,
                first_interaction TIMESTAMP,
                last_interaction TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES sessions(session_id)
            )
        ''')

        # Create daily_summaries table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_summaries (
                date DATE PRIMARY KEY,
                total_sessions INTEGER DEFAULT 0,
                total_duration_hours REAL DEFAULT 0,
                primary_department TEXT,
                ai_summary TEXT,
                top_files TEXT,
                report_path TEXT,
                synced_to_notion BOOLEAN DEFAULT FALSE
            )
        ''')

        conn.commit()
        conn.close()

    def detect_department(self, file_path: Optional[str]) -> str:
        """Detect department based on file path"""
        if not file_path:
            return self.config['department_detection']['default_department']

        # Make path relative to project root
        try:
            rel_path = Path(file_path).relative_to(PROJECT_ROOT)
        except ValueError:
            rel_path = Path(file_path)

        rel_path_str = str(rel_path)

        # Check against department rules
        for rule in self.config['department_detection']['rules']:
            if fnmatch(rel_path_str, rule['pattern']):
                return rule['department']

        return self.config['department_detection']['default_department']

    def should_track_file(self, file_path: Optional[str]) -> bool:
        """Check if file should be tracked based on exclude patterns"""
        if not file_path:
            return True

        exclude_patterns = self.config['tracking'].get('exclude_patterns', [])

        for pattern in exclude_patterns:
            if fnmatch(file_path, pattern):
                return False

        return True

    def get_or_create_session(self, session_id: Optional[str] = None) -> str:
        """Get current active session or create new one"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()

        # If session_id provided, use it
        if session_id:
            cursor.execute('SELECT session_id FROM sessions WHERE session_id = ? AND status = "active"', (session_id,))
            result = cursor.fetchone()
            if result:
                conn.close()
                return session_id

        # Check for active session from last 30 minutes
        cursor.execute('''
            SELECT session_id FROM sessions
            WHERE status = "active"
            AND datetime(start_time) > datetime('now', '-30 minutes')
            ORDER BY start_time DESC LIMIT 1
        ''')
        result = cursor.fetchone()

        if result:
            conn.close()
            return result[0]

        # Create new session
        new_session_id = str(uuid.uuid4())
        git_branch = self._get_git_branch()

        cursor.execute('''
            INSERT INTO sessions (session_id, start_time, git_branch, status)
            VALUES (?, ?, ?, 'active')
        ''', (new_session_id, datetime.now().isoformat(), git_branch))

        conn.commit()
        conn.close()

        return new_session_id

    def _get_git_branch(self) -> Optional[str]:
        """Get current git branch"""
        try:
            import subprocess
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception:
            pass
        return None

    def log_activity(self, session_id: str, activity_type: str, target_file: Optional[str] = None,
                    duration_ms: Optional[int] = None):
        """Log an activity event"""
        # Check if tracking is enabled
        if not self.config['tracking']['enabled']:
            return

        # Check if file should be tracked
        if target_file and not self.should_track_file(target_file):
            return

        department = self.detect_department(target_file)
        duration_seconds = (duration_ms / 1000) if duration_ms else 0

        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()

        # Insert activity
        cursor.execute('''
            INSERT INTO activities
            (session_id, timestamp, activity_type, target_file, department, duration_seconds)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session_id, datetime.now().isoformat(), activity_type, target_file, department, duration_seconds))

        # Update session conversation turns
        cursor.execute('''
            UPDATE sessions
            SET conversation_turns = conversation_turns + 1
            WHERE session_id = ?
        ''', (session_id,))

        # Update file focus if file-based activity
        if target_file:
            self._update_file_focus(cursor, session_id, target_file, department, duration_seconds)

        conn.commit()
        conn.close()

        # Log to JSONL
        self._log_to_jsonl({
            'timestamp': datetime.now().isoformat(),
            'session_id': session_id,
            'event_type': 'tool_use',
            'tool_name': activity_type,
            'file_path': target_file,
            'department': department,
            'duration_seconds': duration_seconds
        })

    def _update_file_focus(self, cursor, session_id: str, file_path: str, department: str, duration: float):
        """Update file focus aggregation"""
        # Check if record exists
        cursor.execute('''
            SELECT focus_id, total_duration_seconds, interaction_count
            FROM file_focus
            WHERE session_id = ? AND file_path = ?
        ''', (session_id, file_path))

        result = cursor.fetchone()

        if result:
            # Update existing
            cursor.execute('''
                UPDATE file_focus
                SET total_duration_seconds = total_duration_seconds + ?,
                    interaction_count = interaction_count + 1,
                    last_interaction = ?
                WHERE focus_id = ?
            ''', (duration, datetime.now().isoformat(), result[0]))
        else:
            # Insert new
            cursor.execute('''
                INSERT INTO file_focus
                (session_id, file_path, department, total_duration_seconds, interaction_count,
                 first_interaction, last_interaction)
                VALUES (?, ?, ?, ?, 1, ?, ?)
            ''', (session_id, file_path, department, duration,
                  datetime.now().isoformat(), datetime.now().isoformat()))

    def _log_to_jsonl(self, event: Dict[str, Any]):
        """Append event to daily JSONL log"""
        today = datetime.now().strftime('%Y-%m-%d')
        log_file = self.log_dir / f"{today}.jsonl"

        try:
            with open(log_file, 'a') as f:
                f.write(json.dumps(event) + '\n')
        except Exception as e:
            print(f"Error writing to JSONL: {e}", file=sys.stderr)

    def end_session(self, session_id: str, generate_summary: bool = False):
        """End active session and optionally generate summary"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()

        # Get session start time
        cursor.execute('SELECT start_time FROM sessions WHERE session_id = ?', (session_id,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            return

        start_time = datetime.fromisoformat(result[0])
        end_time = datetime.now()
        duration_seconds = int((end_time - start_time).total_seconds())

        # Get primary department
        cursor.execute('''
            SELECT department, COUNT(*) as count
            FROM activities
            WHERE session_id = ?
            GROUP BY department
            ORDER BY count DESC
            LIMIT 1
        ''', (session_id,))
        dept_result = cursor.fetchone()
        primary_dept = dept_result[0] if dept_result else 'General'

        # Get unique files touched
        cursor.execute('''
            SELECT COUNT(DISTINCT target_file)
            FROM activities
            WHERE session_id = ? AND target_file IS NOT NULL
        ''', (session_id,))
        files_count = cursor.fetchone()[0]

        # Update session
        cursor.execute('''
            UPDATE sessions
            SET end_time = ?,
                total_duration_seconds = ?,
                primary_department = ?,
                files_touched = ?,
                status = 'completed'
            WHERE session_id = ?
        ''', (end_time.isoformat(), duration_seconds, primary_dept, files_count, session_id))

        conn.commit()
        conn.close()

        # Generate summary if requested
        if generate_summary:
            self._trigger_daily_summary()

    def _trigger_daily_summary(self):
        """Trigger daily summary generation"""
        summary_script = SCRIPT_DIR / "generate-daily-summary.py"
        if summary_script.exists():
            import subprocess
            try:
                subprocess.run([sys.executable, str(summary_script)], check=False)
            except Exception as e:
                print(f"Error generating summary: {e}", file=sys.stderr)


def main():
    """Main entry point for command line usage"""
    parser = argparse.ArgumentParser(description='Track Claude Code activity')
    parser.add_argument('--event', required=True,
                       choices=['tool_start', 'tool_complete', 'session_end'],
                       help='Event type')
    parser.add_argument('--tool', help='Tool name (Read, Edit, Write, etc.)')
    parser.add_argument('--file', help='File path')
    parser.add_argument('--session-id', help='Session ID')
    parser.add_argument('--duration', type=int, help='Duration in milliseconds')
    parser.add_argument('--generate-summary', action='store_true', help='Generate daily summary')

    args = parser.parse_args()

    tracker = ActivityTracker()

    if args.event == 'tool_start':
        session_id = tracker.get_or_create_session(args.session_id)
        if args.tool:
            tracker.log_activity(session_id, args.tool, args.file)
        print(session_id)  # Output session ID for hook to capture

    elif args.event == 'tool_complete':
        if args.session_id and args.tool:
            tracker.log_activity(args.session_id, args.tool, args.file, args.duration)

    elif args.event == 'session_end':
        if args.session_id:
            tracker.end_session(args.session_id, args.generate_summary)


if __name__ == '__main__':
    main()
