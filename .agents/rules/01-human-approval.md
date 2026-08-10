# Rule 01: Human Approval & Escalation Protocol

## 1. Objective
Ensure ultimate human accountability, steering, and verification for all critical architectural, business, security, and deployment decisions.

## 2. Core Policies

### 2.1 Mandatory Human Sign-Off Triggers
Human review and explicit sign-off are strictly required prior to:
1. **Phase Gate Transitions**: Approval of all `*_HANDOFF.json` artifacts.
2. **Scope Alterations**: Any addition, removal, or revision of functional scope in `SCOPE.md`.
3. **Architectural Decisions**: Creation or modification of Architecture Decision Records (ADRs) under `docs/02-design/adr/`.
4. **Security Policy Exemptions**: Introduction of new external integrations, auth flow changes, or security exceptions.
5. **Data Model Breaking Changes**: Destructive schema alterations or data migrations.
6. **Production Deployments**: Authorizing any release execution to staging or production environments.

### 2.2 Escalation Protocol
- When an agent encounters conflicting requirements, architectural impasses, or security risks, it must halt execution.
- The agent must present a structured escalation report containing:
  - Context & Background
  - Problem Statement / Decision Point
  - Options evaluated with pros/cons
  - Recommended course of action
- Execution resumes only after explicit human instruction.

### 2.3 Sign-Off Recording
- Approvals must be recorded with timestamp, approver identifier, and artifact hash in the corresponding handoff JSON.