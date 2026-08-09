# Rollback Plan

## Triggers for Rollback
- Critical error rate > 1% post-deployment.
- Major security vulnerability discovered.
- Severe performance degradation.

## Rollback Procedure
1. Revert deployment image/tag to previous stable version.
2. Execute reverse database migration script if schema changed.
3. Validate system health and notify stakeholders.
