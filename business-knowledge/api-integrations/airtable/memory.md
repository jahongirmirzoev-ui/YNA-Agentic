# Airtable Integration - Memory & Context

*Last Updated: 2026-02-26*

## Overview

Airtable serves as the central database for all business operations. All data (leads, customers, campaigns, tickets, etc.) flows through Airtable as the single source of truth.

---

## Current Status

- **Status**: ✅ Active
- **Personal Access Token (PAT)**: Configured in `.env`
- **Active Bases**: TBD (to be documented)
- **Rate Limit**: 5 requests/second
- **Current Usage**: TBD

---

## Active Bases

**Action Required**: Document all existing bases from your Airtable account in [bases/base-inventory.md](bases/base-inventory.md)

### Recommended Base Structure
- **CRM Main**: Contacts, Companies, Deals, Activities
- **Marketing Hub**: Campaigns, Leads, Content Calendar
- **Support**: Tickets, Customer Feedback
- **Operations**: Projects, Tasks, Resources

---

## Data Architecture

```
External Sources → Clay (Enrichment) → Airtable (Storage) → Make.com (Distribution)
```

**Airtable as Hub**:
- Receives enriched data from Clay
- Stores all business records
- Triggers Make.com via webhooks
- Provides reporting and views
- Enables team collaboration

---

## Webhooks

Airtable webhooks trigger Make.com scenarios when:
- New record created
- Record updated
- Field value changes
- Record matches filter

**Webhook Configuration**: See [automations.md](automations.md)

---

## Field Mapping

See [field-mapping.md](field-mapping.md) for complete cross-platform field mappings.

**Key Principles**:
- Consistent field names across bases
- Proper field types (Email, Phone, Date, etc.)
- Linked records for relationships
- Formulas for calculated fields
- Views for filtering and reporting

---

## Automations

**Native Airtable Automations**: See [automations.md](automations.md)

**Common Automations**:
- Send email when record matches condition
- Create linked record in another table
- Update field based on trigger
- Slack notification on important events

---

## Best Practices

- Use Personal Access Tokens (PAT) instead of deprecated API keys
- Implement proper field types for data validation
- Create views for different team needs
- Use color-coding for visual clarity
- Document all custom fields
- Keep base schemas updated

---

## Rate Limit Management

- **Limit**: 5 requests per second per base
- **Strategy**: Batch operations when possible
- **Monitoring**: Track API usage via Make.com execution logs
- **Fallback**: Implement exponential backoff

---

## Notes for Claude

- Airtable is the single source of truth - always check here first
- Use views to filter data, don't pull all records
- Document field mappings when adding integrations
- Monitor webhook configurations in automations.md

---

*For base documentation, see [bases/base-inventory.md](bases/base-inventory.md)*
