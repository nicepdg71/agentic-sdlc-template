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
   ```text
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
    - Stitch 연동은 **4-Phase 생명주기**를 따르며, Stitch 생성 완료 후 사람의 수정/검토 완료(`CONFIRM_STITCH_DESIGN_COMPLETED`) 전까지 **다음 단계를 진행하지 않고 블로킹**된다:

    ---

    ### 🅰️ Step 4.1: UI 사양 및 화면 워크플로우 정의 (Phase 1)
    - Requirement 및 User Story 기반으로 `docs/02-design/ui/UI_DESIGN_BRIEF.md` 생성:
      - **Main Screens**: 대시보드, 메인 리스트/워크스페이스 등 핵심 1차 진입 화면.
      - **Sub Screens & Modals**: 상세 뷰, 생성/수정 모달, 검색/필터 드로어, 확인 다이얼로그 등 2차 화면.
      - **Screen Workflow & Transition Map**: 화면 간 전이 트리거 이벤트, 데이터/파라미터 전달, 복귀/뒤로가기 흐름, Mermaid 플로우차트.

    ---

    ### 🅱️ Step 4.2: Stitch 디자인 요청 전달 (Phase 2 - Live MCP or Fallback Prompt)
    * **Mode 1 (Live MCP Mode)**:
      - `.agents/mcp_config.json`의 Stitch MCP 도구를 호출하여 Main/Sub 화면 목록과 화면 간 워크플로우를 일괄 전달하고 자동 생성 실행.
    * **Mode 2 (Fallback Prompt Mode)**:
      - Stitch MCP 미연결 시 `STITCH MCP SETUP REQUIRED` 출력 및 가이드 제공.
      - `docs/02-design/ui/STITCH_PROMPTS.md`에 Global Context, Main Screens, Sub Screens, Screen Workflow Prompts를 자동 생성.

    ---

    ### 🆎 Step 4.3: 인간 검토/수정 대기 블로킹 게이트 (Phase 3 - Mandatory Blocking Stop)
    - Stitch에서 디자인 작성이 완료된 후, 에이전트는 **절대 다음 단계를 임의로 진행하지 않고 즉시 실행을 중단**한다.
    - 에이전트는 다음 메시지를 출력하고 대기한다:
      ```text
      STITCH UI DESIGN REVIEW & REFINEMENT REQUIRED
      Project: <PROJECT_NAME_OR_ID>

      Stitch has completed automated generation for Main/Sub screens and screen workflows.
      Human review and adjustments are required in Google Stitch.

      Actions for Human:
      1. Open Google Stitch (Project: <PROJECT_ID_OR_NAME>).
      2. Review and adjust layouts, components, responsive styles, and screen transitions.
      3. When your review and modifications in Stitch are complete, execute:
         CONFIRM_STITCH_DESIGN_COMPLETED
      ```

    ---

    ### 🅾️ Step 4.4: 완료 확인 및 Handoff 최종 동기화 (Phase 4)
    - 인간으로부터 `CONFIRM_STITCH_DESIGN_COMPLETED` 명령을 수령한 후:
      1. Stitch의 최종 디자인(토큰, 레이아웃, 컴포넌트, 화면 흐름)을 `docs/02-design/ui/UI_DESIGN_HANDOFF.md`에 최종 동기화.
      2. `docs/02-design/ui/STITCH_PROJECT_REF.json`의 `human_review_status`를 `COMPLETED`로 업데이트하고 `confirmed_by`, `confirmed_at` 기록.
      3. G2 심사 패키지 준비로 전환.

    ---

    *Fail-Closed 원칙: UI 산출물(`UI_DESIGN_HANDOFF.md`, `STITCH_PROJECT_REF.json`)이 인간 검토 완료 및 확정되기 전에는 G2 승인을 완료할 수 없다.*
    *보안 원칙: Secret/API Key는 절대 코드나 문서 저장소에 기록하지 않는다.*

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
   - `docs/02-design/ui/STITCH_PROMPTS.md` (Stitch 선택 시 생성)
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