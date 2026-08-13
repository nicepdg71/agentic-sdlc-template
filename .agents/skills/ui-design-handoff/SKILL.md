---
name: ui-design-handoff
description: Assess UI applicability, convert approved UI requirements into user flows, screen requirements, component states, accessibility guidelines, and structured design handoffs for Stitch or implementation.
---

# Purpose

Requirement와 UI Design Tool / Implementation 사이의
표준 Handoff를 생성하고 UI 필요성을 체계적으로 평가/연동한다.

# Applicable Stages

DESIGN, BUILD, VERIFY

# Primary Agent

@ux

# Supporting Agents

- @architect
- @engineer

# Activation Lifecycle

- **Activation Phase 1**: DESIGN Stage 시작 시 UI/UX 설계 필요성 평가 (`NOT_REQUIRED`, `RECOMMENDED`, `REQUIRED`).
- **Activation Phase 2**: Human에게 `UI DESIGN DECISION REQUIRED` 제안 후 사용자 선택(`USE_STITCH`, `SKIP_STITCH`, `USE_OTHER_UI_TOOL`) 대기.
- **Activation Phase 3**: 사용자가 UI Tool(예: Stitch)을 선택하면 해당 Tool Integration 수행 및 Handoff 생성.

# Inputs

- Approved Requirements & User Stories
- Acceptance Criteria
- Business Rules & UI NFRs

# Procedure

1. **UI 필요성 평가 (Applicability Assessment)**:
   - 웹/모바일 UI 존재 여부, 사용자 데이터 입력, 대시보드, 다중 화면 흐름, 상태 표현(Loading/Empty/Error/Success), 반응형/접근성 중요도 평가.
2. **사용자 결정 제안**:
   - `UI DESIGN DECISION REQUIRED` 출력 및 사용자 응답 수령.
3. **UI Design Brief 작성**:
   - 화면별 목적, 필수 컴포넌트, 상태별 요구사항, 프롬프트 정의 (`UI_DESIGN_BRIEF.md`).
4. **UI Design Handoff 작성**:
   - 컴포넌트 계층, 레이아웃 규격, 컬러/타이포그래피 토큰, 이벤트 흐름, 접근성 체크리스트 정의 (`UI_DESIGN_HANDOFF.md`).
5. **Tool Reference 기록**:
   - `STITCH_PROJECT_REF.json`에 프로젝트 참조 저장 (API Key 제외).
6. **DESIGN Baseline 통합**:
   - G2 심사 대상에 UI 산출물을 포함.

# Checklist

- [ ] 모든 주요 User Story에 대응하는 UI Flow/화면 정의
- [ ] 5대 UI State(Default, Loading, Empty, Error, Success) 정의
- [ ] 반응형 Breakpoint 및 모바일/데스크톱 대응 정의
- [ ] 접근성(Contrast, Keyboard Nav, ARIA) 기본 규칙 정의
- [ ] Requirement 범위를 벗어난 임의 기능 없음 확인

# Output

- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
- `docs/02-design/ui/STITCH_PROJECT_REF.json`