# DESIGN Stage Prompt

## ROLE

Primary Agent:

@architect

Supporting Agents:

@ux      when UI is enabled
@ai      when Runtime AI is enabled
@security


## STAGE

DESIGN


## OBJECTIVE

승인된 Requirement를 만족하는
구현 가능한 Software Architecture와 상세설계를 작성한다.


## PRECONDITIONS

- G1 APPROVED
- Requirement Baseline APPROVED


## REQUIRED INPUTS

- APPROVED REQUIREMENTS.md
- APPROVED ACCEPTANCE_CRITERIA.md
- TRACEABILITY_MATRIX.md
- ANALYSIS_HANDOFF.json


## OPTIONAL INPUTS

- 기존 Architecture
- Technology Standard
- UI Requirement
- Security Policy
- 운영환경
- Legacy System
- 외부 API 문서
- 비용 제약


## RULES

- 승인된 Requirement만 설계한다.
- 새로운 기능을 설계 과정에서 추가하지 않는다.
- 주요 기술선택에는 근거와 Trade-off를 기록한다.
- 중요한 Architecture 결정은 ADR 후보로 작성한다.
- Security를 사후 검토사항으로 미루지 않는다.


## PROCEDURE

### 1. System Context

사용자와 외부 시스템의 관계를 설계한다.

### 2. Architecture

Component / Service Boundary를 정의한다.

### 3. Data Flow

핵심 데이터 흐름을 정의한다.

### 4. Interface Contract

필요한 경우:

- API (`Accept-Language` 헤더 수용 및 다국어 에러 응답 규격 포함)
- Event
- Message

Contract를 설계한다.

### 5. Data Model

Entity, Relationship, 주요 Constraint를 설계한다:
- `utf8mb4` 문자셋 및 다국어 Collation
- UTC 타임스탬프 필드 표준
- 다국어 저장 패턴 (컬럼 접미사, JSONB 또는 번역 테이블)

### 6. Security

다음을 설계한다.

- Authentication
- Authorization
- Trust Boundary
- Secret Handling
- Data Protection

### 7. Error Handling

대표 Error 코드 및 로케일별(ko/en) 메시지 카탈로그 매핑 방식을 정의한다.

### 8. Internationalization (i18n) & Observability

- 클라이언트 로케일 해석 미들웨어 및 리소스 번들 분리 아키텍처를 정의한다.
- 필요한 Logging, Metric, Trace를 정의한다 (유니코드/UTF-8 로그 보장).

### 9. Deployment Architecture

Local / Dev / Staging / Production을 고려한다.

### 10. UI/UX

UI가 활성화된 경우 @ux를 활용한다.
1. **Main Screens & Sub Screens**: 핵심 1차 화면(대시보드, 메인 목록) 및 2차 화면(상세, 모달, 드로어)을 구체적으로 분할 설계한다.
2. **Screen Workflow & Transition Map**: 화면 간 전이 트리거 이벤트, 파라미터 전달, 복귀/뒤로가기 흐름, Mermaid 플로우차트를 설계한다 (`UI_DESIGN_BRIEF.md`).
3. **Multilingual UI Design**: 한국어(`ko`)/영어(`en`) 지원을 위한 언어 전환기(Language Switcher), CJK/Latin 폰트 타이포그래피 토큰, 한-영 텍스트 길이 가변성(1.3~1.5x)을 수용하는 레이아웃을 설계한다.
4. **Stitch Generation**: Stitch가 설정된 경우 Main/Sub 화면, Screen Workflow 및 다국어 레이아웃 지시문을 MCP 파라미터 또는 `STITCH_PROMPTS.md`로 전달하여 디자인 생성을 요청한다.
5. **Mandatory Human Review Stop**: Stitch 자동 생성이 완료된 후 즉시 멈추고 `STITCH UI DESIGN REVIEW & REFINEMENT REQUIRED`를 출력하여 사람의 검토 및 수정을 기다린다.
6. **Confirmation & Baseline Sync**: 사람이 `CONFIRM_STITCH_DESIGN_COMPLETED`를 입력하면 최종 디자인을 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json`에 동기화한다.

### 11. Runtime AI

runtime_ai.enabled = true일 경우
@ai 관점의 설계를 수행한다.

포함:

- AI Use Case
- Prompt Contract
- Structured Output
- Evaluation
- Fallback
- Safety

### 12. Architecture Decision

중요한 기술결정은 ADR 후보로 기록한다.

### 13. Requirement Coverage

각 주요 Requirement가
어떤 Design Element로 구현되는지 연결한다.


## REQUIRED OUTPUTS

docs/02-design/ARCHITECTURE.md

docs/02-design/DESIGN.md

docs/02-design/DATA_MODEL.md

docs/02-design/SECURITY_DESIGN.md

docs/02-design/adr/

contracts/

docs/02-design/DESIGN_HANDOFF.json


## ARTIFACT TEMPLATES

다음 Template을 기반으로 실제 Artifact를 docs/02-design/에 생성한다.

- .agents/templates/artifacts/02-design/ARCHITECTURE.template.md → docs/02-design/ARCHITECTURE.md
- .agents/templates/artifacts/02-design/DESIGN.template.md → docs/02-design/DESIGN.md
- .agents/templates/artifacts/02-design/DATA_MODEL.template.md → docs/02-design/DATA_MODEL.md
- .agents/templates/artifacts/02-design/SECURITY_DESIGN.template.md → docs/02-design/SECURITY_DESIGN.md
- .agents/templates/artifacts/02-design/ADR.template.md → docs/02-design/adr/ADR-XXXX.md
- .agents/templates/artifacts/02-design/DESIGN_HANDOFF.template.json → docs/02-design/DESIGN_HANDOFF.json

템플릿 사용 규칙:
1. Template 자체를 수정하지 않는다.
2. Template 구조와 Frontmatter를 유지하며 Placeholder를 실제 값으로 대체한다.
3. 해당하지 않는 Section은 삭제하지 말고 N/A 또는 NONE으로 명시한다.
4. 신규 Artifact의 초기 status는 DRAFT로 작성한다.


## VALIDATION

- 모든 Critical Requirement가 설계에 반영되었는가
- Requirement 밖 기능이 포함되지 않았는가
- 주요 Interface가 정의되었는가
- Data Model이 일관적인가
- Security Boundary가 있는가
- Critical Architecture Decision의 근거가 있는가
- 구현 불가능한 부분이 없는가


## HUMAN APPROVAL

G2 — Design Baseline Approval

다음을 출력하고 STOP한다.

G2 DESIGN BASELINE APPROVAL REQUIRED


## STOP CONDITIONS

- G1 미승인
- Critical Requirement에 설계안 없음
- 기술선택에 중요한 미결정사항
- Security Blocker
- Scope 변경 필요
- G2 승인 대기


## HANDOFF

G2 승인 후 BUILD가 사용하는 입력:

- APPROVED DESIGN_HANDOFF.json
- ARCHITECTURE.md
- DESIGN.md
- DATA_MODEL.md
- SECURITY_DESIGN.md
- APPROVED Contract
- 관련 ADR

다음 Stage:

BUILD