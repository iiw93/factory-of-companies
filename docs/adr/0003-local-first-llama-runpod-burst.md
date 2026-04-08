# ADR 0003 — Local-first inference, RunPod only as burst layer

## Status Note (Guardrail-Only, Non-Authorizing)
This ADR is historical architecture context. `Status: Accepted` in this ADR is not the canonical source of current runtime or approval status.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- `docs/specs/thin-runtime-mvp-scenario.md`

Current enforced posture:
- scenario-01 is the only authoritative implemented runtime path
- model-router, scenario-02, bridge, deploy, Telegram, Web Dashboard, Company Builder, and Paperclip integration remain blocked/parked unless explicitly reopened

This ADR does not authorize implementation-planning or coding.

## Status
Accepted

## Context
Проект должен быть управляемым по стоимости, автономности и сложности.
Нужна локальная inference-среда и внешний усилитель для тяжёлых задач.

## Decision
Использовать:
- local llama.cpp как базовый inference layer
- RunPod как burst/cloud layer по policy
- отдельный model-router для выбора провайдера

## Policy
По умолчанию:
- локальная модель

Облако включается только если:
- не хватает контекста
- не хватает качества
- нужна тяжёлая batch/large-model задача
- правило policy это разрешает

## Consequences
Плюсы:
- локальный контроль
- предсказуемые расходы
- независимость от облака
- гибкость расширения

Минусы:
- нужен отдельный router
- нужна отдельная политика budget/approval
