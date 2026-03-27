# Execution Request Contract

## Goal
Определить единый контракт отдельного запроса на выполнение работы без внедрения execution engine.

## Purpose
Execution request contract описывает нормализованный объект запроса на выполнение работы.

Он связывает handoff из orchestration layer с конкретными `trace_id`, `command_id`, `session_id` и `user_id`.

## Execution Request Object

```json
{
  "execution_request_id": "exec-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "session_id": "session-001",
  "user_id": "owner-001",
  "target_role": "planner",
  "action_type": "prepare_project_plan",
  "priority": "normal",
  "created_at": "2026-03-26T00:20:00Z",
  "timeout_seconds": 300,
  "budget_hint": 5.0,
  "payload": {
    "project_id": "project-001",
    "input_summary": "Сформировать первичный план проекта"
  }
}
```

## Required Fields
- `execution_request_id`
- `trace_id`
- `command_id`
- `session_id`
- `user_id`
- `target_role`
- `action_type`
- `priority`
- `created_at`

## Optional Fields
- `timeout_seconds`
- `budget_hint`
- `payload`

## Field Semantics
### execution_request_id
Уникальный идентификатор отдельного execution request.

### trace_id
Ссылка на traceability context, в рамках которого передаётся работа на исполнение.

### command_id
Ссылка на исходную команду, из которой возник execution handoff.

### session_id
Идентификатор пользовательской сессии, к которой относится запрос на исполнение.

### user_id
Идентификатор пользователя, чьё действие или запрос породили execution request.

### target_role
`target_role` определяет логическую роль исполнителя.

### action_type
`action_type` определяет тип исполняемой работы.

### priority
`priority` определяет относительный приоритет запроса на исполнение.

### created_at
Момент создания execution request в формате ISO 8601 date-time.

### timeout_seconds
`timeout_seconds` является опциональным ограничителем по времени исполнения.

### budget_hint
`budget_hint` является опциональным ограничителем или ориентиром по ресурсу исполнения.

### payload
`payload` является опциональным объектом с входными данными для исполнения.

## Rules
1. Каждый execution request должен ссылаться на конкретные `trace_id` и `command_id`.
2. Каждый execution request должен сохранять `session_id` и `user_id` для связи с исходным пользовательским контекстом.
3. `target_role` описывает только логическую роль исполнителя, а не runtime implementation detail.
4. `action_type` фиксирует тип исполняемой работы в нормализованной форме.
5. `priority` должен использоваться как относительный приоритет, а не как гарантия scheduling semantics.
6. `timeout_seconds` и `budget_hint`, если переданы, используются только как ограничители.
7. `payload`, если передан, должен оставаться структурированным объектом входных данных.

## Boundaries
Этот контракт не является execution engine.

Этот контракт не является task queue implementation.

Этот контракт не является scheduler.

Этот контракт не является runtime worker code.

## Expected Usage
- handoff от orchestration layer
- future linkage с agent roles
- future linkage с execution/audit trail

## Source Alignment
`docs/specs/execution-request-contract.md` остаётся смысловым источником execution request semantics.

`packages/shared-contracts/execution-request.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
