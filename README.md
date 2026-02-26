# YNA Agentic - Business Rectory

**Your Complete Business Operating System with Persistent AI Memory**

A comprehensive directory structure ("Rectory") that integrates cloud knowledge management, API orchestration, and persistent memory across Claude Code sessions.

---

## 🚀 What Is This?

YNA Agentic transforms your business operations by:

✅ **Persistent Memory**: Claude remembers your business context across sessions - no more repeating yourself
✅ **Auto-Documentation**: Scripts automatically fetch and document your Make.com, Clay, and Airtable integrations
✅ **Folder-Specific**: Only fetches data from YOUR specified folders/workspaces
✅ **Document Import**: Convert Word/PDF documents to searchable markdown
✅ **Cloud Sync**: Optional Notion integration for team collaboration
✅ **Centralized Knowledge**: Single source of truth for all business operations

---

## ⚡ Quick Start (15 Minutes)

### Step 1: Install Dependencies (2 min)

```bash
cd /Users/jahongirmirzoev/Desktop/YNA_Agentic
pip3 install -r scripts/requirements.txt
```

### Step 2: Add Your API Keys (3 min)

```bash
# Copy template
cp .env.template .env

# Edit and add your API keys
nano .env
```

**Get your API keys**:
- **Make.com**: Settings → API → Create Token
- **Clay**: Dashboard → Settings → API Keys
- **Airtable**: Account → Developer Hub → Personal Access Tokens

### Step 3: Configure Folders (5 min)

Edit [config/integration-filters.json](config/integration-filters.json):

```json
{
  "makecom": {
    "filters": {
      "include_folders": [
        "YNA Agentic - Marketing",
        "YNA Agentic - Sales"
      ]
    }
  },
  "clay": {
    "filters": {
      "include_tables": [
        "YNA Lead Enrichment",
        "YNA Company Research"
      ]
    }
  },
  "airtable": {
    "bases": [
      {
        "base_id": "appXXXXXXXXXXXXXX",
        "base_name": "YNA CRM Main"
      }
    ]
  }
}
```

### Step 4: Run Auto-Documentation (5 min)

```bash
./scripts/update-knowledge-base.sh
```

This automatically:
- Fetches all your Make.com scenarios from specified folders
- Documents all your Clay tables
- Maps all your Airtable bases and fields
- Generates complete markdown documentation

### Step 5: Test It! (immediate)

**Start a new Claude Code session** and ask:

```
"What Make.com scenarios do I have?"
"What's the Marketing department's mission?"
"How does our lead capture flow work?"
```

Claude will read your auto-generated documentation and give you accurate answers!

---

## 📁 What's Inside

```
YNA_Agentic/
├── CLAUDE.md                          # 🧠 Primary memory file Claude reads
├── README.md                          # 📖 This file
├── .env                              # 🔐 Your API keys (gitignored)
├── .gitignore                        # 🔒 Security protection
│
├── business-knowledge/               # 💾 Persistent knowledge base
│   ├── departments/                  # 5 business departments
│   │   ├── marketing/memory.md      # Marketing context & state
│   │   ├── sales/memory.md          # Sales context & state
│   │   ├── customer-service/memory.md
│   │   ├── crm/memory.md
│   │   └── website/memory.md
│   │
│   ├── api-integrations/            # 🔌 All API documentation
│   │   ├── README.md                # Integration hub
│   │   ├── makecom/scenarios/       # Auto-generated scenario docs
│   │   ├── clay/tables/             # Auto-generated table docs
│   │   ├── airtable/bases/          # Auto-generated base docs
│   │   └── integration-flows/       # Data flow diagrams
│   │
│   ├── documents/                   # 📄 Imported Word/PDF docs
│   └── processes/                   # 📋 Cross-functional workflows
│
├── scripts/                         # 🤖 Automation scripts
│   ├── fetch-makecom-scenarios.py  # Auto-fetch Make.com scenarios
│   ├── fetch-clay-tables.py        # Auto-fetch Clay tables
│   ├── fetch-airtable-bases.py     # Auto-fetch Airtable bases
│   ├── import-documents.py         # Convert Word/PDF to markdown
│   ├── update-knowledge-base.sh    # Main update script
│   └── README.md                   # Scripts documentation
│
├── config/                         # ⚙️ Configuration
│   ├── integration-filters.json    # Folder/workspace filters
│   └── environments/               # Dev/staging/prod configs
│
└── execution/                      # 🎯 Active work
    ├── campaigns/                  # Marketing campaigns
    ├── proposals/                  # Sales proposals
    └── reports/                    # Analytics reports
```

---

## 🎯 What You Can Do Now

### 1. Ask Claude About Your Business

**Without Rectory**:
```
You: "What's our marketing strategy?"
Claude: "I don't have that information."
```

**With Rectory**:
```
You: "What's our marketing strategy?"
Claude: *reads marketing/memory.md*
"Your Q1 Lead Generation Campaign is running. Landing page is live,
ads launching next week. Targeting 100 qualified leads/month, currently at 45.
Connected to Clay for enrichment, data flows to Airtable, then Make.com
triggers email nurture sequences..."
```

### 2. Understand Your Integrations

```
You: "How does our lead capture work?"
Claude: *reads data-flow-diagram.md*
"Your lead capture flow:
1. Website form submission
2. Webhook to Clay table 'YNA Lead Enrichment'
3. Clay enriches with Clearbit + Hunter
4. Pushes to Airtable 'CRM Main - Contacts'
5. Airtable webhook triggers Make.com scenario 'Lead Notification'
6. Make.com sends Slack alert to #sales
7. Email nurture sequence begins"
```

### 3. Get Integration Details

```
You: "What Make.com scenarios do I have?"
Claude: *reads auto-generated scenario-index.md*
"You have 12 active scenarios:
1. Lead Enrichment Flow - Triggered by Airtable webhook
2. Daily Sales Report - Runs at 8am daily
3. Customer Onboarding - Triggered when deal closes
..."
```

### 4. Import Your Documents

```bash
# Import brand guidelines
python3 scripts/import-documents.py ~/Documents/Brand_Guidelines.docx --department marketing

# Now ask Claude
"What are our brand colors?"

Claude: *reads imported brand-guidelines.md*
"Your brand colors are:
- Primary: #1E40AF (Blue)
- Secondary: #10B981 (Green)
- Accent: #F59E0B (Orange)"
```

---

## 🔧 Common Tasks

### Update Documentation

When you add/modify integrations:

```bash
./scripts/update-knowledge-base.sh
```

### Import Documents

```bash
# Single file
python3 scripts/import-documents.py Sales_Playbook.docx --department sales

# Entire folder
python3 scripts/import-documents.py ~/Desktop/YNA_Docs/ --directory
```

### Update Department Status

Edit any department memory file:

```bash
# Edit marketing status
nano business-knowledge/departments/marketing/memory.md

# Update current projects, metrics, etc.
```

Claude will read the updated file in the next session!

### Add Manual Notes

Auto-generated docs are templates - add your own notes:

```markdown
<!-- In makecom/scenarios/scenario-index.md -->

## Scenario: Lead Enrichment Flow

**Purpose**: Automatically enriches new leads from website forms

**Notes**:
- Runs 24/7
- Average processing time: 30 seconds
- Fallback: If Clay fails, still saves to Airtable unenriched
- Owner: Marketing team
```

---

## 🌟 Key Features

### Persistent Memory
- Claude remembers your business context
- No more repeating information
- Context survives sessions

### Auto-Documentation
- Scripts fetch data from APIs
- Generate markdown documentation
- Always up-to-date

### Folder-Specific Filtering
- Only fetch YOUR data
- Exclude test/archive folders
- Configurable per platform

### Document Import
- Convert Word/PDF → Markdown
- Auto-link from department files
- Searchable by Claude

### Security-First
- API keys gitignored
- Credentials never committed
- Local-only sensitive data

---

## 📚 Documentation

- **[Scripts README](scripts/README.md)** - Detailed script documentation
- **[Integration Hub](business-knowledge/api-integrations/README.md)** - API integrations overview
- **[CLAUDE.md](CLAUDE.md)** - Primary context file (Claude reads this first)

---

## 🎓 How It Works

### The Magic: CLAUDE.md

Every Claude Code session automatically reads [CLAUDE.md](CLAUDE.md). This file contains:
- Navigation to all department memory files
- Links to API integration docs
- Current system status
- Directives for Claude

### Memory Files

Each department has a `memory.md` file containing:
- Current projects and metrics
- Team context
- Processes and workflows
- Tools and integrations
- Notes for Claude to remember

### Auto-Generated Docs

Scripts fetch data from APIs and generate:
- Make.com scenario index with all scenarios
- Clay table schemas with enrichment providers
- Airtable base inventory with field mappings

### Data Flow

```
Your APIs → Scripts → Markdown Docs → Claude Reads → Intelligent Responses
```

---

## ⚙️ Configuration

### Integration Filters

[config/integration-filters.json](config/integration-filters.json) controls what data is fetched:

```json
{
  "makecom": {
    "enabled": true,
    "filters": {
      "include_folders": ["YNA Agentic - Marketing"],
      "exclude_folders": ["Archive", "Testing"],
      "include_tags": ["production"]
    }
  }
}
```

**Benefits**:
- Only fetch relevant data
- Exclude test/archive data
- Keep documentation focused

### Environment Variables

[.env](.env) stores your API keys:

```bash
MAKECOM_API_KEY=your_key
CLAY_API_KEY=your_key
AIRTABLE_PAT=your_token
```

**Security**:
- Never committed to git
- `.gitignore` prevents accidents
- Local-only storage

---

## 🔄 Workflow Examples

### Daily Routine

```bash
# Morning: Update documentation
./scripts/update-knowledge-base.sh

# Work with Claude all day
# Claude has up-to-date context

# End of day: Import any new documents
python3 scripts/import-documents.py ~/Downloads/new_docs/ --directory
```

### Adding New Integration

```bash
# 1. Add scenario in Make.com to "YNA Agentic - Sales" folder
# 2. Update documentation
./scripts/update-knowledge-base.sh
# 3. Verify
cat business-knowledge/api-integrations/makecom/scenarios/scenario-index.md
# 4. Ask Claude
"What's the new scenario I just added?"
```

### Team Collaboration (Future)

When Notion sync is set up:
1. Update department status in Notion
2. Auto-syncs to local files
3. Claude reads updated context
4. Team has shared knowledge base

---

## 🐛 Troubleshooting

### Scripts Not Running

```bash
# Install dependencies
pip3 install -r scripts/requirements.txt

# Make executable
chmod +x scripts/*.sh scripts/*.py
```

### Empty Documentation

- Check folder names in `config/integration-filters.json`
- Verify API keys in `.env`
- Try removing filters to see all data first

### Claude Not Remembering

- Verify `CLAUDE.md` exists
- Check department `memory.md` files exist
- Start fresh Claude session to reload context

See [scripts/README.md](scripts/README.md) for more troubleshooting.

---

## 🚦 Next Steps

1. ✅ **Run the scripts** - Get your integrations documented
2. 📝 **Populate department files** - Add current projects and metrics
3. 📄 **Import documents** - Convert existing docs to markdown
4. 🧪 **Test with Claude** - Ask questions and see the magic
5. ⚙️ **Set up automation** - Daily cron job to keep docs updated
6. 🌥️ **Add Notion sync** - (Optional) For team collaboration

---

## 💡 Pro Tips

**Start Small**:
- Document 3-5 Make.com scenarios first
- Fill in one department completely
- Test that Claude can reference it
- Then expand

**Keep It Updated**:
- Run update script weekly
- Edit memory files when status changes
- Import new documents as created

**Use It Daily**:
- Ask Claude about integrations
- Request workflow diagrams
- Get help troubleshooting
- Claude knows your setup!

---

## 🎉 Success Metrics

You'll know it's working when:

✅ Claude answers questions about your business accurately
✅ You never repeat yourself to Claude
✅ Integration documentation is always current
✅ Team can reference shared knowledge base
✅ New team members get up to speed faster

---

## 📞 Support

- **Scripts**: See [scripts/README.md](scripts/README.md)
- **Integrations**: See [api-integrations/README.md](business-knowledge/api-integrations/README.md)
- **General**: Check [CLAUDE.md](CLAUDE.md) for navigation

---

**Built with ❤️ and Claude Code - Your business intelligence system with persistent memory.**

*Last updated: 2026-02-26*
