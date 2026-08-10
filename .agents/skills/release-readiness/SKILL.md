---
name: release-readiness
description: Evaluate whether an approved release candidate is operationally ready for production by checking CI, tests, security, environment, secrets, migrations, rollback, smoke tests, monitoring, and release metadata.
---

# Purpose

Release Candidate가 Production 배포 준비상태인지
체계적으로 검증한다.

# Applicable Stages

RELEASE

# Primary Agent

@devops

# Inputs

- VERIFY_HANDOFF
- Test Report
- Security Report
- Release Candidate
- CI Result
- Deployment Configuration

# Procedure

1. Release Commit/Version을 고정한다.
2. Required CI 상태를 확인한다.
3. Test 결과를 확인한다.
4. Security Blocking Issue를 확인한다.
5. Target Environment를 확인한다.
6. Secret 존재 여부를 확인한다.
7. Migration 여부를 확인한다.
8. Backup 필요성을 확인한다.
9. Rollback Plan을 검토한다.
10. Smoke Test를 정의한다.
11. Monitoring/Alert를 정의한다.
12. Release Notes를 검토한다.
13. Release Checklist를 작성한다.

# Checklist

- [ ] CI PASS
- [ ] Critical Test PASS
- [ ] Critical Security Issue 없음
- [ ] Environment 준비
- [ ] Secret 준비
- [ ] Migration 검토
- [ ] Rollback 존재
- [ ] Smoke Test 존재
- [ ] Monitoring 존재

# Blockers

- CI FAIL
- Critical Security Finding
- Production Secret 미설정
- Migration Risk 미해결
- Rollback 불가능성 미승인
- Release Version 불일치

# Output

- Release Readiness Result
- Release Checklist
- Blocker
- Residual Risk

# Traceability

Release Candidate
→ Test/Security Evidence
→ Release Decision

# Handoff

G5 검토자료로 반환한다.