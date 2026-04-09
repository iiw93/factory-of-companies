# Scenario-01 Runtime-Consumer Decision Examples Pack (Compact, Non-Authorizing)

## Status Note (Guardrail-Only, Non-Authorizing)
This document is historical/planning context only and does not authorize implementation-planning, coding, or execution.

## Scope
This pack is scenario-01 only.

- reviewer/consumer aid only
- not implementation authorization
- not a broader platform API
- does not authorize Company Builder, Paperclip integration, model-router/provider, deploy, Telegram, Web Dashboard, bridge, or scenario-02 work
- does not modify scenario-01 runtime behavior

## Source-Of-Truth Alignment
Examples in this pack are subordinate to:

- `docs/specs/thin-runtime-mvp-scenario.md` (`### Scenario-01 Downstream Consumption Contract (Narrow)`)
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-output-consumption-examples-pack.md`
- `tests/runtime/snapshots/thin_runtime_happy_path.snapshot.json`
- `tests/runtime/snapshots/thin_runtime_forced_failure.snapshot.json`
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`

## Example A - Happy-Path Decision Reading

Output slice (illustrative, dynamic fields masked):

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "execution_mode": "happy_path",
  "runtime_status": "completed",
  "terminal_stage_name": "retrieval-result-creation",
  "retrieval_result": { "<present>": true },
  "failure_reports": []
}
```

Decision interpretation (consumer/reviewer aid):

```json
{
  "decision_status": "proceed_with_result",
  "decision_basis": [
    "scenario_id is scenario-01",
    "runtime_status is completed",
    "retrieval_result is present",
    "failure_reports is empty"
  ],
  "safe_next_action": "consume retrieval_result under scenario-01 contract only"
}
```

## Example B - Forced-Failure Decision Reading

Output slice (illustrative, dynamic fields masked):

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "execution_mode": "forced_failure",
  "runtime_status": "failed",
  "terminal_stage_name": "retrieval-result-creation",
  "retrieval_session": { "<present>": true },
  "retrieval_result": null,
  "failure_reports": [
    { "<single_failure_report_present>": true }
  ]
}
```

Decision interpretation (consumer/reviewer aid):

```json
{
  "decision_status": "stop_and_review_failure",
  "decision_basis": [
    "scenario_id is scenario-01",
    "runtime_status is failed",
    "terminal_stage_name is retrieval-result-creation",
    "retrieval_result is null",
    "failure_reports contains one deterministic failure report"
  ],
  "safe_next_action": "inspect failure report and trace/observability artifacts only; do not infer new runtime semantics"
}
```

## Boundary Reminder
- scenario-01 remains the only authoritative implemented runtime path
- this pack is a compact decision-reading aid only
- this pack does not authorize implementation-planning or coding
- this pack does not expand API/runtime scope
