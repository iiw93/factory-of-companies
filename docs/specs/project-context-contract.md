# Project Context Contract
## Status Note (Guardrail-Only, Non-Authorizing)
This contract is historical/planning context only and is not evidence of active execution, active session runtime, or active trace orchestration.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

This contract does not authorize implementation-planning, coding, execution, deployment, release, or artifact publication.

## Goal
Определить единый контракт project context без внедрения runtime project registry.

## Purpose
Project context contract описывает контекст проекта внутри системы.

Он связывает `project_id` с traceability envelope, session context и execution request, чтобы проектный контекст можно было согласованно использовать между контрактами.

## Project Context Object

```json
{
  "project_id": "project-001",
  "project_name": "Factory of Companies",
  "project_status": "active",
  "created_at": "2026-03-27T01:00:00Z",
  "updated_at": "2026-03-27T01:10:00Z",
  "company_id": "factory-main",
  "active_session_id": "session-001",
  "active_trace_id": "trace-0001",
  "owner_user_id": "owner-001",
  "project_note": "Primary project context for active planning and execution linkage"
}
```

## Required Fields
- `project_id`
- `project_name`
- `project_status`
- `created_at`
- `owner_user_id`

## Optional Fields
- `updated_at`
- `company_id`
- `active_session_id`
- `active_trace_id`
- `project_note`

## Field Semantics
### project_id
Уникальный идентификатор project context.

### project_name
Человекочитаемое имя проекта.

### project_status
`project_status` фиксирует текущее состояние project context.

Допустимые значения:
- `draft`
- `active`
- `paused`
- `archived`

### created_at
Момент создания project context в формате ISO 8601 date-time.

### updated_at
`updated_at` является опциональной отметкой последнего обновления project context.

### company_id
`company_id` является опциональной ссылкой на более широкий контекст компании.

### active_session_id
`active_session_id` является опциональной ссылкой на связанную активную сессию.

### active_trace_id
`active_trace_id` является опциональной ссылкой на связанный активный trace.

### owner_user_id
Идентификатор пользователя, владеющего project context.

### project_note
`project_note` является опциональным пояснением project context.

## Rules
1. Project context должен описывать только контекст проекта внутри системы.
2. `project_id` должен использоваться как стабильный идентификатор для связывания project context с traceability envelope, session context и execution request.
3. `project_status` должен отражать состояние project context, а не runtime execution state.
4. `company_id`, если передан, используется только как ссылка на более широкий company context.
5. `active_session_id` и `active_trace_id`, если переданы, используются только как опциональные ссылки на текущий активный контекст.
6. `project_note`, если передан, должен оставаться кратким пояснением.
7. Project context должен позволять grouping execution and traceability без внедрения runtime project management.

## Boundaries
Этот контракт не является runtime project registry.

Этот контракт не является database model.

Этот контракт не является task board.

Этот контракт не является orchestration engine.

## Expected Usage
- связывание контрактов по `project_id`
- grouping execution and traceability
- future linkage with company builder and dashboard views

## Source Alignment
`docs/specs/project-context-contract.md` остаётся смысловым источником project context semantics.

`packages/shared-contracts/project-context.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
