---
name: requirements-analysis
description: Analyze approved project scope into functional requirements, non-functional requirements, user stories, acceptance criteria, dependencies, conflicts, and traceability during the SPEC stage.
---

# Purpose

승인된 Project Definition을
검증 가능한 SW Requirement로 변환한다.

# Applicable Stages

SPEC

# Primary Agent

@analyst

# Inputs

- APPROVED PROJECT_CHARTER
- APPROVED SCOPE
- 사용자 요구
- 업무자료
- 정책
- 기존 시스템 자료

# Procedure

1. Stakeholder Goal을 식별한다.
2. Functional Requirement 후보를 추출한다.
3. 각 FR에 고유 ID를 부여한다.
4. Non-functional Requirement를 식별한다.
5. User Story를 작성한다.
6. Business Rule을 분리한다.
7. 각 Critical Requirement에 Acceptance Criteria를 작성한다.
8. Data Requirement를 식별한다.
9. External Interface Requirement를 식별한다.
10. Requirement Dependency를 분석한다.
11. Requirement Conflict를 탐지한다.
12. Priority 후보를 작성한다.
13. 모호한 항목을 Open Question으로 이동한다.
14. Goal → Requirement → AC Traceability를 생성한다.

# Requirement Quality Checklist

각 Requirement는 가능한 한:

- 명확한가
- 단일 의미인가
- 검증 가능한가
- Scope 안에 있는가
- 중복되지 않는가
- 구현방법을 강제하지 않는가

를 확인한다.

# Blockers

- Requirement 간 Critical Conflict
- Source가 없는 중요 Requirement
- 검증 불가능한 Critical Requirement
- 승인된 Scope 밖 기능
- Business Decision 필요

# Output

- Functional Requirements
- NFR
- User Stories
- Acceptance Criteria
- Conflict
- Dependency
- Open Questions
- Traceability

# Traceability

Business Goal
→ Requirement
→ Acceptance Criteria

# Handoff

SPEC Stage Prompt로 반환한다.