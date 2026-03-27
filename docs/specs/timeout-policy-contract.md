# Timeout Policy Contract

## Goal
Определить единый контракт advisory timeout policy для execution request без внедрения runtime timeout enforcement.

## Purpose
Timeout policy contract описывает нормализованный объект timeout policy.

Он связывает advisory ограничения по времени с `execution-request.timeout_seconds`, а также с конкретными `trace_id` и `command_id`.

Timeout policy задаёт advisory ограничения по времени, а не механизм принудительного runtime timeout enforcement.

## Timeout Policy Object

```json
{
  "timeout_policy_id": "timeout-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "timeout_seconds": 300,
  "created_at": "2026-03-27T00:10:00Z",
  "scope": "request",
  "timeout_strategy": "mark_timed_out",
  "note": "Soft timeout guidance for the initial execution request"
}
```

## Required Fields
- `timeout_policy_id`
- `trace_id`
- `command_id`
- `timeout_seconds`
- `created_at`
- `scope`
- `timeout_strategy`

## Optional Fields
- `note`

## Field Semantics
### timeout_policy_id
Уникальный идентификатор отдельного timeout policy.

### trace_id
Ссылка на traceability context, в рамках которого был сформирован timeout policy.

### command_id
Ссылка на исходную команду, для которой был сформирован advisory timeout policy.

### timeout_seconds
`timeout_seconds` является числовым лимитом времени.

### created_at
Момент создания timeout policy в формате ISO 8601 date-time.

### scope
`scope` определяет область применения policy.

Допустимые значения:
- `request`
- `session`
- `project`

### timeout_strategy
`timeout_strategy` определяет рекомендуемую стратегию обработки истечения таймаута.

Допустимые значения:
- `fail`
- `cancel`
- `escalate`
- `mark_timed_out`

### note
`note` является опциональным пояснением.

## Rules
1. Каждый timeout policy должен ссылаться на конкретные `trace_id` и `command_id`.
2. Timeout policy должен оставаться advisory ограничением по времени, а не runtime timeout handler.
3. `timeout_seconds` фиксирует только числовой лимит времени.
4. `scope` определяет только область применения policy.
5. `timeout_strategy` фиксирует только рекомендуемую стратегию обработки истечения таймаута.
6. `note`, если передан, должен оставаться кратким пояснением контекста или намерения policy.
7. Связь с `execution-request.timeout_seconds` должна оставаться концептуально согласованной без внедрения runtime timeout enforcement.
8. Future linkage с `execution_result.outcome = timed_out` допускается только как семантическая связка контракта.

## Boundaries
Этот контракт не является runtime worker timeout handler.

Этот контракт не является scheduler.

Этот контракт не является queue engine.

Этот контракт не является orchestration runtime.

## Expected Usage
- advisory planning
- execution-request guidance
- future linkage with execution_result.outcome = timed_out

## Source Alignment
`docs/specs/timeout-policy-contract.md` остаётся смысловым источником timeout policy semantics.

`packages/shared-contracts/timeout-policy.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
