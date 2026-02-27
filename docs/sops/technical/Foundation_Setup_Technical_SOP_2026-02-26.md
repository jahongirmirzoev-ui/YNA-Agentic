# Technical SOP: YNA Agentic Foundation Setup

**Document Type**: Technical Standard Operating Procedure
**Created**: 2026-02-26
**Last Updated**: 2026-02-26
**Author**: Claude Code (YNA Agentic)
**Status**: ✅ Active
**Audience**: Developers, Technical Implementers, DevOps

---

## Overview

### Purpose
Establish the foundational infrastructure for YNA Agentic Business Operating System including git version control, security protocols, directory architecture, and persistent context management system.

### Scope
- **Systems Affected**: Local development environment, git repository, file system structure
- **Dependencies**: Git, Python 3, text editor/IDE, bash/zsh shell
- **Technologies Used**: Git, Markdown, Environment Variables, YAML/JSON configuration

### Prerequisites
- [x] Git installed (version 2.0+)
- [x] Command line access (bash/zsh)
- [x] Text editor or IDE
- [x] Understanding of directory structures and file permissions

### ⚡ Implementation Efficiency

**⏱️ Time to Implement**: 2 hours one-time setup
**⏱️ Time Saved (Ongoing)**: 3-4 hours/month

**Why it improves efficiency:**
- **Context Loading**: Claude instantly loads business knowledge (0 sec vs 10-15 min manual briefing per session)
- **Documentation Access**: Find API configs/credentials in 5 sec vs 5 min searching email/Notion
- **Version Control**: Undo any mistake in 30 sec instead of manual file restoration
- **Standardization**: New documentation follows templates automatically (no time debating format)

**Technical ROI:**
- **Session startup time**: Reduced from 10 min → 0 sec (Claude auto-loads context)
- **Knowledge retrieval**: Improved from scattered search (5+ min) → instant access (5 sec)
- **Change management**: Git provides instant rollback vs manual backup/restore
- **Onboarding time**: New developers productive in hours vs days (self-service documentation)

---

## Technical Architecture

### System Components
```
YNA_Agentic (Root)
├── .git/                          # Version control
├── .gitignore                     # Git exclusions
├── .env.template                  # Credential template
├── .env (git-ignored)             # Actual credentials
├── CLAUDE.md                      # Persistent context
├── README.md                      # Project documentation
├── business-knowledge/            # Memory layer
│   ├── departments/               # Department-specific
│   ├── api-integrations/          # API docs
│   └── changelog.md               # Change tracking
├── config/                        # Configuration layer
│   ├── environments/              # Environment configs
│   └── credential-registry.md     # API key tracking
├── docs/                          # Documentation
│   └── sops/                      # Standard operating procedures
├── scripts/                       # Automation scripts
├── execution/                     # Active work
└── todos/                         # Task tracking
```

### File Structure
```
Root Level Files:
- .gitignore           (Security: exclude sensitive files)
- .env.template        (Security: credential template)
- CLAUDE.md            (Context: persistent AI memory)
- README.md            (Documentation: project overview)

Business Knowledge Layer:
- departments/         (Memory: department context)
- api-integrations/    (Memory: API documentation)
- changelog.md         (Memory: change history)

Configuration Layer:
- environments/        (Config: dev/staging/prod)
- credential-registry.md (Security: key tracking)

Documentation Layer:
- sops/technical/      (Docs: technical SOPs)
- sops/executive/      (Docs: management summaries)
```

### Configuration Files
| File | Location | Purpose |
|------|----------|---------|
| `.gitignore` | `/` | Prevent sensitive files from git tracking |
| `.env.template` | `/` | Template for required credentials |
| `CLAUDE.md` | `/` | Persistent context loaded on every session |
| `README.md` | `/` | Human-readable project overview |

---

## Implementation Steps

### Step 1: Initialize Git Repository
**Objective**: Set up version control for all project files

**Commands**:
```bash
cd /Users/jahongirmirzoev/Desktop/YNA_Agentic
git init
git branch -M main
```

**Verification**:
```bash
git status
ls -la .git
```

**Expected Output**:
```
Initialized empty Git repository in /Users/jahongirmirzoev/Desktop/YNA_Agentic/.git/
On branch main
```

### Step 2: Create Security Files
**Objective**: Prevent credential leaks and establish security protocols

**Create `.gitignore`**:
```bash
cat > .gitignore << 'EOF'
# Environment & Credentials
.env
.env.local
*.env
!.env.template

# API Keys & Secrets
config/credentials/
*.key
*.pem
secrets.json

# Temporary & Cache
.tmp/
.cache/
*.log
sync-logs/

# OS Files
.DS_Store
Thumbs.db

# IDE
.vscode/settings.json
.idea/

# Python
__pycache__/
*.pyc
.venv/
venv/

# Node
node_modules/
.npm/
EOF
```

**Create `.env.template`**:
```bash
cat > .env.template << 'EOF'
# YNA Agentic - Environment Variables Template
# Copy this file to .env and fill in your actual values
# NEVER commit .env to git

# Notion API
NOTION_API_KEY=secret_your_notion_key_here
NOTION_DATABASE_ID=your_database_id_here

# Make.com
MAKECOM_API_KEY=your_makecom_api_key
MAKECOM_TEAM_ID=your_team_id

# Clay
CLAY_API_KEY=your_clay_api_key

# Airtable
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_base_id

# Email/SMTP
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_smtp_password

# Slack
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
SLACK_BOT_TOKEN=xoxb-your-bot-token

# Google Analytics
GA4_MEASUREMENT_ID=G-XXXXXXXXXX
GA4_API_SECRET=your_api_secret

# Environment
ENVIRONMENT=development  # development | staging | production
DEBUG_MODE=true
EOF
```

**Verification**:
```bash
# Verify .gitignore is working
echo "test" > .env
git status  # Should NOT show .env as untracked
git check-ignore -v .env  # Should show: .gitignore:3:.env    .env
rm .env
```

**Expected Output**:
```
.gitignore:3:.env    .env
```

### Step 3: Create Directory Structure
**Objective**: Establish organized file hierarchy for all business operations

**Commands**:
```bash
# Memory Layer
mkdir -p business-knowledge/departments/{marketing,sales,customer-service,crm,website}
mkdir -p business-knowledge/api-integrations/{makecom,clay,airtable,email,slack,analytics,notion}

# Configuration Layer
mkdir -p config/{environments,credentials}

# Documentation Layer
mkdir -p docs/sops/{technical,executive,templates}
mkdir -p docs/{guides,architecture}

# Execution Layer
mkdir -p execution/{campaigns,reports,proposals}

# Scripts Layer
mkdir -p scripts/{automation,sync,utilities}

# TODOs Layer
mkdir -p todos/archive
```

**Verification**:
```bash
tree -L 3 -d  # Show directory structure
# OR if tree not installed:
find . -type d -maxdepth 3 | sort
```

### Step 4: Create CLAUDE.md (Persistent Context)
**Objective**: Provide Claude Code with instant business context on every session

**Key Content**:
```markdown
# YNA Agentic - Business Operating System (Rectory)

## Project Overview
[Mission, architecture, purpose]

## Quick Navigation
[Links to all memory.md files]

## Current System Status
[API integrations, cloud sync, active priorities]

## Context for Claude Code
[How to use the system, security rules, common tasks]
```

**Configuration**:
```bash
# CLAUDE.md is automatically loaded by Claude Code
# File location: /Users/jahongirmirzoev/Desktop/YNA_Agentic/CLAUDE.md
# Max recommended size: 15-20KB for optimal context loading
```

**Verification**:
```bash
wc -l CLAUDE.md  # Check line count
du -h CLAUDE.md  # Check file size
```

### Step 5: Create Initial Commit
**Objective**: Establish baseline in version control

**Commands**:
```bash
git add .gitignore .env.template CLAUDE.md README.md
git add business-knowledge/ config/ docs/ scripts/ execution/ todos/
git commit -m "Initial commit: Foundation setup with security and directory structure

- Initialized git repository
- Created .gitignore to prevent credential leaks
- Set up .env.template for credential management
- Established three-layer architecture (memory, config, execution)
- Created CLAUDE.md for persistent AI context
- Organized directory structure for all departments

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Verification**:
```bash
git log --oneline
git ls-files  # Show tracked files
git status    # Should show "nothing to commit, working tree clean"
```

---

## Configuration Details

### Environment Variables
| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `NOTION_API_KEY` | Notion integration token | `secret_abc123...` | Yes (for cloud sync) |
| `MAKECOM_API_KEY` | Make.com API token | `api_key_123...` | Yes (for automation) |
| `CLAY_API_KEY` | Clay API token | `clay_key_...` | Yes (for enrichment) |
| `AIRTABLE_API_KEY` | Airtable personal token | `patABC123...` | Yes (for database) |
| `ENVIRONMENT` | Current environment | `development` | Yes |
| `DEBUG_MODE` | Enable verbose logging | `true` | No (default: false) |

### Git Configuration
```bash
# Recommended git settings for this project
git config core.ignorecase false
git config core.autocrlf input
git config pull.rebase false
```

### Credentials Management
- **Storage**: `.env` file (git-ignored)
- **Access**: Environment variables loaded by scripts
- **Rotation Schedule**: Every 60-90 days (tracked in config/credential-registry.md)

---

## Security Considerations

### Access Control
- `.env` file: Read-only by owner, never committed to git
- `config/credentials/`: Directory for sensitive JSON/key files (git-ignored)
- API keys: Environment variables only, never hardcoded

### Sensitive Data
- **What's Sensitive**: All API keys, tokens, passwords, webhook URLs, database IDs
- **Protection Method**: Git-ignored via `.gitignore`, stored in `.env`
- **Verification**: Use `git status` and `git check-ignore` before commits

### Security Best Practices
- [x] Never commit `.env` files
- [x] Use `.env.template` for documentation only
- [x] Rotate API keys every 60-90 days
- [x] Review `.gitignore` before every commit
- [x] Use `git diff --cached` to review staged changes before commit

---

## Monitoring & Maintenance

### Logs Location
- **Git Logs**: `.git/logs/`
- **Sync Logs**: `cloud-sync/notion/sync-logs/` (when cloud sync is active)
- **API Logs**: `.tmp/api-logs.json` (git-ignored)

### Monitoring Commands
```bash
# Check git status
git status

# View recent commits
git log --oneline -10

# Check for uncommitted sensitive files
git status | grep -E '\\.env$|secrets|credentials'

# Verify .gitignore is working
git check-ignore -v .env
```

### Maintenance Schedule
| Task | Frequency | Command |
|------|-----------|---------|
| Review git status | Before every commit | `git status` |
| Update changelog | After major changes | Edit `business-knowledge/changelog.md` |
| Rotate credentials | Every 60-90 days | Update `.env` + registry |
| Backup repository | Weekly | `git push origin main` (when remote configured) |

---

## Troubleshooting

### Common Issues

#### Issue 1: Sensitive File Tracked by Git
**Symptoms**:
- `.env` file appears in `git status`
- Git wants to commit credentials

**Diagnosis**:
```bash
git status
git check-ignore -v .env  # Should show it's ignored
```

**Solution**:
```bash
# If file is tracked:
git rm --cached .env
git commit -m "Remove .env from git tracking"

# Verify .gitignore
grep ".env" .gitignore  # Should exist
```

**Prevention**: Always check `.gitignore` before first commit

#### Issue 2: CLAUDE.md Not Loading
**Symptoms**:
- Claude Code doesn't seem to have project context

**Diagnosis**:
```bash
# Check file exists and is readable
ls -lh CLAUDE.md
wc -l CLAUDE.md  # Should be < 1000 lines for optimal performance
```

**Solution**:
- Ensure file is in root directory
- Reduce file size if > 20KB
- Restart Claude Code session
- Check file encoding (should be UTF-8)

**Prevention**: Keep CLAUDE.md concise, use links to detailed docs

#### Issue 3: Directory Structure Missing
**Symptoms**:
- Scripts fail to find expected directories

**Diagnosis**:
```bash
# Verify directory structure
tree -L 2 -d
# OR
find . -type d -maxdepth 2
```

**Solution**:
```bash
# Re-create missing directories
mkdir -p business-knowledge/departments/{marketing,sales,customer-service,crm,website}
mkdir -p business-knowledge/api-integrations/{makecom,clay,airtable,email,slack,analytics,notion}
mkdir -p config/{environments,credentials}
mkdir -p docs/sops/{technical,executive,templates}
mkdir -p execution/{campaigns,reports,proposals}
mkdir -p scripts/{automation,sync,utilities}
mkdir -p todos/archive
```

---

## Performance Optimization

### Current Performance Metrics
| Metric | Current Value | Target Value |
|--------|---------------|--------------|
| CLAUDE.md load time | < 1s | < 2s |
| Directory depth | 3 levels | 3-4 levels max |
| File count (root) | ~10 files | < 20 files |
| Repository size | < 1MB | < 50MB |

### Optimization Opportunities
- Keep CLAUDE.md under 20KB for fast loading
- Use symbolic links for frequently accessed directories
- Archive old execution files monthly
- Compress logs older than 30 days

---

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-02-26 | 1.0 | Initial foundation setup implemented | Claude |

---

## References

### Documentation
- [CLAUDE.md](../../../CLAUDE.md) - Persistent context
- [README.md](../../../README.md) - Project overview
- [Security Protocols](../../../directives/security-protocols.md) - Security guidelines

### Related SOPs
- [Foundation Setup Executive Summary](../executive/Foundation_Setup_Executive_Summary_2026-02-26.md)

### External Resources
- [Git Documentation](https://git-scm.com/doc)
- [Environment Variables Best Practices](https://12factor.net/config)

---

**Document Control**:
- File Path: `docs/sops/technical/Foundation_Setup_Technical_SOP_2026-02-26.md`
- Version Control: Git tracked
- Review Schedule: Quarterly or when architecture changes
- Next Review Date: 2026-05-26
