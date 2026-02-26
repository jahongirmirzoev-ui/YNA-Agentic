# Sales Department - Memory & Context

*Last Updated: 2026-02-26*

## Department Mission

Convert qualified leads into customers through consultative selling, relationship building, and data-driven pipeline management. Deliver exceptional customer experience while achieving revenue targets.

---

## Current State

### Active Projects
*To be populated with actual projects*

- [Pipeline optimization initiative]
- [Sales enablement program]
- [CRM implementation/improvement]

### Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Monthly Closed Deals | TBD | TBD | 🔄 Setup |
| Average Deal Size | TBD | TBD | 🔄 Setup |
| Sales Cycle Length (days) | TBD | TBD | 🔄 Setup |
| Win Rate | TBD | 30% | 🔄 Setup |
| Pipeline Value | TBD | TBD | 🔄 Setup |

### Recent Wins
- [Date]: [Achievement]

---

## Team Context

### Roles & Responsibilities
- **Sales Lead**: Strategy, team management, major deal oversight
- **Account Executives**: Lead qualification, demos, closing
- **Sales Development Reps**: Outbound prospecting, lead qualification
- **Sales Ops**: CRM management, reporting, process optimization

### Key Contacts
- **Marketing Lead**: Lead quality feedback, campaign alignment
- **Customer Service**: Customer handoff, account management
- **Product**: Feature requests, customer feedback

---

## Processes & Workflows

### Sales Process Stages
1. **Prospecting**: Lead identification and initial outreach
2. **Qualification**: BANT/MEDDIC framework
3. **Demo/Presentation**: Product demonstration
4. **Proposal**: Customized proposal and pricing
5. **Negotiation**: Terms and contract discussion
6. **Closed Won/Lost**: Deal outcome and handoff

### Standard Operating Procedures
- **Lead Qualification SOP**: See [business-knowledge/processes/lead-management/lead-qualification.md](../../processes/lead-management/lead-qualification.md)
- **Demo Process**: [sops/demo-process.md](sops/demo-process.md) (To be created)
- **Customer Handoff**: [sops/customer-handoff.md](sops/customer-handoff.md) (To be created)

### Automation Triggers
- **New qualified lead** → Airtable → Make.com → Slack notification to sales team
- **Deal stage change** → Airtable webhook → Make.com → Update reporting dashboard
- **Deal closed** → Trigger customer onboarding workflow

---

## Tools & Integrations

### Primary Tools
- **Airtable**: CRM and pipeline management
- **Make.com**: Workflow automation
- **Email**: Outreach and communication
- **Slack**: Team coordination and alerts

### API Connections
| From | To | Purpose | Status |
|------|-----|---------|--------|
| Airtable | Make.com | Deal stage triggers | ✅ Active |
| Make.com | Slack | Deal notifications | 🟡 Setup |
| Make.com | Email | Follow-up sequences | 🟡 Setup |

---

## Knowledge Base

### Important Documents
- **Sales Playbooks**: [playbooks/](playbooks/) (To be created)
- **Pipeline Stages**: [pipeline-stages.md](pipeline-stages.md) (To be created)
- **Scripts & Templates**: [scripts-templates.md](scripts-templates.md) (To be created)
- **Customer Personas**: [customer-personas.md](customer-personas.md) (To be created)

### Templates
- **Email Outreach**: [templates/email-outreach.md](templates/email-outreach.md)
- **Demo Script**: [templates/demo-script.md](templates/demo-script.md)
- **Proposal Template**: [templates/proposal-template.md](templates/proposal-template.md)

---

## Existing Integrations
*To be documented from your actual accounts*

### Make.com Scenarios
[Document in api-integrations/makecom/scenarios/]

### Airtable Bases
[Document in api-integrations/airtable/bases/]

---

## Pain Points & Challenges
*To be populated*

---

## Future Plans
- **Q2 2026**: [To be added]

---

## Notes for Claude

**Important Context**:
- Sales cycle typically 30-90 days depending on deal size
- Always qualify leads using BANT framework before demos
- Pipeline reviews happen weekly - keep Airtable updated
- Customer handoff to Customer Service must be documented

**Common Requests**:
- "Check pipeline status" → Review Airtable CRM data
- "Create proposal" → Use proposal template
- "Update deal stage" → Update in Airtable, triggers Make.com automations

---

*Synced with Notion - updates bidirectional*
