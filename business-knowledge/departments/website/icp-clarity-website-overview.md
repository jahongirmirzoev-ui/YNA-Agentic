# ICP Clarity Website - Complete Overview

*Last Updated: 2026-02-26*
*URL: https://icpclarity.com*
*Platform: Netlify (Static Site)*

---

## Executive Summary

The ICP Clarity website is a conversion-focused Nordic B2B GTM intelligence platform offering data-backed ICP (Ideal Customer Profile) scoring. The site features a comprehensive free assessment tool that captures leads and sends them to Clay for enrichment and Make.com for automation.

---

## Website Structure

### Main Pages

| Page | URL | Purpose | Status |
|------|-----|---------|--------|
| Homepage | `/index.html` | Main landing page, value proposition | ✅ Live |
| Assessment | `/assessment.html` | Free ICP Clarity Assessment (lead capture) | ✅ Live |
| Contact (Modal) | N/A | Embedded contact form in modals | ✅ Live |

### Previous Versions (Redirected)
- `/icp-assessment-v8_2.html` → Redirects to `/assessment.html`
- `/icp-assessment-v9.html` → Redirects to `/assessment.html`
- `/mobile-test.html` → Redirects to `/assessment.html`

---

## Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom styles (`styles.min.css` - 56KB minified)
- **Vanilla JavaScript** - No frameworks (`script.min.js`, `assessment-standalone.min.js`)
- **Fonts**:
  - Bricolage Grotesque (headlines)
  - DM Sans (body text)
  - DM Mono (code/technical elements)

### Hosting & Deployment
- **Platform**: Netlify
- **CDN**: Netlify Edge Network
- **Deployment**: Automatic via Git push
- **Branch Deploys**: Enabled for preview
- **Domain**: icpclarity.com

### Build Process
- **Minification**: CSS and JS are minified
- **Compression**: Gzip/Brotli enabled via Netlify
- **Caching**: Long-term caching for static assets (31536000s = 1 year)

---

## Key Features

### 1. Custom Cursor Animation
- Custom cursor with trailing ring effect
- Pauses after 3 seconds of inactivity (battery optimization)
- Disabled on touch devices
- Interactive hover states on clickable elements

### 2. Typewriter Effect
- Hero headline types out character-by-character on page load
- Realistic timing (38ms + random 18ms per character)
- Blinking cursor that disappears after completion

### 3. Clay Table Mockup Animation
- Animated table showing Nordic companies with ICP scores
- Rows appear sequentially (180ms stagger)
- Shows realistic data: company names, industries, revenue, employee count, ICP scores

### 4. Fade-Up Animations
- Intersection Observer triggers fade-in animations
- Elements appear as user scrolls
- Staggered delays for visual hierarchy

### 5. Stat Counters
- Animated counting effect for statistics
- Easing function for natural appearance
- Triggers on scroll into view

### 6. 3D Card Tilt Effect
- Pricing cards tilt on mouse movement
- Sheen effect follows mouse pointer
- Smooth perspective transforms

---

## ICP Clarity Assessment Tool

### Overview
Free 3-minute assessment that evaluates how clearly a company has defined their Ideal Customer Profile.

### Assessment Flow

1. **Contact Information Capture** (Step 0)
   - First Name
   - Last Name
   - Company Email
   - LinkedIn Profile URL
   - Phone Number

2. **12-Question Assessment** (Steps 1-12)
   - Questions cover 6 categories:
     - ICP Foundation (20 points)
     - Firmographic Clarity (20 points)
     - Signal Coverage (25 points)
     - Process Maturity (25 points)
     - Lead Quality (30 points)
     - Tech Infrastructure (20 points)
   - **Total**: 100 points possible

3. **Results Page**
   - Overall ICP Clarity Score (0-100)
   - Tier classification:
     - 0-39: Discovery Phase
     - 40-69: Foundation Phase
     - 70-100: Optimization Phase
   - Category breakdown with visual bars
   - Personalized recommendations
   - CTA to book discovery call

### Question Types

- **Single-select**: Most questions (radio buttons)
- **Multi-select**: Question 12 (goals selection)
- **Segmentation questions**: Q2-Q4 (sales model, customer base size, team size)

### Scoring System

The assessment uses a new 100-point scoring system (documented in `NEW_SCORING_100.md`):

| Category | Max Points | Purpose |
|----------|------------|---------|
| ICP Foundation | 20 | How well-defined is your ICP |
| Firmographic Clarity | 20 | Clarity on company attributes |
| Signal Coverage | 25 | Tracking behavioral/intent signals |
| Process Maturity | 25 | Win/loss analysis, team alignment |
| Lead Quality | 30 | Lead qualification metrics |
| Tech Infrastructure | 20 | GTM tech stack maturity |

---

## Forms & Lead Capture

### Contact Form (Modal)
**Trigger**: "Get Started" buttons on pricing cards
**Fields**:
- First Name
- Last Name
- Email
- Phone
- LinkedIn URL
- Contact preference (optional checkbox)
- Plan context (audit/build/scale/talk)

**Validation**:
- Email: Company email regex (excludes free providers)
- LinkedIn: Must be valid LinkedIn URL format
- Phone: Nordic format preferred
- Required field indicators

**Submission**:
- Sends to Make.com webhook
- Success modal confirmation
- Error handling with user feedback

### Assessment Form
**Trigger**: Visit `/assessment.html`
**Steps**: Contact info → 12 questions → Results
**Submission**: Sends complete results to both Make.com AND Clay webhooks

---

## Webhooks & Integrations

### 1. Make.com Webhook
**URL**: `https://hook.eu2.make.com/avk8orblmpj250ks7lo229axr9xn93y2`

**Purpose**:
- Receives all form submissions (contact + assessment)
- Triggers automation workflows
- Distributes data to other systems

**Data Sent**:
```json
{
  "event": "assessment_completed",
  "timestamp": "2026-02-26T10:30:00Z",
  "contact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@company.com",
    "linkedin": "https://linkedin.com/in/johndoe",
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
  "answers": [/* All 12 question responses */],
  "segmentation": {
    "salesModel": "mid-market",
    "customerBase": "51-200",
    "salesTeamSize": "4-10",
    "goals": ["lead-quality", "sales-efficiency", "scale-leads"]
  }
}
```

### 2. Clay Webhook
**URL**: `https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-73b930cc-d726-4a88-bc2d-ae7f737d8f50`

**Purpose**:
- Receives assessment submissions
- Enriches contact data with Clay providers
- Stores in Clay table for tracking

**Connected Clay Table**: "ICP Clarity Assessment Submissions" (inferred)

**Data Flow**:
```
Assessment Submission → Clay Webhook → Clay Table → Enrichment Providers →
Airtable Export → Make.com Automation
```

---

## SEO Configuration

### Meta Tags
- **Title**: "ICP Clarity - Nordic B2B GTM Intelligence | Data-Backed ICP Scoring"
- **Description**: "ICP Clarity gives Nordic B2B companies data-backed ICP scoring powered by verified Nordic financial data from Allabolag, Proff, and Virk"
- **Keywords**: ICP, ideal customer profile, Nordic B2B, GTM intelligence, sales targeting, Clay automation
- **Canonical URL**: https://icpclarity.com/

### Open Graph
- Type: website
- Title: "ICP Clarity - Nordic B2B GTM Intelligence"
- Description: "Stop guessing who your best customers are. Get data-backed ICP scoring"
- Image: `/og-image.jpg` (1200x630) - **To be created**
- URL: https://icpclarity.com/

### Twitter Cards
- Card type: summary_large_image
- Same title/description as Open Graph
- Image: `/og-image.jpg` - **To be created**

### Technical SEO
- **Sitemap**: `/sitemap.xml` ✅ Created
- **Robots.txt**: `/robots.txt` ✅ Created
- **SSL**: Enabled via Netlify
- **Mobile-friendly**: Fully responsive
- **Page Speed**: Optimized (cursor pauses after 3s, minified assets)

### Expected Lighthouse Scores
- **Performance**: ~88
- **Accessibility**: ~95 (WCAG AA compliant)
- **Best Practices**: ~95
- **SEO**: ~95

---

## Security Features

### Content Security Policy (CSP)
```
default-src 'self';
script-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://calendly.com;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
font-src 'self' https://fonts.gstatic.com;
img-src 'self' data: https:;
connect-src 'self' https://hook.eu2.make.com https://api.clay.com;
frame-src 'self' https://calendly.com;
```

### Security Headers
- **X-Frame-Options**: SAMEORIGIN (prevent clickjacking)
- **X-Content-Type-Options**: nosniff
- **X-XSS-Protection**: 1; mode=block
- **Strict-Transport-Security**: max-age=31536000 (force HTTPS)
- **Referrer-Policy**: strict-origin-when-cross-origin

### Form Validation
- Email regex excludes free providers (gmail, hotmail, etc.)
- LinkedIn URL must match pattern: `linkedin.com/in/`
- Phone number validation for Nordic formats
- Required field checks

### Webhook Security
- Webhook URLs stored in environment variables (Netlify)
- Serverless function proxy (prevents direct URL exposure)
- Rate limiting on submissions

---

## Accessibility (WCAG AA Compliant)

### Features
- ✅ Visible focus indicators for keyboard navigation
- ✅ Color contrast ratio 4.6:1 or higher
- ✅ Reduced motion support (respects `prefers-reduced-motion`)
- ✅ Semantic HTML structure
- ✅ ARIA labels on interactive elements
- ✅ Alt text on images

### Known Issues (Deferred)
- Full SVG alt text audit incomplete (50+ icons)
- Mobile hamburger navigation not yet built

---

## Performance Optimizations

### Assets
- **CSS**: Minified to 56KB (from 75KB)
- **JS**: Minified to 22KB (script.js), 28KB (assessment.js)
- **Fonts**: Preconnected to Google Fonts CDN
- **Images**: To be optimized (WebP format recommended)

### Caching Strategy
- **Static assets**: 1 year cache (`max-age=31536000, immutable`)
- **HTML files**: No cache (`max-age=0, must-revalidate`)
- **CSS/JS**: Immutable with cache busting via versioning

### Animation Optimizations
- Cursor animation pauses after 3s of inactivity
- IntersectionObserver for fade-up animations (lazy trigger)
- RequestAnimationFrame for smooth animations

---

## Files & Structure

### Key Files
```
/
├── index.html                    # Homepage (38KB)
├── assessment.html               # Assessment tool (7KB)
├── styles.css                    # Source CSS (75KB)
├── styles.min.css                # Minified CSS (56KB) ⭐
├── script.js                     # Source JS (30KB)
├── script.min.js                 # Minified JS (22KB) ⭐
├── assessment-standalone.js      # Assessment logic (40KB)
├── assessment-standalone.min.js  # Minified (28KB) ⭐
├── test-webhooks.js              # Webhook testing script
├── netlify.toml                  # Netlify configuration
├── DEPLOYMENT_GUIDE.md           # Deployment instructions
├── NEW_SCORING_100.md            # Scoring system documentation
├── robots.txt                    # Search engine directives
├── sitemap.xml                   # Site map for SEO
└── site.webmanifest              # PWA manifest
```

### Document Files (Reference Materials)
```
/
├── 100 ICP Signals.docx                    # 100 ICP signals list
├── 5-Minute ICP Clarity Assessment.docx    # Assessment template
├── ICP Framework.docx                      # ICP framework document
├── ICP_Audit_Scope_of_Work.docx           # Audit SOW template
├── ICP_Clarity_Proposal_3_Tier.docx       # 3-tier pricing proposal
├── ICP_Definition_Document_Template.docx   # ICP definition template
├── Top_50_Target_Accounts_Sample.xlsx      # Sample target accounts
└── YOUR_ICP_FROM_ZERO.docx                # ICP creation guide
```

---

## Deployment Process

### Current Setup
- **Repository**: Git-based (local)
- **Hosting**: Netlify
- **Domain**: icpclarity.com
- **Auto-deploy**: On push to main branch

### Environment Variables (Netlify)
```
MAKE_WEBHOOK_URL=https://hook.eu2.make.com/avk8orblmpj250ks7lo229axr9xn93y2
```

### Deployment Steps
1. Make changes locally
2. Test with `netlify dev` (optional)
3. Commit changes: `git add . && git commit -m "message"`
4. Push to main: `git push origin main`
5. Netlify auto-deploys in ~2 minutes

### Rollback Plan
```bash
# Via Git
git revert HEAD
git push origin main

# Or via Netlify Dashboard
Deploys → Find previous deploy → "Publish deploy"
```

---

## Analytics & Tracking

### Current Status
- **Google Analytics 4**: To be configured
- **Measurement ID**: Not yet set
- **Events tracked**: To be configured

### Recommended Events
- `page_view` - All page loads
- `assessment_started` - User begins assessment
- `assessment_completed` - User finishes assessment
- `contact_form_submit` - Contact form submission
- `cta_click` - CTA button clicks
- `pricing_card_click` - Pricing tier selection

### Goals/Conversions
1. Assessment completion
2. Contact form submission
3. Discovery call booking (Calendly)

---

## Lead Flow Summary

### Assessment Lead Flow
```
User visits /assessment.html
    ↓
Fills contact form (Step 0)
    ↓
Completes 12-question assessment
    ↓
Views results page with score
    ↓
Data sent to BOTH webhooks:
    ├─→ Make.com webhook (automation)
    └─→ Clay webhook (enrichment)

Make.com:
    ├─→ Stores in database
    ├─→ Sends notification to Slack/Email
    └─→ Triggers nurture sequence

Clay:
    ├─→ Enriches contact (Clearbit, Hunter, etc.)
    ├─→ Adds Nordic data (Allabolag, Proff, Virk)
    ├─→ Exports to Airtable
    └─→ Calculates ICP fit score
```

### Contact Form Lead Flow
```
User clicks "Get Started" (pricing card)
    ↓
Modal opens with contact form
    ↓
Fills form with plan context (audit/build/scale/talk)
    ↓
Submits form
    ↓
Sent to Make.com webhook
    ↓
Automation triggers:
    ├─→ Email confirmation to user
    ├─→ Slack notification to sales
    ├─→ Create Airtable record
    └─→ Add to nurture sequence
```

---

## Missing Assets (To Create)

### Visual Assets
- ✅ `/favicon-32x32.png` - **Missing**
- ✅ `/favicon-16x16.png` - **Missing**
- ✅ `/apple-touch-icon.png` - **Missing**
- ✅ `/og-image.jpg` (1200x630) - **Missing** (for social sharing)

### Documents
- Privacy Policy page - **Missing** (legal review needed)
- Terms of Service page - **Missing**
- Cookie Policy - **Missing**

---

## Future Improvements

### Priority 1 (High Impact)
1. Create missing favicon and OG images
2. Set up Google Analytics 4 tracking
3. Create privacy policy page (GDPR compliance)
4. Mobile hamburger navigation menu
5. Add CSRF protection to contact form

### Priority 2 (Performance)
1. Convert images to WebP format
2. Implement lazy loading for images
3. Optimize IntersectionObserver memory usage
4. Add service worker for offline support

### Priority 3 (Features)
1. Blog section for content marketing
2. Case studies page
3. Resources/downloads section
4. Video testimonials
5. Live chat integration

---

## Common Tasks

### Update Assessment Questions
1. Edit `assessment-standalone.js`
2. Update `QUESTIONS` array
3. Adjust scoring in `CATEGORIES` if needed
4. Test thoroughly before deploying
5. Update `NEW_SCORING_100.md` documentation

### Add New Page
1. Create HTML file
2. Add to `sitemap.xml`
3. Update navigation links in all pages
4. Test SEO meta tags
5. Deploy via Git push

### Update Webhook URLs
1. Update in Netlify environment variables
2. Update in `test-webhooks.js`
3. Update in `assessment-standalone.js` (if hardcoded)
4. Test with `node test-webhooks.js`
5. Verify both Make.com and Clay receive data

### Performance Check
1. Run Lighthouse audit
2. Check cursor animation stops after idle
3. Test on mobile devices
4. Verify caching headers
5. Check Netlify function logs for errors

---

## Support & Troubleshooting

### Common Issues

**Webhook not receiving data**:
- Check Netlify environment variables are set
- Verify webhook URLs haven't changed
- Test with `node test-webhooks.js`
- Check Netlify Functions logs

**Assessment not submitting**:
- Check browser console for JavaScript errors
- Verify both webhooks are responding (200 status)
- Test form validation (try submitting empty)
- Check CORS headers in webhook response

**Styling broken after deploy**:
- Clear browser cache
- Check minified CSS was uploaded
- Verify Netlify build completed successfully
- Check for CSS syntax errors

**SEO not working**:
- Verify meta tags in `<head>`
- Check `sitemap.xml` is accessible
- Test with Google Rich Results test
- Check `robots.txt` isn't blocking

---

## Contact & Ownership

**Website Owner**: Jahongir Mirzoev
**Domain**: icpclarity.com
**Hosting**: Netlify
**Repository**: Local Git (Desktop/ICP CLarity Website)
**Last Major Update**: February 26, 2026

---

*This document is part of the YNA Agentic Business Rectory and is auto-synced to the Website department memory.*
