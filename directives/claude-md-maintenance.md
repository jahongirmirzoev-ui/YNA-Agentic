# CLAUDE.md Maintenance Directive

*Last Updated: 2026-02-26*

---

## Purpose

This directive establishes the standard operating procedure for maintaining `CLAUDE.md` - the primary context file that Claude reads on every session start.

**Why This Matters**: CLAUDE.md is the single source of truth for the entire YNA Agentic system. Keeping it current ensures Claude always has accurate context without requiring users to repeat information.

---

## CLAUDE.md Structure Overview

The file is organized in sections:

1. **Project Overview** - Mission, architecture, current system
2. **Quick Navigation** - Links to department memory files and API docs
3. **Directives** - Security protocols, SOPs, documentation standards
4. **Current System Status** - Cloud sync, API integrations, active priorities
5. **Context for Claude** - How to use the system, common tasks
6. **Critical Directives** - Security rules, sync rules, documentation standards
7. **Environment Setup** - Current environment, available environments
8. **Common Tasks** - Step-by-step how-to guides
9. **Recent Changes** - What was updated and when
10. **Key Files Reference** - Department-specific file locations
11. **Troubleshooting** - Common issues and solutions

---

## When to Update CLAUDE.md

### ✅ Always Update When:

1. **New Department Files Created**
   - Add links in "Quick Navigation" section
   - Update "Department Memory Files" list
   - Add to "Key Files Reference"

2. **API Integration Changes**
   - Update "Current System Status" → "API Integrations Status" table
   - Add new platform to "API Integration Documentation" section
   - Update integration flows if data flow changes

3. **New Priorities Established**
   - Update "Active Priorities" section
   - Mark completed priorities as done
   - Add new priority tasks

4. **Major Milestones Completed**
   - Update phase status (✅ complete, 🔄 in progress, ⏸️ pending)
   - Add to "Recent Changes" section with date
   - Update "Current System Status"

5. **File Locations Change**
   - Update all affected links
   - Verify links work (check file paths)
   - Update navigation sections

6. **New Directives Created**
   - Add link in "Directives" section
   - Briefly describe what it covers
   - Update "Critical Directives" if it's a key security/process rule

### ⚠️ Consider Updating When:

1. **Department Context Shifts** - Major changes to a department's operations
2. **Integration Status Changes** - API goes from active to paused, or vice versa
3. **Troubleshooting Solutions Found** - New common issues discovered
4. **Workflow Optimizations** - Better ways to do common tasks

### ❌ Don't Update For:

1. **Minor Edits** - Small typo fixes in other files
2. **Temporary Status** - Short-term blockers or one-time issues
3. **Session-Specific Info** - What Claude is currently working on
4. **Redundant Information** - Things already documented in linked files

---

## Update Procedures

### Standard Update Pattern

```markdown
## Step 1: Identify What Changed
Document the change:
- What file/system/integration changed?
- Is it a new capability, update, or removal?
- Is this temporary or permanent?

## Step 2: Determine Impact on CLAUDE.md
Ask:
- Does this affect Claude's ability to help users?
- Will Claude need this info to answer common questions?
- Does this change navigation or file locations?

## Step 3: Update Relevant Section(s)
- Update the specific section (e.g., "API Integrations Status")
- Update cross-references if needed
- Add to "Recent Changes" with date

## Step 4: Verify Links
- Check all modified links point to correct files
- Ensure file paths are accurate
- Test that referenced files exist

## Step 5: Update "Last Updated" Date
- Change date at top of CLAUDE.md
- Add entry to "Recent Changes" section
```

---

## Section-Specific Maintenance

### Quick Navigation Section

**Update When**:
- New department memory file created
- New API integration platform added
- New directive created

**How to Update**:
```markdown
## Quick Navigation

### Department Memory Files (READ THESE FOR CONTEXT)
- **Marketing**: [business-knowledge/departments/marketing/memory.md]
- **Sales**: [business-knowledge/departments/sales/memory.md]
- **[New Department]**: [path/to/memory.md]  <-- Add here

### API Integration Documentation
- **[New Platform]**: [path/to/docs/memory.md]  <-- Add here
```

---

### Current System Status Section

**Update When**:
- Cloud sync status changes
- API integration status changes
- Active priorities shift

**How to Update**:

```markdown
## Current System Status

### Cloud Sync
- **Status**: [Update status: ✅ Active | 🔄 In Progress | 🟡 Setup | 🔴 Issue]
- **Last Sync**: [Update timestamp]

### API Integrations Status

| Platform | Status | Active Resources | Last Updated |
|----------|--------|------------------|--------------|
| Make.com | ✅ Active | 12 scenarios | 2026-02-26 |  <-- Update this
| [New Platform] | 🟡 Setup | TBD | 2026-02-26 |  <-- Add new rows
```

---

### Recent Changes Section

**Update When**: Every time you make a significant change to the system

**How to Update**:
```markdown
## Recent Changes

**2026-02-26**:  <-- Always use current date
- ✅ [What was accomplished]
- ✅ [Another accomplishment]
- 🔄 [What's in progress]
- 🔄 [Another in-progress item]

**[Previous dates below]**
```

**Keep Recent**: Only keep last 30 days of changes. Archive older changes to `business-knowledge/changelog.md`.

---

### Active Priorities Section

**Update When**: Priorities change (new goals, completed goals, shifted focus)

**How to Update**:
```markdown
### Active Priorities
1. [Current top priority]
2. [Next priority]
3. [Third priority]
4. ...

**Mark completed items** and move them to "Recent Changes":
1. ~~Complete Rectory structure~~ ✅ Completed 2026-02-26
```

---

## Quality Checklist

Before saving CLAUDE.md updates, verify:

- [ ] All file path links are correct and use absolute paths from project root
- [ ] Dates are current (format: YYYY-MM-DD)
- [ ] Status indicators are accurate (✅ 🔄 🟡 🔴 ⏸️)
- [ ] Recent Changes section is updated
- [ ] "Last Updated" date at top is current
- [ ] No duplicate information (check if it's better in a linked file)
- [ ] Grammar and formatting are clean
- [ ] New sections follow existing style/structure

---

## File Path Best Practices

### ✅ Good Path Formats

```markdown
- [marketing/memory.md](business-knowledge/departments/marketing/memory.md)
- [API Hub](business-knowledge/api-integrations/README.md)
- [Security Protocols](directives/security-protocols.md)
```

### ❌ Bad Path Formats

```markdown
- [marketing/memory.md](../business-knowledge/departments/marketing/memory.md)  ← Relative paths
- [API Hub](api-integrations/README.md)  ← Missing base directory
- [Security](directives/security-protocols.md) (To be created)  ← Don't add if not created yet
```

**Rule**: Use absolute paths from project root. Remove `(To be created)` tags once files exist.

---

## Maintenance Schedule

### Daily (If Major Work Done)
- Update "Recent Changes" with today's accomplishments
- Update status indicators if integrations/priorities changed

### Weekly
- Review "Active Priorities" - still accurate?
- Check if any "In Progress" items should be "Complete" or "Paused"
- Verify API integration statuses are current

### Monthly
- Archive old "Recent Changes" (>30 days) to `business-knowledge/changelog.md`
- Review entire CLAUDE.md for outdated information
- Check all file path links still work
- Update integration usage statistics if available

### Quarterly
- Full CLAUDE.md audit for accuracy
- Reorganize sections if structure no longer fits
- Update mission/overview if business focus has shifted

---

## Common Update Scenarios

### Scenario 1: New Department Memory File Created

```markdown
1. Open CLAUDE.md
2. Find "Quick Navigation" → "Department Memory Files"
3. Add new department in alphabetical order:
   - **[Department Name]**: [path/to/memory.md]
4. Find "Key Files Reference" section
5. Add new department's key files
6. Update "Recent Changes":
   - ✅ Created [Department] memory file and documentation
7. Update "Last Updated" date at top
```

### Scenario 2: API Integration Goes Live

```markdown
1. Open CLAUDE.md
2. Find "Current System Status" → "API Integrations Status" table
3. Change status from 🟡 Setup to ✅ Active
4. Update "Active Resources" column (e.g., "3 scenarios active")
5. Update "Last Updated" column with current date
6. Update "Recent Changes":
   - ✅ [Platform] integration deployed and active
7. Update "Last Updated" date at top
```

### Scenario 3: Priority Completed

```markdown
1. Open CLAUDE.md
2. Find "Active Priorities" section
3. Mark completed item:
   - ~~Complete cloud sync setup~~ ✅ Completed 2026-02-26
4. Optionally remove from list if no longer relevant
5. Update "Recent Changes":
   - ✅ Cloud sync with Notion fully operational
6. Update implementation status in "Implementation Status" section
7. Update "Last Updated" date at top
```

---

## Integration with Notion Sync

When cloud sync is active, CLAUDE.md changes will:
- ✅ Sync TO Notion every 15 minutes
- ✅ Sync FROM Notion if edited there
- ⚠️ Last-write-wins conflict resolution
- 🔄 Sync logs available in `cloud-sync/notion/sync-logs/`

**Best Practice**: Make CLAUDE.md edits locally (in repo), not in Notion, to avoid sync conflicts.

---

## Notes for Claude

### Proactive Updates

Claude should **automatically update CLAUDE.md** when:
1. Creating new department memory files
2. Completing major milestones (e.g., "Website documentation complete")
3. Changing API integration status
4. Discovering that CLAUDE.md contains outdated information

Claude should **ask before updating CLAUDE.md** when:
1. User priorities have shifted (confirm with user first)
2. Structural changes needed (reorganizing sections)
3. Information conflicts with what user has told Claude in current session

### Update Template

When updating CLAUDE.md, Claude should:
1. Read current CLAUDE.md first
2. Identify the specific section(s) to update
3. Make targeted edits (don't rewrite entire file)
4. Update "Recent Changes" with summary
5. Update "Last Updated" date at top
6. Inform user what was updated

---

## Version Control

CLAUDE.md is tracked in Git:
- ✅ Commit CLAUDE.md updates with clear messages
- ✅ Use descriptive commit messages (e.g., "Update CLAUDE.md: Mark cloud sync as active")
- ❌ Don't bundle CLAUDE.md changes with unrelated commits
- ✅ Review diff before committing to ensure accuracy

**Example Commit**:
```bash
git add CLAUDE.md
git commit -m "Update CLAUDE.md: Added ICP Clarity website documentation links, marked GA4 setup complete"
```

---

## Troubleshooting

**Issue**: File path links broken
**Solution**: Use absolute paths from project root, verify files exist before adding links

**Issue**: CLAUDE.md getting too long
**Solution**: Move detailed documentation to linked files, keep CLAUDE.md as navigation/overview only

**Issue**: Sync conflicts with Notion
**Solution**: Edit CLAUDE.md locally only, check sync logs for conflicts, resolve manually if needed

**Issue**: Outdated information in CLAUDE.md
**Solution**: Review monthly, update as needed, ask user if uncertain about current state

---

## Summary

**Golden Rule**: CLAUDE.md should always reflect the **current** state of the YNA Agentic system.

**Update Frequency**: As needed when significant changes occur, minimum weekly review

**Keep It**: Concise, accurate, navigational (detailed docs go in linked files)

**Think of It As**: A table of contents + current status dashboard for the entire system

---

*This directive ensures CLAUDE.md remains the reliable single source of truth for every Claude Code session.*
