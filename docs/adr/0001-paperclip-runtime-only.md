# ADR 0001 — Paperclip используется только как runtime engine

## Status Note (Guardrail-Only, Non-Authorizing)
This ADR is historical architecture context. `Status: Accepted` in this ADR is not the canonical source of current runtime or approval status.

Mentions of Telegram, Dashboard, or bridge-related architecture in this ADR are not evidence of current availability or approval.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/specs/thin-runtime-mvp-scenario.md`

Current enforced posture:
- scenario-01 is the only authoritative implemented runtime path
- bridge, Telegram, Web Dashboard, scenario-02, deploy, model-router, Company Builder, and Paperclip integration remain blocked/parked unless explicitly reopened

This ADR does not authorize implementation-planning or coding.

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
