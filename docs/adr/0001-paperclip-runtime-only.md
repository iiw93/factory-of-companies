# ADR 0001 — Paperclip используется только как runtime engine

## Status
Accepted

## Context
Проект строит Factory of Companies.
Нужен стабильный runtime для компаний агентов, но нельзя смешивать runtime с пользовательскими каналами и стратегической логикой.

## Decision
Использовать Paperclip только как runtime engine:
- companies
- org charts
- tickets
- heartbeats
- governance
- budgets

Не использовать Paperclip как:
- основной пользовательский интерфейс
- единственный orchestration brain
- место для Telegram/Dashboard bridge
- место для Codex business logic

## Consequences
Плюсы:
- ниже связность
- легче обновлять upstream
- легче тестировать интеграции
- проще заменить или обновить bridge layer

Минусы:
- потребуется отдельный слой adapters и company-builder
