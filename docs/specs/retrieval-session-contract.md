# Retrieval Session Contract

## Goal
Определить отдельный контракт retrieval session без внедрения runtime retrieval engine.

## Purpose
Retrieval session contract описывает одну завершённую или активную retrieval-сессию.

Он связывает session-level reference с `trace_id`, `execution_request_id`, `context_selection_id`, `knowledge_retrieval_id` и `prompt_package_id`, чтобы retrieval run можно было согласованно привязывать к selection context, retrieval output и downstream prompt preparation.

## Retrieval Session Object

```json
{
  "retrieval_session_id": "retrieval-session-0001",
  "session_name": "planner-context-retrieval-run",
  "session_status": "completed",
  "created_at": "2026-03-28T04:30:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "context_selection_id": "context-selection-0001",
  "linked_knowledge_retrieval_id": "retrieval-0001",
  "linked_prompt_package_id": "prompt-package-0001",
  "selected_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "retrieval_outcome": "sufficient",
  "session_note": "Completed retrieval session prepared for prompt packaging"
}
```

## Required Fields
- `retrieval_session_id`
- `session_name`
- `session_status`
- `created_at`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `context_selection_id`
- `linked_knowledge_retrieval_id`
- `linked_prompt_package_id`
- `selected_source_ids`
- `retrieval_outcome`
- `session_note`

## Field Semantics
### retrieval_session_id
Уникальный идентификатор retrieval session.

### session_name
Человекочитаемое имя retrieval-сессии.

### session_status
`session_status` фиксирует текущее состояние retrieval session.

Допустимые значения:
- `draft`
- `prepared`
- `running`
- `completed`
- `failed`
- `archived`

### created_at
Момент фиксации retrieval session в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### context_selection_id
`context_selection_id` является опциональной ссылкой на context selection contract.

### linked_knowledge_retrieval_id
`linked_knowledge_retrieval_id` является опциональной ссылкой на knowledge retrieval contract.

### linked_prompt_package_id
`linked_prompt_package_id` является опциональной ссылкой на prompt package contract.

### selected_source_ids
`selected_source_ids` является опциональным массивом ссылок на knowledge sources.

### retrieval_outcome
`retrieval_outcome` фиксирует декларативный итог retrieval-сессии.

Допустимые значения:
- `empty`
- `partial`
- `sufficient`
- `superseded`

### session_note
`session_note` является опциональным пояснением.

## Rules
1. Retrieval session contract должен описывать только формализованный факт retrieval run/session, а не runtime retrieval executor.
2. `trace_id`, `execution_request_id`, `context_selection_id`, `linked_knowledge_retrieval_id` и `linked_prompt_package_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `selected_source_ids`, если передан, должен содержать только ссылки на knowledge source contract.
4. `retrieval_outcome`, если передан, должен оставаться декларативным итогом retrieval session, а не runtime ranking logic.
5. `session_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime retrieval executor.

Этот контракт не является vector search engine.

Этот контракт не является memory runtime.

Этот контракт не является connector orchestrator.

## Expected Usage
- фиксировать факт retrieval run/session
- связывать sources, retrieval и prompt preparation
- future observability, audit and debugging views

## Source Alignment
`docs/specs/retrieval-session-contract.md` остаётся смысловым источником retrieval session semantics.

`packages/shared-contracts/retrieval-session.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
