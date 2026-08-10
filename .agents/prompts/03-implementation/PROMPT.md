# BUILD Stage Prompt

## ROLE

Primary Agent:

@engineer

Supporting Agents:

@architect
@security
@ai when required


## STAGE

BUILD


## OBJECTIVE

승인된 Design을 기반으로
승인된 범위의 Software를 구현한다.

중요:

코드를 바로 수정하지 않는다.

먼저 Implementation Plan을 작성하고
G3 승인을 받아야 한다.


## PRECONDITIONS

- G2 APPROVED
- DESIGN Baseline APPROVED


## REQUIRED INPUTS

- APPROVED DESIGN_HANDOFF.json
- REQUIREMENTS.md
- ACCEPTANCE_CRITERIA.md
- ARCHITECTURE.md
- DESIGN.md
- DATA_MODEL.md
- SECURITY_DESIGN.md
- Contract
- ADR


## RULES

- Plan Before Change
- Scope Control
- Git Change Control
- Security and Secrets
- Data and Database Governance
- Testing Evidence

승인되지 않은 Design을 변경하지 않는다.


# PHASE A — IMPLEMENTATION PLAN


## PROCEDURE A

### 1. Requirement 확인

이번 변경과 관련된 Requirement ID를 식별한다.

### 2. Acceptance Criteria 확인

완료조건을 명확히 한다.

### 3. Repository Analysis

현재 Codebase와 Dependency를 확인한다.

### 4. Change Scope

다음을 구분한다.

- 생성파일
- 수정파일
- 변경하지 않을 영역

### 5. Impact Analysis

다음을 검토한다.

- API
- Database
- Security
- Dependency
- Configuration
- Deployment

### 6. Test Plan

어떻게 검증할 것인지 정의한다.

### 7. Risk

주요 위험을 정리한다.

### 8. Rollback

가능한 Rollback 방법을 작성한다.


## REQUIRED OUTPUT A

docs/03-implementation/IMPLEMENTATION_PLAN.md


## HUMAN APPROVAL A

G3 — Implementation Plan Approval

다음을 출력한다.

G3 IMPLEMENTATION PLAN APPROVAL REQUIRED

그리고 STOP한다.

G3 승인 이전에는
Source Code를 수정하지 않는다.


# PHASE B — IMPLEMENTATION


## PRECONDITION B

G3가 APPROVED여야 한다.


## PROCEDURE B

### 1. Working Branch 확인

Protected Branch에 직접 작업하지 않는다.

### 2. Approved Plan 범위 구현

Implementation Plan에 승인된 범위만 구현한다.

### 3. Unit Test

구현과 함께 Test를 작성한다.

### 4. Migration

필요한 경우 초안을 생성하되
Database Rule을 적용한다.

### 5. Documentation

변경에 필요한 기술문서를 갱신한다.

### 6. Lint

실제 실행한다.

### 7. Unit Test

실제 실행한다.

### 8. Build

실제 실행한다.

### 9. Diff Review

관련 없는 변경과 Secret 포함 여부를 검사한다.

### 10. Completion Report

실제 결과를 보고한다.


## REQUIRED OUTPUT B

- Source Code
- Unit Tests
- 필요한 Migration
- 변경된 Documentation
- docs/03-implementation/BUILD_HANDOFF.json


## ARTIFACT TEMPLATES

다음 Template을 기반으로 실제 Artifact를 docs/03-implementation/에 생성한다.

- .agents/templates/artifacts/03-implementation/IMPLEMENTATION_PLAN.template.md → docs/03-implementation/IMPLEMENTATION_PLAN.md
- .agents/templates/artifacts/03-implementation/BUILD_HANDOFF.template.json → docs/03-implementation/BUILD_HANDOFF.json

템플릿 사용 규칙:
1. Template 자체를 수정하지 않는다.
2. Template 구조와 Frontmatter를 유지하며 Placeholder를 실제 값으로 대체한다.
3. 해당하지 않는 Section은 삭제하지 말고 N/A 또는 NONE으로 명시한다.
4. 신규 Artifact의 초기 status는 DRAFT로 작성한다.


## VALIDATION

다음을 구분하여 기록한다.

Lint:
PASS / FAIL / NOT EXECUTED

Unit Test:
PASS / FAIL / NOT EXECUTED

Build:
PASS / FAIL / NOT EXECUTED

실행하지 않은 항목을 PASS로 기록하지 않는다.


## STOP CONDITIONS

- G2 미승인
- G3 미승인
- Scope 밖 변경 필요
- 신규 주요 Dependency 필요
- Architecture 변경 필요
- DB Schema 변경 승인 필요
- Security Blocker
- Test 실패
- Build 실패


## HANDOFF

구현이 완료되면 VERIFY Stage가 사용하는 입력:

- BUILD_HANDOFF.json
- Source Code
- Test Code
- Build Evidence
- Requirement / AC