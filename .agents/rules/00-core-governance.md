# Rule 00: Core Governance & Phase-Gate Enforcement

## 1. Objective
Establish the foundational, non-negotiable principles of the Agentic SDLC framework to ensure order, reliability, and human-in-the-loop governance throughout the engineering lifecycle.

## 2. Core Policies

### 2.1 Sequential Phase Progression
- The development process follows a strict sequential phase-gate model:
  1. `00-project-definition`
  2. `01-analysis`
  3. `02-design`
  4. `03-implementation`
  5. `04-test`
  6. `05-release`
- Skipping phases or executing tasks out of order without formal escalation is strictly prohibited.

### 2.2 Handoff Artifact Sealing
- Every phase transition requires a validated and sealed handoff artifact (`*_HANDOFF.json`).
- A handoff artifact must list all completed artifacts, verification status (`APPROVED`), and approval metadata.
- Subsequent phases must consume the previous phase's handoff artifact as an immutable baseline.

### 2.3 Strict Scope & Assumption Boundaries
- Agents must never assume undocumented requirements or make unverified decisions on behalf of stakeholders.
- Any ambiguity must be surfaced to human stakeholders through structured inquiry before proceeding.

### 2.4 Auditability & Compliance
- Every automated action, code change, and test run must leave a verifiable audit trail in documentation.
- All agent modifications must comply with repository policies and safety guidelines.