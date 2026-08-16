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
  - Font Family (Korean CJK): `Pretendard, "Noto Sans KR", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
  - Font Family (English Latin): `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
  - Word Break Standard: Korean (`word-break: keep-all;`), English (`word-break: normal; overflow-wrap: break-word;`)
  - Heading Scales: H1 (`<SIZE>`), H2 (`<SIZE>`), H3 (`<SIZE>`)
  - Body Scales: Regular (`<SIZE>`), Small (`<SIZE>`)
- **Spacing & Elevation**:
  - Grid Base: `<4PX_OR_8PX>`
  - Radii / Shadows: `<BORDER_RADIUS_AND_ELEVATION_TOKENS>`
- **Internationalization (i18n) Tokens**:
  - Resource Catalog: `locales/ko.json`, `locales/en.json`
  - Key Naming Convention: `<domain>.<screen>.<component_or_element>` (e.g. `dashboard.header.title`, `common.button.save`)
  - Layout Tolerance: Accommodate 1.3x~1.5x string length expansion between English and Korean without container clipping.

## Screen & Component Specifications

### 1. Main Screens Specification

#### Screen: <MAIN_SCREEN_NAME>
- **Route / URL**: `<ROUTE_PATH>`
- **Layout Structure**: `<HEADER_SIDEBAR_CONTENT_FOOTER>`
- **Component Breakdown**:
  - `<COMPONENT_A>`: <PURPOSE_AND_BEHAVIOR>
  - `<COMPONENT_B>`: <PURPOSE_AND_BEHAVIOR>
- **State Specifications**:
  - Loading State: <SKELETON_SPECS>
  - Empty State: <EMPTY_ILLUSTRATION_AND_CTA>
  - Error State: <ERROR_BANNER_AND_RETRY_ACTION>
  - Success / Active State: <DATA_POPULATED_VIEW>

### 2. Sub Screens & Modals Specification

#### Sub Screen / Modal: <SUB_SCREEN_OR_MODAL_NAME>
- **Parent Screen**: `<PARENT_MAIN_SCREEN>`
- **Trigger**: `<USER_ACTION_OR_EVENT>`
- **Container Type**: `<PAGE / MODAL_DIALOG / SLIDE_OVER_DRAWER>`
- **Component Breakdown**:
  - `<FORM_OR_DETAIL_PANEL>`: <PURPOSE_AND_INPUT_FIELDS>
  - `<ACTION_BUTTON_GROUP>`: <SUBMIT_CANCEL_DELETE_ACTIONS>
- **State Specifications**:
  - Validation Error State: <FIELD_LEVEL_ERROR_HINTS>
  - Submission Loading State: <BUTTON_SPINNER_AND_DISABLED_INPUTS>

## Inter-Screen Navigation & State Transition Specs

### 1. Navigation Flow & Routing Contracts
- **Route Definitions**:
  - `/`: `<MAIN_DASHBOARD_ROUTE>`
  - `/<entity>`: `<MAIN_LIST_ROUTE>`
  - `/<entity>/:id`: `<SUB_DETAIL_ROUTE>`
- **Modal Stack & Overlay Order**:
  - Base Screen -> Overlay Backdrop (`rgba(0,0,0,0.5)`) -> Modal Dialog (`z-index: 50`) -> Toast Feedback (`z-index: 100`)

### 2. State & Parameter Passing Contracts
| Transition | Source -> Target | Parameters Passed | State Sync / Invalidation |
|---|---|---|---|
| Main to Detail | `<MAIN_SCREEN>` -> `<SUB_SCREEN>` | `id: string` | Load target detail cache |
| Create Submit | `<CREATE_MODAL>` -> `<MAIN_SCREEN>` | `payload: Object` | Invalidate list cache & trigger refresh |
| Filter Apply | `<FILTER_DRAWER>` -> `<MAIN_SCREEN>` | `filters: QueryParams` | Update URL query & filter list |

### 3. Back Navigation & Dismissal Rules
- `ESC` key or backdrop click closes active Modal / Drawer without side effects.
- Breadcrumb / Back button returns user to previous route preserving pagination/filter state.

## Interaction & Animation Guidelines
- Micro-interactions: <HOVER_ACTIVE_FOCUS_TRANSITIONS>
- Responsive Breakpoints: Mobile (`<640px`), Tablet (`640-1024px`), Desktop (`>1024px`)

## Verification Checklist for BUILD & QA
- [ ] Responsive design implemented across all Main & Sub screens
- [ ] Screen transitions, modals, and drawers follow specified workflow and parameter contracts
- [ ] Back navigation and dismiss flows behave consistently
- [ ] Contrast ratios meet WCAG AA standards
- [ ] All 5 UI states handled properly in code
- [ ] Touch/click targets minimum 44x44px
