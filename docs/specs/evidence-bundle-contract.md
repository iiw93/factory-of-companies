# Evidence Bundle Contract

## Goal
Определить отдельный контракт evidence bundle без внедрения runtime audit store, document database или evidence pipeline.

## Purpose
Evidence bundle contract описывает набор доказательств, собранных по одному trace, project или quality decision.

Он связывает bundle-level reference с `trace_id`, `project_id`, `quality_gate_id`, `execution_result_id`, `governance_decision_id` и `artifact_id`, чтобы evidence можно было согласованно связывать с quality и governance linkage.

## Evidence Bundle Object

```json
{
  "evidence_bundle_id": "bundle-0001",
  "bundle_name": "release-readiness-evidence",
  "bundle_status": "reviewed",
  "created_at": "2026-03-27T07:00:00Z",
  "trace_id": "trace-0001",
  "project_id": "project-001",
  "linked_quality_gate_id": "gate-0001",
  "linked_execution_result_id": "result-0001",
  "linked_governance_decision_id": "gov-0001",
  "artifact_ids": [
    "artifact-0001",
    "artifact-0002"
  ],
  "evidence_summary": "Collected verification report, decision note, and release checklist artifacts",
  "bundle_note": "Prepared for governance review"
}
```

## Required Fields
- `evidence_bundle_id`
- `bundle_name`
- `bundle_status`
- `created_at`

## Optional Fields
- `trace_id`
- `project_id`
- `linked_quality_gate_id`
- `linked_execution_result_id`
- `linked_governance_decision_id`
- `artifact_ids`
- `evidence_summary`
- `bundle_note`

## Field Semantics
### evidence_bundle_id
Уникальный идентификатор evidence bundle.

### bundle_name
Человекочитаемое имя evidence bundle.

### bundle_status
`bundle_status` фиксирует текущее состояние набора доказательств.

Допустимые значения:
- `draft`
- `collected`
- `reviewed`
- `accepted`
- `rejected`

### created_at
Момент фиксации evidence bundle в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### project_id
`project_id` является опциональной ссылкой на project context.

### linked_quality_gate_id
`linked_quality_gate_id` является опциональной ссылкой на quality gate contract.

### linked_execution_result_id
`linked_execution_result_id` является опциональной ссылкой на execution result contract.

### linked_governance_decision_id
`linked_governance_decision_id` является опциональной ссылкой на governance decision contract.

### artifact_ids
`artifact_ids` является массивом ссылок на artifact reference.

### evidence_summary
`evidence_summary` является кратким текстовым summary состава или смысла evidence bundle.

### bundle_note
`bundle_note` является опциональным пояснением.

## Rules
1. Evidence bundle contract должен описывать набор доказательств, а не механизм их runtime обработки.
2. `trace_id` и `project_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `linked_quality_gate_id`, `linked_execution_result_id` и `linked_governance_decision_id`, если переданы, используются только как опциональные ссылки.
4. `artifact_ids`, если передан, должен содержать только ссылки на artifact reference.
5. `evidence_summary`, если передан, должен оставаться кратким текстовым summary.
6. `bundle_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является audit database.

Этот контракт не является document store.

Этот контракт не является evidence processing engine.

Этот контракт не является governance runtime.

## Expected Usage
- bundling evidence for quality and governance
- linking artifacts and results to a decision
- future dashboard / audit / release review views

## Source Alignment
`docs/specs/evidence-bundle-contract.md` остаётся смысловым источником evidence bundle semantics.

`packages/shared-contracts/evidence-bundle.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
