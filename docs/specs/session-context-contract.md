# Session Context Contract

## Goal
Определить единый контракт session context без внедрения runtime session manager.

## Purpose
Session context contract описывает контекст пользовательского взаимодействия.

Он связывает session-level context с `session_id`, `user_id`, `channel` и текущим `trace_id` через `active_trace_id`.

Session context фиксирует нормализованный срез состояния пользовательской сессии и не заменяет traceability envelope.

## Session Context Object

```json
{
  "session_id": "session-001",
  "user_id": "owner-001",
  "channel": "telegram",
  "session_status": "active",
  "created_at": "2026-03-27T00:30:00Z",
  "updated_at": "2026-03-27T00:35:00Z",
  "active_trace_id": "trace-0001",
  "project_id": "project-001",
  "company_id": "factory-main",
  "context_note": "User continues discussing the same project scope"
}
```

## Required Fields
- `session_id`
- `user_id`
- `channel`
- `session_status`
- `created_at`

## Optional Fields
- `updated_at`
- `active_trace_id`
- `project_id`
- `company_id`
- `context_note`

## Field Semantics
### session_id
Уникальный идентификатор пользовательской сессии.

### user_id
Идентификатор пользователя, к которому относится session context.

### channel
`channel` фиксирует Bridge Layer, в рамках которого существует сессия.

Допустимые значения:
- `telegram`
- `dashboard`

### session_status
`session_status` фиксирует текущее состояние session context.

Допустимые значения:
- `active`
- `paused`
- `closed`

### created_at
Момент создания session context в формате ISO 8601 date-time.

### updated_at
`updated_at` является опциональной отметкой последнего обновления session context.

### active_trace_id
`active_trace_id` является опциональной ссылкой на текущий активный trace.

### project_id
`project_id` является опциональной ссылкой на проект, если сессия уже связана с конкретным project context.

### company_id
`company_id` является опциональной ссылкой на компанию, если сессия уже связана с конкретным company context.

### context_note
`context_note` является опциональным пояснением текущего session context.

## Rules
1. Session context должен описывать только контекст пользовательского взаимодействия.
2. `session_id`, `user_id` и `channel` должны удерживать стабильную связь с конкретной пользовательской сессией.
3. `session_status` должен отражать только состояние session context, а не runtime execution state.
4. `active_trace_id`, если передан, указывает на текущий активный trace внутри сессии.
5. `project_id` и `company_id`, если переданы, используются только как контекстные ссылки.
6. `context_note`, если передан, должен оставаться кратким пояснением.
7. Session context должен поддерживать связывание команд и ответов внутри одной сессии без внедрения runtime session management.

## Boundaries
Этот контракт не является runtime session store.

Этот контракт не является chat history database.

Этот контракт не является memory engine.

Этот контракт не является auth system.

## Expected Usage
- связывание команд и ответов внутри одной сессии
- future linkage с Telegram и Dashboard
- observability / debugging / human-in-the-loop

## Source Alignment
`docs/specs/session-context-contract.md` остаётся смысловым источником session context semantics.

`packages/shared-contracts/session-context.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
