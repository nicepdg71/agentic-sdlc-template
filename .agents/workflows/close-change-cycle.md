---
description: Formally verify and close an active Change Cycle after successful release and deployment.
---

# Close Change Cycle Workflow

## Purpose

새로운 릴리스(v1.1.0 등)가 완료된 후, 해당 Change Cycle의 모든 재승인 Gate 완료 여부,
Production 배포 검증, Traceability 완성도를 확인하고 Change Cycle을 공식 종료(`CLOSED`)한다.

## Required Agent

Primary:
@pm

Supporting:
@analyst
@release

## Inputs

- Active Change ID (e.g. `CR-0001`)
- Approval Records in `docs/approvals/<CR_ID>/`
- `docs/changes/<CR_ID>/IMPACT_ANALYSIS.md`
- `docs/changes/<CR_ID>/CHANGE_TRACEABILITY.md`
- `docs/05-release/RELEASE_HANDOFF.json`

## Execution Steps

1. **Active Change ID 확인**:
   - `docs/changes/CHANGE_REGISTER.md`에서 현재 `APPROVED` 상태인 Change Request 확인.
2. **필수 Gate 통과 검증**:
   - `IMPACT_ANALYSIS.md`에 명시된 모든 Re-approval Gate(예: G1, G2, G3, G4, G5)의 승인 레코드가 `docs/approvals/<CR_ID>/`에 존재하는지 확인.
3. **Production 배포 상태 검증**:
   - `docs/05-release/RELEASE_HANDOFF.json`의 `status == "APPROVED"`, 릴리스 버전 및 Commit SHA 확인.
4. **Traceability 무결성 검증**:
   - `docs/changes/<CR_ID>/CHANGE_TRACEABILITY.md`의 모든 항목이 PASS 상태이며 미연결/고아 코드가 없는지 검증.
5. **CHANGE_CLOSURE.md 생성**:
   - `.agents/templates/changes/CHANGE_CLOSURE.template.md`를 기반으로 `docs/changes/<CR_ID>/CHANGE_CLOSURE.md` 작성 및 `status = "CLOSED"` 설정.
6. **CHANGE_REGISTER.md 갱신**:
   - 해당 CR의 상태를 `CLOSED`, `Closed At` 타임스탬프, 배포된 버전 기록.
7. **종료 보고 출력**:
   ```
   CR-XXXX
   Required Gates:
     G1 PASS
     G2 PASS
     G3 PASS
     G4 PASS
     G5 PASS

   Production: <Version>
   Commit: <Commit_SHA>
   Traceability: COMPLETE

   CR-XXXX
   status = CLOSED
   ```

## Next Command

프로젝트는 다음 개발 또는 새로운 변경 요청을 처리할 준비가 완료되었습니다:
- `/request-change` (다음 변경 요청 발생 시)
