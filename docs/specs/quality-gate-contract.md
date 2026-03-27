# Quality Gate Contract

## Goal
Определить отдельный контракт quality gate без внедрения CI engine, pipeline runner или test framework.

## Purpose
Quality gate contract описывает контрольную точку качества для артефакта, handoff или execution результата.

Он связывает фиксацию quality check с `trace_id`, `project_id` и опциональными ссылками на `artifact_id`, `execution_result_id` и `governance_decision_id`, чтобы evidence и результат проверки можно было согласованно привязывать к traceability, project context и governance-level decisions.

## Quality Gate Object

```json
{
  "quality_gate_id": "gate-0001",
  "gate_name": "shared-contracts-verification",
  "gate_type": "schema_check",
  "gate_status": "passed",
  "created_at": "2026-03-27T06:40:00Z",
  "trace_id": "trace-0001",
  "project_id": "project-001",
  "artifact_id": "artifact-0001",
  "execution_result_id": "result-0001",
  "linked_governance_decision_id": "gov-0001",
  "evidence_uri": "logs/verify_shared_contracts_2026-03-27.txt",
  "gate_note": "Shared contracts verification completed successfully"
}
```

## Required Fields
- `quality_gate_id`
- `gate_name`
- `gate_type`
- `gate_status`
- `created_at`

## Optional Fields
- `trace_id`
- `project_id`
- `artifact_id`
- `execution_result_id`
- `linked_governance_decision_id`
- `evidence_uri`
- `gate_note`

## Field Semantics
### quality_gate_id
Уникальный идентификатор quality gate record.

### gate_name
Человекочитаемое имя контрольной точки качества.

### gate_type
`gate_type` фиксирует тип контрольной проверки.

Допустимые значения:
- `requirement_check`
- `schema_check`
- `quality_check`
- `acceptance_check`
- `release_check`

### gate_status
`gate_status` фиксирует результат проверки.

Допустимые значения:
- `pending`
- `passed`
- `failed`
- `waived`

### created_at
Момент фиксации quality gate в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### project_id
`project_id` является опциональной ссылкой на project context.

### artifact_id
`artifact_id` является опциональной ссылкой на artifact reference.

### execution_result_id
`execution_result_id` является опциональной ссылкой на execution result.

### linked_governance_decision_id
`linked_governance_decision_id` является опциональной ссылкой на governance decision.

### evidence_uri
`evidence_uri` является опциональной строковой ссылкой на доказательство прохождения или провала quality gate.

### gate_note
`gate_note` является опциональным человеко-читаемым пояснением.

## Rules
1. Quality gate contract должен фиксировать факт quality check, а не исполнять проверку.
2. `trace_id` и `project_id`, если переданы, используются только как ссылки на уже существующие контракты.
3. `artifact_id`, `execution_result_id` и `linked_governance_decision_id`, если переданы, используются только как опциональные ссылки.
4. `evidence_uri`, если передан, должен использоваться только как строковая ссылка на доказательство.
5. `gate_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является CI engine.

Этот контракт не является test runner.

Этот контракт не является release manager runtime.

Этот контракт не является database model.

## Expected Usage
- фиксация факта quality check
- связь evidence с artifact/result
- future linkage с dashboard, audit и release governance

## Source Alignment
`docs/specs/quality-gate-contract.md` остаётся смысловым источником quality gate semantics.

`packages/shared-contracts/quality-gate.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.

