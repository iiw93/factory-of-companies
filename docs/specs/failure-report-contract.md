# Failure Report Contract

## Goal
Define a standalone failure report contract without introducing a runtime alerting system, incident manager, pager system, remediation engine, or diagnostic UI.

## Purpose
Failure report contract describes one recorded failure or chain break inside the pipeline.

It aggregates diagnostic information around a detected problem so future debugging and observability layers can localize the breakage point, reason about root cause hypotheses, and preserve failure context without replacing lower-level contracts.

This contract is expected to align with:
- `trace_id`
- `observability_event_id`
- `trace_step_id`
- `embedding_job_id`
- `retrieval_index_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`
- `retrieval_result_id`

## Failure Report Object

```json
{
  "failure_report_id": "failure-report-0001",
  "failure_name": "retrieval-session-chain-break",
  "failure_type": "linkage_error",
  "failure_status": "open",
  "created_at": "2026-03-28T11:00:00Z",
  "trace_id": "trace-0001",
  "severity": "error",
  "source_contract": "retrieval-session",
  "source_id": "retrieval-session-0001",
  "linked_event_id": "observability-event-0003",
  "linked_trace_step_id": "trace-step-0004",
  "linked_embedding_job_id": "embedding-job-0001",
  "linked_retrieval_index_id": "retrieval-index-0001",
  "linked_knowledge_retrieval_id": "knowledge-retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "linked_retrieval_result_id": "retrieval-result-0001",
  "failure_message": "Retrieval session lost linkage to retrieval result",
  "failure_root_cause": "Result contract was not recorded after session completion",
  "requires_manual_review": true,
  "failure_note": "Initial diagnostic report for future visual debugger analysis"
}
```

## Required Fields
- `failure_report_id`
- `failure_name`
- `failure_type`
- `failure_status`
- `created_at`
- `trace_id`
- `severity`
- `source_contract`
- `source_id`
- `failure_message`
- `requires_manual_review`

## Optional Fields
- `linked_event_id`
- `linked_trace_step_id`
- `linked_embedding_job_id`
- `linked_retrieval_index_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `linked_retrieval_result_id`
- `failure_root_cause`
- `failure_note`

## Field Semantics
### failure_report_id
Unique identifier of the failure report contract.

### failure_name
Human-readable name of the recorded failure.

### failure_type
Contract-level failure classification.

Allowed values:
- `validation_error`
- `processing_error`
- `linkage_error`
- `missing_input`
- `timeout`
- `unexpected_state`
- `other`

### failure_status
Lifecycle state of the recorded failure report.

Allowed values:
- `open`
- `triaged`
- `mitigated`
- `resolved`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### trace_id
Reference to the parent trace that contains the failure context.

### severity
Severity classification of the failure report.

Allowed values:
- `warning`
- `error`
- `critical`

### source_contract
Name of the primary problematic contract.

### source_id
Identifier of the primary problematic entity.

### linked_event_id
Optional reference to the related observability event.

### linked_trace_step_id
Optional reference to the related trace step.

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

### failure_message
Short human-readable description of the failure.

### failure_root_cause
Optional string with a root cause hypothesis.

### requires_manual_review
Boolean flag that indicates whether the failure needs human review.

### failure_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Failure report is built on top of observability events and trace steps.

Failure report does not replace event or step contracts and instead aggregates diagnostic information around them.

## Rules
1. `source_contract` and `source_id` identify the primary problematic entity.
2. Linked fields are optional references to related event, step, embedding, indexing, and retrieval contracts.
3. `failure_message` stores a short human-readable failure description.
4. `failure_root_cause`, when present, stores a root cause hypothesis and not a guaranteed diagnosis.
5. `requires_manual_review` is a boolean decision aid for future debugging and triage.
6. `failure_note`, when present, is an optional explanation and not executable configuration.

## Boundaries
This is not an incident manager implementation.

This is not an alert transport.

This is not a pager system.

This is not a remediation engine.

## Expected Usage
- localize the breakage point
- record a root cause hypothesis
- feed the Visual Debugger Module and future diagnostics

## Source Alignment
`docs/specs/failure-report-contract.md` defines failure report semantics for diagnostic aggregation.

`packages/shared-contracts/failure-report.schema.json` is the machine-readable projection of the same contract.
