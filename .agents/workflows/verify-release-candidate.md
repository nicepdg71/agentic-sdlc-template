# Workflow: Verify Release Candidate

1. Execute automated test suites according to `TEST_PLAN.md`.
2. Verify each acceptance criterion in `TEST_CASES.md`.
3. Run security and vulnerability scans (`SECURITY_REPORT.md`).
4. Aggregate results in `TEST_REPORT.md`.
5. Generate `VERIFY_HANDOFF.json`.