# ICP Clarity Website - Site Architecture

*Last Updated: 2026-02-26*
*Live URL: https://icpclarity.com*

---

## Site Structure

```
icpclarity.com/
│
├── / (index.html)                    # Homepage
│   ├── #hero                         # Hero section with typewriter headline
│   ├── #clay-mockup                  # Animated Clay table demonstration
│   ├── #solution                     # ICP Clarity System overview
│   ├── #nordic-data                  # Nordic data sources (Allabolag, Proff, Virk)
│   ├── #problem                      # Pain points section
│   ├── #how-it-works                 # Process explanation
│   ├── #pricing                      # 3-tier pricing (Audit, Build, Scale)
│   ├── #proof                        # Stats and social proof
│   └── #cta                          # Final call-to-action
│
├── /assessment.html                  # Free ICP Clarity Assessment
│   ├── Contact Form (Step 0)        # Lead capture before assessment
│   ├── Question 1-12                # Assessment questions
│   └── Results Page                  # Score + recommendations
│
├── /robots.txt                       # Search engine directives
├── /sitemap.xml                      # Site map for SEO
└── /site.webmanifest                # PWA manifest

Archived/Redirected:
├── /icp-assessment-v8_2.html        → /assessment.html (301)
├── /icp-assessment-v9.html          → /assessment.html (301)
└── /mobile-test.html                → /assessment.html (301)
```

---

## Homepage Structure (`/index.html`)

### Navigation
- Logo: "ICP Clarity"
- Links: Solution | Data | Pricing
- CTA Button: "Get Free ICP Score" → `/assessment.html`

### Hero Section (`#hero`)
**Purpose**: Capture attention, communicate value proposition

**Elements**:
- Grid lines background animation
- Floating shapes (visual interest)
- **Headline**: "Stop Guessing Who Your Best Customers Are." (typewriter effect)
- **Subheadline**: "ICP Clarity gives Nordic B2B companies a data-backed system to identify, score, and convert the right accounts — built on Clay, powered by verified Nordic financial data."
- **Primary CTA**: "Take the Free ICP Clarity Assessment" → `/assessment.html`
- **Proof Line**: "Free. Takes 3 minutes. Get your ICP Clarity Score instantly."
- **Secondary Link**: "Already know what you need? See our services ↓"

### Clay Table Mockup (`#clay-mockup`)
**Purpose**: Demonstrate what Clay-powered ICP scoring looks like

**Animation**:
- Rows appear sequentially (180ms stagger)
- Shows 5 sample Nordic companies
- Displays: Company | Industry | Revenue | Employees | ICP Score

**Sample Data**:
| Company | Industry | Revenue | Employees | ICP Score |
|---------|----------|---------|-----------|-----------|
| Nordic SaaS AB | B2B Software | 45M SEK | 120 | 94 |
| Fjord Analytics AS | Data Analytics | 28M SEK | 65 | 88 |
| København Tech ApS | Tech Services | 62M SEK | 180 | 76 |
| Oslo Growth Solutions | Marketing | 18M SEK | 35 | 82 |
| Stockholm Ventures | VC/Investment | 95M SEK | 250 | 91 |

### Solution Section (`#solution`)
**Purpose**: Explain the ICP Clarity System

**3 Steps**:
1. **Audit** - Analyze your current ICP clarity (or lack thereof)
2. **Build** - Create data-backed ICP scoring system in Clay
3. **Scale** - Ongoing optimization and target account discovery

### Nordic Data Section (`#nordic-data`)
**Purpose**: Emphasize Nordic data advantage

**Data Sources**:
- 🇸🇪 **Allabolag** (Sweden) - 1.5M+ companies, verified financials
- 🇳🇴 **Proff** (Norway) - 800K+ companies, credit ratings
- 🇩🇰 **Virk** (Denmark) - 600K+ companies, ownership data

**Value Proposition**:
- More accurate than generic tools (Clearbit, ZoomInfo)
- Real-time financial data
- Nordic-specific signals (hiring, funding, M&A)

### Problem Section (`#problem`)
**Purpose**: Resonate with pain points

**Problems Addressed**:
- ❌ ICP defined but not data-backed
- ❌ Sales chasing unqualified leads
- ❌ Marketing attracting wrong companies
- ❌ No systematic way to score prospects
- ❌ Relying on gut feeling instead of data

### How It Works (`#how-it-works`)
**Purpose**: Demystify the process

**Process Steps**:
1. **Take Free Assessment** (3 minutes)
2. **Get ICP Clarity Score** (instant results)
3. **Book Discovery Call** (15 minutes, optional)
4. **Choose Your Path**:
   - Tier 1: ICP Intelligence Audit (25,000 SEK)
   - Tier 2: GTM Intelligence Engine (70,000 SEK)
   - Tier 3: GTM Intelligence Retainer (monthly)

### Pricing Section (`#pricing`)
**Purpose**: Present 3-tier offering

#### Tier 1: ICP Intelligence Audit
**Price**: 25,000 SEK
**Timeline**: 2 weeks
**Deliverables**:
- Current ICP analysis
- Win/loss pattern analysis
- Data-backed ICP definition
- 50 target accounts (scored)
- 1-hour strategy session

**CTA**: "Get Started" → Contact form modal

#### Tier 2: GTM Intelligence Engine
**Price**: 70,000 SEK
**Timeline**: 4-6 weeks
**Deliverables**:
- Everything in Tier 1 +
- Clay table setup (ICP scoring system)
- Nordic data integration (Allabolag, Proff, Virk)
- 500+ target accounts (scored & enriched)
- Signal tracking (hiring, funding, tech stack changes)
- Airtable integration
- Make.com automation (lead routing)
- Training session (2 hours)

**CTA**: "Get Started" → Contact form modal

#### Tier 3: GTM Intelligence Retainer
**Price**: Contact for information
**Timeline**: Ongoing
**Deliverables**:
- Everything in Tier 2 +
- Monthly ICP refresh
- New target account discovery (100/month)
- Signal monitoring & alerts
- Quarterly strategy sessions
- Priority support

**CTA**: "Get Started" → Contact form modal

### Proof Section (`#proof`)
**Purpose**: Build credibility with stats

**Stats** (animated counters):
- **100+** ICP signals tracked
- **1.5M+** Nordic companies in database
- **500+** target accounts scored per engagement

### Final CTA Section (`#cta`)
**Headline**: "Stop Guessing. Start Knowing."
**CTA Button**: "Take the Free ICP Clarity Assessment" → `/assessment.html`

---

## Assessment Page Structure (`/assessment.html`)

### Header
- Headline: "Discover Your ICP Clarity Score"
- Subheadline: "A free 3-minute assessment to evaluate how clearly you've defined your Ideal Customer Profile — and where you can improve."

### Step 0: Contact Form
**Purpose**: Capture lead information before assessment begins

**Fields** (all required):
- First Name
- Last Name
- Company Email (validated - no free providers)
- LinkedIn Profile URL (validated format)
- Phone Number (Nordic format preferred)

**CTA Button**: "Start Assessment"

**Validation**:
- Email regex: `^[a-zA-Z0-9._+-]+@(?!gmail|yahoo|hotmail|outlook|protonmail|icloud|aol|mail|gmx|zoho)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- LinkedIn regex: `^https?://(www\.)?linkedin\.com/in/[\w-]+/?$`
- Phone: Basic format check

### Steps 1-12: Assessment Questions

**Question Categories**:
1. **ICP Foundation** (Q1) - 20 points max
2. **Firmographic Clarity** (Q5) - 20 points max
3. **Signal Coverage** (Q6) - 25 points max
4. **Process Maturity** (Q7-Q8) - 25 points max
5. **Lead Quality** (Q9-Q10) - 30 points max
6. **Tech Infrastructure** (Q11) - 20 points max

**Segmentation Questions** (0 points, for targeting):
- Q2: Sales Model (SMB, Mid-Market, Enterprise)
- Q3: Customer Base Size (0-20, 21-50, 51-200, 201-500, 500+)
- Q4: Sales Team Size (1-3, 4-10, 11-25, 26-50, 50+)
- Q12: Goals (multi-select: lead quality, sales efficiency, scale leads, data clarity, team alignment)

**Question Details**:
See [assessment-questions.md](assessment-questions.md) for full question list

**Progress Indicator**:
- Shows current step (e.g., "QUESTION 1 of 12")
- Visual progress bar

**Navigation**:
- "Continue" button (disabled until answer selected)
- "Back" button (except Step 0)

### Results Page
**Trigger**: After answering all 12 questions

**Layout**:
- **Hero Score**: Large display of total score (0-100)
- **Tier Badge**: Discovery Phase | Foundation Phase | Optimization Phase
- **Tier Descriptions**:
  - **0-39 (Discovery)**: "You're just starting to define your ICP. High potential for quick wins."
  - **40-69 (Foundation)**: "You have ICP basics but need data validation and systematic scoring."
  - **70-100 (Optimization)**: "Your ICP is mature. Focus on ongoing refinement and signal tracking."

**Category Breakdown**:
- 6 category scores displayed with:
  - Category name
  - Points earned / Max points
  - Percentage bar (visual)
  - Color coding (red < 50%, yellow 50-79%, green 80%+)

**Personalized Recommendations**:
- Based on tier and category scores
- Top 3 areas for improvement
- Suggested next steps

**CTAs**:
- Primary: "Book Free Discovery Call" (Calendly embed/link)
- Secondary: "Download Full Results" (PDF generation - future feature)
- Tertiary: "Explore Our Services" → Homepage #pricing

**Social Sharing** (future feature):
- "I scored X/100 on the ICP Clarity Assessment" → LinkedIn share

---

## Modals & Overlays

### Contact Form Modal
**Trigger**: Click "Get Started" on any pricing card

**Fields**:
- First Name
- Last Name
- Email
- Phone
- LinkedIn URL
- Checkbox: "I'd like to discuss this over a call"
- Hidden field: Plan context (audit/build/scale/talk)

**Submit**: Sends to Make.com webhook → Success modal

### Success Modal
**Trigger**: Contact form submission successful

**Content**:
- ✅ "Thanks! We'll be in touch within 24 hours."
- Email confirmation sent
- Booking link: "Or schedule a call now" (Calendly)

**Close**: Click outside or close button

---

## Redirects

Configured in `netlify.toml`:

| From | To | Status |
|------|-----|--------|
| `/icp-assessment-v8_2.html` | `/assessment.html` | 301 |
| `/icp-assessment-v9.html` | `/assessment.html` | 301 |
| `/mobile-test.html` | `/assessment.html` | 301 |
| `/*` | `/index.html` | 200 (catch-all) |

---

## Navigation Flow

### Primary User Journey
```
1. Land on homepage (/)
    ↓
2. Read value proposition
    ↓
3. Click "Take Free Assessment" CTA
    ↓
4. Redirected to /assessment.html
    ↓
5. Fill contact form (Step 0)
    ↓
6. Answer 12 questions (Steps 1-12)
    ↓
7. View results page
    ↓
8. Book discovery call OR explore services
```

### Alternative Journey (Direct to Pricing)
```
1. Land on homepage (/)
    ↓
2. Scroll to #pricing section
    ↓
3. Click "Get Started" on pricing card
    ↓
4. Fill contact form modal
    ↓
5. Submit → Success modal
    ↓
6. Await contact from sales team
```

---

## Responsive Design

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Mobile Optimizations
- Hamburger menu (to be built)
- Stacked layout for pricing cards
- Simplified animations (reduced motion)
- Larger touch targets (48px minimum)
- Optimized font sizes

### Desktop Features
- Custom cursor animation
- 3D card tilt effects
- Full navigation menu
- Multi-column layouts

---

## Page Load Sequence

### Homepage Load
1. HTML parsed
2. CSS loaded (`styles.min.css`)
3. JavaScript loaded (`script.min.js`)
4. Fonts loaded (Google Fonts)
5. Typewriter effect starts (hero headline)
6. Fade-up animations triggered (scroll-based)
7. Custom cursor activates
8. IntersectionObservers initialized

### Assessment Page Load
1. HTML parsed
2. CSS loaded (`styles.min.css`)
3. Assessment script loaded (`assessment-standalone.min.js`)
4. Contact form rendered
5. Validation initialized
6. Progress tracking initialized

---

## Performance Considerations

### Critical Rendering Path
- Minified CSS (56KB) loaded in `<head>`
- JavaScript loaded at end of `<body>` (non-blocking)
- Fonts preconnected to Google Fonts CDN

### Asset Optimization
- CSS: Minified (75KB → 56KB)
- JS: Minified (30KB → 22KB for script.js, 40KB → 28KB for assessment.js)
- Images: To be converted to WebP (future optimization)

### Animation Optimizations
- Custom cursor pauses after 3s idle
- IntersectionObserver lazy-loads animations
- `prefers-reduced-motion` respected

---

## Future Architecture Plans

### Blog Section
```
/blog/
├── index.html              # Blog listing page
├── /what-is-icp/          # Individual post
├── /nordic-b2b-data/      # Individual post
└── /icp-signals-guide/    # Individual post
```

### Resources Section
```
/resources/
├── /templates/            # ICP templates for download
├── /guides/              # Educational guides
└── /case-studies/        # Customer success stories
```

### Additional Pages
- `/privacy-policy/` - GDPR compliance
- `/terms-of-service/` - Legal terms
- `/about/` - Team & mission
- `/contact/` - Dedicated contact page

---

*This document is part of the YNA Agentic Business Rectory website department documentation.*
