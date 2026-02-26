# Airtable Bases Inventory

*Last Updated: 2026-02-26*

## Overview

This document catalogs all Airtable bases and their table structures.

---

## Active Bases

**Action Required**: Log into your Airtable account and document all bases below.

### Template Format

```markdown
## Base Name: [Name]

**Base ID**: app[XXXXXXXXXXXXX]
**Purpose**: [What this base manages]
**Created**: [Date]
**Owner**: [Team/Person]
**Shared With**: [List of users/teams]
**Connected Integrations**: Clay, Make.com, etc.

### Tables

#### Table: [Table Name]
**Primary Field**: [Field name]
**Record Count**: [Number]

**Fields**:
| Field Name | Type | Purpose | Required | Default |
|-----------|------|---------|----------|---------|
| [Field 1] | Text/Number/etc. | [Purpose] | Yes/No | [Value] |

**Views**:
- [View 1]: [Purpose and filters]
- [View 2]: [Purpose and filters]

**Automations**:
- [Automation 1]: [What it does]

**Webhooks**:
- [Webhook to Make.com]: [Trigger condition]

---
```

---

## Base Categories

### CRM & Sales
| Base Name | Tables | Purpose | Integrations | Records |
|-----------|--------|---------|--------------|----------|
| *To be documented* | - | - | - | - |

### Marketing
| Base Name | Tables | Purpose | Integrations | Records |
|-----------|--------|---------|--------------|----------|
| *To be documented* | - | - | - | - |

### Customer Service
| Base Name | Tables | Purpose | Integrations | Records |
|-----------|--------|---------|--------------|----------|
| *To be documented* | - | - | - | - |

### Operations
| Base Name | Tables | Purpose | Integrations | Records |
|-----------|--------|---------|--------------|----------|
| *To be documented* | - | - | - | - |

---

## Common Table Patterns

### Contacts Table
Standard fields:
- Email (Email type)
- First Name (Text)
- Last Name (Text)
- Company (Linked to Companies table)
- Status (Single select)
- Created Date (Created time)

### Companies Table
Standard fields:
- Company Name (Text)
- Domain (URL)
- Industry (Single select)
- Size (Single select)
- Contacts (Linked to Contacts table)

### Deals/Opportunities Table
Standard fields:
- Deal Name (Text)
- Company (Linked to Companies)
- Contact (Linked to Contacts)
- Stage (Single select)
- Value (Currency)
- Close Date (Date)
- Owner (Collaborator)

---

## Field Naming Conventions

**Consistency is Key**:
- ✅ Use: "Email", "First Name", "Company Name"
- ❌ Avoid: "email", "firstname", "company_name"

**Field Types**:
- Email addresses: Use Email type (not Text)
- Phone numbers: Use Phone number type
- Dates: Use Date type
- Links: Use URL type
- Money: Use Currency type

---

## Integration Points

### Clay → Airtable
Tables receiving data from Clay:
- [Table]: [What data]

### Airtable → Make.com
Tables with webhook triggers:
- [Table]: [Trigger conditions]

### Airtable ← Make.com
Tables updated by Make.com:
- [Table]: [What updates]

---

## Next Steps

1. Log into Airtable
2. List all bases
3. For each base:
   - Document tables and fields
   - Note views and automations
   - Identify integrations
4. Create schema diagrams for complex bases
5. Keep this inventory updated

---

*This inventory is critical for understanding data architecture - keep it current!*
