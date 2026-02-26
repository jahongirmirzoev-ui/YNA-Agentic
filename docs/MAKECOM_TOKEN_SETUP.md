# Make.com API Token Setup Guide

## Problem
Getting 401 Unauthorized error when fetching Make.com scenarios.

## Solution
Create a new API token with the correct scopes.

---

## Step-by-Step Instructions

### 1. Open Make.com
Go to: https://www.make.com/

### 2. Navigate to API Settings
1. Click your **profile picture/avatar** (bottom-left corner)
2. Click **Profile**
3. Click the **API** tab

### 3. Create New Token
1. Click **"Add token"** button
2. Enter a label: `YNA Agentic ICP Clarity`

### 4. SELECT THESE SCOPES (CRITICAL!)
✅ Check these boxes:
- **scenarios:read** - Required to read scenarios
- **connections:read** - Helpful for connection info
- **organizations:read** - Optional but recommended
- **teams:read** - Optional but recommended

⚠️ **IMPORTANT**: The token MUST have `scenarios:read` checked or it won't work!

### 5. Save and Copy Token
1. Click **Save**
2. **IMMEDIATELY COPY** the generated token (you won't see it again!)
3. The token will look like: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### 6. Update .env File
Replace the token in your .env file:

```bash
# Open .env file
open /Users/jahongirmirzoev/Desktop/YNA_Agentic/.env

# Replace this line:
MAKECOM_API_KEY=8854096e-3c89-4604-ab33-cd282e4d4826

# With your new token:
MAKECOM_API_KEY=your_new_token_here
```

### 7. Test
Run this command:
```bash
cd /Users/jahongirmirzoev/Desktop/YNA_Agentic
python3 scripts/fetch-makecom-scenarios.py
```

---

## Alternative: Get Organization ID (Optional)

While in Make.com:
1. Go to **Settings** → **Organization**
2. Copy your **Organization ID**
3. Add it to `config/integration-filters.json`:
   ```json
   "organization_id": "your_org_id_here"
   ```

---

## What If It Still Doesn't Work?

### Check Token Status
1. Go back to Profile → API tab
2. Look for your token in the list
3. Verify it shows as "Active"
4. Check the scopes listed - should include `scenarios:read`

### Verify Token Format
- Should be UUID format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- No spaces before or after
- No quotes around it in .env file

### Common Issues
- ❌ Token created without `scenarios:read` scope
- ❌ Token not active
- ❌ Token copied with extra spaces
- ❌ Token expired or deleted

---

## Need Help?
Paste the new token in the chat and I'll update the .env file for you automatically.
