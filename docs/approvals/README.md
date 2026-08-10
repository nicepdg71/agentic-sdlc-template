# Human Approval Records

이 디렉터리는 Agentic SDLC의
Human Approval Evidence를 저장한다.

## Standard Gate Files

G0:
G0-project-definition.review.md
G0-project-definition.approval.json

G1:
G1-requirement-baseline.review.md
G1-requirement-baseline.approval.json

G2:
G2-design-baseline.review.md
G2-design-baseline.approval.json

G3:
G3-implementation-plan.review.md
G3-implementation-plan.approval.json

G4:
G4-release-candidate.review.md
G4-release-candidate.approval.json

G5:
G5-production-release.review.md
G5-production-release.approval.json

## Principle

Approval은 대화에만 존재해서는 안 된다.

승인 대상 Artifact의 정확한 Version을 기록한다.

승인된 Artifact가 변경되면
기존 Approval은 새 Version에 적용되지 않는다.

Human Approval은 다음 Workflow를 자동 실행하지 않는다.
