# Website Department - Memory & Context

*Last Updated: 2026-02-26*

## Department Mission

Maintain a high-performing, user-friendly website that drives lead generation, educates prospects, and supports all business objectives through optimal user experience and technical excellence.

---

## Current State

### Active Website: ICP Clarity
**URL**: https://icpclarity.com
**Platform**: Netlify (Static Site)
**Status**: ✅ **LIVE**
**Last Deploy**: February 26, 2026
**Repository**: Desktop/ICP CLarity Website

### Active Projects
1. ✅ **ICP Clarity Website v1.0** - LIVE on Netlify
2. ✅ **Free ICP Assessment Tool** - LIVE and capturing leads
3. ✅ **Dual Webhook Integration** - Make.com + Clay webhooks active
4. 🔄 **Google Analytics 4 Setup** - Pending configuration
5. 🔄 **Missing Visual Assets** - Favicons, OG images to be created

### Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Monthly Visitors | TBD (GA4 pending) | 500+ | 🔄 Setup |
| Assessment Completions | Active | 50+/month | ✅ Tracking |
| Conversion Rate | TBD | >3% | 🔄 Setup |
| Page Load Time | ~2s (optimized) | <2s | ✅ Good |
| Lighthouse Performance | 88 | >85 | ✅ Excellent |
| Lighthouse Accessibility | 95 | >90 | ✅ Excellent |
| Lighthouse SEO | 95 | >90 | ✅ Excellent |
| Bounce Rate | TBD | <40% | 🔄 Setup |

### Recent Wins
- **2026-02-26**: ICP Clarity website launched on icpclarity.com ✅
- **2026-02-26**: Complete website documentation created in YNA Agentic ✅
- **2026-02-26**: Dual webhook integration (Make.com + Clay) deployed ✅
- **2026-02-26**: Free ICP Assessment tool live and functional ✅
- **2026-02-25**: Security improvements (CSP, HSTS, webhook proxy) ✅
- **2026-02-25**: Accessibility compliance achieved (WCAG AA) ✅

---

## Team Context

### Current Role
- **Owner/Developer**: Jahongir Mirzoev (handles all aspects currently)

### Future Roles & Responsibilities
- **Web Manager**: Strategy, content, performance
- **Developer**: Technical implementation, integrations
- **Content Manager**: Page content, blog posts
- **SEO Specialist**: Search optimization, analytics

### Key Contacts
- **Marketing**: ICP Clarity lead generation and nurture campaigns
- **Sales**: Lead qualification and discovery calls
- **Design**: Visual assets creation (favicons, OG images pending)

---

## Processes & Workflows

### Website Management
1. **Content Updates**: Edit locally → Test → Git commit → Push to main → Netlify auto-deploys
2. **Performance Monitoring**: Check Netlify logs, Lighthouse audits weekly
3. **SEO Optimization**: Meta tags configured, sitemap.xml live, robots.txt active
4. **Lead Capture**: Assessment form → Dual webhooks (Make.com + Clay) → Enrichment → Airtable

### Deployment Process
```bash
# 1. Make changes locally in ~/Desktop/"ICP CLarity Website"
# 2. Test locally (optional): netlify dev
# 3. Commit changes
git add .
git commit -m "Description of changes"
# 4. Push to main branch
git push origin main
# 5. Netlify auto-deploys in ~2 minutes
```

### Webhook Testing
```bash
cd ~/Desktop/"ICP CLarity Website"
node test-webhooks.js  # Tests both Make.com and Clay webhooks
```

### Automation Triggers
- **Assessment submission** → Dual webhooks (Make.com + Clay) → Clay enrichment → Airtable → Make.com automation → Sales notification
- **Contact form submission** → Make.com webhook → Email confirmation → Slack notification → Airtable record
- **Page published** → Netlify deploy → SSL certificate auto-renews

---

## Tools & Integrations

### Primary Tools
- **Platform**: Netlify (Static site hosting)
- **Domain**: icpclarity.com (DNS via Netlify)
- **Version Control**: Git (local repository)
- **Google Analytics 4**: To be configured
- **Make.com**: Webhook automation (Organization ID: 1966188)
- **Clay**: Lead enrichment and Nordic data integration

### API Connections
| From | To | Purpose | Status |
|------|-----|---------|--------|
| Assessment Form | Make.com Webhook | Lead automation | ✅ Active |
| Assessment Form | Clay Webhook | Lead enrichment | ✅ Active |
| Clay | Airtable | Enriched data export | ✅ Active |
| Make.com | Slack | Lead notifications | 🔄 To configure |
| Website | Google Analytics 4 | Traffic tracking | 🔄 Pending |

### Webhook URLs
**Make.com**: `https://hook.eu2.make.com/avk8orblmpj250ks7lo229axr9xn93y2`
**Clay**: `https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-73b930cc-d726-4a88-bc2d-ae7f737d8f50`

**Security**: Make.com webhook stored in Netlify environment variable `MAKE_WEBHOOK_URL`

---

## Knowledge Base

### ✅ Complete Documentation Created
- **Website Overview**: [icp-clarity-website-overview.md](icp-clarity-website-overview.md) - Comprehensive 40+ page documentation
- **Site Architecture**: [site-architecture.md](site-architecture.md) - Page structure, navigation flows, responsive design
- **Webhooks & Integrations**: [webhooks-integrations.md](webhooks-integrations.md) - Make.com + Clay integration details

### Reference Files on Desktop
Located at: `~/Desktop/"ICP CLarity Website"/`
- `DEPLOYMENT_GUIDE.md` - Deployment instructions
- `NEW_SCORING_100.md` - Assessment scoring system
- `test-webhooks.js` - Webhook testing script
- `netlify.toml` - Netlify configuration
- `100 ICP Signals.docx` - ICP signals reference
- `ICP_Clarity_Proposal_3_Tier.docx` - Service tiers proposal

### To Be Created
- **Content Inventory**: [content-inventory.md](content-inventory.md) - Full page content audit
- **SEO Strategy**: [seo-strategy.md](seo-strategy.md) - Keyword targeting, link building
- **Analytics Setup**: [analytics-setup.md](analytics-setup.md) - GA4 configuration guide
- **Content Publishing SOP**: [sops/content-publishing.md](sops/content-publishing.md)
- **Performance Monitoring SOP**: [sops/performance-monitoring.md](sops/performance-monitoring.md)

---

## Website Structure

### Main Pages
| Page | URL | Purpose | Status |
|------|-----|---------|--------|
| Homepage | `/` | Value proposition, pricing, Clay demo | ✅ Live |
| Assessment | `/assessment.html` | Free 3-min ICP assessment | ✅ Live |
| Sitemap | `/sitemap.xml` | SEO site structure | ✅ Live |
| Robots | `/robots.txt` | Search engine directives | ✅ Live |

### Homepage Sections
- `#hero` - Typewriter headline, primary CTA
- `#clay-mockup` - Animated Clay table demonstration
- `#solution` - ICP Clarity System overview
- `#nordic-data` - Data sources (Allabolag, Proff, Virk)
- `#problem` - Pain points addressed
- `#how-it-works` - Process flow
- `#pricing` - 3-tier pricing (Audit, Build, Scale)
- `#proof` - Statistics and credibility
- `#cta` - Final call-to-action

### Lead Capture Forms
1. **Assessment Form** (`/assessment.html`)
   - Step 0: Contact info (First/Last name, Email, LinkedIn, Phone)
   - Steps 1-12: ICP assessment questions
   - Results page with score and recommendations
   - **Webhooks**: Make.com + Clay (dual submission)

2. **Contact Form** (Modal - triggered from pricing cards)
   - First/Last name, Email, Phone, LinkedIn
   - Plan context (audit/build/scale/talk)
   - **Webhook**: Make.com only

---

## ICP Clarity Assessment Tool

### Overview
**Free 3-minute assessment** that scores companies on ICP clarity (0-100 points)

### Scoring System (NEW_SCORING_100)
| Category | Max Points | Purpose |
|----------|------------|---------|
| ICP Foundation | 20 | How well-defined is ICP |
| Firmographic Clarity | 20 | Company attributes clarity |
| Signal Coverage | 25 | Behavioral/intent signal tracking |
| Process Maturity | 25 | Win/loss analysis, team alignment |
| Lead Quality | 30 | Lead qualification metrics |
| Tech Infrastructure | 20 | GTM tech stack maturity |
| **TOTAL** | **140** | **100 points max** |

### Tiers
- **0-39**: Discovery Phase (just starting, high quick-win potential)
- **40-69**: Foundation Phase (basics in place, needs validation)
- **70-100**: Optimization Phase (mature ICP, ongoing refinement)

### Data Captured
- Contact information (name, email, LinkedIn, phone)
- All 12 question responses
- Category scores
- Segmentation data (sales model, customer base, team size, goals)
- Timestamp

### Data Flow
```
User completes assessment
    ↓
Submitted to BOTH webhooks simultaneously:
    ├─→ Make.com (automation)
    └─→ Clay (enrichment)

Make.com:
    ├─→ Stores in database
    ├─→ Sends email confirmation
    ├─→ Notifies sales team (Slack)
    └─→ Triggers nurture sequence

Clay:
    ├─→ Enriches contact data (Clearbit, Hunter, etc.)
    ├─→ Adds Nordic data (Allabolag, Proff, Virk)
    ├─→ Exports to Airtable
    └─→ Calculates company ICP fit score
```

---

## SEO Configuration

### Meta Tags
✅ **Title**: "ICP Clarity - Nordic B2B GTM Intelligence | Data-Backed ICP Scoring"
✅ **Description**: "ICP Clarity gives Nordic B2B companies data-backed ICP scoring powered by verified Nordic financial data from Allabolag, Proff, and Virk"
✅ **Keywords**: ICP, ideal customer profile, Nordic B2B, GTM intelligence, sales targeting, Clay automation
✅ **Canonical URL**: https://icpclarity.com/

### Open Graph
✅ Type: website
✅ Title: "ICP Clarity - Nordic B2B GTM Intelligence"
✅ Description: "Stop guessing who your best customers are. Get data-backed ICP scoring"
⚠️ Image: `/og-image.jpg` (1200x630) - **TO BE CREATED**
✅ URL: https://icpclarity.com/

### Technical SEO
| Item | Status | Notes |
|------|--------|-------|
| Sitemap.xml | ✅ Live | https://icpclarity.com/sitemap.xml |
| Robots.txt | ✅ Live | https://icpclarity.com/robots.txt |
| SSL Certificate | ✅ Active | Auto-renewed by Netlify |
| Mobile-friendly | ✅ Yes | Fully responsive design |
| Page Speed | ✅ Optimized | ~2s load time |
| WCAG AA | ✅ Compliant | Accessibility score 95 |

---

## Google Analytics Setup

### Status
🔄 **Pending** - GA4 property to be created

### Recommended Events
- `page_view` - All page loads (automatic)
- `assessment_started` - User begins assessment
- `assessment_completed` - User finishes assessment
- `contact_form_submit` - Contact form submission
- `cta_click` - CTA button clicks
- `pricing_card_click` - Pricing tier selection

### Goals/Conversions
1. Assessment completion (primary)
2. Contact form submission
3. Discovery call booking (Calendly - future)

---

## Tech Stack

### Frontend
- HTML5 (semantic markup)
- CSS3 (custom styles, minified to 56KB)
- Vanilla JavaScript (no frameworks, minified to 22KB + 28KB)
- Google Fonts: Bricolage Grotesque, DM Sans, DM Mono

### Hosting & Infrastructure
- **Hosting**: Netlify
- **CDN**: Netlify Edge Network
- **SSL**: Auto-provisioned by Netlify (Let's Encrypt)
- **Deploy**: Auto-deploy on git push to main
- **Caching**: 1 year for static assets, no cache for HTML

### Security Features
✅ Content Security Policy (CSP)
✅ HTTPS/SSL enforced
✅ Security headers (HSTS, X-Frame-Options, X-XSS-Protection)
✅ Form validation (prevents free email providers)
✅ Webhook proxy (URLs not exposed in frontend)

### Performance Features
✅ Minified CSS/JS
✅ Optimized animations (cursor pauses after 3s idle)
✅ IntersectionObserver for lazy animations
✅ Preconnect to Google Fonts
✅ Long-term caching for static assets

---

## Existing Integrations

### Make.com Scenarios for Website
**Scenario**: "ICP Clarity Assessment Handler"
**Folder**: ICP Clarity
**Organization ID**: 1966188
**Webhook URL**: `https://hook.eu2.make.com/avk8orblmpj250ks7lo229axr9xn93y2`
**Status**: ✅ Active
**Purpose**: Receives assessment submissions, distributes to Airtable, sends notifications

**To document**:
- Scenario structure and flow steps
- Connected modules (Airtable, Email, Slack)
- Error handling and retry logic

### Clay Tables
**Table**: "ICP Clarity Assessment Submissions" (inferred name)
**Webhook**: `https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-73b930cc-d726-4a88-bc2d-ae7f737d8f50`
**Status**: ✅ Active
**Purpose**: Receives leads, enriches with Clearbit/Hunter/Nordic data, exports to Airtable

**Enrichment Providers**:
- Clearbit (company data)
- Hunter (email verification)
- Allabolag (Swedish companies)
- Proff (Norwegian companies)
- Virk (Danish companies)

**To document**:
- Table schema and column configuration
- Enrichment provider settings
- Credit usage and costs
- Export destinations

---

## Pain Points & Challenges

### Current Challenges
1. ⚠️ **Missing visual assets** - Favicons, OG image not yet created
2. ⚠️ **Google Analytics not configured** - Can't track traffic yet
3. ⚠️ **No mobile hamburger menu** - Desktop nav works, mobile needs improvement
4. ⚠️ **Privacy policy missing** - GDPR compliance needed
5. ⚠️ **Clay webhook hardcoded** - Should move to environment variable

### Future Challenges
- Scale to handle high traffic (currently static site, no scalability issues)
- Blog content creation (no blog section yet)
- Case study collection (no customers yet for testimonials)

---

## Future Plans

### Q2 2026 - Immediate Priorities
1. ✅ Create favicon and OG images
2. ✅ Set up Google Analytics 4 tracking
3. ✅ Create privacy policy page (GDPR)
4. ✅ Build mobile hamburger navigation
5. ✅ Move Clay webhook to environment variable

### Q2 2026 - Growth Features
1. Blog section for content marketing
2. Case studies page (once customers acquired)
3. Resources/downloads section (ICP templates, guides)
4. Video testimonials
5. Live chat integration (Intercom or similar)

### Q3 2026 - Advanced Features
1. Personalized assessment results (A/B testing)
2. Assessment result PDF download
3. Social sharing for assessment scores
4. Calendly integration for booking
5. CRM direct integration (bypass Airtable)

---

## Notes for Claude

### Important Context
- **All form submissions** must go to BOTH Make.com AND Clay webhooks (dual submission)
- **Page performance** is critical - animations pause after idle, assets minified
- **SEO best practices** already implemented - meta tags, sitemap, robots.txt all configured
- **Mobile-first design** - responsive breakpoints at 768px and 1024px
- **Security-first** - CSP, HSTS, webhook proxy all active

### Common Requests & Responses

**"How's the ICP Clarity website doing?"**
- Read [icp-clarity-website-overview.md](icp-clarity-website-overview.md) for complete details
- Status: LIVE on https://icpclarity.com
- Webhooks: Active (Make.com + Clay)
- Performance: Excellent (Lighthouse 88-95)

**"Update assessment questions"**
- Edit `~/Desktop/"ICP CLarity Website"/assessment-standalone.js`
- Update `QUESTIONS` array
- Adjust scoring in `CATEGORIES` if needed
- Test locally, then git push to deploy

**"Check webhook status"**
- Run: `cd ~/Desktop/"ICP CLarity Website" && node test-webhooks.js`
- Should see 200 OK responses from both Make.com and Clay

**"Add new page"**
- Create HTML file in `~/Desktop/"ICP CLarity Website"/`
- Add to `sitemap.xml`
- Update navigation links
- Test SEO meta tags
- Git commit + push to deploy

**"Optimize for SEO"**
- Already optimized! Lighthouse SEO score: 95
- Sitemap: ✅ | Robots.txt: ✅ | SSL: ✅ | Mobile: ✅ | Speed: ✅

### Integration Notes
- **Data flow**: Website → Make.com webhook → Automation → Airtable
- **Data flow**: Website → Clay webhook → Enrichment → Airtable → Make.com
- **Webhook testing**: Use `test-webhooks.js` before making changes
- **Deployment**: Auto-deploys from git push (no manual steps)
- **Rollback**: `git revert HEAD && git push` or Netlify dashboard

### Quick Reference
- **Website repo**: `~/Desktop/"ICP CLarity Website"/`
- **Documentation**: This folder (`business-knowledge/departments/website/`)
- **Live site**: https://icpclarity.com
- **Netlify admin**: Check for deploy status and logs
- **Make.com org**: 1966188 (ICP Clarity folder)

---

*Synced with YNA Agentic Business Rectory - Complete documentation available in this folder*
