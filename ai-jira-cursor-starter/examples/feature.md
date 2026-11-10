# Feature: Role-based access control (RBAC)

Existing FastAPI application needs admin and viewer roles. Admin can manage users; viewer can read users but cannot modify them. All unauthorized write attempts return 403. Preserve existing authentication behavior. Record permission-denied events without exposing secrets.

Clarify: role assignment policy, migration/backfill, and whether roles are tenant-specific.
