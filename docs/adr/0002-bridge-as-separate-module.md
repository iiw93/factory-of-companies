# ADR 0002 — Telegram и Dashboard строятся как отдельный Bridge Layer

## Status Note (Guardrail-Only, Non-Authorizing)
This ADR is historical architecture context. `Status: Accepted` in this ADR is not the canonical source of current runtime or approval status.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

Current enforced posture:
- scenario-01 is the only authoritative implemented runtime path
- bridge, Telegram, and Web Dashboard remain blocked/parked unless explicitly reopened

This ADR does not authorize implementation-planning or coding.

## Status
Accepted

## Context
Система должна принимать команды от пользователя через Telegram и Dashboard.
Нельзя смешивать transport layer с runtime engine.

## Decision
Построить Bridge Layer как отдельный модуль:
- apps/bridge-gateway
- apps/telegram-bot
- apps/dashboard-web

Bridge Layer отвечает за:
- приём сообщений
- нормализацию команд
- auth/context metadata
- approvals
- маршрутизацию ответов

Bridge Layer не отвечает за:
- бизнес-логику компании агентов
- model routing
- deploy policy
- Paperclip core logic

## Consequences
Плюсы:
- проще масштабировать каналы
- проще тестировать
- проще обновлять runtime
- меньше энтропия архитектуры
