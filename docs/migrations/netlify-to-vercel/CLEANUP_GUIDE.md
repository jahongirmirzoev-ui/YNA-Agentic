# Netlify to Vercel Migration - Cleanup Guide

**Date**: 2026-02-27
**Project**: ICP Clarity Website
**Migrated From**: Netlify
**Migrated To**: Vercel

---

## Netlify Account Cleanup

### What to Delete on Netlify Dashboard

**Site Information:**
- **Site Name**: icp-clarity-deploy
- **Site ID**: ba0884a7-7983-47db-a82f-3820826d9e55
- **Current URL**: https://symphonious-tanuki-59c36d.netlify.app
- **Custom Domain**: icpclarity.com (now on Vercel)

### Steps to Delete Netlify Site:

1. **Log into Netlify**: https://app.netlify.com
2. **Navigate to Site**: Go to "Sites" → "icp-clarity-deploy"
3. **Go to Site Settings**: Click "Site settings" in the top menu
4. **Scroll to Danger Zone**: At the bottom of the General settings page
5. **Delete Site**:
   - Click "Delete this site"
   - Type the site name to confirm: `icp-clarity-deploy`
   - Click "Delete"

### Optional: Keep or Cancel Netlify Account

**Option A: Keep Account (Free Tier)**
- No action needed
- Free tier remains available for future projects
- No cost

**Option B: Downgrade/Cancel Account**
- Go to User Settings → Billing
- Review any active subscriptions
- Cancel if no longer needed

### What Was on Netlify (Now on Vercel):

- ✅ Static website files (HTML, CSS, JS)
- ✅ Custom domain: icpclarity.com
- ✅ SSL certificate (auto-provisioned)
- ⚠️ Serverless function (not used - webhooks are client-side)
- ✅ Redirects and rewrites
- ✅ Security headers

---

## Local Files Cleanup

### Files to Remove:

**Netlify Configuration:**
- `/netlify.toml` - Replaced by `vercel.json`
- `/.netlify/` - Netlify CLI cache and state
- `/netlify/` - Old functions directory (not used)

**Keep These Files:**
- ✅ `vercel.json` - New configuration
- ✅ `/api/` - Vercel functions directory (for future use)
- ✅ `.vercel/` - Vercel CLI state (in .gitignore)

### Commands to Clean Up:

```bash
cd "/Users/jahongirmirzoev/Desktop/ICP CLarity Website"

# Remove Netlify configuration
rm netlify.toml

# Remove Netlify cache and state
rm -rf .netlify/

# Remove old Netlify functions directory (if exists)
rm -rf netlify/

# Commit cleanup
git add -A
git commit -m "Remove Netlify artifacts after migration to Vercel"
git push origin main
```

---

## Verification Checklist

After cleanup, verify:

- [ ] Site loads at https://icpclarity.com (once DNS propagates)
- [ ] Site loads at https://icp-clarity.vercel.app
- [ ] Assessment page works: https://icpclarity.com/assessment.html
- [ ] Form submissions reach Make.com webhook
- [ ] Form submissions reach Clay webhook
- [ ] All redirects work (v8_2, v9, mobile-test)
- [ ] SSL certificate valid (green padlock)
- [ ] Security headers present (check securityheaders.com)
- [ ] No Netlify references in code
- [ ] Git repository clean (no .netlify artifacts)

---

## Rollback Plan (If Needed)

**If something goes wrong after Netlify deletion:**

1. **Redeploy to Netlify**:
   - Create new site on Netlify
   - Connect GitHub repository
   - Deploy from main branch
   - Add netlify.toml back (from backup)

2. **Revert DNS**:
   - Log into GoDaddy
   - Change nameservers back to GoDaddy defaults
   - Add A record pointing to new Netlify site

3. **Restore from Backup**:
   - Backup location: `/Users/jahongirmirzoev/Desktop/ICP CLarity Website_BACKUP_[timestamp]`

**Note**: Netlify keeps deleted sites for 7 days - can restore within that window.

---

## Migration Success Criteria

✅ **Completed when:**
- icpclarity.com loads from Vercel (not Netlify)
- All pages and functionality work
- Form submissions work (Make.com + Clay)
- DNS fully propagated globally
- Netlify site deleted
- Local Netlify files removed
- Documentation updated

---

## Support Resources

- **Vercel Dashboard**: https://vercel.com/jahongir-yournextautos-projects/icp-clarity
- **Netlify Dashboard**: https://app.netlify.com
- **GoDaddy DNS**: https://dcc.godaddy.com/control/dns
- **DNS Propagation Check**: https://www.whatsmydns.net/#A/icpclarity.com

---

*Last Updated: 2026-02-27*
