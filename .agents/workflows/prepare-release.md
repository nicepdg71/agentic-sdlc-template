---
description: Prepare a verified release candidate for production without deploying it.
---

# Release Preparation Workflow

## Purpose

승인된 Release Candidate의
Production 배포 준비 상태를 검증한다.

이 Workflow는 Production Deploy를 수행하지 않는다.


## Required Agent

Primary:

@devops

Supporting:

@qa
@security


## Required Skills

- release-readiness
- security-review


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G4 Approval Record (`docs/approvals/G4-release-candidate.approval.json`)의 `decision == "APPROVED"` 확인
2. Verify Handoff (`docs/04-test/VERIFY_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 Release Candidate Version/Commit과 실제 대상 일치 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- VERIFY_HANDOFF.json
- TEST_REPORT.md
- SECURITY_REPORT.md
- Release Candidate
- Deployment Configuration
- Environment Configuration


## Critical Restriction

다음을 수행하지 않는다.

- Production Deploy
- Production Migration
- Production Secret 변경
- Production Data 변경
- Production Traffic 변경


## Execution

1. project.yaml 확인

2. Rules 확인

3. @devops 역할 적용

4. 다음 Prompt 읽기

.agents/prompts/05-release/PROMPT.md

5. RELEASE Prompt의:

PHASE A — RELEASE PREPARATION

만 수행한다.

PHASE B는 수행하지 않는다.

6. Release Candidate Commit / Version 확인

7. CI 상태 확인

8. Environment 검증

9. Secret 존재 여부만 검증

10. Migration Risk 확인

11. Rollback 작성

12. Smoke Test 작성

13. Monitoring 계획 작성


## Expected Outputs

docs/05-release/RELEASE_PLAN.md

docs/05-release/RELEASE_CHECKLIST.md

docs/05-release/RELEASE_NOTES.md

docs/05-release/ROLLBACK_PLAN.md

docs/05-release/RELEASE_HANDOFF.json


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact(`docs/05-release/RELEASE_PLAN.md`, `docs/05-release/RELEASE_CHECKLIST.md`, `docs/05-release/RELEASE_NOTES.md`, `docs/05-release/ROLLBACK_PLAN.md`)의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. Stage Handoff(`docs/05-release/RELEASE_HANDOFF.json`)를 갱신하고 `status = "READY_FOR_APPROVAL"`로 설정한다.
4. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G5-production-release.review.md`를 생성한다.
5. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact 목록, Version 및 Release Candidate Commit
   - Validation 결과 (배포절차, DB 마이그레이션, 백업/롤백, 모니터링 등)
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G5`, `APPROVE_WITH_COMMENTS G5: <comments>`, `REJECT G5: <reason>`)


## Human Gate

G5 — Production Release Approval

다음을 출력하고 STOP한다.

G5 PRODUCTION RELEASE APPROVAL REQUIRED

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

- G4 미승인
- CI 실패
- Security Blocker
- Production 환경 미준비
- Secret 미설정
- Migration Risk 미해결
- Rollback 불명확
- G5 승인 대기


## Next Command

G5 승인 후에만:

/deploy-production