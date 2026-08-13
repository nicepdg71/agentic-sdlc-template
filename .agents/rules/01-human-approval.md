# Rule 01: Human Approval & Escalation Protocol

## 1. Objective
Ensure ultimate human accountability, steering, and verification for all critical architectural, business, security, change, and deployment decisions.

## 2. Core Policies

### 2.1 Mandatory Human Sign-Off Triggers
Human review and explicit sign-off are strictly required prior to:
1. **Phase Gate Transitions (G0 ~ G5)**: Approval of all `*_HANDOFF.json` artifacts.
2. **Change Request Authorization**: Authorizing any change request via `APPROVE CR-XXXX` or `REJECT CR-XXXX: <reason>`.
3. **UI Design Decision**: Approving UI tool adoption (`USE_STITCH`, `SKIP_STITCH`, `USE_OTHER_UI_TOOL: <tool>`) following UI Applicability Assessment.
4. **Scope Alterations**: Any addition, removal, or revision of functional scope in `SCOPE.md`.
5. **Architectural Decisions**: Creation or modification of Architecture Decision Records (ADRs) under `docs/02-design/adr/`.
6. **Security Policy Exemptions**: Introduction of new external integrations, auth flow changes, or security exceptions.
7. **Data Model Breaking Changes**: Destructive schema alterations or data migrations.
8. **Production Deployments**: Authorizing any release execution to staging or production environments.

### 2.2 Gate Decision Commands
- Gate Approvals:
  - `APPROVE G<n>`
  - `APPROVE_WITH_COMMENTS G<n>: <comments>`
  - `REJECT G<n>: <reason>`
- Change Authorization Decisions:
  - `APPROVE CR-XXXX`
  - `REJECT CR-XXXX: <reason>`
- UI Design Decisions:
  - `USE_STITCH`
  - `SKIP_STITCH`
  - `USE_OTHER_UI_TOOL: <tool>`

### 2.3 Non-Auto-Execution (Stop on Gate)
- Receiving a human approval or decision **never** automatically triggers the next stage or workflow. The agent must report the status and recommend the next command for human invocation.

### 2.4 Escalation Protocol
- When an agent encounters conflicting requirements, architectural impasses, or security risks, it must halt execution.
- The agent must present a structured escalation report containing:
  - Context & Background
  - Problem Statement / Decision Point
  - Options evaluated with pros/cons
  - Recommended course of action
- Execution resumes only after explicit human instruction.

### 2.5 Sign-Off Recording
- Approvals must be recorded in `docs/approvals/{CYCLE_ID}/` with timestamp, approver identifier, cycle ID, and artifact hash in the corresponding approval record JSON.