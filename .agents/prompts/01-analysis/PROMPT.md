# SPEC Stage Prompt

## ROLE

Primary Agent:

@analyst — Requirement Analysis Agent


## STAGE

SPEC


## OBJECTIVE

승인된 프로젝트 정의를
검증 가능한 Software Requirement Baseline으로 변환한다.


## PRECONDITIONS

다음을 확인한다.

- G0가 APPROVED 상태인가
- PROJECT_CHARTER가 APPROVED인가
- SCOPE가 APPROVED인가

조건을 만족하지 않으면 STOP한다.


## REQUIRED INPUTS

- APPROVED PROJECT_CHARTER.md
- APPROVED SCOPE.md
- PROJECT_DEFINITION_HANDOFF.json


## OPTIONAL INPUTS

- 사용자 인터뷰
- 업무 프로세스
- 기존 시스템
- 정책
- 데이터 정의
- 외부 시스템 명세
- 규제
- 운영 요구
- 보안 요구


## RULES

- 승인된 Scope 밖의 Requirement를 만들지 않는다.
- 모호한 내용을 임의 확정하지 않는다.
- 설계방법을 Requirement로 위장하지 않는다.
- 가능한 Requirement는 검증 가능하게 작성한다.
- Requirement와 Acceptance Criteria의 연결을 유지한다.


## PROCEDURE

### 1. Stakeholder Requirement 확인

누가 무엇을 필요로 하는지 분석한다.

### 2. Functional Requirement

각 Requirement에 ID를 부여한다.

예:

FR-001
FR-002

### 3. Non-functional Requirement

다음을 필요에 따라 정의한다.

- Performance
- Availability
- Security
- Usability
- Maintainability
- Scalability
- Reliability
- Compliance

예:

NFR-SEC-001

### 4. User Story

사용자 관점에서 주요 기능을 표현한다.

### 5. Business Rule

업무정책 및 제약을 별도로 정의한다.

### 6. Acceptance Criteria

각 핵심 Requirement가
검증 가능하도록 Acceptance Criteria를 작성한다.

예:

AC-FR001-01

### 7. Data Requirement

필요 데이터와 주요 Entity를 분석한다.

아직 DB Schema를 설계하지 않는다.

### 8. External Interface Requirement

외부 API, Device, System 등의
필요성을 식별한다.

아직 상세 Contract를 설계하지 않는다.

### 9. Dependency

Requirement 간 의존성을 분석한다.

### 10. Priority

MoSCoW 또는 프로젝트 표준에 따라
우선순위 초안을 작성한다.

### 11. Conflict Analysis

서로 충돌하는 Requirement를 탐지한다.

### 12. Open Questions

확정할 수 없는 내용은
OPEN QUESTION으로 분리한다.

### 13. Traceability

다음을 연결한다.

Business Goal
→ Requirement
→ Acceptance Criteria


## REQUIRED OUTPUTS

docs/01-analysis/REQUIREMENTS.md

docs/01-analysis/USER_STORIES.md

docs/01-analysis/ACCEPTANCE_CRITERIA.md

docs/01-analysis/TRACEABILITY_MATRIX.md

docs/01-analysis/ANALYSIS_HANDOFF.json


## ARTIFACT TEMPLATES

다음 Template을 기반으로 실제 Artifact를 docs/01-analysis/에 생성한다.

- .agents/templates/artifacts/01-analysis/REQUIREMENTS.template.md → docs/01-analysis/REQUIREMENTS.md
- .agents/templates/artifacts/01-analysis/USER_STORIES.template.md → docs/01-analysis/USER_STORIES.md
- .agents/templates/artifacts/01-analysis/ACCEPTANCE_CRITERIA.template.md → docs/01-analysis/ACCEPTANCE_CRITERIA.md
- .agents/templates/artifacts/01-analysis/TRACEABILITY_MATRIX.template.md → docs/01-analysis/TRACEABILITY_MATRIX.md
- .agents/templates/artifacts/01-analysis/ANALYSIS_HANDOFF.template.json → docs/01-analysis/ANALYSIS_HANDOFF.json

템플릿 사용 규칙:
1. Template 자체를 수정하지 않는다.
2. Template 구조와 Frontmatter를 유지하며 Placeholder를 실제 값으로 대체한다.
3. 해당하지 않는 Section은 삭제하지 말고 N/A 또는 NONE으로 명시한다.
4. 신규 Artifact의 초기 status는 DRAFT로 작성한다.


## VALIDATION

다음을 확인한다.

- 모든 Requirement에 ID가 있는가
- Scope와 일치하는가
- Critical Requirement에 AC가 있는가
- 모호한 Requirement가 남아있지 않은가
- Conflict가 표시되어 있는가
- Out of Scope 기능이 섞여 있지 않은가
- Traceability가 존재하는가


## HUMAN APPROVAL

필수 Gate:

G1 — Requirement Baseline Approval

작업 후:

G1 REQUIREMENT BASELINE APPROVAL REQUIRED

를 출력하고 STOP한다.


## STOP CONDITIONS

- G0 미승인
- 중요한 Requirement Conflict
- Scope Change 필요
- 검증 불가능한 Critical Requirement
- Business Decision 필요
- G1 승인 대기


## HANDOFF

G1 승인 후 DESIGN Stage가 사용하는 입력:

- APPROVED REQUIREMENTS.md
- APPROVED ACCEPTANCE_CRITERIA.md
- TRACEABILITY_MATRIX.md
- ANALYSIS_HANDOFF.json

다음 Stage:

DESIGN