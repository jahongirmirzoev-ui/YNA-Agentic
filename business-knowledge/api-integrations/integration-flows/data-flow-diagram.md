# Data Flow Diagrams

*Last Updated: 2026-02-26*

## Primary Data Flow Architecture

```
                               YNA Agentic Data Flow
┌─────────────────────────────────────────────────────────────────────────┐
│                           DATA SOURCES                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Website  │  │  Manual  │  │  Import  │  │   APIs   │              │
│  │  Forms   │  │  Entry   │  │  Files   │  │          │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │             │              │             │                      │
│       └─────────────┴──────────────┴─────────────┘                      │
│                          │                                              │
│                          ▼                                              │
│               ┌────────────────────┐                                    │
│               │   CLAY (Enrichment │                                    │
│               │    Data Quality)   │                                    │
│               └─────────┬──────────┘                                    │
│                         │                                               │
│                         ▼                                               │
│               ┌────────────────────┐                                    │
│               │  AIRTABLE (Central │                                    │
│               │   Database / CRM)  │                                    │
│               └─────────┬──────────┘                                    │
│                         │                                               │
│                         ▼                                               │
│               ┌────────────────────┐                                    │
│               │  MAKE.COM (Workflow│                                    │
│               │    Orchestration)  │                                    │
│               └─────────┬──────────┘                                    │
│                         │                                               │
│          ┌──────────────┼──────────────┬─────────────┐                 │
│          ▼              ▼              ▼             ▼                 │
│     ┌────────┐    ┌────────┐    ┌─────────┐   ┌─────────┐            │
│     │ Email  │    │ Slack  │    │ Notion  │   │ Reports │            │
│     │ Sends  │    │ Alerts │    │  Sync   │   │ & Logs  │            │
│     └────────┘    └────────┘    └─────────┘   └─────────┘            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Flow 1: Lead Capture & Enrichment

**Trigger**: New form submission on website

```
Step 1: User submits form
    ↓
Step 2: Form webhook → Clay table
    ↓
Step 3: Clay enriches data
   - Clearbit: Company info
   - Hunter: Email validation
   - LinkedIn: Professional profile
    ↓
Step 4: Enriched data → Airtable (Leads table)
    ↓
Step 5: Airtable webhook → Make.com scenario
    ↓
Step 6: Make.com evaluates lead score
    ├─ If qualified → Sales team Slack notification
    │                 + Sales email sequence
    └─ If not qualified → Marketing nurture sequence
```

**Timing**: ~30-60 seconds end-to-end
**Error Handling**: Retry 3x with exponential backoff, log failures in Airtable

---

## Flow 2: Sales Deal Pipeline Updates

**Trigger**: Deal stage changed in Airtable

```
Step 1: Sales rep updates deal stage in Airtable
    ↓
Step 2: Airtable webhook → Make.com
    ↓
Step 3: Make.com checks new stage
    ├─ If "Proposal Sent" → Schedule follow-up task
    ├─ If "Negotiation" → Notify sales manager (Slack)
    ├─ If "Closed Won" → Trigger customer onboarding workflow
    │                     + Send to Customer Service
    │                     + Update revenue dashboard
    └─ If "Closed Lost" → Log loss reason
                          + Update pipeline report
```

**Timing**: Real-time (< 10 seconds)

---

## Flow 3: Customer Support Ticket Routing

**Trigger**: New support ticket received

```
Step 1: Email received → Make.com email watcher
    ↓
Step 2: Parse email content
    ↓
Step 3: Create record in Airtable (Support Tickets)
    ↓
Step 4: Airtable webhook → Make.com
    ↓
Step 5: Evaluate ticket severity/category
    ├─ If urgent → Slack alert to on-call support
    │             + Assign to Tier 2 immediately
    ├─ If technical → Route to technical support queue
    └─ If general → Assign to Tier 1 support queue
    ↓
Step 6: Send auto-response email to customer
```

**Timing**: < 2 minutes for first response

---

## Flow 4: Cloud Knowledge Sync (Notion ↔ Local)

**Trigger**: Scheduled (every 15 minutes) OR Notion webhook

```
Step 1: Cron trigger OR Notion page updated
    ↓
Step 2: Python sync script runs
    ↓
Step 3: Compare timestamps
   - Notion last_edited_time
   - Local file modification time
    ↓
Step 4: Determine sync direction
    ├─ If Notion newer → Update local file
    └─ If local newer → Update Notion page
    ↓
Step 5: Perform sync with conflict handling
    ↓
Step 6: Log sync operation
    ↓
Step 7: Commit changes (optional)
```

**Timing**: 15-minute intervals (or ~30 seconds via webhook)
**Conflict Resolution**: Last-write-wins with conflict markers

---

## Flow 5: Marketing Campaign Launch

**Trigger**: Campaign status set to "Launch" in Airtable

```
Step 1: Marketing team updates campaign status
    ↓
Step 2: Airtable webhook → Make.com
    ↓
Step 3: Make.com retrieves campaign details
    ↓
Step 4: Query Airtable for target audience
    ↓
Step 5: For each contact:
   - Generate personalized email
   - Schedule send (batch to avoid rate limits)
    ↓
Step 6: Track sends in Airtable (campaign tracking table)
    ↓
Step 7: Post campaign launch notification to Slack (#marketing)
```

**Timing**: Batch processing over several hours
**Rate Limit**: 500 emails/day, spread evenly

---

## Flow 6: Scheduled Daily Sales Report

**Trigger**: Schedule (daily at 8am)

```
Step 1: Make.com schedule trigger fires
    ↓
Step 2: Query Airtable for yesterday's activity
   - New leads
   - Deals created
   - Deals closed (won/lost)
   - Pipeline value change
    ↓
Step 3: Format data into HTML email
    ↓
Step 4: Send email to sales team
    ↓
Step 5: Log report generation in Airtable
```

**Timing**: Daily at 8:00 AM

---

## Flow 7: Website Analytics to Airtable

**Trigger**: Schedule (daily)

```
Step 1: Make.com schedule trigger
    ↓
Step 2: Fetch GA4 data via API
   - Page views
   - Conversions
   - Top pages
   - Traffic sources
    ↓
Step 3: Transform data
    ↓
Step 4: Update Airtable (Analytics table)
    ↓
Step 5: Calculate trends and alerts
    ├─ If traffic spike → Slack notification
    ├─ If conversion drop → Alert marketing team
    └─ If goal reached → Celebrate in #general
```

---

## Integration Dependencies

**Critical Path**:
```
Website → Clay → Airtable → Make.com → Slack/Email
```

If any component fails:
- **Clay down**: Data still captured in Airtable (unenriched)
- **Airtable down**: Queue data in Make.com, retry
- **Make.com down**: Webhooks queued, will retry when online
- **Slack down**: Fallback to email notifications

---

## Data Retention & Archiving

**Active Data**: Airtable (last 12 months)
**Archived Data**: Export to CSV/Database quarterly
**Logs**: 30 days retention
**Analytics**: 26 months (GA4 default)

---

## Performance Metrics

**Target Metrics**:
- Lead capture to enrichment: < 1 minute
- Enrichment to Airtable: < 30 seconds
- Airtable to notification: < 10 seconds
- Total lead-to-notification: < 2 minutes

---

*Update this diagram when data flows change. Keep it synchronized with actual implementation.*
