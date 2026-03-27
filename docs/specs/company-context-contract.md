# Company Context Contract

## Goal
Определить единый контракт company context без внедрения runtime company registry.

## Purpose
Company context contract описывает контекст компании внутри Factory of Companies.

Он связывает `company_id` с project context, session context и traceability envelope, чтобы контракты могли согласованно ссылаться на один и тот же company-level context.

## Company Context Object

```json
{
  "company_id": "factory-main",
  "company_name": "Factory of Companies",
  "company_status": "active",
  "created_at": "2026-03-27T01:20:00Z",
  "updated_at": "2026-03-27T01:30:00Z",
  "owner_user_id": "owner-001",
  "active_project_id": "project-001",
  "active_session_id": "session-001",
  "active_trace_id": "trace-0001",
  "company_note": "Primary company context for grouped project and session linkage"
}
```

## Required Fields
- `company_id`
- `company_name`
- `company_status`
- `created_at`
- `owner_user_id`

## Optional Fields
- `updated_at`
- `active_project_id`
- `active_session_id`
- `active_trace_id`
- `company_note`

## Field Semantics
### company_id
Уникальный идентификатор company context.

### company_name
Человекочитаемое имя компании внутри Factory of Companies.

### company_status
`company_status` фиксирует текущее состояние company context.

Допустимые значения:
- `draft`
- `active`
- `paused`
- `archived`

### created_at
Момент создания company context в формате ISO 8601 date-time.

### updated_at
`updated_at` является опциональной отметкой последнего обновления company context.

### owner_user_id
Идентификатор пользователя, владеющего company context.

### active_project_id
`active_project_id` является опциональной ссылкой на активный project context.

### active_session_id
`active_session_id` является опциональной ссылкой на активный session context.

### active_trace_id
`active_trace_id` является опциональной ссылкой на активный traceability envelope.

### company_note
`company_note` является опциональным пояснением company context.

## Rules
1. Company context должен описывать только контекст компании внутри Factory of Companies.
2. `company_id` должен использоваться как стабильный идентификатор для связывания company context с project context, session context и traceability envelope.
3. `company_status` должен отражать состояние company context, а не runtime execution state.
4. `active_project_id`, `active_session_id` и `active_trace_id`, если переданы, используются только как опциональные ссылки на текущий активный контекст.
5. `company_note`, если передан, должен оставаться кратким пояснением.
6. Company context должен поддерживать grouping projects, sessions и traces без внедрения runtime company management.

## Boundaries
Этот контракт не является runtime company registry.

Этот контракт не является org chart implementation.

Этот контракт не является governance engine.

Этот контракт не является database model.

## Expected Usage
- связывание контрактов по `company_id`
- grouping projects, sessions и traces
- future linkage с company builder и dashboard views

## Source Alignment
`docs/specs/company-context-contract.md` остаётся смысловым источником company context semantics.

`packages/shared-contracts/company-context.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
