---
name: ui-design-handoff
description: Convert approved UI requirements into user flows, screen requirements, component states, accessibility considerations, and a structured handoff for Stitch or implementation.
---

# Purpose

Requirement와 UI Design Tool 사이의
표준 Handoff를 생성한다.

# Applicable Stages

DESIGN

# Primary Agent

@ux

# Activation

project.yaml의 UI Design이 활성화된 경우 사용한다.

# Inputs

- Approved Requirement
- User Story
- Acceptance Criteria
- Business Rule
- UI 관련 NFR

# Procedure

1. 사용자 Goal을 식별한다.
2. 주요 User Flow를 정의한다.
3. 필요한 Screen을 식별한다.
4. Screen별 목적을 정의한다.
5. 입력/출력 Component를 정의한다.
6. 다음 UI State를 정의한다.
   - Empty
   - Loading
   - Success
   - Error
   - Disabled
7. Responsive Requirement를 정의한다.
8. 기본 Accessibility 요구를 확인한다.
9. Stitch 입력 Prompt를 생성한다.
10. 생성된 UI가 Requirement와 일치하는지 검토한다.
11. 승인된 UI 정보를 DESIGN Handoff 형태로 정리한다.

# Checklist

- [ ] 모든 주요 User Story에 UI Flow 존재
- [ ] Error State 존재
- [ ] Loading State 존재
- [ ] Mobile/Responsive 요구 검토
- [ ] Requirement 밖 기능 없음

# Blockers

- User Flow 결정 불가능
- 서로 충돌하는 UI Requirement
- UI 변경이 Business Rule 변경을 요구함

# Output

- UI Flow
- Screen Definition
- Component State
- Stitch Prompt
- UI Handoff

# Traceability

User Story
→ Screen
→ UI Component

# Handoff

@architect 및 DESIGN Stage로 반환한다.