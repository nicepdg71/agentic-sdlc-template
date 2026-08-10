# Rule 05: Git Version Control & Change Hygiene

## 1. Objective
Maintain a clean, traceable, auditable, and reproducible version control history across all branches and commits, enforcing strict branch protection, PR verification, and release commit binding.

## 2. Core Policies

### 2.1 Branching Model & Protected Branches
- Direct feature development, implementation, or direct commits to `main` or any protected branches are strictly prohibited.
- All functional, documentation, and infrastructure changes must be performed on dedicated **Working Branches** (Feature / Fix / Chore branches).
- Feature branches must follow the naming convention: `<type>/<issue-id>-<short-description>` (e.g., `feat/US-102-jwt-auth`, `fix/FR-003-login-validation`).
- Force-push (`git push --force` or `--force-with-lease`) and branch deletion on `main` and protected branches are strictly forbidden.

### 2.2 Conventional & Atomic Commits
- All commit messages must follow the **Conventional Commits** specification:
  - `feat`: A new user-facing feature.
  - `fix`: A bug fix.
  - `docs`: Documentation only changes.
  - `refactor`: A code change that neither fixes a bug nor adds a feature.
  - `test`: Adding missing tests or correcting existing tests.
  - `infra` / `ci`: CI/CD configurations or infrastructure scripts.
  - `chore`: Maintenance tasks, dependency updates.
- Commits must be atomic: each commit should represent a single logical unit of work.
- Every functional commit must reference the relevant User Story or Requirement ID (e.g., `feat(auth): implement token refresh flow (FR-001, US-102)`).

### 2.3 Pull Request & Traceability Governance
- All changes must be integrated into `main` exclusively via Pull Requests.
- Every Pull Request must complete `.github/pull_request_template.md` with explicit traceability:
  - **Requirement ID & User Story**
  - **Acceptance Criteria**
  - **Approved Implementation Plan (`G3`) reference & version**
  - **Real Test & Build Evidence** (Lint, Unit Tests, Build passes)
- Required CI checks (`ci-gate`) must completely **PASS** before any PR can be merged.
- **Agent Self-Merge Prohibition**: Under no circumstances may an Agent self-approve or merge its own Pull Request without explicit **Human Approval** and CODEOWNERS sign-off.
- **CI Integrity**: Modifying, skipping, or deleting tests or required checks to bypass CI/CD failures is strictly prohibited.

### 2.4 Release Candidate Identification & Production Commit Binding
- **G4 Release Candidate Identification**: Every candidate submitted for `G4 (Release Candidate Approval)` must be uniquely and immutably identified by its exact Git Commit SHA.
- **G5 Production Commit Binding**: The exact Release Candidate Git Commit SHA approved under `G5 (Production Release Approval)` in `docs/approvals/G5-production-release.approval.json` must be 100% identical to the commit deployed to Production.
- Deploying unapproved commits or modifying code post-G5 approval without a new baseline and re-approval is strictly forbidden.