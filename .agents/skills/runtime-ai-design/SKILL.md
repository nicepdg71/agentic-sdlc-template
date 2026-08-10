---
name: runtime-ai-design
description: Design runtime AI features including use cases, prompts, structured outputs, model contracts, safety constraints, evaluation cases, fallback behavior, and hallucination risk controls.
---

# Purpose

애플리케이션에 포함되는 Runtime AI 기능을
검증 가능하고 안전하게 설계한다.

# Applicable Stages

SPEC
DESIGN
BUILD
VERIFY

# Primary Agent

@ai

# Activation

runtime_ai.enabled = true인 경우 사용한다.

# Inputs

- AI 관련 Requirement
- User Story
- Acceptance Criteria
- Data Policy
- Security Requirement

# Procedure

1. AI가 해야 할 일과 하지 말아야 할 일을 정의한다.
2. Model Input을 정의한다.
3. Model Output을 정의한다.
4. Structured Output 필요성을 정의한다.
5. Prompt 역할을 정의한다.
6. 사실성 요구를 정의한다.
7. Hallucination 위험을 분석한다.
8. 사람 확인이 필요한 결과를 정의한다.
9. Fallback 동작을 설계한다.
10. Evaluation Case를 작성한다.
11. 실패/거부/Timeout 처리를 정의한다.
12. Runtime Secret가 Client에 노출되지 않는지 검토한다.

# Checklist

- [ ] AI의 권한범위가 정의됨
- [ ] Output Contract 존재
- [ ] Evaluation Case 존재
- [ ] Failure/Fallback 존재
- [ ] Human Review 필요조건 존재
- [ ] Secret 노출 없음

# Blockers

- AI가 위험한 최종결정을 자동 수행해야 함
- Output을 검증할 수 없음
- 개인정보 사용 근거 불명확
- Secret Exposure 위험

# Output

- AI Use Case
- Prompt Contract
- Structured Output Schema
- Evaluation Cases
- Safety Constraints

# Traceability

AI Requirement
→ Prompt/Contract
→ Evaluation Case

# Handoff

SPEC/DESIGN/BUILD/VERIFY Stage에 반환한다.
