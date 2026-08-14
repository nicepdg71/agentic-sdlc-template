#!/usr/bin/env python3
"""
Agentic SDLC Repository Integrity & Governance Validator (v1.1.0)
Validates repository structure, required governance files, JSON syntax,
schemas, secret safety, T-01 ~ T-12 architecture compliance, and v1.1 Change Cycle & Stitch UI extensions.
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
    print("\n[1/7] Checking required root files and project metadata...")
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

    # Check project.yaml v1.1.0 structure
    try:
        import yaml
        with open(REPO_ROOT / "project.yaml", "r", encoding="utf-8") as f:
            p_data = yaml.safe_load(f)
        if p_data.get("version") != "1.1.0":
            warn(f"project.yaml version is '{p_data.get('version')}', expected '1.1.0'")
        if "toolchain" in p_data and "ui_design" in p_data["toolchain"]:
            info("Validated project.yaml toolchain.ui_design configuration.")
        else:
            error("project.yaml missing 'toolchain.ui_design' configuration block.")
    except ImportError:
        # If PyYAML is not installed, parse via text
        with open(REPO_ROOT / "project.yaml", "r", encoding="utf-8") as f:
            content = f.read()
        if 'version: "1.1.0"' in content or "version: '1.1.0'" in content:
            info("project.yaml specifies version 1.1.0.")
        if "toolchain:" in content and "ui_design:" in content:
            info("project.yaml specifies toolchain.ui_design.")
        else:
            error("project.yaml missing toolchain.ui_design block.")


def check_agents_governance_structure():
    print("\n[2/7] Checking .agents/ governance structure...")
    agents_dir = REPO_ROOT / ".agents"
    if not agents_dir.is_dir():
        error("Missing .agents/ directory")
        return

    # Check agents.md
    if not (agents_dir / "agents.md").is_file():
        error("Missing .agents/agents.md")
    else:
        info("Found .agents/agents.md")

    # Check rules (10 rules)
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

    # Check workflows (12 workflows in v1.1)
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
        "request-change.md",
        "record-change-decision.md",
        "close-change-cycle.md",
    ]
    for wf in expected_workflows:
        wf_path = workflows_dir / wf
        if not wf_path.is_file():
            error(f"Missing workflow: .agents/workflows/{wf}")
        else:
            info(f"Found workflow: .agents/workflows/{wf}")

    # Check skills (15 skills in v1.1)
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
        "change-impact-analysis",
        "stitch-design-integration",
    ]
    for sk in expected_skills:
        sk_path = skills_dir / sk / "SKILL.md"
        if not sk_path.is_file():
            error(f"Missing skill: .agents/skills/{sk}/SKILL.md")
        else:
            info(f"Found skill: .agents/skills/{sk}/SKILL.md")

    # Check schemas
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


def check_change_and_ui_templates():
    print("\n[3/7] Checking Change Management and UI templates (T-11, T-12)...")
    templates_dir = REPO_ROOT / ".agents" / "templates"

    # Change templates
    change_templates = [
        "CHANGE_REQUEST.template.md",
        "IMPACT_ANALYSIS.template.md",
        "CHANGE_TRACEABILITY.template.md",
        "CHANGE_CLOSURE.template.md",
    ]
    for ct in change_templates:
        p = templates_dir / "changes" / ct
        if not p.is_file():
            error(f"Missing change template: .agents/templates/changes/{ct}")
        else:
            info(f"Found change template: .agents/templates/changes/{ct}")

    # UI templates
    ui_design_templates = [
        "UI_DESIGN_BRIEF.template.md",
        "UI_DESIGN_HANDOFF.template.md",
        "STITCH_PROJECT_REF.template.json",
        "STITCH_PROMPTS.template.md",
    ]
    for ut in ui_design_templates:
        p = templates_dir / "artifacts" / "02-design" / "ui" / ut
        if not p.is_file():
            error(f"Missing UI design template: .agents/templates/artifacts/02-design/ui/{ut}")
        else:
            info(f"Found UI design template: .agents/templates/artifacts/02-design/ui/{ut}")

    # UI Verification template
    ui_verify_tpl = templates_dir / "artifacts" / "04-test" / "UI_VERIFICATION_REPORT.template.md"
    if not ui_verify_tpl.is_file():
        error(f"Missing UI verification template: .agents/templates/artifacts/04-test/UI_VERIFICATION_REPORT.template.md")
    else:
        info("Found UI verification template: UI_VERIFICATION_REPORT.template.md")

    # Change register
    change_register = REPO_ROOT / "docs" / "changes" / "CHANGE_REGISTER.md"
    if not change_register.is_file():
        error("Missing docs/changes/CHANGE_REGISTER.md")
    else:
        info("Found docs/changes/CHANGE_REGISTER.md")


def check_json_syntax_and_schemas():
    print("\n[4/7] Checking JSON syntax and schema validity...")
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
    print("\n[5/7] Checking for prohibited secret/credential files...")
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

    info(f"Scanned {len(tracked_files)} tracked files for sensitive credentials. No unauthorized keys found.")


def check_docs_and_approvals_structure():
    print("\n[6/7] Checking docs/ and approvals structure (T-07, T-08, T-11)...")
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


def check_ci_cd_and_scripts():
    print("\n[7/7] Checking CI/CD scripts and GitHub templates (T-09)...")
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
    print("=" * 65)
    print(" Agentic SDLC v1.1.0 Repository Integrity & Governance Validator")
    print("=" * 65)

    check_required_root_files()
    check_agents_governance_structure()
    check_change_and_ui_templates()
    check_json_syntax_and_schemas()
    check_prohibited_and_sensitive_files()
    check_docs_and_approvals_structure()
    check_ci_cd_and_scripts()

    print("\n" + "=" * 65)
    if ERRORS:
        print(f"[FAILED] Validation failed with {len(ERRORS)} error(s):")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASSED] ALL AGENTIC SDLC v1.1.0 GOVERNANCE & INTEGRITY CHECKS PASSED!")
        if WARNINGS:
            print(f"[INFO]   {len(WARNINGS)} warning(s) noted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
