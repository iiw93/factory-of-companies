# ADR 0003 — Local-first inference, RunPod only as burst layer

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
