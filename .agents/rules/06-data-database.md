# Rule 06: Data Integrity & Database Governance

## 1. Objective
Ensure database schema evolution is safe, deterministic, backward-compatible where necessary, and thoroughly documented to prevent data corruption or runtime failures.

## 2. Core Policies

### 2.1 Authoritative Data Model Documentation
- The canonical Entity Relationship Diagram (ERD), table schemas, indices, and constraints must be documented in `docs/02-design/DATA_MODEL.md`.
- No database changes may be applied without prior updating of `DATA_MODEL.md`.

### 2.2 Versioned Migrations & Rollback Scripts
- Every schema change must be packaged as an idempotent, forward migration script.
- Every forward migration must be paired with an exact, tested rollback script (e.g., `V1__init.sql` and `U1__init.sql`).

### 2.3 Non-Destructive Schema Evolution
- Destructive schema operations (such as dropping tables, removing columns, or changing column data types) must follow an expand-and-contract / multi-phase migration pattern to avoid downtime.
- Data deletion or destructive scripts require explicit human sign-off and validated backup procedures.

### 2.4 Integrity & Indexing Governance
- Foreign key constraints, unique indices, and check constraints must be declared at the database layer to guarantee referential integrity.
- Queries on large datasets must be backed by appropriate index designs reviewed in `DATA_MODEL.md`.

### 2.5 Multilingual Data, Character Encoding & Timezone Standards
- Persistent databases must standardize on `utf8mb4` character set with appropriate collation (`utf8mb4_unicode_ci` or language-aware collations) to fully support Korean (Hangul CJK) and English text.
- Datetime fields must strictly store timestamps in UTC (`TIMESTAMP WITH TIME ZONE` or UTC ISO8601).
- Multilingual data schemas (e.g., column suffix `name_ko`/`name_en`, JSONB localization payloads, or translation reference tables) must be explicitly designed and documented in `DATA_MODEL.md`.