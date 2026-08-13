---
description: Record human authorization decision for a Change Request (CR-XXXX) and initialize the change cycle.
---

# Record Change Decision Workflow

## Purpose

사람이 제출한 `APPROVE CR-XXXX` 또는 `REJECT CR-XXXX: <reason>` 결정을 검증하여
Change Request의 상태를 확정하고, 승인 시 하위 영향 산출물을 STALE로 전환하며
재진입할 워크플로우를 안내한다.

## Required Input

다음 중 하나의 명시적 Human Decision:
- `APPROVE CR-XXXX`
- `REJECT CR-XXXX: <reason>`

## Preconditions

1. `docs/changes/<CR_ID>/CHANGE_REQUEST.md` 존재 확인
2. `docs/changes/<CR_ID>/IMPACT_ANALYSIS.md` 존재 확인
3. `docs/changes/<CR_ID>/CHANGE_REQUEST.md`의 status가 `DRAFT`인지 확인

## Procedure

### 1. Decision 파싱 및 검증
- CR ID 및 결정 유형(APPROVED / REJECTED) 추출.

### 2. Process APPROVED
결정이 `APPROVE`인 경우:
1. `docs/changes/<CR_ID>/CHANGE_REQUEST.md`의 `status = "APPROVED"`로 변경.
2. `docs/changes/<CR_ID>/IMPACT_ANALYSIS.md`의 `status = "APPROVED"`로 변경.
3. `docs/changes/CHANGE_REGISTER.md`의 상태를 `APPROVED`로 갱신.
4. **Downstream Artifact STALE 전환**:
   - `IMPACT_ANALYSIS.md`에 명시된 Earliest Impacted Stage의 하위 Stage 산출물 상태를 `APPROVED`에서 `STALE`로 전환.
   - 예: Requirement 변경 시, 기존 Design v1.0, Implementation Plan, Test Baseline을 `STALE`로 표시.
5. **Cycle Approval 폴더 준비**:
   - `docs/approvals/<CR_ID>/` 디렉토리 준비.
6. **다음 단계 안내 출력**:
   ```
   CR-XXXX
   status = APPROVED

   Recommended next workflow:
   /<earliest-stage-workflow> (e.g. /analyze-requirements)

   Change Cycle:
   <CR_ID>

   Next Workflow has NOT been executed.
   ```

### 3. Process REJECTED
결정이 `REJECT`인 경우:
1. `docs/changes/<CR_ID>/CHANGE_REQUEST.md`의 `status = "REJECTED"`, 거절 사유 기록.
2. `docs/changes/CHANGE_REGISTER.md`의 상태를 `REJECTED`로 갱신.
3. 기존 Baseline과 Artifact 상태 유지.
4. 거절 결과 보고 후 STOP.

## Critical Rule

Change 승인 완료 후에도 **Next Workflow를 자동 실행하지 않는다.**
사용자가 권장된 다음 명령(예: `/analyze-requirements`)을 직접 실행하도록 안내하고 멈춘다.
