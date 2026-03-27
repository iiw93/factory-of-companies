# Approval Action Contract

## Goal
Определить единый контракт для отдельного действия подтверждения или отклонения команды без внедрения runtime approval engine.

## Purpose
Approval action contract описывает нормализованный объект действия подтверждения или отклонения.

Он связывает решение пользователя с конкретным `command_id`, `trace_id`, `user_id` и `session_id`.

## Approval Action Object

```json
{
  "approval_action_id": "approval-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "user_id": "owner-001",
  "session_id": "session-001",
  "decision": "approve",
  "created_at": "2026-03-26T00:15:00Z",
  "reason": "owner_confirmed",
  "comment": "Подтверждаю запуск действия"
}
```

## Required Fields
- `approval_action_id`
- `trace_id`
- `command_id`
- `user_id`
- `session_id`
- `decision`
- `created_at`

## Optional Fields
- `reason`
- `comment`

## Field Semantics
### approval_action_id
Уникальный идентификатор отдельного approval action.

### trace_id
Ссылка на traceability context, в котором фиксируется решение.

### command_id
Ссылка на исходную команду, для которой принимается решение.

### user_id
Идентификатор пользователя, принявшего решение.

### session_id
Идентификатор пользовательской сессии, в рамках которой было принято решение.

### decision
`decision` может быть только `approve` или `reject`.

### created_at
Момент фиксации решения в формате ISO 8601 date-time.

### reason
`reason` является кратким машинно-читаемым основанием решения.

### comment
`comment` является опциональным человеко-читаемым пояснением.

## Rules
1. Каждый approval action должен ссылаться на конкретные `trace_id` и `command_id`.
2. Каждый approval action должен быть привязан к конкретным `user_id` и `session_id`.
3. `decision` допускает только значения `approve` и `reject`.
4. `reason`, если передан, должен оставаться коротким машинно-читаемым основанием.
5. `comment`, если передан, используется только как человеко-читаемое пояснение.

## Boundaries
Этот контракт не является policy engine.

Этот контракт не является governance engine.

Этот контракт не является audit database.

Этот контракт не является runtime approval workflow.

## Expected Usage
- Telegram approval
- Dashboard approval
- future linkage with governance and audit trail

## Source Alignment
`docs/specs/approval-action-contract.md` остаётся смысловым источником approval action semantics.

`packages/shared-contracts/approval-action.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
