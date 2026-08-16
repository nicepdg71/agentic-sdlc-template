# Agentic SDLC Project Handover & Conversation History

이 문서는 다른 PC 또는 다른 개발 환경에서 프로젝트 작업을 즉시 이어서 진행할 수 있도록, 지금까지 진행된 모든 설정, 프레임워크 업그레이드(v1.0 -> v1.1.0), 거버넌스 규칙, 세부 워크플로우, 검증 결과 및 인수인계 절차를 상세히 기록한 마스터 인수인계 문서입니다.

---

## 1. 프로젝트 및 환경 기본 정보

* **프로젝트 명**: `agentic-sdlc-template`
* **프레임워크 버전**: `v1.1.0` (Governance-first Agentic SDLC)
* **원격 저장소 (GitHub)**: `https://github.com/nicepdg71/agentic-sdlc-template.git`
* **기본 브랜치**: `main`
* **로컬 기본 경로**: `F:\repository\agentic-sdlc-template`
* **DryRun 테스트 경로**: `F:\repository\agentic-sdlc-template_dryrun`

---

## 2. 작업 이력 및 보완 상세 (Full Chronological Summary)

### Phase 1: 로컬 리포지토리 초기화 및 원격 동기화
1. **로컬 디렉토리 생성 및 Git 초기화**:
   - `agentic-sdlc-template` 폴더 생성 및 `git init` 수행.
   - 원격 저장소(`origin`)를 `https://github.com/nicepdg71/agentic-sdlc-template.git`로 등록.
2. **GitHub PAT 인증 및 MCP 환경 설정**:
   - [`.agents/mcp_config.json`](file:///F:/repository/agentic-sdlc-template/.agents/mcp_config.json) 생성 및 GitHub PAT 토큰 구성.
   - PAT 토큰 및 환경설정 파일의 원격 노출을 방지하기 위해 [`.gitignore`](file:///F:/repository/agentic-sdlc-template/.gitignore)에 `.agents/mcp_config.json`, `.env` 등을 추가.
3. **원격 코드베이스 동기화**:
   - GitHub PAT 인증을 통해 원격 `main` 브랜치를 로컬로 성공적으로 fetch 및 checkout 완료.

---

### Phase 2: SDLC 표준화 프레임워크 v1.0 -> v1.1.0 구조적 업그레이드
제공된 **[agentic-sdlc-template v1.1 설계]** 명세서에 따라 다음 핵심 거버넌스 구조를 표준화했습니다.

#### A. 순환형 Change Cycle 표준화 (T-11)
* **SDLC 순환 구조 확립**:
  - 기존 일회성 선형 구조에서 변경 발생 시 영향받는 단계부터 재진입하는 순환형 모델로 확장:
    $$\text{DEFINE} \rightarrow \text{SPEC} \rightarrow \text{DESIGN} \rightarrow \text{BUILD} \rightarrow \text{VERIFY} \rightarrow \text{RELEASE} \rightarrow \text{CHANGE} \rightarrow \text{Earliest Impacted Stage Re-entry}$$
* **Earliest Impacted Stage Re-entry 원칙**:
  - 모든 변경을 무조건 처음(DEFINE)부터 다시 하지 않고, 영향이 최초 발생하는 Stage부터 재진입:
    | 변경 내용 | Re-entry Stage | 재승인 필요 Gate |
    |---|---|---|
    | 사업목표 / Project Scope 변경 | `DEFINE` | G0 $\rightarrow$ G5 |
    | 요구사항(FR/NFR) 추가 / 변경 | `SPEC` | G1 $\rightarrow$ G5 (G0 유지) |
    | Architecture / UI / API / DB 설계 변경 | `DESIGN` | G2 $\rightarrow$ G5 |
    | 구현 방법 / 코드 / 버그 수정 | `BUILD PLAN` | G3 $\rightarrow$ G5 |
    | 테스트 계획 / 테스트 증적 변경 | `VERIFY` | G4 $\rightarrow$ G5 |
    | 배포 설정 / 릴리스 계획 변경 | `RELEASE` | G5 |
* **공식 워크플로우 3종 추가 (총 9개 -> 12개)**:
  1. [`/request-change`](file:///F:/repository/agentic-sdlc-template/.agents/workflows/request-change.md): CR 생성 (`CR-XXXX`), `CHANGE_REQUEST.md`, `IMPACT_ANALYSIS.md`, `CHANGE_TRACEABILITY.md` 생성
  2. [`/record-change-decision`](file:///F:/repository/agentic-sdlc-template/.agents/workflows/record-change-decision.md): 사람의 승인(`APPROVE CR-XXXX` / `REJECT CR-XXXX`), 하위 산출물 `STALE` 처리, 자동 실행 없이 대기
  3. [`/close-change-cycle`](file:///F:/repository/agentic-sdlc-template/.agents/workflows/close-change-cycle.md): 릴리스 후 필수 Gate 및 추적성 검증 후 CR을 `CLOSED`로 종료
* **신규 스킬 추가 (총 13개 -> 14개)**:
  - [`.agents/skills/change-impact-analysis/SKILL.md`](file:///F:/repository/agentic-sdlc-template/.agents/skills/change-impact-analysis/SKILL.md)
* **Cycle별 승인 아카이빙 구조**:
  - `docs/approvals/{CYCLE_ID}/` (예: `INIT-001/`, `CR-0001/`) 폴더별로 Gate 승인 이력을 격리 보존하여 과거 이력 보존.
* **산출물 상태 및 메타데이터 확장**:
  - 상태: `DRAFT`, `IN_REVIEW`, `APPROVED`, `STALE`, `SUPERSEDED`
  - 메타데이터: `cycle_id` (`INIT-001` 또는 `CR-0001`), `change_id` (null 또는 `CR-0001`)

#### B. DESIGN 단계 UI 자동 진단 & Google Stitch MCP 연동 (T-12)
* **`project.yaml` 정책 반영**: `toolchain.ui_design.policy: suggest_when_applicable`
* **UI Applicability Assessment**: DESIGN Stage 시작 시 화면, 데이터 입력, 대시보드 등의 필요성을 Agent가 평가 (`NOT_REQUIRED` / `RECOMMENDED` / `REQUIRED`).
* **Human UI Decision**: Agent가 임의 결정하지 않고 `UI DESIGN DECISION REQUIRED` 메시지로 사용자에게 선택권 제시 (`USE_STITCH`, `SKIP_STITCH`, `USE_OTHER_UI_TOOL`).
* **신규 스킬 추가 (총 14개 -> 15개)**:
  - [`.agents/skills/stitch-design-integration/SKILL.md`](file:///F:/repository/agentic-sdlc-template/.agents/skills/stitch-design-integration/SKILL.md)
  - [`.agents/skills/ui-design-handoff/SKILL.md`](file:///F:/repository/agentic-sdlc-template/.agents/skills/ui-design-handoff/SKILL.md) 3-phase 구조로 개편
* **UI 전용 Artifacts & 템플릿**:
  - `UI_DESIGN_BRIEF.template.md`, `UI_DESIGN_HANDOFF.template.md`, `STITCH_PROJECT_REF.template.json`
  - `UI_VERIFICATION_REPORT.template.md` (VERIFY 단계에서 Stitch 디자인과 실제 구현 화면 비교 검증)
* **SSOT 우선순위**:
  - `Requirements -> UI Design Handoff -> Stitch Project Reference -> Implementation` (충돌 시 `DESIGN CONFLICT DETECTED` 보고)

---

### Phase 3: DryRun 검증 및 인터랙티브 프로세스 문서화
1. **DryRun 환경 복제**:
   - `F:\repository\agentic-sdlc-template`의 전체 내용을 [`F:\repository\agentic-sdlc-template_dryrun`](file:///F:/repository/agentic-sdlc-template_dryrun)으로 복제하여 독립된 모의 실행 환경 구성.
2. **프로세스 다이어그램 문서화**:
   - [`docs/agentic_sdlc_process_diagrams.html`](file:///F:/repository/agentic-sdlc-template/docs/agentic_sdlc_process_diagrams.html) 생성 (HTML/CSS 기반 시각화 프로세스 가이드).

---

### Phase 4: Stitch MCP 연동 가이드 및 이원화 모드(Dual Modes) 보완
`USE_STITCH` 선택 시 Stitch MCP 미설정 환경에서도 안전하고 유연하게 대처할 수 있도록 방법론을 보완했습니다:

1. **이원화 동작 모드 확립**:
   * **Mode 1: Live MCP Mode (실시간 자동 연동)**:
     - `.agents/mcp_config.json`에 `stitch` MCP 서버가 정상 설정되어 통신 가능한 경우, 화면 구조, 디자인 토큰, 컴포넌트 메타데이터를 실시간 조회·동기화하여 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json` 생성.
   * **Mode 2: Fallback Prompt Mode (프롬프트 생성 및 Web UI 연계)**:
     - Stitch MCP 서버가 미등록/미연결 상태인 경우, `STITCH MCP SETUP REQUIRED` 메시지와 설정 가이드(Remote HTTP / Local npx / 전역 설정)를 출력.
     - 동시에 [`.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md`](file:///F:/repository/agentic-sdlc-template/.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md)를 기반으로 `docs/02-design/ui/STITCH_PROMPTS.md`를 자동 생성하여 Google Stitch Web Console과 수동 연계 지원.
2. **Fail-Closed 안전 원칙 유지**:
   - MCP 미연결 시 임의로 UI 설계를 생략하지 않으며, Fallback 프롬프트를 통해 완성된 UI 산출물(`UI_DESIGN_HANDOFF.md`)이 준비되어야 G2 승인을 완료할 수 있도록 통제.
3. **Stitch MCP 설정 템플릿 제공**:
   - [`.agents/mcp_config.example.json`](file:///F:/repository/agentic-sdlc-template/.agents/mcp_config.example.json) 추가.

### Phase 5: Google Stitch MCP & UI Handoff 연동 고도화 (Main/Sub 화면, 워크플로우 전달 및 인간 수정 게이트)
Stitch UI 연동을 단순 화면 조회를 넘어, 엔드투엔드 사용자 흐름과 인간 디자이너/엔지니어의 직접 검토·수정을 보장하는 4-Phase 생명주기로 고도화했습니다:

1. **Main 화면 & Sub 화면(모달/드로어/상세) 및 Screen Workflow 구체화**:
   - `UI_DESIGN_BRIEF.template.md`, `UI_DESIGN_HANDOFF.template.md`에 Main Screens와 Sub Screens 계층을 분리 정의.
   - 화면 간 전이 트리거 이벤트, 파라미터 전달, 복귀/뒤로가기 흐름, Mermaid 플로우차트를 필수 명세화.
2. **Stitch MCP 전달 시 화면 목록 및 워크플로우 동시 반영**:
   - Live MCP 호출 및 `STITCH_PROMPTS.template.md`에 Main/Sub 화면 사양뿐 아니라 화면 간 연결 및 상호작용 지시문을 함께 패키징하여 Stitch가 화면 흐름까지 인지하여 생성하도록 구성.
3. **Stitch 자동 생성 후 인간 수정 대기 블로킹 게이트 (Human-in-the-Loop)**:
   - Stitch 자동 생성이 완료된 후 에이전트가 임의로 다음 단계(G2 또는 BUILD)로 진행하지 않고 즉시 정지하는 `STITCH UI DESIGN REVIEW & REFINEMENT REQUIRED` 게이트 신설 (`Rule 01` 반영).
   - 사람이 Stitch 콘솔에서 레이아웃, 토큰, 컴포넌트, 화면 흐름을 직접 검토하고 보정할 수 있도록 보장.
4. **완료 확인(`CONFIRM_STITCH_DESIGN_COMPLETED`) 및 Handoff 최종 동기화**:
   - 사람이 `CONFIRM_STITCH_DESIGN_COMPLETED` 명령을 입력하면 Stitch의 최종 결과물을 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json`에 동기화하고 G2 승인 심사 패키지로 안전하게 전환.
5. **시각화 다이어그램 갱신**:
   - `docs/agentic_sdlc_process_diagrams.html`에 Google Stitch MCP & UI Handoff 연동 생명주기 다이어그램 카드 추가.

### Phase 6: 한국어 및 영어 다국어(i18n & l10n) 시스템 표준화
UI 프론트엔드부터 백엔드 API, 데이터 모델, 런타임 AI 및 테스트 검증까지 시스템 전 계층에 걸쳐 한국어(`ko`)와 영어(`en`)를 일관되게 지원하도록 Agentic SDLC 표준을 구축했습니다:

1. **프로젝트 메타데이터 및 거버넌스 룰**:
   - `project.yaml`에 `i18n` 표준 블록(`default_locale: "ko"`, `supported_locales: ["ko", "en"]`, `charset: "UTF-8"`, `timezone: "UTC"`) 명세.
   - `Rule 02` (i18n SSOT 및 하드코딩 금지), `Rule 06` (데이터베이스 `utf8mb4` 및 다국어 모델링), `Rule 07` (다국어 테스트 증적 의무화) 반영.
2. **UI & Stitch 연동 템플릿**:
   - `UI_DESIGN_BRIEF.template.md`, `UI_DESIGN_HANDOFF.template.md`, `STITCH_PROMPTS.template.md`에 언어 전환기(Language Switcher) 컴포넌트, CJK/Latin 폰트 타이포그래피 토큰, 한-영 텍스트 가변성(1.3~1.5배) 수용 레이아웃 가이드라인 추가.
3. **아키텍처 및 API 인터페이스**:
   - `ARCHITECTURE.template.md`에 로케일 협상 미들웨어(`Accept-Language` 헤더 해석), 다국어 에러 디스패치 및 메시지 카탈로그 구조 신설.
   - `api-contract-design` 스킬에 다국어 API 응답 및 에러 규격 표준화.
4. **데이터베이스 & 런타임 AI**:
   - `DATA_MODEL.template.md`에 `utf8mb4` 문자셋, 다국어 Collation, UTC 타임스탬프 및 다국어 컬럼/JSONB 저장 전략 추가.
   - `runtime-ai-design` 스킬에 사용자 로케일 일치 응답 계약 명세.
5. **테스트 및 검증**:
   - `TEST_PLAN.template.md`, `TEST_REPORT.template.md`에 한/영 입력 검증, 유니코드 완성형/조합형(NFC/NFD) 정규화, UI 텍스트 오버플로우/말줄임 검증 항목 추가.
6. **무결성 검증 도구**:
   - `validate_agentic_sdlc.py`에 `i18n` 메타데이터 및 구조 무결성 검증 추가.

---

## 3. 거버넌스 및 유효성 검증 (Validation)

통합 유효성 검증 스크립트 실행 결과:
```powershell
python .github/scripts/validate_agentic_sdlc.py
```
```text
=================================================================
 Agentic SDLC v1.1.0 Repository Integrity & Governance Validator
=================================================================

[1/7] Checking required root files and project metadata... [OK]
[2/7] Checking .agents/ governance structure (10 rules, 12 workflows, 15 skills)... [OK]
[3/7] Checking Change Management and UI templates (T-11, T-12)... [OK]
[4/7] Checking JSON syntax and schema validity... [OK] (18 files)
[5/7] Checking for prohibited secret/credential files... [OK] (141 files)
[6/7] Checking docs/ and approvals structure (T-07, T-08, T-11)... [OK]
[7/7] Checking CI/CD scripts and GitHub templates (T-09)... [OK]

=================================================================
[PASSED] ALL AGENTIC SDLC v1.1.0 GOVERNANCE & INTEGRITY CHECKS PASSED!
```

---

## 4. 다른 PC에서 작업을 이어갈 때의 Step-by-Step 가이드

새로운 PC나 환경에서 이 저장소를 작업할 때는 다음 순서로 설정하시면 됩니다.

### Step 1: 저장소 복제 (Clone)
```powershell
git clone https://<YOUR_GITHUB_PAT>@github.com/nicepdg71/agentic-sdlc-template.git
cd agentic-sdlc-template
```

### Step 2: MCP 설정 파일 생성 (`.agents/mcp_config.json`)
보안상 Git에 커밋되지 않은 `.agents/mcp_config.json` 파일을 로컬에 생성합니다 ([`.agents/mcp_config.example.json`](file:///F:/repository/agentic-sdlc-template/.agents/mcp_config.example.json) 참조):
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_GITHUB_PAT_HERE>"
      }
    },
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "<YOUR_GOOGLE_STITCH_API_KEY>"
      }
    }
  }
}
```

### Step 3: 거버넌스 무결성 검증 실행
```powershell
python .github/scripts/validate_agentic_sdlc.py
```

### Step 4: SDLC 프로세스 진행
* **신규 프로젝트 시작 (Initial Cycle)**:
  ```text
  /define-project
  ```
  -> G0 산출물 검토 후 `APPROVE G0` 입력하여 단계별 진행.
* **디자인 단계 진입 시**:
  ```text
  /design-system
  ```
  -> UI 필요 시 `USE_STITCH` 선택 (Live MCP 또는 Fallback 프롬프트 활용) -> `APPROVE G2`.
* **운영 중 변경 요청 (Change Cycle)**:
  ```text
  /request-change
  ```
  -> 영향도 분석 보고서 검토 후 `APPROVE CR-XXXX` 입력하여 Earliest Impacted Stage부터 재진입.
* **배포 완료 후 Change Cycle 공식 종료**:
  ```text
  /close-change-cycle
  ```

---

## 5. 프로젝트 전체 디렉토리 구조 맵

```text
agentic-sdlc-template/
├── .agents/
│   ├── mcp_config.example.json             # MCP 설정 예시 템플릿 (GitHub, Stitch)
│   ├── mcp_config.json                     # 로컬 MCP 설정 (gitignore 대상)
│   ├── agents.md                           # Agent 역할 정의 (@pm, @analyst, @architect, @engineer, @qa, @devops, @ux 등)
│   ├── rules/                              # Rules 00 ~ 09 (핵심 거버넌스 룰)
│   ├── workflows/                          # 12개 공식 SDLC & Change 워크플로우
│   ├── skills/                             # 15개 전문 스킬 (Stitch MCP, Change Impact, Architecture 등)
│   ├── prompts/                            # 00 ~ 05 단계별 프롬프트
│   ├── schemas/                            # 승인 레코드 및 Handoff JSON 스키마
│   └── templates/                          # 산출물, 승인 패키지, 변경관리, UI 템플릿
├── docs/
│   ├── CONVERSATION_HISTORY.md             # [본 문서] 인수인계 및 히스토리
│   ├── agentic_sdlc_process_diagrams.html  # 프로세스 시각화 다이어그램
│   ├── 00-project-definition/ ~ 05-release/ # Phase별 공식 엔지니어링 산출물
│   ├── changes/                            # CHANGE_REGISTER.md 및 CR-XXXX별 산출물
│   └── approvals/                          # INIT-001/, CR-0001/ 등 Cycle별 Gate 승인 보존소
├── contracts/                              # API, Event, AI 스키마 인터페이스 계약
├── src/                                    # 소스 코드
├── tests/                                  # 테스트 스위트 (Unit, Integration, Security, UI)
├── infra/                                  # IaC 및 환경 설정
├── scripts/                                # CI, 배포, 스모크 테스트 스크립트
├── .github/                                # CI/CD 액션, 검증 스크립트, PR/Issue 템플릿
├── project.yaml                            # 프로젝트 거버넌스 & UI 툴체인 메타데이터 (v1.1.0)
└── README.md                               # 프레임워크 공식 매뉴얼
```
