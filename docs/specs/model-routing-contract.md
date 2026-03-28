# Model Routing Contract

## Goal
Определить отдельный контракт model routing без внедрения runtime router.

## Purpose
Model routing contract описывает решение о выборе model, provider и runtime path для конкретной работы.

Он связывает routing-level reference с `trace_id`, `execution_request_id`, `prompt_package_id`, runtime capability, `priority`, budget hint и timeout policy, чтобы routing choice можно было согласованно привязывать к prompt package, execution intent и будущему observability/audit context.

## Model Routing Object

```json
{
  "model_routing_id": "routing-0001",
  "routing_name": "planner-primary-route",
  "routing_status": "selected",
  "created_at": "2026-03-28T03:10:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "prompt_package_id": "prompt-package-0001",
  "provider_type": "openai",
  "model_class": "reasoning",
  "routing_mode": "fallback",
  "priority_level": "high",
  "linked_budget_hint_id": "budget-hint-0001",
  "linked_timeout_policy_id": "timeout-policy-0001",
  "routing_note": "Routing choice prepared for primary reasoning execution with fallback allowance"
}
```

## Required Fields
- `model_routing_id`
- `routing_name`
- `routing_status`
- `created_at`
- `provider_type`
- `model_class`
- `routing_mode`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `prompt_package_id`
- `priority_level`
- `linked_budget_hint_id`
- `linked_timeout_policy_id`
- `routing_note`

## Field Semantics
### model_routing_id
Уникальный идентификатор model routing contract.

### routing_name
Человекочитаемое имя routing choice.

### routing_status
`routing_status` фиксирует текущее состояние routing decision.

Допустимые значения:
- `draft`
- `selected`
- `applied`
- `superseded`

### created_at
Момент фиксации routing decision в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### prompt_package_id
`prompt_package_id` является опциональной ссылкой на prompt package contract.

### provider_type
`provider_type` фиксирует тип provider или vendor, выбранный для выполнения.

Допустимые значения:
- `local_llm`
- `cloud_llm`
- `openai`
- `other`

### model_class
`model_class` фиксирует нормализованный класс модели, к которому относится routing choice.

Допустимые значения:
- `reasoning`
- `coding`
- `general`
- `embedding`
- `other`

### routing_mode
`routing_mode` фиксирует декларативный режим маршрутизации.

Допустимые значения:
- `local_only`
- `cloud_only`
- `hybrid`
- `fallback`

### priority_level
`priority_level` является опциональным текстовым значением, которое концептуально должно оставаться согласованным с priority contract.

### linked_budget_hint_id
`linked_budget_hint_id` является опциональной ссылкой на budget hint contract.

### linked_timeout_policy_id
`linked_timeout_policy_id` является опциональной ссылкой на timeout policy contract.

### routing_note
`routing_note` является опциональным пояснением.

## Rules
1. Model routing contract должен описывать только формализованное routing choice, а не runtime router implementation.
2. `trace_id`, `execution_request_id` и `prompt_package_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `provider_type`, `model_class` и `routing_mode` должны оставаться нормализованными contract-level descriptors, а не provider SDK configuration.
4. `priority_level`, если передан, должен концептуально совпадать с priority contract.
5. `linked_budget_hint_id` и `linked_timeout_policy_id`, если переданы, используются только как опциональные ссылки.
6. Связь с runtime capability остаётся декларативной и концептуальной: routing choice должен интерпретироваться совместно с runtime capability contract, но не заменяет его.
7. `routing_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime router.

Этот контракт не является inference engine.

Этот контракт не является provider SDK.

Этот контракт не является quota manager.

## Expected Usage
- фиксация routing choice
- linkage between prompt package and actual execution path
- future observability, debugging and policy views

## Source Alignment
`docs/specs/model-routing-contract.md` остаётся смысловым источником model routing semantics.

`packages/shared-contracts/model-routing.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
