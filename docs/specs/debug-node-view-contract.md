# Debug Node View Contract

## Goal
Define a standalone debug node view contract without introducing a UI renderer, graph engine, dashboard implementation, or runtime state manager.

## Purpose
Debug node view contract describes the state of one visual node in the future Visual Debugger Module.

It provides one node-level representation that can connect domain, observability, trace, and failure diagnostics into a single debugger-facing view without replacing the underlying contracts.

This contract is expected to align with:
- `trace_id`
- `trace_step_id`
- `observability_event_id`
- `failure_report_id`
- `embedding_job_id`
- `retrieval_index_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`
- `retrieval_result_id`

## Debug Node View Object

```json
{
  "debug_node_view_id": "debug-node-view-0001",
  "node_name": "retrieval-index-node",
  "node_type": "index_node",
  "node_status": "active",
  "created_at": "2026-03-28T12:00:00Z",
  "trace_id": "trace-0001",
  "source_contract": "retrieval-index",
  "source_id": "retrieval-index-0001",
  "display_label": "Retrieval Index",
  "sequence_order": 4,
  "linked_trace_step_id": "trace-step-0004",
  "linked_event_ids": [
    "observability-event-0004",
    "observability-event-0005"
  ],
  "linked_failure_report_ids": [
    "failure-report-0001"
  ],
  "linked_embedding_job_id": "embedding-job-0001",
  "linked_retrieval_index_id": "retrieval-index-0001",
  "linked_knowledge_retrieval_id": "knowledge-retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "linked_retrieval_result_id": "retrieval-result-0001",
  "is_current_focus": true,
  "debug_message": "Retrieval index is the current active focus of the trace",
  "debug_note": "Future visual debugger node can highlight this state without changing runtime contracts"
}
```

## Required Fields
- `debug_node_view_id`
- `node_name`
- `node_type`
- `node_status`
- `created_at`
- `trace_id`
- `source_contract`
- `source_id`
- `display_label`
- `sequence_order`
- `is_current_focus`

## Optional Fields
- `linked_trace_step_id`
- `linked_event_ids`
- `linked_failure_report_ids`
- `linked_embedding_job_id`
- `linked_retrieval_index_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `linked_retrieval_result_id`
- `debug_message`
- `debug_note`

## Field Semantics
### debug_node_view_id
Unique identifier of the debug node view contract.

### node_name
Human-readable technical node name for debugging and audit usage.

### node_type
Contract-level visual node classification.

Allowed values:
- `input_node`
- `processing_node`
- `embedding_node`
- `index_node`
- `retrieval_node`
- `validation_node`
- `output_node`
- `failure_node`

### node_status
Observed state of the visual node.

Allowed values:
- `idle`
- `ready`
- `active`
- `completed`
- `failed`
- `blocked`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Reference to the parent trace represented by this node.

### source_contract
Name of the primary source contract behind the node.

### source_id
Identifier of the primary source entity behind the node.

### display_label
Human-readable node label intended for future debugger rendering.

### sequence_order
Integer node order inside the visual trace with minimum value `0`.

### linked_trace_step_id
Optional reference to the related trace step.

### linked_event_ids
Optional array of references to related observability events.

### linked_failure_report_ids
Optional array of references to related failure reports.

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

### is_current_focus
Boolean flag for future highlighting of the active node.

### debug_message
Optional short description of the current node state.

### debug_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Debug node view is a representation layer built on top of domain and observability contracts.

It does not replace trace step, failure report, or observability event contracts.

## Rules
1. `display_label` stores a human-readable node caption.
2. `sequence_order` is an integer with minimum value `0`.
3. `linked_event_ids` is an array of references to observability events.
4. `linked_failure_report_ids` is an array of references to failure reports.
5. `is_current_focus` is a boolean intended for future active-node highlighting.
6. `debug_message`, when present, stores a short description of the current node state.
7. `debug_note`, when present, is an optional explanation and not executable configuration.
8. The contract is a debugger-facing representation and not a runtime state container.

## Boundaries
This is not a UI renderer.

This is not a graph engine.

This is not a dashboard implementation.

This is not a runtime state manager.

## Expected Usage
- form nodes for the future Visual Debugger
- highlight active and problematic parts of the chain
- connect timeline, events, and failures in one representation

## Source Alignment
`docs/specs/debug-node-view-contract.md` defines debug node view semantics for the future Visual Debugger layer.

`packages/shared-contracts/debug-node-view.schema.json` is the machine-readable projection of the same contract.
