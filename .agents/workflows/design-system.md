---
description: Design the system architecture and UI/UX from the approved requirement baseline.
---

# System Design Workflow

## Purpose

승인된 Requirement Baseline을 기반으로 구현 가능한 Software Architecture 및 UI/UX Design Baseline으로 변환한다.

## Required Agent

Primary:
@architect

Supporting when applicable:
- @ux
- @ai
- @security

## Required Skills

- architecture-design
- security-review
- ui-design-handoff
- stitch-design-integration (when Stitch is selected)
- api-contract-design (when interfaces are required)
- database-design-review (when persistent database is required)
- runtime-ai-design (when runtime_ai.enabled = true)

## Execution Context 확인

- **Cycle Type**: `INITIAL` / `CHANGE`
- **Cycle ID**: `INIT-001` 또는 `CR-XXXX`
- **Active Change ID**: null 또는 `CR-XXXX`
- **Current Approved Baseline**: 기존 Architecture 및 UI 설계 버전
- **Earliest Impacted Stage**: `DESIGN` (또는 상위)

## Preconditions

1. 현재 Cycle ID에 해당하는 G1 Approval Record(`docs/approvals/<CYCLE_ID>/G1-requirement-baseline.approval.json`)의 `decision == "APPROVED"` 확인
2. Analysis Handoff (`docs/01-analysis/ANALYSIS_HANDOFF.json`)의 `status == "APPROVED"` 확인

## UI Applicability Assessment & Human Decision

DESIGN 시작 시 UI/UX 설계 필요성을 평가한다:

1. **평가 기준**:
   - 웹/모바일 화면 존재 여부
   - 사용자 데이터 입력 필요성
   - Dashboard 존재 여부
   - 복수 Screen / User Flow 존재 여부
   - Loading / Empty / Error 등 상태 표현 중요성
   - Responsive Design & UI 일관성 필요성
   *(CLI, Batch Job, Backend-only API, Library, Headless Service인 경우 `NOT_REQUIRED`)*

2. **분류**:
   - `NOT_REQUIRED`
   - `RECOMMENDED`
   - `REQUIRED`

3. **Human UI Decision 제안 (RECOMMENDED 또는 REQUIRED인 경우)**:
   Agent는 도구를 임의로 자동 선택하지 않고, 반드시 사용자에게 다음을 출력하고 결정을 요청한다:
   ```
   UI DESIGN DECISION REQUIRED

   UI design is recommended for this project.

   Reason:
   - <Evaluation reasons>

   Recommended Tool:
   Google Stitch

   Integration:
   Antigravity <-> Stitch MCP

   Options:
   USE_STITCH
   SKIP_STITCH
   USE_OTHER_UI_TOOL: <tool>
   ```
   *Human Decision 전에는 UI Tool Integration을 실행하지 않는다.*

4. **Stitch Integration 절차 (Human 선택이 USE_STITCH인 경우)**:
   - `project.yaml`의 `toolchain.ui_design.enabled = true`, `selected_tool = stitch`로 설정.
   - Stitch MCP 연결 상태 확인.
   - **Fail-Closed 원칙**: MCP가 연결되어 있지 않은 경우 `STITCH INTEGRATION BLOCKED`를 출력한다.
     ```
     STITCH INTEGRATION BLOCKED
     Reason: Stitch MCP not connected
     Required Action: Configure Stitch MCP in .agents/mcp_config.json
     ```
     *(Non-UI 아키텍처 설계는 진행 가능하나, UI Artifact가 누락된 상태에서는 G2를 완료할 수 없음)*
   - Secret/API Key를 Repository에 절대 기록하지 않는다.
   - Requirement 기반으로 `docs/02-design/ui/UI_DESIGN_BRIEF.md` 생성.
   - Stitch MCP를 통해 Design Context/Tokens를 가져와 `docs/02-design/ui/UI_DESIGN_HANDOFF.md` 및 `docs/02-design/ui/STITCH_PROJECT_REF.json` 생성.

## Execution

1. `project.yaml` 및 Rules 읽기
2. `@architect` 및 `@ux` 역할 적용
3. `.agents/prompts/02-design/PROMPT.md` 읽기
4. **Baseline-aware Differential Update (CHANGE 모드 시)**:
   - 기존 Architecture / UI 산출물을 기반으로 변경/신규 컴포넌트만 수정 반영.
5. 산출물 생성/갱신:
   - `docs/02-design/ARCHITECTURE.md`
   - `docs/02-design/DESIGN.md`
   - `docs/02-design/DATA_MODEL.md`
   - `docs/02-design/SECURITY_DESIGN.md`
   - `docs/02-design/ui/UI_DESIGN_BRIEF.md` (UI 활성화 시)
   - `docs/02-design/ui/UI_DESIGN_HANDOFF.md` (UI 활성화 시)
   - `docs/02-design/ui/STITCH_PROJECT_REF.json` (Stitch 사용 시)
   - `docs/02-design/adr/`
   - `contracts/`
   - `docs/02-design/DESIGN_HANDOFF.json`

## Validation

- Critical Requirement Coverage, Architecture Consistency, Data Model, Interface Contracts, Security, UI Design Alignment 검증

## Gate Review Preparation

1. Stage Validation 수행
2. Gate 대상 Artifact status를 `IN_REVIEW`로 변경 (UI Artifacts 포함)
3. `DESIGN_HANDOFF.json`의 `status = "READY_FOR_APPROVAL"` 설정
4. `docs/approvals/<CYCLE_ID>/G2-design-baseline.review.md` 생성
5. Review Package 작성

## Human Gate

G2 — Design Baseline Approval

완료 후 반드시 다음을 출력하고 STOP한다:

```
G2 DESIGN BASELINE APPROVAL REQUIRED
Cycle ID: <CYCLE_ID>
```

Critical Rule: Human Gate 요청 후 반드시 STOP하며, 다음 Workflow를 자동 실행하지 않는다.

## Next Command

G2 승인 후:
`/plan-implementation`