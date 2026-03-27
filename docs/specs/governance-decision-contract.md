# Governance Decision Contract

## Goal
Определить единый контракт управленческого решения без внедрения runtime governance engine.

## Purpose
Governance decision contract описывает управленческое решение над запросом или исполнением.

Он связывает решение с `trace_id`, `command_id`, `execution_request_id`, `user_id` и `approval_action_id`, чтобы governance-level linkage можно было согласованно использовать между approval, budget, timeout и execution contracts.

## Governance Decision Object

```json
{
  "governance_decision_id": "gov-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "execution_request_id": "exec-0001",
  "user_id": "owner-001",
  "decision_type": "allow",
  "decision_scope": "request",
  "created_at": "2026-03-27T02:20:00Z",
  "rationale": "owner_confirmed",
  "linked_approval_action_id": "approval-0001",
  "linked_budget_hint_id": "budget-0001",
  "linked_timeout_policy_id": "timeout-0001",
  "decision_note": "Approved after reviewing budget and timeout constraints"
}
```

## Required Fields
- `governance_decision_id`
- `trace_id`
- `command_id`
- `user_id`
- `decision_type`
- `decision_scope`
- `created_at`

## Optional Fields
- `execution_request_id`
- `rationale`
- `linked_approval_action_id`
- `linked_budget_hint_id`
- `linked_timeout_policy_id`
- `decision_note`

## Field Semantics
### governance_decision_id
Уникальный идентификатор отдельного governance decision.

### trace_id
Ссылка на traceability envelope, в рамках которого фиксируется управленческое решение.

### command_id
Ссылка на исходную команду, к которой относится управленческое решение.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request, если решение относится к уже сформированному запросу на исполнение.

### user_id
Идентификатор пользователя, принявшего управленческое решение.

### decision_type
`decision_type` фиксирует тип управленческого решения.

Допустимые значения:
- `allow`
- `deny`
- `escalate`
- `defer`

### decision_scope
`decision_scope` фиксирует уровень действия управленческого решения.

Допустимые значения:
- `request`
- `session`
- `project`
- `company`

### created_at
Момент фиксации governance decision в формате ISO 8601 date-time.

### rationale
`rationale` является кратким машинно-читаемым основанием решения.

### linked_approval_action_id
`linked_approval_action_id` является опциональной ссылкой на уже существующий approval action contract.

### linked_budget_hint_id
`linked_budget_hint_id` является опциональной ссылкой на уже существующий budget hint contract.

### linked_timeout_policy_id
`linked_timeout_policy_id` является опциональной ссылкой на уже существующий timeout policy contract.

### decision_note
`decision_note` является опциональным человеко-читаемым пояснением.

## Rules
1. Governance decision contract должен описывать только управленческое решение над запросом или исполнением.
2. `trace_id`, `command_id` и `user_id` должны сохранять связь решения с исходным пользовательским и traceability context.
3. `execution_request_id`, `linked_approval_action_id`, `linked_budget_hint_id` и `linked_timeout_policy_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
4. `rationale`, если передан, должен оставаться кратким машинно-читаемым основанием.
5. `decision_note`, если передан, должен оставаться человеко-читаемым пояснением.
6. `decision_type` и `decision_scope` должны фиксировать только управленческое решение, а не runtime execution state.

## Boundaries
Этот контракт не является runtime governance engine.

Этот контракт не является approval workflow engine.

Этот контракт не является access control system.

Этот контракт не является database model.

## Expected Usage
- фиксация решений human-in-the-loop
- linkage между approval, budget, timeout и execution
- future linkage с dashboard, audit и policy layers

## Source Alignment
`docs/specs/governance-decision-contract.md` остаётся смысловым источником governance decision semantics.

`packages/shared-contracts/governance-decision.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
