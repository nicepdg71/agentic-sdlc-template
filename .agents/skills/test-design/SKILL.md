---
name: test-design
description: Design requirement-based unit, integration, contract, end-to-end, negative, regression, and edge-case tests with explicit traceability and evidence classification.
---

# Purpose

Requirement와 Acceptance Criteria를
검증 가능한 Test Case로 변환한다.

# Applicable Stages

VERIFY

# Primary Agent

@qa

# Inputs

- Requirements
- Acceptance Criteria
- Design
- Implementation
- Existing Tests

# Procedure

1. Critical AC를 식별한다.
2. Test Level을 결정한다.
3. Positive Case를 작성한다.
4. Negative Case를 작성한다.
5. Boundary/Edge Case를 작성한다.
6. Integration Case를 작성한다.
7. Contract Test를 작성한다.
8. 주요 User Flow의 E2E Test를 정의한다.
9. Regression 범위를 정의한다.
10. Test Data를 정의한다.
11. 실행 결과를 Evidence로 기록한다.
12. AC → TC → Result를 연결한다.

# Result Values

PASS
FAIL
SKIPPED
NOT_EXECUTED
BLOCKED

# Blockers

- Critical AC에 Test 없음
- Test 환경 없음
- Test 결과 재현 불가
- 요구사항이 검증 불가능

# Output

- Test Plan
- Test Cases
- Test Evidence
- Coverage Gap

# Traceability

Requirement
→ Acceptance Criteria
→ Test Case
→ Test Result

# Handoff

VERIFY Stage에 반환한다.