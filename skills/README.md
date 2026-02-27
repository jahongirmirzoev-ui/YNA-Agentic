# Skills Directory

*Custom capabilities and automation scripts for YNA Agentic Business Operating System*

## Overview

This directory contains custom skills, scripts, and automation workflows that extend Claude Code's capabilities for business operations.

### 💡 Value Proposition

**⏱️ Time Savings**: Skills convert hours of manual work into seconds of automated execution
**💰 Money Savings**: Eliminates repetitive labor costs and enables team to focus on high-value work

**Why skills save time and money:**

1. **Automation at Scale**
   - Manual task: 30 minutes → Automated skill: 30 seconds (60x faster)
   - One skill can be executed unlimited times with zero additional cost
   - Example: "Generate monthly report" saves 4 hours/month = $400/month (at $100/hr)

2. **Consistency & Quality**
   - Eliminates human error that causes rework (estimated 10-15% of time wasted on fixing mistakes)
   - Follows exact process every time, ensuring compliance and quality
   - No training required for new team members - skills encode institutional knowledge

3. **Self-Service Enablement**
   - Team members execute complex workflows without technical expertise
   - Reduces dependency bottlenecks (e.g., waiting 2 days for IT to run a report)
   - Enables 24/7 operations - skills can run on schedules or triggers

4. **Faster Decision-Making**
   - Real-time data access instead of waiting for manual reporting cycles
   - Reduces time-to-decision from days to minutes
   - Opportunity cost savings: Earlier decisions = earlier revenue/earlier problem resolution

**Example ROI Calculation:**
- **5 skills** × **4 uses/week** × **25 minutes saved per use** = **8.3 hours/week saved**
- At $100/hr: **$43,300/year in labor savings**
- Plus: Reduced errors, faster turnaround, better customer experience

## Structure

```
skills/
├── departments/        # Department-specific skills
│   ├── marketing/     # Marketing automation & workflows
│   ├── sales/         # Sales playbook execution
│   ├── customer-service/  # Support automation
│   ├── crm/           # CRM operations
│   └── website/       # Website management
├── integrations/      # API platform skills
│   ├── makecom/       # Make.com scenario management
│   ├── clay/          # Clay table operations
│   ├── airtable/      # Airtable automation
│   ├── email/         # Email campaign automation
│   ├── slack/         # Slack notifications & workflows
│   └── analytics/     # Analytics & reporting
├── automation/        # Cross-functional automation
│   ├── workflows/     # Multi-step business processes
│   ├── reports/       # Automated reporting
│   └── monitoring/    # System health checks
└── templates/         # Skill templates and examples
```

## Skill Types

### 1. Department Skills
Execute department-specific workflows using existing templates and SOPs.

**Examples**:
- Marketing campaign launch
- Sales pipeline health check
- Customer ticket triage
- CRM data cleanup
- Website content updates

### 2. Integration Skills
Automate API operations across platforms.

**Examples**:
- Trigger Make.com scenarios
- Enrich Clay tables
- Update Airtable records
- Send email sequences
- Post Slack alerts
- Generate analytics dashboards

### 3. Automation Skills
Cross-functional workflows that span multiple departments or systems.

**Examples**:
- End-to-end lead processing
- Monthly business reporting
- System health monitoring
- Data synchronization checks
- Credential rotation reminders

## Creating New Skills

### Skill Template

See [templates/skill-template.md](templates/skill-template.md) for the standard format.

### Naming Convention

```
[category]-[action]-[target].sh
```

**Examples**:
- `marketing-launch-campaign.sh`
- `makecom-trigger-scenario.sh`
- `crm-cleanup-duplicates.sh`
- `reports-generate-monthly.sh`

### Documentation Requirements

Each skill must include:
1. **Purpose**: What it does and why
2. **Prerequisites**: Required credentials, dependencies
3. **Parameters**: Input arguments and flags
4. **Output**: What it produces or modifies
5. **Example Usage**: Sample command invocations
6. **Error Handling**: Common issues and solutions

## Usage Patterns

### From Claude Code
Skills can be invoked directly by Claude when processing user requests:

```
User: "Launch the Q1 marketing campaign"
Claude: [Reads skill] → [Executes marketing-launch-campaign.sh]
```

### From Command Line
Skills are executable scripts that can run standalone:

```bash
# Direct execution
./skills/marketing/launch-campaign.sh --campaign Q1_2026

# Via automation
cron: 0 9 * * 1 /path/to/skills/reports/generate-weekly.sh
```

### From API Integrations
Skills can be triggered by webhooks or Make.com scenarios:

```json
{
  "trigger": "deal_won",
  "action": "execute_skill",
  "skill": "sales/onboard-customer.sh",
  "params": {"deal_id": "12345"}
}
```

## Security Considerations

- **Credentials**: All skills use `.env` for sensitive data (NEVER hardcode)
- **Validation**: Input validation required for all parameters
- **Logging**: All executions logged to `.tmp/skill-logs/`
- **Rate Limits**: Respect API limits defined in `business-knowledge/api-integrations/`
- **Permissions**: Skills run with user's permissions (no sudo unless explicitly required)

## Integration with Memory System

Skills should:
1. Read relevant `memory.md` files for context
2. Update memory files after significant operations
3. Log changes to `business-knowledge/changelog.md`
4. Follow documentation standards in `directives/documentation-standards.md`

## Skill Registry

Active skills are tracked in [skill-registry.md](skill-registry.md) with:
- Name and purpose
- Last updated date
- Maintenance status
- Usage frequency
- Dependencies

## Testing

All skills should include:
- Unit tests (where applicable)
- Dry-run mode (`--dry-run` flag)
- Verbose output (`--verbose` flag)
- Error simulation (`--test-error` flag)

## Examples

### Department Skill Example
```bash
# Marketing campaign launcher
./skills/departments/marketing/launch-campaign.sh \
  --campaign Q1_2026 \
  --channels email,social \
  --dry-run
```

### Integration Skill Example
```bash
# Trigger Make.com scenario
./skills/integrations/makecom/trigger-scenario.sh \
  --scenario lead-enrichment \
  --payload '{"email":"contact@example.com"}'
```

### Automation Skill Example
```bash
# Generate monthly report
./skills/automation/reports/generate-monthly.sh \
  --month 2026-02 \
  --departments marketing,sales \
  --output execution/reports/
```

## Maintenance

- Review skill registry monthly
- Update dependencies quarterly
- Rotate credentials per security protocols
- Archive unused skills (inactive > 6 months)
- Document breaking changes in changelog

---

*For questions or issues, refer to [docs/troubleshooting.md](../docs/troubleshooting.md) or update this README with new patterns.*

*Last updated: 2026-02-26*
