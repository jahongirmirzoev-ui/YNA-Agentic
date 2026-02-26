# YNA Agentic - Automation Scripts

This directory contains all automation scripts for fetching data from external APIs and importing documents into your knowledge base.

## 📋 Quick Start

### 1. Install Dependencies

```bash
cd /Users/jahongirmirzoev/Desktop/YNA_Agentic
pip3 install -r scripts/requirements.txt
```

### 2. Configure Your API Keys

Edit `.env` file and add your API keys:

```bash
# Make.com
MAKECOM_API_KEY=your_makecom_api_key_here

# Clay
CLAY_API_KEY=your_clay_api_key_here

# Airtable
AIRTABLE_PAT=your_airtable_personal_access_token_here
```

### 3. Configure Filters

Edit `config/integration-filters.json` to specify which folders/workspaces to fetch:

**Make.com - Specify Folders:**
```json
"include_folders": [
  "YNA Agentic - Marketing",
  "YNA Agentic - Sales"
]
```

**Clay - Specify Tables:**
```json
"include_tables": [
  "YNA Lead Enrichment",
  "YNA Company Research"
]
```

**Airtable - Add Base IDs:**
```json
"bases": [
  {
    "base_id": "appXXXXXXXXXXXXXX",
    "base_name": "YNA CRM Main"
  }
]
```

### 4. Run the Update Script

```bash
./scripts/update-knowledge-base.sh
```

This will fetch all data and generate documentation automatically!

---

## 🛠️ Individual Scripts

### Fetch Make.com Scenarios

**Purpose**: Fetches scenarios from specific folders and generates scenario documentation.

**Usage**:
```bash
python3 scripts/fetch-makecom-scenarios.py
```

**Output**:
- `business-knowledge/api-integrations/makecom/scenarios/scenario-index.md`
- `business-knowledge/api-integrations/makecom/scenarios/scenarios-data.json` (backup)

**What It Does**:
1. Reads your Make.com API key from `.env`
2. Fetches all scenarios
3. Filters by folders/tags specified in `config/integration-filters.json`
4. Categorizes scenarios (Lead Management, Sales, Marketing, etc.)
5. Generates markdown documentation
6. Saves JSON backup

**Configuration**:
```json
{
  "makecom": {
    "enabled": true,
    "organization_id": "your_org_id",
    "filters": {
      "include_folders": ["YNA Agentic - Marketing"],
      "exclude_folders": ["Archive", "Testing"],
      "include_tags": ["YNA", "production"]
    }
  }
}
```

---

### Fetch Clay Tables

**Purpose**: Fetches table schemas from specific workspaces and generates documentation.

**Usage**:
```bash
python3 scripts/fetch-clay-tables.py
```

**Output**:
- `business-knowledge/api-integrations/clay/tables/table-schemas.md`
- `business-knowledge/api-integrations/clay/tables/tables-data.json` (backup)

**What It Does**:
1. Reads your Clay API key from `.env`
2. Fetches tables from specified workspace
3. Filters by table names specified in config
4. Documents table schemas, enrichment providers, outputs
5. Generates markdown documentation

**Configuration**:
```json
{
  "clay": {
    "enabled": true,
    "workspace_id": "your_workspace_id",
    "workspace_name": "YNA Agentic",
    "filters": {
      "include_tables": ["YNA Lead Enrichment"],
      "exclude_tables": ["Test", "Archive"]
    }
  }
}
```

---

### Fetch Airtable Bases

**Purpose**: Fetches base schemas for specific bases and generates documentation.

**Usage**:
```bash
python3 scripts/fetch-airtable-bases.py
```

**Output**:
- `business-knowledge/api-integrations/airtable/bases/base-inventory.md`
- `business-knowledge/api-integrations/airtable/bases/bases-data.json` (backup)

**What It Does**:
1. Reads your Airtable PAT from `.env`
2. Fetches schema for each configured base
3. Documents all tables, fields, and field types
4. Filters tables per base configuration
5. Generates comprehensive markdown documentation

**Configuration**:
```json
{
  "airtable": {
    "enabled": true,
    "bases": [
      {
        "base_id": "appXXXXXXXXXXXXXX",
        "base_name": "YNA CRM Main",
        "include_tables": ["all"],
        "exclude_tables": ["Archive"]
      }
    ]
  }
}
```

**Getting Base IDs**:
- Go to Airtable base
- Look at URL: `https://airtable.com/appXXXXXXXXXXXXXX/...`
- Copy the `appXXXXXXXXXXXXXX` part

---

### Import Documents

**Purpose**: Converts Word/PDF documents to Markdown and imports into knowledge base.

**Usage**:

**Import Single File**:
```bash
python3 scripts/import-documents.py Brand_Guidelines.docx
```

**Import to Specific Department**:
```bash
python3 scripts/import-documents.py Sales_Playbook.docx --department sales
```

**Import Entire Directory**:
```bash
python3 scripts/import-documents.py ~/Desktop/YNA_Documents/ --directory
```

**Import with Custom Name**:
```bash
python3 scripts/import-documents.py guide.docx --department marketing --output brand-guidelines.md
```

**Supported File Types**:
- `.docx` - Microsoft Word documents
- `.pdf` - PDF documents
- `.txt` - Plain text files

**Output Locations**:
- **Shared**: `business-knowledge/documents/`
- **Department-specific**: `business-knowledge/departments/{dept}/documents/`

**What It Does**:
1. Reads Word/PDF document
2. Converts to clean Markdown format
3. Preserves headings, lists, tables
4. Saves to appropriate location
5. Auto-links from department `memory.md` file

**Departments Available**:
- `marketing`
- `sales`
- `customer-service`
- `crm`
- `website`
- `shared` (default)

---

### Update Knowledge Base (Main Script)

**Purpose**: Runs all fetch scripts and updates entire knowledge base.

**Usage**:
```bash
./scripts/update-knowledge-base.sh
```

**What It Does**:
1. Checks dependencies are installed
2. Verifies `.env` file exists
3. Runs Make.com fetcher (if enabled)
4. Runs Clay fetcher (if enabled)
5. Runs Airtable fetcher (if enabled)
6. Updates CLAUDE.md timestamp
7. Shows summary of what was updated

**When to Run**:
- **Daily**: Automated via cron (optional)
- **After Changes**: When you add/modify scenarios, tables, or bases
- **Initial Setup**: First time to populate all documentation

---

## 🔐 Security Notes

### API Keys

**Never commit API keys to git!**
- `.env` is gitignored
- Only `.env.template` is committed
- API keys stay local only

**Webhook URLs**:
- Not fetched by default (security)
- Store in `.env` if needed
- Reference as `${MAKECOM_WEBHOOK_MARKETING}` in config

### Credentials

**Make.com**:
- Get API key: Settings → API → Create Token
- Scope: Read scenarios, connections

**Clay**:
- Get API key: Dashboard → Settings → API Keys
- Scope: Read tables

**Airtable**:
- Get PAT: Account → Developer Hub → Personal Access Tokens
- Scopes: `data.records:read`, `schema.bases:read`

---

## 📁 File Structure

```
scripts/
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── fetch-makecom-scenarios.py      # Fetch Make.com scenarios
├── fetch-clay-tables.py            # Fetch Clay tables
├── fetch-airtable-bases.py         # Fetch Airtable bases
├── import-documents.py             # Import Word/PDF docs
└── update-knowledge-base.sh        # Main update script
```

---

## 🎯 Common Workflows

### First-Time Setup

```bash
# 1. Install dependencies
pip3 install -r scripts/requirements.txt

# 2. Copy environment template
cp .env.template .env

# 3. Edit .env and add your API keys
nano .env

# 4. Edit config to specify folders/workspaces
nano config/integration-filters.json

# 5. Run first update
./scripts/update-knowledge-base.sh

# 6. Review generated documentation
```

### Daily Updates

```bash
# Run update script
./scripts/update-knowledge-base.sh
```

### Import Documents

```bash
# Import all docs from a folder
python3 scripts/import-documents.py ~/Desktop/YNA_Docs/ --directory

# Import specific doc to marketing
python3 scripts/import-documents.py Brand_Guide.docx --department marketing
```

### Update Specific Integration

```bash
# Just Make.com
python3 scripts/fetch-makecom-scenarios.py

# Just Clay
python3 scripts/fetch-clay-tables.py

# Just Airtable
python3 scripts/fetch-airtable-bases.py
```

---

## 🔄 Automation Setup

### Daily Auto-Update (Optional)

**Using Cron (Mac/Linux)**:

```bash
# Edit crontab
crontab -e

# Add this line (runs daily at 8am)
0 8 * * * cd /Users/jahongirmirzoev/Desktop/YNA_Agentic && ./scripts/update-knowledge-base.sh >> .tmp/cron.log 2>&1
```

**Using Launchd (Mac)**:

Create `~/Library/LaunchAgents/com.yna.knowledge-update.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yna.knowledge-update</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/jahongirmirzoev/Desktop/YNA_Agentic/scripts/update-knowledge-base.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.yna.knowledge-update.plist
```

---

## 🐛 Troubleshooting

### "Module not found" Error

```bash
# Install dependencies
pip3 install -r scripts/requirements.txt
```

### "API Key not found" Error

- Check `.env` file exists
- Verify API key is correct format
- Ensure no extra spaces around `=`

### "No scenarios/tables found"

- Check API key has correct permissions
- Verify folder/workspace names in config
- Check organization/workspace IDs

### "Permission denied" on Scripts

```bash
# Make scripts executable
chmod +x scripts/*.sh scripts/*.py
```

### Empty Documentation Generated

- Check filters in `config/integration-filters.json`
- Verify folder names match exactly
- Try removing filters to see all data first

---

## 📊 Output Examples

### Make.com Scenario Index

```markdown
| Scenario Name | Trigger | Status | Last Run | Folder |
|--------------|---------|--------|----------|--------|
| Lead Notification | Webhook | ✅ Active | 2026-02-26 | YNA - Marketing |
| Daily Sales Report | Schedule | ✅ Active | 2026-02-26 | YNA - Sales |
```

### Clay Table Schema

```markdown
### Table: YNA Lead Enrichment
**Purpose**: Enrich contact information from website forms
**Record Count**: 1,234
**Output**: Airtable CRM Main - Contacts table
```

### Airtable Base Inventory

```markdown
## Base: YNA CRM Main
**Tables**: 4 (Contacts, Companies, Deals, Activities)
**Connected Integrations**: Clay, Make.com
```

---

## 🎓 Learning Resources

- **Make.com API**: https://www.make.com/en/api-documentation
- **Clay API**: https://clay.com/docs
- **Airtable API**: https://airtable.com/developers/web/api/introduction

---

## ✅ Next Steps

After running the scripts:

1. **Review Generated Documentation**
   - Check `business-knowledge/api-integrations/` files
   - Verify data looks correct

2. **Add Manual Notes**
   - Add descriptions to scenarios
   - Document enrichment providers in Clay tables
   - Note automation details in Airtable

3. **Test Claude Integration**
   - Start new Claude session
   - Ask: "What Make.com scenarios do I have?"
   - Claude will read the generated documentation!

4. **Set Up Daily Updates**
   - Configure cron job (optional)
   - Or run manually when things change

5. **Import Your Documents**
   - Use `import-documents.py` to add existing docs
   - Claude will be able to reference them

---

*For issues or questions, check the main project README or troubleshooting guide.*
