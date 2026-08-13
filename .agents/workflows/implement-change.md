---
description: Implement an explicitly approved implementation plan and produce build evidence within the active cycle.
---

# Implementation Workflow

## Purpose

G3에서 승인된 Implementation Plan을 정확한 범위 내에서 구현하고, 빌드 및 단위 테스트 증거를 생성한다.

## Required Agent

Primary:
@engineer

Supporting when applicable:
- @security
- @ai

## Required Skills

- secure-coding
- code-review

## Conditional Skills

- runtime-ai-design (when runtime_ai.enabled = true)
- database-design-review (when database impact exists)
- security-review (when security boundary is affected)

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Plan**: `docs/03-implementation/IMPLEMENTATION_PLAN.md`

## Preconditions

1. 현재 Cycle ID에 해당하는 G3 Approval Record(`docs/approvals/<CYCLE_ID>/G3-implementation-plan.approval.json`)의 `decision == "APPROVED"` 확인
2. Approval Record에 명시된 Approved Implementation Plan Version과 실제 파일 버전 일치 확인

## Required Inputs

- APPROVED `IMPLEMENTATION_PLAN.md`
- Approved Design & UI Handoffs
- Requirements & Acceptance Criteria
- Contracts & ADRs

## Execution

1. `project.yaml` 및 Rules 확인
2. Git Branch 확인 (Protected branch 직접 커밋 금지)
3. `.agents/prompts/03-implementation/PROMPT.md`의 PHASE B (IMPLEMENTATION) 수행
4. 승인된 Plan 범위만 구현
5. 단위 테스트 작성 및 실제 실행
6. Lint, Build 실제 실행
7. `docs/03-implementation/BUILD_HANDOFF.json` 생성/갱신 (metadata에 `cycle_id`, `change_id` 기록)

## Validation

- Lint, Unit Test, Build 실행 결과 기록 (실행하지 않은 항목을 PASS로 기록하지 않음)
- Secret 및 Scope 밖 변경 없음 확인

## Next Command

구현 검증 준비 완료 시:
`/verify-release-candidate`