# GitHub Repository Settings

Agentic SDLC Project를 생성한 후
다음 GitHub 설정을 구성한다.


# 1. Default Branch

main


# 2. Main Branch Protection / Ruleset

Target:

main

Recommended Rules:

- Require a pull request before merging
- Require at least 1 approval
- Require status checks before merging
- Required check: ci-gate
- Require conversation resolution
- Block force pushes
- Block branch deletion
- Require Code Owner review when CODEOWNERS is configured
- Do not allow bypass where organizational policy permits


# 3. Actions Permissions

Recommended:

Restricted / least privilege

Workflow에서 필요한 permission만 명시적으로 부여한다.


# 4. Actions Security

Third-party actions는 최소화한다.

사용하는 Action은 가능한 경우
verified full-length commit SHA로 고정한다.


# 5. Staging Environment

Environment:

staging

Deployment:

optional

Repository Variable:

STAGING_DEPLOY_ENABLED=false

프로젝트 Deployment Target이 구성된 이후
true로 변경한다.


# 6. Production Environment

Environment:

production

Recommended:

- Required reviewers when supported
- Prevent self-review when supported
- Restrict deployment branches/tags
- Do not allow protection bypass where supported


# 7. Production Secrets

Production Secret은
Repository Source Code에 저장하지 않는다.

가능하면 Production Environment에 저장한다.


# 8. CODEOWNERS

실제 프로젝트 Team/User로
.github/CODEOWNERS를 설정한다.

최소 검토 대상:

- .agents/
- .github/
- docs/approvals/
- infra/
- contracts/


# 9. Merge Policy

main에 직접 기능 Push하지 않는다.

Working Branch
→ Pull Request
→ ci-gate
→ Human Review
→ Merge

방식을 사용한다.


# 10. Production Policy

main Merge는
Production Release 승인을 의미하지 않는다.

Production에는
G5에서 승인된 exact commit SHA만 배포한다.
