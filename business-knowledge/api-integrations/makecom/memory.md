# Make.com Integration - Memory & Context

*Last Updated: 2026-02-26*

## Overview

Make.com (formerly Integromat) serves as the central workflow automation platform, orchestrating data flows between Clay, Airtable, Email, Slack, and other systems.

---

## Current Status

- **Status**: ✅ Active
- **API Key**: Configured in `.env`
- **Active Scenarios**: TBD (to be documented)
- **Monthly Operations**: TBD / 100,000 limit

---

## Active Scenarios

**Action Required**: Document all existing scenarios from your Make.com account in [scenarios/scenario-index.md](scenarios/scenario-index.md)

### Scenario Categories
- **Lead Management**: Lead capture, enrichment, routing
- **Sales Automation**: Deal updates, notifications, reporting
- **Customer Service**: Ticket routing, escalations
- **Marketing**: Campaign triggers, email sends
- **Reporting**: Scheduled reports, dashboards

---

## Common Scenario Patterns

### Webhook Receiver
- **Trigger**: Webhook from external source
- **Actions**: Parse data → Transform → Send to destination

### Scheduled Task
- **Trigger**: Schedule (daily/weekly/hourly)
- **Actions**: Query data → Process → Send report

### Database Watcher
- **Trigger**: Airtable webhook (record created/updated)
- **Actions**: Evaluate conditions → Route → Notify

---

## Connections

See [connections.md](connections.md) for detailed connection inventory.

**Connected Services**:
- Airtable (PAT)
- Email/SMTP
- Slack (Webhook)
- Clay (API)
- Notion (API)

---

## Webhooks

See [webhooks.md](webhooks.md) for all webhook URLs.

**Important**: Webhook URLs are sensitive - store in `.env`, not in documentation.

---

## Rate Limits

- **Monthly Operations**: 100,000
- **Current Usage**: TBD
- **Alert Threshold**: 80,000 (80%)

---

## Best Practices

- Use error handlers on all scenarios
- Implement retry logic (3 attempts, exponential backoff)
- Log errors to designated Airtable table
- Test thoroughly in development before activating
- Document all scenarios in scenario-index.md

---

## Notes for Claude

- Always check scenario execution history for debugging
- Webhook URLs must be kept secure (in .env only)
- Monitor operations count to avoid hitting limits
- Document new scenarios immediately after creation

---

*For detailed scenario documentation, see [scenarios/scenario-index.md](scenarios/scenario-index.md)*
