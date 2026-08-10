---
name: implementation-planning
description: Analyze approved requirements, design, and repository state to produce an implementation plan before source code is modified.
---

# Purpose

Coding 전에 변경범위와 위험을 명확히 한다.

# Applicable Stages

BUILD — Phase A

# Primary Agent

@engineer

# Inputs

- Approved Design
- Requirement
- Acceptance Criteria
- Current Repository
- Contract
- ADR

# Procedure

1. 관련 Requirement ID를 식별한다.
2. Acceptance Criteria를 확인한다.
3. 현재 구현 상태를 분석한다.
4. 생성파일을 식별한다.
5. 수정파일을 식별한다.
6. 변경하지 않을 영역을 명시한다.
7. API 영향을 분석한다.
8. DB 영향을 분석한다.
9. Dependency 영향을 분석한다.
10. Security 영향을 분석한다.
11. Test Plan을 작성한다.
12. Risk를 작성한다.
13. Rollback 전략을 작성한다.

# Critical Rule

이 Skill을 수행하는 동안
Source Code를 수정하지 않는다.

# Blockers

- Scope Change 필요
- Architecture 변경 필요
- 주요 Dependency 추가 필요
- DB 변경 승인 필요
- 중요 설계정보 누락

# Output

IMPLEMENTATION_PLAN 내용

# Traceability

Requirement
→ Implementation Plan
→ Planned Files

# Handoff

G3 검토 대상으로 반환한다.