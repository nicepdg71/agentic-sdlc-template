---
artifact_id: "UI-PROMPT-001"
project_id: "<PROJECT_ID>"
cycle_id: "<CYCLE_ID>"
change_id: "<CHANGE_ID_OR_NULL>"
stage: "DESIGN"
artifact_type: "STITCH_PROMPTS"
version: "1.0"
status: "DRAFT"
baseline_version: "<BASELINE_VERSION>"
owner: "@ux"
approval_gate: "G2"
---

# Google Stitch UI Design Prompts: <PROJECT_OR_FEATURE_NAME>

이 문서는 Stitch MCP 서버 미연결 시 또는 Web UI(Google Stitch Console)에서 직접 디자인을 생성할 때 사용하는 구조화된 프롬프트 모음입니다.

---

## 1. Global Design System Context Prompt
Google Stitch의 초기 프로젝트 컨텍스트 설정에 입력하는 프롬프트입니다:

```text
Project: <PROJECT_NAME>
Target Domain: <DOMAIN_TYPE (e.g. Enterprise Dashboard, IoT Signage, Consumer Web)>
Target Users: <TARGET_USER_DESCRIPTION>
Design Tone: <Clean, Modern, Accessible, High Contrast, Minimalist>
Color Palette Requirements:
- Primary: <PRIMARY_COLOR_GOAL>
- Background/Surface: <SURFACE_TONE>
- State Feedback: Success (Green), Warning (Amber), Error (Red), Info (Blue)
Typography & Layout:
- Font: Modern Sans-Serif with full CJK Hangul and Latin character support (e.g. Pretendard, Inter, Roboto)
- Layout Grid: 8pt Grid, Fluid Responsive, Maximum Content Legibility
- Multilingual Layout Support: Accommodate Korean (`ko`) and English (`en`) text variations (1.3x~1.5x length difference) without layout breaks
- Top Navigation: Include a subtle, modern Language Switcher dropdown/toggle (KR / EN)
Accessibility:
- Strict WCAG AA compliance (4.5:1 minimum contrast ratio, touch targets >= 44px)
```

---

## 2. Main Screen Generation Prompts

### Main Screen 1: <MAIN_SCREEN_NAME_1> (Ref: <REQ_ID_1>)
* **Role & Route**: Primary Landing / Dashboard (`<ROUTE_1>`)
* **Stitch Generation Prompt**:
```text
Create a modern, responsive <MAIN_SCREEN_NAME_1> screen for <PROJECT_NAME>.
Screen Architecture & Layout:
- Top Navigation / Header with brand logo, search bar, and user profile
- Primary workspace grid / table displaying <KEY_DATA_ENTITIES>
- Action Toolbar: CTA button "New <Entity>", Filter toggle, and Batch action buttons

Key Components:
1. <COMPONENT_1>: <SPECS_AND_CONTROLS>
2. <COMPONENT_2>: <SPECS_AND_DATA_DISPLAY>
3. <COMPONENT_3>: <SPECS_AND_KPI_CARDS>

States to generate:
- Default State with realistic dummy data
- Empty State with guided illustration and "Create First <Entity>" CTA
- Loading State with skeleton placeholders
- Error State with inline retry button
```

---

## 3. Sub Screen, Modal & Drawer Generation Prompts

### Sub Screen 1: <SUB_SCREEN_NAME_1> (Ref: <REQ_ID_2>)
* **Role & Parent**: Detail View (Parent: `<MAIN_SCREEN_NAME_1>`)
* **Stitch Generation Prompt**:
```text
Create a detail view screen for <ENTITY_NAME> in <PROJECT_NAME>.
- Header with Breadcrumbs ("<MAIN_SCREEN_NAME_1> / <ENTITY_NAME>"), Title, and Status Badge
- Tabbed layout: Overview, Details, Audit Logs, Settings
- Actions: Edit, Delete, Export, and Back to List button
```

### Modal 1: <MODAL_NAME_1> (Ref: <REQ_ID_3>)
* **Role & Trigger**: Creation / Edit Dialog (Triggered from `<MAIN_SCREEN_NAME_1>` CTA button)
* **Stitch Generation Prompt**:
```text
Create a focused modal dialog for creating a new <ENTITY_NAME>.
- Centered overlay with backdrop blur
- Form fields: <FIELD_1> (required input), <FIELD_2> (dropdown select), <FIELD_3> (toggle)
- Validation hints and helper texts
- Footer buttons: "Cancel" (ghost), "Create <Entity>" (primary solid)
```

---

## 4. Inter-Screen Workflow & Navigation Prompts

Stitch 프로젝트 내 화면 간 상호작용 및 연결 흐름을 위한 프롬프트입니다:

```text
Inter-Screen Workflow & Navigation Instructions for <PROJECT_NAME>:
1. Main Dashboard -> Sub Detail Screen:
   - Clicking a table row or card in <MAIN_SCREEN_NAME_1> navigates to <SUB_SCREEN_NAME_1> with selected entity ID.
   - Breadcrumb navigation on <SUB_SCREEN_NAME_1> allows returning directly to <MAIN_SCREEN_NAME_1>.
2. Main Dashboard -> Create Modal:
   - Clicking "+ New <Entity>" on <MAIN_SCREEN_NAME_1> opens <MODAL_NAME_1> as a foreground dialog.
   - Submitting or canceling <MODAL_NAME_1> dismisses modal and refreshes <MAIN_SCREEN_NAME_1>.
3. Filter & Search Workflow:
   - Toggling filter on <MAIN_SCREEN_NAME_1> opens slide-over drawer and applies query parameters to the data view.
```

---

## 5. Human Review, Refinement & Confirmation Protocol

Stitch Web Console 또는 MCP를 통한 생성이 완료된 후 **인간 디자이너/엔지니어의 검토 및 수정이 완료될 때까지 에이전트는 대기**합니다:

- [ ] Google Stitch 프로젝트를 열고 생성된 Main Screens, Sub Screens, Modal을 확인
- [ ] 레이아웃 간격, 타이포그래피, 컬러 대비, 반응형 동작을 Stitch에서 직접 수정/보정
- [ ] 화면 간 워크플로우(클릭 시 모달 오픈, 뒤로가기 링크 등) 연결성 검토
- [ ] 수정이 완료되면 Antigravity 세션에 다음 명령을 입력하여 Handoff 동기화 및 G2 진행:
  ```text
  CONFIRM_STITCH_DESIGN_COMPLETED
  ```
