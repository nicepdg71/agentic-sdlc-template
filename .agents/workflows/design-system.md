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
   - Stitch MCP 연결 상태를 확인하고 다음 두 가지 모드 중 하나로 동작한다:

   ---

   ### 🅰️ Mode 1: MCP 실시간 자동 연동 모드 (Live MCP Mode)
   * **조건**: `.agents/mcp_config.json` 또는 Antigravity IDE에 Stitch MCP 서버가 등록되어 통신 가능한 경우
   * **동작**:
     1. Requirement 기반으로 `docs/02-design/ui/UI_DESIGN_BRIEF.md` 생성.
     2. Stitch MCP 툴을 직접 호출하여 화면 레이아웃, 컬러/타이포그래피 토큰, 컴포넌트 메타데이터를 실시간 조회·동기화.
     3. 동기화된 정보를 바탕으로 `docs/02-design/ui/UI_DESIGN_HANDOFF.md` 및 `docs/02-design/ui/STITCH_PROJECT_REF.json` 생성.

   ---

   ### 🅱️ Mode 2: 프롬프트 생성 모드 (Fallback Prompt Mode / Web UI 연계)
   * **조건**: Stitch MCP 서버가 미등록/미연결 상태인 경우
   * **동작**:
     1. **설정 안내 출력**: 사용자에게 Stitch MCP 미연결 상태임을 알리고 설정 가이드를 제공한다:
        ```text
        STITCH MCP SETUP REQUIRED (Fallback Mode Activated)

        Reason: Stitch MCP server is not configured in .agents/mcp_config.json.

        [Stitch MCP 연동 방법]
        방법 1: .agents/mcp_config.json에 Stitch MCP 추가 (Remote SSE 방식 권장)
        {
          "mcpServers": {
            "stitch": {
              "serverUrl": "https://stitch.googleapis.com/mcp",
              "headers": {
                "X-Goog-Api-Key": "<YOUR_GOOGLE_STITCH_API_KEY>"
              }
            }
          }
        }
        (또는 Stdio npx 방식: "command": "npx", "args": ["-y", "@google/stitch-mcp-server"])

        방법 2: Antigravity IDE 전역 MCP 설정에 Stitch 서버 등록
        ```
     2. **프롬프트 산출물 자동 생성**:
        `.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md`를 기반으로 `docs/02-design/ui/STITCH_PROMPTS.md`를 자동 생성한다. 사용자는 이 프롬프트를 Google Stitch Web Console에 입력하여 디자인을 생성할 수 있다.
     3. **UI 산출물 초안 생성**:
        `docs/02-design/ui/UI_DESIGN_BRIEF.md`, `docs/02-design/ui/UI_DESIGN_HANDOFF.md`, `docs/02-design/ui/STITCH_PROJECT_REF.json` 초안을 작성한다.
     4. **Fail-Closed 안전 원칙**:
        Non-UI 아키텍처 설계는 계속 진행할 수 있으나, UI 산출물(`UI_DESIGN_HANDOFF.md` 등)이 검토/확정되기 전에는 G2 승인을 완료할 수 없다.

   ---

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