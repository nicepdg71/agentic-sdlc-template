# Agentic SDLC Artifact Templates

본 디렉터리는
Agentic SDLC의 공식 Artifact Template을 관리한다.

## Principle

.agents/templates/artifacts/
파일은 Template이다.

실제 프로젝트 Artifact는
docs/ 아래에 생성한다.

Template 자체를 프로젝트 산출물로 사용하지 않는다.

## Generation Rule

Agent가 Stage Output을 생성할 때:

1. 해당 Artifact Template을 찾는다.
2. Template 구조를 유지한다.
3. Placeholder를 실제 Project 값으로 대체한다.
4. 실제 Artifact를 docs/<stage>/에 생성한다.
5. 불필요한 Section도 임의 삭제하지 않는다.
6. 해당하지 않는 항목은 NONE 또는 N/A로 명시한다.
7. Metadata를 작성한다.
8. 최초 Status는 DRAFT로 한다.

## Approval

Human Approval 전:

DRAFT 또는 IN_REVIEW

Human Approval 후:

APPROVED

새 Version으로 교체된 기존 Artifact:

SUPERSEDED
