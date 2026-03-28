# Observability Event Contract

## Goal
Define a standalone observability event contract without introducing a runtime event bus, tracing backend, metrics engine, or logger implementation.

## Purpose
Observability event contract describes one observable event in the execution, retrieval, or indexing pipeline.

It records one event around pipeline progress, validation, warnings, or failures so future debugging and observability layers can reason about pipeline behavior without changing domain contracts.

This contract is expected to align with:
- `trace_id`
- `embedding_job_id`
- `retrieval_index_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`
- `retrieval_result_id`

## Observability Event Object

```json
{
  "observability_event_id": "observability-event-0001",
  "event_name": "retrieval-index-build-started",
  "event_type": "processing",
  "event_status": "started",
  "created_at": "2026-03-28T09:00:00Z",
  "trace_id": "trace-0001",
  "source_contract": "retrieval-index",
  "source_id": "retrieval-index-0001",
  "stage_name": "index_build",
  "severity": "info",
  "linked_embedding_job_id": "embedding-job-0001",
  "linked_retrieval_index_id": "retrieval-index-0001",
  "linked_knowledge_retrieval_id": "knowledge-retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "linked_retrieval_result_id": "retrieval-result-0001",
  "event_message": "Retrieval index build entered processing stage",
  "event_note": "Initial indexing trace event for future visual debugging"
}
```

## Required Fields
- `observability_event_id`
- `event_name`
- `event_type`
- `event_status`
- `created_at`
- `source_contract`
- `source_id`
- `stage_name`
- `severity`

## Optional Fields
- `trace_id`
- `linked_embedding_job_id`
- `linked_retrieval_index_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `linked_retrieval_result_id`
- `event_message`
- `event_note`

## Field Semantics
### observability_event_id
Unique identifier of the observability event contract.

### event_name
Human-readable event name for debugging, audit, and future visualization use.

### event_type
Contract-level event classification.

Allowed values:
- `state_transition`
- `processing`
- `validation`
- `warning`
- `error`
- `info`

### event_status
Observed execution status for the event.

Allowed values:
- `started`
- `in_progress`
- `completed`
- `failed`
- `skipped`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Optional traceability reference that links the event to a wider pipeline trace.

### source_contract
Name of the source contract that emitted or is represented by the event.

### source_id
Identifier of the source entity behind the event.

### stage_name
Pipeline stage label that localizes where the event occurred.

### severity
Severity classification for future debugging and observability views.

Allowed values:
- `debug`
- `info`
- `warning`
- `error`
- `critical`

### linked_embedding_job_id
Optional reference to a related embedding job.

### linked_retrieval_index_id
Optional reference to a related retrieval index.

### linked_knowledge_retrieval_id
Optional reference to a related knowledge retrieval record.

### linked_retrieval_session_id
Optional reference to a related retrieval session.

### linked_retrieval_result_id
Optional reference to a related retrieval result.

### event_message
Optional short human-readable description of the event.

### event_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Observability events must be suitable for a future Visual Debugger Module.

They do not replace domain contracts and instead reflect events around those contracts.

## Rules
1. `source_contract` stores the name of the contract-source of the event.
2. `source_id` stores the identifier of the source entity.
3. Linked fields are optional references to related embedding, indexing, and retrieval contracts.
4. `event_message`, when present, is a short human-readable event description.
5. `event_note`, when present, is an optional explanation and not executable configuration.
6. The contract captures observability around pipeline execution; it does not become the pipeline runtime itself.

## Boundaries
This is not an event bus implementation.

This is not a tracing backend.

This is not a metrics engine.

This is not a runtime logger implementation.

## Expected Usage
- record pipeline progress step by step
- localize errors and pipeline stalls
- feed a future visual debugging view

## Source Alignment
`docs/specs/observability-event-contract.md` defines observability event semantics for the indexing and retrieval debug layer.

`packages/shared-contracts/observability-event.schema.json` is the machine-readable projection of the same contract.
