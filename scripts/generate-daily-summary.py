#!/usr/bin/env python3
"""
Daily Summary Generator for Claude Code Sessions
Generates AI-powered professional reports for manager review
"""

import sqlite3
import json
import os
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict
import argparse

# Add project root to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / '.env')
except ImportError:
    pass


class DailySummaryGenerator:
    """Generates daily summary reports from activity tracking data"""

    def __init__(self, target_date: Optional[date] = None):
        """Initialize the summary generator"""
        self.target_date = target_date or date.today()
        self.config = self._load_config()
        self.db_path = PROJECT_ROOT / self.config['storage']['database_path']
        self.report_dir = PROJECT_ROOT / "execution" / "analytics" / "time-tracking" / "daily"
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration"""
        config_file = PROJECT_ROOT / "config" / "activity-tracking-config.json"
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}", file=sys.stderr)
            return {}

    def query_session_data(self) -> Dict[str, Any]:
        """Query all data for the target date"""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        date_str = self.target_date.isoformat()

        # Get all sessions for the date
        cursor.execute('''
            SELECT * FROM sessions
            WHERE date(start_time) = ?
            ORDER BY start_time
        ''', (date_str,))
        sessions = [dict(row) for row in cursor.fetchall()]

        # Get all activities for the date
        cursor.execute('''
            SELECT * FROM activities
            WHERE date(timestamp) = ?
            ORDER BY timestamp
        ''', (date_str,))
        activities = [dict(row) for row in cursor.fetchall()]

        # Get file focus data
        cursor.execute('''
            SELECT ff.* FROM file_focus ff
            JOIN sessions s ON ff.session_id = s.session_id
            WHERE date(s.start_time) = ?
            ORDER BY ff.total_duration_seconds DESC
        ''', (date_str,))
        file_focus = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return {
            'sessions': sessions,
            'activities': activities,
            'file_focus': file_focus
        }

    def categorize_by_department(self, activities: List[Dict]) -> Dict[str, float]:
        """Categorize time by department"""
        dept_time = defaultdict(float)

        for activity in activities:
            dept = activity.get('department', 'General')
            duration = activity.get('duration_seconds', 0)
            dept_time[dept] += duration

        return dict(dept_time)

    def format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format"""
        hours = seconds / 3600
        if hours < 1:
            minutes = seconds / 60
            return f"{int(minutes)} min"
        return f"{hours:.1f} hrs"

    def generate_ai_summary(self, data: Dict[str, Any]) -> str:
        """Generate AI-powered summary using Claude API"""
        if not self.config.get('summaries', {}).get('ai_powered', False):
            return self.generate_template_summary(data)

        try:
            # Import Anthropic SDK
            import anthropic

            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                print("Warning: ANTHROPIC_API_KEY not set, using template summary", file=sys.stderr)
                return self.generate_template_summary(data)

            # Prepare context
            sessions = data['sessions']
            activities = data['activities']
            dept_breakdown = self.categorize_by_department(activities)

            total_duration = sum(s.get('total_duration_seconds', 0) for s in sessions)
            total_hours = total_duration / 3600

            # Get top files
            top_files = data['file_focus'][:5]

            # Build prompt
            prompt = f"""You are generating a professional work summary for a manager's review.

Data for {self.target_date.strftime('%B %d, %Y')}:
- Total time worked: {total_hours:.1f} hours
- Number of sessions: {len(sessions)}
- Files worked on: {len(data['file_focus'])} unique files

Department breakdown:
{json.dumps(dept_breakdown, indent=2)}

Top 5 files by time spent:
{json.dumps([{'file': f['file_path'], 'time_seconds': f['total_duration_seconds']} for f in top_files], indent=2)}

Please write a concise 2-3 paragraph summary suitable for a manager that includes:
1. Overview paragraph: What was accomplished today in professional language
2. Focus areas paragraph: Which departments/projects received attention and why
3. Key outcomes: Specific deliverables or progress made

Write in past tense, professional tone. Focus on business value and outcomes, not technical minutiae.
Do not include pleasantries or meta-commentary. Just the summary paragraphs."""

            # Call Claude API
            client = anthropic.Anthropic(api_key=api_key)
            model = self.config.get('summaries', {}).get('ai_model', 'claude-sonnet-4-5-20250929')

            message = client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return message.content[0].text

        except Exception as e:
            print(f"Error generating AI summary: {e}", file=sys.stderr)
            if self.config.get('summaries', {}).get('fallback_to_template', True):
                return self.generate_template_summary(data)
            raise

    def generate_template_summary(self, data: Dict[str, Any]) -> str:
        """Generate template-based summary (fallback when AI unavailable)"""
        sessions = data['sessions']
        activities = data['activities']
        dept_breakdown = self.categorize_by_department(activities)

        primary_dept = max(dept_breakdown.items(), key=lambda x: x[1])[0] if dept_breakdown else 'General'

        total_duration = sum(s.get('total_duration_seconds', 0) for s in sessions)
        total_hours = total_duration / 3600

        summary = f"""Today's work focused primarily on {primary_dept} activities. """
        summary += f"Across {len(sessions)} work session{'s' if len(sessions) != 1 else ''}, "
        summary += f"a total of {total_hours:.1f} hours were logged. "

        if len(data['file_focus']) > 0:
            summary += f"Work involved {len(data['file_focus'])} different files across multiple departments. "

        top_dept = sorted(dept_breakdown.items(), key=lambda x: x[1], reverse=True)[:3]
        if len(top_dept) > 1:
            summary += f"Time was distributed across {', '.join([d[0] for d in top_dept])} departments. "

        summary += "Progress was made on documentation, configuration, and implementation tasks."

        return summary

    def create_markdown_report(self, data: Dict[str, Any], ai_summary: str) -> str:
        """Create formatted markdown report"""
        sessions = data['sessions']
        activities = data['activities']
        file_focus = data['file_focus']

        total_duration = sum(s.get('total_duration_seconds', 0) for s in sessions)
        total_hours = total_duration / 3600

        dept_breakdown = self.categorize_by_department(activities)
        primary_dept = max(dept_breakdown.items(), key=lambda x: x[1])[0] if dept_breakdown else 'General'

        # Calculate percentages
        dept_percentages = {}
        for dept, seconds in dept_breakdown.items():
            pct = (seconds / total_duration * 100) if total_duration > 0 else 0
            dept_percentages[dept] = pct

        # Build markdown
        md = f"# Work Summary - {self.target_date.strftime('%B %d, %Y')}\n\n"
        md += f"**Total Time**: {total_hours:.1f} hours\n"
        md += f"**Sessions**: {len(sessions)}\n"
        md += f"**Primary Focus**: {primary_dept}\n\n"

        md += "## Summary of Work\n\n"
        md += ai_summary + "\n\n"

        # Department breakdown table
        if dept_breakdown:
            md += "## Time Allocation by Department\n\n"
            md += "| Department | Time Spent | Percentage |\n"
            md += "|------------|------------|------------|\n"

            sorted_depts = sorted(dept_breakdown.items(), key=lambda x: x[1], reverse=True)
            for dept, seconds in sorted_depts:
                md += f"| {dept} | {self.format_duration(seconds)} | {dept_percentages[dept]:.0f}% |\n"
            md += "\n"

        # Top files
        if file_focus:
            md += "## Key Files Worked On\n\n"
            for i, file_data in enumerate(file_focus[:10], 1):
                file_path = file_data['file_path']
                duration = file_data['total_duration_seconds']
                interactions = file_data['interaction_count']
                md += f"{i}. `{file_path}` - {self.format_duration(duration)} ({interactions} interaction{'s' if interactions != 1 else ''})\n"
            md += "\n"

        # Session details
        if sessions:
            md += "## Session Details\n\n"
            for i, session in enumerate(sessions, 1):
                start = datetime.fromisoformat(session['start_time'])
                end_time = session.get('end_time')
                end = datetime.fromisoformat(end_time) if end_time else datetime.now()
                duration = session.get('total_duration_seconds', 0)

                md += f"### Session {i}: {start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}"
                md += f" ({self.format_duration(duration)})\n"

                if session.get('primary_department'):
                    md += f"- Focus: {session['primary_department']}\n"

                files_touched = session.get('files_touched', 0)
                md += f"- Files: {files_touched} file{'s' if files_touched != 1 else ''} edited\n"

                if session.get('git_branch'):
                    md += f"- Branch: `{session['git_branch']}`\n"

                md += "\n"

        md += "---\n"
        md += "*Generated automatically by YNA_Agentic Time Tracking System*\n"

        return md

    def save_to_database(self, data: Dict[str, Any], ai_summary: str, report_path: str):
        """Save summary to daily_summaries table"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()

        sessions = data['sessions']
        total_duration = sum(s.get('total_duration_seconds', 0) for s in sessions)
        total_hours = total_duration / 3600

        dept_breakdown = self.categorize_by_department(data['activities'])
        primary_dept = max(dept_breakdown.items(), key=lambda x: x[1])[0] if dept_breakdown else 'General'

        top_files = json.dumps([f['file_path'] for f in data['file_focus'][:5]])

        cursor.execute('''
            INSERT OR REPLACE INTO daily_summaries
            (date, total_sessions, total_duration_hours, primary_department, ai_summary, top_files, report_path)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.target_date.isoformat(), len(sessions), total_hours, primary_dept,
              ai_summary, top_files, report_path))

        conn.commit()
        conn.close()

    def generate(self) -> Optional[str]:
        """Generate daily summary report"""
        # Query data
        data = self.query_session_data()

        if not data['sessions']:
            print(f"No sessions found for {self.target_date}", file=sys.stderr)
            return None

        # Generate AI summary
        print(f"Generating summary for {self.target_date}...")
        ai_summary = self.generate_ai_summary(data)

        # Create markdown report
        markdown = self.create_markdown_report(data, ai_summary)

        # Save to file
        report_filename = f"{self.target_date.isoformat()}_work_summary.md"
        report_path = self.report_dir / report_filename

        with open(report_path, 'w') as f:
            f.write(markdown)

        # Save to database
        self.save_to_database(data, ai_summary, str(report_path))

        print(f"✓ Report generated: {report_path}")
        return str(report_path)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Generate daily activity summary')
    parser.add_argument('--date', help='Date to generate summary for (YYYY-MM-DD), defaults to today')
    parser.add_argument('--yesterday', action='store_true', help='Generate summary for yesterday')

    args = parser.parse_args()

    if args.yesterday:
        target_date = date.today() - timedelta(days=1)
    elif args.date:
        target_date = date.fromisoformat(args.date)
    else:
        target_date = date.today()

    generator = DailySummaryGenerator(target_date)
    report_path = generator.generate()

    if report_path:
        print(f"\nDaily summary report available at:")
        print(f"  {report_path}")
    else:
        print("No data to summarize.")
        sys.exit(1)


if __name__ == '__main__':
    main()
