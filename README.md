# Agentic SDLC Template (v1.1.0)

A structured, governance-first Software Development Life Cycle (SDLC) framework optimized for AI coding agents and human-agent collaboration.

## Overview
This template establishes a standardized directory layout, agent governance rules, workflows, prompts, skills, contracts, and phase-gate documentation. 

**Version 1.1 Enhancements:**
- **Repeatable Change Cycle**: Upgrades the linear SDLC to a circular lifecycle (`/request-change` -> Impact Analysis -> Earliest Impacted Stage Re-entry -> Gate Re-approvals -> `/close-change-cycle`).
- **UI Design Decision & Google Stitch MCP Integration**: Automated UI applicability assessment in DESIGN (`/design-system`), human-in-the-loop tool decision (`USE_STITCH`), and fail-closed Stitch MCP design synchronization.
- **Cycle-scoped Approvals & STALE State**: Archival of approval records in `docs/approvals/{CYCLE_ID}/` with downstream artifact staleness tracking.

---

## Project Structure
- `.agents/`: Agent configurations, governance rules, workflows (12), prompts, and skills (15).
  - `rules/`: Non-negotiable phase-gate and governance rules (Rules 00 ~ 09).
  - `workflows/`: Standard operational runbooks for initial SDLC and change cycles.
  - `skills/`: Specialized capabilities (Change Impact Analysis, Stitch MCP, Architecture, etc.).
  - `templates/`: Structured templates for phase artifacts, approvals, changes, and UI design.
  - `schemas/`: JSON schemas for approval records and stage handoffs.
- `docs/`: Phase-by-phase engineering artifacts, change logs, and handoff contracts.
  - `00-project-definition/` ~ `05-release/`
  - `changes/`: `CHANGE_REGISTER.md` and cycle folders (`CR-XXXX/`).
  - `approvals/`: Cycle-scoped human sign-offs (`INIT-001/`, `CR-0001/`, etc.).
- `contracts/`: Interface definitions (API, Events, AI schemas).
- `src/`: Source code implementation.
- `tests/`: Test suites (unit, integration, e2e, security, UI verification).
- `infra/`: Infrastructure-as-code and environment configurations.
- `.github/`: CI/CD workflows, issue templates, PR templates, and validation scripts.

---

## SDLC Workflows

### 1. Initial Cycle (`INIT-001`)
1. `/define-project` -> G0: Project Definition Approval
2. `/analyze-requirements` -> G1: Requirement Baseline Approval
3. `/design-system` (with UI Applicability & Stitch Decision) -> G2: Design Baseline Approval
4. `/plan-implementation` -> G3: Implementation Plan Approval
5. `/implement-change` -> Implementation & Test Execution
6. `/verify-release-candidate` (with UI Verification) -> G4: Release Candidate Approval
7. `/prepare-release` -> G5: Production Release Approval
8. `/deploy-production` -> Production v1.0.0

### 2. Repeatable Change Cycle (`CR-XXXX`)
1. `/request-change`: Receive change request, perform Impact Analysis, determine Earliest Impacted Stage.
2. `APPROVE CR-XXXX`: Human authorizes change, marks downstream artifacts as `STALE`.
3. Re-enter Earliest Impacted Stage (`DEFINE`, `SPEC`, `DESIGN`, `BUILD PLAN`, `VERIFY`, or `RELEASE`).
4. Re-obtain required gates up to G5.
5. `/deploy-production`: Deploy updated release (e.g. v1.1.0).
6. `/close-change-cycle`: Formally verify traceability and seal the Change Request as `CLOSED`.

---

## Governance & Phase Gate Rules
- **Rule 00**: Core Governance & Phase-Gate Enforcement (Earliest Impacted Stage Re-entry)
- **Rule 01**: Human Approval & Escalation Protocol (`APPROVE/REJECT G<n>`, `APPROVE/REJECT CR-XXXX`, UI Decisions)
- **Rule 02**: Single Source of Truth (`Requirements -> UI Handoff -> Stitch Ref -> Contracts -> Plan -> Code`)
- **Rule 03**: Scope Management & Change Control (`/request-change`, Impact Analysis, STALE states)
- **Rule 04**: Security, Secrets & Credential Protection
- **Rule 05**: Git Branching & Change Control
- **Rule 06**: Data & Database Governance
- **Rule 07**: Testing & Evidence-based Verification
- **Rule 08**: Release & Deployment Protection
- **Rule 09**: End-to-End Documentation Traceability

---

## Verification & Integrity Check
Run the governance integrity validator:
```bash
python .github/scripts/validate_agentic_sdlc.py
```
