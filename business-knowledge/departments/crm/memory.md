# CRM Department - Memory & Context

*Last Updated: 2026-02-26*

## Department Mission

Manage customer data, ensure data integrity, optimize CRM workflows, and provide actionable insights through reporting and analytics. Enable all departments with clean, accessible customer data.

---

## Current State

### Active Projects
*To be populated*

- [CRM optimization initiative]
- [Data quality improvement]
- [Integration expansion]

### Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Data Quality Score | TBD | >95% | 🔄 Setup |
| Duplicate Records | TBD | <1% | 🔄 Setup |
| Total Contacts/Companies | TBD | TBD | 🔄 Setup |
| Active Workflows | TBD | TBD | 🔄 Setup |

### Recent Wins
- [Date]: [Achievement]

---

## Team Context

### Roles & Responsibilities
- **CRM Manager**: Strategy, data governance, integrations
- **CRM Administrator**: Configuration, user management
- **Data Analyst**: Reporting, insights, data quality

### Key Contacts
- **Sales**: CRM usage, pipeline management
- **Marketing**: Campaign data, lead management
- **Customer Service**: Customer records, ticket integration

---

## Processes & Workflows

### Data Management
1. **Data Collection**: Multi-source ingestion (web forms, APIs, manual)
2. **Data Enrichment**: Clay integration for contact/company data
3. **Data Storage**: Airtable as central CRM database
4. **Data Distribution**: Make.com for cross-platform sync

### Standard Operating Procedures
- **Data Entry Standards**: [sops/data-entry-standards.md](sops/data-entry-standards.md) (To be created)
- **Deduplication Process**: [sops/deduplication.md](sops/deduplication.md) (To be created)
- **Data Governance**: See [business-knowledge/processes/data-governance/](../../processes/data-governance/)

### Automation Workflows
- **New contact** → Clay enrichment → Airtable storage → Notify relevant team
- **Duplicate detection** → Auto-merge or flag for review
- **Data quality check** → Weekly automated scan → Report anomalies

---

## Tools & Integrations

### Primary Tools
- **Airtable**: Primary CRM database
- **Clay**: Data enrichment and validation
- **Make.com**: Workflow automation and integration
- **Analytics**: Reporting and dashboards

### CRM Architecture

```
Data Sources → Clay (Enrichment) → Airtable (Storage) → Make.com (Distribution) → Teams
```

### API Connections
| From | To | Purpose | Status |
|------|-----|---------|--------|
| Web Forms | Clay | Lead capture | ✅ Active |
| Clay | Airtable | Enriched data storage | ✅ Active |
| Airtable | Make.com | Workflow triggers | ✅ Active |
| Make.com | Slack | Data quality alerts | 🟡 Setup |

---

## Knowledge Base

### Important Documents
- **Data Schema**: [data-schema.md](data-schema.md) (To be created)
- **Workflow Automations**: [workflow-automations.md](workflow-automations.md) (To be created)
- **Custom Fields**: [custom-fields.md](custom-fields.md) (To be created)
- **Integration Map**: [integration-map.md](integration-map.md) (To be created)

### Airtable Base Structure
*To be documented*

**Bases**:
- CRM Main: Contacts, Companies, Deals, Activities
- Marketing Hub: Campaigns, Leads, Content
- Support: Tickets, Customer Feedback

---

## Existing Integrations
*To be documented from actual accounts*

### Airtable Bases
[Document in api-integrations/airtable/bases/base-inventory.md]

### Clay Tables
[Document in api-integrations/clay/tables/table-schemas.md]

### Make.com Scenarios
[Document in api-integrations/makecom/scenarios/scenario-index.md]

---

## Data Flow Patterns

### Primary Flow: Lead Capture → Enrichment → Storage
1. Lead submits form
2. Webhook to Clay
3. Clay enriches (Clearbit, Hunter, etc.)
4. Push to Airtable
5. Airtable webhook to Make.com
6. Make.com notifies relevant team (Sales/Marketing)

### Field Mapping
See [business-knowledge/api-integrations/integration-flows/field-mapping.md](../../api-integrations/integration-flows/field-mapping.md)

---

## Pain Points & Challenges
*To be populated*

---

## Future Plans
- **Q2 2026**: [To be added]

---

## Notes for Claude

**Important Context**:
- Airtable is the single source of truth for all customer data
- All data changes should flow through established workflows
- Data quality is critical - validate before import
- Cross-platform field mapping must be consistent

**Common Requests**:
- "Add new field" → Update data-schema.md, configure in Airtable, update integrations
- "Check data quality" → Run deduplication, validate required fields
- "Document integration" → Add to integration-map.md and api-integrations folder

**Integration Notes**:
- Clay → Airtable is real-time
- Use UPSERT operations to prevent duplicates
- Always map fields consistently across platforms

---

*Synced with Notion - updates bidirectional*
