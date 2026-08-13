# Gate Approval Records Repository

This directory archives all formal human sign-offs, review packages, and approval records across project lifecycles.

## Directory Structure

In v1.1, approvals are organized per execution cycle to preserve full audit history without overwriting previous decisions:

```
docs/approvals/
│
├── INIT-001/                                      # Initial SDLC Lifecycle
│   ├── G0-project-definition.approval.json
│   ├── G0-project-definition.review.md
│   ├── G1-requirement-baseline.approval.json
│   ├── G1-requirement-baseline.review.md
│   ├── G2-design-baseline.approval.json
│   ├── G2-design-baseline.review.md
│   ├── G3-implementation-plan.approval.json
│   ├── G3-implementation-plan.review.md
│   ├── G4-release-candidate.approval.json
│   ├── G4-release-candidate.review.md
│   ├── G5-production-release.approval.json
│   └── G5-production-release.review.md
│
├── CR-0001/                                       # First Change Request Cycle
│   ├── G1-requirement-baseline.approval.json      # Re-approved Gates
│   ├── G2-design-baseline.approval.json
│   ├── G3-implementation-plan.approval.json
│   ├── G4-release-candidate.approval.json
│   └── G5-production-release.approval.json
│
└── CR-XXXX/                                       # Subsequent Change Cycles
```

## Approval Preservation Rules
1. **Never Overwrite**: Past approval records are permanently retained in their respective cycle folder.
2. **Upstream Retention**: Unaffected upstream approvals (e.g. G0 during a SPEC change) remain valid in their original cycle folder.
3. **Downstream Re-approval**: All gates from the Earliest Impacted Stage to G5 must be re-approved in the active `CR-XXXX` cycle folder.
