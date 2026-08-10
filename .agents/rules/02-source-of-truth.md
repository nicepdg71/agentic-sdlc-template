# Rule 02: Single Source of Truth (SSOT)

## 1. Objective
Establish a clear hierarchy of authority across all project artifacts to prevent specification drift, undocumented code behavior, and inconsistencies.

## 2. Hierarchy of Authority

The priority order of authority is strictly defined as follows:

1. **`project.yaml` & Project Charter**: Top-level project constraints, governance rules, and phase configuration.
2. **Phase Documentation (`docs/`)**: Approved requirements (`docs/01-analysis/`), architecture specifications (`docs/02-design/`), and test criteria (`docs/04-test/`).
3. **Interface Contracts (`contracts/`)**: Formal schemas for APIs (OpenAPI/gRPC), asynchronous events, and AI interaction protocols.
4. **Implementation Plans (`docs/03-implementation/IMPLEMENTATION_PLAN.md`)**: Scheduled work breakdown structure.
5. **Source Code (`src/`) & Automated Tests (`tests/`)**: Executable realization of approved documentation and contracts.

## 3. Core Policies

### 3.1 Code Follows Specification (Never Vice Versa)
- Source code must directly implement and reflect the approved designs and interface contracts.
- Code must never introduce undocumented endpoints, fields, data structures, or behaviors.

### 3.2 Specification Synchronization
- If implementation reveals a necessary change to an interface or architecture, the corresponding documentation in `docs/` or contract in `contracts/` must be updated and approved **before** modifying the source code.