---
description: Analyze the approved project definition and create the requirement baseline.
---

# Requirement Analysis Workflow

## Purpose

승인된 Project Definition을
검증 가능한 Software Requirement Baseline으로 변환한다.


## Required Agent

@analyst


## Required Skills

- requirements-analysis


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G0 Approval Record (`docs/approvals/G0-project-definition.approval.json`)의 `decision == "APPROVED"` 확인
2. Project Definition Handoff (`docs/00-project-definition/PROJECT_DEFINITION_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 `PROJECT_CHARTER.md` 및 `SCOPE.md`의 버전과 실제 파일 버전 일치 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- docs/00-project-definition/PROJECT_CHARTER.md
- docs/00-project-definition/SCOPE.md
- PROJECT_DEFINITION_HANDOFF.json
- 사용자 또는 업무 관련 자료


## Execution

1. project.yaml을 읽는다.

2. 적용되는 Rules를 읽는다.

3. .agents/agents.md의 @analyst 역할을 적용한다.

4. 다음 Prompt를 읽는다.

.agents/prompts/01-analysis/PROMPT.md

5. SPEC Stage Prompt의 절차만 수행한다.

6. 승인된 Scope 밖 기능을 추가하지 않는다.


## Expected Outputs

docs/01-analysis/REQUIREMENTS.md

docs/01-analysis/USER_STORIES.md

docs/01-analysis/ACCEPTANCE_CRITERIA.md

docs/01-analysis/TRACEABILITY_MATRIX.md

docs/01-analysis/ANALYSIS_HANDOFF.json


## Validation

다음을 확인한다.

- Requirement ID
- FR/NFR
- Acceptance Criteria
- Scope 일치
- Conflict
- Open Question
- Traceability


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact(`docs/01-analysis/REQUIREMENTS.md`, `docs/01-analysis/USER_STORIES.md`, `docs/01-analysis/ACCEPTANCE_CRITERIA.md`, `docs/01-analysis/TRACEABILITY_MATRIX.md`)의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. Stage Handoff(`docs/01-analysis/ANALYSIS_HANDOFF.json`)를 갱신하고 `status = "READY_FOR_APPROVAL"`로 설정한다.
4. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G1-requirement-baseline.review.md`를 생성한다.
5. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact 목록 및 Version
   - Validation 결과
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G1`, `APPROVE_WITH_COMMENTS G1: <comments>`, `REJECT G1: <reason>`)


## Human Gate

G1 — Requirement Baseline Approval

완료 후:

G1 REQUIREMENT BASELINE APPROVAL REQUIRED

를 출력하고 STOP한다.

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

- G0 미승인
- 중요 Requirement Conflict
- Scope 변경 필요
- 중요 Business Decision 필요
- G1 승인 대기


## Next Command

G1 승인 후:

/design-system