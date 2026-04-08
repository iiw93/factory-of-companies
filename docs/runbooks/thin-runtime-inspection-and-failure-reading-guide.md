# Thin Runtime Inspection and Failure Reading Guide

## Scope
This runbook explains how to inspect one `thin-runtime-mvp-scenario-01` runtime result using the currently implemented runtime surface.

It is operational and inspection-oriented:
- no new runtime behavior is defined here
- no scenario expansion is implied
- no dashboard, Telegram, orchestration, or autonomy behavior is covered

## Git/SSH Access Baseline (Windows + Ubuntu)
Purpose:
- capture the current Git/GitHub access model after the SSH recovery
- document safe diagnostics and safe recovery order only
- no runtime, deploy, or scenario behavior changes

Current access state (this session facts):
- Windows repo path: `C:\PAPERCLIP\factory-of-companies`
- GitHub transport mode (Windows): SSH
  - `origin` now uses `git@github.com:iiw93/factory-of-companies.git`
  - prior mode was HTTPS (`https://github.com/iiw93/factory-of-companies.git`)
- Ubuntu repo path: `/home/superp/factory-of-companies`
- GitHub transport mode (Ubuntu): SSH

Incident summary (doc-only):
- Windows GitHub SSH access was repaired by switching the repo `origin` from HTTPS to SSH.

Safe diagnostics (non-destructive):
```powershell
# repo location and current remote
git -C C:\PAPERCLIP\factory-of-companies remote -v

# SSH auth check (no repo changes)
ssh -T git@github.com
```

Safe recovery order (Windows + Ubuntu):
1. Confirm repo path and current `origin` transport (`git remote -v`).
2. Confirm SSH auth to GitHub (`ssh -T git@github.com`).
3. If `origin` is HTTPS, switch to SSH and re-check auth.

Verification commands (non-destructive):
```powershell
git -C C:\PAPERCLIP\factory-of-companies remote -v
ssh -T git@github.com
git -C C:\PAPERCLIP\factory-of-companies fetch --dry-run
```

Destructive commands to avoid (not allowed in this runbook):
- `git reset --hard`
- `git clean -fdx`
- `git push --force`
- any SSH key deletion or rotation

## Scenario-01 Operator Quick-Reference (Compact)
Use this section for fast operator review and handoff consistency.

Scenario scope:
- scenario-01 only (`thin-runtime-mvp-scenario-01`)
- inspection-only guidance
- no runtime expansion and no scenario-02 authorization

Inspect first (order):
1. top-level terminal state:
   - `execution_mode`
   - `runtime_status`
   - `terminal_stage_name`
   - `failure_reports`
2. terminal exhaust:
   - `trace_steps[-1]`
   - `observability_events[-1]`
3. projection terminal summaries:
   - `pipeline_view.terminal_step_name/status`
   - `debug_panel.terminal_step_name/status`
4. path-critical artifacts:
   - `retrieval_session`
   - `retrieval_result`

Happy-path quick checklist:
- `execution_mode == "happy_path"`
- `runtime_status == "completed"`
- `terminal_stage_name == "retrieval-result-creation"`
- `failure_reports == []`
- `retrieval_session` present
- `retrieval_result` present and usable
- `pipeline_view.view_status == "ready"`
- `debug_panel.panel_status == "ready"` and `requires_attention == false`

Forced-failure quick checklist:
- `execution_mode == "forced_failure"`
- `runtime_status == "failed"`
- `terminal_stage_name == "retrieval-result-creation"`
- `len(failure_reports) == 1`
- `retrieval_session` present
- `retrieval_result is None`
- `pipeline_view.view_status == "degraded"`
- `debug_panel.panel_status == "degraded"` and `requires_attention == true`

Terminal helper alignment cues:
- exactly one `trace_step` has `is_terminal_step == true` and it is the final step
- top-level terminal state aligns with terminal trace-step:
  - `terminal_stage_name == trace_steps[-1].step_name`
  - `runtime_status` derived from terminal `step_status`
- terminal trace-step links terminal event id
- projection terminal summaries match terminal trace-step name/status

Snapshot-boundary `v2` cues:
- terminal helper fields are snapshot-pinned at terminal scope
- non-terminal helper values are not snapshot-pinned
- non-terminal helper drift is not a snapshot-boundary failure

## Scenario-01 Guard-Map Quick Card
Use this card to jump from a failing guard area to the most relevant test module and first triage location.

Scope/constraint note:
- scenario-01 only
- inspection/review aid only
- no new runtime semantics
- no scenario-02 authorization

| Guard area | Protects | Main test module(s) | High-level failure meaning | First place to look |
| --- | --- | --- | --- | --- |
| package export + canonical entry point | approved narrow public import surface and entry-point invariants | `tests/runtime/test_thin_runtime_package_exports.py` | export drift or caller entry-path drift | `paperclip_adapter.__init__` exports and runtime entry return surface |
| output snapshots + snapshot-boundary `v2` | stable terminal-scope review boundary and normalized snapshot contract | `tests/runtime/test_thin_runtime_output_snapshots.py` | boundary drift, snapshot contract drift, or normalization drift | normalized snapshot shape and terminal helper pinning logic |
| shape consistency | top-level shape parity and trace/projection field consistency across paths | `tests/runtime/test_thin_runtime_shape_consistency.py` | surface mismatch between happy/failure paths or projection-shape drift | top-level runtime result assembly and projection field mapping |
| linkage + terminal invariants | artifact chain correctness and path-specific terminal-state invariants | `tests/runtime/test_thin_runtime_linkage_invariants.py` | broken artifact linkage or invalid terminal path truth | id linkage fields across source->retrieval chain and failure linkage fields |
| terminal alignment + parity guard | terminal trace/top-level/projection alignment, marker uniqueness, and parity pattern | `tests/runtime/test_thin_runtime_terminal_alignment.py` | terminal summary mismatch, marker ambiguity, or parity model break | terminal trace-step/event linkage and projection terminal summary derivation |
| debug projection guards | projection derivation integrity from shared runtime exhaust | `tests/runtime/test_thin_runtime_debug_projections.py` | projection/view drift or focus/reference mismatch | `debug_node_views`, `pipeline_view`, `debug_panel` derivation from trace/events/failures |
| forced-failure guards | approved deterministic forced-failure behavior and failure-exhaust expectations | `tests/runtime/test_thin_runtime_forced_failure.py` | failure mode drift or non-approved failure-path behavior | forced-failure branch around `retrieval-result-creation` and failure report construction |

Operator usage note:
1. identify the failing guard category first (export, snapshot, linkage, terminal, projection, forced-failure)
2. open the mapped test module and read the failing assertion before inspecting runtime internals
3. validate whether drift is in contract interpretation vs runtime output shape/linkage
4. if multiple categories fail, triage in this order: export -> shape/snapshot -> linkage/terminal -> projection -> forced-failure specifics

## Scenario-01 Review-Commands Mini-Profile
Purpose:
- compact scenario-01 review aid for inspection/review/handoff work
- complements the guard-map quick card with copyable command patterns
- does not define runtime behavior or testing semantics

Command set (minimal and practical):

### 1) Quick orientation (docs first)
Use when: starting review/handoff and re-establishing scenario-01 truth.

```powershell
# spec + runbook + checkpoint
Get-Content docs/specs/thin-runtime-mvp-scenario.md -TotalCount 220
Get-Content docs/runbooks/thin-runtime-inspection-and-failure-reading-guide.md -TotalCount 260
Get-Content docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md -TotalCount 220
```

### 2) Locate scenario-01 runtime guard tests
Use when: confirming which runtime guard modules exist before running focused checks.

```powershell
Get-ChildItem tests/runtime/test_thin_runtime_*.py | Select-Object -ExpandProperty Name
```

### 3) Review after docs-only changes
Use when: validating marker/section presence and avoiding unnecessary full test runs.

```powershell
Select-String -Path docs/runbooks/thin-runtime-inspection-and-failure-reading-guide.md -Pattern "Scenario-01 Guard-Map Quick Card","Scenario-01 Review-Commands Mini-Profile"
Select-String -Path docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md -Pattern "Guard-Map Quick Card"
```

### 4) Focused guard-test runs (scenario-01)
Use when: reviewing runtime/test changes or validating a specific guard area from the guard-map.

```powershell
# targeted examples
python -m unittest tests.runtime.test_thin_runtime_terminal_alignment
python -m unittest tests.runtime.test_thin_runtime_linkage_invariants
python -m unittest tests.runtime.test_thin_runtime_output_snapshots
python -m unittest tests.runtime.test_thin_runtime_package_exports

# narrow full scenario-01 runtime test sweep (when needed)
python -m unittest discover -s tests/runtime -p "test_thin_runtime_*.py"
```

### 5) Targeted inspection when one guard area fails
Use when: one category is in question and you need first-look code/test context.

```powershell
# example: terminal-alignment guard
Get-Content tests/runtime/test_thin_runtime_terminal_alignment.py -TotalCount 220
Get-Content packages/paperclip-adapter/src/paperclip_adapter/thin_runtime.py -TotalCount 320
```

Scope/constraint note:
- scenario-01 only
- review/inspection aid only
- no new runtime semantics
- no scenario-02 authorization
- no new tooling requirement implied

## Scenario-01 Verification Profile Mini-Card
Purpose:
- compact verification profile for common scenario-01 review situations
- reuses existing command surface only (docs + unittest)
- does not authorize runtime expansion or blocked tracks

### Profile A) Quick docs-only verification
Use when: the change is docs/runbook/handoff only and runtime behavior is unchanged.

```powershell
Select-String -Path docs/runbooks/thin-runtime-inspection-and-failure-reading-guide.md -Pattern "Scenario-01 Guard-Map Quick Card","Scenario-01 Review-Commands Mini-Profile","Scenario-01 Verification Profile Mini-Card"
Select-String -Path docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md -Pattern "scenario-01 = implemented runtime truth","scenario-02 = parked planning track","bridge = parked planning track"
```

### Profile B) Quick runtime/test verification
Use when: reviewing scenario-01 runtime/test edits or validating guard behavior after code-adjacent changes.

```powershell
python -m unittest tests.runtime.test_thin_runtime_package_exports
python -m unittest tests.runtime.test_thin_runtime_linkage_invariants
python -m unittest tests.runtime.test_thin_runtime_forced_failure
```

### Profile C) Snapshot/alignment-focused verification
Use when: checking output-shape snapshots and terminal-alignment expectations.

```powershell
python -m unittest tests.runtime.test_thin_runtime_output_snapshots
python -m unittest tests.runtime.test_thin_runtime_terminal_alignment
```

Scope/constraint note:
- scenario-01 only
- review/verification aid only
- no bridge authorization
- no scenario-02 authorization
- planning completion does not authorize implementation

## Source Of Truth
Use implemented runtime output and runtime tests as source of truth:
- `packages/paperclip-adapter/src/paperclip_adapter/thin_runtime.py`
- `tests/runtime/test_thin_runtime_source_intake.py`
- `tests/runtime/test_thin_runtime_forced_failure.py`
- `tests/runtime/test_thin_runtime_debug_projections.py`
- `tests/runtime/test_thin_runtime_shape_consistency.py`
- `tests/runtime/test_thin_runtime_output_snapshots.py`
- `tests/runtime/test_thin_runtime_linkage_invariants.py`
- `tests/runtime/test_thin_runtime_terminal_alignment.py`

If this runbook and tests disagree, treat tests/runtime output as authoritative and update this document.

## Thin Runtime Output Anatomy
Inspect these top-level fields first:

1. `created_at`
2. `scenario_id`
3. `trace_id`
4. `execution_mode`
5. `runtime_status`
6. `terminal_stage_name`
7. `failure_reports`

Then inspect the emitted runtime exhaust and derived projections:
- `observability_events`
- `trace_steps`
- `debug_node_views`
- `pipeline_view`
- `debug_panel`

Then inspect core artifacts:
- `knowledge_source`
- `normalized_source`
- `embedding_provider`
- `embedding_job`
- `embedding_output`
- `retrieval_index`
- `knowledge_retrieval`
- `retrieval_session`
- `retrieval_result`

### Top-Level State Rules
- `runtime_status` is derived from terminal trace-step status.
- `terminal_stage_name` is derived from the terminal trace-step `step_name`.
- `failure_reports` is `[]` on happy path and non-empty on forced failure.

## Trace Readability Notes
These fields improve inspection readability only:
- `trace_step.step_display_name`
- `trace_step.is_terminal_step`

How to read them:
- `step_display_name` is a display helper derived from `step_name` (for example, `retrieval-result-creation` -> `Retrieval Result Creation`).
- `is_terminal_step` is true only for the last emitted step in the current trace path.
- These fields do not change stage ordering, terminal semantics, or linkage rules.

Terminal truth still comes from emitted runtime exhaust:
- terminal order is still the actual `trace_steps` sequence
- terminal stage identity is still `trace_steps[-1].step_name`
- top-level terminal alignment is still validated via `runtime_status` and `terminal_stage_name`

### Test-Backed Terminal Helper Alignment
Terminal helper alignment is explicitly test-backed and required in both happy path and forced failure:
- terminal `trace_step.step_name/status` must align with top-level `terminal_stage_name` and derived `runtime_status`
- `pipeline_view.terminal_step_name/status` must match terminal trace-step `step_name/status`
- `debug_panel.terminal_step_name/status` must match terminal trace-step `step_name/status`
- these are terminal-scope inspection guarantees backed by snapshot-boundary `v2` and terminal-alignment tests

Terminal marker uniqueness:
- exactly one trace step should have `is_terminal_step == true`
- that step should be the final emitted trace step

Terminal event linkage:
- terminal trace-step must link terminal observability-event id
- terminal observability-event `stage_name` and `event_status` should align with terminal trace-step stage/status
- these alignment rules are review clarifications only and do not expand runtime behavior

## Artifact Linkage Chain
Read linkage in this exact order:

1. `knowledge_source`
2. `normalized_source`
3. `embedding_provider`
4. `embedding_job`
5. `embedding_output`
6. `retrieval_index`
7. `knowledge_retrieval`
8. `retrieval_session`
9. `retrieval_result` (happy path only)

Use these linkage checks as the baseline:
- `normalized_source.source_contract == "knowledge-source"` and `normalized_source.source_id == knowledge_source.knowledge_source_id`
- `embedding_job.embedding_provider_id == embedding_provider.embedding_provider_id`
- `embedding_job.knowledge_source_ids == [knowledge_source.knowledge_source_id]`
- `embedding_output.embedding_job_id == embedding_job.embedding_job_id`
- `embedding_output.source_id == knowledge_source.knowledge_source_id`
- `embedding_output.text_sha256 == normalized_source.text_sha256`
- `retrieval_index.embedding_provider_id == embedding_provider.embedding_provider_id`
- `retrieval_index.linked_embedding_job_ids == [embedding_job.embedding_job_id]`
- `retrieval_index.knowledge_source_ids == [knowledge_source.knowledge_source_id]`
- `knowledge_retrieval.selected_source_ids == [knowledge_source.knowledge_source_id]`
- `knowledge_retrieval.retrieved_artifact_ids == [normalized_source.normalized_artifact_id]`
- `retrieval_session.linked_knowledge_retrieval_id == knowledge_retrieval.knowledge_retrieval_id`
- `retrieval_session.selected_source_ids == [knowledge_source.knowledge_source_id]`
- happy path only: `retrieval_result.linked_knowledge_retrieval_id == knowledge_retrieval.knowledge_retrieval_id`
- happy path only: `retrieval_result.linked_retrieval_session_id == retrieval_session.retrieval_session_id`
- happy path only: `retrieval_result.resolved_source_ids == [knowledge_source.knowledge_source_id]`

Read `next_*_input` handoff objects as cross-stage linkage checkpoints:
- `next_embedding_input` should carry current `trace_id`, `knowledge_source_id`, and `normalized_artifact_id`.
- `next_retrieval_input` should carry current `trace_id`, `knowledge_source_id`, `normalized_artifact_id`, `embedding_provider_id`, `embedding_job_id`, and `retrieval_index_id`.
- `next_retrieval_input.retrieval_query_text` should align with `knowledge_retrieval.query_text`.

Suspicious linkage signals:
- any source id mismatch between `knowledge_source`, `normalized_source`, and retrieval artifacts
- embedding job/provider mismatch
- retrieval index linked to a different embedding job/provider than runtime output shows
- retrieval session not linked to current `knowledge_retrieval`
- happy path retrieval result not linked to current retrieval session/retrieval chain
- `next_*_input` ids that do not match artifacts in the same runtime result

## Happy-Path Inspection
Happy-path trigger:
- `execution_mode="happy_path"` (default path when no override is provided)

Expected terminal state:
- `runtime_status == "completed"`
- `terminal_stage_name == "retrieval-result-creation"`
- `failure_reports == []`

Expected artifact state:
- `retrieval_session` exists
- `retrieval_result` exists and is usable (`result_status == "usable"`)

Expected terminal exhaust:
- terminal `trace_step`:
  - `step_name == "retrieval-result-creation"`
  - `step_display_name == "Retrieval Result Creation"`
  - `step_status == "completed"`
  - `is_terminal_step == true` on the final emitted step only
- terminal `observability_event`:
  - `stage_name == "retrieval_result_creation"`
  - `event_status == "completed"`

Reference integrity checks:
- terminal trace-step `linked_event_ids` includes terminal observability-event id
- `terminal_stage_name == trace_steps[-1].step_name`
- `pipeline_view.terminal_step_name/status` matches `trace_steps[-1].step_name/status`
- `debug_panel.terminal_step_name/status` matches `trace_steps[-1].step_name/status`

## Forced-Failure Linkage Reading
Approved forced-failure trigger:
- `execution_mode="forced_failure"`

Only one deterministic failure mode is approved:
- terminal failure at `retrieval-result-creation`

Expected terminal state:
- `runtime_status == "failed"`
- `terminal_stage_name == "retrieval-result-creation"`
- `failure_reports` contains one `failure-report` record

Expected artifact state:
- `retrieval_session` exists before terminal failure
- no usable `retrieval_result` is produced (`retrieval_result is None`)

Expected terminal exhaust:
- terminal `trace_step`:
  - `step_name == "retrieval-result-creation"`
  - `step_display_name == "Retrieval Result Creation"`
  - `step_status == "failed"`
  - `is_terminal_step == true` on the final emitted step only
- terminal `observability_event`:
  - `stage_name == "retrieval_result_creation"`
  - `event_status == "failed"`
  - error-severity signal is present
- `failure_reports[0]` links terminal event/step ids and retrieval-session context

Required forced-failure linkage checks:
- `failure_report.source_contract == "knowledge-source"`
- `failure_report.source_id == knowledge_source.knowledge_source_id`
- `failure_report.linked_knowledge_retrieval_id == knowledge_retrieval.knowledge_retrieval_id`
- `failure_report.linked_retrieval_session_id == retrieval_session.retrieval_session_id`
- `failure_report.linked_trace_step_id == trace_steps[-1].trace_step_id`
- `failure_report.linked_event_id == observability_events[-1].observability_event_id`

Failure-aware projection checks:
- terminal `debug_node_view` is failure-focused (`node_type == "failure_node"`, `node_status == "failed"`)
- terminal `debug_node_view.linked_failure_report_ids == [failure_report.failure_report_id]`
- `pipeline_view.failure_report_ids == [failure_report.failure_report_id]`
- `pipeline_view.terminal_step_name/status` matches terminal `trace_step` name/status
- `debug_panel.focused_failure_report_id == failure_report.failure_report_id`
- `debug_panel.terminal_step_name/status` matches terminal `trace_step` name/status
- no usable retrieval result is implied:
  - `retrieval_result is None`
  - no terminal failure node should carry `linked_retrieval_result_id`
  - no `debug_node_views` entry should leak `linked_retrieval_result_id` on forced failure

## Terminal Invariant Reading
Interpret terminal invariants by path:

Happy path invariants:
- terminal state is successful (`runtime_status == "completed"`)
- terminal step is `retrieval-result-creation` with completed status
- usable `retrieval_result` exists (`result_status == "usable"`)
- `failure_reports == []`
- projection state is success-aligned:
  - `pipeline_view.view_status == "ready"`
  - `debug_panel.panel_status == "ready"`
  - `debug_panel.requires_attention == false`

Forced failure invariants:
- terminal state is failed (`runtime_status == "failed"`)
- terminal step is `retrieval-result-creation` with failed status
- `retrieval_session` exists before terminal failure
- `retrieval_result is None` (no usable result)
- exactly one `failure_report` exists
- projection state is failure-aligned:
  - `pipeline_view.view_status == "degraded"`
  - `debug_panel.panel_status == "degraded"`
  - `debug_panel.requires_attention == true`

Top-level alignment invariants (both paths):
- `terminal_stage_name == trace_steps[-1].step_name`
- `runtime_status` must match terminal trace-step status (`failed/blocked -> failed`, otherwise completed)
- exactly one terminal trace marker is present (`trace_steps[*].is_terminal_step`)
- terminal trace-step must link terminal observability-event id
- projection terminal summaries must match terminal trace-step:
  - `pipeline_view.terminal_step_name/status`
  - `debug_panel.terminal_step_name/status`
- projection focus should align with terminal step and terminal event

## Projection Inspection
Projections are derived from shared runtime exhaust. They are not a separate debugger state model.

Shared inputs:
- `trace_steps`
- `observability_events`
- optional `failure_reports`

Derived outputs:
- `debug_node_views`
- `pipeline_view`
- `debug_panel`

## Projection Terminal Summary Notes
These fields provide quick terminal-state readability in projections:
- `pipeline_view.terminal_step_name`
- `pipeline_view.terminal_step_status`
- `debug_panel.terminal_step_name`
- `debug_panel.terminal_step_status`

How to read them:
- They mirror terminal trace-step values for quick inspection.
- They are derived summaries only.
- They do not introduce a second state model or change terminal decision logic.
- Any mismatch with terminal trace/event output should be treated as suspicious drift and investigated.

## Snapshot Reading Notes (Boundary v2)
Snapshot boundary `v2` pins terminal readability helpers at terminal scope.

Terminal helper fields included in approved stable snapshots:
- terminal `trace_step.step_display_name`
- terminal `trace_step.is_terminal_step`
- `pipeline_view.terminal_step_name`
- `pipeline_view.terminal_step_status`
- `debug_panel.terminal_step_name`
- `debug_panel.terminal_step_status`

Terminal-scope rule:
- these helpers are snapshot-pinned only as terminal review surface
- pinning does not broaden runtime semantics or stage behavior

Non-terminal rule:
- non-terminal helper values may exist on emitted `trace_steps`
- non-terminal helper values are outside the pinned snapshot boundary in this increment
- review non-terminal helper values via runtime output/tests, not snapshot-value pinning
- drift in non-terminal helper values should not be treated as a snapshot-boundary failure

Happy-path snapshot read:
- terminal helper fields align to `retrieval-result-creation` + completed terminal status
- terminal helper alignment is consistent with usable `retrieval_result`
- non-terminal helper drift does not change boundary-v2 snapshot expectations

Forced-failure snapshot read:
- terminal helper fields align to `retrieval-result-creation` + failed terminal status
- terminal helper alignment is consistent with terminal failure, linked `failure_report`, and absent usable `retrieval_result`
- non-terminal helper drift does not change boundary-v2 snapshot expectations

### Happy Path Projection Read
- `debug_node_views` terminal node is completed and current focus.
- `pipeline_view.view_status == "ready"`.
- `pipeline_view.terminal_step_name == "retrieval-result-creation"`.
- `pipeline_view.terminal_step_status == "completed"`.
- `debug_panel.panel_status == "ready"`.
- `debug_panel.terminal_step_name == "retrieval-result-creation"`.
- `debug_panel.terminal_step_status == "completed"`.
- `debug_panel.requires_attention == false`.

### Forced Failure Projection Read
- terminal debug node is failure-focused (`node_type == "failure_node"`, `node_status == "failed"`).
- `pipeline_view.view_status == "degraded"`.
- `pipeline_view.terminal_step_name == "retrieval-result-creation"`.
- `pipeline_view.terminal_step_status == "failed"`.
- `debug_panel.panel_status == "degraded"`.
- `debug_panel.terminal_step_name == "retrieval-result-creation"`.
- `debug_panel.terminal_step_status == "failed"`.
- `debug_panel.requires_attention == true`.
- failure references resolve through shared ids (event/step/failure report linkage).

## Quick Operator Checklist

### Happy-Path Linkage Review
- [ ] source-to-normalized linkage is correct (`knowledge_source` -> `normalized_source`)
- [ ] embedding linkage is correct (`embedding_provider` -> `embedding_job` -> `embedding_output`)
- [ ] retrieval linkage is correct (`retrieval_index` -> `knowledge_retrieval` -> `retrieval_session` -> `retrieval_result`)
- [ ] `next_embedding_input` and `next_retrieval_input` ids match artifacts in the same runtime result

### Forced-Failure Linkage Review
- [ ] `failure_report` links current source, retrieval chain, terminal trace-step, and terminal event
- [ ] terminal debug node is failure-focused and linked to the same `failure_report`
- [ ] `pipeline_view` and `debug_panel` reference the same `failure_report`
- [ ] no `linked_retrieval_result_id` leakage appears in forced-failure node views

### Terminal Invariant Review (Happy Path)
- [ ] `execution_mode` is `happy_path`
- [ ] `runtime_status` is `completed`
- [ ] `terminal_stage_name` is `retrieval-result-creation`
- [ ] exactly one `trace_step` has `is_terminal_step == true`
- [ ] terminal `trace_step.step_display_name` is the display form of terminal `step_name`
- [ ] `failure_reports` is empty
- [ ] `retrieval_session` exists
- [ ] `retrieval_result` exists and is usable
- [ ] terminal trace-step is completed at `retrieval-result-creation`
- [ ] terminal observability-event is completed at `retrieval_result_creation`
- [ ] `pipeline_view.terminal_step_name/status` matches terminal trace-step `step_name/status`
- [ ] `debug_panel.terminal_step_name/status` matches terminal trace-step `step_name/status`
- [ ] projection statuses are `ready` and do not require attention

### Terminal Invariant Review (Forced Failure)
- [ ] `execution_mode` is `forced_failure`
- [ ] `runtime_status` is `failed`
- [ ] `terminal_stage_name` is `retrieval-result-creation`
- [ ] exactly one `trace_step` has `is_terminal_step == true`
- [ ] terminal `trace_step.step_display_name` is the display form of terminal `step_name`
- [ ] exactly one `failure-report` exists
- [ ] `retrieval_session` exists
- [ ] `retrieval_result` is absent/not usable
- [ ] terminal trace-step is failed at `retrieval-result-creation`
- [ ] terminal observability-event is failed at `retrieval_result_creation`
- [ ] `pipeline_view.terminal_step_name/status` matches terminal trace-step `step_name/status`
- [ ] `debug_panel.terminal_step_name/status` matches terminal trace-step `step_name/status`
- [ ] projections are degraded/failure-aware and reference shared exhaust ids

## Explicit Boundaries And Non-Goals
- readability/usability fields in this runbook are inspection helpers only
- no runtime stage expansion is implied by these fields
- no separate debugger/projection state model is introduced
- one thin scenario only: `thin-runtime-mvp-scenario-01`
- one approved forced-failure mode only
- no retry behavior
- no recovery behavior
- no multi-failure behavior
- projections are derived from shared runtime exhaust, not a separate debugger state model
- no generalized incident framework
- no dashboard/Telegram/bridge behavior in this runbook
- no broader platform semantics should be inferred from this document
