# Marketing Department - Memory & Context

*Last Updated: 2026-02-26*

## Department Mission

Drive brand awareness, generate qualified leads, and support sales through integrated digital marketing campaigns across all channels. Focus on data-driven strategies that deliver measurable ROI and sustainable growth.

---

## Current State

### Active Projects
*To be populated with actual projects*

- **Example**: Q1 2026 Lead Generation Campaign - Status, next steps
- **Example**: Website Redesign - Current phase, timeline
- **Example**: Content Calendar 2026 - Progress, upcoming milestones

### Key Metrics
*To be updated with actual metrics*

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Monthly Qualified Leads | TBD | TBD | 🔄 Setup |
| Website Traffic (monthly) | TBD | TBD | 🔄 Setup |
| Email Open Rate | TBD | 25% | 🔄 Setup |
| Social Media Engagement | TBD | 4% | 🔄 Setup |
| Campaign ROI | TBD | TBD | 🔄 Setup |

### Recent Wins
*To be populated with achievements*

- [Date]: [Achievement description]
- [Date]: [Achievement description]

---

## Team Context

### Roles & Responsibilities
*To be populated with actual team structure*

- **Marketing Lead**: Strategy, budget, team coordination
- **Content Manager**: Blog, social media, email campaigns
- **Paid Media Specialist**: PPC, social ads, retargeting
- **Marketing Ops**: Automation, analytics, integrations

### Key Contacts
*To be populated with actual contacts*

- **Sales Lead**: [Name] - Lead quality feedback, sales enablement
- **Product**: [Name] - Feature launches, product marketing
- **Design**: [Name] - Creative assets, brand consistency

---

## Processes & Workflows

### Standard Operating Procedures (SOPs)
*Links to detailed SOPs*

- **Campaign Launch Process**: `business-knowledge/departments/marketing/sops/campaign-launch-sop.md` (To be created)
- **Content Publishing**: `business-knowledge/departments/marketing/sops/content-publishing-sop.md` (To be created)
- **Lead Handoff to Sales**: See `business-knowledge/processes/lead-management/lead-qualification.md` (To be created)

### Automation Triggers
*Document automated workflows*

Example workflow:
1. **New lead from website form** → Clay enrichment → Airtable storage → Make.com trigger → Email nurture sequence
2. **Blog publish** → Auto-post to social media (via Make.com)
3. **Weekly performance report** → Auto-generate & email (via Make.com)

*To be documented with actual Make.com scenarios*

---

## Tools & Integrations

### Primary Tools
*Document all marketing tools*

- **Clay**: Lead enrichment, data scraping for prospecting
- **Airtable**: Campaign tracking, content calendar, lead database
- **Make.com**: All workflow automation (scenarios to be documented)
- **Email Platform**: Campaign sends, nurture sequences (to be configured)
- **Slack**: Team notifications, campaign alerts
- **Google Analytics**: Website traffic, conversion tracking

### API Connections
*Document active integrations*

| From | To | Connection Name | Purpose | Status |
|------|-----|-----------------|---------|--------|
| Clay | Airtable | Marketing Lead Enrichment | Real-time lead data push | ✅ Active |
| Airtable | Make.com | Campaign Trigger | Webhook on status change | ✅ Active |
| Make.com | Email | Nurture Sequence | Daily batch send | 🟡 Setup |
| Make.com | Slack | Campaign Alerts | Real-time notifications | 🟡 Setup |

---

## Knowledge Base

### Important Documents
*Links to key marketing resources*

- **Brand Guidelines**: [business-knowledge/departments/marketing/brand-guidelines.md](brand-guidelines.md) (To be created)
- **Content Calendar**: [business-knowledge/departments/marketing/content-calendar.md](content-calendar.md) (To be created)
- **Metrics Dashboard**: [business-knowledge/departments/marketing/metrics-kpis.md](metrics-kpis.md) (To be created)
- **Campaign Archive**: `execution/campaigns/` (Active campaigns stored here)

### Templates Used
*Marketing templates*

- **Campaign Brief**: [campaigns/templates/campaign-brief-template.md](campaigns/templates/campaign-brief-template.md) (To be created)
- **Blog Post**: [campaigns/templates/blog-post-template.md](campaigns/templates/blog-post-template.md) (To be created)
- **Social Media Post**: [campaigns/templates/social-post-template.md](campaigns/templates/social-post-template.md) (To be created)
- **Email Campaign**: [campaigns/templates/email-template.md](campaigns/templates/email-template.md) (To be created)

---

## Make.com Scenarios (Existing)
*To be documented based on your actual Make.com account*

### Active Scenarios
| Scenario Name | Purpose | Trigger | Actions | Last Updated |
|--------------|---------|---------|---------|--------------|
| [To be documented] | - | - | - | - |

**Action Required**: Document all existing Make.com scenarios in [business-knowledge/api-integrations/makecom/scenarios/scenario-index.md](../../api-integrations/makecom/scenarios/scenario-index.md)

---

## Clay Tables (Existing)
*To be documented based on your actual Clay account*

### Active Tables
| Table Name | Purpose | Enrichment Providers | Output Destination | Records |
|-----------|---------|---------------------|-------------------|----------|
| [To be documented] | - | - | - | - |

**Action Required**: Document all existing Clay tables in [business-knowledge/api-integrations/clay/tables/table-schemas.md](../../api-integrations/clay/tables/table-schemas.md)

---

## Airtable Bases (Existing)
*To be documented based on your actual Airtable account*

### Marketing Bases
| Base Name | Tables | Purpose | Connected To | Records |
|-----------|--------|---------|--------------|----------|
| [To be documented] | - | - | - | - |

**Action Required**: Document all existing Airtable bases in [business-knowledge/api-integrations/airtable/bases/base-inventory.md](../../api-integrations/airtable/bases/base-inventory.md)

---

## Pain Points & Challenges
*Current blockers and issues*

- [To be populated with actual challenges]
- Example: Lead quality from paid ads needs improvement
- Example: Content production bottleneck
- Example: Attribution tracking across multi-touch journeys

---

## Future Plans
*Roadmap and upcoming initiatives*

- **Q2 2026**: [Plans to be added]
- **Q3 2026**: [Plans to be added]
- **Q4 2026**: [Plans to be added]

---

## Notes for Claude

**Important Context to Remember**:
- Always check lead quality metrics before suggesting new lead sources
- Marketing campaigns typically have 2-week planning cycle
- Budget decisions require approval from Marketing Lead
- When creating campaign content, reference [brand-guidelines.md](brand-guidelines.md) for voice/tone
- Use Airtable as the single source of truth for campaign tracking
- All API integrations should be documented in the api-integrations folder

**Common Requests**:
- "Create a new campaign" → Use campaign brief template, save to execution/campaigns/
- "Check campaign performance" → Review metrics in this file and Airtable data
- "Update marketing metrics" → Edit the Key Metrics table above
- "Document Make.com scenario" → Add to api-integrations/makecom/scenarios/

**Integration Notes**:
- Clay → Airtable integration is real-time
- Make.com scenarios trigger on Airtable webhooks
- Email sends are scheduled (not real-time) to manage rate limits
- Slack notifications should be used for urgent alerts only

---

*This memory file is synced with Notion. Updates made here will sync to cloud within 15 minutes (when sync is configured). Updates made in Notion will sync back to this file automatically.*
