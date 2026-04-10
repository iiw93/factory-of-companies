# Acceptance Checklist - Thin Runtime MVP Scenario 01

## Status Note (Guardrail-Only, Non-Authorizing)
This document is historical/planning context only and does not authorize implementation-planning, coding, or execution.

## Acceptance Scope

This checklist defines the acceptance skeleton for the first thin runtime MVP scenario described in `docs/handoff/scenario-01-consumer-handoff-pack.md` and aligned to `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`.

Scope is intentionally narrow:

- one local-first run
- one selected `knowledge-source`
- one explicit retrieval query
- one explicit text-capable `embedding-provider`
- one `happy_path`
- one `forced_failure`
- single-process
- text-first
- contract-shaped artifacts only

This checklist does not add runtime behavior. It defines and refines acceptance expectations that must remain aligned with implemented Paperclip runtime truth.

## Scenario Under Test

- scenario id: `thin-runtime-mvp-scenario-01`
- governing authority pointers:
  - `docs/handoff/scenario-01-consumer-handoff-pack.md`
  - `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- historical traceability note: prior `approved next commit after this refinement` entry (`runtime/tests: tighten contract-shape consistency and fixture discipline`) is historical context only and does not authorize implementation-planning or coding.

- [ ] AC-7100 governing spec exists and explicitly defines `thin-runtime-mvp-scenario-01`

## Shared Fixture Assumptions

- [ ] AC-7101 one deterministic local `knowledge-source` fixture is used per run
- [ ] AC-7102 one explicit text retrieval query string is used per run
- [ ] AC-7103 one explicit text-capable `embedding-provider` is declared per run
- [ ] AC-7104 execution mode is explicit and limited to `happy_path` or `forced_failure`
- [ ] AC-7105 no remote connector, bridge, scheduler, Telegram, dashboard, or multi-agent dependency is required for this scenario
- [ ] AC-7106 no hidden default input is required for successful scenario setup
- [ ] AC-7107 scenario boundaries remain explicit and limited to the approved thin executable flow
- [ ] AC-7108 ordered execution stages remain explicit in the governing spec and this acceptance skeleton
- [ ] AC-7109 runtime ownership remains deferred to Paperclip rather than implemented in this repository

## Stage-to-Assertion Map

| Stage | Future acceptance focus |
| --- | --- |
| source selection | AC-7110, AC-7120, AC-7130 |
| text normalization | AC-7111, AC-7121, AC-7131 |
| embedding provider selection | AC-7112, AC-7122, AC-7132 |
| embedding job creation | AC-7113, AC-7123, AC-7133 |
| retrieval index creation | AC-7114, AC-7124, AC-7134 |
| retrieval execution | AC-7115, AC-7125, AC-7135 |
| retrieval session creation | AC-7116, AC-7126, AC-7136, AC-7162 |
| retrieval result creation | AC-7117, AC-7127, AC-7137, AC-7163 |
| observability-event emission | AC-7140 through AC-7146 |
| trace-step emission | AC-7150 through AC-7156 |
| debug projection eligibility | AC-7170 through AC-7174 |
| controlled failure path | AC-7180 through AC-7189 |
| runtime boundary refinements | AC-7200 through AC-7204 |
| output snapshot drift checks | AC-7210 through AC-7216 |

## Happy-Path Acceptance Cases

- [ ] AC-7110 happy-path run selects exactly one `knowledge-source`
- [ ] AC-7111 happy-path run normalizes the selected source into deterministic text
- [ ] AC-7112 happy-path run selects exactly one text-capable `embedding-provider`
- [ ] AC-7113 happy-path run creates exactly one `embedding-job`
- [ ] AC-7114 happy-path run creates exactly one `retrieval-index`
- [ ] AC-7115 happy-path run executes exactly one `knowledge-retrieval`
- [ ] AC-7116 happy-path run creates exactly one `retrieval-session`
- [ ] AC-7117 happy-path run creates exactly one usable `retrieval-result`
- [ ] AC-7118 happy-path run reports top-level `runtime_status` as `completed`
- [ ] AC-7119 happy-path run reports top-level `terminal_stage_name` as `retrieval-result-creation` and remains local-first, single-process, text-first, and within scenario scope

## Input Acceptance Boundaries

- [ ] AC-7120 exactly one `knowledge-source` is accepted per run
- [ ] AC-7121 selected input must resolve to deterministic text for the approved thin path
- [ ] AC-7122 exactly one explicit `embedding-provider` is accepted per run
- [ ] AC-7123 exactly one explicit retrieval query string is accepted per run
- [ ] AC-7124 accepted inputs remain local-first and do not require remote connector behavior
- [ ] AC-7125 image, audio, video, streaming, and PDF-only paths remain out of scope for this scenario
- [ ] AC-7126 multiple-source and multi-query inputs are rejected or left unsupported for MVP purposes
- [ ] AC-7127 hidden provider fallback and hidden execution branching are not required for scenario completion

## Stage Ordering Acceptance Cases

- [ ] AC-7130 source selection occurs before text normalization
- [ ] AC-7131 text normalization occurs before embedding provider selection
- [ ] AC-7132 embedding provider selection occurs before `embedding-job` creation
- [ ] AC-7133 `embedding-job` creation occurs before `retrieval-index` creation
- [ ] AC-7134 `retrieval-index` creation occurs before `knowledge-retrieval` execution
- [ ] AC-7135 `knowledge-retrieval` execution occurs before `retrieval-session` creation
- [ ] AC-7136 `retrieval-session` creation occurs before successful `retrieval-result` creation on the happy path
- [ ] AC-7137 observability and trace finalization reflect the executed stage order rather than an inferred or reordered path
- [ ] AC-7138 debug projection eligibility is evaluated after the required domain, event, and trace records exist

## Required Outputs and Contract-Shaped Artifact Cases

- [ ] AC-7140 happy-path run records one selected `knowledge-source`
- [ ] AC-7141 happy-path run records one selected `embedding-provider`
- [ ] AC-7142 happy-path run records one created `embedding-job`
- [ ] AC-7143 happy-path run records one created `retrieval-index`
- [ ] AC-7144 happy-path run records one executed `knowledge-retrieval`
- [ ] AC-7145 happy-path run records one created `retrieval-session`
- [ ] AC-7146 happy-path run records one created usable `retrieval-result`
- [ ] AC-7147 `embedding-job` links `embedding_provider_id` and `knowledge_source_ids` as required by the scenario spec
- [ ] AC-7148 `retrieval-index` links `embedding_provider_id`, `linked_embedding_job_ids`, and `knowledge_source_ids` as required by the scenario spec
- [ ] AC-7149 `knowledge-retrieval`, `retrieval-session`, and `retrieval-result` retain the approved contract linkage chain required by the scenario spec

## Observability Acceptance Cases

- [ ] AC-7150 one or more `observability-event` records exist for each executed stage transition
- [ ] AC-7151 `observability-event` coverage includes source selection completed
- [ ] AC-7152 `observability-event` coverage includes text normalization completed
- [ ] AC-7153 `observability-event` coverage includes provider selection completed
- [ ] AC-7154 `observability-event` coverage includes `embedding-job` created and `retrieval-index` created
- [ ] AC-7155 `observability-event` coverage includes `knowledge-retrieval` started and completed on the happy path
- [ ] AC-7156 `observability-event` coverage includes `retrieval-session` created and `retrieval-result` created on the happy path
- [ ] AC-7157 every emitted `observability-event` identifies `source_contract` and `source_id`
- [ ] AC-7158 event sequence is sufficient to localize the stage break point without runtime-only logs

## Traceability Acceptance Cases

- [ ] AC-7160 ordered `trace-step` coverage exists for the executed path
- [ ] AC-7161 trace coverage includes source selection, text normalization, and provider selection
- [ ] AC-7162 trace coverage includes `embedding-job`, `retrieval-index`, `knowledge-retrieval`, and `retrieval-session`
- [ ] AC-7163 trace coverage includes `retrieval-result` on the happy path
- [ ] AC-7164 every `trace-step` carries `trace_id`
- [ ] AC-7165 `sequence_order` reflects actual approved stage order
- [ ] AC-7166 every `trace-step` identifies `source_contract` and `source_id`
- [ ] AC-7167 `trace-step` records link to relevant `observability-event` records where available
- [ ] AC-7168 the executed trace remains reconstructable from `trace_id` plus linked contract ids

## Debug Projection Acceptance Cases

- [ ] AC-7170 happy-path records are sufficient to derive `debug-node-view`
- [ ] AC-7171 happy-path records are sufficient to derive `pipeline-view`
- [ ] AC-7172 happy-path records are sufficient to derive `debug-panel`
- [ ] AC-7173 debugger projections are derivable from formal contracts only
- [ ] AC-7174 projection eligibility does not require dashboard UI, Telegram bridge state, or hidden runtime memory

## Forced Failure Acceptance Cases

- [ ] AC-7180 forced failure is triggered only by `execution_mode="forced_failure"` and reuses the same single thin-scenario shape
- [ ] AC-7181 forced failure terminal stage is `retrieval-result-creation`
- [ ] AC-7182 approved failure point occurs after `retrieval-session` creation and before successful `retrieval-result` completion
- [ ] AC-7183 `retrieval-session` exists on the forced-failure path and `retrieval_result` is not usable (`null` / absent)
- [ ] AC-7184 top-level forced-failure exhaust includes `runtime_status="failed"` and `terminal_stage_name="retrieval-result-creation"`
- [ ] AC-7185 top-level forced-failure exhaust includes `failure_reports` with exactly one `failure-report`
- [ ] AC-7186 terminal forced-failure `observability-event` is explicit and failed (error-severity, terminal-stage visibility)
- [ ] AC-7187 terminal forced-failure `trace-step` is explicit and failed (`step_name="retrieval-result-creation"`, ordered terminal step)
- [ ] AC-7188 earlier successful stages remain intact and inspectable on the forced-failure path
- [ ] AC-7189 forced-failure records remain projection-compatible: degraded `debug-node-view`, `pipeline-view`, and `debug-panel` are derivable from the same runtime exhaust

## Runtime Boundary Refinement Cases

- [ ] AC-7200 exactly one explicit deterministic forced-failure mode is approved for the thin runtime MVP
- [ ] AC-7201 retry behavior, recovery behavior, and multi-failure orchestration are explicitly out of scope for this scenario
- [ ] AC-7202 projections consume shared runtime exhaust (`trace_steps`, `observability_events`, optional `failure_reports`) rather than a separate debugger state model
- [ ] AC-7203 happy-path and forced-failure assertions remain clearly separated in acceptance coverage
- [ ] AC-7204 deferred/non-goal items remain clearly separated from implemented behavior assertions

## Output Snapshot Drift Cases

- [ ] AC-7210 one approved happy-path runtime output snapshot exists for `execution_mode="happy_path"`
- [ ] AC-7211 one approved forced-failure runtime output snapshot exists for `execution_mode="forced_failure"`
- [ ] AC-7212 snapshots pin only the stable review surface (top-level fields, terminal state, required artifact presence/absence, terminal event/step properties including terminal readability helpers, projection terminal alignment including terminal summary helpers)
- [ ] AC-7213 dynamic values (`*_id`, `trace_id`, `created_at`) are normalized and not value-pinned
- [ ] AC-7214 happy-path drift test compares normalized runtime output to the approved happy-path snapshot
- [ ] AC-7215 forced-failure drift test compares normalized runtime output to the approved forced-failure snapshot
- [ ] AC-7216 normalization behavior is explicitly checked so snapshot comparisons stay deterministic and non-brittle

## Acceptance-to-Guard Crosswalk (Scenario-01, review-only)

This crosswalk is historical/planning context only and does not authorize implementation-planning, coding, or execution.
It is a documentation traceability aid that maps existing acceptance ranges to existing runbook guard categories and existing runtime test modules.
It does not modify acceptance assertions, runtime behavior, or pass/fail interpretation.

| AC range(s) | Crosswalk focus | Runbook guard category | Runtime test module pointer(s) |
| --- | --- | --- | --- |
| AC-7100, AC-7108, AC-7130-AC-7138 | scenario identity and ordered stage flow | shape consistency; linkage + terminal invariants | `tests/runtime/test_thin_runtime_shape_consistency.py`; `tests/runtime/test_thin_runtime_linkage_invariants.py` |
| AC-7101-AC-7107, AC-7120-AC-7127 | thin-scope input and fixture boundaries | linkage + terminal invariants; shape consistency | `tests/runtime/test_thin_runtime_linkage_invariants.py`; `tests/runtime/test_thin_runtime_shape_consistency.py` |
| AC-7110-AC-7119, AC-7140-AC-7149 | happy-path artifact presence and linkage chain | linkage + terminal invariants | `tests/runtime/test_thin_runtime_linkage_invariants.py` |
| AC-7150-AC-7158 | observability event coverage and source linkage | debug projection guards; linkage + terminal invariants | `tests/runtime/test_thin_runtime_debug_projections.py`; `tests/runtime/test_thin_runtime_linkage_invariants.py` |
| AC-7160-AC-7168 | ordered trace-step coverage and trace linkage | terminal alignment + parity guard; shape consistency | `tests/runtime/test_thin_runtime_terminal_alignment.py`; `tests/runtime/test_thin_runtime_shape_consistency.py` |
| AC-7170-AC-7174 | projection derivation eligibility from formal contracts | debug projection guards | `tests/runtime/test_thin_runtime_debug_projections.py` |
| AC-7180-AC-7189 | deterministic forced-failure terminal behavior | forced-failure guards; terminal alignment + parity guard | `tests/runtime/test_thin_runtime_forced_failure.py`; `tests/runtime/test_thin_runtime_terminal_alignment.py` |
| AC-7200-AC-7204 | explicit boundary and non-expansion constraints | shape consistency; terminal alignment + parity guard | `tests/runtime/test_thin_runtime_shape_consistency.py`; `tests/runtime/test_thin_runtime_terminal_alignment.py` |
| AC-7210-AC-7216 | snapshot drift and terminal-surface stability checks | output snapshots + snapshot-boundary `v2`; terminal alignment + parity guard | `tests/runtime/test_thin_runtime_output_snapshots.py`; `tests/runtime/test_thin_runtime_terminal_alignment.py` |

## Explicit Non-Goals and Deferred Assertions

- [ ] AC-7190 this acceptance skeleton does not require production runtime implementation in this repository
- [ ] AC-7191 this acceptance skeleton does not broaden beyond one thin text-first scenario
- [ ] AC-7192 this acceptance skeleton does not add Telegram, dashboard, scheduling, autonomy, remote execution, or multi-agent orchestration
- [ ] AC-7193 runtime-backed fixture execution assertions are deferred until Paperclip runtime stubs exist
- [ ] AC-7194 normalized text content assertions are deferred until source intake and normalization stubs exist
- [ ] AC-7195 concrete artifact payload assertions are deferred until runtime can emit contract-shaped records
- [ ] AC-7196 event payload detail assertions are deferred until runtime emits formal `observability-event` records
- [ ] AC-7197 trace payload detail assertions are deferred until runtime emits formal `trace-step` records
- [ ] AC-7198 debugger projection content assertions are deferred until runtime can derive projection records from emitted contracts
- [ ] AC-7199 additional failure payload detail assertions beyond the approved single forced-failure path remain deferred

## Implementation Notes

- This file is the acceptance skeleton for the approved thin runtime MVP scenario only.
- Future runtime commits should satisfy these assertions incrementally without expanding the scenario boundary.
- The next follow-on runtime refinement is contract-shape consistency and fixture-discipline tightening.
