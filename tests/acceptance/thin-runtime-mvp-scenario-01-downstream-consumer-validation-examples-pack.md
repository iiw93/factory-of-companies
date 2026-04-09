# Scenario-01 Downstream-Consumer Validation Examples Pack (Compact, Non-Authorizing)

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
- `tests/acceptance/thin-runtime-mvp-scenario-01-runtime-consumer-decision-examples-pack.md`
- `tests/runtime/snapshots/thin_runtime_happy_path.snapshot.json`
- `tests/runtime/snapshots/thin_runtime_forced_failure.snapshot.json`
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`

## Scenario-01 Consumer-Aids Consistency Checklist (Compact)
Use this checklist to compare the current consumer-aids set for terminology and interpretation drift:

- `docs/handoff/scenario-01-consumer-handoff-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-output-consumption-examples-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-runtime-consumer-decision-examples-pack.md`
- `tests/acceptance/thin-runtime-mvp-scenario-01-downstream-consumer-validation-examples-pack.md` (this file)

Checklist (scenario-01 only, reviewer/consumer aid only):

- [ ] Happy-path interpretation is consistent: `execution_mode="happy_path"` with `runtime_status=="completed"`, usable `retrieval_result`, and `failure_reports==[]`.
- [ ] Forced-failure interpretation is consistent: `execution_mode="forced_failure"` with `runtime_status=="failed"`, `terminal_stage_name=="retrieval-result-creation"`, `retrieval_result is None`, and one deterministic failure report.
- [ ] `runtime_status` interpretation is consistent across all consumer aids and remains path-scoped (`completed` happy path, `failed` forced-failure path).
- [ ] `terminal_stage_name` interpretation is consistent and not broadened beyond current frozen scenario-01 truth.
- [ ] `retrieval_result` presence/absence interpretation is consistent and path-scoped (present/usable on happy path, absent/not usable on forced-failure path).
- [ ] `failure_reports` interpretation is consistent and path-scoped (empty on happy path, exactly one report on forced-failure path).
- [ ] Read/use order remains consistent with `docs/handoff/scenario-01-consumer-handoff-pack.md` (`## Recommended Consumer-Aids Read/Use Order`).

Consistency boundary reminder:
- scenario-01 only
- reviewer/consumer aid only
- no implementation authorization
- no broader platform API implied

## Compact Downstream-Consumer Validation Matrix

### Happy-Path Validation Row Set

| Validation Category | Expected Interpretation (Scenario-01 Only) | Downstream Review Action |
| --- | --- | --- |
| Required top-level fields | `scenario_id`, `execution_mode`, `runtime_status`, `terminal_stage_name`, `retrieval_session`, `retrieval_result`, `failure_reports` are present at top level. | Continue happy-path checks only if all required fields are present. |
| Terminal-state interpretation | `runtime_status == "completed"` and terminal stage remains explicit for the same run. | Treat run as terminally successful under the frozen scenario-01 boundary. |
| `retrieval_result` interpretation | `retrieval_result` is present and usable. | Consume `retrieval_result` only within scenario-01 downstream contract. |
| `failure_reports` interpretation | `failure_reports == []`. | Keep failure handling path inactive for this run. |
| Projection/summary interpretation (frozen-only) | Interpret projection/summary state only as terminal alignment from shared runtime exhaust and `thin-runtime-mvp-output-v2` frozen review surface. | Do not infer new projection/runtime semantics beyond frozen review scope. |

### Forced-Failure Validation Row Set

| Validation Category | Expected Interpretation (Scenario-01 Only) | Downstream Review Action |
| --- | --- | --- |
| Required top-level fields | `scenario_id`, `execution_mode`, `runtime_status`, `terminal_stage_name`, `retrieval_session`, `retrieval_result`, `failure_reports` are present at top level. | Continue forced-failure checks only if all required fields are present. |
| Terminal-state interpretation | `runtime_status == "failed"` and `terminal_stage_name == "retrieval-result-creation"`. | Treat run as terminally failed at the approved forced-failure stage. |
| `retrieval_result` interpretation | `retrieval_result is None` / not usable. | Do not run happy-path result consumption. |
| `failure_reports` interpretation | `failure_reports` contains exactly one deterministic failure report. | Route to failure-review handling only. |
| Projection/summary interpretation (frozen-only) | Interpret projection/summary state only as terminal alignment from shared runtime exhaust and `thin-runtime-mvp-output-v2` frozen review surface. | Do not infer new projection/runtime semantics beyond frozen review scope. |

## Example A - Happy-Path Downstream Validation

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

Validation example (downstream boundary aid):

```json
{
  "validation_status": "pass",
  "validation_checks": [
    "scenario_id equals thin-runtime-mvp-scenario-01",
    "runtime_status equals completed",
    "retrieval_result is present",
    "failure_reports is empty"
  ],
  "downstream_boundary_action": "accept output as happy-path-valid under scenario-01 contract"
}
```

## Example B - Forced-Failure Downstream Validation

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

Validation example (downstream boundary aid):

```json
{
  "validation_status": "pass",
  "validation_checks": [
    "scenario_id equals thin-runtime-mvp-scenario-01",
    "runtime_status equals failed",
    "terminal_stage_name equals retrieval-result-creation",
    "retrieval_result is null",
    "failure_reports contains exactly one deterministic failure report"
  ],
  "downstream_boundary_action": "accept output as forced-failure-valid and route to failure-review handling only"
}
```

## Boundary Reminder
- scenario-01 remains the only authoritative implemented runtime path
- this pack is a compact downstream-validation aid only
- this pack does not authorize implementation-planning or coding
- this pack does not expand API/runtime scope
