[최초 시작 프롬프트]
현재 Repository는 신규 SW 프로젝트를 위한
표준 Agentic SDLC Template으로 생성되었다.

아직 프로젝트 정의 작업을 수행하지 말라.
파일도 수정하지 말라.

먼저 Repository 전체 구조를 확인하라.

특히 다음을 확인한다.

1. project.yaml

2. .agents/agents.md

3. .agents/rules/

4. .agents/workflows/

5. .agents/prompts/

6. .agents/skills/

7. docs/
   - readyForStart.md
   - 00-project-definition
   - 01-analysis
   - 02-design
   - 03-implementation
   - 04-test
   - 05-release
   - approvals

8. contracts/

9. tests/

10. infra/

11. .github/workflows/

다음 형식으로만 결과를 보고하라.

# Agentic SDLC Template Validation

Repository:
Project ID:
Project Name:

## Required Structure

각 필수 항목에 대해:

PASS
MISSING
WARNING

중 하나로 표시한다.

## Rules

발견된 Rule 파일 목록

## Workflows

발견된 Workflow 파일 목록

## Skills

발견된 Skill 목록

## Prompts

발견된 Stage Prompt 목록

## Problems

누락되거나 구조가 잘못된 항목

## Result

READY
또는
NOT READY

중 하나를 표시한다.

파일을 생성하거나 수정하지 말라.
프로젝트 요구사항 분석을 시작하지 말라.
