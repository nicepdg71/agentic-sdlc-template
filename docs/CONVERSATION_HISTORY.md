# Agentic SDLC Project Handover & Conversation History

이 문서는 다른 PC 또는 다른 개발 환경에서 프로젝트 작업을 원활하게 이어갈 수 있도록, 지금까지 진행된 모든 설정, 프레임워크 업그레이드(v1.0 -> v1.1), 거버넌스 규칙, 검증 결과 및 후속 작업 가이드를 상세히 기록한 인수인계 문서입니다.

---

## 1. 프로젝트 및 환경 기본 정보

* **프로젝트 명**: `agentic-sdlc-template`
* **프레임워크 버전**: `v1.1.0` (Governance-first Agentic SDLC)
* **원격 저장소(GitHub)**: `https://github.com/nicepdg71/agentic-sdlc-template.git`
* **기본 브랜치**: `main`
* **로컬 기본 경로**: `f:\repository\agentic-sdlc-template`

---

## 2. 작업 이력 요약 (Chronological History)

### Phase 1: 로컬 리포지토리 초기화 및 원격 동기화
1. **로컬 디렉토리 생성 및 Git 초기화**:
   - `agentic-sdlc-template` 폴더 생성 및 `git init` 수행.
   - 원격 저장소(`origin`)를 `https://github.com/nicepdg71/agentic-sdlc-template.git`로 등록.
2. **GitHub MCP 환경 설정 및 보안 조치**:
   - [`.agents/mcp_config.json`](file:///f:/repository/agentic-sdlc-template/.agents/mcp_config.json) 생성 및 GitHub PAT 토큰 구성.
   - PAT 토큰 및 환경설정 파일의 원격 노출을 방지하기 위해 [`.gitignore`](file:///f:/repository/agentic-sdlc-template/.gitignore)에 `.agents/mcp_config.json`, `.env` 등을 추가.
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
  1. [`/request-change`](file:///f:/repository/agentic-sdlc-template/.agents/workflows/request-change.md): CR 생성 (`CR-XXXX`), `CHANGE_REQUEST.md`, `IMPACT_ANALYSIS.md`, `CHANGE_TRACEABILITY.md` 생성
  2. [`/record-change-decision`](file:///f:/repository/agentic-sdlc-template/.agents/workflows/record-change-decision.md): 사람의 승인(`APPROVE CR-XXXX` / `REJECT CR-XXXX`), 하위 산출물 `STALE` 처리, 자동 실행 없이 대기
  3. [`/close-change-cycle`](file:///f:/repository/agentic-sdlc-template/.agents/workflows/close-change-cycle.md): 릴리스 후 필수 Gate 및 추적성 검증 후 CR을 `CLOSED`로 종료
* **신규 스킬 추가 (총 13개 -> 14개)**:
  - [`.agents/skills/change-impact-analysis/SKILL.md`](file:///f:/repository/agentic-sdlc-template/.agents/skills/change-impact-analysis/SKILL.md)
* **Cycle별 승인 아카이빙 구조**:
  - `docs/approvals/{CYCLE_ID}/` (예: `INIT-001/`, `CR-0001/`) 폴더별로 Gate 승인 이력을 격리 보존하여 과거 이력 보존.
* **산출물 상태 및 메타데이터 확장**:
  - 상태: `DRAFT`, `IN_REVIEW`, `APPROVED`, `STALE`, `SUPERSEDED`
  - 메타데이터: `cycle_id` (`INIT-001` 또는 `CR-0001`), `change_id` (null 또는 `CR-0001`)

#### B. DESIGN 단계 UI 자동 진단 & Google Stitch MCP 연동 (T-12)
* **`project.yaml` 정책 반영**:
  ```yaml
  toolchain:
    ui_design:
      policy: suggest_when_applicable
      enabled: false
      preferred_tool: stitch
      selected_tool: TBD
      integration: mcp
      stitch_project_ref: ""
  ```
* **UI Applicability Assessment**:
  - [`/design-system`](file:///f:/repository/agentic-sdlc-template/.agents/workflows/design-system.md) 시작 시 화면, 데이터 입력, 대시보드 등의 필요성을 Agent가 평가 (`NOT_REQUIRED` / `RECOMMENDED` / `REQUIRED`).
* **Human UI Decision**:
  - Agent가 임의 결정하지 않고 `UI DESIGN DECISION REQUIRED` 메시지로 사용자에게 선택권 제시 (`USE_STITCH`, `SKIP_STITCH`, `USE_OTHER_UI_TOOL`).
* **Fail-Closed MCP 보안 원칙**:
  - `USE_STITCH` 선택 시 Stitch MCP가 연결되어 있지 않으면 `STITCH INTEGRATION BLOCKED`를 출력하고 G2 승인 완료를 차단.
  - Stitch API Key는 절대 문서나 소스코드에 저장하지 않음.
* **신규 스킬 추가 (총 14개 -> 15개)**:
  - [`.agents/skills/stitch-design-integration/SKILL.md`](file:///f:/repository/agentic-sdlc-template/.agents/skills/stitch-design-integration/SKILL.md)
  - [`.agents/skills/ui-design-handoff/SKILL.md`](file:///f:/repository/agentic-sdlc-template/.agents/skills/ui-design-handoff/SKILL.md) 3-phase 구조로 개편
* **UI 전용 Artifacts & 템플릿**:
  - `UI_DESIGN_BRIEF.template.md`, `UI_DESIGN_HANDOFF.template.md`, `STITCH_PROJECT_REF.template.json`
  - `UI_VERIFICATION_REPORT.template.md` (VERIFY 단계에서 Stitch 디자인과 실제 구현 화면 비교 검증)
* **SSOT 우선순위**:
  - `Requirements -> UI Design Handoff -> Stitch Project Reference -> Implementation` (충돌 시 `DESIGN CONFLICT DETECTED` 보고)

#### C. 거버넌스 룰 & 스키마 업데이트
* [Rules 00 ~ 09](file:///f:/repository/agentic-sdlc-template/.agents/rules/): Earliest Stage Re-entry, STALE 상태, UI SSOT 계층, 승인 비자동 실행 원칙 반영.
* [Schemas](file:///f:/repository/agentic-sdlc-template/.agents/schemas/): `approval-record.schema.json` 및 `stage-handoff.schema.json`에 `cycle_id`, `change_id`, `STALE` 상태 추가.

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
[4/7] Checking JSON syntax and schema validity... [OK] (17 files)
[5/7] Checking for prohibited secret/credential files... [OK] (125 files)
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
보안상 Git에 커밋되지 않은 `.agents/mcp_config.json` 파일을 로컬에 생성합니다:
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
    }
  }
}
```
*(Google Stitch를 사용하는 경우 Stitch MCP 설정 추가 가능)*

### Step 3: 거버넌스 무결성 검증 실행
```powershell
python .github/scripts/validate_agentic_sdlc.py
```

### Step 4: SDLC 프로세스 진행 또는 Dry Run 수행
* **신규 프로젝트 시작 시**:
  ```text
  /define-project
  ```
  -> G0 산출물 검토 후 `APPROVE G0` 입력하여 단계별 진행.
* **운영 중 변경 요청(Change Cycle) 시**:
  ```text
  /request-change
  ```
  -> 영향도 분석 보고서 검토 후 `APPROVE CR-XXXX` 입력하여 Earliest Impacted Stage부터 재진입.
* **배포 완료 후 Change Cycle 공식 종료**:
  ```text
  /close-change-cycle
  ```

---

## 5. 프로젝트 주요 디렉토리 구조 맵

```text
agentic-sdlc-template/
├── .agents/
│   ├── mcp_config.json                     # MCP 서버 설정 (로컬 전용, gitignore)
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
