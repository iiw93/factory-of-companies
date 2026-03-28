# Debug Panel Contract

## Goal
Define a standalone debug panel contract without introducing a UI implementation, frontend component, live websocket panel, or runtime state manager.

## Purpose
Debug panel contract describes one detailed representation of the current focus in the future Visual Debugger Module.

It provides one presentation-oriented detail view that can assemble pipeline, node, step, event, and failure context into a single debugger-facing panel without replacing the underlying contracts.

This contract is expected to align with:
- `trace_id`
- `pipeline_view_id`
- `debug_node_view_id`
- `trace_step_id`
- `observability_event_id`
- `failure_report_id`

## Debug Panel Object

```json
{
  "debug_panel_id": "debug-panel-0001",
  "panel_name": "retrieval-debug-focus-panel",
  "panel_status": "active",
  "created_at": "2026-03-28T14:00:00Z",
  "trace_id": "trace-0001",
  "panel_scope": "failure_focus",
  "linked_pipeline_view_id": "pipeline-view-0001",
  "focused_node_id": "debug-node-view-0002",
  "focused_step_id": "trace-step-0004",
  "focused_event_id": "observability-event-0005",
  "focused_failure_report_id": "failure-report-0001",
  "primary_message": "Retrieval node is the active debugger focus with a linked failure report",
  "secondary_message": "Failure remains unresolved and requires operator review before pipeline recovery",
  "highlight_level": "critical",
  "requires_attention": true,
  "panel_note": "Presentation contract for future inspector and detail-panel rendering"
}
```

## Required Fields
- `debug_panel_id`
- `panel_name`
- `panel_status`
- `created_at`
- `trace_id`
- `panel_scope`
- `linked_pipeline_view_id`
- `primary_message`
- `highlight_level`
- `requires_attention`

## Optional Fields
- `focused_node_id`
- `focused_step_id`
- `focused_event_id`
- `focused_failure_report_id`
- `secondary_message`
- `panel_note`

## Field Semantics
### debug_panel_id
Unique identifier of the debug panel contract.

### panel_name
Human-readable name of the detailed debug panel.

### panel_status
Lifecycle status of the debug panel.

Allowed values:
- `draft`
- `ready`
- `active`
- `degraded`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Reference to the parent trace represented by the panel.

### panel_scope
Logical scope of the current debugger focus.

Allowed values:
- `node_focus`
- `step_focus`
- `failure_focus`
- `pipeline_focus`
- `mixed`

### linked_pipeline_view_id
Required reference to the aggregated `pipeline_view_id` that provides the broader pipeline context for the panel.

### focused_node_id
Optional reference to the focused `debug_node_view_id`.

### focused_step_id
Optional reference to the focused `trace_step_id`.

### focused_event_id
Optional reference to the focused `observability_event_id`.

### focused_failure_report_id
Optional reference to the focused `failure_report_id`.

### primary_message
Required short description of the current state shown by the panel.

### secondary_message
Optional additional description that expands the primary state summary.

### highlight_level
Highlight intensity for future debugger presentation.

Allowed values:
- `normal`
- `attention`
- `warning`
- `critical`

### requires_attention
Boolean flag that indicates whether the panel is signaling a state that requires user attention.

### panel_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Debug panel is a presentation contract built on top of node, step, event, failure, and pipeline views.

Debug panel does not replace the underlying contracts and instead assembles them into a convenient form for analysis.

## Rules
1. `linked_pipeline_view_id` links the panel to the aggregated pipeline view context.
2. `focused_*` fields are optional references to the concrete object that currently owns the debugger focus.
3. `primary_message` stores the mandatory short summary of the current panel state.
4. `secondary_message`, when present, stores optional supporting context.
5. `requires_attention` is a boolean decision aid for future debugger focus and triage.
6. `panel_note`, when present, is an optional explanation and not executable configuration.
7. The contract is a presentation layer and not a runtime orchestration or state container.

## Boundaries
This is not a UI implementation.

This is not a frontend component.

This is not a live websocket panel.

This is not a runtime state manager.

## Expected Usage
- form an inspector or detail panel in the future Visual Debugger
- show the current focus and the importance of the active issue
- connect pipeline overview with detailed diagnostics

## Source Alignment
`docs/specs/debug-panel-contract.md` defines debug panel semantics for the future Visual Debugger detail layer.

`packages/shared-contracts/debug-panel.schema.json` is the machine-readable projection of the same contract.
