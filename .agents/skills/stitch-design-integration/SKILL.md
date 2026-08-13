---
name: stitch-design-integration
description: Integrate Google Stitch with Antigravity via Model Context Protocol (MCP) to fetch design tokens, layouts, screen structures, and establish UI design handoff baselines.
---

# Purpose

Google Stitch 디자인 도구와 Antigravity Agent를 MCP(Model Context Protocol)로 연동하여,
승인된 요구사항 기반의 UI 디자인 프롬프트를 전달하고,
생성된 디자인 컨텍스트(토큰, 레이아웃, 컴포넌트)를 안전하게 가져와 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json`으로 구조화한다.

# Applicable Stages

DESIGN, BUILD, VERIFY

# Primary Agent

@ux

# Supporting Agents

- @architect
- @engineer
- @qa

# Inputs

- Approved Requirements & Acceptance Criteria
- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- Stitch MCP Configuration in `.agents/mcp_config.json`
- Stitch Project ID / Name

# Procedure

1. **UI 필요성 및 사용자 결정 확인**:
   - `toolchain.ui_design.enabled == true` 및 `toolchain.ui_design.selected_tool == "stitch"` 확인.
2. **Stitch MCP 연결 상태 검증 (Fail-Closed)**:
   - Antigravity MCP 환경 설정에 Stitch MCP 서버가 구성되어 있는지 확인.
   - MCP 연결이 불가능한 경우 `STITCH INTEGRATION BLOCKED`를 출력하고 진행 차단.
   - *보안 원칙: Stitch API Key는 절대 코드/문서 저장소에 직접 기록하지 않으며, 환경 변수 또는 MCP 설정을 통해서만 참조한다.*
3. **UI Design Brief 생성**:
   - 승인된 Requirement, User Story, AC를 기반으로 `docs/02-design/ui/UI_DESIGN_BRIEF.md` 작성 (대상 사용자, 목표, 필수 화면, 상태별 UI 요구사항, Stitch Prompt 포함).
4. **Stitch Design Context Fetch**:
   - Stitch MCP를 통해 디자인 프로젝트의 화면 구성, 컬러/타이포그래피 토큰, 레이아웃 메타데이터를 조회.
5. **Human UI Review**:
   - 생성/동기화된 UI 디자인에 대해 Human Review를 요청.
6. **UI Artifacts 생성 및 Baseline 등록**:
   - `docs/02-design/ui/STITCH_PROJECT_REF.json`에 프로젝트 참조 메타데이터 기록 (API Key 제외).
   - `docs/02-design/ui/UI_DESIGN_HANDOFF.md`에 컴포넌트 사양, 상태(Loading/Empty/Error/Success), 반응형 규칙, 접근성 요구사항을 정리.
   - G2 Design Baseline 심사 대상에 등록.
7. **BUILD / VERIFY 단계 연동**:
   - BUILD 시: `@engineer`가 Stitch Design Tokens와 Handoff를 참조하여 UI 컴포넌트 구현.
   - VERIFY 시: `@qa`가 Antigravity 브라우저 환경에서 실제 구현된 UI와 Stitch 디자인을 비교 검증하고 `UI_VERIFICATION_REPORT.md` 작성.

# Critical Rules

- **Fail-Closed**: 사용자가 `USE_STITCH`를 선택했으나 MCP 미연결 시, "Stitch 없이 그냥 진행하겠다"고 임의 판단하지 않고 `STITCH INTEGRATION BLOCKED`로 보고 후 멈춘다.
- **SSOT Hierarchy**: `Approved Requirement -> Approved UI Design Handoff -> Approved Stitch Project Reference -> Implementation`.
- **Conflict Escalation**: `DESIGN.md`와 Stitch UI 디자인 간 충돌 발생 시 `DESIGN CONFLICT DETECTED`를 보고한다.

# Output

- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
- `docs/02-design/ui/STITCH_PROJECT_REF.json`
- `docs/04-test/UI_VERIFICATION_REPORT.md` (검증 단계)
