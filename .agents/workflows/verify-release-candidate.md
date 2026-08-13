---
description: Verify the implementation against requirements, UI handoffs, and prepare a release candidate decision.
---

# Release Candidate Verification Workflow

## Purpose

구현된 Software가 승인된 Requirement, Acceptance Criteria 및 UI Design을 실제로 만족하는지 검증한다.

## Required Agent

Primary:
@qa

Supporting:
- @security
- @ux (when UI design is active)

## Required Skills

- test-design
- security-review
- code-review
- stitch-design-integration (when UI design is active)

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 기존 테스트 베이스라인 및 산출물
- **Earliest Impacted Stage**: `VERIFY` (또는 상위)

## Preconditions

1. 현재 Cycle ID에 해당하는 G3 Approval Record(`docs/approvals/<CYCLE_ID>/G3-implementation-plan.approval.json`)의 `decision == "APPROVED"` 확인
2. Build Handoff (`docs/03-implementation/BUILD_HANDOFF.json`)의 `status == "READY"` 확인

## Required Inputs

- `REQUIREMENTS.md` / `ACCEPTANCE_CRITERIA.md` / `TRACEABILITY_MATRIX.md`
- `DESIGN.md` / `BUILD_HANDOFF.json`
- **UI Design Baseline (UI 활성화 시)**:
  - `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
  - `docs/02-design/ui/STITCH_PROJECT_REF.json`
- Source Code & Test Code

## Execution

1. `project.yaml` 및 Rules 읽기
2. `@qa`, `@security`, `@ux` 역할 적용
3. `.agents/prompts/04-test/PROMPT.md` 읽기
4. 테스트 케이스 설계 및 실제 실행
5. **UI Design Verification (UI 활성화 시)**:
   - 구현된 UI를 승인된 Stitch 디자인/핸드오프와 시각적/기능적으로 비교 검증 (브라우저 검증).
   - 상태별(Loading, Empty, Error, Success), Responsive, Accessibility 검증.
   - `docs/04-test/UI_VERIFICATION_REPORT.md` 생성.
6. 산출물 생성/갱신:
   - `docs/04-test/TEST_PLAN.md`
   - `docs/04-test/TEST_CASES.md`
   - `docs/04-test/TEST_REPORT.md`
   - `docs/04-test/SECURITY_REPORT.md`
   - `docs/04-test/UI_VERIFICATION_REPORT.md` (UI 활성화 시)
   - `docs/04-test/VERIFY_HANDOFF.json` (metadata에 `cycle_id`, `change_id` 기록)

## Validation

- Critical AC PASS, Required CI PASS, Critical Security Finding 없음, Blocking Defect 없음 확인

## Gate Review Preparation

1. Stage Validation 수행
2. Gate 대상 Artifact status를 `IN_REVIEW`로 설정 (UI Report 포함)
3. `VERIFY_HANDOFF.json`의 `status = "READY_FOR_APPROVAL"` 설정
4. `docs/approvals/<CYCLE_ID>/G4-release-candidate.review.md` 생성
5. Review Package 작성

## Human Gate

G4 — Release Candidate Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G4 RELEASE CANDIDATE APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G4 승인 후:
`/prepare-release`