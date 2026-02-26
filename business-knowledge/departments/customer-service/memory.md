# Customer Service Department - Memory & Context

*Last Updated: 2026-02-26*

## Department Mission

Deliver exceptional customer support, resolve issues efficiently, and build long-term customer relationships that drive retention and advocacy.

---

## Current State

### Active Projects
*To be populated*

- [Support process optimization]
- [Knowledge base development]
- [Customer feedback system]

### Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| First Response Time | TBD | <2 hours | 🔄 Setup |
| Resolution Time | TBD | <24 hours | 🔄 Setup |
| Customer Satisfaction (CSAT) | TBD | >90% | 🔄 Setup |
| Ticket Volume (monthly) | TBD | TBD | 🔄 Setup |
| Escalation Rate | TBD | <5% | 🔄 Setup |

### Recent Wins
- [Date]: [Achievement]

---

## Team Context

### Roles & Responsibilities
- **CS Lead**: Team management, escalations, process improvement
- **Support Specialists**: Ticket resolution, customer communication
- **Technical Support**: Complex technical issues

### Key Contacts
- **Sales**: Customer handoff, account context
- **Product**: Bug reports, feature requests
- **Engineering**: Technical escalations

---

## Processes & Workflows

### Support Tiers
1. **Tier 1**: General inquiries, basic troubleshooting
2. **Tier 2**: Technical issues, account management
3. **Tier 3**: Engineering escalations, critical bugs

### Standard Operating Procedures
- **Ticket Triage**: [sops/ticket-triage.md](sops/ticket-triage.md) (To be created)
- **Escalation Matrix**: [escalation-matrix.md](escalation-matrix.md) (To be created)
- **Response Templates**: [response-templates.md](response-templates.md) (To be created)
- **Customer Onboarding**: See [business-knowledge/processes/onboarding/customer-onboarding.md](../../processes/onboarding/customer-onboarding.md)

### Automation Triggers
- **New support ticket** → Airtable → Make.com → Slack notification
- **Ticket unresolved >24hrs** → Auto-escalation alert
- **Customer survey** → Auto-send after ticket resolution

---

## Tools & Integrations

### Primary Tools
- **Airtable**: Ticket management system
- **Email**: Customer communication
- **Slack**: Team coordination, escalations
- **Make.com**: Workflow automation

### API Connections
| From | To | Purpose | Status |
|------|-----|---------|--------|
| Email | Airtable | Ticket creation | 🟡 Setup |
| Airtable | Make.com | Escalation triggers | 🟡 Setup |
| Make.com | Slack | Team notifications | 🟡 Setup |

---

## Knowledge Base

### Important Documents
- **FAQ Database**: [faq-database.md](faq-database.md) (To be created)
- **Escalation Matrix**: [escalation-matrix.md](escalation-matrix.md) (To be created)
- **Response Templates**: [response-templates.md](response-templates.md) (To be created)

### Templates
- **First Response**: [templates/first-response.md](templates/first-response.md)
- **Resolution Email**: [templates/resolution-email.md](templates/resolution-email.md)
- **Escalation Notice**: [templates/escalation-notice.md](templates/escalation-notice.md)

---

## Existing Integrations
*To be documented*

---

## Pain Points & Challenges
*To be populated*

---

## Future Plans
- **Q2 2026**: [To be added]

---

## Notes for Claude

**Important Context**:
- First response SLA is critical - prioritize new tickets
- Always use escalation matrix for severity 1 issues
- Document all resolutions for knowledge base
- Customer feedback drives product improvements

**Common Requests**:
- "Check support queue" → Review Airtable tickets
- "Send response" → Use appropriate template
- "Escalate ticket" → Follow escalation matrix

---

*Synced with Notion - updates bidirectional*
