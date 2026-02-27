# Standard Operating Procedure: Hosting Platform Migration

**Document Type**: SOP
**Category**: Infrastructure & DevOps
**Last Updated**: 2026-02-27
**Version**: 1.0

---

## Purpose

This SOP documents the process for migrating websites between hosting platforms (e.g., Netlify → Vercel, Vercel → Cloudflare, etc.) to ensure zero-downtime migrations and proper cleanup.

---

## Scope

**Applies to:**
- Static websites
- JAMstack applications
- Sites with serverless functions
- Sites with custom domains
- Sites with webhook integrations

**Reference Migration:**
- **Project**: ICP Clarity Website (icpclarity.com)
- **From**: Netlify
- **To**: Vercel
- **Date**: 2026-02-27
- **Duration**: ~2 hours active work + DNS propagation time

---

## Prerequisites

Before starting migration:

- [ ] Access to source hosting platform (Netlify/Vercel/etc.)
- [ ] Access to target hosting platform
- [ ] Access to domain registrar (GoDaddy/Namecheap/etc.)
- [ ] Git repository access
- [ ] Environment variable documentation
- [ ] Webhook/API integration documentation

---

## Phase 1: Pre-Migration Setup (Est. 10-15 min)

### 1.1 Verify Target Platform CLI

```bash
# For Vercel
npm install -g vercel
vercel --version
vercel login

# For Netlify
npm install -g netlify-cli
netlify --version
netlify login
```

### 1.2 Create Backup

```bash
# Backup project directory
cp -r "/path/to/project" "/path/to/project_BACKUP_$(date +%Y%m%d_%H%M%S)"

# Document current deployment
# - Site ID
# - Custom domains
# - Environment variables
# - Deployment URL
```

### 1.3 Document Current Configuration

**Create checklist:**
- Current domain(s)
- SSL certificate status
- Redirects/rewrites
- Security headers
- Environment variables
- Build commands
- Serverless functions
- Webhook URLs
- API integrations

---

## Phase 2: Code Migration (Est. 20-30 min)

### 2.1 Create Target Platform Configuration

**For Vercel** (`vercel.json`):
```json
{
  "version": 2,
  "redirects": [/* ... */],
  "rewrites": [],
  "headers": [/* ... */]
}
```

**For Netlify** (`netlify.toml`):
```toml
[build]
  publish = "."

[[redirects]]
  from = "/old"
  to = "/new"
  status = 301

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
```

### 2.2 Migrate Serverless Functions

**Netlify Functions** (`/netlify/functions/`) →
**Vercel Functions** (`/api/`)

**Convert function format:**

Netlify:
```javascript
exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Success' })
  };
};
```

Vercel:
```javascript
export default async function handler(req, res) {
  return res.status(200).json({ message: 'Success' });
}
```

### 2.3 Update .gitignore

```
# Hosting platform artifacts
.netlify/
.vercel/
```

---

## Phase 3: Deploy & Test (Est. 15-30 min)

### 3.1 Initial Deployment

```bash
cd /path/to/project

# Vercel
vercel --yes

# Netlify
netlify deploy --prod
```

### 3.2 Set Environment Variables

```bash
# Vercel
vercel env add VARIABLE_NAME production
# Enter value when prompted

# Netlify
netlify env:set VARIABLE_NAME value
```

### 3.3 Test on Preview URL

**Test checklist:**
- [ ] Homepage loads (200 OK)
- [ ] All pages load
- [ ] Redirects work
- [ ] Static assets load (CSS, JS, images)
- [ ] Security headers present
- [ ] Serverless functions work (if applicable)
- [ ] Form submissions work
- [ ] Webhook integrations work
- [ ] Analytics tracking works

---

## Phase 4: DNS Migration (Est. 10-20 min + propagation)

### 4.1 Add Custom Domain to Target Platform

**Vercel:**
1. Go to Project → Settings → Domains
2. Add domain: `example.com`
3. Note DNS configuration instructions

**Netlify:**
1. Go to Site → Domain settings
2. Add custom domain
3. Verify DNS requirements

### 4.2 Update DNS at Registrar

**Option A: Change Nameservers (Recommended)**
- Simplest approach
- Target platform manages all DNS
- Auto-SSL provisioning

**Option B: Update DNS Records**
- Keep current registrar
- Update A/CNAME records manually
- More control, but more complex

### 4.3 Verify Domain Configuration

```bash
# Check nameservers
dig example.com NS +short

# Check A record
dig example.com A +short

# Check CNAME (for www)
dig www.example.com CNAME +short
```

### 4.4 Wait for DNS Propagation

- **Typical**: 5-60 minutes
- **Maximum**: 24-48 hours globally
- **Monitor**: https://www.whatsmydns.net/#A/example.com

---

## Phase 5: Cleanup (Est. 10-15 min)

### 5.1 Verify Migration Success

Wait 24-48 hours after DNS propagation, then verify:

- [ ] Custom domain loads from new platform
- [ ] All functionality works
- [ ] Form submissions reach webhooks
- [ ] Analytics show traffic
- [ ] No errors in function logs
- [ ] SSL certificate valid

### 5.2 Delete Old Platform Site

**Important**: Only after verifying everything works!

1. Log into old hosting platform
2. Navigate to site settings
3. Delete site (usually in "Danger Zone")
4. Confirm deletion
5. (Optional) Cancel subscription if no longer needed

### 5.3 Clean Up Local Files

```bash
# Remove old platform artifacts
rm old-platform-config.toml  # netlify.toml, etc.
rm -rf .old-platform/        # .netlify/, etc.
rm -rf old-functions/        # netlify/functions/, etc.

# Commit cleanup
git add -A
git commit -m "Remove old platform artifacts after migration"
git push origin main
```

### 5.4 Update Documentation

- [ ] Update README with new deployment info
- [ ] Update team wiki/docs
- [ ] Update .env.template if needed
- [ ] Document new deployment URL
- [ ] Update CI/CD pipelines (if applicable)

---

## Common Issues & Solutions

### Issue 1: DNS Still Points to Old Platform

**Symptoms**: Domain shows old site even after DNS change
**Cause**: DNS caching
**Solution**:
1. Clear local DNS cache: `sudo dscacheutil -flushcache`
2. Clear browser cache (hard refresh: Cmd+Shift+R)
3. Try incognito/private mode
4. Wait longer for global DNS propagation
5. Test with: `dig @8.8.8.8 example.com A +short`

### Issue 2: Serverless Functions Fail

**Symptoms**: 500 errors, function invocation failed
**Cause**: Function format incompatibility
**Solution**:
1. Check function export format (Netlify vs Vercel)
2. Verify environment variables are set
3. Check function logs in dashboard
4. Test function in isolation
5. Ensure body parsing is correct

### Issue 3: Form Submissions Don't Work

**Symptoms**: Forms submit but data doesn't reach webhook
**Cause**: Webhook URL not updated or CORS issues
**Solution**:
1. Verify webhook URL in code
2. Check Content-Security-Policy headers allow webhook domain
3. Test webhook directly with curl
4. Check webhook logs in Make.com/Clay/etc.
5. Verify CORS settings

### Issue 4: SSL Certificate Issues

**Symptoms**: "Not secure" warning, SSL errors
**Cause**: Certificate not provisioned or DNS not verified
**Solution**:
1. Wait for automatic certificate provisioning (5-10 min)
2. Verify DNS is correct in platform dashboard
3. Click "Refresh" on domain in platform dashboard
4. Check certificate status in platform settings
5. Contact platform support if persists

---

## Time Estimates

**Total Migration Time**: 2-3 hours active work + DNS propagation

| Phase | Active Work | Waiting Time |
|-------|-------------|--------------|
| Phase 1: Pre-Migration | 10-15 min | - |
| Phase 2: Code Migration | 20-30 min | - |
| Phase 3: Deploy & Test | 15-30 min | - |
| Phase 4: DNS Migration | 10-20 min | 5-60 min (propagation) |
| Phase 5: Cleanup | 10-15 min | 24-48 hrs (verification) |
| **Total** | **65-110 min** | **~2 days full cycle** |

---

## Success Criteria

Migration is complete when:

✅ Custom domain loads from new platform (not old)
✅ All pages and assets load correctly
✅ All redirects work
✅ Form submissions work (webhooks receive data)
✅ Security headers present
✅ SSL certificate valid
✅ Analytics tracking works
✅ No errors in function logs (24 hours)
✅ Old platform site deleted
✅ Local artifacts cleaned up
✅ Documentation updated

---

## Rollback Plan

**If migration fails:**

1. **Immediate rollback** (within 48 hours):
   - Revert DNS to old platform
   - Wait for DNS propagation (5-60 min)
   - Old site should start serving again

2. **If old site was deleted**:
   - Redeploy from Git repository
   - Restore configuration from backup
   - Netlify keeps deleted sites for 7 days (can restore)

3. **Prevention**:
   - Keep old platform active until DNS propagates
   - Test thoroughly on preview URL before DNS change
   - Document all configuration before making changes

---

## Related Documents

- [Netlify to Vercel Cleanup Guide](../docs/migrations/netlify-to-vercel/CLEANUP_GUIDE.md)
- [Security Protocols](./security-protocols.md)
- [Documentation Standards](./documentation-standards.md)

---

## Approval & Updates

**Created By**: Claude (AI Assistant)
**Approved By**: [Pending]
**Next Review Date**: 2027-02-27 (1 year)

**Change Log**:
- 2026-02-27 v1.0 - Initial SOP created based on ICP Clarity migration

---

*This SOP is a living document. Update it after each migration to improve the process.*
