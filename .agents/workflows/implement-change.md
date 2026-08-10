---
description: Implement an explicitly approved implementation plan and produce build evidence.
---

# Implementation Workflow

## Purpose

G3에서 승인된 Implementation Plan을
정확한 범위 내에서 구현한다.


## Required Agent

@engineer

Supporting when applicable:

@security
@ai


## Required Skills

- secure-coding
- code-review


## Conditional Skills

- runtime-ai-design (when runtime_ai.enabled = true and the change affects runtime AI)
- database-design-review (when database impact exists)
- security-review (when security boundary is affected)


## Preconditions

다음을 먼저 엄격하게 검증한다 (Stage Entry Validation).

1. G3 Approval Record (`docs/approvals/G3-implementation-plan.approval.json`)의 `decision == "APPROVED"` 확인
2. Approval Record에 명시된 Approved Implementation Plan Version과 현재 `docs/03-implementation/IMPLEMENTATION_PLAN.md`의 실제 파일 버전 일치 확인

어느 하나라도 일치하지 않거나 누락된 경우:

APPROVAL / HANDOFF INTEGRITY CHECK FAILED

를 출력하고 즉시 STOP한다 (다음 Stage를 자동으로 복구하거나 Version을 임의 변경하지 않는다).


## Required Inputs

- APPROVED IMPLEMENTATION_PLAN.md
- Approved Design
- Requirement
- Acceptance Criteria
- Contract
- ADR


## Execution

1. project.yaml 확인

2. Rules 확인

3. Git Branch 확인

4. Protected Branch 직접 작업 여부 확인

5. BUILD Stage Prompt를 읽는다.

.agents/prompts/03-implementation/PROMPT.md

6. PHASE B — IMPLEMENTATION만 수행한다.

7. 승인된 Plan 범위만 구현한다.

8. 필요한 Unit Test를 작성한다.

9. Lint를 실제 실행한다.

10. Unit Test를 실제 실행한다.

11. Build를 실제 실행한다.

12. git diff를 검토한다.

13. Secret 포함 여부를 확인한다.

14. Scope 밖 변경을 확인한다.


## Expected Outputs

- Source Code
- Unit Tests
- 승인된 범위의 Migration 초안
- 필요한 Documentation
- docs/03-implementation/BUILD_HANDOFF.json


## Validation

다음을 실제 결과로 기록한다.

Lint:
PASS / FAIL / NOT_EXECUTED

Unit Test:
PASS / FAIL / NOT_EXECUTED

Build:
PASS / FAIL / NOT_EXECUTED

실행하지 않은 항목을 PASS로 기록하지 않는다.


## Human Gate

이 Workflow는 별도 Stage Gate를 새로 만들지 않는다.

VERIFY로 넘길 수 있는 상태인지 결과를 보고한다.

단, 승인범위를 벗어나는 변경이 필요하면
자동 진행하지 않고 STOP한다.


## Stop Conditions

- G3 미승인
- Plan Version 불일치
- Scope 변경 필요
- 신규 주요 Dependency 필요
- Architecture 변경 필요
- 별도 승인 필요한 DB 변경
- Security Blocker
- Test FAIL
- Build FAIL


## Next Command

구현 검증 준비가 완료되면:

/verify-release-candidate