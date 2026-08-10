---
review_package_id: "<GATE>-RP-<ID>"
project_id: "<PROJECT-ID>"
gate: "<G0-G5>"
stage: "<STAGE>"
status: "IN_REVIEW"
created_at: "<ISO-8601>"
created_by: "<AGENT>"
---

# Human Review Package

## 1. Approval Request

### Gate

<GATE>

### Gate Name

<GATE-NAME>

### Stage

<STAGE>

### Decision Requested

본 Review Package에 포함된 Artifact를
해당 Stage의 공식 Baseline으로 승인할 것인지 결정한다.


## 2. Review Scope

| Artifact ID | Path | Version | Status |
|---|---|---:|---|
| | | | IN_REVIEW |


## 3. What Changed

<이전 Version 또는 이전 Stage 대비 주요 변경사항>


## 4. Validation Summary

| Validation | Result |
|---|---|
| Stage Validation | |
| Traceability | |
| Security | |
| Test / Build | |


## 5. Blocking Issues

NONE

또는

<Blocking Issue>


## 6. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| | | |


## 7. Open Questions

| Question | Blocking | Owner |
|---|---|---|
| | YES / NO | |


## 8. Human Review Checklist

<Gate별 Checklist>


## 9. Agent Recommendation

READY_FOR_APPROVAL
또는
NOT_READY


## 10. Human Decision

허용되는 응답:

APPROVE <GATE>

APPROVE_WITH_COMMENTS <GATE>: <comments>

REJECT <GATE>: <reason>
