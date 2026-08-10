---
name: database-design-review
description: Design or review data models, database schemas, constraints, migrations, indexes, permissions, and destructive-change risks while respecting database approval rules.
---

# Purpose

Data Requirement를 안전한 Data Model과
Database 변경안으로 변환·검토한다.

# Applicable Stages

DESIGN
BUILD

# Primary Agent

@architect

Supporting:

@engineer
@security

# Inputs

- Data Requirements
- Architecture
- Existing Schema
- Security Requirement

# Procedure

1. 주요 Entity를 식별한다.
2. Entity Relationship을 정의한다.
3. 식별자를 정의한다.
4. 주요 Constraint를 정의한다.
5. Nullability를 검토한다.
6. Index 필요성을 검토한다.
7. 데이터 무결성을 검토한다.
8. Permission/RLS 요구를 확인한다.
9. Schema 변경이라면 Migration 방향을 작성한다.
10. Backward Compatibility를 검토한다.
11. Data Loss 위험을 검사한다.
12. Rollback 가능성을 검토한다.

# Human Approval Required

다음은 별도 승인을 요구한다.

- Table 생성/삭제
- Column 삭제
- Type 변경
- Migration 실행
- RLS
- Permission
- Production Data 변경

# Blockers

- Data Loss 가능성
- Irreversible Migration
- 권한모델 불명확
- Production Data 영향 불명확

# Output

- Data Model Review
- Schema Proposal
- Migration Risk
- Permission Review

# Traceability

Data Requirement
→ Entity
→ Schema

# Handoff

DESIGN 또는 BUILD Stage에 반환한다.