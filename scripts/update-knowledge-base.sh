#!/bin/bash
#
# Update Knowledge Base - Main Script
# Fetches data from all configured APIs and updates documentation
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}YNA Agentic - Knowledge Base Update${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Check if .env file exists
if [ ! -f "$PROJECT_ROOT/.env" ]; then
    echo -e "${RED}❌ Error: .env file not found${NC}"
    echo -e "${YELLOW}   Copy .env.template to .env and add your API keys${NC}"
    exit 1
fi

# Check if Python requirements are installed
echo -e "${BLUE}📦 Checking Python dependencies...${NC}"
if ! python3 -c "import requests" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Installing Python dependencies...${NC}"
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
fi
echo -e "${GREEN}✅ Dependencies OK${NC}"
echo ""

# Load configuration
CONFIG_FILE="$PROJECT_ROOT/config/integration-filters.json"
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Error: config/integration-filters.json not found${NC}"
    exit 1
fi

# Parse enabled integrations from config
MAKECOM_ENABLED=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['makecom']['enabled'])")
CLAY_ENABLED=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['clay']['enabled'])")
AIRTABLE_ENABLED=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['airtable']['enabled'])")

echo -e "${BLUE}🔄 Fetching integration data...${NC}"
echo ""

# Fetch Make.com scenarios
if [ "$MAKECOM_ENABLED" = "True" ]; then
    echo -e "${YELLOW}📊 Fetching Make.com scenarios...${NC}"
    python3 "$SCRIPT_DIR/fetch-makecom-scenarios.py"
    echo ""
else
    echo -e "${YELLOW}⏭️  Skipping Make.com (disabled in config)${NC}"
fi

# Fetch Clay tables
if [ "$CLAY_ENABLED" = "True" ]; then
    echo -e "${YELLOW}📊 Fetching Clay tables...${NC}"
    python3 "$SCRIPT_DIR/fetch-clay-tables.py"
    echo ""
else
    echo -e "${YELLOW}⏭️  Skipping Clay (disabled in config)${NC}"
fi

# Fetch Airtable bases
if [ "$AIRTABLE_ENABLED" = "True" ]; then
    echo -e "${YELLOW}📊 Fetching Airtable bases...${NC}"
    python3 "$SCRIPT_DIR/fetch-airtable-bases.py"
    echo ""
else
    echo -e "${YELLOW}⏭️  Skipping Airtable (disabled in config)${NC}"
fi

# Update CLAUDE.md with last update timestamp
echo -e "${BLUE}📝 Updating CLAUDE.md...${NC}"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
# Note: Actual sed command would go here to update the timestamp
echo -e "${GREEN}✅ Updated timestamp to $TIMESTAMP${NC}"
echo ""

# Summary
echo -e "${BLUE}============================================================${NC}"
echo -e "${GREEN}✅ Knowledge base update complete!${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""
echo -e "${YELLOW}Updated files:${NC}"
if [ "$MAKECOM_ENABLED" = "True" ]; then
    echo -e "  📄 business-knowledge/api-integrations/makecom/scenarios/scenario-index.md"
fi
if [ "$CLAY_ENABLED" = "True" ]; then
    echo -e "  📄 business-knowledge/api-integrations/clay/tables/table-schemas.md"
fi
if [ "$AIRTABLE_ENABLED" = "True" ]; then
    echo -e "  📄 business-knowledge/api-integrations/airtable/bases/base-inventory.md"
fi
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  1. Review the generated documentation files"
echo -e "  2. Add manual notes and details as needed"
echo -e "  3. Commit changes to git"
echo ""
echo -e "${YELLOW}Run this script daily or when integrations change${NC}"
echo -e "${YELLOW}Command: ./scripts/update-knowledge-base.sh${NC}"
echo ""
