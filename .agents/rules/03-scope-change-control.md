# Rule 03: Scope Management & Change Control

## 1. Objective
Prevent uncontrolled scope creep and ensure that all new requirements, feature modifications, or scope reductions undergo rigorous impact analysis and human authorization.

## 2. Core Policies

### 2.1 Scope Boundary Enforcement
- All functional capabilities must be explicitly classified under `In Scope` or `Out of Scope` in `docs/00-project-definition/SCOPE.md`.
- Agents must reject or flag any implementation request that addresses out-of-scope items without formal approval.

### 2.2 Scope Change Request (SCR) Process
When a scope change is proposed:
1. **Document the Request**: Record the change proposal, rationale, and business justification.
2. **Impact Analysis**: Assess impacts on:
   - Architecture & Contracts (`docs/02-design/`, `contracts/`)
   - Test Plans & Coverage (`docs/04-test/`)
   - Security & Performance profiles
   - Delivery Timeline & Dependencies
3. **Traceability Update**: Update `docs/01-analysis/TRACEABILITY_MATRIX.md` to reflect additions or deprecations.
4. **Formal Approval**: Obtain human sign-off before modifying implementation plans or code.