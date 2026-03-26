# vendor/paperclip

Эта папка зарезервирована для controlled integration с внешним runtime Paperclip.

## Rules
- Не писать сюда наш основной код.
- Не смешивать сюда bridge layer.
- Не смешивать сюда company-builder logic.
- Любые изменения Paperclip должны идти через upstream policy.
- Любая локальная модификация должна быть отдельно задокументирована.

## Purpose
Использовать Paperclip как внешний runtime engine:
- companies
- tickets
- governance
- budgets
- heartbeats

## Prohibited
- превращать vendor/paperclip в основную рабочую папку нашего проекта
- смешивать сюда Telegram bridge
- смешивать сюда Dashboard code
- писать сюда business logic агентов
