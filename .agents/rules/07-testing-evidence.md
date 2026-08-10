# Rule 07: Testing & Verification Evidence

## 1. Objective
Mandate empirical, automated verification for all code changes so that quality, functionality, and regression immunity are proven prior to release gating.

## 2. Core Policies

### 2.1 Test-First Mindset & Complete Coverage
- Every feature, enhancement, or bug fix must be accompanied by automated tests:
  - **Unit Tests**: Test business logic and boundary conditions in isolation.
  - **Integration Tests**: Verify database queries, API endpoints, and inter-service communications.
  - **Contract Tests**: Validate conformance to schemas under `contracts/`.

### 2.2 Acceptance Criteria Verification
- Every acceptance criterion documented in `docs/01-analysis/ACCEPTANCE_CRITERIA.md` must have at least one dedicated test case in `docs/04-test/TEST_CASES.md`.
- No task is complete until corresponding test cases pass successfully.

### 2.3 Empirical Evidence Recording
- Test execution outputs, logs, pass/fail summaries, and code coverage metrics must be systematically recorded in `docs/04-test/TEST_REPORT.md`.
- Claims of "code working" without logged test evidence will be rejected during Phase 04 gate review.

### 2.4 Regression & Flaky Test Prevention
- Tests must be deterministic, self-contained, and idempotent.
- Flaky or environment-dependent tests must be resolved immediately before code merge.