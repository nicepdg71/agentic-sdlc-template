---
artifact_id: "UI-VERIFY-001"
project_id: "<PROJECT_ID>"
cycle_id: "<CYCLE_ID>"
change_id: "<CHANGE_ID_OR_NULL>"
stage: "VERIFY"
artifact_type: "UI_VERIFICATION_REPORT"
version: "1.0"
status: "DRAFT"
baseline_version: "<BASELINE_VERSION>"
owner: "@qa"
approval_gate: "G4"
---

# UI Verification Report: <PROJECT_OR_FEATURE_NAME>

## Stitch Reference
- Project Name: `<STITCH_PROJECT_NAME>`
- Reference Document: `docs/02-design/ui/STITCH_PROJECT_REF.json`
- UI Handoff Specification: `docs/02-design/ui/UI_DESIGN_HANDOFF.md`

## Screens Verified

| Screen | Requirement | Functional Verification | Visual Verification | Result |
|---|---|---|---|---|
| `<SCREEN_NAME>` | `<REQ_ID>` | `<PASS/FAIL>` | `<PASS/FAIL>` | `<PASS/FAIL>` |

## State Verification

| State | Result | Notes |
|---|---|---|
| Loading State | `<PASS/FAIL>` | `<NOTES>` |
| Empty State | `<PASS/FAIL>` | `<NOTES>` |
| Error State | `<PASS/FAIL>` | `<NOTES>` |
| Success State | `<PASS/FAIL>` | `<NOTES>` |
| Disabled State | `<PASS/FAIL>` | `<NOTES>` |

## Responsive Verification
- Desktop Viewport (>1024px): `<PASS/FAIL - NOTES>`
- Tablet Viewport (640-1024px): `<PASS/FAIL - NOTES>`
- Mobile Viewport (<640px): `<PASS/FAIL - NOTES>`

## Accessibility Findings
- Color Contrast (WCAG AA): `<PASS/FAIL>`
- Keyboard Tab Navigation: `<PASS/FAIL>`
- Form Labels & ARIA Attributes: `<PASS/FAIL>`

## Visual Differences
- `<RECORD_ANY_MINOR_OR_MAJOR_VISUAL_DISCREPANCIES_VS_STITCH>`

## Blocking Issues
- `<LIST_ANY_BLOCKING_UI_DEFECTS_OR_NONE>`

## Overall UI Result
PASS / FAIL / BLOCKED
