# YNA Agentic - TODO List

**Last Updated**: 2026-02-26 (Post-Privacy Policy Deployment)

---

## 🔴 High Priority

### ICP Clarity Website (Immediate User Actions)
- [x] **🤖 Set up Google Analytics 4 tracking** - GA4 code added to both pages (2026-02-26)
- [x] **🤖 Create privacy policy page** - Swedish GDPR-compliant, YNA AB info added (2026-02-26)
- [x] **🤖 Deploy to production** - Live at icpclarity.com with privacy policy v2.0 (2026-02-26)
- [ ] **👤 Replace GA4 placeholder ID** - Change `G-XXXXXXXXXX` to real Measurement ID in index.html & assessment.html
- [ ] **👤 Test live website** - Verify privacy policy, links, GA4 tracking at icpclarity.com
- [ ] **👤 Create favicon images** - 16x16, 32x32, 180x180 PNG files (guide: FAVICON-CREATION-GUIDE.md)
- [ ] **👤 Create OG image** - 1200x630 JPG for social sharing (template in guide)

### Business Operations (Foundation - Priority 1)
- [ ] **🤖 Document existing Make.com scenarios** - List all active scenarios with purpose and connections
- [ ] **🤖 Document Clay tables** - Inventory tables, fields, and automations
- [ ] **🤖 Document Airtable bases** - Schema, views, and integrations
- [ ] **🤖 Populate department memory.md files** - Add current state for all 5 departments (Marketing, Sales, Customer Service, CRM, Website)
- [ ] **👤 Set up Notion API integration** - Configure credentials and test connection (then enables cloud sync)

---

## 🟡 Medium Priority

### API Integrations
- [ ] **🤖 Configure Email/SMTP integration** - Set up credentials and test sending (for privacy contact form)
- [ ] **🤖 Set up Slack webhooks** - Configure notifications and channels (document existing webhooks)
- [ ] **👤 Configure Analytics (GA4) dashboard** - Set up GA4 account and grant access after ID replacement
- [ ] **🤖 Create cloud sync automation** - Set up 15-minute cron job for Notion sync (after Notion API configured)

### Documentation & SOPs
- [ ] **🤖 Create SOP: Privacy Policy Deployment** - Document privacy policy v2.0 implementation process
- [ ] **🤖 Document webhook registry** - Inventory all active webhooks (Make.com, Clay, Assessment form)
- [ ] **🤖 Create API integration map** - Visual diagram showing data flow between all systems

---

## 🟢 Low Priority / Future

- [ ] **Create department templates** - Campaign, report, and SOP templates
- [ ] **Set up webhook monitoring** - Track API call volumes and errors
- [ ] **Build data flow visualization** - Diagram showing all integration connections
- [ ] **Create onboarding documentation** - How to use this system for new team members
- [ ] **Set up automated testing** - Test API connections and sync operations

---

## 📋 Standard Operating Procedures

**IMPORTANT**: After completing any major task or project milestone, Claude will automatically create two SOPs:

1. **Technical SOP** (`docs/sops/technical/`) - Detailed technical implementation guide for developers
2. **Executive SOP** (`docs/sops/executive/`) - Plain-English summary for management and non-technical stakeholders

**Completed SOPs**:
- ✅ Foundation Setup (2026-02-26)
- ✅ ICP Clarity Website Documentation & GA4 (2026-02-26)
- 🔄 Privacy Policy v2.0 Deployment (2026-02-26) - *Pending SOP creation*

**Templates Available**:
- [docs/sops/templates/TECHNICAL_SOP_TEMPLATE.md](../docs/sops/templates/TECHNICAL_SOP_TEMPLATE.md)
- [docs/sops/templates/EXECUTIVE_SOP_TEMPLATE.md](../docs/sops/templates/EXECUTIVE_SOP_TEMPLATE.md)

**Full Overview**:
- [docs/SOP_CREATION_SUMMARY.md](../docs/SOP_CREATION_SUMMARY.md) - Complete SOP system documentation

---

## ✅ Completed

### 2026-02-26
- [x] Initial Rectory structure created
- [x] Security files configured (.gitignore, .env.template)
- [x] Git repository initialized
- [x] CLAUDE.md created for persistent context
- [x] Created TODO tracking system
- [x] **ICP Clarity Website - Complete documentation created**
  - Website overview (40+ pages)
  - Webhooks & integrations documentation
  - Site architecture documentation
  - Updated website department memory.md
- [x] **ICP Clarity Website - GA4 tracking implemented**
  - Tracking code added to index.html and assessment.html
  - Custom events configured (CTA clicks, pricing card clicks)
  - Created ga4-setup-instructions.md guide
  - Created ga4-assessment-events.js for future implementation
- [x] **ICP Clarity Website - Privacy policy v2.0 deployed (2026-02-26)**
  - Swedish GDPR-compliant privacy-policy.html (Dataskyddslag 2018:218)
  - YNA AB company information: Org# 559508-0770, Jakobsbergsgatan 24, Stockholm
  - Legal basis mapping for all processing activities (GDPR Art. 6)
  - 7-year retention policy (Bokföringslagen 2010:1142)
  - IMY (Swedish Data Protection Authority) contact details
  - Standard Contractual Clauses for US data transfers
  - Service provider documentation (Make.com EU2, Clay, Airtable, Slack)
  - Deployed live to icpclarity.com via Netlify
- [x] **Infrastructure - Credential registry created**
  - Template for tracking API keys and rotation schedules
  - Documented all services (Make.com, Clay, Airtable, Notion, GA4, Email/SMTP, Slack)
  - Located at config/credential-registry.md
- [x] **Infrastructure - CLAUDE.md maintenance directive created**
  - SOP for maintaining CLAUDE.md as single source of truth
  - Update procedures and quality checklist
  - Located at directives/claude-md-maintenance.md
- [x] **Documentation - SOP System Created (2026-02-26)**
  - Created comprehensive SOP templates (technical + executive)
  - Generated Technical SOP: Foundation Setup (15+ pages)
  - Generated Executive SOP: Foundation Setup (management-friendly)
  - Generated Technical SOP: ICP Clarity Website & GA4 (20+ pages)
  - Generated Executive SOP: ICP Clarity Website & GA4 (business-focused)
  - All SOPs located in docs/sops/ with templates for future use

---

## How to Use This TODO List

**For You:**
- Check boxes as you complete tasks
- Add new items as needed (or ask Claude to add them)
- Move completed items to archive when list gets long

**For Claude:**
- Proactively suggest adding items during sessions
- Update checkboxes when tasks are completed
- Move completed items to ✅ section with date
- Suggest re-prioritization when priorities shift
- **Automatically create SOPs after major task completion** (Technical + Executive versions)

**Icons:**
- 🤖 = Claude can do autonomously
- 👤 = Requires user input/credentials
- 🔴 = High priority (do now)
- 🟡 = Medium priority (do soon)
- 🟢 = Low priority (future)

---

## Archive

When the Completed section gets too long, move old items to [archive/](archive/) by month.
