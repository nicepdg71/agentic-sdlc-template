# Rule 04: Security, Credentials & Secrets Protection

## 1. Objective
Enforce a zero-tolerance policy against credential leakage, insecure coding practices, and vulnerabilities across all repository artifacts and automated agent workflows.

## 2. Core Policies

### 2.1 Absolute Prohibition of Hardcoded Secrets
- **No Hardcoded Secrets**: Under no circumstances should API keys, access tokens, passwords, private keys, database connection strings with credentials, or encryption certificates be committed to the repository.
- **Environment Variable Abstraction**: All sensitive configurations must be injected via runtime environment variables.
- **Template Maintenance**: Only dummy / placeholder keys are permitted in `.env.example`.

### 2.2 Git Hygiene & `.gitignore` Enforcement
- Environment files (`.env`, `.env.local`, `.env.*.local`), credential stores, and scratch directories must remain strictly ignored by `.gitignore`.

### 2.3 Secure Coding Standards
- All code must adhere to OWASP Top 10 security standards:
  - Robust input sanitization and parameterized queries (SQLi prevention).
  - Proper output encoding (XSS prevention).
  - Secure authentication & token handling (stateless JWT validation, HTTPS-only cookies).
  - Principle of Least Privilege for API permissions and database roles.

### 2.4 Security Auditing & Gating
- Automated secret scanning and dependency vulnerability analysis must be executed during Phase `04-test` and documented in `docs/04-test/SECURITY_REPORT.md`.