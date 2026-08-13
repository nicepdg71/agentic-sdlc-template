---
description: Record and validate an explicit human approval or rejection for an Agentic SDLC gate in the active cycle.
---

# Record Human Gate Decision

## Purpose

사용자가 명시적으로 전달한 G0~G5 Human Decision을 검증하고,
해당 Cycle 디렉토리(`docs/approvals/<CYCLE_ID>/`)에 공식 Approval Record Evidence로 기록한다.

## Required Input

다음 중 하나의 명시적 Human Decision:
- `APPROVE G<n>`
- `APPROVE_WITH_COMMENTS G<n>: <comments>`
- `REJECT G<n>: <reason>`

## Preconditions

1. Active Cycle ID 확인 (`INIT-001` 또는 `CR-XXXX`)
2. 해당 Gate의 Review Package (`docs/approvals/<CYCLE_ID>/G<n>-<stage>.review.md`) 존재 확인
3. Review Package가 참조하는 Artifact 존재 및 Version 일치 확인
4. Gate가 현재 Stage와 일치하는지 확인

## Procedure

### 1. Parse Decision
- Gate 번호(G0~G5)와 Decision 유형(APPROVED, APPROVED_WITH_COMMENTS, REJECTED) 식별.

### 2. Validate Gate & Review Package
- 현재 Stage와 매칭 여부 및 `docs/approvals/<CYCLE_ID>/G<n>-<stage>.review.md` 검증.

### 3. Process APPROVED
결정이 `APPROVE`인 경우:
- `docs/approvals/<CYCLE_ID>/G<n>-<stage>.approval.json` 생성/갱신.
- `cycle_id`, `change_id`, `decision = "APPROVED"`, `decided_by`, `decided_at` 기록.
- 승인 대상 Artifact들의 status를 `IN_REVIEW`에서 `APPROVED`로 변경.
- Stage Handoff (`*_HANDOFF.json`)의 `status = "APPROVED"`로 변경.

### 4. Process APPROVED_WITH_COMMENTS
- Comment가 Non-blocking인지 확인.
- Artifact 변경이 불필요하면 `decision = "APPROVED_WITH_COMMENTS"`로 기록.
- Artifact 변경이 필요하면 승인을 확정하지 않고 STOP.

### 5. Process REJECTED
- `decision = "REJECTED"`로 기록.
- 대상 Artifact를 APPROVED로 전환하지 않고 수정 필요사항 기록 후 STOP.

### 6. Report
다음을 보고한다:
```
Gate: G<n>
Cycle ID: <CYCLE_ID>
Decision: APPROVED / REJECTED
Approved Artifact Versions: <List>
Approval Record: docs/approvals/<CYCLE_ID>/G<n>-<stage>.approval.json
Handoff Status: APPROVED
Next Workflow: /<next-workflow>

Next Workflow has NOT been executed.
```

## Critical Rule

Human Approval 후 **Next Workflow를 자동 실행하지 않는다.**
사용자가 다음 워크플로우를 직접 실행할 수 있도록 안내하고 멈춘다.
