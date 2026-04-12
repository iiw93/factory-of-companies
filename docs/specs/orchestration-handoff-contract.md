# Orchestration Handoff Contract

## Status Note (Guardrail-Only, Non-Authorizing)
This contract is historical/planning context only and does not authorize implementation-planning, coding, or execution.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

## Goal
Определить отдельный контракт передачи единицы работы между слоями и ролями системы без внедрения runtime orchestration engine.

## Purpose
Orchestration handoff contract описывает нормализованный объект передачи работы от одного слоя или роли к другому.

Он связывает handoff с `trace_id`, `command_id`, `execution_request_id`, `governance_decision_id`, `source_role`, `target_role` и `action_type`, чтобы linkage между decision, execution и role-level coordination оставался формализованным.

## Orchestration Handoff Object

```json
{
  "handoff_id": "handoff-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "execution_request_id": "exec-0001",
  "source_role": "planner_agent",
  "target_role": "developer_agent",
  "action_type": "write_code",
  "handoff_status": "prepared",
  "created_at": "2026-03-27T03:10:00Z",
  "priority": "high",
  "linked_governance_decision_id": "gov-0001",
  "linked_artifact_id": "artifact-0001",
  "handoff_note": "Historical/planning handoff context only; no implementation-planning or coding is authorized by this example."
}
```

## Required Fields
- `handoff_id`
- `trace_id`
- `command_id`
- `source_role`
- `target_role`
- `action_type`
- `handoff_status`
- `created_at`
- `priority`

## Optional Fields
- `execution_request_id`
- `linked_governance_decision_id`
- `linked_artifact_id`
- `handoff_note`

## Field Semantics
### handoff_id
Уникальный идентификатор отдельного orchestration handoff.

### trace_id
Ссылка на traceability envelope, в рамках которого передаётся работа.

### command_id
Ссылка на исходную команду, из которой возник handoff.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request, если handoff уже связан с нормализованным запросом на исполнение.

### source_role
`source_role` определяет логическую роль источника передачи работы.

Значение `source_role` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### target_role
`target_role` определяет логическую роль получателя передачи работы.

Значение `target_role` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### action_type
`action_type` определяет тип передаваемой работы.

Значение `action_type` должно оставаться согласованным с `docs/specs/action-type-contract.md`.

### handoff_status
`handoff_status` фиксирует текущее состояние handoff.

Допустимые значения:
- `prepared`
- `dispatched`
- `accepted`
- `rejected`
- `cancelled`

### created_at
Момент создания handoff в формате ISO 8601 date-time.

### priority
`priority` фиксирует относительный приоритет handoff.

Значение `priority` должно концептуально совпадать с priority contract и оставаться согласованным с `docs/specs/priority-contract.md`.

### linked_governance_decision_id
`linked_governance_decision_id` является опциональной ссылкой на governance decision, если handoff был сформирован или изменён под влиянием управленческого решения.

### linked_artifact_id
`linked_artifact_id` является опциональной ссылкой на artifact reference, если handoff связан с конкретным артефактом.

### handoff_note
`handoff_note` является опциональным человеко-читаемым пояснением.

## Rules
1. Каждый orchestration handoff должен ссылаться на конкретные `trace_id` и `command_id`.
2. Orchestration handoff contract должен описывать передачу одной единицы работы от одного слоя или роли к другому.
3. `source_role` и `target_role` описывают только логические роли, а не runtime implementation detail.
4. `execution_request_id`, `linked_governance_decision_id` и `linked_artifact_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
5. `action_type` должен фиксировать тип передаваемой работы в нормализованной форме.
6. `priority` должен использоваться как advisory signal и концептуально совпадать с priority contract.
7. `handoff_note`, если передан, должен оставаться кратким человеко-читаемым пояснением.

## Boundaries
Этот контракт не является runtime queue.

Этот контракт не является worker implementation.

Этот контракт не является scheduler.

Этот контракт не является transport protocol.

## Expected Usage
- handoff between planner / architect / developer / qa / devops and other roles
- linkage between decision and execution
- future dashboard and observability views

## Source Alignment
`docs/specs/orchestration-handoff-contract.md` остаётся смысловым источником orchestration handoff semantics.

`packages/shared-contracts/orchestration-handoff.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
