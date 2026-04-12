# Owner Identity Contract
## Status Note (Guardrail-Only, Non-Authorizing)
This contract is historical/planning context only and is not evidence of active Telegram, Web Dashboard, or bridge availability.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

This contract does not authorize implementation-planning, coding, execution, deployment, release, or artifact publication.

## Goal
Определить единый контракт owner identity без внедрения auth system, IAM или runtime identity manager.

## Purpose
Owner identity contract описывает идентичность пользователя или владельца в рамках системы.

Он связывает `user_id` и `owner_user_id` с session context, project context, company context и approval action, чтобы user-level identity можно было согласованно использовать между контрактами.

## Owner Identity Object

```json
{
  "user_id": "owner-001",
  "display_name": "Factory Owner",
  "identity_type": "human_owner",
  "created_at": "2026-03-27T01:40:00Z",
  "updated_at": "2026-03-27T01:45:00Z",
  "primary_channel": "telegram",
  "telegram_user_id": "tg-001",
  "dashboard_user_id": "dash-001",
  "default_company_id": "factory-main",
  "default_project_id": "project-001",
  "identity_note": "Primary owner identity for company and project linkage"
}
```

## Required Fields
- `user_id`
- `display_name`
- `identity_type`
- `created_at`
- `primary_channel`

## Optional Fields
- `updated_at`
- `telegram_user_id`
- `dashboard_user_id`
- `default_company_id`
- `default_project_id`
- `identity_note`

## Field Semantics
### user_id
Уникальный идентификатор пользователя внутри системы.

### display_name
Человекочитаемое имя пользователя или владельца.

### identity_type
`identity_type` фиксирует тип identity record.

Допустимые значения:
- `human_owner`
- `human_operator`
- `service_account`

### created_at
Момент создания owner identity в формате ISO 8601 date-time.

### updated_at
`updated_at` является опциональной отметкой последнего обновления owner identity.

### primary_channel
`primary_channel` фиксирует основной канал, с которым связана identity record.

Допустимые значения:
- `telegram`
- `dashboard`
- `system`

### telegram_user_id
`telegram_user_id` является опциональной ссылкой на идентичность пользователя в Telegram.

### dashboard_user_id
`dashboard_user_id` является опциональной ссылкой на идентичность пользователя в Dashboard.

### default_company_id
`default_company_id` является опциональной ссылкой на company context по умолчанию.

### default_project_id
`default_project_id` является опциональной ссылкой на project context по умолчанию.

### identity_note
`identity_note` является опциональным пояснением owner identity.

## Rules
1. Owner identity contract должен описывать только идентичность пользователя или владельца в рамках системы.
2. `user_id` должен использоваться как стабильный идентификатор для связывания session context и approval action.
3. `owner_user_id` в project context и company context должен указывать на `user_id` из owner identity contract.
4. `identity_type` должен отражать тип identity record, а не runtime permission state.
5. `telegram_user_id`, `dashboard_user_id`, `default_company_id` и `default_project_id`, если переданы, используются только как опциональные ссылки.
6. `identity_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является auth system.

Этот контракт не является IAM.

Этот контракт не является permissions engine.

Этот контракт не является runtime access control.

## Expected Usage
- связывание контрактов по `user_id`
- owner linkage для projects и companies
- future linkage с Telegram и Dashboard
- human-in-the-loop traceability

## Source Alignment
`docs/specs/owner-identity-contract.md` остаётся смысловым источником owner identity semantics.

`packages/shared-contracts/owner-identity.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
