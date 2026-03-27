# Artifact Reference Contract

## Goal
Определить единый контракт ссылки на артефакт без внедрения runtime storage, file service или repository manager.

## Purpose
Artifact reference contract описывает ссылку на артефакт, используемый или произведённый системой.

Он связывает artifact-level reference с `trace_id`, `project_id`, `company_id` и `execution_result`, чтобы артефакты можно было согласованно привязывать к execution outputs и более широкому контексту системы.

## Artifact Reference Object

```json
{
  "artifact_id": "artifact-0001",
  "artifact_name": "company-context-report",
  "artifact_type": "report",
  "artifact_uri": "docs/reports/company-context-report.md",
  "created_at": "2026-03-27T02:00:00Z",
  "trace_id": "trace-0001",
  "project_id": "project-001",
  "company_id": "factory-main",
  "produced_by_execution_result_id": "result-0001",
  "artifact_note": "Reference to report produced during contract verification"
}
```

## Required Fields
- `artifact_id`
- `artifact_name`
- `artifact_type`
- `artifact_uri`
- `created_at`

## Optional Fields
- `trace_id`
- `project_id`
- `company_id`
- `produced_by_execution_result_id`
- `artifact_note`

## Field Semantics
### artifact_id
Уникальный идентификатор artifact reference.

### artifact_name
Человекочитаемое имя артефакта.

### artifact_type
`artifact_type` фиксирует тип артефакта.

Допустимые значения:
- `document`
- `schema`
- `script`
- `repository`
- `report`
- `binary`
- `other`

### artifact_uri
`artifact_uri` является строковой ссылкой или путём к артефакту.

### created_at
Момент фиксации artifact reference в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### project_id
`project_id` является опциональной ссылкой на project context.

### company_id
`company_id` является опциональной ссылкой на company context.

### produced_by_execution_result_id
`produced_by_execution_result_id` является опциональной ссылкой на execution result, породивший артефакт.

### artifact_note
`artifact_note` является опциональным пояснением artifact reference.

## Rules
1. Artifact reference contract должен описывать только ссылку на артефакт, а не способ его runtime хранения.
2. `artifact_uri` должен использоваться только как строковая ссылка или путь к артефакту.
3. `trace_id`, `project_id`, `company_id` и `produced_by_execution_result_id`, если переданы, используются только как опциональные ссылки.
4. `artifact_type` должен отражать тип артефакта, а не runtime storage class.
5. `artifact_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является file storage engine.

Этот контракт не является artifact repository implementation.

Этот контракт не является binary registry.

Этот контракт не является document database.

## Expected Usage
- связывание execution results с output artifacts
- grouping artifacts by project/company/trace
- future linkage с dashboard, audit и knowledge layers

## Source Alignment
`docs/specs/artifact-reference-contract.md` остаётся смысловым источником artifact reference semantics.

`packages/shared-contracts/artifact-reference.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
