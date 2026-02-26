# API Integration Hub

*Last Updated: 2026-02-26*

## Overview

This directory contains all configuration, documentation, and memory for external API integrations. All integrations follow the primary data flow pattern: **Clay → Airtable → Make.com → External APIs**.

---

## Integration Architecture

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌─────────────┐
│   Clay   │────▶│ Airtable │────▶│ Make.com │────▶│  External   │
│  (Enrich)│     │ (Storage)│     │(Workflow)│     │APIs (Email, │
│          │     │          │     │          │     │Slack, etc.) │
└──────────┘     └──────────┘     └──────────┘     └─────────────┘
      ▲                                                     │
      │                                                     │
      └─────────────────────────────────────────────────────┘
                    (Notion for Knowledge Sync)
```

---

## Active Integrations

### Core Platforms

| Platform | Status | Purpose | API Docs | Rate Limit | Usage |
|----------|--------|---------|----------|------------|-------|
| **Make.com** | ✅ Active | Workflow automation | [Make.com Docs](https://www.make.com/en/api-documentation) | 100k ops/month | TBD |
| **Clay** | ✅ Active | Data enrichment | [Clay Docs](https://clay.com/docs) | 100 credits/month | TBD |
| **Airtable** | ✅ Active | Central database | [Airtable API](https://airtable.com/developers/web/api/introduction) | 5 req/sec | TBD |
| **Email (SMTP)** | 🟡 Setup | Communication | [SMTP Docs](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) | 500/day | 0 |
| **Slack** | 🟡 Setup | Team notifications | [Slack API](https://api.slack.com/) | Unlimited webhooks | 0 |
| **Google Analytics** | 🟡 Setup | Website analytics | [GA4 Docs](https://developers.google.com/analytics/devguides/collection/ga4) | 2M events/month | 0 |
| **Notion** | 🟡 Setup | Knowledge sync | [Notion API](https://developers.notion.com) | 3 req/sec | 0 |

**Status Legend**:
- ✅ Active: Fully configured and operational
- 🟡 Setup: In configuration phase
- 🔴 Issue: Experiencing problems
- ⏸️ Paused: Temporarily disabled

---

## Connection Registry

### Make.com Scenarios

**Existing Scenarios** (To be documented from your account):

| Scenario Name | ID | Trigger | Actions | Status | Owner | Last Updated |
|--------------|-----|---------|---------|--------|-------|--------------|
| *To be documented* | - | - | - | - | - | - |

**Action Required**: Log into Make.com and document all active scenarios in [makecom/scenarios/scenario-index.md](makecom/scenarios/scenario-index.md)

**Common Scenario Patterns**:
- Lead enrichment flow: Clay → Airtable → Email notification
- Sales alerts: Airtable webhook → Slack notification
- Weekly reports: Schedule trigger → Query Airtable → Send email
- Customer onboarding: Deal closed → Create tasks → Send welcome email

---

### Clay Tables

**Existing Tables** (To be documented from your account):

| Table Name | ID | Purpose | Enrichment Providers | Output Destination | Records |
|-----------|-----|---------|---------------------|-------------------|----------|
| *To be documented* | - | - | - | - | - |

**Action Required**: Log into Clay and document all tables in [clay/tables/table-schemas.md](clay/tables/table-schemas.md)

**Common Clay Use Cases**:
- Lead enrichment: Email → Company data, contact info, social profiles
- Company research: Domain → Company size, funding, tech stack
- Contact finding: Company → Find decision makers, emails
- Data validation: Email/phone verification

---

### Airtable Bases

**Existing Bases** (To be documented from your account):

| Base Name | ID | Tables | Purpose | Connected Integrations | Records |
|-----------|-----|--------|---------|----------------------|----------|
| *To be documented* | - | - | - | - | - |

**Action Required**: Log into Airtable and document all bases in [airtable/bases/base-inventory.md](airtable/bases/base-inventory.md)

**Recommended Base Structure**:
- **CRM Main**: Contacts, Companies, Deals, Activities
- **Marketing Hub**: Campaigns, Leads, Content Calendar
- **Support**: Tickets, Customer Feedback, Knowledge Base
- **Operations**: Projects, Tasks, Team Resources

---

## Rate Limits & Usage Monitoring

### Current Usage (Updated: 2026-02-26)

| Platform | Limit | Used This Month | Remaining | Buffer % | Alert Level |
|----------|-------|-----------------|-----------|----------|-------------|
| Make.com | 100k operations | TBD | TBD | TBD | 🟢 OK |
| Clay | 100 credits | TBD | TBD | TBD | 🟢 OK |
| Airtable | 5 req/sec | TBD | TBD | TBD | 🟢 OK |
| Notion | 3 req/sec | TBD | TBD | TBD | 🟢 OK |
| Email/SMTP | 500/day | TBD | TBD | TBD | 🟢 OK |

**Alert Levels**:
- 🟢 OK: <70% usage
- 🟡 Warning: 70-85% usage
- 🟠 Caution: 85-95% usage
- 🔴 Critical: >95% usage

**Rate Limit Strategy**:
- Monitor usage weekly
- Alert at 80% threshold
- Implement exponential backoff on all API calls
- Use batching where possible
- Consider upgrading plans at 90% sustained usage

---

## Data Flow Patterns

### Pattern 1: Lead Capture & Enrichment
```
Website Form → Webhook → Clay Table → Enrichment (Clearbit, Hunter) →
Airtable (Leads) → Make.com Webhook → Slack Notification + Email Nurture
```

**Timing**: Real-time (~30-60 seconds end-to-end)
**Error Handling**: Retry 3x with exponential backoff, alert on failure

### Pattern 2: Scheduled Batch Processing
```
Cron Trigger (Make.com) → Query Airtable (yesterday's leads) →
Format data → Send email report → Log completion
```

**Timing**: Scheduled (e.g., daily at 8am)
**Error Handling**: Log failures, retry next day

### Pattern 3: Bidirectional Sync
```
Airtable ↔ Make.com ↔ External System (e.g., External CRM)
```

**Timing**: Webhook-based (real-time)
**Conflict Resolution**: Last-write-wins, log conflicts

### Pattern 4: Knowledge Base Sync
```
Local Files ↔ Python Script ↔ Notion API ↔ Notion Workspace
```

**Timing**: Every 15 minutes via cron
**Conflict Resolution**: Last-write-wins with conflict markers

---

## Field Mapping Standards

See [integration-flows/field-mapping.md](integration-flows/field-mapping.md) for complete cross-platform field mappings.

**Standard Contact/Lead Object**:

| Field | Clay | Airtable | Notion | Email | Description |
|-------|------|----------|--------|-------|-------------|
| Email | `email` | Email (Email type) | Email (Email) | To | Primary email address |
| First Name | `first_name` | First Name (Text) | First Name (Title) | - | Contact first name |
| Last Name | `last_name` | Last Name (Text) | Last Name (Text) | - | Contact last name |
| Company | `company` | Company (Text) | Company (Relation) | - | Company name |
| Status | `status` | Status (Select) | Status (Select) | - | Lead/customer status |
| Created Date | `created_at` | Created (Date) | Created (Date) | - | Record creation timestamp |

**Consistency Rules**:
- Use same field names across platforms where possible
- Maintain data type compatibility
- Document all custom field mappings
- Version control mapping changes

---

## Security & Credentials

### Credential Storage
- **Development**: `.env` file (gitignored)
- **Production**: AWS Secrets Manager / Cloud KMS (future)
- **Access**: Principle of least privilege
- **Rotation**: Every 60-90 days

### Credential Registry
See [/config/credential-registry.md](../../config/credential-registry.md) for complete inventory:
- API keys and tokens
- Webhook URLs
- Database IDs
- Rotation schedules
- Owners

### API Key Scopes
- **Make.com**: Full access (scenarios, connections, organizations)
- **Clay**: Workspace access (tables, enrichment)
- **Airtable**: Base-specific PATs with minimal required scopes
- **Notion**: Database access only (not full workspace)
- **Slack**: Incoming webhooks only
- **Google Analytics**: Read access to properties

---

## Integration Workflows

### Adding New Integration

Follow [/directives/api-integration-sop.md](../../directives/api-integration-sop.md):

1. **Planning**: Purpose, API docs, rate limits, credentials needed
2. **Configuration**: Obtain credentials, add to `.env`, create folder structure
3. **Implementation**: Set up connection, create test workflow
4. **Documentation**: Update this README, create platform memory.md
5. **Testing**: Validate in development environment
6. **Deployment**: Deploy to production, set up monitoring

### Modifying Existing Integration

1. **Impact Assessment**: Review current usage, identify dependencies
2. **Testing**: Test changes in development environment
3. **Documentation**: Update relevant documentation
4. **Deployment**: Deploy during low-traffic period
5. **Monitoring**: Watch for errors/issues for 24-48 hours

---

## Platform-Specific Documentation

### Make.com
- **Memory**: [makecom/memory.md](makecom/memory.md)
- **Scenarios Index**: [makecom/scenarios/scenario-index.md](makecom/scenarios/scenario-index.md)
- **Connections**: [makecom/connections.md](makecom/connections.md)
- **Webhooks**: [makecom/webhooks.md](makecom/webhooks.md)

### Clay
- **Memory**: [clay/memory.md](clay/memory.md)
- **Tables**: [clay/tables/table-schemas.md](clay/tables/table-schemas.md)
- **Enrichment Providers**: [clay/enrichment-providers.md](clay/enrichment-providers.md)

### Airtable
- **Memory**: [airtable/memory.md](airtable/memory.md)
- **Base Inventory**: [airtable/bases/base-inventory.md](airtable/bases/base-inventory.md)
- **Field Mapping**: [airtable/field-mapping.md](airtable/field-mapping.md)
- **Automations**: [airtable/automations.md](airtable/automations.md)

### Email/SMTP
- **Memory**: [email/memory.md](email/memory.md)
- **SMTP Config**: [email/smtp-config.md](email/smtp-config.md)
- **Templates**: [email/email-templates/](email/email-templates/)

### Slack
- **Memory**: [slack/memory.md](slack/memory.md)
- **Webhook Config**: [slack/webhook-config.md](slack/webhook-config.md)

### Google Analytics
- **Memory**: [analytics/memory.md](analytics/memory.md)
- **GA4 Setup**: [analytics/ga4-setup.md](analytics/ga4-setup.md)

---

## Integration Flows Documentation

### Cross-Platform Data Flows
- **Data Flow Diagram**: [integration-flows/data-flow-diagram.md](integration-flows/data-flow-diagram.md)
- **Field Mapping**: [integration-flows/field-mapping.md](integration-flows/field-mapping.md)

### Specific Workflows
*To be documented as integrations are mapped*
- Clay to Airtable flow
- Airtable to Make.com triggers
- Make.com to Email/Slack notifications
- Notion bidirectional sync

---

## Monitoring & Alerts

### What to Monitor
- **API Usage**: Track against rate limits
- **Error Rates**: Integration failures, webhook failures
- **Latency**: Time from trigger to completion
- **Data Quality**: Validation errors, missing data

### Alert Channels
- **Slack**: #alerts channel for critical issues
- **Email**: Daily digest of warnings
- **Make.com**: Built-in error notifications

### Health Checks
- **Daily**: Review error logs
- **Weekly**: Check rate limit usage
- **Monthly**: Audit all integrations, review performance

---

## Troubleshooting

### Common Issues

**Make.com Scenario Failing**:
1. Check execution history in Make.com dashboard
2. Verify webhook URLs are correct
3. Check API rate limits
4. Review error logs

**Airtable Sync Issues**:
1. Verify PAT is valid and not expired
2. Check base/table IDs in config
3. Ensure field mappings are correct
4. Review webhook configuration

**Clay Enrichment Not Working**:
1. Check credit balance
2. Verify enrichment provider is enabled
3. Test with single record
4. Check output configuration

See [/docs/troubleshooting.md](../../docs/troubleshooting.md) for complete troubleshooting guide.

---

## Next Steps

### Immediate Actions Required

1. **Document Existing Make.com Scenarios**:
   - Log into Make.com
   - List all active scenarios
   - Document each in [makecom/scenarios/scenario-index.md](makecom/scenarios/scenario-index.md)

2. **Document Existing Clay Tables**:
   - Log into Clay
   - List all tables
   - Document enrichment providers and outputs in [clay/tables/table-schemas.md](clay/tables/table-schemas.md)

3. **Document Existing Airtable Bases**:
   - Log into Airtable
   - List all bases and tables
   - Document schema in [airtable/bases/base-inventory.md](airtable/bases/base-inventory.md)

4. **Set Up New Integrations**:
   - Configure Email/SMTP credentials
   - Set up Slack webhook
   - Configure Google Analytics 4

5. **Create Integration Flow Diagrams**:
   - Map current data flows
   - Document field mappings
   - Create visual diagrams

---

## Contact & Support

### Platform Support
- **Make.com**: https://www.make.com/en/help/support
- **Clay**: support@clay.com
- **Airtable**: support.airtable.com
- **Notion**: support@makenotion.com
- **Slack**: https://slack.com/help
- **Google Analytics**: https://support.google.com/analytics

### Internal Contacts
- **API Integrations Lead**: [Contact]
- **CRM Manager**: [Contact]
- **Marketing Ops**: [Contact]

---

*This integration hub is the central source of truth for all API connections. Keep it updated as integrations are added, modified, or removed.*
