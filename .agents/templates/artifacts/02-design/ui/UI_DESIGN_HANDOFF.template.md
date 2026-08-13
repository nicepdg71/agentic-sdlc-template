---
artifact_id: "UI-HANDOFF-001"
project_id: "<PROJECT_ID>"
cycle_id: "<CYCLE_ID>"
change_id: "<CHANGE_ID_OR_NULL>"
stage: "DESIGN"
artifact_type: "UI_DESIGN_HANDOFF"
version: "1.0"
status: "DRAFT"
baseline_version: "<BASELINE_VERSION>"
owner: "@ux"
approval_gate: "G2"
---

# UI Design Handoff: <PROJECT_OR_FEATURE_NAME>

## Executive Summary
- Tool Source: Google Stitch / MCP Integration
- Stitch Reference: `docs/02-design/ui/STITCH_PROJECT_REF.json`
- Target Framework/Style: <CSS_OR_COMPONENT_LIBRARY>

## Design Tokens
- **Colors**:
  - Primary: `<COLOR_HEX_OR_HSL>`
  - Secondary / Accent: `<COLOR_HEX_OR_HSL>`
  - Neutral Background / Surface: `<COLOR_HEX_OR_HSL>`
  - Text (High/Medium/Low Contrast): `<COLOR_HEX_OR_HSL>`
  - State Colors (Success/Warning/Error/Info): `<COLOR_HEX_OR_HSL>`
- **Typography**:
  - Font Family: `<FONT_FAMILY>`
  - Heading Scales: H1 (`<SIZE>`), H2 (`<SIZE>`), H3 (`<SIZE>`)
  - Body Scales: Regular (`<SIZE>`), Small (`<SIZE>`)
- **Spacing & Elevation**:
  - Grid Base: `<4PX_OR_8PX>`
  - Radii / Shadows: `<BORDER_RADIUS_AND_ELEVATION_TOKENS>`

## Screen & Component Specifications

### Screen: <SCREEN_NAME>
- **Route / URL**: `<ROUTE_PATH>`
- **Layout Structure**: `<HEADER_SIDEBAR_CONTENT_FOOTER>`
- **Component Breakdown**:
  - `<COMPONENT_A>`: <PURPOSE_AND_BEHAVIOR>
  - `<COMPONENT_B>`: <PURPOSE_AND_BEHAVIOR>
- **State Specifications**:
  - Loading State: <SKELETON_SPECS>
  - Empty State: <EMPTY_ILLUSTRATION_AND_CTA>
  - Error State: <ERROR_BANNER_AND_RETRY_ACTION>

## Interaction & Animation Guidelines
- Micro-interactions: <HOVER_ACTIVE_FOCUS_TRANSITIONS>
- Responsive Breakpoints: Mobile (`<640px`), Tablet (`640-1024px`), Desktop (`>1024px`)

## Verification Checklist for BUILD & QA
- [ ] Responsive design implemented without horizontal scroll
- [ ] Contrast ratios meet WCAG AA standards
- [ ] All 5 UI states handled properly in code
- [ ] Touch/click targets minimum 44x44px
