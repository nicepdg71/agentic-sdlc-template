---
description: Prepare a verified release candidate for production without deploying it.
---

# Release Preparation Workflow

## Purpose

승인된 Release Candidate의 Production 배포 준비 상태를 검증하고 G5 심사 패키지를 준비한다.
이 Workflow는 Production Deploy를 수행하지 않는다.

## Required Agent

Primary:
@devops

Supporting:
- @qa
- @security

## Required Skills

- release-readiness
- security-review

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 릴리스 대상 버전 및 커밋
- **Earliest Impacted Stage**: `RELEASE` (또는 상위)

## Preconditions

1. 현재 Cycle ID에 해당하는 G4 Approval Record(`docs/approvals/<CYCLE_ID>/G4-release-candidate.approval.json`)의 `decision == "APPROVED"` 확인
2. Verify Handoff (`docs/04-test/VERIFY_HANDOFF.json`)의 `status == "APPROVED"` 확인

## Critical Restriction

이 단계에서는 실제 배포(Deploy)를 수행하지 않는다.

## Execution

1. `project.yaml` 및 Rules 확인
2. `@devops` 역할 적용
3. `.agents/prompts/05-release/PROMPT.md`의 PHASE A (RELEASE PREPARATION) 수행
4. 배포 계획, 롤백 계획, 스모크 테스트 계획, 릴리스 노트 작성
5. 산출물 생성/갱신:
   - `docs/05-release/RELEASE_PLAN.md`
   - `docs/05-release/RELEASE_CHECKLIST.md`
   - `docs/05-release/RELEASE_NOTES.md`
   - `docs/05-release/ROLLBACK_PLAN.md`
   - `docs/05-release/RELEASE_HANDOFF.json` (metadata에 `cycle_id`, `change_id` 기록)

## Gate Review Preparation

1. Stage Validation 수행
2. Gate 대상 Artifact status를 `IN_REVIEW`로 설정
3. `RELEASE_HANDOFF.json`의 `status = "READY_FOR_APPROVAL"` 설정
4. `docs/approvals/<CYCLE_ID>/G5-production-release.review.md` 생성
5. Review Package 작성

## Human Gate

G5 — Production Release Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G5 PRODUCTION RELEASE APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G5 승인 후에만:
`/deploy-production`