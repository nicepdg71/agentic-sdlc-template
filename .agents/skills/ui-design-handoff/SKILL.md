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
- **Activation Phase 3**: UI Tool(예: Stitch)을 통해 디자인 생성 후 `STITCH UI DESIGN REVIEW & REFINEMENT REQUIRED`로 인간 검토 대기.
- **Activation Phase 4**: `CONFIRM_STITCH_DESIGN_COMPLETED` 수령 후 최종 화면 사양 및 워크플로우를 Handoff 산출물에 동기화.

# Inputs

- Approved Requirements & User Stories
- Acceptance Criteria
- Business Rules & UI NFRs

# Procedure

1. **UI 필요성 평가 (Applicability Assessment)**:
   - 웹/모바일 UI 존재 여부, 사용자 데이터 입력, 대시보드, 다중 화면 흐름, 상태 표현(Loading/Empty/Error/Success), 반응형/접근성 중요도 평가.
2. **사용자 결정 제안**:
   - `UI DESIGN DECISION REQUIRED` 출력 및 사용자 응답 수령.
3. **UI Design Brief 작성 (`UI_DESIGN_BRIEF.md`)**:
   - **Main Screens**: 핵심 워크스페이스, 대시보드, 메인 리스트 등 1차 진입 화면의 목적, 주요 컨트롤, 표시 엔티티 정의.
   - **Sub Screens & Modals**: 상세 뷰, 생성/수정 모달, 필터/검색 드로어, 확인 다이얼로그 등의 목적 및 진입 조건 정의.
   - **Screen Workflow & Transition Map**: 화면 간 전이 트리거 이벤트, 파라미터 전달, 복귀/닫기 흐름, Mermaid 플로우차트 정의.
   - **Multilingual (i18n) UI Requirements**: 한국어(`ko`)/영어(`en`) 지원, 언어 전환기(Language Switcher) 위치, 다국어 날짜/숫자 포맷, 한-영 텍스트 길이 가변성(1.3~1.5배) 고려.
   - 5대 UI State(Default, Loading, Empty, Error, Success) 및 접근성/반응형 요구사항 명세.
4. **Stitch 생성 및 Human 검토/수정 연계**:
   - Stitch MCP 또는 프롬프트로 Main/Sub 화면, Screen Workflow 및 다국어(ko/en) 레이아웃 지시문 일괄 전달.
   - Stitch 생성 완료 후 사람의 검토 및 수정이 완료될 때까지 대기 (`CONFIRM_STITCH_DESIGN_COMPLETED` 대기).
5. **UI Design Handoff 작성 (`UI_DESIGN_HANDOFF.md`)**:
   - 확정된 Main/Sub 화면별 컴포넌트 계층, 레이아웃 규격, CJK/Latin 폰트 타이포그래피 토큰, 화면 간 내비게이션 및 상태 전이 사양, i18n 리소스 번들 키 구조, 접근성 체크리스트 확정.
6. **Tool Reference 기록 (`STITCH_PROJECT_REF.json`)**:
   - 프로젝트 ID, 검증된 Main/Sub 화면 목록, 워크플로우 식별자, 인간 검토 완료 상태 기록.
7. **DESIGN Baseline 통합**:
   - G2 심사 대상에 UI 산출물을 포함하여 `G2 DESIGN BASELINE APPROVAL REQUIRED` 준비.

# Checklist

- [ ] 모든 주요 User Story에 대응하는 Main Screens 및 Sub Screens 분할 정의
- [ ] 화면 간 상호작용 워크플로우 (Trigger, Transition, Parameter passing, Back flow) 정의
- [ ] 화면 흐름을 시각화한 Mermaid 플로우차트 포함 여부
- [ ] 한국어/영어 다국어 지원 및 언어 전환기(Language Switcher) 컴포넌트 정의
- [ ] 한-영 텍스트 길이 가변성(1.3~1.5x) 및 CJK/Latin 폰트 가독성 토큰 정의
- [ ] 5대 UI State(Default, Loading, Empty, Error, Success) 정의
- [ ] 반응형 Breakpoint 및 모바일/데스크톱 대응 정의
- [ ] 접근성(Contrast, Keyboard Nav, ARIA) 기본 규칙 정의
- [ ] Stitch 자동 생성 후 사람의 검토/수정 완료(`CONFIRM_STITCH_DESIGN_COMPLETED`) 확인
- [ ] Requirement 범위를 벗어난 임의 기능 없음 확인

# Output

- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
- `docs/02-design/ui/STITCH_PROJECT_REF.json`