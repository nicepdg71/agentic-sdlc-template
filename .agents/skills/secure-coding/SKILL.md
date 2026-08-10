---
name: secure-coding
description: Implement approved changes while applying secure coding practices for inputs, outputs, authentication, authorization, secrets, errors, logging, dependencies, and data access.
---

# Purpose

승인된 Implementation Plan을
보안 원칙에 맞게 구현한다.

# Applicable Stages

BUILD — Phase B

# Primary Agent

@engineer

# Inputs

- APPROVED Implementation Plan
- Security Design
- Coding Standard
- Data Contract
- API Contract

# Procedure

1. 승인된 범위만 구현한다.
2. 외부 입력을 신뢰하지 않는다.
3. Input Validation을 적용한다.
4. Authentication 경계를 유지한다.
5. Authorization을 서버 측에서 검증한다.
6. Secret을 코드에 포함하지 않는다.
7. 오류 메시지에 민감정보를 노출하지 않는다.
8. Log에 Secret/민감정보를 기록하지 않는다.
9. Parameterized Query 또는 안전한 Data Access를 사용한다.
10. 새로운 Dependency가 필요하면 승인 여부를 확인한다.
11. Unit Test를 추가한다.
12. Security 영향이 있는 변경을 명시한다.

# Blockers

- 승인되지 않은 Security Boundary 변경
- Secret 필요하지만 안전한 관리방법 없음
- 승인되지 않은 Dependency
- 인증/인가 설계 변경 필요

# Output

- Secure Implementation
- Unit Test
- Security Impact Notes

# Traceability

Implementation Plan
→ Code
→ Test

# Handoff

BUILD Stage에 반환한다.