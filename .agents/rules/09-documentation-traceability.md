# Rule 09: End-to-End Documentation Traceability

## 1. Objective
Guarantee full bidirectional auditability from top-level business requirements down to source code changes, automated tests, and release artifacts.

## 2. Traceability Chain

Every software artifact must be linked according to the following lineage:

```
[Project Charter & Scope]
          │
          ▼
[System Requirements (REQ-xxx)]
          │
          ▼
[User Stories (US-xxx) & Acceptance Criteria (AC-xxx)]
          │
          ▼
[Architecture & Interface Contracts (ARCH-xxx / API-xxx)]
          │
          ▼
[Implementation Plan Tasks (TASK-xxx)]
          │
          ▼
[Source Code Commits (feat/fix referencing US/REQ)]
          │
          ▼
[Test Cases (TC-xxx) & Test Results]
          │
          ▼
[Release Notes & Deployment Package]
```

## 3. Core Policies

### 3.1 Traceability Matrix Maintenance
- The primary artifact for tracking lineage is `docs/01-analysis/TRACEABILITY_MATRIX.md`.
- It must map each Requirement ID (`REQ-*`) to its corresponding User Story (`US-*`), Architecture component, Test Case (`TC-*`), and Verification Status.

### 3.2 Orphan Code & Spec Prohibition
- **No Orphan Code**: Code must not exist without a corresponding requirement or approved maintenance task.
- **No Orphan Requirements**: Every requirement must have mapped test cases and implementation tasks before phase completion.

### 3.3 Continuous Matrix Verification
- QA and Release agents must verify the completeness of the Traceability Matrix during phase gating. Any unlinked or unverified items will block the phase transition.