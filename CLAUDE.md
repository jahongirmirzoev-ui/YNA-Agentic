# YNA Agentic - Business Operating System (Rectory)

*Last Updated: 2026-02-26*

## Project Overview

YNA Agentic is a comprehensive business operating system that integrates cloud knowledge management, API orchestration, and persistent memory across Claude Code sessions. This "Rectory" (directory structure) serves as the single source of truth for all business operations.

### Core Mission
- **Centralize business knowledge** with cloud synchronization to Notion
- **Automate workflows** via API integrations (Make.com, Clay, Airtable, Email, Slack, Analytics)
- **Maintain persistent context** across all departments
- **Enable Claude Code** to access full business context instantly without restarting conversations

### Architecture
This project uses a **three-layer architecture**:

1. **Memory Layer** ([business-knowledge/](business-knowledge/))
   - Persistent department context in `memory.md` files
   - Cloud-synced from Notion every 15 minutes
   - Survives Claude Code session restarts

2. **Integration Layer** ([config/](config/) + [cloud-sync/](cloud-sync/))
   - API configurations for all platforms
   - Credential management (secure .env)
   - Webhook registries and endpoints

3. **Execution Layer** ([execution/](execution/))
   - Active campaigns, reports, proposals
   - Temporary workspaces
   - Output artifacts

---

## Quick Navigation

### Department Memory Files (READ THESE FOR CONTEXT)

When asked about any department, **ALWAYS read the memory.md file first** before responding:

- **Marketing**: [business-knowledge/departments/marketing/memory.md](business-knowledge/departments/marketing/memory.md)
- **Sales**: [business-knowledge/departments/sales/memory.md](business-knowledge/departments/sales/memory.md)
- **Customer Service**: [business-knowledge/departments/customer-service/memory.md](business-knowledge/departments/customer-service/memory.md)
- **CRM**: [business-knowledge/departments/crm/memory.md](business-knowledge/departments/crm/memory.md)
- **Website**: [business-knowledge/departments/website/memory.md](business-knowledge/departments/website/memory.md)

### API Integration Documentation

- **Integration Hub**: [business-knowledge/api-integrations/README.md](business-knowledge/api-integrations/README.md)
- **Data Flow Diagram**: [business-knowledge/api-integrations/integration-flows/data-flow-diagram.md](business-knowledge/api-integrations/integration-flows/data-flow-diagram.md)
- **Field Mappings**: [business-knowledge/api-integrations/integration-flows/field-mapping.md](business-knowledge/api-integrations/integration-flows/field-mapping.md)

**Platform-Specific**:
- **Make.com**: [business-knowledge/api-integrations/makecom/memory.md](business-knowledge/api-integrations/makecom/memory.md)
- **Clay**: [business-knowledge/api-integrations/clay/memory.md](business-knowledge/api-integrations/clay/memory.md)
- **Airtable**: [business-knowledge/api-integrations/airtable/memory.md](business-knowledge/api-integrations/airtable/memory.md)
- **Email/SMTP**: [business-knowledge/api-integrations/email/memory.md](business-knowledge/api-integrations/email/memory.md)
- **Slack**: [business-knowledge/api-integrations/slack/memory.md](business-knowledge/api-integrations/slack/memory.md)
- **Analytics**: [business-knowledge/api-integrations/analytics/memory.md](business-knowledge/api-integrations/analytics/memory.md)

### Directives (FOLLOW THESE RULES)

- **Security Protocols**: [directives/security-protocols.md](directives/security-protocols.md)
- **API Integration SOP**: [directives/api-integration-sop.md](directives/api-integration-sop.md)
- **Documentation Standards**: [directives/documentation-standards.md](directives/documentation-standards.md)
- **Cloud Sync Procedures**: [directives/cloud-sync-procedures.md](directives/cloud-sync-procedures.md)

---

## Current System Status

### Cloud Sync
- **Platform**: Notion API (primary knowledge base)
- **Sync Frequency**: Every 15 minutes (cron) + real-time webhooks (optional)
- **Last Sync**: [To be updated by sync script]
- **Status**: [Setup in progress - Phase 5]

### API Integrations Status

| Platform | Status | Active Resources | Last Updated |
|----------|--------|------------------|--------------|
| Make.com | ✅ Active | [Scenarios: TBD] | 2026-02-26 |
| Clay | ✅ Active | [Tables: TBD] | 2026-02-26 |
| Airtable | ✅ Active | [Bases: TBD] | 2026-02-26 |
| Email/SMTP | 🟡 Setup | [Configuration pending] | 2026-02-26 |
| Slack | 🟡 Setup | [Webhook pending] | 2026-02-26 |
| Analytics | 🟡 Setup | [GA4 pending] | 2026-02-26 |
| Notion | 🟡 Setup | [Integration pending] | 2026-02-26 |

**Legend**: ✅ Active | 🟡 Setup in progress | 🔴 Issue | ⏸️ Paused

### Active Priorities
1. Complete initial Rectory structure setup
2. Document existing Make.com scenarios, Clay tables, Airtable bases
3. Set up Notion integration and cloud sync
4. Populate department memory files with current state
5. Configure remaining API integrations (Email, Slack, Analytics)

---

## TODO Tracking

**Active TODO List**: [todos/TODO.md](todos/TODO.md)

All tasks, priorities, and completed items are tracked in the dedicated TODO folder. Claude will proactively suggest adding items and update completion status.

---

## Context for Claude Code

### How to Use This System

**When Asked About Departments:**
1. Read the relevant `memory.md` file first
2. Check related API integration docs if needed
3. Review recent changes in [business-knowledge/changelog.md](business-knowledge/changelog.md)
4. Provide context-aware responses based on current state

**When Making Changes to Business Knowledge:**
1. Edit local files in `business-knowledge/`
2. Changes will auto-sync to Notion (when cloud sync is active)
3. Update [business-knowledge/changelog.md](business-knowledge/changelog.md) with summary
4. Mark changes with timestamp

**When Working with APIs:**
1. Check rate limits in [business-knowledge/api-integrations/README.md](business-knowledge/api-integrations/README.md)
2. Verify credentials exist in `.env` file
3. Use correct environment from [config/environments/](config/environments/)
4. Follow [directives/api-integration-sop.md](directives/api-integration-sop.md)

**When Creating Documentation:**
1. Use templates from department folders
2. Follow naming convention: `[DocumentType]_[Department]_[Topic]_[Date]_v[Version].ext`
3. Reference [directives/documentation-standards.md](directives/documentation-standards.md)
4. Update relevant memory.md file

---

## Critical Directives

### Security Rules (STRICTLY ENFORCE)

- ⛔ **NEVER** commit `.env` files to git
- ✅ **ALWAYS** use `.env.template` for examples
- ✅ **CHECK** `.gitignore` before any git commits
- ✅ **ROTATE** API keys every 60-90 days (tracked in [config/credential-registry.md](config/credential-registry.md))
- ⛔ **NEVER** include credentials in code or documentation
- ✅ **VERIFY** git status shows no sensitive files before commits

### Cloud Sync Rules

- Cloud sync runs automatically every 15 minutes (when configured)
- Manual sync command: `python3 cloud-sync/scripts/notion-sync.py`
- Conflict resolution: Last-write-wins with conflict markers
- Sync logs location: `cloud-sync/notion/sync-logs/`
- Webhook sync (optional): ~30 second latency via Make.com

### Documentation Standards

- Use templates from `business-knowledge/departments/[dept]/templates/`
- File naming: `[DocumentType]_[Department]_[Topic]_[Date]_v[Version].ext`
- Update `memory.md` files after major changes
- Keep [business-knowledge/changelog.md](business-knowledge/changelog.md) current
- All markdown files use absolute paths for cross-references

### API Operation Rules

- Always check rate limits before bulk operations
- Implement retry logic with exponential backoff
- Log all API errors to `.tmp/api-logs.json`
- Document new integrations following [directives/api-integration-sop.md](directives/api-integration-sop.md)
- Update connection registry when adding/modifying integrations

---

## Environment Setup

### Current Environment
- **Active**: Development
- **Config**: [config/environments/development.json](config/environments/development.json)
- **Debug Mode**: Enabled
- **Cloud Sync**: Not yet configured

### Available Environments
- **Development**: Local testing, debug logging, sample data
- **Staging**: Pre-production, Make.com test scenarios
- **Production**: Live integrations, minimal logging, production credentials

---

## Common Tasks & How-To

### Update Department Context
**User Request**: "Update Marketing memory with [new information]"

**Claude Actions**:
1. Read current [business-knowledge/departments/marketing/memory.md](business-knowledge/departments/marketing/memory.md)
2. Make requested updates
3. Update timestamp
4. Update [business-knowledge/changelog.md](business-knowledge/changelog.md)

### Check API Integration Status
**User Request**: "What's the status of our API integrations?"

**Claude Actions**:
1. Read [business-knowledge/api-integrations/README.md](business-knowledge/api-integrations/README.md)
2. Check rate limits and usage
3. Review platform-specific memory.md files
4. Report current state and any issues

### Document Existing Integration
**User Request**: "Document my Make.com scenario for [process]"

**Claude Actions**:
1. Follow [directives/api-integration-sop.md](directives/api-integration-sop.md)
2. Create entry in [business-knowledge/api-integrations/makecom/scenarios/scenario-index.md](business-knowledge/api-integrations/makecom/scenarios/scenario-index.md)
3. Update [business-knowledge/api-integrations/makecom/memory.md](business-knowledge/api-integrations/makecom/memory.md)
4. Update connection registry

### Create Campaign/Report
**User Request**: "Create [type] for [department]"

**Claude Actions**:
1. Check for templates in `business-knowledge/departments/[dept]/templates/`
2. Use template or create from scratch
3. Save to `execution/[campaigns|reports]/`
4. Follow documentation standards

### Manual Cloud Sync
**User Request**: "Sync with Notion now"

**Claude Actions**:
```bash
python3 cloud-sync/scripts/notion-sync.py
```
Check logs: `cloud-sync/notion/sync-logs/sync-$(date +%Y-%m-%d).log`

---

## Recent Changes

**2026-02-26**:
- ✅ Initial Rectory structure created
- ✅ Security files configured (.gitignore, .env.template)
- ✅ Git repository initialized
- ✅ Core directory structure established
- ✅ CLAUDE.md created for persistent context
- 🔄 Department memory files: In progress
- 🔄 API integration documentation: In progress
- 🔄 Cloud sync setup: Pending

---

## Key Files Reference

### For Marketing Tasks
- Campaign templates: [business-knowledge/departments/marketing/campaigns/templates/](business-knowledge/departments/marketing/campaigns/templates/)
- Brand guidelines: [business-knowledge/departments/marketing/brand-guidelines.md](business-knowledge/departments/marketing/brand-guidelines.md)
- Content calendar: [business-knowledge/departments/marketing/content-calendar.md](business-knowledge/departments/marketing/content-calendar.md)
- Metrics/KPIs: [business-knowledge/departments/marketing/metrics-kpis.md](business-knowledge/departments/marketing/metrics-kpis.md)

### For Sales Tasks
- Playbooks: [business-knowledge/departments/sales/playbooks/](business-knowledge/departments/sales/playbooks/)
- Pipeline stages: [business-knowledge/departments/sales/pipeline-stages.md](business-knowledge/departments/sales/pipeline-stages.md)
- Scripts/Templates: [business-knowledge/departments/sales/scripts-templates.md](business-knowledge/departments/sales/scripts-templates.md)

### For Customer Service
- SOPs: [business-knowledge/departments/customer-service/sops/](business-knowledge/departments/customer-service/sops/)
- Escalation matrix: [business-knowledge/departments/customer-service/escalation-matrix.md](business-knowledge/departments/customer-service/escalation-matrix.md)
- Response templates: [business-knowledge/departments/customer-service/response-templates.md](business-knowledge/departments/customer-service/response-templates.md)

### For CRM Management
- Data schema: [business-knowledge/departments/crm/data-schema.md](business-knowledge/departments/crm/data-schema.md)
- Workflow automations: [business-knowledge/departments/crm/workflow-automations.md](business-knowledge/departments/crm/workflow-automations.md)
- Custom fields: [business-knowledge/departments/crm/custom-fields.md](business-knowledge/departments/crm/custom-fields.md)

### For Website Tasks
- Site architecture: [business-knowledge/departments/website/site-architecture.md](business-knowledge/departments/website/site-architecture.md)
- Content inventory: [business-knowledge/departments/website/content-inventory.md](business-knowledge/departments/website/content-inventory.md)
- SEO strategy: [business-knowledge/departments/website/seo-strategy.md](business-knowledge/departments/website/seo-strategy.md)

---

## Troubleshooting

### Common Issues

**Cloud Sync Not Working**:
1. Check sync logs: `cloud-sync/notion/sync-logs/`
2. Verify Notion API key in `.env`
3. Test manual sync: `python3 cloud-sync/scripts/notion-sync.py`
4. See [docs/troubleshooting.md](docs/troubleshooting.md)

**API Errors**:
1. Check rate limits in API integration README
2. Verify credentials in `.env`
3. Review error logs in `.tmp/api-logs.json`
4. Check platform status pages

**Missing Context**:
1. Verify `memory.md` files exist and are updated
2. Check file paths in this CLAUDE.md
3. Review [business-knowledge/changelog.md](business-knowledge/changelog.md)
4. Refresh by reading relevant files

### Support Resources
- **Setup Guide**: [docs/setup-guide.md](docs/setup-guide.md)
- **Troubleshooting**: [docs/troubleshooting.md](docs/troubleshooting.md)
- **API Integration Guide**: [docs/api-integration-guide.md](docs/api-integration-guide.md)
- **Architecture**: [docs/architecture.md](docs/architecture.md)

---

## Implementation Status

**Completed Phases**:
- ✅ Phase 1: Foundation & Security (git, .gitignore, .env.template, structure, CLAUDE.md)

**In Progress**:
- 🔄 Phase 2: Department Structure & Memory Files
- 🔄 Phase 3: API Integration Hub
- 🔄 Phase 4: Directives & SOPs
- ⏸️ Phase 5: Cloud Sync with Notion
- ⏸️ Phase 6: Configuration & Credential Management
- ⏸️ Phase 7: Documentation
- ⏸️ Phase 8: Testing & Launch

---

*This file is automatically loaded by Claude Code on every session start. It provides the primary context for understanding the YNA Agentic business operating system. Keep it updated with current priorities, system status, and navigation to detailed documentation.*

*For detailed documentation, see [README.md](README.md)*
