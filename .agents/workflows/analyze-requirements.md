---
description: Analyze requirements, create user stories, acceptance criteria, and traceability matrix from project definition or change request.
---

# Analyze Requirements Workflow

## Purpose

승인된 Project Definition 또는 승인된 Change Request를 기반으로
구체적이고 검증 가능한 시스템 요구사항, 사용자 스토리, 인수 조건, 추적 매트릭스를 도출/갱신한다.

## Required Agent

@analyst

Supporting when applicable:
- @pm
- @architect
- @security

## Required Skills

- requirements-analysis
- change-impact-analysis (when in CHANGE mode)

## Execution Context 확인

Workflow 시작 시 다음 Context를 먼저 확인한다:
- **Cycle Type**: `INITIAL` (신규 개발 `INIT-001`) / `CHANGE` (요구사항 변경 `CR-XXXX`)
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 기존 `REQUIREMENTS.md` (v1.0 등)
- **Earliest Impacted Stage**: `SPEC` (또는 `DEFINE`)

## Preconditions

1. INITIAL 모드인 경우:
   - G0 Approval Record(`docs/approvals/INIT-001/G0-project-definition.approval.json`)의 `decision == "APPROVED"` 확인
   - `PROJECT_DEFINITION_HANDOFF.json`의 `status == "APPROVED"` 확인
2. CHANGE 모드인 경우:
   - `docs/changes/<CR_ID>/CHANGE_REQUEST.md`의 `status == "APPROVED"` 확인
   - 상위 승인(G0) 유효성 확인

## Execution

1. `project.yaml` 및 Rules 읽기
2. `@analyst` 역할 적용
3. `.agents/prompts/01-analysis/PROMPT.md` 읽기
4. **Baseline-aware Differential Update (CHANGE 모드)**:
   - 기존 `REQUIREMENTS.md`를 처음부터 다시 만들지 않고, Diff Analysis(유지 / 변경 / 신규 / 삭제)를 수행하여 버전 업데이트 (예: `v1.0 -> v1.1`).
   - `docs/changes/<CR_ID>/CHANGE_TRACEABILITY.md` 동기화.
5. 다음 산출물 생성/갱신:
   - `docs/01-analysis/REQUIREMENTS.md`
   - `docs/01-analysis/USER_STORIES.md`
   - `docs/01-analysis/ACCEPTANCE_CRITERIA.md`
   - `docs/01-analysis/TRACEABILITY_MATRIX.md`
   - `docs/01-analysis/ANALYSIS_HANDOFF.json` (metadata에 `cycle_id`, `change_id` 기록)

## Validation

- FR / NFR 완결성, 인수 조건의 테스트 가능성, Traceability Matrix 100% 매핑, Scope 일치성 검증

## Gate Review Preparation

1. Stage Validation 수행
2. Gate 대상 Artifact status를 `IN_REVIEW`로 변경
3. `ANALYSIS_HANDOFF.json`의 `status = "READY_FOR_APPROVAL"` 설정
4. `docs/approvals/<CYCLE_ID>/G1-requirement-baseline.review.md` 생성
5. Review Package 작성

## Human Gate

G1 — Requirement Baseline Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G1 REQUIREMENT BASELINE APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G1 승인 후:
`/design-system`