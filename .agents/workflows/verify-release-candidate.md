---
description: Verify the implementation against requirements and prepare a release candidate decision.
---

# Release Candidate Verification Workflow

## Purpose

구현된 Software가
승인된 Requirement와 Acceptance Criteria를
실제로 만족하는지 검증한다.


## Required Agent

Primary:

@qa

Supporting:

@security


## Required Skills

- test-design
- security-review
- code-review


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G3 Approval Record (`docs/approvals/G3-implementation-plan.approval.json`)의 `decision == "APPROVED"` 확인
2. Build Handoff (`docs/03-implementation/BUILD_HANDOFF.json`)의 `status == "READY"` 확인
3. 실제 구현 및 테스트 코드가 승인된 Implementation Plan Version을 참조하고 있는지 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- REQUIREMENTS.md
- ACCEPTANCE_CRITERIA.md
- TRACEABILITY_MATRIX.md
- DESIGN.md
- BUILD_HANDOFF.json
- Source Code
- Test Code
- Build Evidence


## Execution

1. project.yaml 읽기

2. Rules 읽기

3. @qa 역할 적용

4. @security 검토 적용

5. 다음 Prompt를 읽는다.

.agents/prompts/04-test/PROMPT.md

6. VERIFY Stage를 수행한다.

7. Requirement별 Evidence를 확인한다.


## Expected Outputs

docs/04-test/TEST_PLAN.md

docs/04-test/TEST_CASES.md

docs/04-test/TEST_REPORT.md

docs/04-test/SECURITY_REPORT.md

docs/04-test/VERIFY_HANDOFF.json


## Validation

각 결과를 다음 중 하나로 표시한다.

PASS
FAIL
SKIPPED
NOT_EXECUTED
BLOCKED

Release Candidate 최소조건:

- Critical AC PASS
- Required CI PASS
- Critical Security Finding 없음
- Blocking Defect 없음


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact(`docs/04-test/TEST_PLAN.md`, `docs/04-test/TEST_CASES.md`, `docs/04-test/TEST_REPORT.md`, `docs/04-test/SECURITY_REPORT.md`)의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. Stage Handoff(`docs/04-test/VERIFY_HANDOFF.json`)를 갱신하고 `status = "READY_FOR_APPROVAL"`로 설정한다.
4. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G4-release-candidate.review.md`를 생성한다.
5. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact 목록 및 Version
   - Release Candidate 평가 결과 및 Validation 요약 (Critical AC PASS, CI PASS 등)
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G4`, `APPROVE_WITH_COMMENTS G4: <comments>`, `REJECT G4: <reason>`)


## Human Gate

G4 — Release Candidate Approval

다음을 출력하고 STOP한다.

G4 RELEASE CANDIDATE APPROVAL REQUIRED

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

- Critical Test FAIL
- Critical Security Finding
- Critical AC 미검증
- Blocking Defect
- G4 승인 대기


## Next Command

G4 승인 후:

/prepare-release