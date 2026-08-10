---
description: Analyze the approved design and prepare an implementation plan without modifying source code.
---

# Implementation Planning Workflow

## Purpose

Source Code를 변경하기 전에
구현 범위와 영향을 분석하고
Implementation Plan을 작성한다.


## Required Agent

@engineer

Supporting when required:

@architect
@security


## Required Skills

- implementation-planning


## Conditional Skills

- database-design-review (when database impact exists)
- security-review (when security impact exists)


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G2 Approval Record (`docs/approvals/G2-design-baseline.approval.json`)의 `decision == "APPROVED"` 확인
2. Design Handoff (`docs/02-design/DESIGN_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 Design 산출물(`ARCHITECTURE.md`, `DESIGN.md`, `DATA_MODEL.md`, `SECURITY_DESIGN.md`, `adr/*`)의 버전과 실제 파일 버전 일치 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- DESIGN_HANDOFF.json
- REQUIREMENTS.md
- ACCEPTANCE_CRITERIA.md
- ARCHITECTURE.md
- DESIGN.md
- DATA_MODEL.md
- SECURITY_DESIGN.md
- Contracts
- ADR


## Critical Restriction

이 Workflow에서는
Source Code를 수정하면 안 된다.

Dependency 설치도 하지 않는다.

Migration을 실행하지 않는다.


## Execution

1. project.yaml 읽기

2. Rules 읽기

3. @engineer 역할 적용

4. 다음 Prompt를 읽는다.

.agents/prompts/03-implementation/PROMPT.md

5. BUILD Prompt의:

PHASE A — IMPLEMENTATION PLAN

만 수행한다.

PHASE B는 절대 수행하지 않는다.

6. Repository를 READ-ONLY로 분석한다.

7. 구현 범위와 영향을 정의한다.


## Expected Output

docs/03-implementation/IMPLEMENTATION_PLAN.md


## Validation

Plan에 최소한 다음이 있는지 확인한다.

- Requirement ID
- Acceptance Criteria
- 생성파일
- 수정파일
- 변경하지 않을 영역
- API 영향
- Database 영향
- Dependency 영향
- Security 영향
- Test Plan
- Risk
- Rollback


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact인 `docs/03-implementation/IMPLEMENTATION_PLAN.md`의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G3-implementation-plan.review.md`를 생성한다.
4. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact (`IMPLEMENTATION_PLAN.md`) 및 Version
   - Validation 결과 (영향분석, 테스트계획, 위험, 롤백 등)
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G3`, `APPROVE_WITH_COMMENTS G3: <comments>`, `REJECT G3: <reason>`)


## Human Gate

G3 — Implementation Plan Approval

다음을 출력하고 STOP한다.

G3 IMPLEMENTATION PLAN APPROVAL REQUIRED

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

- G2 미승인
- Scope 변경 필요
- Architecture 변경 필요
- 중요한 정보 누락
- G3 승인 대기

어떤 경우에도 이 Workflow에서
Source Code를 수정하지 않는다.


## Next Command

G3 승인 후:

/implement-change