# ADR 0002 — Telegram и Dashboard строятся как отдельный Bridge Layer

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
