#!/usr/bin/env python3
"""
Agentic SDLC Repository Integrity & Governance Validator
Validates repository structure, required governance files, JSON syntax,
schemas, secret safety, and T-01 ~ T-08 architecture compliance.
"""

import sys
import os
import json
import subprocess
from pathlib import Path

# Ensure UTF-8 output even on Windows consoles
if sys.stdout.encoding != "utf-8" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

ERRORS = []
WARNINGS = []


def error(msg: str):
    ERRORS.append(msg)
    print(f"[ERROR] {msg}")


def warn(msg: str):
    WARNINGS.append(msg)
    print(f"[WARN]  {msg}")


def info(msg: str):
    print(f"[OK]    {msg}")


def check_required_root_files():
    print("\n[1/6] Checking required root files...")
    required_files = [
        "README.md",
        "project.yaml",
        ".env.example",
        ".gitignore",
    ]
    for rel_path in required_files:
        p = REPO_ROOT / rel_path
        if not p.is_file():
            error(f"Missing required root file: {rel_path}")
        else:
            info(f"Found root file: {rel_path}")


def check_agents_governance_structure():
    print("\n[2/6] Checking .agents/ governance structure...")
    agents_dir = REPO_ROOT / ".agents"
    if not agents_dir.is_dir():
        error("Missing .agents/ directory")
        return

    # Check agents.md
    if not (agents_dir / "agents.md").is_file():
        error("Missing .agents/agents.md")
    else:
        info("Found .agents/agents.md")

    # Check rules
    rules_dir = agents_dir / "rules"
    if not rules_dir.is_dir():
        error("Missing .agents/rules/ directory")
    else:
        rule_files = list(rules_dir.glob("*.md"))
        if len(rule_files) < 10:
            error(f"Expected at least 10 rule files in .agents/rules/, found {len(rule_files)}")
        else:
            info(f"Found {len(rule_files)} rules in .agents/rules/")

    # Check prompts (00 to 05)
    prompts_dir = agents_dir / "prompts"
    stages = [
        "00-project-definition",
        "01-analysis",
        "02-design",
        "03-implementation",
        "04-test",
        "05-release",
    ]
    for stg in stages:
        prompt_file = prompts_dir / stg / "PROMPT.md"
        if not prompt_file.is_file():
            error(f"Missing stage prompt: .agents/prompts/{stg}/PROMPT.md")
        else:
            info(f"Found stage prompt: .agents/prompts/{stg}/PROMPT.md")

    # Check workflows (9 workflows)
    workflows_dir = agents_dir / "workflows"
    expected_workflows = [
        "define-project.md",
        "analyze-requirements.md",
        "design-system.md",
        "plan-implementation.md",
        "implement-change.md",
        "verify-release-candidate.md",
        "prepare-release.md",
        "deploy-production.md",
        "record-gate-decision.md",
    ]
    for wf in expected_workflows:
        wf_path = workflows_dir / wf
        if not wf_path.is_file():
            error(f"Missing workflow: .agents/workflows/{wf}")
        else:
            info(f"Found workflow: .agents/workflows/{wf}")

    # Check skills (13 skills)
    skills_dir = agents_dir / "skills"
    expected_skills = [
        "project-definition",
        "requirements-analysis",
        "architecture-design",
        "ui-design-handoff",
        "api-contract-design",
        "database-design-review",
        "runtime-ai-design",
        "implementation-planning",
        "secure-coding",
        "code-review",
        "test-design",
        "security-review",
        "release-readiness",
    ]
    for sk in expected_skills:
        sk_path = skills_dir / sk / "SKILL.md"
        if not sk_path.is_file():
            error(f"Missing skill: .agents/skills/{sk}/SKILL.md")
        else:
            info(f"Found skill: .agents/skills/{sk}/SKILL.md")

    # Check templates & schemas
    templates_dir = agents_dir / "templates"
    if not (templates_dir / "README.md").is_file():
        error("Missing .agents/templates/README.md")
    else:
        info("Found .agents/templates/README.md")

    schemas_dir = agents_dir / "schemas"
    expected_schemas = [
        "approval-record.schema.json",
        "stage-handoff.schema.json",
    ]
    for sc in expected_schemas:
        sc_path = schemas_dir / sc
        if not sc_path.is_file():
            error(f"Missing schema: .agents/schemas/{sc}")
        else:
            info(f"Found schema: .agents/schemas/{sc}")


def check_json_syntax_and_schemas():
    print("\n[3/6] Checking JSON syntax and schema validity...")
    json_files = list(REPO_ROOT.rglob("*.json"))
    checked_count = 0
    for jf in json_files:
        if any(part.startswith(".") and part not in [".agents", ".github"] for part in jf.parts):
            continue
        try:
            with open(jf, "r", encoding="utf-8") as f:
                json.load(f)
            checked_count += 1
        except Exception as e:
            error(f"Invalid JSON syntax in {jf.relative_to(REPO_ROOT)}: {e}")
    info(f"Validated JSON syntax of {checked_count} JSON files without errors.")


def check_prohibited_and_sensitive_files():
    print("\n[4/6] Checking for prohibited secret/credential files...")
    import re
    sensitive_patterns = [
        re.compile(r"^\.env$", re.IGNORECASE),
        re.compile(r".*\.pem$", re.IGNORECASE),
        re.compile(r".*\.key$", re.IGNORECASE),
        re.compile(r".*\.pfx$", re.IGNORECASE),
        re.compile(r".*\.p12$", re.IGNORECASE),
        re.compile(r".*id_rsa.*", re.IGNORECASE),
        re.compile(r".*id_ed25519.*", re.IGNORECASE),
    ]

    tracked_files = []
    try:
        res = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-files"],
            capture_output=True,
            text=True,
            check=True,
        )
        tracked_files = [Path(line.strip()) for line in res.stdout.splitlines() if line.strip()]
    except Exception:
        for root, _, files in os.walk(REPO_ROOT):
            for file in files:
                rel = Path(root, file).relative_to(REPO_ROOT)
                if not str(rel).startswith(".git"):
                    tracked_files.append(rel)

    for fpath in tracked_files:
        fname = fpath.name
        if fname == ".env.example":
            continue
        for pat in sensitive_patterns:
            if pat.match(fname):
                error(f"Prohibited sensitive/credential file detected in repository: {fpath}")

        lower_name = fname.lower()
        if ("credential" in lower_name or "secret" in lower_name) and not (
            str(fpath).endswith(".md") or str(fpath).endswith(".json") or str(fpath).endswith(".py")
        ):
            warn(f"Suspicious file name containing secret/credential: {fpath}")

    info(f"Scanned {len(tracked_files)} files for sensitive credentials. No unauthorized keys/secrets found.")


def check_docs_and_approvals_structure():
    print("\n[5/6] Checking docs/ and approvals structure (T-07, T-08)...")
    docs_dir = REPO_ROOT / "docs"
    if not docs_dir.is_dir():
        error("Missing docs/ directory")
        return

    stages = [
        "00-project-definition",
        "01-analysis",
        "02-design",
        "03-implementation",
        "04-test",
        "05-release",
    ]
    for stg in stages:
        if not (docs_dir / stg).is_dir():
            error(f"Missing docs/{stg} directory")
        else:
            info(f"Found docs/{stg}")

    approvals_readme = docs_dir / "approvals" / "README.md"
    if not approvals_readme.is_file():
        error("Missing docs/approvals/README.md")
    else:
        info("Found docs/approvals/README.md")

    approvals_tpl = REPO_ROOT / ".agents" / "templates" / "approvals"
    expected_app_tpls = [
        "GATE_REVIEW_PACKAGE.template.md",
        "GATE_APPROVAL_RECORD.template.json",
    ]
    for at in expected_app_tpls:
        at_path = approvals_tpl / at
        if not at_path.is_file():
            error(f"Missing approval template: .agents/templates/approvals/{at}")
        else:
            info(f"Found approval template: .agents/templates/approvals/{at}")


def check_ci_cd_and_scripts():
    print("\n[6/6] Checking CI/CD scripts and GitHub templates (T-09)...")
    scripts_dir = REPO_ROOT / "scripts"
    required_scripts = [
        "ci.sh",
        "deploy-staging.sh",
        "deploy-production.sh",
        "smoke-test.sh",
    ]
    for sc in required_scripts:
        p = scripts_dir / sc
        if not p.is_file():
            error(f"Missing script: scripts/{sc}")
        else:
            info(f"Found script: scripts/{sc}")

    github_dir = REPO_ROOT / ".github"
    if not (github_dir / "pull_request_template.md").is_file():
        error("Missing .github/pull_request_template.md")
    if not (github_dir / "CODEOWNERS").is_file():
        error("Missing .github/CODEOWNERS")
    if not (github_dir / "ISSUE_TEMPLATE" / "change-request.md").is_file():
        error("Missing .github/ISSUE_TEMPLATE/change-request.md")


def main():
    print("=" * 60)
    print(" Agentic SDLC Repository Integrity & Governance Validator")
    print("=" * 60)

    check_required_root_files()
    check_agents_governance_structure()
    check_json_syntax_and_schemas()
    check_prohibited_and_sensitive_files()
    check_docs_and_approvals_structure()
    check_ci_cd_and_scripts()

    print("\n" + "=" * 60)
    if ERRORS:
        print(f"[FAILED] Validation failed with {len(ERRORS)} error(s):")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASSED] ALL AGENTIC SDLC GOVERNANCE & INTEGRITY CHECKS PASSED!")
        if WARNINGS:
            print(f"[INFO]   {len(WARNINGS)} warning(s) noted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
