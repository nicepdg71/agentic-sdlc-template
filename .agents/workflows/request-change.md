---
description: Formal workflow to receive, classify, and analyze a change request against current approved baseline.
---

# Request Change Workflow

## Purpose

Production 배포 이후 또는 Baseline 확정 후 발생하는 모든 변경 요구를
공식 Change Request로 접수하고, Baseline 대비 영향도 분석을 수행하여
Earliest Impacted Stage와 재승인 Gate를 결정한다.

## Required Agent

Primary:
@analyst

Supporting:
@pm
@architect
@security

## Required Skills

- change-impact-analysis
- requirements-analysis

## Inputs

- Stakeholder Change Request description
- Current Production Version & Git Commit
- Existing approved artifacts in `docs/`
- Prior Approval records in `docs/approvals/`

## Execution Steps

1. **Change ID 생성**:
   - `docs/changes/CHANGE_REGISTER.md`를 확인하여 다음 번호 할당 (`CR-0001`, `CR-0002` 등).
2. **CHANGE_REQUEST.md 작성**:
   - `.agents/templates/changes/CHANGE_REQUEST.template.md`를 기반으로 `docs/changes/<CR_ID>/CHANGE_REQUEST.md` 생성.
3. **IMPACT_ANALYSIS.md 작성**:
   - `.agents/templates/changes/IMPACT_ANALYSIS.template.md`를 기반으로 `docs/changes/<CR_ID>/IMPACT_ANALYSIS.md` 생성.
   - Impact Matrix 평가 (Requirement, Architecture, UI, DB, AI, Security, Implementation, Test, Release).
   - Earliest Impacted Stage 결정.
   - Required Re-approval Gates (Earliest Stage ~ G5) 및 Unaffected Upstream Approvals 도출.
4. **CHANGE_TRACEABILITY.md 초기화**:
   - `.agents/templates/changes/CHANGE_TRACEABILITY.template.md`를 기반으로 `docs/changes/<CR_ID>/CHANGE_TRACEABILITY.md` 생성.
5. **CHANGE_REGISTER.md 갱신**:
   - Status: `DRAFT`로 항목 추가.
6. **결과 보고 및 Human Decision 요청**:
   - 분석 요약 출력:
     ```
     Change Request ID: CR-XXXX
     Change: <Summary>
     Current Production: <Version>
     Affected Requirements: <List>
     Earliest Impacted Stage: <Stage>
     Potential Impact:
       Requirements: YES/NO
       Architecture: YES/NO
       UI: YES/NO/POSSIBLE
       Runtime AI: YES/NO/POSSIBLE
       Database: YES/NO/POSSIBLE
       Security: REVIEW/NO
       Test: YES/NO
       Release: YES/NO
     Recommended Re-entry: <Stage>
     ```

## Human Decision Required

새로운 Gate(G6 등)를 추가하지 않고, 독립된 Change Authorization 결정을 요청한다:
- `APPROVE CR-XXXX`
- `REJECT CR-XXXX: <reason>`

## Critical Rule

분석 완료 후 **반드시 STOP**하며, 사용자의 명시적 `APPROVE CR-XXXX` 이전에는 다음 Stage를 절대 자동 실행하지 않는다.
