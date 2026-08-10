---
name: code-review
description: Review code changes for correctness, scope compliance, bugs, regressions, maintainability, security, tests, secrets, and unintended changes before verification or pull request approval.
---

# Purpose

변경된 Code가 승인된 목적과 범위를
정확히 만족하는지 검토한다.

# Applicable Stages

BUILD
VERIFY

# Primary Agent

@engineer / @qa

# Inputs

- Requirement
- Implementation Plan
- git diff
- Test Result
- Design

# Procedure

1. 변경목적을 확인한다.
2. Diff 범위를 확인한다.
3. 승인되지 않은 변경을 탐지한다.
4. Logic Error를 검사한다.
5. Edge Case를 검사한다.
6. Error Handling을 검사한다.
7. Security Risk를 검사한다.
8. Secret 포함 여부를 검사한다.
9. Test Coverage를 검토한다.
10. 관련 없는 Refactoring을 탐지한다.
11. API/DB Contract 위반을 확인한다.
12. 개선사항과 Blocker를 구분한다.

# Finding Classification

BLOCKER
MAJOR
MINOR
SUGGESTION

# Blockers

- Secret 포함
- Scope 밖 변경
- Critical Bug
- Security Vulnerability
- Contract Breaking Change
- Test 실패 은폐

# Output

- Review Findings
- Blocking Issues
- Recommended Fixes

# Traceability

Change
→ Requirement
→ Review Finding

# Handoff

BUILD 또는 VERIFY Stage에 반환한다.