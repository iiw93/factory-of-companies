# AGENTS.md

## Purpose
Этот репозиторий предназначен для построения Factory of Companies.

## Global Rules
- Не смешивать runtime, bridge и business logic.
- Не изменять vendor/paperclip напрямую без отдельного ADR и review.
- Любая задача должна иметь:
  - цель
  - ограничения
  - критерии приёмки
  - тестовый план
- Сначала писать тесты или тестовые сценарии, затем код.
- Любое изменение должно обновлять документацию.

## Architecture Boundaries
- vendor/paperclip = внешний runtime
- packages/paperclip-adapter = слой интеграции
- apps/bridge-gateway = вход и выход команд
- packages/company-builder = логика компании агентов
- packages/model-router = выбор модели
- packages/codex-adapter = интеграция с Codex
- packages/deploy-agent = выкладка на сервер

## Testing Policy
- Unit tests for pure logic
- Integration tests for adapters and bridges
- System tests for full workflows
- Acceptance tests for user goals

## Forbidden Changes
- Не встраивать Telegram внутрь Paperclip core
- Не встраивать Dashboard внутрь Paperclip core
- Не деплоить в production без smoke-test
- Не принимать upstream updates без compatibility checks

