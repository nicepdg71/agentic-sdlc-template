---
name: change-impact-analysis
description: Classify incoming change requests, perform differential impact analysis against current baseline, identify affected artifacts, determine earliest impacted stage and required re-approval gates, and flag downstream artifacts for STALE transition.
---

# Purpose

기존 승인된 Baseline과 신규 변경 요청(Change Request) 간의
영향 범위를 분석하고, Earliest Impacted Stage 및 재승인 Gate를 결정한다.

# Applicable Stages

CHANGE_CONTROL (Pre-re-entry), DEFINE, SPEC, DESIGN, BUILD, VERIFY, RELEASE

# Primary Agent

@analyst

# Supporting Agents

- @pm
- @architect
- @security

# Inputs

- User / Stakeholder Change Request
- Current Production Release Version & Commit
- Active Approved Baselines:
  - `docs/00-project-definition/`
  - `docs/01-analysis/`
  - `docs/02-design/` (including `docs/02-design/ui/`)
  - `contracts/`
  - `docs/03-implementation/`
  - `docs/04-test/`
  - `docs/05-release/`
- Prior Approval Records in `docs/approvals/`

# Procedure

1. **Change Request 접수 및 분류**:
   - Change ID 부여 (`CR-0001`, `CR-0002`, ...)
   - 변경 유형 분류 (Scope, Requirement, Architecture/UI, Code/BugFix, Test, Config)
   - `docs/changes/CR-XXXX/CHANGE_REQUEST.md` 생성
2. **Current Baseline 비교 및 Diff Analysis**:
   - 현재 승인된 산출물과 변경 요구사항을 비교
   - 유지(Retained), 변경(Modified), 신규(Added), 삭제(Deprecated) 산출물 분류
3. **영향 영역 매트릭스(Impact Matrix) 작성**:
   - Requirement / Architecture / UI / API / DB / AI / Security / Code / Test / Release 영향 여부 평가
4. **Earliest Impacted Stage 결정**:
   - Earliest Impacted Stage 원칙에 따라 재진입할 첫 번째 Stage 도출:
     - Scope/목표 변경 -> `DEFINE` (G0 -> G5)
     - 요구사항 추가/변경 -> `SPEC` (G1 -> G5)
     - Architecture/API/DB/UI 설계 변경 -> `DESIGN` (G2 -> G5)
     - 구현방법/코드/Bug 수정 -> `BUILD PLAN` (G3 -> G5)
     - Test/Evidence 변경 -> `VERIFY` (G4 -> G5)
     - 배포설정만 변경 -> `RELEASE` (G5)
5. **재승인 대상 Gate 및 상위 승인 보존 확인**:
   - 상위 승인은 유지 (예: Requirement 변경 시 G0 유지)
   - Earliest Stage부터 G5까지 재승인 목록 확정
6. **Downstream Artifact STALE 후보 식별**:
   - 영향받는 하위 산출물들을 `STALE` 전환 목록으로 등록
7. **Impact Analysis 산출물 작성**:
   - `docs/changes/CR-XXXX/IMPACT_ANALYSIS.md` 및 `docs/changes/CR-XXXX/CHANGE_TRACEABILITY.md` 생성

# Output

- `docs/changes/CR-XXXX/CHANGE_REQUEST.md`
- `docs/changes/CR-XXXX/IMPACT_ANALYSIS.md`
- `docs/changes/CR-XXXX/CHANGE_TRACEABILITY.md`
- `docs/changes/CHANGE_REGISTER.md` 갱신

# Critical Rules

- Agent는 임의로 "간단한 수정이니 바로 코딩하겠다"고 판단하지 않는다.
- Impact Analysis 완료 후 반드시 STOP하고 Human Approval (`APPROVE CR-XXXX` / `REJECT CR-XXXX`)을 대기한다.
