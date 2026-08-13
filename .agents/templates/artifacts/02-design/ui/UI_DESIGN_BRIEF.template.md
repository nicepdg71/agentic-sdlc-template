---
artifact_id: "UI-BRIEF-001"
project_id: "<PROJECT_ID>"
cycle_id: "<CYCLE_ID>"
change_id: "<CHANGE_ID_OR_NULL>"
stage: "DESIGN"
artifact_type: "UI_DESIGN_BRIEF"
version: "1.0"
status: "DRAFT"
baseline_version: "<BASELINE_VERSION>"
owner: "@ux"
approval_gate: "G2"
---

# UI Design Brief: <PROJECT_OR_FEATURE_NAME>

## Target Users
- <PRIMARY_PERSONAS_AND_TARGET_USERS>

## Primary User Goals
- <KEY_GOALS_USERS_WANT_TO_ACCOMPLISH>

## Required Screens

| Screen | Purpose | Related Requirement |
|---|---|---|
| <SCREEN_NAME> | <SCREEN_PURPOSE_DESCRIPTION> | <REQ_ID_OR_FR_ID> |

## Required States
- **Default**: <DEFAULT_VIEW_STATE>
- **Loading**: <SKELETON_OR_SPINNER_STATE>
- **Empty**: <ZERO_DATA_GUIDE_STATE>
- **Error**: <INLINE_OR_BANNER_ERROR_STATE>
- **Success**: <COMPLETION_OR_TOAST_FEEDBACK_STATE>

## Responsive Requirements
- Desktop: <DESKTOP_LAYOUT_GUIDELINES>
- Mobile/Tablet: <MOBILE_VIEWPORT_GUIDELINES>

## Accessibility Requirements
- Color Contrast (WCAG AA): <CONTRAST_RATIO_TARGETS>
- Keyboard Navigation & Focus Order: <FOCUS_FLOW>
- Screen Reader Labels: <ARIA_LABELING_REQUIREMENTS>

## Out of Scope
- <EXPLICIT_UI_OUT_OF_SCOPE_ITEMS>

## Stitch Design Prompt
```text
<STRUCTURED_PROMPT_PREPARED_FOR_GOOGLE_STITCH_DESIGN_GENERATION>
```
