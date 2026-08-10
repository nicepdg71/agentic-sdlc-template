---
name: security-review
description: Review architecture, code, configuration, dependencies, authentication, authorization, data access, secrets, input handling, and deployment risks for security findings.
---

# Purpose

Security Risk를 독립적인 관점에서 식별한다.

# Applicable Stages

DESIGN
BUILD
VERIFY
RELEASE

# Primary Agent

@security

# Inputs

상황에 따라:

- Security Requirement
- Architecture
- Code
- Dependency
- Infrastructure
- Configuration
- Deployment Plan

# Procedure

1. Trust Boundary를 확인한다.
2. Authentication을 검토한다.
3. Authorization을 검토한다.
4. Secret 관리방식을 검토한다.
5. Input Validation을 검토한다.
6. Output/Data Exposure를 검토한다.
7. API Security를 검토한다.
8. Database Permission/RLS를 검토한다.
9. Dependency Risk를 검토한다.
10. Logging의 민감정보 노출을 검토한다.
11. Deployment Configuration을 검토한다.
12. Finding을 Severity별로 분류한다.

# Severity

CRITICAL
HIGH
MEDIUM
LOW
INFO

# Blockers

CRITICAL Finding은 자동진행을 중단한다.

HIGH Finding은 Risk Acceptance 또는 수정상태를
명확하게 확인해야 한다.

# Output

- Security Findings
- Severity
- Evidence
- Recommendation
- Blocking Status

# Traceability

Security Requirement
→ Security Control
→ Finding/Test

# Handoff

호출한 Stage와 Human Gate에 반환한다.