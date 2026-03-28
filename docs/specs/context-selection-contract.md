# Context Selection Contract

## Goal
Определить отдельный контракт выбора контекста без внедрения runtime retrieval, RAG engine, vector search service или memory engine.

## Purpose
Context selection contract описывает выбранный набор источников контекста для конкретной работы.

Он связывает selection-level reference с `trace_id`, `execution_request_id`, `knowledge_source_id`, `tool_invocation_id` и `evidence_bundle_id`, чтобы выбранный контекст можно было согласованно привязывать к execution flow, knowledge sources и evidence-backed linkage.

## Context Selection Object

```json
{
  "context_selection_id": "context-selection-0001",
  "selection_name": "verification-context-set",
  "selection_status": "prepared",
  "created_at": "2026-03-28T00:30:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "selected_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "selection_strategy": "evidence_guided",
  "linked_tool_invocation_id": "tool-0001",
  "linked_evidence_bundle_id": "bundle-0001",
  "selection_note": "Prepared context set for shared contracts verification"
}
```

## Required Fields
- `context_selection_id`
- `selection_name`
- `selection_status`
- `created_at`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `selected_source_ids`
- `selection_strategy`
- `linked_tool_invocation_id`
- `linked_evidence_bundle_id`
- `selection_note`

## Field Semantics
### context_selection_id
Уникальный идентификатор context selection.

### selection_name
Человекочитаемое имя выбранного набора контекста.

### selection_status
`selection_status` фиксирует текущее состояние context selection.

Допустимые значения:
- `draft`
- `prepared`
- `applied`
- `superseded`
- `archived`

### created_at
Момент фиксации context selection в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request, если выбор контекста уже привязан к конкретной работе.

### selected_source_ids
`selected_source_ids` является массивом ссылок на knowledge sources.

### selection_strategy
`selection_strategy` фиксирует способ, которым был собран выбранный контекст.

Допустимые значения:
- `manual`
- `rule_based`
- `evidence_guided`
- `hybrid`

### linked_tool_invocation_id
`linked_tool_invocation_id` является опциональной ссылкой на tool invocation, если выбор контекста был зафиксирован рядом с конкретным вызовом инструмента.

### linked_evidence_bundle_id
`linked_evidence_bundle_id` является опциональной ссылкой на evidence bundle.

### selection_note
`selection_note` является опциональным пояснением.

## Rules
1. Context selection contract должен описывать только выбранный набор источников контекста для конкретной работы, а не retrieval implementation.
2. `trace_id`, `execution_request_id`, `linked_tool_invocation_id` и `linked_evidence_bundle_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `selected_source_ids`, если передан, должен содержать только ссылки на knowledge source contract.
4. `selection_strategy`, если передан, должен описывать способ выбора контекста, а не runtime retrieval stage.
5. `selection_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является RAG engine.

Этот контракт не является retrieval runtime.

Этот контракт не является vector search service.

Этот контракт не является memory engine.

## Expected Usage
- фиксация выбранного контекста для execution
- linkage between knowledge sources and actual work
- future dashboard, audit and evidence-aware views

## Source Alignment
`docs/specs/context-selection-contract.md` остаётся смысловым источником context selection semantics.

`packages/shared-contracts/context-selection.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
