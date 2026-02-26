# Time Tracking System - Setup & Usage Guide

*Professional session tracking for manager reporting*

## Overview

The YNA_Agentic time tracking system automatically monitors your Claude Code sessions and generates professional daily/weekly reports suitable for management review. It tracks what files you work on, how much time you spend, and provides AI-powered summaries of your accomplishments.

---

## Phase 1: Core Tracking (✅ COMPLETED)

The following components have been implemented and tested:

### Implemented Files

1. **`scripts/track-activity.py`** - Core tracking engine
   - Logs session starts/ends
   - Records file interactions
   - Stores data in SQLite database
   - Creates JSONL backup logs

2. **`scripts/generate-daily-summary.py`** - Report generator
   - Queries session data
   - Generates AI-powered summaries (or template fallback)
   - Creates professional markdown reports
   - Saves to database for Notion sync

3. **`config/activity-tracking-config.json`** - Configuration
   - Department detection rules
   - Privacy settings (what to track/exclude)
   - Storage settings
   - AI summary preferences

4. **`.tmp/activity-tracking.db`** - SQLite database
   - Sessions, activities, file focus, daily summaries
   - Automatically initialized on first run

5. **`.gitignore` updates** - Security
   - Excludes tracking database from git
   - Excludes JSONL logs from git

---

## Quick Start

### Step 1: Install Dependencies

```bash
cd /Users/jahongirmirzoev/Desktop/YNA_Agentic
pip install -r scripts/requirements.txt
```

**Note**: The `anthropic` package was added for AI-powered summaries. If you don't want to use AI summaries, the system will fall back to template-based summaries automatically.

### Step 2: Configure Environment Variables (Optional)

For AI-powered summaries, add to your `.env` file:

```bash
# Claude API for AI-powered summaries
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx
```

If you don't have an API key, the system will use template-based summaries instead (still professional and useful).

### Step 3: Test Manual Tracking

You can manually test the tracking system:

```bash
# Start a session and log activity
SESSION_ID=$(python3 scripts/track-activity.py --event tool_start --tool Read --file "CLAUDE.md")
echo "Session ID: $SESSION_ID"

# Log more activities
python3 scripts/track-activity.py --event tool_start --tool Edit --file "config/activity-tracking-config.json" --session-id "$SESSION_ID"

# End the session
python3 scripts/track-activity.py --event session_end --session-id "$SESSION_ID"

# Generate daily summary
python3 scripts/generate-daily-summary.py
```

### Step 4: View Reports

Daily reports are saved to:
```
execution/analytics/time-tracking/daily/YYYY-MM-DD_work_summary.md
```

Open the report in your editor or browser to review.

---

## Automated Tracking with VSCode Hooks

To enable **automatic tracking** every time you use Claude Code, you need to configure VSCode extension hooks.

### Option A: User-Level Configuration

Edit your global Claude Code settings:
```
~/.claude/settings.json
```

Add this hooks configuration:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "name": "Track Activity Start",
        "pattern": ".*",
        "command": "cd /Users/jahongirmirzoev/Desktop/YNA_Agentic && python3 scripts/track-activity.py --event tool_start --tool ${toolName} --file '${filePath}'"
      }
    ],
    "PostToolUse": [
      {
        "name": "Track Activity Complete",
        "pattern": ".*",
        "command": "cd /Users/jahongirmirzoev/Desktop/YNA_Agentic && python3 scripts/track-activity.py --event tool_complete --tool ${toolName} --duration ${durationMs}"
      }
    ],
    "SessionEnd": [
      {
        "name": "Generate Session Summary",
        "command": "cd /Users/jahongirmirzoev/Desktop/YNA_Agentic && python3 scripts/track-activity.py --event session_end --generate-summary"
      }
    ]
  }
}
```

### Option B: Project-Level Configuration

Create a `.vscode/settings.json` file in your YNA_Agentic project:

```json
{
  "claude.hooks": {
    "PreToolUse": [
      {
        "name": "Track Activity Start",
        "pattern": ".*",
        "command": "python3 scripts/track-activity.py --event tool_start --tool ${toolName} --file '${filePath}'"
      }
    ],
    "PostToolUse": [
      {
        "name": "Track Activity Complete",
        "pattern": ".*",
        "command": "python3 scripts/track-activity.py --event tool_complete --tool ${toolName} --duration ${durationMs}"
      }
    ],
    "SessionEnd": [
      {
        "name": "Generate Session Summary",
        "command": "python3 scripts/track-activity.py --event session_end --generate-summary"
      }
    ]
  }
}
```

**Note**: Check Claude Code's documentation for the exact hook syntax, as it may vary by version.

---

## Daily Workflow

### Automatic (Recommended)

Once hooks are configured:

1. **Work normally in Claude Code** - tracking happens automatically
2. **End your session** - summary is auto-generated
3. **Review report** - Open `execution/analytics/time-tracking/daily/[date]_work_summary.md`
4. **Share with manager** - Send the markdown file or Notion link (Phase 3)

### Manual

If you prefer manual control:

```bash
# At end of day, generate summary
python3 scripts/generate-daily-summary.py

# For yesterday's summary
python3 scripts/generate-daily-summary.py --yesterday

# For specific date
python3 scripts/generate-daily-summary.py --date 2026-02-25
```

---

## Database Queries (Advanced)

You can query the SQLite database directly for custom reports:

```bash
# View all sessions today
sqlite3 .tmp/activity-tracking.db "
  SELECT session_id, start_time, total_duration_seconds/3600.0 as hours, primary_department
  FROM sessions
  WHERE date(start_time) = date('now');
"

# View department breakdown
sqlite3 .tmp/activity-tracking.db "
  SELECT department, SUM(duration_seconds)/3600.0 as hours
  FROM activities
  WHERE date(timestamp) = date('now')
  GROUP BY department
  ORDER BY hours DESC;
"

# Top files worked on today
sqlite3 .tmp/activity-tracking.db "
  SELECT file_path, total_duration_seconds/60.0 as minutes, interaction_count
  FROM file_focus ff
  JOIN sessions s ON ff.session_id = s.session_id
  WHERE date(s.start_time) = date('now')
  ORDER BY total_duration_seconds DESC
  LIMIT 10;
"
```

---

## Configuration Options

Edit `config/activity-tracking-config.json` to customize:

### Tracking Settings

```json
{
  "tracking": {
    "enabled": true,                    // Turn tracking on/off
    "idle_threshold_seconds": 300,       // 5 min idle = break
    "session_timeout_seconds": 1800,     // 30 min = end session
    "exclude_patterns": [               // Files to never track
      "*.env*",
      "*credentials*",
      "*secrets*"
    ]
  }
}
```

### Department Detection

Add or modify department rules:

```json
{
  "department_detection": {
    "rules": [
      {
        "pattern": "business-knowledge/departments/marketing/*",
        "department": "Marketing"
      },
      {
        "pattern": "your-custom-path/*",
        "department": "Your Custom Department"
      }
    ],
    "default_department": "General"
  }
}
```

### AI Summary Settings

```json
{
  "summaries": {
    "daily_enabled": true,
    "weekly_enabled": true,
    "ai_powered": true,                           // Use AI summaries
    "ai_model": "claude-sonnet-4-5-20250929",    // Model to use
    "fallback_to_template": true                  // Fallback if AI fails
  }
}
```

---

## Privacy & Security

### What is Tracked

✅ Session start/end times
✅ File paths (relative to project)
✅ Tool usage (Read, Edit, Write, etc.)
✅ Time spent per file
✅ Department categorization
✅ Git branch name

### What is NOT Tracked

❌ File contents or code
❌ User messages or prompts
❌ API keys or credentials
❌ .env file interactions
❌ Files matching exclude patterns

### Security Measures

- Database and logs are gitignored (never committed)
- Sensitive file patterns are excluded by default
- Only relative paths stored (no home directory paths)
- Notion sync uses HTTPS encryption
- Can be disabled anytime with `DISABLE_ACTIVITY_TRACKING=1` in `.env`

---

## Troubleshooting

### Problem: No data being tracked

**Solution**: Check if tracking is enabled
```bash
cat config/activity-tracking-config.json | grep '"enabled"'
```

### Problem: Database locked error

**Solution**: Close any open database connections
```bash
# Kill any processes accessing the database
lsof .tmp/activity-tracking.db
```

### Problem: AI summary fails

**Solution**: Check API key and install anthropic package
```bash
# Check if API key is set
grep ANTHROPIC_API_KEY .env

# Install package
pip install anthropic==0.42.0
```

### Problem: Reports show 0 hours

**Solution**: Ensure session was ended properly
```bash
# Check session status
sqlite3 .tmp/activity-tracking.db "SELECT * FROM sessions WHERE status='active';"

# Manually end active sessions
sqlite3 .tmp/activity-tracking.db "UPDATE sessions SET status='completed', end_time=datetime('now') WHERE status='active';"
```

---

## Next Steps

### Phase 2: Weekly Summaries (Upcoming)

- [ ] Create `scripts/generate-weekly-summary.sh`
- [ ] Schedule weekly summary generation (Sunday 11:59 PM)
- [ ] Add trend analysis and comparisons

### Phase 3: Notion Integration (Upcoming)

- [ ] Set up Notion integration
- [ ] Create "Work Sessions Tracker" database
- [ ] Configure bidirectional sync
- [ ] Enable manager access via Notion

### Phase 4: Advanced Features (Future)

- [ ] Monthly summaries
- [ ] Productivity score algorithm
- [ ] Dashboard creation
- [ ] Alerting for unproductive patterns

---

## Example Output

Here's what a daily summary looks like:

```markdown
# Work Summary - February 26, 2026

**Total Time**: 7.5 hours
**Sessions**: 3
**Primary Focus**: Marketing Department

## Summary of Work

Today's work focused primarily on the marketing department's campaign automation
infrastructure. Key accomplishments include completing Make.com scenario
documentation, updating marketing memory with current campaign status, and
configuring Clay table integrations for lead enrichment.

## Time Allocation by Department

| Department | Time Spent | Percentage |
|------------|------------|------------|
| Marketing | 5.5 hrs | 73% |
| API Integrations | 1.5 hrs | 20% |
| Documentation | 0.5 hrs | 7% |

## Key Files Worked On

1. `business-knowledge/departments/marketing/memory.md` - 45 min
2. `business-knowledge/api-integrations/makecom/scenarios/lead-nurture-flow.md` - 90 min
3. `business-knowledge/api-integrations/clay/tables/lead-enrichment.md` - 120 min
...
```

---

## Support

For issues or questions:
1. Check this documentation first
2. Review `docs/troubleshooting.md`
3. Check database with SQL queries above
4. Verify configuration in `config/activity-tracking-config.json`

---

*Last updated: 2026-02-26*
*System status: Phase 1 Complete ✅*
