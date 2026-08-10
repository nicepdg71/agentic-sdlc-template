---
description: Record and validate an explicit human approval or rejection for an Agentic SDLC gate.
---

# Record Human Gate Decision

## Purpose

사용자가 명시적으로 전달한
G0~G5 Human Decision을 검증하고
Repository에 공식 Approval Evidence로 기록한다.


## Required Input

다음 중 하나의 명시적 Human Decision:

APPROVE G<n>

APPROVE_WITH_COMMENTS G<n>: <comments>

REJECT G<n>: <reason>


## Preconditions

1. 해당 Gate의 Review Package가 존재해야 한다.

2. Review Package가 참조하는 Artifact가 존재해야 한다.

3. 현재 Artifact Version과
   Review Package Version이 일치해야 한다.

4. Gate가 현재 Stage와 일치해야 한다.


## Procedure

### 1. Parse Decision

Gate와 Decision을 식별한다.


### 2. Validate Gate

현재 Stage에 맞는 Gate인지 확인한다.


### 3. Validate Review Package

해당 Gate의 Review Package를 확인한다.


### 4. Validate Artifact Versions

Review Package가 포함한
Artifact ID / Path / Version과
현재 Artifact를 비교한다.

불일치하면 STOP한다.


### 5. Process APPROVED

APPROVE이면:

- Approval Record 생성/갱신
- decision = APPROVED
- decided_by 기록
- decided_at 기록
- 승인 대상 Artifact status = APPROVED
- Handoff status = APPROVED


### 6. Process APPROVED_WITH_COMMENTS

Comment가 non-blocking인지 확인한다.

Artifact 변경이 필요 없으면:

decision = APPROVED_WITH_COMMENTS

로 기록한다.

Artifact 수정이 필요하면
승인을 확정하지 않고 STOP한다.


### 7. Process REJECTED

REJECT이면:

decision = REJECTED

로 기록한다.

대상 Artifact를 APPROVED로 변경하지 않는다.

수정 필요사항을 기록하고 STOP한다.


### 8. Report

다음을 보고한다.

Gate:
Decision:
Approved Artifact Versions:
Approval Record:
Handoff Status:
Next Workflow:


## Critical Rule

Human Approval 후
Next Workflow를 자동 실행하지 않는다.


## Stop Conditions

- Review Package 없음
- Artifact Version mismatch
- Gate mismatch
- Blocking Issue
- Conditional Approval이 실제 Artifact 변경을 요구함
