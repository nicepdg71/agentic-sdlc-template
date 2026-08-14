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
- Font: Modern Sans-Serif (e.g. Inter, Roboto)
- Layout Grid: 8pt Grid, Fluid Responsive, Maximum Content Legibility
Accessibility:
- Strict WCAG AA compliance (4.5:1 minimum contrast ratio, touch targets >= 44px)
```

---

## 2. Screen-by-Screen Stitch Generation Prompts

### Screen 1: <SCREEN_NAME_1> (Ref: <REQ_ID_1>)
* **Purpose**: <SCREEN_PURPOSE>
* **Stitch Generation Prompt**:
```text
Create a responsive <SCREEN_NAME> screen for <PROJECT_NAME>.
Key Components:
1. <COMPONENT_1>: <SPECS>
2. <COMPONENT_2>: <SPECS>
3. <COMPONENT_3>: <SPECS>

States to provide:
- Default State with representative mock data
- Empty State with guidance illustration and CTA button
- Loading State with skeleton UI placeholders
- Error State with inline retry mechanism
```

---

### Screen 2: <SCREEN_NAME_2> (Ref: <REQ_ID_2>)
* **Purpose**: <SCREEN_PURPOSE>
* **Stitch Generation Prompt**:
```text
Create a responsive <SCREEN_NAME> screen for <PROJECT_NAME>.
Key Components:
1. <COMPONENT_1>: <SPECS>
2. <COMPONENT_2>: <SPECS>

States to provide:
- Default State
- Loading & Error States
```

---

## 3. Stitch Output Import & Handoff Checklist
Stitch Web Console에서 디자인 생성을 완료한 후:
- [ ] 생성된 디자인의 Screen Layout 및 Color Token을 `docs/02-design/ui/UI_DESIGN_HANDOFF.md`에 복사/정리
- [ ] Stitch 프로젝트 ID/URL을 `docs/02-design/ui/STITCH_PROJECT_REF.json`에 기록
- [ ] G2 Design Baseline 검토 패키지에 등록
