# ICP Clarity Website - Webhooks & Integrations

*Last Updated: 2026-02-26*

---

## Overview

The ICP Clarity website uses a dual-webhook architecture to capture leads and distribute them to automation (Make.com) and enrichment (Clay) systems simultaneously.

---

## Active Webhooks

### 1. Make.com Webhook

**Webhook URL**: `https://hook.eu2.make.com/avk8orblmpj250ks7lo229axr9xn93y2`

**Region**: EU2 (Europe)

**Purpose**:
- Receives all assessment submissions and contact form submissions
- Triggers automated workflows in Make.com
- Distributes data to other connected systems (Airtable, email, Slack)
- Serves as the primary automation hub

**Triggered By**:
- Assessment completion (`assessment-standalone.js`)
- Contact form submission (pricing cards, modals)

**Data Format**:
```json
{
  "event": "assessment_completed" | "contact_form_submitted",
  "timestamp": "2026-02-26T14:30:00.000Z",
  "contact": {
    "firstName": "Erik",
    "lastName": "Johansson",
    "email": "erik@company.se",
    "linkedin": "https://linkedin.com/in/erikjohansson",
    "phone": "+46 70 123 4567",
    "contactRequested": false
  },
  "score": {
    "total": 79,
    "tier": "optimization",
    "tierLabel": "Optimization Phase",
    "maxPossible": 100
  },
  "categoryScores": {
    "icpFoundation": { "score": 20, "max": 20, "percentage": 100 },
    "firmographicClarity": { "score": 20, "max": 20, "percentage": 100 },
    "signalCoverage": { "score": 15, "max": 25, "percentage": 60 },
    "processMaturity": { "score": 25, "max": 25, "percentage": 100 },
    "leadQuality": { "score": 18, "max": 30, "percentage": 60 },
    "techInfrastructure": { "score": 12, "max": 20, "percentage": 60 }
  },
  "answers": [
    {
      "questionId": 1,
      "questionNumber": "QUESTION 1",
      "questionText": "How well-defined is your Ideal Customer Profile (ICP)?",
      "isMultiselect": false,
      "selectedAnswer": {
        "label": "Detailed, data-backed ICP used by all teams",
        "description": "We have a documented ICP validated with CRM data",
        "value": "20"
      },
      "pointsEarned": 20,
      "maxPoints": 20
    }
    // ... remaining 11 questions
  ],
  "segmentation": {
    "salesModel": "mid-market",
    "customerBase": "51-200",
    "salesTeamSize": "4-10",
    "goals": ["lead-quality", "sales-efficiency", "scale-leads"]
  }
}
```

**Expected Response**:
- Status: `200 OK` or `202 Accepted`
- Body: Can be empty or confirmation message

**Error Handling**:
- JavaScript catches fetch errors and shows user feedback
- No retry mechanism currently implemented
- Errors logged to browser console

**Security**:
- Stored in Netlify environment variable: `MAKE_WEBHOOK_URL`
- Accessed via serverless function proxy (prevents direct URL exposure)
- Rate limiting: TBD (recommended: 5 submissions per IP per hour)

**Make.com Scenario Connected** (to be documented):
- Scenario Name: "ICP Clarity Assessment Handler"
- Folder: "ICP Clarity"
- Organization ID: 1966188

---

### 2. Clay Webhook

**Webhook URL**: `https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-73b930cc-d726-4a88-bc2d-ae7f737d8f50`

**Clay Webhook ID**: `73b930cc-d726-4a88-bc2d-ae7f737d8f50`

**Purpose**:
- Receives assessment submissions for lead enrichment
- Stores submissions in Clay table
- Triggers enrichment providers (Clearbit, Hunter, ZoomInfo, etc.)
- Adds Nordic-specific data (Allabolag, Proff, Virk)
- Exports enriched data to Airtable

**Triggered By**:
- Assessment completion only (not contact form)
- Sends identical payload as Make.com webhook

**Connected Clay Table**: "ICP Clarity Assessment Submissions" (inferred - to be verified)

**Data Flow**:
```
Assessment Submission
    ↓
Clay Webhook Receives Data
    ↓
Stored in Clay Table
    ↓
Enrichment Providers Triggered:
    ├─→ Clearbit (company data)
    ├─→ Hunter (email verification)
    ├─→ LinkedIn (profile enrichment)
    ├─→ Allabolag (Swedish company data)
    ├─→ Proff (Norwegian company data)
    └─→ Virk (Danish company data)
    ↓
Enriched Data Available
    ↓
Export to Airtable (via Clay)
    ↓
Make.com reads from Airtable
    ↓
Nurture sequence begins
```

**Expected Response**:
- Status: `200 OK`
- Body: JSON with Clay record ID (optional)

**Error Handling**:
- JavaScript catches fetch errors
- No retry mechanism
- Errors logged to browser console
- User still sees results page (fire-and-forget approach)

**Security**:
- Hardcoded in `assessment-standalone.js` (consider moving to env var)
- Clay API handles authentication via webhook URL token

---

## Webhook Testing

### Test Script
**File**: `test-webhooks.js`

**Usage**:
```bash
cd ~/Desktop/"ICP CLarity Website"
node test-webhooks.js
```

**Purpose**:
- Sends sample assessment data to both webhooks
- Verifies both endpoints are responding
- Tests data format compatibility

**Test Data**:
- Realistic Nordic user (Erik Johansson, Nordic Tech AB)
- Score: 79/100 (Optimization Phase)
- All 12 questions answered
- Multi-select goals included

**Expected Output**:
```
🚀 Testing webhooks with sample data...

✅ Make.com webhook: 200 OK
   Response: (empty)
✅ Clay webhook: 200 OK
   Response: {"success": true}
```

---

## Integration Architecture

### Dual-Webhook Strategy

**Why Two Webhooks?**
1. **Separation of Concerns**:
   - Make.com = Automation & workflow orchestration
   - Clay = Data enrichment & intelligence gathering

2. **Redundancy**:
   - If one webhook fails, the other still captures data
   - No single point of failure

3. **Specialized Processing**:
   - Make.com excels at workflow automation (email, Slack, CRM updates)
   - Clay excels at data enrichment (company research, signal tracking)

**Tradeoffs**:
- ❌ Double the API calls
- ❌ Slightly slower submission (both must complete)
- ✅ Better data coverage
- ✅ More robust system

---

## Data Flow Diagram

```
┌─────────────────────────────────────────┐
│     ICP Clarity Website (Frontend)     │
│  (assessment.html + assessment.js)     │
└─────────────────┬───────────────────────┘
                  │
        User completes assessment
                  │
                  ▼
┌─────────────────────────────────────────┐
│      JavaScript Submission Handler      │
│  - Validates data                       │
│  - Formats JSON payload                 │
│  - Sends to BOTH webhooks simultaneously│
└───────┬─────────────────────┬───────────┘
        │                     │
        ▼                     ▼
┌───────────────┐     ┌───────────────────┐
│  Make.com     │     │   Clay Webhook    │
│   Webhook     │     │                   │
└───────┬───────┘     └─────────┬─────────┘
        │                       │
        ▼                       ▼
┌───────────────┐     ┌───────────────────┐
│  Make.com     │     │   Clay Table      │
│  Scenario     │     │  "ICP Clarity     │
│  Processing   │     │   Submissions"    │
└───────┬───────┘     └─────────┬─────────┘
        │                       │
        ├─→ Airtable           │
        ├─→ Email              ├─→ Enrichment
        ├─→ Slack              │   (Clearbit,
        └─→ CRM Update         │    Hunter,
                               │    Allabolag,
                               │    Proff, Virk)
                               │
                               ▼
                       ┌───────────────────┐
                       │  Enriched Data    │
                       │  Exported to      │
                       │  Airtable         │
                       └───────┬───────────┘
                               │
                               ▼
                       ┌───────────────────┐
                       │  Make.com Reads   │
                       │  from Airtable    │
                       │  & Triggers       │
                       │  Nurture Sequence │
                       └───────────────────┘
```

---

## Make.com Scenarios (To Be Documented)

### Scenario 1: ICP Clarity Assessment Handler
**Folder**: ICP Clarity
**Trigger**: Webhook (URL above)
**Steps** (to be mapped):
1. Receive webhook data
2. Parse JSON payload
3. Create/update Airtable record
4. Send Slack notification to #sales channel
5. Trigger email to user (confirmation + resources)
6. Add to Mailchimp/ActiveCampaign nurture list
7. If score < 40: Tag as "Discovery Phase"
8. If score 40-69: Tag as "Foundation Phase"
9. If score 70+: Tag as "Optimization Phase" + priority flag

**Status**: ✅ Active (to be verified)
**Last Modified**: TBD

---

## Clay Tables (To Be Documented)

### Table 1: ICP Clarity Assessment Submissions
**Webhook Connected**: Yes (URL above)
**Enrichment Providers**:
- Clearbit (company data)
- Hunter (email verification)
- Apollo (contact enrichment)
- Allabolag (Swedish company registry)
- Proff (Norwegian company registry)
- Virk (Danish company registry)

**Fields** (inferred):
- First Name
- Last Name
- Email
- Phone
- LinkedIn URL
- Company Name (enriched)
- Company Domain (enriched)
- Company Size (enriched)
- Revenue (enriched)
- Industry (enriched)
- Country (enriched)
- ICP Score (from assessment)
- Tier (Discovery/Foundation/Optimization)
- Submission Date
- Category Scores (6 categories)
- Segmentation Data (sales model, customer base, team size)
- Goals (multi-select)

**Outputs**:
- Export to Airtable (CRM Main base)
- Webhook to Make.com (for further processing)

**Credit Usage**: ~5-10 credits per enrichment (depending on providers)

**Status**: ✅ Active (to be verified)

---

## Airtable Bases (To Be Documented)

### Base: YNA CRM Main (or ICP Clarity CRM)
**Receives Data From**:
- Clay (enriched assessment data)
- Make.com (direct form submissions)

**Tables** (inferred):
1. **Contacts** - All lead contact information
2. **Assessments** - Assessment results and scoring
3. **Companies** - Company/account data
4. **Activities** - Touchpoints and interactions

**Automations**:
- Webhook to Make.com when new contact added
- Notification to Slack when high-score lead (70+)
- Email to sales when contact requests follow-up

---

## Troubleshooting

### Webhook Not Receiving Data

**Make.com**:
1. Check Make.com scenario is active (not paused)
2. Verify webhook URL hasn't changed
3. Test with `node test-webhooks.js`
4. Check Make.com scenario execution history
5. Verify Netlify environment variable `MAKE_WEBHOOK_URL` is set

**Clay**:
1. Check Clay table webhook is connected
2. Verify webhook URL format is correct
3. Test with `node test-webhooks.js`
4. Check Clay table for new rows
5. Verify Clay workspace has sufficient credits

### Data Not Enriching in Clay

1. Check Clay enrichment providers are configured
2. Verify API keys for Clearbit, Hunter, etc. are active
3. Check Clay credit balance
4. Review Clay enrichment column for error messages
5. Test with a known-good email domain

### Duplicate Submissions

**Cause**: User refreshes results page or clicks "Submit" multiple times

**Solution**:
- Add submission tracking (localStorage or session storage)
- Disable submit button after first click
- Implement server-side deduplication (email + timestamp)

---

## Security Best Practices

### Current Implementation
✅ Webhooks use HTTPS
✅ Make.com webhook stored in environment variable
✅ Form validation prevents basic injection attacks
✅ CORS headers configured in Netlify

### Recommended Improvements
- ⚠️ Add HMAC signature verification for webhooks
- ⚠️ Implement rate limiting (5 submissions per IP per hour)
- ⚠️ Add CAPTCHA for bot prevention
- ⚠️ Store Clay webhook in environment variable (currently hardcoded)
- ⚠️ Add timestamp validation (reject old submissions)

---

## Monitoring & Alerts

### Recommended Setup

**Webhook Monitoring**:
- Set up Make.com email alert if scenario fails
- Monitor Clay table for new rows (should match submission count)
- Check Airtable daily for new records

**Error Tracking**:
- Implement Sentry or similar for JavaScript errors
- Monitor Netlify function logs
- Set up uptime monitoring (Pingdom, UptimeRobot)

**Analytics**:
- Track `assessment_completed` event in Google Analytics
- Monitor webhook success/failure rates
- Track time between submission and enrichment completion

---

## Change Log

**2026-02-26**:
- Documented dual-webhook architecture
- Identified Make.com webhook URL
- Identified Clay webhook URL
- Created test script for verification
- Outlined data flow and integration points

---

## Next Steps

1. ✅ Verify Make.com scenario configuration
2. ✅ Verify Clay table configuration and enrichment providers
3. ✅ Verify Airtable base structure
4. ⚠️ Move Clay webhook to environment variable
5. ⚠️ Add HMAC signature verification
6. ⚠️ Implement rate limiting
7. ⚠️ Set up monitoring and alerts
8. ⚠️ Document specific Make.com scenario steps
9. ⚠️ Document Clay table schema
10. ⚠️ Map complete data flow from website → Airtable → nurture

---

*This document is part of the YNA Agentic Business Rectory website department documentation.*
