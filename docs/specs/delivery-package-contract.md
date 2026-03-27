# Delivery Package Contract

## Goal
Определить отдельный контракт delivery package без внедрения runtime package manager, deployment engine, storage service или binary registry.

## Purpose
Delivery package contract описывает собранную единицу поставки результата.

Он связывает package-level reference с `project_id`, `trace_id`, `artifact_ids`, `evidence_bundle_id`, `release_decision_id` и `execution_result_id`, чтобы deliverable package можно было согласованно увязывать с артефактами, evidence, release decision и execution linkage.

## Delivery Package Object

```json
{
  "delivery_package_id": "package-0001",
  "package_name": "release-ready-company-context-package",
  "package_status": "approved",
  "created_at": "2026-03-27T12:00:00Z",
  "project_id": "project-001",
  "trace_id": "trace-0001",
  "artifact_ids": [
    "artifact-0001",
    "artifact-0002"
  ],
  "linked_evidence_bundle_id": "bundle-0001",
  "linked_release_decision_id": "release-0001",
  "linked_execution_result_id": "result-0001",
  "package_uri": "deliverables/project-001/release-ready-company-context-package.json",
  "package_note": "Assembled package for approved release-ready artifacts"
}
```

## Required Fields
- `delivery_package_id`
- `package_name`
- `package_status`
- `created_at`

## Optional Fields
- `project_id`
- `trace_id`
- `artifact_ids`
- `linked_evidence_bundle_id`
- `linked_release_decision_id`
- `linked_execution_result_id`
- `package_uri`
- `package_note`

## Field Semantics
### delivery_package_id
Уникальный идентификатор delivery package.

### package_name
Человекочитаемое имя delivery package.

### package_status
`package_status` фиксирует текущее состояние delivery package.

Допустимые значения:
- `draft`
- `assembled`
- `approved`
- `published`
- `archived`

### created_at
Момент фиксации delivery package в формате ISO 8601 date-time.

### project_id
`project_id` является опциональной ссылкой на project context.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### artifact_ids
`artifact_ids` является массивом ссылок на artifacts.

### linked_evidence_bundle_id
`linked_evidence_bundle_id` является опциональной ссылкой на evidence bundle contract.

### linked_release_decision_id
`linked_release_decision_id` является опциональной ссылкой на release decision contract.

### linked_execution_result_id
`linked_execution_result_id` является опциональной ссылкой на execution result contract.

### package_uri
`package_uri` является опциональной строковой ссылкой или путём на пакет.

### package_note
`package_note` является опциональным пояснением.

## Rules
1. Delivery package contract должен описывать собранную единицу поставки результата, а не исполнять deployment или publication runtime.
2. `project_id` и `trace_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `artifact_ids`, если передан, должен содержать только ссылки на artifacts.
4. `linked_evidence_bundle_id`, `linked_release_decision_id` и `linked_execution_result_id`, если переданы, используются только как опциональные ссылки.
5. `package_uri`, если передан, должен использоваться только как строковая ссылка или путь на пакет.
6. `package_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является deployment engine.

Этот контракт не является storage service.

Этот контракт не является release runtime.

Этот контракт не является binary registry.

## Expected Usage
- bundling release-ready artifacts
- linkage between release decision and deliverable package
- future linkage with dashboard, audit and publication flows

## Source Alignment
`docs/specs/delivery-package-contract.md` остаётся смысловым источником delivery package semantics.

`packages/shared-contracts/delivery-package.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
