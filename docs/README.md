# Documentation Directory

This directory contains all documentation for the YNA Agentic Business Operating System.

## Directory Structure

```
docs/
├── README.md (this file)
├── SOP_CREATION_SUMMARY.md          # Index of all Standard Operating Procedures
├── migrations/                       # Platform & infrastructure migrations
│   ├── netlify-to-vercel/           # ICP Clarity website hosting migration
│   └── README.md                    # Migration documentation standards
├── session-summaries/               # AI session summaries and work logs
├── setup-guides/                    # Initial setup and configuration guides
│   └── MAKECOM_TOKEN_SETUP.md       # Make.com API setup
├── sops/                            # Standard Operating Procedures
│   ├── executive/                   # Management-friendly summaries
│   ├── technical/                   # Developer implementation guides
│   └── templates/                   # SOP templates for future use
└── time-tracking/                   # Time tracking documentation
    ├── TIME_TRACKING_QUICK_REFERENCE.md
    ├── TIME_TRACKING_IMPLEMENTATION_COMPLETE.md
    ├── MANAGEMENT_TIME_TRACKING.md
    ├── NOTION_TIME_TRACKING_SETUP.md
    └── TIME_TRACKING_SETUP.md
```

## Navigation Guide

### 📋 For Standard Operating Procedures
**Start here**: [SOP_CREATION_SUMMARY.md](SOP_CREATION_SUMMARY.md)

This master index lists all SOPs with:
- Technical SOPs for developers
- Executive summaries for management
- Current status and completion dates
- Direct links to all documentation

**Current SOPs** (145+ pages total):
1. **Foundation Setup** - Git, security, directory structure
2. **ICP Clarity Website & GA4** - Website documentation and analytics
3. **Netlify to Vercel Migration** - Hosting platform migration

### 🔄 For Migration Documentation
**Directory**: [migrations/](migrations/)

All platform migrations, infrastructure changes, and system transitions:
- [Netlify to Vercel Migration](migrations/netlify-to-vercel/) - ICP Clarity hosting migration (2026-02-27)

Each migration includes:
- Migration summary (chronological record)
- Cleanup guide (post-migration steps)
- Technical SOP (implementation details)
- Executive summary (business impact)

### 🚀 For Setup and Configuration
**Directory**: [setup-guides/](setup-guides/)

Initial setup guides for:
- API integrations (Make.com, Clay, etc.)
- Tool configurations
- Environment setup

### ⏱️ For Time Tracking
**Directory**: [time-tracking/](time-tracking/)

Complete time tracking system documentation:
- Quick reference guide
- Implementation details
- Management reports
- Notion integration setup

### 📝 For Session Summaries
**Directory**: [session-summaries/](session-summaries/)

AI conversation summaries and work session logs.

---

## Quick Links

### Most Referenced Documents
- [SOP Creation Summary](SOP_CREATION_SUMMARY.md) - Master index of all SOPs
- [Netlify to Vercel Migration](migrations/netlify-to-vercel/MIGRATION_SUMMARY.md) - Recent hosting migration
- [Time Tracking Quick Reference](time-tracking/TIME_TRACKING_QUICK_REFERENCE.md) - How to use time tracking

### By Audience

**For Developers**:
- [Technical SOPs](sops/technical/) - Implementation guides with code
- [Setup Guides](setup-guides/) - Configuration and API setup
- [Migration Technical Docs](migrations/) - Infrastructure changes

**For Management**:
- [Executive Summaries](sops/executive/) - Plain English overviews
- [SOP Creation Summary](SOP_CREATION_SUMMARY.md) - What's been built and ROI
- [Time Tracking Reports](time-tracking/) - Project hours and analytics

**For Team Members**:
- [SOP Creation Summary](SOP_CREATION_SUMMARY.md) - Start here to understand the system
- [Setup Guides](setup-guides/) - How to configure tools
- [Session Summaries](session-summaries/) - What was accomplished

---

## Documentation Standards

All documentation follows these standards:
- ✅ **Complete** - No missing steps or information
- ✅ **Accurate** - Reflects actual implementation
- ✅ **Actionable** - Reader can follow and reproduce
- ✅ **Clear** - Appropriate for target audience
- ✅ **Organized** - Consistent structure
- ✅ **Current** - Dated and version controlled
- ✅ **Referenced** - Links to related docs

For detailed standards, see [Documentation Standards](../directives/documentation-standards.md).

---

## Contributing

When creating new documentation:

1. **Choose the right directory**:
   - SOPs → `sops/technical/` or `sops/executive/`
   - Migrations → `migrations/[migration-name]/`
   - Setup → `setup-guides/`
   - Time tracking → `time-tracking/`

2. **Use templates**:
   - [Technical SOP Template](sops/templates/TECHNICAL_SOP_TEMPLATE.md)
   - [Executive SOP Template](sops/templates/EXECUTIVE_SOP_TEMPLATE.md)

3. **Update indexes**:
   - Add to [SOP_CREATION_SUMMARY.md](SOP_CREATION_SUMMARY.md)
   - Update this README if creating new categories

4. **Follow naming conventions**:
   - `[Subject]_[Type]_[Date].md` for dated docs
   - `README.md` for directory indexes
   - ALL_CAPS for important standalone docs

---

## Questions?

- **About a specific SOP**: Check [SOP_CREATION_SUMMARY.md](SOP_CREATION_SUMMARY.md)
- **About migrations**: See [migrations/README.md](migrations/README.md)
- **About documentation standards**: See [../directives/documentation-standards.md](../directives/documentation-standards.md)
- **About the system**: See [../CLAUDE.md](../CLAUDE.md) or [../README.md](../README.md)

---

*Last Updated: 2026-02-27*
