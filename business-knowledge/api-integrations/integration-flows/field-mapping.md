# Cross-Platform Field Mapping

*Last Updated: 2026-02-26*

## Overview

This document defines how fields map across Clay, Airtable, Notion, Make.com, and other platforms. Consistent field mapping ensures data integrity and smooth integration flows.

---

## Standard Contact/Lead Object

| Field Name | Clay | Airtable | Notion | Make.com Variable | Email Merge | Description |
|-----------|------|----------|--------|-------------------|-------------|-------------|
| Email | `email` | Email (Email type) | Email (Email) | `{{email}}` | `{{email}}` | Primary email address |
| First Name | `first_name` | First Name (Text) | First Name (Title) | `{{firstName}}` | `{{firstName}}` | Contact first name |
| Last Name | `last_name` | Last Name (Text) | Last Name (Text) | `{{lastName}}` | `{{lastName}}` | Contact last name |
| Full Name | `full_name` | Full Name (Formula) | Full Name (Formula) | `{{fullName}}` | `{{fullName}}` | Concatenated first + last |
| Company | `company` | Company (Linked Record) | Company (Relation) | `{{company}}` | `{{company}}` | Company name |
| Job Title | `job_title` | Job Title (Text) | Job Title (Text) | `{{jobTitle}}` | `{{title}}` | Professional title |
| Phone | `phone` | Phone (Phone type) | Phone (Phone) | `{{phone}}` | - | Phone number |
| LinkedIn | `linkedin_url` | LinkedIn (URL type) | LinkedIn (URL) | `{{linkedin}}` | - | LinkedIn profile URL |
| Status | `status` | Status (Single Select) | Status (Select) | `{{status}}` | - | Lead/customer status |
| Lead Score | `lead_score` | Lead Score (Number) | Lead Score (Number) | `{{leadScore}}` | - | Qualification score |
| Created Date | `created_at` | Created (Created time) | Created (Created time) | `{{createdDate}}` | - | Record creation timestamp |
| Updated Date | `updated_at` | Last Modified (Last modified) | Edited (Last edited) | `{{updatedDate}}` | - | Last update timestamp |

---

## Standard Company Object

| Field Name | Clay | Airtable | Notion | Make.com Variable | Description |
|-----------|------|----------|--------|-------------------|-------------|
| Company Name | `company_name` | Company Name (Text) | Company (Title) | `{{companyName}}` | Legal company name |
| Domain | `domain` | Domain (URL type) | Domain (URL) | `{{domain}}` | Company website |
| Industry | `industry` | Industry (Single Select) | Industry (Select) | `{{industry}}` | Business sector |
| Company Size | `company_size` | Size (Single Select) | Size (Select) | `{{companySize}}` | Employee count range |
| Revenue | `revenue` | Revenue (Currency) | Revenue (Number) | `{{revenue}}` | Annual revenue |
| Funding | `funding` | Funding (Currency) | Funding (Number) | `{{funding}}` | Total funding raised |
| Founded Year | `founded_year` | Founded (Number) | Founded (Number) | `{{foundedYear}}` | Year established |
| Location | `location` | Location (Text) | Location (Text) | `{{location}}` | HQ location |
| Description | `description` | Description (Long Text) | Description (Text) | `{{description}}` | Company description |

---

## Status Values Mapping

Consistent status values across platforms:

| Stage | Clay | Airtable | Notion | Meaning |
|-------|------|----------|--------|---------|
| New | `new` | New Lead | 🆕 New | Just captured, not yet contacted |
| Contacted | `contacted` | Contacted | 📧 Contacted | Initial outreach made |
| Qualified | `qualified` | Qualified | ✅ Qualified | Meets qualification criteria |
| Opportunity | `opportunity` | Opportunity | 💼 Opportunity | Active sales opportunity |
| Customer | `customer` | Customer | 🎉 Customer | Closed won, active customer |
| Lost | `lost` | Closed Lost | ❌ Lost | Opportunity lost |
| Unqualified | `unqualified` | Unqualified | ⛔ Unqualified | Does not meet criteria |

---

## Deal/Opportunity Object

| Field Name | Airtable | Notion | Make.com Variable | Description |
|-----------|----------|--------|-------------------|-------------|
| Deal Name | Deal Name (Text) | Deal (Title) | `{{dealName}}` | Descriptive deal name |
| Company | Company (Linked Record) | Company (Relation) | `{{company}}` | Associated company |
| Contact | Contact (Linked Record) | Contact (Relation) | `{{contact}}` | Primary contact |
| Stage | Stage (Single Select) | Stage (Select) | `{{stage}}` | Sales pipeline stage |
| Value | Value (Currency) | Value (Number) | `{{dealValue}}` | Deal amount |
| Close Date | Close Date (Date) | Close Date (Date) | `{{closeDate}}` | Expected close date |
| Owner | Owner (Collaborator) | Owner (Person) | `{{owner}}` | Sales rep responsible |
| Probability | Probability (Number 0-100) | Probability (Number) | `{{probability}}` | Win probability % |

---

## Pipeline Stage Mapping

| Stage Number | Stage Name | Airtable | Probability | Typical Actions |
|-------------|-----------|----------|-------------|-----------------|
| 1 | Prospecting | Prospecting | 10% | Research, initial outreach |
| 2 | Qualification | Qualified | 25% | BANT qualification |
| 3 | Demo/Presentation | Demo Scheduled | 40% | Product demonstration |
| 4 | Proposal | Proposal Sent | 60% | Customized proposal |
| 5 | Negotiation | Negotiating | 75% | Contract discussion |
| 6 | Closed Won | Closed Won | 100% | Customer onboarding |
| 7 | Closed Lost | Closed Lost | 0% | Loss analysis |

---

## Support Ticket Object

| Field Name | Airtable | Make.com Variable | Description |
|-----------|----------|-------------------|-------------|
| Ticket ID | Ticket ID (Autonumber) | `{{ticketId}}` | Unique ticket number |
| Subject | Subject (Text) | `{{subject}}` | Ticket subject line |
| Description | Description (Long Text) | `{{description}}` | Full ticket details |
| Customer | Customer (Linked Record) | `{{customer}}` | Associated customer |
| Status | Status (Single Select) | `{{status}}` | Open/In Progress/Resolved/Closed |
| Priority | Priority (Single Select) | `{{priority}}` | Low/Medium/High/Urgent |
| Assigned To | Assigned To (Collaborator) | `{{assignedTo}}` | Support agent |
| Created Date | Created (Created time) | `{{createdDate}}` | Ticket creation |
| Resolved Date | Resolved (Date) | `{{resolvedDate}}` | Resolution timestamp |

---

## Field Type Compatibility

### Text Fields
- **Clay**: String
- **Airtable**: Single line text / Long text
- **Notion**: Text / Title
- **Make.com**: String

### Email Fields
- **Clay**: String (email format)
- **Airtable**: **Email type** (use this, not Text)
- **Notion**: Email type
- **Make.com**: String

### Dates
- **Clay**: ISO 8601 format `2026-02-26T19:00:00Z`
- **Airtable**: Date / DateTime
- **Notion**: Date
- **Make.com**: Date (various formats, transform as needed)

### Numbers
- **Clay**: Number
- **Airtable**: Number / Currency / Percent
- **Notion**: Number
- **Make.com**: Number

### Select/Dropdown
- **Clay**: String (value)
- **Airtable**: Single Select / Multiple Select
- **Notion**: Select / Multi-select
- **Make.com**: String (must match exact option value)

---

## Transformation Rules

### Name Formatting
```
Clay "john smith" → Transform → Airtable "John Smith" (title case)
```

### Phone Formatting
```
Clay "+1234567890" → Transform → Airtable "+1 (234) 567-8900"
```

### Date Formatting
```
Clay "2026-02-26T19:00:00Z" → Transform → Airtable "2026-02-26"
```

### Company Name Cleanup
```
Clay "Company Name, Inc." → Transform → Airtable "Company Name"
(Remove legal suffixes: Inc., LLC, Ltd., etc.)
```

---

## Validation Rules

**Email**: Must match email regex pattern
**Phone**: Must be valid phone number format
**Domain**: Must be valid URL format
**Required Fields**: Email, Company (for leads)
**Unique Fields**: Email (no duplicates)

---

## Data Flow Mapping

### Lead Capture Flow
```
Website Form Fields → Clay Fields → Airtable Fields
- form_email → email → Email
- form_first_name → first_name → First Name
- form_last_name → last_name → Last Name
- form_company → company → Company (lookup/create)
- form_message → message → Notes
```

### Clay → Airtable Enrichment
```
Clay Enrichment → Airtable Update
- company_name (Clearbit) → Company Name
- company_size (Clearbit) → Size
- company_industry (Clearbit) → Industry
- linkedin_url (Hunter) → LinkedIn
- phone (Hunter) → Phone
```

---

## Best Practices

1. **Consistency**: Use exact same field names across platforms when possible
2. **Data Types**: Always use appropriate field types (Email type for emails, not Text)
3. **Transformation**: Transform data in Make.com before writing to Airtable
4. **Validation**: Validate data before import to prevent bad data
5. **Documentation**: Document any custom field mappings
6. **Version Control**: Track changes to field mappings in changelog

---

## Custom Field Documentation

**When adding custom fields**:
1. Document in this file immediately
2. Add to all platform schemas
3. Update transformation rules in Make.com scenarios
4. Test data flow end-to-end
5. Update department memory files if relevant

---

*This field mapping is critical for data integrity. Update whenever fields are added, modified, or removed.*
