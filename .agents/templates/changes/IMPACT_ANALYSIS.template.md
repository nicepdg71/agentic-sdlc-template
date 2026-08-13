---
artifact_id: "IA-<CR_ID>"
project_id: "<PROJECT_ID>"
cycle_id: "<CR_ID>"
change_id: "<CR_ID>"
stage: "CHANGE_CONTROL"
artifact_type: "IMPACT_ANALYSIS"
version: "1.0"
status: "DRAFT"
baseline_version: "<CURRENT_PRODUCTION_VERSION>"
owner: "@analyst"
---

# Change Impact Analysis: <CR_ID>

## Change ID
<CR_ID>

## Current Baseline
- **Release Version**: <CURRENT_PRODUCTION_VERSION>
- **Commit**: <CURRENT_COMMIT_SHA>
- **Active Cycle**: <CR_ID>

## Impact Matrix

| Area | Impact | Details / Affected Artifacts |
|---|---|---|
| Project Definition (Scope/Charter) | <NO / YES> | <DETAILS_OR_NONE> |
| Requirements (FR/NFR/User Stories) | <NO / YES / POSSIBLE> | <AFFECTED_REQ_IDS> |
| Architecture & System Design | <NO / YES / POSSIBLE> | <AFFECTED_ARCH_COMPONENTS> |
| UI / UX Design (Screens/Flows) | <NO / YES / POSSIBLE> | <AFFECTED_SCREENS_OR_COMPONENTS> |
| API Contracts | <NO / YES / POSSIBLE> | <AFFECTED_CONTRACT_FILES> |
| Database / Data Model | <NO / YES / POSSIBLE> | <AFFECTED_ENTITIES_OR_MIGRATIONS> |
| Runtime AI | <NO / YES / POSSIBLE> | <AFFECTED_PROMPTS_OR_SCHEMAS> |
| Security & Secrets | <NO / REVIEW / YES> | <SECURITY_REVIEW_SCOPE> |
| Implementation / Code | <NO / YES> | <AFFECTED_PACKAGES_OR_FILES> |
| Test Strategy & Cases | <NO / YES> | <AFFECTED_TEST_CASES> |
| Release & Deployment Plan | <NO / YES> | <RELEASE_PLAN_MODIFICATIONS> |

## Earliest Impacted Stage
<DEFINE / SPEC / DESIGN / BUILD / VERIFY / RELEASE>

## Required Re-approval Gates
<!-- List all gates from Earliest Impacted Stage to G5 -->
- [<G1|G2|G3|G4|G5>]

## Unaffected Upstream Approvals
<!-- Upstream gates that remain valid -->
<e.g., G0 remains valid.>

## Downstream Artifacts Tagged STALE
- <LIST_OF_DOWNSTREAM_ARTIFACTS_THAT_REQUIRE_UPDATE_AND_RE_APPROVAL>

## Recommended Next Workflow
<e.g., /analyze-requirements or /design-system or /plan-implementation>
