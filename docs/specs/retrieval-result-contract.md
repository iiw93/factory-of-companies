# Retrieval Result Contract

## Goal
Определить отдельный контракт retrieval result без внедрения runtime retrieval engine.

## Purpose
Retrieval result contract описывает результат завершённого retrieval.

Он связывает result-level reference с `trace_id`, `execution_request_id`, `context_selection_id`, `knowledge_retrieval_id`, `retrieval_session_id`, `prompt_package_id` и `knowledge_source_id`, чтобы завершённый retrieval outcome можно было согласованно привязывать к retrieval session, downstream prompt preparation и source resolution context.

## Retrieval Result Object

```json
{
  "retrieval_result_id": "retrieval-result-0001",
  "result_name": "planner-context-retrieval-result",
  "result_status": "usable",
  "created_at": "2026-03-28T05:10:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "context_selection_id": "context-selection-0001",
  "linked_knowledge_retrieval_id": "retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "linked_prompt_package_id": "prompt-package-0001",
  "resolved_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "result_quality": "high",
  "selected_excerpt_count": 4,
  "result_note": "Retrieval result is suitable for prompt preparation"
}
```

## Required Fields
- `retrieval_result_id`
- `result_name`
- `result_status`
- `created_at`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `context_selection_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `linked_prompt_package_id`
- `resolved_source_ids`
- `result_quality`
- `selected_excerpt_count`
- `result_note`

## Field Semantics
### retrieval_result_id
Уникальный идентификатор retrieval result.

### result_name
Человекочитаемое имя retrieval result.

### result_status
`result_status` фиксирует текущее состояние retrieval result.

Допустимые значения:
- `draft`
- `prepared`
- `usable`
- `insufficient`
- `superseded`
- `archived`

### created_at
Момент фиксации retrieval result в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### context_selection_id
`context_selection_id` является опциональной ссылкой на context selection contract.

### linked_knowledge_retrieval_id
`linked_knowledge_retrieval_id` является опциональной ссылкой на knowledge retrieval contract.

### linked_retrieval_session_id
`linked_retrieval_session_id` является опциональной ссылкой на retrieval session contract.

### linked_prompt_package_id
`linked_prompt_package_id` является опциональной ссылкой на prompt package contract.

### resolved_source_ids
`resolved_source_ids` является массивом ссылок на knowledge sources.

### result_quality
`result_quality` фиксирует декларативную оценку качества retrieval result.

Допустимые значения:
- `low`
- `medium`
- `high`
- `mixed`

### selected_excerpt_count
`selected_excerpt_count` является целым числом и отражает количество отобранных excerpt references в рамках результата.

### result_note
`result_note` является опциональным пояснением.

## Rules
1. Retrieval result contract должен описывать только формализованный результат завершённого retrieval, а не runtime retrieval executor.
2. `trace_id`, `execution_request_id`, `context_selection_id`, `linked_knowledge_retrieval_id`, `linked_retrieval_session_id` и `linked_prompt_package_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `resolved_source_ids`, если передан, должен содержать только ссылки на knowledge source contract.
4. `selected_excerpt_count`, если передан, должен оставаться простым количественным descriptor и не должен встраивать excerpt-selection logic.
5. `result_quality`, если передан, должен оставаться декларативной оценкой результата, а не runtime reranking policy.
6. `result_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime retrieval executor.

Этот контракт не является embedding engine.

Этот контракт не является vector DB.

Этот контракт не является reranker runtime.

## Expected Usage
- фиксировать outcome retrieval
- связывать retrieval session с prompt package
- future audit, observability and debugging views

## Source Alignment
`docs/specs/retrieval-result-contract.md` остаётся смысловым источником retrieval result semantics.

`packages/shared-contracts/retrieval-result.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
