# VERIFY Stage Prompt

## ROLE

Primary Agent:

@qa

Supporting Agent:

@security


## STAGE

VERIFY


## OBJECTIVE

구현된 Software가
승인된 Requirement와 Acceptance Criteria를
실제로 충족하는지 독립적으로 검증한다.


## PRECONDITIONS

- BUILD 결과가 존재한다.
- Build Evidence가 존재한다.
- 테스트 가능한 상태이다.


## REQUIRED INPUTS

- REQUIREMENTS.md
- ACCEPTANCE_CRITERIA.md
- TRACEABILITY_MATRIX.md
- DESIGN.md
- BUILD_HANDOFF.json
- Source Code
- Existing Tests
- Build Evidence


## RULES

- 실행하지 않은 Test를 PASS 처리하지 않는다.
- 실패 Test를 삭제하거나 약화하지 않는다.
- Acceptance Criteria를 Test 편의를 위해 변경하지 않는다.
- Defect를 숨기지 않는다.


## PROCEDURE

### 1. Test Scope

Critical Requirement와 AC를 확인한다.

### 2. Test Plan

검증전략을 작성한다.

### 3. Test Case

Requirement와 Test Case를 연결한다.

### 4. Unit Test Evidence

기존 Unit Test 실행 결과를 검토한다.

### 5. Integration Test

필요한 통합 테스트를 수행한다.

### 6. Contract Test

API/Event Contract를 검증한다.

### 7. E2E Test

주요 사용자 Flow를 검증한다.

### 8. Negative Test

잘못된 입력과 실패상황을 검증한다.

### 9. Multilingual (i18n) Verification

한국어(`ko`) 및 영어(`en`) 로케일 환경에서 다음을 검증한다:
- 언어 전환 및 다국어 텍스트/메시지 정상 표시
- 한글 유니코드 정규화(NFC/NFD) 및 특수문자 입출력 무결성
- 다국어 전환 시 UI 텍스트 오버플로우/말줄임 및 레이아웃 유지

### 10. Security Review

@security 관점의 검증을 수행한다.

### 11. Regression

기존 기능 영향 여부를 검증한다.

### 12. Coverage

Requirement → AC → Test Case → Result를 연결한다.

### 13. Defect

미해결 문제를 기록한다.


## REQUIRED OUTPUTS

docs/04-test/TEST_PLAN.md

docs/04-test/TEST_CASES.md

docs/04-test/TEST_REPORT.md

docs/04-test/SECURITY_REPORT.md

docs/04-test/VERIFY_HANDOFF.json


## ARTIFACT TEMPLATES

다음 Template을 기반으로 실제 Artifact를 docs/04-test/에 생성한다.

- .agents/templates/artifacts/04-test/TEST_PLAN.template.md → docs/04-test/TEST_PLAN.md
- .agents/templates/artifacts/04-test/TEST_CASES.template.md → docs/04-test/TEST_CASES.md
- .agents/templates/artifacts/04-test/TEST_REPORT.template.md → docs/04-test/TEST_REPORT.md
- .agents/templates/artifacts/04-test/SECURITY_REPORT.template.md → docs/04-test/SECURITY_REPORT.md
- .agents/templates/artifacts/04-test/VERIFY_HANDOFF.template.json → docs/04-test/VERIFY_HANDOFF.json

템플릿 사용 규칙:
1. Template 자체를 수정하지 않는다.
2. Template 구조와 Frontmatter를 유지하며 Placeholder를 실제 값으로 대체한다.
3. 해당하지 않는 Section은 삭제하지 말고 N/A 또는 NONE으로 명시한다.
4. 신규 Artifact의 초기 status는 DRAFT로 작성한다.


## RESULT CLASSIFICATION

각 검증항목은 다음 중 하나로 기록한다.

PASS
FAIL
SKIPPED
NOT_EXECUTED
BLOCKED


## VALIDATION

Release Candidate 조건:

- Critical AC PASS
- CI PASS
- Critical Security Finding 없음
- High Risk 처리상태 확인
- Blocking Defect 없음


## HUMAN APPROVAL

G4 — Release Candidate Approval

다음을 출력하고 STOP한다.

G4 RELEASE CANDIDATE APPROVAL REQUIRED


## STOP CONDITIONS

- Critical Test FAIL
- Critical Security Finding
- 테스트 환경 부재
- Requirement Coverage 부족
- Release Blocking Defect
- G4 승인 대기


## HANDOFF

G4 승인 후 RELEASE Stage 입력:

- APPROVED VERIFY_HANDOFF.json
- TEST_REPORT.md
- SECURITY_REPORT.md
- Release Candidate