# Knowledge Source Contract

## Goal
Определить отдельный контракт источника знаний без внедрения runtime RAG engine, vector DB, connector runtime или document store.

## Purpose
Knowledge source contract описывает источник знаний или контекста, используемый системой.

Он связывает knowledge-source level reference с `artifact_id`, `trace_id`, `project_id`, `tool_invocation_id` и `evidence_bundle_id`, чтобы knowledge context можно было согласованно привязывать к артефактам, трассировке и evidence-backed flows.

## Knowledge Source Object

```json
{
  "knowledge_source_id": "knowledge-source-0001",
  "source_name": "artifact-reference-spec",
  "source_type": "document",
  "source_status": "available",
  "created_at": "2026-03-27T18:30:00Z",
  "artifact_id": "artifact-0001",
  "trace_id": "trace-0001",
  "project_id": "project-001",
  "linked_tool_invocation_id": "tool-0001",
  "linked_evidence_bundle_id": "bundle-0001",
  "source_uri": "docs/specs/artifact-reference-contract.md",
  "source_note": "Semantic source used for context selection during shared contract verification"
}
```

## Required Fields
- `knowledge_source_id`
- `source_name`
- `source_type`
- `source_status`
- `created_at`

## Optional Fields
- `artifact_id`
- `trace_id`
- `project_id`
- `linked_tool_invocation_id`
- `linked_evidence_bundle_id`
- `source_uri`
- `source_note`

## Field Semantics
### knowledge_source_id
Уникальный идентификатор knowledge source.

### source_name
Человекочитаемое имя источника знаний или контекста.

### source_type
`source_type` фиксирует тип knowledge source.

Допустимые значения:
- `document`
- `repository`
- `file`
- `web_resource`
- `note`
- `other`

### source_status
`source_status` фиксирует текущее состояние knowledge source.

Допустимые значения:
- `draft`
- `available`
- `stale`
- `archived`

### created_at
Момент фиксации knowledge source в формате ISO 8601 date-time.

### artifact_id
`artifact_id` является опциональной ссылкой на artifact reference, если источник знаний связан с конкретным артефактом.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### project_id
`project_id` является опциональной ссылкой на project context.

### linked_tool_invocation_id
`linked_tool_invocation_id` является опциональной ссылкой на tool invocation, если knowledge source был зафиксирован или использован рядом с конкретным вызовом инструмента.

### linked_evidence_bundle_id
`linked_evidence_bundle_id` является опциональной ссылкой на evidence bundle.

### source_uri
`source_uri` является опциональной строковой ссылкой или путём к knowledge source.

### source_note
`source_note` является опциональным пояснением.

## Rules
1. Knowledge source contract должен описывать только источник знаний или контекста, а не retrieval implementation.
2. `artifact_id`, `trace_id`, `project_id`, `linked_tool_invocation_id` и `linked_evidence_bundle_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `source_uri`, если передан, должен оставаться строковой ссылкой или путём без встраивания runtime connector semantics.
4. `source_note`, если передан, должен оставаться кратким пояснением.
5. `source_type` и `source_status` должны описывать источник и его состояние, а не runtime processing stage.

## Boundaries
Этот контракт не является vector DB.

Этот контракт не является connector runtime.

Этот контракт не является retrieval engine.

Этот контракт не является document store.

## Expected Usage
- linking knowledge sources to artifacts and traces
- evidence-backed context selection
- future linkage with RAG, dashboard and audit views

## Source Alignment
`docs/specs/knowledge-source-contract.md` остаётся смысловым источником knowledge source semantics.

`packages/shared-contracts/knowledge-source.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
