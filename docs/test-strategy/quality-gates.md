# Quality Gates

## Status Note (Guardrail-Only, Non-Authorizing)
This quality-gates document is historical/planning context and is not evidence that deploy is currently authorized or active.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/specs/thin-runtime-mvp-scenario.md`

Current enforced posture:
- scenario-01 is the only authoritative implemented runtime path
- deploy, scenario-02, bridge, Telegram, Web Dashboard, model-router, Company Builder, and Paperclip integration remain blocked/parked unless explicitly reopened

This document does not authorize implementation-planning, coding, or deploy execution.

## Principle
Ни один важный change не должен проходить без проверок.

## Required Gates
1. Requirement check
2. Acceptance criteria check
3. Test design check
4. Unit tests
5. Integration tests
6. System tests
7. Acceptance tests
8. Documentation update check
9. Smoke deploy check

## Test Levels

### Unit
Проверка чистой логики модулей.

### Integration
Проверка связи между:
- Telegram Bridge
- Dashboard Bridge
- Paperclip Adapter
- Model Router
- Deploy Agent
- Codex Adapter

### System
Полный сценарий:
User request → planning → code → test → deploy → status

### Acceptance
Проверка того, что бизнес-цель пользователя реально достигнута.

## Merge Policy
Запрещено сливать изменения, если:
- нет описания цели
- нет acceptance criteria
- нет тестового плана
- нет обновления документации
- не пройдены обязательные тесты

## Evidence
Для каждой фичи должны сохраняться:
- что требовалось
- какие тесты написаны
- какой результат тестов
- какой commit реализовал изменение
- как обновлена документация
