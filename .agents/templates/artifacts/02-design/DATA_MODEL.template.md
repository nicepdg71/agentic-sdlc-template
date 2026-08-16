---
artifact_id: "<DATA-ID>"
project_id: "<PROJECT-ID>"
stage: "DESIGN"
artifact_type: "DATA_MODEL"
version: "0.1"
status: "DRAFT"
owner: "@architect"
approval_gate: "G2"
---

# Data Model

## 1. Data Model Overview

-


## 2. Entities

### Entity: <Name>

Purpose:

Related Requirement:


### Attributes

| Field | Type | Required | Description | Sensitive |
|---|---|---|---|---|
| id | | YES | | NO |


## 3. Relationships

| Source | Relationship | Target |
|---|---|---|
| | | |


## 4. Character Encoding, Collation & Multilingual Strategy

- **Character Set**: `utf8mb4` (Strict UTF-8 encoding support for full Unicode including CJK/Hangul)
- **Collation**: `utf8mb4_unicode_ci` / `ko_KR.utf8`
- **Timezone Standard**: UTC (`TIMESTAMP WITH TIME ZONE`)
- **Multilingual Storage Pattern**:
  - Pattern Choice: `<COLUMN_SUFFIX (e.g. name_ko, name_en) | LOCALIZED_JSONB | TRANSLATION_TABLE>`
  - Fallback Strategy: Return English (`en`) when requested locale field is empty

## 5. Constraints

-


## 5. Index Considerations

-


## 6. Security / Access

-


## 7. Migration Considerations

-


## 8. Data Risks

-
