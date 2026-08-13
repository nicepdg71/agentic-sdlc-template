# Rule 00: Core Governance & Phase-Gate Enforcement

## 1. Objective
Establish the foundational, non-negotiable principles of the Agentic SDLC framework to ensure order, reliability, and human-in-the-loop governance throughout the engineering lifecycle.

## 2. Core Policies

### 2.1 Sequential Phase Progression & Circular Change Cycle
- **Initial Lifecycle**:
  `DEFINE (G0) -> SPEC (G1) -> DESIGN (G2) -> BUILD (G3) -> VERIFY (G4) -> RELEASE (G5) -> Production v1.0`
- **Repeatable Change Lifecycle**:
  `Production -> CHANGE REQUEST (/request-change) -> IMPACT ANALYSIS -> Human Approval (APPROVE CR-XXXX) -> Re-enter Earliest Impacted Stage -> Re-approve Required Gates -> Production v1.1 -> CLOSE CHANGE CYCLE (/close-change-cycle)`
- Skipping phases or jumping directly to implementation without formal change impact assessment is strictly prohibited ("Agent must never decide: 'this fix is simple so I will just code it'").

### 2.2 Earliest Impacted Stage Re-entry Principle
When a Change Request is approved, re-entry begins strictly at the earliest impacted stage:
| Change Scope | Re-entry Stage | Required Gates for Re-approval |
|---|---|---|
| Business Objective / Project Scope | DEFINE | G0 -> G5 |
| Functional / Non-Functional Requirements | SPEC | G1 -> G5 |
| Architecture / API / Data Model / UI Design | DESIGN | G2 -> G5 |
| Implementation / Code / Bug Fix | BUILD PLAN | G3 -> G5 |
| Test Strategy / Test Cases / Evidence only | VERIFY | G4 -> G5 |
| Deployment Config / Release Plan only | RELEASE | G5 |

### 2.3 Upstream Approval Preservation
- Upper-level approved gates remain valid if unaffected (e.g., Requirement change preserves G0 Project Charter approval).
- Downstream affected artifacts and approvals transition to `STALE` and must be superseded upon re-approval in the new change cycle.
- Historical approvals are permanently preserved in `docs/approvals/{CYCLE_ID}/` without deletion.

### 2.4 Handoff Artifact Sealing & Cycle Scoping
- Every phase transition requires a sealed handoff artifact (`*_HANDOFF.json`).
- All handoff and phase artifacts must record `cycle_id` (e.g. `INIT-001` or `CR-0001`) and `change_id`.
- Subsequent phases consume previous phase handoffs as an immutable baseline.

### 2.5 Strict Scope & Assumption Boundaries
- Agents must never assume undocumented requirements or make unverified decisions on behalf of stakeholders.
- Ambiguities must be surfaced to humans via structured escalation before proceeding.

### 2.6 Auditability & Traceability
- Every automated action, code change, and test run must leave a verifiable audit trail.
- Full traceability is maintained: `Change Request -> Requirements -> Design -> Implementation -> Test -> Release`.