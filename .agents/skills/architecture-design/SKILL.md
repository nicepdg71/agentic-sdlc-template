---
name: architecture-design
description: Design system context, components, service boundaries, data flows, deployment architecture, observability, error handling, and technical decisions from an approved requirement baseline.
---

# Purpose

Requirement를 구현 가능한
Software Architecture로 변환한다.

# Applicable Stages

DESIGN

# Primary Agent

@architect

# Inputs

- APPROVED Requirements
- Acceptance Criteria
- NFR
- 기술 제약
- 기존 Architecture
- Security Requirement

# Procedure

1. System Context를 작성한다.
2. Actor와 External System을 식별한다.
3. 주요 Component를 정의한다.
4. Component Responsibility를 정의한다.
5. Service Boundary를 결정한다.
6. 주요 Data Flow를 설계한다.
7. Sync/Async Interface를 식별한다.
8. Error Handling 정책을 설계한다 (에러 코드 기반 다국어 메시지 매핑 전략 포함).
9. Internationalization (i18n) & Localization 구조를 설계한다:
   - 클라이언트 요청(`Accept-Language` 헤더 / 프로필 설정) 기반 Locale Resolution Middleware.
   - 다국어 메시지 카탈로그(ko/en) 분리 및 동적 로딩 아키텍처.
   - 전 계층 UTF-8 인코딩 및 시각 표준(UTC) 파이프라인.
10. Logging/Metric/Tracing 필요성을 정의한다.
11. Deployment 구조를 작성한다.
12. Scalability와 Availability 요구를 반영한다.
13. 주요 기술 선택의 대안을 비교한다.
14. 중요한 결정을 ADR 후보로 기록한다.
15. Requirement Coverage를 검증한다.

# Checklist

- [ ] Critical Requirement가 Architecture에 반영됨
- [ ] Component 책임이 겹치지 않음
- [ ] Trust Boundary가 식별됨
- [ ] 주요 Data Flow가 존재함
- [ ] Deployment 구조가 존재함
- [ ] 중요한 기술결정에 근거가 있음

# Blockers

- Critical Requirement 미해결
- 승인되지 않은 Scope 확장 필요
- 중요한 기술선택을 사람이 결정해야 함
- Security Blocker

# Output

- Architecture Proposal
- Component Model
- Data Flow
- Deployment Design
- ADR Candidate
- Risk

# Traceability

Requirement
→ Architecture Component

# Handoff

DESIGN Stage Prompt에 반환한다.