---
description: Deploy the approved release candidate to production after explicit G5 approval and transition to cycle closure.
---

# Production Deployment Workflow

## Purpose

G5에서 명시적으로 승인된 Release Candidate만 Production에 배포하고, 배포 결과를 검증하여 Change Cycle 종료를 준비한다.

## Required Agent

Primary:
@devops

Supporting:
- @qa
- @security

## Required Skills

- release-readiness

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Target Release Version & Commit**: G5 승인 레코드와 일치 여부 확인

## Preconditions

1. 현재 Cycle ID에 해당하는 G5 Approval Record(`docs/approvals/<CYCLE_ID>/G5-production-release.approval.json`)의 `decision == "APPROVED"` 확인
2. Release Handoff (`docs/05-release/RELEASE_HANDOFF.json`)의 `status == "APPROVED"` 확인
3. Approval Record에 명시된 Version/Commit과 실제 배포 대상 일치 확인
4. Required CI 상태 PASS 확인

## Critical Restriction

명시적인 G5 Approval을 확인할 수 없는 경우 어떤 Production 작업도 수행하지 않는다.

## Execution

1. Release Candidate 식별 및 G5 Approval 확인
2. 승인된 배포 절차 수행 (`scripts/deploy-production.sh`)
3. Smoke Test 실행 (`scripts/smoke-test.sh`)
4. 모니터링 및 상태 확인
5. 실패 시 승인된 롤백 기준 적용 (`docs/05-release/ROLLBACK_PLAN.md`)
6. 최종 결과 기록

## Completion & Next Steps

배포 성공 시:
- **INITIAL Cycle (`INIT-001`)**:
  - Production v1.0.0 출시 완료.
  - 다음 변경 요구 발생 시: `/request-change` 실행.
- **CHANGE Cycle (`CR-XXXX`)**:
  - Production 새 버전 출시 완료.
  - 공식 Change Cycle 종료를 위해 다음 Workflow 실행 안내:
    ```
    PRODUCTION DEPLOYMENT COMPLETED
    Cycle ID: <CYCLE_ID>
    Target Version: <VERSION>

    Recommended next workflow:
    /close-change-cycle
    ```
