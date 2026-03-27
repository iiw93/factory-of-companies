# Execution Result Contract

## Goal
Определить единый контракт результата исполнения отдельного действия без внедрения execution engine.

## Purpose
Execution result contract описывает нормализованный объект результата выполнения execution request.

Он связывает итог исполнения с конкретными `execution_request_id`, `trace_id`, `command_id`, `session_id` и `user_id`.

## Execution Result Object

```json
{
  "execution_result_id": "result-0001",
  "execution_request_id": "exec-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "session_id": "session-001",
  "user_id": "owner-001",
  "outcome": "completed",
  "created_at": "2026-03-26T00:30:00Z",
  "completed_at": "2026-03-26T00:31:10Z",
  "status_message": "Execution completed successfully",
  "result_payload": {
    "plan_id": "plan-001",
    "artifacts_count": 2
  }
}
```

## Required Fields
- `execution_result_id`
- `execution_request_id`
- `trace_id`
- `command_id`
- `session_id`
- `user_id`
- `outcome`
- `created_at`

## Optional Fields
- `completed_at`
- `status_message`
- `result_payload`
- `error_code`
- `error_message`

## Field Semantics
### execution_result_id
Уникальный идентификатор отдельного execution result.

### execution_request_id
Ссылка на execution request, результат которого фиксируется этим контрактом.

### trace_id
Ссылка на traceability context, в рамках которого происходило исполнение.

### command_id
Ссылка на исходную команду, породившую execution request.

### session_id
Идентификатор пользовательской сессии, к которой относится результат исполнения.

### user_id
Идентификатор пользователя, чьё действие или запрос породили execution request.

### outcome
`outcome` отражает итог исполнения.

Допустимые значения:
- `completed`
- `failed`
- `cancelled`
- `timed_out`

### created_at
Момент фиксации execution result в формате ISO 8601 date-time.

### completed_at
`completed_at` является опциональным временем фактического завершения исполнения.

### status_message
`status_message` является кратким человеко-читаемым описанием результата.

### result_payload
`result_payload` является опциональным объектом результата.

### error_code
`error_code` является опциональным машинно-читаемым кодом ошибки.

### error_message
`error_message` является опциональным человеко-читаемым описанием ошибки.

## Rules
1. Каждый execution result должен ссылаться на конкретный `execution_request_id`.
2. Каждый execution result должен сохранять `trace_id`, `command_id`, `session_id` и `user_id` для связи с исходным пользовательским контекстом.
3. `outcome` фиксирует только итог исполнения, а не внутренние шаги runtime.
4. `status_message`, если передан, должен оставаться коротким человеко-читаемым описанием результата.
5. `result_payload`, если передан, должен оставаться структурированным объектом результата.
6. `error_code` и `error_message`, если переданы, используются только для ошибочных исходов, таких как `failed` или `timed_out`.

## Boundaries
Этот контракт не является runtime worker log.

Этот контракт не является event stream.

Этот контракт не является audit database.

Этот контракт не является execution engine.

## Expected Usage
- фиксация завершения execution request
- связь с traceability envelope
- future linkage с observability и audit trail

## Source Alignment
`docs/specs/execution-result-contract.md` остаётся смысловым источником execution result semantics.

`packages/shared-contracts/execution-result.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
