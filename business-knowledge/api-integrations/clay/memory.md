# Clay Integration - Memory & Context

*Last Updated: 2026-02-26*

## Overview

Clay is the primary data enrichment platform, used for lead enrichment, company research, and contact finding. Enriched data flows to Airtable for storage and further processing.

---

## Current Status

- **Status**: ✅ Active
- **API Key**: Configured in `.env`
- **Workspace ID**: TBD
- **Active Tables**: TBD (to be documented)
- **Monthly Credits**: TBD / 100 limit

---

## Active Tables

**Action Required**: Document all existing tables from your Clay account in [tables/table-schemas.md](tables/table-schemas.md)

### Common Table Types
- **Lead Enrichment**: Enrich contact information (email, phone, social profiles)
- **Company Research**: Company data (size, funding, tech stack, industry)
- **Contact Finding**: Find decision makers at target companies
- **Data Validation**: Verify email addresses, phone numbers

---

## Enrichment Providers

See [enrichment-providers.md](enrichment-providers.md) for details.

**Available Providers**:
- Clearbit: Company and contact data
- Hunter: Email finder and verification
- LinkedIn: Professional profiles
- Crunchbase: Company funding and financials
- BuiltWith: Technology stack detection
- [Others to be documented]

---

## Data Flow

```
Input → Clay Table → Enrichment Providers → Enriched Data → Airtable
```

**Typical Flow**:
1. Lead captured from website form
2. Sent to Clay via webhook/API
3. Clay runs enrichment waterfall
4. Enriched data pushed to Airtable
5. Airtable triggers Make.com for notifications

---

## Credit Management

- **Monthly Allocation**: 100 credits
- **Current Usage**: TBD
- **Alert Threshold**: 80 credits (80%)
- **Cost per Enrichment**: Varies by provider (1-10 credits)

**Credit Optimization**:
- Use enrichment waterfalls (try cheap providers first)
- Cache results in Airtable to avoid re-enrichment
- Only enrich qualified leads
- Monitor credit usage weekly

---

## Best Practices

- Test enrichment waterfalls before running on bulk data
- Use filters to enrich only qualified records
- Set up fallback providers for critical data points
- Document all table schemas
- Monitor credit usage closely

---

## Notes for Claude

- Clay credits are precious - only enrich when necessary
- Always check credit balance before bulk operations
- Document new tables immediately after creation
- Keep table schemas updated in tables/table-schemas.md

---

*For table documentation, see [tables/table-schemas.md](tables/table-schemas.md)*
