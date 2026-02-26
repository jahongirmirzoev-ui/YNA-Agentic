# Credential Registry & API Key Management

*Last Updated: 2026-02-26*

---

## Purpose

This document tracks all API credentials, their rotation schedules, access levels, and security status.

**⚠️ IMPORTANT**: This file does NOT contain actual credentials - only metadata about them. Actual credentials are stored in `.env` files (gitignored).

---

## Credential Rotation Schedule

| Service | Last Rotated | Next Rotation | Auto-Rotate? | Owner |
|---------|--------------|---------------|--------------|-------|
| Make.com API | TBD | TBD + 90 days | ❌ Manual | Jahongir |
| Clay API | TBD | TBD + 90 days | ❌ Manual | Jahongir |
| Airtable PAT | TBD | TBD + 90 days | ❌ Manual | Jahongir |
| Notion API | TBD | TBD + 90 days | ❌ Manual | Jahongir |
| Google Analytics 4 | N/A | N/A | N/A | Jahongir |
| Email/SMTP | TBD | TBD + 180 days | ❌ Manual | Jahongir |
| Slack Webhook | TBD | Never (unless compromised) | N/A | Jahongir |

**Recommended Rotation**: Every 60-90 days for high-security APIs, 180 days for low-risk

---

## Active Credentials

### Make.com

**Credential Type**: API Token
**Location**: `.env` → `MAKECOM_API_KEY`
**Scope**: Full organization access (Org ID: 1966188)
**Created**: TBD
**Last Rotated**: TBD
**Expires**: Never (manual rotation recommended)
**Access Level**: Admin
**Used By**:
- ICP Clarity website webhooks
- Automation scenarios
- Data routing

**Security Notes**:
- Stored in Netlify environment variables (for webhook proxy)
- Also in local `.env` for scripts
- Rate limits: [Check Make.com documentation]

**Rotation Procedure**:
1. Go to Make.com → Profile → API
2. Create new token with same scopes
3. Update `.env` file: `MAKECOM_API_KEY=new_token_here`
4. Update Netlify environment variable: `MAKE_WEBHOOK_URL`
5. Test scenarios still work
6. Delete old token in Make.com
7. Update "Last Rotated" date in this registry

---

### Clay

**Credential Type**: API Key
**Location**: `.env` → `CLAY_API_KEY`
**Scope**: Full workspace access
**Created**: TBD
**Last Rotated**: TBD
**Expires**: Never (manual rotation recommended)
**Access Level**: Owner
**Used By**:
- ICP Clarity assessment webhook
- Lead enrichment workflows
- Nordic data integration scripts

**Webhook URL**:
- Location: `assessment-standalone.js` (hardcoded - TODO: move to env var)
- Format: `https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-{ID}`

**Security Notes**:
- Consider moving webhook URL to environment variable
- Rate limits: [Check Clay documentation]
- Credit usage tracking: Monitor in Clay dashboard

**Rotation Procedure**:
1. Go to Clay → Settings → API Keys
2. Generate new API key
3. Update `.env` file: `CLAY_API_KEY=new_key_here`
4. Test webhook and enrichment still work
5. Revoke old API key in Clay
6. Update "Last Rotated" date in this registry

---

### Airtable

**Credential Type**: Personal Access Token (PAT)
**Location**: `.env` → `AIRTABLE_PAT`
**Scope**: Specific bases (list base IDs below)
**Created**: TBD
**Last Rotated**: TBD
**Expires**: TBD (check Airtable settings)
**Access Level**: Creator
**Used By**:
- CRM data sync
- Make.com integration
- Clay data export destination

**Connected Bases**:
- Base ID: `[TBD]` - YNA CRM Main
- Base ID: `[TBD]` - Marketing Hub
- Base ID: `[TBD]` - Support/Tickets

**Security Notes**:
- Scoped to specific bases only (not full account)
- OAuth recommended for production (TODO)
- Rate limits: 5 requests/second per base

**Rotation Procedure**:
1. Go to Airtable → Account → Developer Hub → Personal Access Tokens
2. Create new token with same base scopes
3. Update `.env` file: `AIRTABLE_PAT=new_token_here`
4. Test integrations still work
5. Revoke old token in Airtable
6. Update "Last Rotated" date in this registry

---

### Notion API

**Credential Type**: Integration Token
**Location**: `.env` → `NOTION_API_KEY`
**Scope**: Specific pages/databases shared with integration
**Created**: TBD
**Last Rotated**: TBD
**Expires**: Never (manual rotation recommended)
**Access Level**: Full access to shared pages
**Used By**:
- Cloud sync (15-minute cron job)
- Department memory.md bidirectional sync
- Knowledge base updates

**Connected Databases**:
- Database ID: `[TBD]` - Marketing Department
- Database ID: `[TBD]` - Sales Department
- Database ID: `[TBD]` - Customer Service
- Database ID: `[TBD]` - CRM
- Database ID: `[TBD]` - Website

**Security Notes**:
- Only has access to explicitly shared pages
- Cannot access private workspace content
- Rate limits: 3 requests/second

**Rotation Procedure**:
1. Go to Notion → Settings & Members → Integrations
2. Create new internal integration
3. Share all databases with new integration
4. Update `.env` file: `NOTION_API_KEY=new_token_here`
5. Test sync scripts still work
6. Remove old integration
7. Update "Last Rotated" date in this registry

---

### Google Analytics 4

**Credential Type**: Measurement ID (public)
**Location**: `index.html`, `assessment.html` (in GA4 tracking code)
**Scope**: Website tracking only
**Created**: TBD
**Last Rotated**: N/A (Measurement ID doesn't rotate)
**Expires**: Never
**Access Level**: Public (Measurement ID), Admin (Analytics dashboard)
**Used By**:
- ICP Clarity website analytics
- Event tracking (CTA clicks, assessment completion)
- Performance monitoring

**Current Value**: `G-XXXXXXXXXX` (placeholder - needs to be replaced)

**Security Notes**:
- Measurement ID is public (safe to expose in frontend)
- Dashboard access controlled by Google Account
- Enable IP anonymization (already configured)

**No Rotation Needed** - Measurement IDs are permanent and public.

---

### Email/SMTP

**Credential Type**: App-specific password
**Location**: `.env` → `SMTP_PASSWORD`
**Scope**: Send-only (no inbox access)
**Created**: TBD
**Last Rotated**: TBD
**Expires**: TBD (check email provider)
**Access Level**: Send-only
**Used By**:
- Transactional emails (assessment results)
- Contact form confirmations
- Lead notifications

**Provider**: [TBD - Gmail/SendGrid/Mailchimp/etc.]

**Security Notes**:
- Use app-specific password (not main account password)
- Restrict to send-only permissions
- Consider dedicated sending service (SendGrid, Postmark)

**Rotation Procedure**:
1. Go to email provider → Security → App passwords
2. Generate new app-specific password
3. Update `.env` file: `SMTP_PASSWORD=new_password_here`
4. Test email sending still works
5. Revoke old app password
6. Update "Last Rotated" date in this registry

---

### Slack Webhooks

**Credential Type**: Incoming Webhook URL
**Location**: `.env` → `SLACK_WEBHOOK_URL`
**Scope**: Specific channel (e.g., #sales, #alerts)
**Created**: TBD
**Last Rotated**: N/A (rotate only if compromised)
**Expires**: Never
**Access Level**: Post to specific channel
**Used By**:
- Lead notifications
- Assessment completion alerts
- System monitoring alerts

**Channels**:
- Webhook URL 1: `[TBD]` → #sales (lead notifications)
- Webhook URL 2: `[TBD]` → #alerts (system alerts)

**Security Notes**:
- Webhook URLs should be treated as secrets
- Can only post to assigned channel
- Rate limits: 1 request/second per webhook

**Rotation Procedure** (only if compromised):
1. Go to Slack → Apps → Incoming Webhooks
2. Revoke old webhook
3. Create new webhook for same channel
4. Update `.env` file: `SLACK_WEBHOOK_URL=new_url_here`
5. Test notifications still work
6. Update this registry

---

## Security Best Practices

### Storage
- ✅ All credentials in `.env` file (gitignored)
- ✅ `.env.template` for examples (no real credentials)
- ✅ Netlify environment variables for production
- ❌ NEVER commit credentials to Git
- ❌ NEVER share credentials via email/Slack

### Access Control
- Limit credentials to minimum required scope
- Use service-specific API keys (not personal accounts)
- Regular audits of who has access

### Rotation
- **High Security (60-90 days)**: Make.com, Clay, Airtable, Notion
- **Medium Security (180 days)**: Email/SMTP
- **No Rotation**: Slack webhooks, GA4 Measurement ID (unless compromised)

### Monitoring
- Monitor API usage for anomalies
- Set up alerts for failed authentication
- Track rate limit hits
- Review access logs monthly

---

## Compromised Credential Response Plan

If a credential is compromised or suspected of compromise:

### Immediate Actions (Within 1 hour)
1. **Revoke** the compromised credential immediately
2. **Generate** new credential
3. **Update** `.env` and production environment variables
4. **Test** that services still work
5. **Document** in this registry (date, reason for rotation)

### Investigation (Within 24 hours)
1. **Review** access logs for unauthorized usage
2. **Check** what data may have been accessed
3. **Assess** impact and notify affected parties if necessary
4. **Update** security procedures to prevent recurrence

### Follow-up (Within 1 week)
1. **Audit** all other credentials for similar vulnerabilities
2. **Implement** additional security measures if needed
3. **Report** incident (if required by compliance/legal)

---

## Credential Audit Log

| Date | Service | Action | Reason | Updated By |
|------|---------|--------|--------|------------|
| 2026-02-26 | All | Registry created | Initial setup | Claude |
| | | | | |
| | | | | |

**Actions**: Created, Rotated, Revoked, Compromised, Scope Changed

---

## Notes for Claude

**When adding new services**:
1. Add credential metadata to this registry
2. Ensure credential is in `.env` (not committed to Git)
3. Add to `.env.template` with placeholder value
4. Set rotation schedule (60-90 days recommended)
5. Document rotation procedure

**Monthly Checklist**:
- Review rotation schedule
- Check for expired credentials
- Audit credential usage logs
- Update this registry with any changes

---

*This registry is part of the YNA Agentic Business Rectory security infrastructure.*
