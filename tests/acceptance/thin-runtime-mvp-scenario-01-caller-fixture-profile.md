# Scenario-01 Caller Fixture Profile (Review/Planning-Only)

## Status Note (Guardrail-Only, Non-Authorizing)
This document is historical/planning context only and does not authorize implementation-planning, coding, or execution.

## Purpose

Provide a small, consistent caller-fixture reference for scenario-01 review and planning work.
This file is a docs/tests aid only. It does not authorize runtime, bridge, or scenario-02 implementation.

Governing sources:
- `docs/handoff/scenario-01-consumer-handoff-pack.md` (authoritative narrow consumer baseline)
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`

Boundary note:
- bridge-related, external-caller, and scenario-02 sections are out of scope for this file
- this file is a Scenario-01 review/planning aid only
- this file does not authorize bridge, external-caller, or implementation work

## Fixture A - Happy Path Reference Shape

Reference caller request shape:

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "execution_mode": "happy_path",
  "trace_id": "trace-happy-ref-001",
  "source_ref": "source/local/reference-A",
  "query_text": "What is the key result?",
  "embedding_provider_id": "provider-text-reference",
  "caller_context": {
    "review_mode": "fixture_profile"
  }
}
```

Reference response shape:

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "created_at": "<dynamic>",
  "trace_id": "<dynamic>",
  "execution_mode": "happy_path",
  "runtime_status": "completed",
  "terminal_stage_name": "retrieval-result-creation",
  "retrieval_session": { "<session_fields>": "<present>" },
  "retrieval_result": { "<result_fields>": "<present>" },
  "failure_reports": [],
  "observability_events": [ "<optional_review_surface>" ],
  "trace_steps": [ "<optional_review_surface>" ],
  "debug_node_views": [ "<optional_review_surface>" ],
  "pipeline_view": { "<optional_review_surface>": "<present>" },
  "debug_panel": { "<optional_review_surface>": "<present>" }
}
```

## Fixture B - Forced-Failure Reference Shape

Reference caller request shape:

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "execution_mode": "forced_failure",
  "trace_id": "trace-failure-ref-001",
  "source_ref": "source/local/reference-A",
  "query_text": "What is the key result?",
  "caller_context": {
    "review_mode": "fixture_profile"
  }
}
```

Reference response shape:

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "created_at": "<dynamic>",
  "trace_id": "<dynamic>",
  "execution_mode": "forced_failure",
  "runtime_status": "failed",
  "terminal_stage_name": "retrieval-result-creation",
  "retrieval_session": { "<session_fields>": "<present>" },
  "retrieval_result": null,
  "failure_reports": [
    { "<failure_report_fields>": "<single_report_present>" }
  ],
  "observability_events": [ "<optional_review_surface>" ],
  "trace_steps": [ "<optional_review_surface>" ],
  "debug_node_views": [ "<optional_review_surface>" ],
  "pipeline_view": { "<optional_review_surface>": "<present>" },
  "debug_panel": { "<optional_review_surface>": "<present>" }
}
```

## Usage Note

Use these fixtures when:
- reviewing scenario-01 docs/spec wording for caller-side consistency
- planning future scenario-01 caller-side work without opening implementation
- sanity-checking happy-path vs forced-failure expectations in review/handoff sessions

These fixtures are good for:
- stable reference examples of request/response shape at a planning/review level
- preserving scenario-01-only boundaries while discussing external caller consumption

These fixtures do not authorize:
- bridge implementation
- runtime implementation-planning or coding
- scenario-02 work
- Telegram/Dashboard/orchestration behavior

## Scope and Truth Boundaries

- Scenario-01 remains the only authoritative implemented runtime path.
- Dynamic values (`created_at`, `trace_id`, generated ids) are illustrative placeholders only.
- This profile is subordinate to the scenario-01 output-contract and bridge-consumption boundaries in the governing spec.
