---
name: dashboard
description: Generate professional McKinsey-level dashboard with activity analytics and AI insights
invocable: user
type: exec
---

# Dashboard Generation Skill

Generates a professional HTML dashboard with interactive charts and AI-powered insights from your activity tracking data.

## Overview

This skill creates executive-ready dashboards featuring:
- **Interactive Plotly charts** (time series, pie charts, bar charts, heatmaps)
- **AI-powered insights** using Claude API (trends, anomalies, recommendations)
- **McKinsey-level styling** (professional design, responsive layout)
- **Multiple data sources** (SQLite activity tracking + optional API integrations)

### ⏱️ Time Savings
**Saves 2-4 hours per week** per stakeholder reviewing the dashboard.

**Why it saves time:**
- **Manual reporting eliminated**: No need to manually gather data from multiple sources, create spreadsheets, or design presentations
- **Instant insights**: AI analyzes patterns and generates recommendations automatically instead of manual analysis
- **Self-service access**: Stakeholders can generate their own department-specific dashboards on-demand without waiting for reports
- **Visual clarity**: Interactive charts communicate trends faster than tables or text (studies show 60% faster comprehension)

### 💰 Money Savings
**Saves $500-2,000/month** depending on organization size.

**Why it saves money:**
- **Labor cost reduction**: If manager ($100/hr) spends 4 hours/week on manual reporting, that's $1,600/month saved
- **No BI tool subscription**: Eliminates need for Tableau ($70/user/month), Power BI ($10-20/user/month), or Looker ($hundreds/month)
- **Faster decision-making**: Data-driven decisions made 3-5 days faster, reducing opportunity costs and improving ROI
- **Identifies waste**: Highlights low-value activities, allowing reallocation of resources to high-impact work

## Usage

```
/dashboard
/dashboard --range 30d
/dashboard --range 7d --department Marketing
/dashboard --type summary
/dashboard --range custom --start 2026-02-01 --end 2026-02-26
```

## Parameters

### `--range` (Time Range)
Specifies the time period for the dashboard. Default: `7d`

**Options:**
- `7d`, `30d`, `90d`: Last N days
- `today`: Today only
- `custom`: Custom date range (requires `--start` and `--end`)

**Examples:**
```
/dashboard --range 7d        # Last 7 days
/dashboard --range 30d       # Last 30 days
/dashboard --range today     # Today only
/dashboard --range custom --start 2026-02-01 --end 2026-02-26
```

### `--start` (Start Date)
Start date for custom range in YYYY-MM-DD format. Only used with `--range custom`.

**Example:**
```
/dashboard --range custom --start 2026-02-01 --end 2026-02-26
```

### `--end` (End Date)
End date for custom range in YYYY-MM-DD format. Only used with `--range custom`.

### `--department` (Department Filter)
Filter dashboard to show only a specific department's activity.

**Available Departments:**
- Marketing
- Sales
- Customer Service
- CRM
- Website
- API Integrations
- Automation
- Configuration
- Documentation
- Execution
- Cloud Sync
- General

**Examples:**
```
/dashboard --range 30d --department Marketing
/dashboard --range 7d --department Sales
```

### `--type` (Dashboard Type)
Type of dashboard to generate. Default: `full`

**Options:**
- `summary`: Lightweight overview with key metrics and charts
- `full`: Complete dashboard with all sections (activity, insights, optional CRM/integrations)
- `integrations`: API integration health dashboard only

**Examples:**
```
/dashboard --type summary        # Quick overview
/dashboard --type full           # Complete analysis
/dashboard --type integrations   # API health check
```

### `--output` (Output Path)
Custom output file path. Optional - if not specified, uses automatic naming in `execution/analytics/dashboards/`.

**Example:**
```
/dashboard --range 7d --output /custom/path/my-dashboard.html
```

## Dashboard Sections

### 1. Executive Summary
- **4 KPI Cards**: Total Time, Work Sessions, Files Touched, Primary Focus
- **AI-Generated Summary**: 2-3 paragraph professional narrative
- **Period Comparison**: Shows % change vs previous period

### 2. Activity Analytics
- **Daily Timeline**: Line chart showing hours per day (multi-department)
- **Department Breakdown**: Interactive donut chart with percentages
- **Top 10 Files**: Horizontal bar chart sorted by time spent
- **Activity Heatmap**: Files × Days heat visualization (full dashboard only)
- **Hourly Distribution**: Activity by hour of day

### 3. AI Insights & Recommendations
- **Key Trends**: 3-5 notable patterns identified by AI
- **Anomalies**: Unusual spikes, gaps, or patterns
- **Recommendations**: 3 actionable suggestions for optimization

### 4. CRM Performance (if Airtable enabled)
- Lead pipeline funnel
- Deal value over time
- Lead source distribution

### 5. Integration Health (if enabled)
- Make.com scenario status
- Clay credit usage
- API response times

## Output

Dashboard is saved to: `execution/analytics/dashboards/[DATE]_[TYPE]_dashboard.html`

**File Naming:**
- `2026-02-26_full_dashboard.html` - Full dashboard
- `2026-02-26_summary_dashboard.html` - Summary dashboard
- `2026-02-26_full_dashboard_marketing.html` - Department-filtered

**How to View:**
Open the HTML file in any modern web browser. The dashboard is fully self-contained (no internet connection required after generation).

## Common Use Cases

### Weekly Manager Report
Every Monday, generate last week's dashboard for manager review:
```
/dashboard --range 7d --type full
```

### Monthly Department Review
End-of-month analysis of Marketing activity:
```
/dashboard --range 30d --department Marketing
```

### Quarterly Executive Presentation
Q1 review for leadership with ROI metrics:
```
/dashboard --range custom --start 2026-01-01 --end 2026-03-31
```

### API Integration Health Check
Monthly review of Make.com, Clay, Airtable health:
```
/dashboard --range 30d --type integrations
```

### Daily Quick Check
Evening review of today's work:
```
/dashboard --range today --type summary
```

## Requirements

- **Activity Tracking**: SQLite database must exist at `.tmp/activity-tracking.db`
- **Python Dependencies**: plotly, jinja2, pandas, numpy (installed via requirements.txt)
- **Claude API Key** (optional): Set `ANTHROPIC_API_KEY` in `.env` for AI insights
  - If not set, uses template-based insights

## Configuration

Dashboard settings are in `config/dashboard-config.json`:

- **AI Insights**: Enable/disable AI analysis
- **Data Sources**: Toggle Airtable, Make.com, Clay integrations
- **Chart Settings**: Colors, height, interactivity
- **Output**: Directory, filename format, retention

## Troubleshooting

**No data available:**
- Check that activity tracking is enabled and running
- Verify SQLite database exists: `.tmp/activity-tracking.db`
- Try a broader date range

**AI insights not generated:**
- Check `ANTHROPIC_API_KEY` is set in `.env`
- Dashboard will use template insights as fallback

**Charts not showing:**
- Open browser console for errors
- Ensure modern browser (Chrome, Safari, Firefox)
- Check Plotly.js loaded correctly

**Slow generation:**
- Use `--type summary` for faster generation
- Disable optional integrations in config
- Reduce date range

## Implementation

Execute the Python dashboard generation script and present key highlights to the user.

```bash
python3 scripts/generate-dashboard.py {{args}}
```

After generation completes, read the output file path from the script output and provide the user with:
- Time range covered
- Total hours logged
- Primary department
- Key insight from AI summary (first trend)
- Full path to interactive HTML dashboard

## Examples with Expected Output

### Example 1: Quick Weekly Dashboard
**Command:**
```
/dashboard --range 7d
```

**Expected Response:**
```
Generating your dashboard for the last 7 days...

Dashboard Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Time Range: Feb 19-26, 2026
⏱️  Total Hours: 32.5 hrs
📁 Files Touched: 47 files
🎯 Primary Focus: Marketing (45%)

💡 Key Insight: Marketing activity increased 34% compared to previous period, with significant focus on campaign strategy documentation.

📄 Full Dashboard: execution/analytics/dashboards/2026-02-26_full_dashboard.html
```

### Example 2: Department-Specific Dashboard
**Command:**
```
/dashboard --range 30d --department Sales
```

**Expected Response:**
```
Generating Sales department dashboard for the last 30 days...

Dashboard Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Time Range: Jan 27 - Feb 26, 2026
🏢 Department: Sales
⏱️  Total Hours: 87.3 hrs
📁 Files Touched: 123 files

💡 Key Insight: Focus on playbook development and pipeline documentation shows 67% time allocation to strategic planning activities.

📄 Full Dashboard: execution/analytics/dashboards/2026-02-26_full_dashboard_sales.html
```

---

**Note:** This skill requires the activity tracking system to be operational. If no activity data is available, the dashboard will show an empty state with a helpful message.
