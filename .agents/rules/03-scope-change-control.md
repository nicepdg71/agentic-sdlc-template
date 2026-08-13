# Rule 03: Scope Management & Change Control

## 1. Objective
Prevent uncontrolled scope creep and ensure that all new requirements, feature modifications, bug fixes, or architecture shifts undergo structured impact analysis, Earliest Impacted Stage re-entry, and human authorization.

## 2. Core Policies

### 2.1 Scope Boundary Enforcement
- All functional capabilities must be explicitly classified under `In Scope` or `Out of Scope` in `docs/00-project-definition/SCOPE.md`.
- Agents must reject or flag any direct implementation request that alters scope without a formal Change Request.

### 2.2 Formal Change Request (CR) Process
All post-baseline or post-release changes must follow the structured change process rather than arbitrary prompts:
1. **Trigger**: Execute `/request-change` to create `docs/changes/CR-XXXX/CHANGE_REQUEST.md`.
2. **Impact Analysis**: Generate `docs/changes/CR-XXXX/IMPACT_ANALYSIS.md` assessing:
   - Requirements (`docs/01-analysis/`)
   - Architecture & Contracts (`docs/02-design/`, `contracts/`)
   - UI/UX Design (`docs/02-design/ui/`)
   - Database / Runtime AI / Security
   - Test Plans & Coverage (`docs/04-test/`)
   - Release Configuration (`docs/05-release/`)
3. **Earliest Impacted Stage Determination**: Identify the earliest affected stage (`DEFINE`, `SPEC`, `DESIGN`, `BUILD PLAN`, `VERIFY`, `RELEASE`).
4. **Human Authorization**: Obtain explicit human decision (`APPROVE CR-XXXX` or `REJECT CR-XXXX: <reason>`).
5. **Artifact STALE Marking**: Upon CR approval, downstream affected artifacts transition from `APPROVED` to `STALE`.
6. **Re-entry & Re-approval**: Execute SDLC workflows starting at the Earliest Impacted Stage and re-obtain all required gates up to G5.
7. **Change Closure**: Run `/close-change-cycle` to verify traceability and seal the change cycle.