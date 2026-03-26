# Shared Contracts Verification

## Purpose
Verification layer нужен для быстрой локальной проверки того, что shared contracts остаются согласованными на базовом структурном уровне.

## Source of Meaning
Docs в `docs/specs` являются смысловым источником контракта.

JSON Schema в `packages/shared-contracts` являются машиночитаемой формализацией этих правил.

Acceptance checklist в `tests/acceptance` проверяет проектные требования на уровне репозитория, а не runtime-исполнение.

## What Is Verified
`scripts/verify_shared_contracts.py` проверяет только базовые, зафиксированные требования:

- наличие `packages/shared-contracts/command.schema.json`
- наличие `packages/shared-contracts/response.schema.json`
- что оба файла содержат валидный JSON
- что `command.schema.json` содержит обязательные поля `command_id`, `channel`, `user_id`, `intent`, `message`, `created_at`
- что `response.schema.json` содержит обязательные поля `response_id`, `command_id`, `channel`, `user_id`, `status`, `message`, `created_at`
- что `command.schema.json` содержит значения `telegram` и `dashboard` в `properties.channel.enum`
- что `command.schema.json` содержит значения `create_project`, `update_project`, `request_status`, `approve_action`, `reject_action`, `ask_question` в `properties.intent.enum`
- что `response.schema.json` содержит значения `accepted`, `rejected`, `requires_approval`, `routed`, `planned`, `executing`, `completed`, `failed`, `cancelled` в `properties.status.enum`

## Verification Boundaries
Эта проверка не является runtime validation.

Эта проверка не является end-to-end test.

Эта проверка не является Telegram/Dashboard integration test.

Скрипт намеренно не проверяет весь schema surface и не подменяет полноценную schema validation на стороне runtime.

## Expected Usage
Скрипт предназначен для локального запуска в репозитории.

Его стоит запускать перед commit, когда изменяются shared contracts или связанные specs/checklists.

В будущем этот же скрипт может быть подключён к CI как минимальная автоматизированная проверка согласованности schema.
