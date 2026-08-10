---
description: Start the DEFINE stage and create the initial project definition.
---

# DEFINE Project Workflow

## Purpose

신규 프로젝트의 최초 정의 작업을 수행한다.

이 Workflow는 실제 구현을 시작하지 않는다.


## Required Agent

@pm


## Required Skills

- project-definition


## Preconditions

다음을 확인한다.

- Repository Root가 올바른가
- project.yaml이 존재하는가
- .agents/rules/가 존재하는가
- .agents/agents.md가 존재하는가
- DEFINE Stage Prompt가 존재하는가

이 Workflow는 최초 Stage이므로
Previous Gate는 요구하지 않는다.


## Required Inputs

최소한 사용자로부터 다음 중 사용 가능한 정보를 확인한다.

- 프로젝트 아이디어
- 해결하려는 문제
- 예상 사용자
- 알려진 제약조건
- 관련 사업자료

필수 정보가 부족하면 추측하지 말고 질문한다.


## Execution

1. project.yaml을 읽는다.

2. .agents/rules/를 적용한다.

3. .agents/agents.md의 @pm 역할을 따른다.

4. 다음 Stage Prompt를 읽는다.

.agents/prompts/00-project-definition/PROMPT.md

5. DEFINE Stage Prompt의 절차만 수행한다.

6. 다음 Artifact를 생성한다.

docs/00-project-definition/PROJECT_CHARTER.md

docs/00-project-definition/SCOPE.md

docs/00-project-definition/PROJECT_DEFINITION_HANDOFF.json


## Validation

Stage Prompt의 Validation을 수행한다.

특히 다음을 확인한다.

- Business Problem
- Goal
- Target User
- In Scope
- Out of Scope
- Success Metrics
- Risk
- Open Questions


## Expected Outputs

PROJECT_CHARTER.md
SCOPE.md
PROJECT_DEFINITION_HANDOFF.json


## Gate Review Preparation

Human Gate 요청 직전에 다음 절차를 수행한다.

1. Stage Validation을 수행한다.
2. Gate 대상 Artifact(`PROJECT_CHARTER.md`, `SCOPE.md`)의 status를 DRAFT에서 IN_REVIEW로 변경한다.
3. Stage Handoff(`docs/00-project-definition/PROJECT_DEFINITION_HANDOFF.json`)를 갱신하고 `status = "READY_FOR_APPROVAL"`로 설정한다.
4. `.agents/templates/approvals/GATE_REVIEW_PACKAGE.template.md`를 기반으로 `docs/approvals/G0-project-definition.review.md`를 생성한다.
5. Review Package에는 다음을 포함한다.
   - 승인 대상 Artifact 목록 및 Version
   - Validation 결과
   - Blocking Issue
   - Risks
   - Open Questions
   - Human Review Checklist
   - 허용된 Decision Format (`APPROVE G0`, `APPROVE_WITH_COMMENTS G0: <comments>`, `REJECT G0: <reason>`)


## Human Gate

G0 — Project Definition Approval

완료 후 반드시 다음을 출력하고 STOP한다.

G0 PROJECT DEFINITION APPROVAL REQUIRED

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.


## Stop Conditions

G0 승인 전에:

- Requirement 분석 금지
- Architecture 설계 금지
- Coding 금지

반드시 STOP한다.


## Next Command

G0가 승인된 후:

/analyze-requirements