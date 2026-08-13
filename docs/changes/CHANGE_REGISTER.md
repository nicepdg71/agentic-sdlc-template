# Change Request Register

This register maintains a master index of all formal Change Requests processed throughout the lifecycle of the project.

## Master Change Log

| Change ID | Title | Requester | Earliest Stage | Status | Released Version | Created At | Closed At |
|---|---|---|---|---|---|---|---|
| *None* | *Initial Baseline (INIT-001)* | System | DEFINE | COMPLETED | v1.0.0 | - | - |

## Register Maintenance Policy
1. Every new Change Request triggered via `/request-change` is assigned an incrementing ID (`CR-0001`, `CR-0002`, ...).
2. The register is updated on:
   - Initial submission (Status: `DRAFT`)
   - Human decision (Status: `APPROVED` / `REJECTED`)
   - Release closure (Status: `CLOSED`)
