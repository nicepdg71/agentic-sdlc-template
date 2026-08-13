---
description: Analyze the approved design and UI handoffs to prepare an implementation plan without modifying source code.
---

# Implementation Planning Workflow

## Purpose

Source Code를 변경하기 전에 구현 범위, UI Handoff, 아키텍처 및 영향을 분석하고
`IMPLEMENTATION_PLAN.md`를 작성한다.

## Required Agent

Primary:
@engineer

Supporting when required:
- @architect
- @ux
- @security

## Required Skills

- implementation-planning
- ui-design-handoff (when UI is active)

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 기존 코드베이스 및 설계 산출물
- **Earliest Impacted Stage**: `BUILD` (또는 상위)

## Preconditions

1. 현재 Cycle ID에 해당하는 G2 Approval Record(`docs/approvals/<CYCLE_ID>/G2-design-baseline.approval.json`)의 `decision == "APPROVED"` 확인
2. Design Handoff (`docs/02-design/DESIGN_HANDOFF.json`)의 `status == "APPROVED"` 확인

## Required Inputs

- `DESIGN_HANDOFF.json`
- `REQUIREMENTS.md` / `ACCEPTANCE_CRITERIA.md`
- `ARCHITECTURE.md` / `DESIGN.md` / `DATA_MODEL.md` / `SECURITY_DESIGN.md`
- **UI Design Artifacts (UI 활성화 시)**:
  - `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
  - `docs/02-design/ui/STITCH_PROJECT_REF.json`
- Contracts & ADRs

## Critical Restriction

이 Workflow에서는 **Source Code를 수정하지 않는다** (READ-ONLY 분석).

## Execution

1. `project.yaml` 및 Rules 읽기
2. `@engineer` 역할 적용
3. `.agents/prompts/03-implementation/PROMPT.md` 읽기 (PHASE A만 수행)
4. **UI Design Handoff 통합**:
   - Stitch/UI가 활성화된 경우 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json`을 읽고 디자인 토큰, 레이아웃, 상태별 컴포넌트 구현 계획을 수립.
   - Source of Truth 우선순위 준수: `Requirements -> UI Design Handoff -> Stitch Reference -> Code`.
   - 충돌 발생 시 `DESIGN CONFLICT DETECTED`를 보고하고 STOP.
5. `docs/03-implementation/IMPLEMENTATION_PLAN.md` 생성/갱신 (metadata에 `cycle_id`, `change_id` 기록).

## Gate Review Preparation

1. Stage Validation 수행
2. `IMPLEMENTATION_PLAN.md` status를 `IN_REVIEW`로 설정
3. `docs/approvals/<CYCLE_ID>/G3-implementation-plan.review.md` 생성
4. Review Package 작성

## Human Gate

G3 — Implementation Plan Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G3 IMPLEMENTATION PLAN APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G3 승인 후:
`/implement-change`