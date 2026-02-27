# Migrations Documentation

This directory contains documentation for platform migrations, infrastructure changes, and system transitions.

## Purpose

Track all migration activities including:
- Hosting platform migrations (Netlify → Vercel, etc.)
- Database migrations
- API platform changes
- Infrastructure transitions
- Service provider switches

## Structure

Each migration gets its own subdirectory with comprehensive documentation:

```
migrations/
├── [platform-name-to-platform-name]/
│   ├── MIGRATION_SUMMARY.md      # Complete chronological record
│   ├── CLEANUP_GUIDE.md          # Post-migration cleanup steps
│   └── [other related docs]
└── README.md (this file)
```

## Current Migrations

### Netlify to Vercel Migration (2026-02-27)
**Project**: ICP Clarity Website (icpclarity.com)
**Status**: ✅ Complete

**Documentation**:
- [Migration Summary](netlify-to-vercel/MIGRATION_SUMMARY.md) - Complete record with timeline, changes, testing results
- [Cleanup Guide](netlify-to-vercel/CLEANUP_GUIDE.md) - Steps to delete old Netlify site and verify migration

**Related SOPs**:
- [Technical SOP](../sops/technical/Netlify_To_Vercel_Migration_Technical_SOP_2026-02-27.md) - Developer implementation guide
- [Executive Summary](../sops/executive/Netlify_To_Vercel_Migration_Executive_Summary_2026-02-27.md) - Management overview
- [Reusable Migration SOP](../../directives/hosting-platform-migration-sop.md) - Generic process for future migrations

---

## Documentation Standards

Each migration should include:
1. **Migration Summary** - Chronological record of all changes
2. **Cleanup Guide** - Post-migration steps and verification
3. **Rollback Plan** - How to revert if needed
4. **Lessons Learned** - What went well, what could be improved

For detailed documentation standards, see [Documentation Standards](../../directives/documentation-standards.md).

---

*Last Updated: 2026-02-27*
