---
artifact_id: "<CR_ID>"
project_id: "<PROJECT_ID>"
cycle_id: "<CR_ID>"
change_id: "<CR_ID>"
stage: "CHANGE_CONTROL"
artifact_type: "CHANGE_REQUEST"
version: "1.0"
status: "DRAFT"
baseline_version: "<CURRENT_PRODUCTION_VERSION>"
owner: "@analyst"
---

# Change Request: <CHANGE_TITLE>

## Change ID
<CR_ID>

## Current Production Version
- Version: <CURRENT_PRODUCTION_VERSION>
- Commit: <CURRENT_COMMIT_SHA>

## Requested Change
- **Summary**: <DETAILED_DESCRIPTION_OF_CHANGE>
- **Target Area**: <REQUIREMENT / UI / ARCHITECTURE / BUG_FIX / TEST / DEPLOYMENT>

## Reason & Business Justification
- **Driver**: <USER_FEEDBACK / DEFECT / MARKET_EXPANSION / REFACTORING>
- **Rationale**: <WHY_THIS_CHANGE_IS_NEEDED>

## Requested By
- **Requester**: <STAKEHOLDER_OR_USER_NAME>
- **Requested Date**: <ISO8601_DATE>

## Business Impact
- **Impact Level**: <LOW / MEDIUM / HIGH / CRITICAL>
- **Urgency**: <NORMAL / HIGH / CRITICAL>

## Initial Scope Impact
- [ ] New Requirements added
- [ ] Existing Requirements modified
- [ ] Existing Requirements deprecated/removed
- [ ] Non-functional requirements / Performance / Security impacted

## Expected Functional Impact
- <SUMMARY_OF_AFFECTED_USER_FLOWS_AND_MODULES>

## Initial Risk
- <RISK_ASSESSMENT_AND_MITIGATION_STRATEGY>

## Status
DRAFT
