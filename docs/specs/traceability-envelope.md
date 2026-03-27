# Traceability Envelope

## Purpose
Traceability envelope фиксирует единый слой корреляции для команды и связанных ответов на протяжении жизненного цикла запроса.

Envelope не заменяет `command` и `response` contracts. Он связывает их и удерживает минимальный набор полей трассировки в одном нормализованном объекте.

## Traceability Fields
- `trace_id`
- `command_id`
- `response_id`
- `session_id`
- `user_id`
- `channel`
- `company_id`
- `project_id`
- `created_at`
- `updated_at`
- `current_state`

## Field Semantics
### trace_id
`trace_id` связывает весь жизненный цикл запроса от исходной команды до связанных ответов и последующих состояний.

### command_id
`command_id` ссылается на исходную команду из bridge command contract.

### response_id
`response_id` ссылается на связанный response, если он уже существует для данного trace context.

### session_id
`session_id` связывает цепочку пользовательского взаимодействия в пределах одного диалога или сценария.

### current_state
`current_state` должен соответствовать состояниям, определённым в `docs/specs/command-state-machine.md` и машиночитаемой проекции `packages/shared-contracts/command-state-rules.json`.

## Boundaries
Этот envelope не является event store.

Этот envelope не является orchestration engine.

Этот envelope не является audit database.

Этот envelope не является runtime execution log.

## Expected Usage
Envelope предназначен для локальной трассировки в репозитории и формальной фиксации correlation между `command` и `response`.

Он также подготавливает базу для future observability, debugging и audit linkage, не вводя runtime implementation.

## Source Alignment
Смысловой источник для статуса и жизненного цикла остаётся в `docs/specs/command-state-machine.md`.

`packages/shared-contracts/traceability-envelope.schema.json` является формальной машиночитаемой проекцией envelope contract и должен оставаться согласованным с docs и state rules.
