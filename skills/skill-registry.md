# Skill Registry

*Active skills and automation workflows for YNA Agentic*

Last updated: 2026-02-26

## Overview

This registry tracks all custom skills, their status, usage, and maintenance schedule.

### 💡 Value of Skills System

**⏱️ Cumulative Time Savings**: TBD as skills are added
**💰 Cumulative Money Savings**: TBD as skills are added

**Why skills save time and money:**
- **Automation**: Repetitive manual tasks converted to one-command execution
- **Consistency**: No variation in quality or process between executions
- **Self-service**: Team members can execute workflows without technical expertise or waiting for support
- **Error reduction**: Automated skills eliminate human error in repetitive processes
- **Knowledge retention**: Skills capture institutional knowledge that survives employee turnover
- **Scalability**: Once built, skills can be executed unlimited times with zero additional cost

## Active Skills

### Department Skills

#### Marketing

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No marketing skills yet. Add first skill using template.*

#### Sales

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No sales skills yet. Add first skill using template.*

#### Customer Service

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No customer service skills yet. Add first skill using template.*

#### CRM

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No CRM skills yet. Add first skill using template.*

#### Website

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No website skills yet. Add first skill using template.*

---

### Integration Skills

#### Make.com

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No Make.com skills yet. Add first skill using template.*

#### Clay

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No Clay skills yet. Add first skill using template.*

#### Airtable

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No Airtable skills yet. Add first skill using template.*

#### Email

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No email skills yet. Add first skill using template.*

#### Slack

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No Slack skills yet. Add first skill using template.*

#### Analytics

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No analytics skills yet. Add first skill using template.*

---

### Automation Skills

#### Workflows

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No workflow automation yet. Add first skill using template.*

#### Reports

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No reporting automation yet. Add first skill using template.*

#### Monitoring

| Skill Name | Purpose | Status | Last Used | Dependencies |
|------------|---------|--------|-----------|--------------|
| - | - | - | - | - |

*No monitoring automation yet. Add first skill using template.*

---

## Skill Status Legend

- ✅ **Active**: In production use, tested and maintained
- 🔄 **In Development**: Being built or tested
- 🟡 **Experimental**: Proof of concept, not production-ready
- ⏸️ **Paused**: Temporarily disabled, may reactivate
- 🔴 **Deprecated**: No longer maintained, scheduled for removal
- 📦 **Archived**: Removed from active use, saved for reference

## Maintenance Schedule

### Monthly Reviews (1st of each month)
- [ ] Test all Active skills
- [ ] Update dependencies
- [ ] Review logs for errors
- [ ] Update "Last Used" dates
- [ ] Archive skills inactive >6 months

### Quarterly Tasks
- [ ] Credential rotation check
- [ ] Performance optimization
- [ ] Documentation updates
- [ ] User feedback integration

### Annual Tasks
- [ ] Full security audit
- [ ] Architecture review
- [ ] Deprecation planning
- [ ] Skill consolidation

## Usage Statistics

*To be populated as skills are created and used*

| Month | Total Executions | Most Used Skill | Error Rate |
|-------|------------------|-----------------|------------|
| 2026-02 | 0 | - | - |

## Dependencies Overview

### Required Credentials (from .env)
*None yet - will populate as skills are added*

### Python Packages
*None yet - will populate as skills are added*

### Node Packages
*None yet - will populate as skills are added*

### External Services
*None yet - will populate as skills are added*

## Quick Start Guide

### Creating Your First Skill

1. **Choose a category**: departments, integrations, or automation
2. **Copy the template**: `cp skills/templates/skill-template.md skills/[category]/[skill-name].md`
3. **Write the script**: Create executable script in same directory
4. **Document it**: Fill out template with details
5. **Test it**: Run with `--dry-run` and `--test-mode`
6. **Register it**: Add entry to this registry
7. **Update changelog**: Add to `business-knowledge/changelog.md`

### Example: Marketing Campaign Launcher

```bash
# 1. Create documentation
cp skills/templates/skill-template.md skills/departments/marketing/launch-campaign.md

# 2. Create script
touch skills/departments/marketing/launch-campaign.sh
chmod +x skills/departments/marketing/launch-campaign.sh

# 3. Edit and implement
# ... write your script ...

# 4. Test
./skills/departments/marketing/launch-campaign.sh --dry-run

# 5. Add to registry (this file)
# 6. Update changelog
```

## Troubleshooting

### Common Issues

**Permission Denied**:
```bash
chmod +x skills/[category]/[skill-name].sh
```

**Missing Dependencies**:
```bash
pip install -r scripts/requirements.txt
```

**Credential Errors**:
- Check `.env` file has required keys
- Verify key format matches platform requirements
- Test credentials manually via platform UI

---

*For skill template, see [templates/skill-template.md](templates/skill-template.md)*

*For skill creation guide, see [README.md](README.md)*
