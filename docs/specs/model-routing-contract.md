# Model Routing Contract

## Goal
Определить отдельный контракт model routing без внедрения runtime routing logic, prompt builder, model gateway или policy engine.

## Purpose
Model routing contract описывает зафиксированное routing decision для выбора модели и связанного routing target в рамках конкретного выполнения.

Он связывает routing-level reference с `trace_id`, `execution_request_id`, `prompt_package_id`, `tool_invocation_id`, `role_type` и `action_type`, чтобы routing decision можно было согласованно привязывать к execution context, prompt packaging и audit linkage.

## Model Routing Object

```json
{
  "model_routing_id": "routing-0001",
  "routing_name": "planner-primary-route",
  "routing_status": "prepared",
  "created_at": "2026-03-28T02:20:00Z",
  "routing_target_id": "planner-primary",
  "provider_name": "openai",
  "model_name": "gpt-5.1",
  "routing_mode": "direct",
  "contract_version": "1.0",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "prompt_package_id": "prompt-package-0001",
  "role_type": "planner_agent",
  "action_type": "plan_work",
  "required_capability_ids": [
    "cap-0001"
  ],
  "routing_constraints": [
    "budget-aware",
    "text-only"
  ],
  "fallback_target_ids": [
    "planner-fallback-01",
    "planner-fallback-02"
  ],
  "linked_tool_invocation_id": "tool-0001",
  "routing_note": "Declarative route prepared for planner execution"
}
```

## Required Fields
- `model_routing_id`
- `routing_name`
- `routing_status`
- `created_at`
- `routing_target_id`
- `provider_name`
- `model_name`
- `routing_mode`
- `contract_version`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `prompt_package_id`
- `role_type`
- `action_type`
- `required_capability_ids`
- `routing_constraints`
- `fallback_target_ids`
- `linked_tool_invocation_id`
- `routing_note`

## Field Semantics
### model_routing_id
Уникальный идентификатор model routing contract.

### routing_name
Человекочитаемое имя routing decision.

### routing_status
`routing_status` фиксирует текущее состояние routing decision.

Допустимые значения:
- `draft`
- `prepared`
- `applied`
- `superseded`
- `archived`

### created_at
Момент фиксации model routing contract в формате ISO 8601 date-time.

### routing_target_id
`routing_target_id` фиксирует идентичность выбранного routing target.

### provider_name
`provider_name` фиксирует provider или vendor identity для выбранного route.

### model_name
`model_name` фиксирует идентичность выбранной модели.

### routing_mode
`routing_mode` фиксирует декларативный режим маршрутизации.

Допустимые значения:
- `direct`
- `capability_aware`
- `constraint_aware`
- `fallback_chain`

### contract_version
`contract_version` фиксирует версию контрактного представления routing decision.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### prompt_package_id
`prompt_package_id` является опциональной ссылкой на prompt package contract.

### role_type
`role_type` является опциональной ссылкой на логическую роль исполнителя, для которой зафиксирован route.

Значение `role_type` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### action_type
`action_type` является опциональной ссылкой на нормализованный тип работы, для которого зафиксирован route.

Значение `action_type` должно оставаться согласованным с `docs/specs/action-type-contract.md`.

### required_capability_ids
`required_capability_ids` является опциональным массивом ссылок на runtime capability contracts.

### routing_constraints
`routing_constraints` является опциональным массивом декларативных constraint descriptors.

### fallback_target_ids
`fallback_target_ids` является опциональным упорядоченным массивом routing target identities для fallback chain.

### linked_tool_invocation_id
`linked_tool_invocation_id` является опциональной ссылкой на tool invocation.

### routing_note
`routing_note` является опциональным пояснением.

## Rules
1. Model routing contract должен описывать только формализованное routing decision, а не runtime routing logic.
2. `trace_id`, `execution_request_id`, `prompt_package_id`, `role_type`, `action_type` и `linked_tool_invocation_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `required_capability_ids`, если передан, должен содержать только ссылки на runtime capability contracts.
4. `routing_constraints`, если передан, должен оставаться декларативным набором descriptors, а не executable policy.
5. `fallback_target_ids`, если передан, должен оставаться декларативной ordered fallback chain без встраивания selection logic.
6. `contract_version` должен использоваться только для versionability самого контракта, а не runtime compatibility negotiation.
7. `routing_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime policy engine.

Этот контракт не является routing selection logic.

Этот контракт не является model gateway.

Этот контракт не является inference engine.

## Expected Usage
- фиксация model-routing decision на уровне контракта
- linkage between prompt package and actual execution route
- future dashboard, audit and debugging views

## Source Alignment
`docs/specs/model-routing-contract.md` остаётся смысловым источником model routing semantics.

`packages/shared-contracts/model-routing.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
