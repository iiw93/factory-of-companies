# Pipeline View Contract

## Goal
Define a standalone pipeline view contract without introducing a UI implementation, graph renderer, runtime scheduler, or live websocket transport.

## Purpose
Pipeline view contract describes one aggregated pipeline representation for the future Visual Debugger.

It provides one debugger-facing view that aggregates nodes, steps, events, and failures into a single pipeline snapshot without replacing the underlying domain or observability contracts.

This contract is expected to align with:
- `trace_id`
- `trace_step_id`
- `observability_event_id`
- `failure_report_id`
- `debug_node_view_id`

## Pipeline View Object

```json
{
  "pipeline_view_id": "pipeline-view-0001",
  "view_name": "retrieval-debug-pipeline-view",
  "view_status": "active",
  "created_at": "2026-03-28T13:00:00Z",
  "trace_id": "trace-0001",
  "view_scope": "debug_pipeline",
  "node_ids": [
    "debug-node-view-0001",
    "debug-node-view-0002"
  ],
  "step_ids": [
    "trace-step-0003",
    "trace-step-0004"
  ],
  "event_ids": [
    "observability-event-0004",
    "observability-event-0005"
  ],
  "failure_report_ids": [
    "failure-report-0001"
  ],
  "active_node_id": "debug-node-view-0002",
  "active_step_id": "trace-step-0004",
  "summary_message": "Retrieval pipeline is active with one degraded failure-linked node",
  "view_note": "Aggregated pipeline representation for future timeline, graph, and panel views"
}
```

## Required Fields
- `pipeline_view_id`
- `view_name`
- `view_status`
- `created_at`
- `trace_id`
- `view_scope`
- `node_ids`
- `step_ids`
- `event_ids`
- `failure_report_ids`
- `summary_message`

## Optional Fields
- `active_node_id`
- `active_step_id`
- `view_note`

## Field Semantics
### pipeline_view_id
Unique identifier of the pipeline view contract.

### view_name
Human-readable name of the aggregated pipeline view.

### view_status
Lifecycle status of the pipeline view.

Allowed values:
- `draft`
- `ready`
- `active`
- `degraded`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Reference to the parent trace represented by the pipeline view.

### view_scope
Logical scope of the aggregated pipeline representation.

Allowed values:
- `indexing_pipeline`
- `retrieval_pipeline`
- `debug_pipeline`
- `mixed`

### node_ids
Array of references to debug node views included in the pipeline view.

### step_ids
Array of references to trace steps included in the pipeline view.

### event_ids
Array of references to observability events included in the pipeline view.

### failure_report_ids
Array of references to failure reports included in the pipeline view.

### active_node_id
Optional reference to the current focused debug node view.

### active_step_id
Optional reference to the current focused trace step.

### summary_message
Short human-readable description of current pipeline state.

### view_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Pipeline view aggregates nodes, steps, events, and failures.

Pipeline view does not replace domain or observability contracts and is built on top of them.

## Rules
1. `node_ids` is an array of references to debug node views.
2. `step_ids` is an array of references to trace steps.
3. `event_ids` is an array of references to observability events.
4. `failure_report_ids` is an array of references to failure reports.
5. `active_node_id` and `active_step_id`, when present, point to the current debugger focus.
6. `summary_message` stores a short description of the pipeline state.
7. `view_note`, when present, is an optional explanation and not executable configuration.
8. The contract is an aggregated representation layer and not a runtime orchestration object.

## Boundaries
This is not a UI implementation.

This is not a graph renderer.

This is not a runtime scheduler.

This is not a live websocket transport.

## Expected Usage
- assemble a pipeline representation for the Visual Debugger
- show current progress and problematic zones
- provide a foundation for timeline, graph, and panel views

## Source Alignment
`docs/specs/pipeline-view-contract.md` defines pipeline view semantics for the future Visual Debugger aggregation layer.

`packages/shared-contracts/pipeline-view.schema.json` is the machine-readable projection of the same contract.
