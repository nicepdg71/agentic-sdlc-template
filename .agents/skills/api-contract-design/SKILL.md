---
name: api-contract-design
description: Design stable API, event, or message contracts from approved requirements and architecture, including inputs, outputs, errors, validation, versioning, and compatibility.
---

# Purpose

Service 또는 Component 간 Interface를
명확하고 검증 가능한 Contract로 정의한다.

# Applicable Stages

DESIGN

# Primary Agent

@architect

# Inputs

- Requirement
- Acceptance Criteria
- Architecture
- Data Model

# Procedure

1. Contract 목적을 정의한다.
2. Consumer와 Provider를 식별한다.
3. Operation 또는 Event를 정의한다.
4. Input Schema를 정의한다.
5. Output Schema를 정의한다.
6. 필수/선택 Field를 명확히 한다.
7. Validation Rule을 정의한다.
8. Error Contract를 정의한다.
9. Authentication/Authorization 필요성을 식별한다.
10. Versioning 정책을 검토한다.
11. Breaking Change 위험을 확인한다.
12. Contract Test 가능성을 확인한다.

# Blockers

- Consumer 요구 불명확
- 주요 Data Definition 미결정
- Breaking Change 발생
- 승인되지 않은 외부 Interface 추가

# Output

- API Contract
- Event Contract
- Error Contract
- Compatibility Risk

# Traceability

Requirement
→ Interface Contract

# Handoff

DESIGN Stage 및 VERIFY의 Contract Test로 전달한다.