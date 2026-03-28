# Trace Step Contract

## Goal
Define a standalone trace step contract without introducing a runtime tracer, pipeline engine, scheduler, event bus, or visual debugger UI.

## Purpose
Trace step contract describes one step inside an observable trace or pipeline.

It records one pipeline-level step that can later be used to visualize progress, ordering, blockage points, and linkage to observability events without turning the contract into a runtime implementation.

This contract is expected to align with:
- `trace_id`
- `observability_event_id`
- `embedding_job_id`
- `retrieval_index_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`
- `retrieval_result_id`

## Trace Step Object

```json
{
  "trace_step_id": "trace-step-0001",
  "step_name": "retrieval-index-preparation",
  "step_type": "preparation",
  "step_status": "completed",
  "created_at": "2026-03-28T10:00:00Z",
  "trace_id": "trace-0001",
  "sequence_order": 1,
  "source_contract": "retrieval-index",
  "source_id": "retrieval-index-0001",
  "linked_event_ids": [
    "observability-event-0001",
    "observability-event-0002"
  ],
  "linked_embedding_job_id": "embedding-job-0001",
  "linked_retrieval_index_id": "retrieval-index-0001",
  "linked_knowledge_retrieval_id": "knowledge-retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "linked_retrieval_result_id": "retrieval-result-0001",
  "step_message": "Retrieval index preparation completed",
  "step_note": "Pipeline visualization step prepared for future debugger timeline"
}
```

## Required Fields
- `trace_step_id`
- `step_name`
- `step_type`
- `step_status`
- `created_at`
- `trace_id`
- `sequence_order`
- `source_contract`
- `source_id`

## Optional Fields
- `linked_event_ids`
- `linked_embedding_job_id`
- `linked_retrieval_index_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `linked_retrieval_result_id`
- `step_message`
- `step_note`

## Field Semantics
### trace_step_id
Unique identifier of the trace step contract.

### step_name
Human-readable name of the pipeline step.

### step_type
Contract-level pipeline step classification.

Allowed values:
- `input`
- `preparation`
- `embedding`
- `indexing`
- `retrieval`
- `validation`
- `output`

### step_status
Observed execution status of the step.

Allowed values:
- `pending`
- `ready`
- `running`
- `completed`
- `failed`
- `blocked`
- `skipped`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Reference to the parent trace.

### sequence_order
Integer step ordering inside the trace with minimum value `0`.

### source_contract
Name of the primary source contract behind the step.

### source_id
Identifier of the primary source entity behind the step.

### linked_event_ids
Optional array of references to observability events linked to the step.

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

### step_message
Optional short human-readable description of the step.

### step_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Trace step is the pipeline visualization layer.

Observability event is the event layer around steps.

Trace step and observability event are linked, but they do not replace one another.

## Rules
1. `sequence_order` is an integer with minimum value `0`.
2. `linked_event_ids` is an array of references to observability events.
3. `source_contract` and `source_id` identify the primary entity represented by the step.
4. `step_message`, when present, is a short human-readable description.
5. `step_note`, when present, is an optional explanation and not executable configuration.
6. The contract records pipeline visualization structure and not runtime orchestration behavior.

## Boundaries
This is not a runtime tracer implementation.

This is not a scheduler.

This is not an event bus.

This is not the UI layer of the visualizer.

## Expected Usage
- build a pipeline timeline
- display progress and blockage points
- feed a future Visual Debugger Module

## Source Alignment
`docs/specs/trace-step-contract.md` defines trace step semantics for the future pipeline visualization layer.

`packages/shared-contracts/trace-step.schema.json` is the machine-readable projection of the same contract.
