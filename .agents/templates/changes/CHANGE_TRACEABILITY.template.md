---
artifact_id: "TR-<CR_ID>"
project_id: "<PROJECT_ID>"
cycle_id: "<CR_ID>"
change_id: "<CR_ID>"
stage: "CHANGE_CONTROL"
artifact_type: "TRACEABILITY"
version: "1.0"
status: "DRAFT"
baseline_version: "<CURRENT_PRODUCTION_VERSION>"
owner: "@analyst"
---

# Change Traceability Matrix: <CR_ID>

## Lineage Chain
`Change Request (CR-xxxx) -> Requirements -> Acceptance Criteria -> Design / UI -> Pull Request / Commit -> Test Cases -> Release`

## Traceability Table

| Change ID | Requirement ID | Acceptance Criteria | Design / UI Artifact | PR / Commit | Test Case ID | Verification Status | Target Release |
|---|---|---|---|---|---|---|---|
| <CR_ID> | <REQ_ID> | <AC_ID> | <DESIGN_OR_UI_REF> | <PR_OR_COMMIT> | <TC_ID> | <PENDING/PASSED> | <NEXT_RELEASE_VER> |

## Validation Checklist
- [ ] Every modified or added requirement is traced to a Change ID
- [ ] Every code commit references the CR ID
- [ ] Every new test case is mapped to modified AC
- [ ] No orphan code or orphaned test cases
