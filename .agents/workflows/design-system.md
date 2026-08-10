---
description: Design the system architecture from the approved requirement baseline.
---

# System Design Workflow

## Purpose

승인된 Requirement를
구현 가능한 Software Design Baseline으로 변환한다.


## Required Agent

Primary:

@architect

Supporting when applicable:

@ux
@ai
@security


## Required Skills

- architecture-design
- security-review


## Conditional Skills

- api-contract-design (when interfaces are required)
- database-design-review (when persistent database is required)
- ui-design-handoff (when toolchain.ui_design.enabled = true)
- runtime-ai-design (when runtime_ai.enabled = true)


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G1 Approval Record (`docs/approvals/G1-requirement-baseline.approval.json`)의 `decision == "APPROVED"` 확인
2. Analysis Handoff (`docs/01-analysis/ANALYSIS_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 Requirement 산출물(`REQUIREMENTS.md`, `USER_STORIES.md`, `ACCEPTANCE_CRITERIA.md`, `TRACEABILITY_MATRIX.md`)의 버전과 실제 파일 버전 일치 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Conditional Agent Check

project.yaml을 확인한다.

UI가 활성화되어 있으면:

@ux 관점을 적용한다.

Runtime AI가 활성화되어 있으면:

@ai 관점을 적용한다.

Security는 필요한 설계영역에 적용한다.


## Required Inputs

- REQUIREMENTS.md
- ACCEPTANCE_CRITERIA.md
- TRACEABILITY_MATRIX.md
- ANALYSIS_HANDOFF.json


## Execution

1. project.yaml 읽기

2. Rules 읽기

3. @architect 역할 적용

4. Conditional Agent 활성상태 확인

5. 다음 Prompt 읽기

.agents/prompts/02-design/PROMPT.md

6. DESIGN Prompt의 절차를 수행한다.

7. Requirement Coverage를 검증한다.


## Expected Outputs

docs/02-design/ARCHITECTURE.md

docs/02-design/DESIGN.md

docs/02-design/DATA_MODEL.md

docs/02-design/SECURITY_DESIGN.md

docs/02-design/adr/

contracts/

docs/02-design/DESIGN_HANDOFF.json


## Validation

- Critical Requirement Coverage
- Architecture Consistency
- Data Model
- Interface
- Security
- ADR 필요성
- Scope 일치


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact(`docs/02-design/ARCHITECTURE.md`, `docs/02-design/DESIGN.md`, `docs/02-design/DATA_MODEL.md`, `docs/02-design/SECURITY_DESIGN.md`, `docs/02-design/adr/*`)의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. Stage Handoff(`docs/02-design/DESIGN_HANDOFF.json`)를 갱신하고 `status = "READY_FOR_APPROVAL"`로 설정한다.
4. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G2-design-baseline.review.md`를 생성한다.
5. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact 목록 및 Version
   - Validation 결과
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G2`, `APPROVE_WITH_COMMENTS G2: <comments>`, `REJECT G2: <reason>`)


## Human Gate

G2 — Design Baseline Approval

완료 후:

G2 DESIGN BASELINE APPROVAL REQUIRED

를 출력하고 STOP한다.

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

- G1 미승인
- Critical Requirement 미설계
- Scope 변경 필요
- Security Blocker
- 중요한 Architecture 미결정
- G2 승인 대기


## Next Command

G2 승인 후:

/plan-implementation