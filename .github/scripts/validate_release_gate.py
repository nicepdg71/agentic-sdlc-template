#!/usr/bin/env python3
"""
Agentic SDLC Production Release Gate Validator (v1.1.0)
Validates G5 Approval Record and Release Handoff integrity before production deployment across lifecycle cycles.
"""

import sys
import os
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output even on Windows consoles
if sys.stdout.encoding != "utf-8" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def main():
    parser = argparse.ArgumentParser(description="Validate G5 Production Release Gate Approval")
    parser.add_argument("--version", required=True, help="Expected release version")
    parser.add_argument("--commit", required=True, help="Expected release Git commit SHA")
    parser.add_argument("--cycle", default="INIT-001", help="Execution cycle ID (e.g. INIT-001, CR-0001)")
    parser.add_argument("--root", default=str(REPO_ROOT), help="Repository root path")

    args = parser.parse_args()
    root_dir = Path(args.root)

    print("=" * 65)
    print(" Agentic SDLC G5 Release Gate Validator (v1.1.0)")
    print("=" * 65)
    print(f"Cycle ID:       {args.cycle}")
    print(f"Target Version: {args.version}")
    print(f"Target Commit:  {args.commit}")
    print("-" * 65)

    errors = []

    # 1. Check G5 Approval Record (in cycle directory or root approvals)
    cycle_approval_file = root_dir / "docs" / "approvals" / args.cycle / "G5-production-release.approval.json"
    root_approval_file = root_dir / "docs" / "approvals" / "G5-production-release.approval.json"

    approval_file = cycle_approval_file if cycle_approval_file.is_file() else root_approval_file

    if not approval_file.is_file():
        errors.append(f"G5 Approval Record file not found: checked {cycle_approval_file.relative_to(root_dir)} and {root_approval_file.relative_to(root_dir)}")
    else:
        try:
            with open(approval_file, "r", encoding="utf-8") as f:
                approval_data = json.load(f)

            # Check Gate
            if approval_data.get("gate") != "G5":
                errors.append(f"Invalid gate in approval record: expected 'G5', got '{approval_data.get('gate')}'")

            # Check Decision
            decision = approval_data.get("decision")
            if decision not in ["APPROVED", "APPROVED_WITH_COMMENTS"]:
                errors.append(f"G5 decision is not approved: current decision is '{decision}'")

            # Check Release Candidate commit & version in decision_scope
            rc = approval_data.get("decision_scope", {}).get("release_candidate", {})
            approved_commit = rc.get("commit", "").strip()
            approved_version = rc.get("version", "").strip()

            if not approved_commit:
                errors.append("G5 approval record missing 'decision_scope.release_candidate.commit'")
            elif approved_commit.lower() != args.commit.strip().lower():
                errors.append(f"G5 approved commit mismatch: approved '{approved_commit}', requested '{args.commit}'")

            if approved_version and approved_version != args.version.strip():
                errors.append(f"G5 approved version mismatch: approved '{approved_version}', requested '{args.version}'")

            print(f"[OK]    G5 Approval Record verified ({approval_file.relative_to(root_dir)}): decision={decision}, commit={approved_commit}")

        except Exception as e:
            errors.append(f"Failed to parse G5 approval record {approval_file.name}: {e}")

    # 2. Check RELEASE_HANDOFF.json
    handoff_file = root_dir / "docs" / "05-release" / "RELEASE_HANDOFF.json"
    if not handoff_file.is_file():
        errors.append(f"Release Handoff file not found: {handoff_file.relative_to(root_dir)}")
    else:
        try:
            with open(handoff_file, "r", encoding="utf-8") as f:
                handoff_data = json.load(f)

            if handoff_data.get("stage") != "RELEASE":
                errors.append(f"Invalid stage in release handoff: expected 'RELEASE', got '{handoff_data.get('stage')}'")

            handoff_status = handoff_data.get("status")
            if handoff_status != "APPROVED":
                errors.append(f"Release handoff status is not APPROVED: current status is '{handoff_status}'")
            else:
                print(f"[OK]    Release Handoff verified: status={handoff_status}")

        except Exception as e:
            errors.append(f"Failed to parse Release Handoff {handoff_file.name}: {e}")

    print("-" * 65)
    if errors:
        print(f"[FAILED] G5 RELEASE GATE VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        print("\nProduction deployment is BLOCKED until G5 Approval and Release Handoff are properly signed off.")
        sys.exit(1)
    else:
        print("[PASSED] G5 PRODUCTION RELEASE GATE VERIFICATION SUCCEEDED!")
        print(f"Authorized deployment for Commit: {args.commit} (Version: {args.version}, Cycle: {args.cycle})")
        sys.exit(0)


if __name__ == "__main__":
    main()
