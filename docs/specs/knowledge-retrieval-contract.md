# Knowledge Retrieval Contract

## Goal
Определить отдельный контракт knowledge retrieval без внедрения search engine, ranking logic, RAG runtime behavior или retrieval policy engine.

## Purpose
Knowledge retrieval contract описывает декларативный результат retrieval/context gathering, который может быть передан дальше в prompt preparation и последующее runtime execution.

Он связывает retrieval-level reference с `trace_id`, `execution_request_id`, `context_selection_id` и `knowledge_source_id`, чтобы retrieval output можно было согласованно привязывать к selection context, query intent и downstream prompt packaging.

## Knowledge Retrieval Object

```json
{
  "knowledge_retrieval_id": "retrieval-0001",
  "contract_version": "1.0",
  "retrieval_status": "finalized",
  "retrieval_mode": "hybrid_search",
  "query_text": "company context and planning constraints",
  "created_at": "2026-03-28T03:10:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "context_selection_id": "context-selection-0001",
  "selected_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "retrieved_artifact_ids": [
    "artifact-0001",
    "artifact-0002"
  ],
  "retrieval_constraints": [
    "project-scoped",
    "evidence-preferred"
  ],
  "ranking_hint": "prefer the most recent verified artifacts first",
  "token_budget_hint": 4000
}
```

## Required Fields
- `knowledge_retrieval_id`
- `contract_version`
- `retrieval_status`
- `retrieval_mode`
- `query_text`
- `created_at`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `context_selection_id`
- `selected_source_ids`
- `retrieved_artifact_ids`
- `retrieval_constraints`
- `ranking_hint`
- `token_budget_hint`

## Field Semantics
### knowledge_retrieval_id
Уникальный идентификатор knowledge retrieval contract.

### contract_version
`contract_version` фиксирует версию контрактного представления retrieval result.

### retrieval_status
`retrieval_status` фиксирует текущее состояние retrieval result.

Допустимые значения:
- `draft`
- `prepared`
- `collected`
- `filtered`
- `finalized`
- `archived`

### retrieval_mode
`retrieval_mode` фиксирует декларативный режим retrieval.

Допустимые значения:
- `direct_lookup`
- `semantic_search`
- `hybrid_search`
- `curated_context`

### query_text
`query_text` фиксирует текст запроса или retrieval intent, на основании которого был собран результат.

### created_at
Момент фиксации knowledge retrieval contract в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### context_selection_id
`context_selection_id` является опциональной ссылкой на context selection contract.

### selected_source_ids
`selected_source_ids` является опциональным массивом ссылок на knowledge sources.

### retrieved_artifact_ids
`retrieved_artifact_ids` является опциональным упорядоченным массивом ссылок на retrieved artifacts.

### retrieval_constraints
`retrieval_constraints` является опциональным массивом декларативных constraint descriptors.

### ranking_hint
`ranking_hint` является опциональным декларативным указанием на желаемый порядок или приоритет retrieval results.

### token_budget_hint
`token_budget_hint` является опциональным hint для ожидаемого token budget downstream prompt preparation.

## Rules
1. Knowledge retrieval contract должен описывать только формализованный результат retrieval/context gathering, а не search engine implementation.
2. `trace_id`, `execution_request_id` и `context_selection_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `selected_source_ids`, если передан, должен содержать только ссылки на knowledge source contract.
4. `retrieved_artifact_ids`, если передан, должен содержать только ссылки на artifact reference contract и оставаться декларативным ordered result set.
5. `retrieval_constraints`, если передан, должен оставаться декларативным набором descriptors, а не executable policy.
6. `ranking_hint`, если передан, должен оставаться текстовым hint, а не ranking logic.
7. `token_budget_hint`, если передан, должен оставаться advisory hint для downstream preparation, а не runtime enforcement rule.
8. `contract_version` должен использоваться только для versionability самого контракта.

## Boundaries
Этот контракт не является search engine.

Этот контракт не является ranking logic.

Этот контракт не является RAG runtime behavior.

Этот контракт не является retrieval policy engine.

## Expected Usage
- фиксация результата retrieval/context gathering на уровне контракта
- linkage between context selection and downstream prompt preparation
- future dashboard, audit and debugging views

## Source Alignment
`docs/specs/knowledge-retrieval-contract.md` остаётся смысловым источником knowledge retrieval semantics.

`packages/shared-contracts/knowledge-retrieval.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
