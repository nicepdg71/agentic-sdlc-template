# RELEASE Stage Prompt

## ROLE

Primary Agent:

@devops

Supporting Agents:

@qa
@security


## STAGE

RELEASE


## OBJECTIVE

승인된 Release Candidate를
Production에 안전하게 배포할 수 있도록 준비하고,
Human G5 승인 후 승인된 배포 절차를 수행한다.


## PRECONDITIONS

- G4 APPROVED
- VERIFY_HANDOFF APPROVED
- Release Candidate 존재


## REQUIRED INPUTS

- APPROVED VERIFY_HANDOFF.json
- TEST_REPORT.md
- SECURITY_REPORT.md
- Release Candidate
- Deployment Configuration
- Environment Configuration


## RULES

- Production Release는 반드시 G5 승인이 필요하다.
- Secret을 Repository에 저장하지 않는다.
- 승인되지 않은 Migration을 실행하지 않는다.
- Rollback 가능성을 검토한다.


# PHASE A — RELEASE PREPARATION


## PROCEDURE A

### 1. Release Candidate 확인

배포 대상 Version과 Commit을 확인한다.

### 2. CI Status

필수 CI가 PASS인지 확인한다.

### 3. Test / Security

Blocking Issue가 없는지 확인한다.

### 4. Environment

Staging / Production 설정을 확인한다.

### 5. Secrets

필요한 Secret이 안전하게 설정되어 있는지 확인한다.

Secret 값 자체를 출력하지 않는다.

### 6. Migration

DB 변경이 있는 경우:

- 순서
- 영향
- Backup
- Rollback

을 검토한다.

### 7. Rollback Plan

배포 실패 시 복구절차를 작성한다.

### 8. Smoke Test

배포 직후 실행할 최소 검증을 정의한다.

### 9. Monitoring

배포 후 확인할 Log, Metric, Alert를 정의한다.

### 10. Release Notes

변경사항을 작성한다.


## REQUIRED OUTPUTS

docs/05-release/RELEASE_PLAN.md

docs/05-release/RELEASE_CHECKLIST.md

docs/05-release/RELEASE_NOTES.md

docs/05-release/ROLLBACK_PLAN.md

docs/05-release/RELEASE_HANDOFF.json


## ARTIFACT TEMPLATES

다음 Template을 기반으로 실제 Artifact를 docs/05-release/에 생성한다.

- .agents/templates/artifacts/05-release/RELEASE_PLAN.template.md → docs/05-release/RELEASE_PLAN.md
- .agents/templates/artifacts/05-release/RELEASE_CHECKLIST.template.md → docs/05-release/RELEASE_CHECKLIST.md
- .agents/templates/artifacts/05-release/RELEASE_NOTES.template.md → docs/05-release/RELEASE_NOTES.md
- .agents/templates/artifacts/05-release/ROLLBACK_PLAN.template.md → docs/05-release/ROLLBACK_PLAN.md
- .agents/templates/artifacts/05-release/RELEASE_HANDOFF.template.json → docs/05-release/RELEASE_HANDOFF.json

템플릿 사용 규칙:
1. Template 자체를 수정하지 않는다.
2. Template 구조와 Frontmatter를 유지하며 Placeholder를 실제 값으로 대체한다.
3. 해당하지 않는 Section은 삭제하지 말고 N/A 또는 NONE으로 명시한다.
4. 신규 Artifact의 초기 status는 DRAFT로 작성한다.


## HUMAN APPROVAL

G5 — Production Release Approval

다음을 출력한다.

G5 PRODUCTION RELEASE APPROVAL REQUIRED

그리고 STOP한다.


# PHASE B — PRODUCTION RELEASE


## PRECONDITION B

명시적인:

APPROVE G5

가 있어야 한다.


## PROCEDURE B

승인된 Deployment Workflow만 실행한다.

배포 후:

1. Deployment Status 확인
2. Smoke Test 실행
3. 주요 Monitoring 확인
4. 실패 시 Rollback 기준 적용
5. Release 결과 기록


## VALIDATION

Deployment:

SUCCESS / FAILED / ROLLED_BACK

Smoke Test:

PASS / FAIL / NOT_EXECUTED

Monitoring:

NORMAL / WARNING / CRITICAL / NOT_CHECKED


## STOP CONDITIONS

- G4 미승인
- G5 미승인
- CI 실패
- Critical Security Issue
- Production Secret 미설정
- Rollback 불가능한 위험 발견
- Migration 불확실성
- Deployment 실패


## HANDOFF

성공 시:

Release 결과를 공식 Artifact로 기록한다.

운영/유지관리 단계로 넘길 수 있다.

Agentic SDLC의 기본 Release Cycle은 여기서 완료한다.