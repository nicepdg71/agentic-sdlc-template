---
name: stitch-design-integration
description: Integrate Google Stitch with Antigravity via Model Context Protocol (MCP) in Live MCP Mode or Fallback Prompt Mode to fetch design tokens, layouts, screen structures, and establish UI design handoff baselines.
---

# Purpose

Google Stitch 디자인 도구와 Antigravity Agent를 연동하여,
승인된 요구사항 기반의 UI 디자인 프롬프트를 생성/전달하고,
디자인 컨텍스트(토큰, 레이아웃, 컴포넌트)를 안전하게 가져와 `UI_DESIGN_HANDOFF.md`, `STITCH_PROMPTS.md`, `STITCH_PROJECT_REF.json`으로 구조화한다.

# Applicable Stages

DESIGN, BUILD, VERIFY

# Primary Agent

@ux

# Supporting Agents

- @architect
- @engineer
- @qa

# Inputs

- Approved Requirements & Acceptance Criteria
- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- Stitch MCP Configuration in `.agents/mcp_config.json` (or global MCP config)
- Stitch Project ID / Name / API Key

# Operation Modes

### 1. Mode 1: Live MCP Mode (실시간 MCP 연동)
* **발동 조건**: `.agents/mcp_config.json`에 `stitch` MCP 서버가 정상 설정되어 통신 가능한 경우.
* **실행 흐름**:
  1. `UI_DESIGN_BRIEF.md` 생성.
  2. Stitch MCP 툴을 직접 호출하여 화면 레이아웃, 디자인 토큰(컬러, 폰트, 간격), 컴포넌트 사양을 실시간 조회·동기화.
  3. `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json`에 실시간 컨텍스트 자동 바인딩.

### 2. Mode 2: Fallback Prompt Mode (프롬프트 생성 및 Web UI 연계)
* **발동 조건**: `.agents/mcp_config.json`에 `stitch` MCP 서버가 미등록/미연결 상태인 경우.
* **실행 흐름**:
  1. `STITCH MCP SETUP REQUIRED` 출력 및 연동 설정 가이드(Remote HTTP / Local npx / 전역 설정) 안내.
  2. `.agents/templates/artifacts/02-design/ui/STITCH_PROMPTS.template.md`를 기반으로 `docs/02-design/ui/STITCH_PROMPTS.md` 자동 생성.
  3. 사용자가 Google Stitch Web Console에 해당 프롬프트를 입력하여 생성한 디자인 결과를 기반으로 `UI_DESIGN_HANDOFF.md` 및 `STITCH_PROJECT_REF.json` 초안을 작성/검토.

# Stitch MCP Configuration Guide

### 방법 1: 프로젝트 로컬 `.agents/mcp_config.json`에 등록 (권장)
* **Remote SSE / HTTP 방식**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_GITHUB_PAT>"
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
* **Stdio / Local npx 방식**:
```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@google/stitch-mcp-server"],
      "env": {
        "STITCH_API_KEY": "<YOUR_GOOGLE_STITCH_API_KEY>",
        "STITCH_PROJECT_ID": "<PROJECT_ID>"
      }
    }
  }
}
```

### 방법 2: Antigravity IDE 전역 MCP 설정에 등록
`~/.gemini/antigravity/mcp/` 또는 `~/.gemini/config/mcp_config.json`에 Stitch 서버 스키마 및 환경설정을 구성하여 모든 워크스페이스에서 공통 사용.

# Critical Rules

- **Fail-Closed Principle**: 사용자가 `USE_STITCH`를 선택했으나 MCP 미연결 시 임의로 UI를 생략하거나 코딩으로 직행하지 않으며, Fallback Prompt 모드로 전환하여 반드시 UI Handoff 산출물을 완결해야 G2 승인이 가능하다.
- **Secret Protection**: Stitch API Key나 토큰은 절대 문서나 코드베이스에 직접 커밋하지 않는다.
- **SSOT Hierarchy**: `Approved Requirement -> Approved UI Design Handoff -> Approved Stitch Project Reference -> Implementation`.
- **Conflict Escalation**: `DESIGN.md`와 Stitch UI 디자인 간 불일치 시 `DESIGN CONFLICT DETECTED`를 보고한다.

# Output

- `docs/02-design/ui/UI_DESIGN_BRIEF.md`
- `docs/02-design/ui/STITCH_PROMPTS.md` (Stitch 선택 시)
- `docs/02-design/ui/UI_DESIGN_HANDOFF.md`
- `docs/02-design/ui/STITCH_PROJECT_REF.json`
- `docs/04-test/UI_VERIFICATION_REPORT.md` (검증 단계)
