# Deployment Target Contract

## Goal
Определить отдельный контракт deployment target без внедрения runtime deployment engine, infra manager, secrets manager или environment registry implementation.

## Purpose
Deployment target contract описывает целевую среду поставки результата.

Он связывает deployment target с `delivery_package_id`, `release_decision_id`, `project_id` и `company_id`, чтобы linkage между release, delivery package и целевой средой поставки оставался согласованным и явным.

## Deployment Target Object

```json
{
  "deployment_target_id": "target-0001",
  "target_name": "primary-staging-vm",
  "target_type": "vm",
  "target_status": "ready",
  "created_at": "2026-03-27T12:30:00Z",
  "project_id": "project-001",
  "company_id": "factory-main",
  "linked_delivery_package_id": "package-0001",
  "linked_release_decision_id": "release-0001",
  "environment_name": "staging",
  "target_uri": "ssh://staging.internal.example/vm-01",
  "target_note": "Primary staging deployment target for approved release-ready package"
}
```

## Required Fields
- `deployment_target_id`
- `target_name`
- `target_type`
- `target_status`
- `created_at`

## Optional Fields
- `project_id`
- `company_id`
- `linked_delivery_package_id`
- `linked_release_decision_id`
- `environment_name`
- `target_uri`
- `target_note`

## Field Semantics
### deployment_target_id
Уникальный идентификатор deployment target.

### target_name
Человекочитаемое имя deployment target.

### target_type
`target_type` фиксирует тип целевой среды поставки.

Допустимые значения:
- `local_server`
- `container_host`
- `vm`
- `bare_metal`
- `cloud_service`
- `other`

### target_status
`target_status` фиксирует текущее состояние deployment target.

Допустимые значения:
- `draft`
- `ready`
- `active`
- `paused`
- `retired`

### created_at
Момент фиксации deployment target в формате ISO 8601 date-time.

### project_id
`project_id` является опциональной ссылкой на project context.

### company_id
`company_id` является опциональной ссылкой на company context.

### linked_delivery_package_id
`linked_delivery_package_id` является опциональной ссылкой на delivery package contract.

### linked_release_decision_id
`linked_release_decision_id` является опциональной ссылкой на release decision contract.

### environment_name
`environment_name` фиксирует логическое имя среды поставки.

Допустимые значения:
- `dev`
- `staging`
- `prod`
- `test`
- `other`

### target_uri
`target_uri` является опциональной строковой ссылкой или адресом deployment target.

### target_note
`target_note` является опциональным пояснением.

## Rules
1. Deployment target contract должен описывать целевую среду поставки, а не исполнять deployment.
2. `project_id` и `company_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `linked_delivery_package_id` и `linked_release_decision_id`, если переданы, используются только как опциональные ссылки.
4. `environment_name`, если передан, должен фиксировать только логическую среду поставки.
5. `target_uri`, если передан, должен использоваться только как строковая ссылка или адрес.
6. `target_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является deployment engine.

Этот контракт не является infra-as-code runtime.

Этот контракт не является secrets manager.

Этот контракт не является environment registry implementation.

## Expected Usage
- linkage between release and deployment target
- environment-aware delivery planning
- future dashboard and audit visibility

## Source Alignment
`docs/specs/deployment-target-contract.md` остаётся смысловым источником deployment target semantics.

`packages/shared-contracts/deployment-target.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
