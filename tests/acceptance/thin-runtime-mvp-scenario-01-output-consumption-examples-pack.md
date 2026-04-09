# Scenario-01 Output-Consumption Examples Pack (Adapter/Caller Planning-Only)

## Status Note (Guardrail-Only, Non-Authorizing)
This document is historical/planning context only and does not authorize implementation-planning, coding, or execution.

## Scope
This examples pack is scenario-01 only.

- adapter/caller planning aid only
- not implementation authorization
- not a broader platform API
- does not authorize scenario-02, bridge, Telegram, or Web Dashboard work
- does not modify scenario-01 runtime behavior

## Source-Of-Truth Alignment
Examples in this pack are subordinate to:

- `docs/specs/thin-runtime-mvp-scenario.md` (`### Scenario-01 Downstream Consumption Contract (Narrow)`)
- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-caller-fixture-profile.md`
- `tests/runtime/snapshots/thin_runtime_happy_path.snapshot.json`
- `tests/runtime/snapshots/thin_runtime_forced_failure.snapshot.json`
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`

## Example A - Happy-Path Output Consumption

Output slice (illustrative, dynamic fields masked):

```json
{
  "scenario_id": "thin-runtime-mvp-scenario-01",
  "execution_mode": "happy_path",
  "runtime_status": "completed",
  "terminal_stage_name": "retrieval-result-creation",
  "retrieval_session": { "<present>": true },
  "retrieval_result": { "<present>": true },
  "failure_reports": []
}
```

Adapter/caller read pattern (planning example):

```python
def consume_scenario_01_happy(output: dict) -> dict:
    if output["scenario_id"] != "thin-runtime-mvp-scenario-01":
        raise ValueError("unsupported scenario")
    if output["runtime_status"] != "completed":
        raise ValueError("expected completed status")
    if output["retrieval_result"] is None:
        raise ValueError("expected retrieval_result on happy path")
    if output["failure_reports"]:
        raise ValueError("expected no failure_reports on happy path")
    return output["retrieval_result"]
```

## Example B - Forced-Failure Output Consumption

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

Adapter/caller read pattern (planning example):

```python
def consume_scenario_01_forced_failure(output: dict) -> dict:
    if output["scenario_id"] != "thin-runtime-mvp-scenario-01":
        raise ValueError("unsupported scenario")
    if output["runtime_status"] != "failed":
        raise ValueError("expected failed status")
    if output["terminal_stage_name"] != "retrieval-result-creation":
        raise ValueError("unexpected terminal stage")
    if output["retrieval_result"] is not None:
        raise ValueError("retrieval_result must be null on forced_failure")
    if len(output["failure_reports"]) != 1:
        raise ValueError("expected exactly one failure report")
    return output["failure_reports"][0]
```

## Boundary Reminder
- scenario-01 remains the only authoritative implemented runtime path
- this pack is review/planning material only
- these examples do not authorize coding or runtime expansion
