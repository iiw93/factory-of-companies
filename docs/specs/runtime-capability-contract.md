# Runtime Capability Contract

## Goal
Определить отдельный контракт возможностей среды или исполнителя без внедрения runtime capability engine.

## Purpose
Runtime capability contract описывает доступные возможности конкретной среды или исполнителя.

Он связывает capability с `deployment_target_id`, `role_type`, `action_type` и orchestration handoff, чтобы feasibility между target, ролью и типом действия оставалась явной и формализованной.

## Runtime Capability Object

```json
{
  "capability_id": "cap-0001",
  "capability_name": "developer-local-checks",
  "capability_status": "available",
  "created_at": "2026-03-27T14:20:00Z",
  "deployment_target_id": "target-0001",
  "role_type": "developer_agent",
  "supported_action_types": [
    "write_code",
    "run_checks",
    "update_documentation"
  ],
  "supports_local_execution": true,
  "supports_remote_execution": false,
  "supports_file_artifacts": true,
  "supports_deployment": false,
  "supports_validation": true,
  "capability_note": "Local developer runtime supports implementation and validation work without deployment access"
}
```

## Required Fields
- `capability_id`
- `capability_name`
- `capability_status`
- `created_at`
- `role_type`

## Optional Fields
- `deployment_target_id`
- `supported_action_types`
- `supports_local_execution`
- `supports_remote_execution`
- `supports_file_artifacts`
- `supports_deployment`
- `supports_validation`
- `capability_note`

## Field Semantics
### capability_id
Уникальный идентификатор runtime capability.

### capability_name
Человекочитаемое имя capability.

### capability_status
`capability_status` фиксирует текущее состояние capability.

Допустимые значения:
- `available`
- `limited`
- `unavailable`
- `deprecated`

### created_at
Момент фиксации capability в формате ISO 8601 date-time.

### deployment_target_id
`deployment_target_id` является опциональной ссылкой на deployment target contract, если capability относится к конкретной целевой среде.

### role_type
`role_type` определяет логическую роль исполнителя, для которой описывается capability.

Значение `role_type` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### supported_action_types
`supported_action_types` является массивом action types, допустимых для данной capability.

Значения `supported_action_types` должны оставаться согласованными с `docs/specs/action-type-contract.md`.

### supports_local_execution
`supports_local_execution` отражает базовый capability flag локального исполнения.

### supports_remote_execution
`supports_remote_execution` отражает базовый capability flag удалённого исполнения.

### supports_file_artifacts
`supports_file_artifacts` отражает базовый capability flag работы с file artifacts.

### supports_deployment
`supports_deployment` отражает базовый capability flag deployment-oriented работы.

### supports_validation
`supports_validation` отражает базовый capability flag validation-oriented работы.

### capability_note
`capability_note` является опциональным пояснением.

## Rules
1. Runtime capability contract должен описывать доступные возможности среды или исполнителя, а не выполнять orchestration.
2. `deployment_target_id`, если передан, используется только как опциональная ссылка на deployment target contract.
3. `role_type` должен оставаться согласованным с role model.
4. `supported_action_types`, если передан, должен содержать только action types.
5. Булевы поля capability отражают только базовые capability flags.
6. `capability_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime scheduler.

Этот контракт не является worker registry.

Этот контракт не является infra monitoring system.

Этот контракт не является deployment orchestrator.

## Expected Usage
- matching handoff with available capability
- validating role-to-action feasibility
- future linkage with dashboard and orchestration decisions

## Source Alignment
`docs/specs/runtime-capability-contract.md` остаётся смысловым источником runtime capability semantics.

`packages/shared-contracts/runtime-capability.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
