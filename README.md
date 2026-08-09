# Agentic SDLC Template

A structured, governance-driven Software Development Life Cycle (SDLC) framework optimized for AI coding agents and human-agent collaboration.

## Overview
This template establishes a standardized directory layout, agent rules, workflows, prompts, skills, contracts, and phase-gate documentation for agentic software engineering.

## Project Structure
- `.agents/`: Agent configurations, governance rules, workflows, prompts, and skills.
- `docs/`: Phase-by-phase engineering artifacts and handoff contracts.
- `contracts/`: Interface definitions (API, Events, AI schemas).
- `src/`: Source code.
- `tests/`: Test suites (unit, integration, e2e, security).
- `infra/`: Infrastructure-as-code and environment configurations.
- `.github/`: CI/CD workflows, issue templates, PR templates, and CODEOWNERS.

## Workflow Phases
1. **00 - Project Definition**: Charter, high-level scope, and constraints.
2. **01 - Analysis**: Detailed requirements, user stories, acceptance criteria, and traceability.
3. **02 - Design**: System architecture, component design, data models, ADRs, and security.
4. **03 - Implementation**: Implementation planning, iterative development, and working changelog.
5. **04 - Test & Verification**: Test design, test cases execution, test reports, and security verification.
6. **05 - Release**: Release planning, checklists, release notes, and rollback procedures.
