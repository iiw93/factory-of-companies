# Release Decision Contract

## Status Note (Guardrail-Only, Non-Authorizing)
This contract is historical/planning context only and is not evidence of active release, deploy, or artifact publication authorization.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/specs/thin-runtime-mvp-scenario.md`

This contract does not authorize implementation-planning, coding, deployment, or artifact publication.

## Goal
Определить отдельный контракт решения о выпуске без внедрения runtime release manager, deployment engine, CI/CD pipeline или environment registry.

## Purpose
Release decision contract описывает решение о выпуске результата или артефакта.

Он связывает release-level decision с `trace_id`, `project_id`, `execution_result_id`, `artifact_id`, `quality_gate_id`, `evidence_bundle_id` и `governance_decision_id`, чтобы итоговое решение о выпуске можно было согласованно увязывать с traceability, quality, evidence и governance linkage.

## Release Decision Object

```json
{
  "release_decision_id": "release-0001",
  "decision_name": "release-readiness-decision",
  "release_status": "historical_planning_trace",
  "created_at": "2026-03-27T11:10:00Z",
  "trace_id": "trace-0001",
  "project_id": "project-001",
  "execution_result_id": "result-0001",
  "artifact_id": "artifact-0001",
  "linked_quality_gate_id": "gate-0001",
  "linked_evidence_bundle_id": "bundle-0001",
  "linked_governance_decision_id": "gov-0001",
  "release_scope": "artifact",
  "release_note": "Historical/planning release context only; no deploy or artifact publication is authorized by this example."
}
```

## Required Fields
- `release_decision_id`
- `decision_name`
- `release_status`
- `created_at`

## Optional Fields
- `trace_id`
- `project_id`
- `execution_result_id`
- `artifact_id`
- `linked_quality_gate_id`
- `linked_evidence_bundle_id`
- `linked_governance_decision_id`
- `release_scope`
- `release_note`

## Field Semantics
### release_decision_id
Уникальный идентификатор отдельного release decision.

### decision_name
Человекочитаемое имя решения о выпуске.

### release_status
`release_status` фиксирует итоговый статус решения о выпуске.

Допустимые значения:
- `approved`
- `blocked`
- `deferred`
- `requires_review`

### created_at
Момент фиксации release decision в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### project_id
`project_id` является опциональной ссылкой на project context.

### execution_result_id
`execution_result_id` является опциональной ссылкой на execution result contract.

### artifact_id
`artifact_id` является опциональной ссылкой на artifact reference contract.

### linked_quality_gate_id
`linked_quality_gate_id` является опциональной ссылкой на quality gate contract.

### linked_evidence_bundle_id
`linked_evidence_bundle_id` является опциональной ссылкой на evidence bundle contract.

### linked_governance_decision_id
`linked_governance_decision_id` является опциональной ссылкой на governance decision contract.

### release_scope
`release_scope` фиксирует уровень решения о выпуске.

Допустимые значения:
- `artifact`
- `project`
- `bundle`

### release_note
`release_note` является опциональным пояснением.

## Rules
1. Release decision contract должен фиксировать решение о выпуске результата или артефакта, а не исполнять выпуск.
2. `trace_id` и `project_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `execution_result_id` и `artifact_id`, если переданы, используются только как опциональные ссылки.
4. `linked_quality_gate_id`, `linked_evidence_bundle_id` и `linked_governance_decision_id`, если переданы, используются только как опциональные ссылки.
5. `release_scope`, если передан, должен фиксировать только logical release scope.
6. `release_note`, если передан, должен оставаться кратким человеко-читаемым пояснением.

## Boundaries
Этот контракт не является deployment engine.

Этот контракт не является runtime release manager.

Этот контракт не является CI/CD pipeline.

Этот контракт не является environment registry.

## Expected Usage
- фиксация решения о выпуске
- связь quality/evidence/governance с итоговым решением
- future linkage с dashboard, audit и release workflows

## Source Alignment
`docs/specs/release-decision-contract.md` остаётся смысловым источником release decision semantics.

`packages/shared-contracts/release-decision.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
