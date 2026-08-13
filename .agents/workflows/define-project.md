---
description: Start the DEFINE stage and create or differentially update project definition baselines.
---

# DEFINE Project Workflow

## Purpose

신규 프로젝트의 최초 정의 또는 Scope 변경으로 인한 재정의 작업을 수행한다.
이 Workflow는 실제 구현을 시작하지 않는다.

## Required Agent

@pm

## Required Skills

- project-definition
- change-impact-analysis (when in CHANGE mode)

## Execution Context 확인

Workflow 시작 시 다음 Context를 먼저 확인한다:
- **Cycle Type**: `INITIAL` (신규 프로젝트) / `CHANGE` (Scope 변경 Re-entry)
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 기존 `PROJECT_CHARTER.md`, `SCOPE.md` 버전 확인
- **Earliest Impacted Stage**: `DEFINE`

## Preconditions

다음을 확인한다:
- Repository Root 및 project.yaml 존재 여부
- .agents/rules/ 및 .agents/agents.md 존재 여부
- DEFINE Stage Prompt 존재 여부
- CHANGE 모드인 경우: `docs/changes/<CR_ID>/CHANGE_REQUEST.md`의 `status == "APPROVED"` 및 Earliest Impacted Stage가 `DEFINE`인지 확인

## Required Inputs

- INITIAL 모드: 사용자 아이디어, 해결 과제, 대상 사용자, 제약 조건
- CHANGE 모드: `docs/changes/<CR_ID>/CHANGE_REQUEST.md` 및 `IMPACT_ANALYSIS.md`

## Execution

1. `project.yaml` 및 Rules 읽기
2. `@pm` 역할 적용
3. `.agents/prompts/00-project-definition/PROMPT.md` 읽기
4. **Baseline-aware Update (CHANGE 모드 시)**:
   - 기존 산출물을 처음부터 다시 작성하지 않고, Scope Diff(유지/변경/신규/삭제) 분석을 적용하여 버전 증가(`v1.0 -> v1.1` 등).
5. 다음 Artifact 생성/갱신:
   - `docs/00-project-definition/PROJECT_CHARTER.md`
   - `docs/00-project-definition/SCOPE.md`
   - `docs/00-project-definition/PROJECT_DEFINITION_HANDOFF.json` (metadata에 `cycle_id`, `change_id` 기록)

## Validation

- Business Problem, Goal, Target User, In Scope, Out of Scope, Success Metrics, Risk, Open Questions 검증

## Gate Review Preparation

1. Stage Validation 수행
2. Gate 대상 Artifact status를 `IN_REVIEW`로 변경
3. `PROJECT_DEFINITION_HANDOFF.json`의 `status = "READY_FOR_APPROVAL"` 설정
4. `docs/approvals/<CYCLE_ID>/G0-project-definition.review.md` 생성
5. Review Package 내용 구성 (승인 대상 목록, Validation 결과, Risks, 허용 Decision Format)

## Human Gate

G0 — Project Definition Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G0 PROJECT DEFINITION APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G0 승인 후:
`/analyze-requirements`