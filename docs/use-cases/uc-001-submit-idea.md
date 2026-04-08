# UC-001 — Пользователь отправляет идею на создание проекта

## Status Note (Guardrail-Only, Non-Authorizing)
This use case is historical/planning context and is not evidence of current availability of Telegram, Dashboard, or Bridge inputs.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/specs/thin-runtime-mvp-scenario.md`

Current enforced posture:
- scenario-01 is the only authoritative implemented runtime path
- bridge, Telegram, and Web Dashboard remain blocked/parked unless explicitly reopened

This document does not authorize implementation-planning or coding.

## Goal
Пользователь должен иметь возможность отправить идею через Telegram или Dashboard и инициировать создание нового проекта.

## Primary Actor
Owner / CEO

## Trigger
Пользователь отправляет сообщение:
"Создай AI SaaS для анализа логов"

## Preconditions
- Bridge Layer доступен
- пользователь аутентифицирован
- система доступна
- контракт команды определён

## Main Flow
1. Пользователь отправляет сообщение через Telegram или Dashboard
2. Bridge Layer принимает сообщение
3. Bridge Layer нормализует сообщение в command contract
4. Bridge Layer валидирует обязательные поля
5. Команда получает command_id
6. Команда передаётся в orchestration layer
7. Система подтверждает приём команды

## Success Result
- команда принята
- команда имеет идентификатор
- команда попала в orchestration pipeline

## Failure Cases
- отсутствует текст команды
- не распознан канал
- отсутствует user_id
- ошибка валидации контракта

## Acceptance Criteria
- одна и та же идея из Telegram и Dashboard превращается в одинаковый command contract
- пустая команда отклоняется
- команда без user_id отклоняется
- корректная команда получает идентификатор и статус accepted
