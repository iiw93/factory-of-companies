# Budget Hint Contract

## Goal
Определить единый контракт advisory budget signal для execution request без внедрения budget engine.

## Purpose
Budget hint contract описывает нормализованный объект budget hint.

Он связывает advisory budget signal с `execution-request.budget_hint`, а также с конкретными `trace_id` и `command_id`.

Budget hint является advisory budget signal, а не механизмом принудительного исполнения.

## Budget Hint Object

```json
{
  "budget_hint_id": "budget-0001",
  "trace_id": "trace-0001",
  "command_id": "cmd-0001",
  "budget_amount": 5.0,
  "budget_unit": "usd",
  "created_at": "2026-03-26T00:25:00Z",
  "scope": "request",
  "note": "Soft budget guidance for initial planning pass"
}
```

## Required Fields
- `budget_hint_id`
- `trace_id`
- `command_id`
- `budget_amount`
- `budget_unit`
- `created_at`
- `scope`

## Optional Fields
- `note`

## Field Semantics
### budget_hint_id
Уникальный идентификатор отдельного budget hint.

### trace_id
Ссылка на traceability context, в рамках которого был сформирован budget hint.

### command_id
Ссылка на исходную команду, для которой был сформирован advisory budget signal.

### budget_amount
`budget_amount` является числовой оценкой допустимого лимита.

### budget_unit
`budget_unit` является единицей измерения budget hint.

Допустимые значения:
- `usd`
- `credits`
- `tokens`
- `seconds`

### created_at
Момент создания budget hint в формате ISO 8601 date-time.

### scope
`scope` определяет область применения hint.

Допустимые значения:
- `request`
- `session`
- `project`

### note
`note` является опциональным пояснением.

## Rules
1. Каждый budget hint должен ссылаться на конкретные `trace_id` и `command_id`.
2. Budget hint должен оставаться advisory budget signal, а не budget enforcement механизмом.
3. `budget_amount` фиксирует только числовую оценку допустимого лимита.
4. `budget_unit` фиксирует единицу измерения budget hint и не должен трактоваться как billing settlement record.
5. `scope` определяет только область применения advisory hint.
6. `note`, если передан, должен оставаться кратким пояснением контекста или намерения hint.
7. Связь с `execution-request.budget_hint` должна оставаться концептуально согласованной без внедрения budget engine.

## Boundaries
Этот контракт не является billing engine.

Этот контракт не является governance engine.

Этот контракт не является budget enforcement runtime.

Этот контракт не является accounting system.

## Expected Usage
- advisory planning
- execution-request guidance
- future linkage with governance/budget policy

## Source Alignment
`docs/specs/budget-hint-contract.md` остаётся смысловым источником budget hint semantics.

`packages/shared-contracts/budget-hint.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
