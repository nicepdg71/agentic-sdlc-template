# Agentic SDLC Project Handover & Conversation History

이 문서는 다른 PC 또는 다른 개발 환경에서 프로젝트 작업을 원활하게 이어갈 수 있도록, 지금까지 진행된 모든 설정, 프레임워크 업그레이드(v1.0 -> v1.1), 거버넌스 규칙, 검증 결과 및 후속 작업 가이드를 상세히 기록한 인수인계 문서입니다.

---

## 1. 프로젝트 및 환경 기본 정보

* **프로젝트 명**: `agentic-sdlc-template`
* **프레임워크 버전**: `v1.1.0` (Governance-first Agentic SDLC)
* **원격 저장소(GitHub)**: `https://github.com/nicepdg71/agentic-sdlc-template.git`
* **기본 브랜치**: `main`
* **로컬 기본 경로**: `F:\repository\agentic-sdlc-template`

---

## 2. 작업 이력 요약 (Chronological History)

### Phase 1: 로컬 리포지토리 초기화 및 원격 동기화
1. **로컬 디렉토리 생성 및 Git 초기화**:
   - `agentic-sdlc-template` 폴더 생성 및 `git init` 수행.
   - 원격 저장소(`origin`)를 `https://github.com/nicepdg71/agentic-sdlc-template.git`로 등록.
2. **GitHub MCP 환경 설정 및 보안 조치**:
   - [`.agents/mcp_config.json`](file:///F:/repository/agentic-sdlc-template/.agents/mcp_config.json) 생성 및 GitHub PAT 토큰 구성.
   - PAT 토큰 및 환경설정 파일의 원격 노출을 방지하기 위해 [`.gitignore`](file:///F:/repository/agentic-sdlc-template/.gitignore)에 `.agents/mcp_config.json`, `.env` 등을 추가.
3. **원격 코드베이스 동기화**:
   - GitHub PAT 인증을 통해 원격 `main` 브랜치를 로컬로 성공적으로 fetch 및 checkout 완료.

---

### Phase 2: SDLC 표준화 프레임워크 v1.0 -> v1.1 구조적 업그레이드
첨부된 **[agentic-sdlc-template v1.1 설계]** 명세서에 따라 다음 핵심 기능들을 구현 및 표준화했습니다.

#### A. 순환형 Change Cycle 표준화 (T-11)
* **SDLC 순환 구조 확립**:
  - 기존 일회성 선형 구조에서 변경 발생 시 영향받는 단계부터 재진입하는 순환형 모델로 확장:
    $$\text{DEFINE} \rightarrow \text{SPEC} \rightarrow \text{DESIGN} \rightarrow \text{BUILD} \rightarrow \text{VERIFY} \rightarrow \text{RELEASE} \rightarrow \text{CHANGE} \rightarrow \text{Earliest Impacted Stage Re-entry}$$
* **Earliest Impacted Stage Re-entry 원칙**:
  - 모든 변경을 무조건 처음(DEFINE)부터 다시 하지 않고, 영향이 최초 발생하는 Stage부터 재진입:
    - Scope/사업목표 변경: `DEFINE` (G0 ~ G5 재승인)
    - 요구사항 추가/변경: `SPEC` (G1 ~ G5 재승인, G0 유지)
    - Architecture / UI / API / DB 변경: `DESIGN` (G2 ~ G5 재승인)
    - 구현 / 코드 / 버그 수정: `BUILD PLAN` (G3 ~ G5 재승인)
    - 테스트 / 증적 변경: `VERIFY` (G4 ~ G5 재승인)
    - 배포 설정 / 릴리스 계획: `RELEASE` (G5 재승인)
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
* **UI Applicability Assessment**: DESIGN Stage 시작 시 UI 필요성 평가 (`NOT_REQUIRED` / `RECOMMENDED` / `REQUIRED`).
* **Human UI Decision**: Agent가 임의 결정하지 않고 `UI DESIGN DECISION REQUIRED` 메시지로 사용자에게 선택권 제시 (`USE_STITCH`, `SKIP_STITCH`, `USE_OTHER_UI_TOOL`).
* **신규 스킬 추가 (총 14개 -> 15개)**:
  - [`.agents/skills/stitch-design-integration/SKILL.md`](file:///F:/repository/agentic-sdlc-template/.agents/skills/stitch-design-integration/SKILL.md)
  - [`.agents/skills/ui-design-handoff/SKILL.md`](file:///F:/repository/agentic-sdlc-template/.agents/skills/ui-design-handoff/SKILL.md) 3-phase 구조로 개편

---

### Phase 3: Stitch MCP 연동 가이드 및 이원화 모드(Dual Modes) 보완
`USE_STITCH` 선택 시 Stitch MCP 미설정 환경에서도 안전하고 유연하게 대처할 수 있도록 방법론을 보완했습니다:

1. **이원화 동작 모드 확립**:
   * **Mode 1: Live MCP Mode (실시간 자동 연동)**:
     - `.agents/mcp_config.json`에 `stitch` MCP 서버가 정상 설정되어 통신 가능한 경우, 화면 구조, 디자인 토큰, 컴포넌트 메타데이터를 실시간 조회·동기화하여 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json` 생성.
   * **Mode 2: Fallback Prompt Mode (프롬프트 생성 및 Web UI 연계)**:
     - Stitch MCP 서버가 미등록/미연결 상태인 경우, `STITCH MCP SETUP REQUIRED` 메시지와 설정 가이드(Remote HTTP / Local npx / 전역 설정)를 출력.
     - 동시에 [`.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md`](file:///F:/repository/agentic-sdlc-template/.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md)를 기반으로 `docs/02-design/ui/STITCH_PROMPTS.md`를 자동 생성하여 Google Stitch Web Console과 수동 연계 지원.
2. **Fail-Closed 안전 원칙 유지**:
   - MCP 미연결 시 임의로 UI 설계를 생략하지 않으며, Fallback 프롬프트를 통해 완성된 UI 산출물(`UI_DESIGN_HANDOFF.md`)이 준비되어야 G2 승인 완료 가능.
3. **Stitch MCP 설정 템플릿 제공**:
   - [`.agents/mcp_config.example.json`](file:///F:/repository/agentic-sdlc-template/.agents/mcp_config.example.json) 추가.

---

## 3. 검증 결과 (Validation)

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
      "args": ["-y", "@modelcontextprotocol/server-github"],
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
* **신규 프로젝트 시작 시**: `/define-project` -> G0 검토 후 `APPROVE G0` 입력
* **디자인 단계 진입 시**: `/design-system` -> UI 필요 시 `USE_STITCH` 선택 (Live MCP 또는 Fallback 프롬프트 활용)
* **운영 중 변경 요청 시**: `/request-change` -> `APPROVE CR-XXXX` -> Re-entry

---

## 5. 프로젝트 주요 디렉토리 구조 맵

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
