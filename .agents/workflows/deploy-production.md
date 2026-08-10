---
description: Deploy the approved release candidate to production after explicit G5 approval.
---

# Production Deployment Workflow

## Purpose

G5에서 명시적으로 승인된
Release Candidate만 Production에 배포한다.


## Required Agent

@devops

Supporting:

@qa
@security


## Required Skills

- release-readiness


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G5 Approval Record (`docs/approvals/G5-production-release.approval.json`)의 `decision == "APPROVED"` 확인
2. Release Handoff (`docs/05-release/RELEASE_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 승인된 Release Candidate Version/Commit과 실제 배포 대상 Version/Commit 일치 확인
4. Required CI 상태 PASS 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- APPROVED RELEASE_HANDOFF.json
- RELEASE_PLAN.md
- RELEASE_CHECKLIST.md
- ROLLBACK_PLAN.md
- Release Candidate


## Critical Approval Check

G5 승인상태를 확인한다.

명시적인 G5 Approval을 확인할 수 없는 경우
어떤 Production 작업도 수행하지 않는다.


## Execution

1. Release Candidate 식별

2. Deployment Target 확인

3. G5 Approval 확인

4. 승인된 Deployment Workflow만 실행

5. Deployment 결과 확인

6. Smoke Test 실행

7. Monitoring 확인

8. 실패 시 승인된 Rollback 기준 적용

9. 최종 결과 기록


## Expected Result

Deployment:

SUCCESS
FAILED
ROLLED_BACK

Smoke Test:

PASS
FAIL
NOT_EXECUTED

Monitoring:

NORMAL
WARNING
CRITICAL
NOT_CHECKED


## Prohibited

이 Workflow는 다음을 임의로 수행하지 않는다.

- 다른 Version 배포
- Release Plan 변경
- 승인되지 않은 Migration
- 승인되지 않은 Secret 변경
- Production 데이터 임의 수정


## Stop Conditions

- G5 확인 불가
- Release Version 불일치
- CI 실패
- Critical Security Finding
- Deployment 환경 이상
- 승인되지 않은 Migration
- Rollback 필요조건 발생


## Completion

성공한 경우 Agentic SDLC Release Cycle을 완료한다.

최종 Release 결과를 공식 Artifact에 기록한다.
