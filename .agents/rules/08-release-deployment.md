# Rule 08: Release Management & Deployment Governance

## 1. Objective
Establish rigorous release gating, checklist compliance, rollback preparedness, auditability, and absolute commit-level production integrity to ensure zero-defect, authorized deployments.

## 2. Core Policies

### 2.1 Release Checklist Completion
- No release candidate may be promoted to production without 100% completion of `docs/05-release/RELEASE_CHECKLIST.md`.
- All checklist items (unit/integration test passes, security scan clearances, environment config readiness) must be verified.

### 2.2 Mandatory Rollback Plan & Execution
- Every release must have a documented, tested, and actionable `docs/05-release/ROLLBACK_PLAN.md`.
- Rollback plans must define:
  - Trigger conditions for initiating a rollback (Smoke test failure, error rate surge, data integrity risks).
  - Step-by-step rollback procedure (including database migration rollback and traffic diversion).
  - Verification steps to confirm system health post-rollback.
- In the event of a deployment or smoke test failure, the rollback procedure must be strictly followed immediately.

### 2.3 Transparent Release Documentation & Evidence Recording
- Clear, user-facing `docs/05-release/RELEASE_NOTES.md` must be generated, summarizing features, bug fixes, breaking changes, and migration instructions.
- Deployment operational steps must be outlined in `docs/05-release/RELEASE_PLAN.md`.
- Deployment and smoke test execution results must be permanently recorded into the official Release Evidence (`docs/05-release/RELEASE_HANDOFF.json`).

### 2.4 Production Release Integrity & Commit Binding
- **Release Candidate Identification**: Every Production Release Candidate must be unambiguously identified by its **Semantic Version** and **exact Git Commit SHA**.
- **G5 Approval Record Match**: The release candidate (`version` and `commit`) specified in `docs/approvals/G5-production-release.approval.json` must be 100% identical to the inputs provided to the Production Deployment Workflow.
- **Checked-out SHA Verification**: The actual Git Commit SHA checked out in the Production Deployment Workflow must strictly match the G5-approved commit SHA.
- **No Floating References**: Using floating references such as `latest`, `HEAD`, `main`, or arbitrary recent commits to replace an approved release candidate is strictly prohibited.
- **Separation of Merge and Release**: Merging code into `main` does NOT constitute a `G5 (Production Release Approval)`.
- **Fail-Closed Gate Enforcement**: Any execution of the Production Deployment Workflow without a verified, signed `G5 Approval Record` and `APPROVED` `RELEASE_HANDOFF.json` must fail immediately and be blocked from entering the deployment step.
- **Mandatory Post-Deployment Smoke Test**: Immediately following deployment, an automated Smoke Test (`scripts/smoke-test.sh production`) must be executed to verify critical user paths and operational health.