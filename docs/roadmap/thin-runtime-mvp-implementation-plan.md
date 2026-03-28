# Thin Runtime MVP Implementation Plan

## Context
The contract backbone for the knowledge, retrieval, observability, and debugger layers is already in place and verified.

This repository remains responsible for:

- contracts
- specs
- acceptance criteria
- verification rules

The next approved step is to define the first executable thin runtime vertical slice without implementing production runtime in this change.

Ownership remains explicit:

- Paperclip = runtime engine
- Telegram + Dashboard = Bridge Layer
- this repository = contracts, specs, acceptance, and verification

This document is planning-only. It does not add runtime code, bridge code, or debugger UI code.

## Why Now
Thin runtime MVP is the correct next step because the project already has enough verified contract surface to support a narrow execution path.

It should happen now for four reasons:

1. Contracts-first has reached the point where the next useful validation is execution against the existing contract spine rather than more abstract modeling.
2. Observability and debugger contracts already exist, so the first runtime slice can be forced to emit formal observability data from day one.
3. A single thin vertical scenario is the smallest safe way to validate linkage between `knowledge-source`, `embedding-provider`, `embedding-job`, `retrieval-index`, `knowledge-retrieval`, `retrieval-session`, `retrieval-result`, `observability-event`, `trace-step`, `failure-report`, `debug-node-view`, `pipeline-view`, and `debug-panel`.
4. It preserves discipline: no autonomy before observability, no scaling before one verified path, and no runtime generalization before one deterministic local-first scenario works.

## MVP Objective
Define the first executable text-first runtime slice that can run in a local single-process mode and prove that Paperclip can traverse one narrow retrieval flow while producing domain records, observability records, trace structure, debugger projections, and a controlled failure path.

The MVP objective is not broad capability. The objective is one contract-aligned, inspectable, reproducible flow.

## Scope
The thin runtime MVP is explicitly bounded to:

- local-first execution only
- single-process execution only
- one deterministic text-first scenario only
- one `knowledge-source` selection path only
- one `embedding-provider` selection path only
- one `embedding-job` creation path only
- one `retrieval-index` creation path only
- one `knowledge-retrieval` execution path only
- one `retrieval-session` recording path only
- one `retrieval-result` recording path only
- formal emission of `observability-event` and `trace-step`
- debugger-facing projection into `debug-node-view`, `pipeline-view`, and `debug-panel`
- one controlled failure path with `failure-report`

## Non-Goals
This MVP must not include:

- production runtime architecture
- multi-process execution
- distributed queues or workers
- live bridge integration with Telegram or Dashboard
- autonomous planning or self-directed recovery
- multimodal retrieval
- multi-provider orchestration
- reranking systems
- background synchronization
- production vector database infrastructure
- real-time debugger UI
- scaling, throughput, or concurrency optimization
- generalized workflow abstraction beyond the first vertical slice

## First Vertical Scenario
The first executable scenario should be a single deterministic retrieval run over a small local text fixture.

Recommended scenario shape:

1. Choose one `knowledge-source` from a local deterministic sample set.
2. Normalize source text into a stable text-first representation.
3. Choose one `embedding-provider` declared by contract.
4. Create one `embedding-job` for the normalized source.
5. Create one `retrieval-index` from the embedding job output.
6. Execute one `knowledge-retrieval` request against that index.
7. Create one `retrieval-session` that records the run.
8. Create one `retrieval-result` that records the usable or insufficient outcome.
9. Emit `observability-event` records at every meaningful stage transition.
10. Emit ordered `trace-step` records that make the pipeline reconstructable.
11. Produce `debug-node-view`, `pipeline-view`, and `debug-panel` projections from formal contracts only.
12. Support one deliberate controlled failure path that terminates in `failure-report` plus degraded debugger projections.

The vertical slice should remain text-first, deterministic where possible, and small enough to reason about without hidden orchestration.

## Runtime Component Breakdown
The first runtime slice should be built from narrow stub components, not a generalized platform.

Required stub components:

1. Source chooser
   - resolves the target `knowledge-source`
   - rejects unsupported or missing local input early
2. Text normalizer
   - converts the chosen source into stable normalized text
   - keeps normalization deterministic and text-first
3. Embedding provider selector
   - resolves one `embedding-provider`
   - enforces that provider choice is explicit and contract-backed
4. Embedding job recorder
   - creates the `embedding-job`
   - links provider and source identities before downstream work
5. Thin embedding executor stub
   - produces the minimal embedding output needed for the vertical slice
   - stays local-first and replaceable
6. Retrieval index builder stub
   - creates the `retrieval-index`
   - records dimension, modality scope, and record count as available
7. Retrieval executor stub
   - runs one `knowledge-retrieval`
   - returns a minimal deterministic result set
8. Session/result recorder
   - records `retrieval-session` and `retrieval-result`
   - preserves linkage back to retrieval and source identities
9. Observability emitter
   - emits `observability-event` records from the runtime path
   - never bypasses formal contracts
10. Trace assembler
   - emits ordered `trace-step` records
   - links steps to emitted events and source entities
11. Debug projection builder
   - derives `debug-node-view`, `pipeline-view`, and `debug-panel`
   - consumes contracts rather than runtime internals
12. Failure injector
   - triggers one controlled failure mode
   - guarantees `failure-report` coverage for the broken path

## Increment-by-Increment Implementation Plan
Implementation should proceed in strict order and stop after the first complete vertical slice works.

### Increment 1: Define the runtime slice fixture
- Choose the deterministic local sample input for the first `knowledge-source`.
- Fix the expected query text for the first `knowledge-retrieval`.
- Fix the allowed `embedding-provider` choice for the MVP.
- Define the expected happy-path artifact chain and the expected failure-path break.

### Increment 2: Add runtime-facing acceptance skeletons in this repository
- Add acceptance skeletons for the thin runtime happy path.
- Add acceptance skeletons for the controlled failure path.
- Keep them contract-oriented and runtime-agnostic.
- Do not add Paperclip runtime code here.

### Increment 3: Implement minimal Paperclip stubs for source and normalization
- Build the smallest source chooser and text normalizer that can support the fixed sample.
- Keep the input local and deterministic.
- Make normalization output explicit enough to support verification.

### Increment 4: Implement provider selection and `embedding-job` creation
- Resolve one valid `embedding-provider`.
- Create and persist one `embedding-job`.
- Fail fast if provider capability or linkage requirements are not satisfied.

### Increment 5: Implement thin embedding and `retrieval-index` creation
- Run the minimal embedding path required for the sample.
- Create one `retrieval-index`.
- Keep index backend local-first and single-process.

### Increment 6: Implement thin `knowledge-retrieval`
- Execute one retrieval request against the created index.
- Record one `knowledge-retrieval`.
- Keep ranking behavior narrow, explicit, and deterministic where possible.

### Increment 7: Implement `retrieval-session` and `retrieval-result`
- Record the session boundary for the run.
- Record the final result with source linkage and quality state.
- Ensure result creation is impossible without a traceable retrieval chain.

### Increment 8: Implement formal observability and trace emission
- Emit `observability-event` at each stage transition.
- Emit ordered `trace-step` for the whole runtime path.
- Link events and steps back to the domain contracts they describe.

### Increment 9: Implement debugger projections
- Build `debug-node-view` from domain, event, step, and failure data.
- Build `pipeline-view` as the aggregated trace projection.
- Build `debug-panel` as the focused inspection view.
- Ensure projections are derived from formal records, not ad hoc runtime memory.

### Increment 10: Implement the controlled failure path
- Force one known failure at a chosen stage in the same vertical slice.
- Emit failure-oriented `observability-event`.
- Emit blocked or failed `trace-step`.
- Create `failure-report`.
- Produce degraded debugger projections that make the break obvious.

### Increment 11: Verify end-to-end behavior
- Verify happy-path contract creation and linkage.
- Verify failure-path contract creation and linkage.
- Verify debugger projections are reconstructable from formal records.
- Verify the slice remains local-first, single-process, and text-first.

## Observability + Traceability Model
Observability is not optional for this MVP. It is a gate.

Required observability behavior:

1. Every major stage transition must emit at least one `observability-event`.
2. Every major stage in the vertical slice must have a corresponding `trace-step`.
3. Event and step linkage must identify the primary `source_contract` and `source_id`.
4. Retrieval and indexing events must remain additive and must not replace domain contracts.
5. Failure states must be visible as formal events before debugger projections are derived.

Required traceability behavior:

1. The run must remain reconstructable from `trace_id` plus linked contract ids.
2. `knowledge-source` to `embedding-job` linkage must be explicit.
3. `embedding-job` to `retrieval-index` linkage must be explicit.
4. `retrieval-index` to `knowledge-retrieval` linkage must be explicit.
5. `knowledge-retrieval` to `retrieval-session` linkage must be explicit.
6. `retrieval-session` to `retrieval-result` linkage must be explicit.
7. `observability-event`, `trace-step`, and `failure-report` must link back to the domain entities they describe.

## Debugger Projection Expectations
The Visual Debugger must remain contract-driven.

Projection requirements:

1. `debug-node-view` must represent each meaningful stage node in the thin runtime path.
2. `pipeline-view` must aggregate node, step, event, and failure identifiers into one pipeline snapshot.
3. `debug-panel` must be able to focus the current or failed stage without requiring UI-specific state.
4. Focus and highlight semantics must be derivable from existing contracts, not handwritten debugger-only metadata.
5. Happy path should produce a coherent active-to-completed pipeline progression.
6. Failure path should produce a degraded pipeline view and an attention-worthy debug panel.

## Failure-Path Design
The failure path must be intentional, controlled, and repeatable.

Required properties:

1. The chosen failure should break one contract linkage or one required stage transition in a predictable way.
2. The failure should occur after enough earlier steps succeed that observability and debugger projections have meaningful context.
3. The runtime must emit a terminal `observability-event` with failure semantics.
4. The runtime must emit a failed or blocked `trace-step`.
5. The runtime must create a `failure-report` with a clear `source_contract`, `source_id`, and root-cause hypothesis.
6. The debugger projections must surface the failed focus without needing log inspection.

Recommended first failure:

- force a missing or invalid linkage between `retrieval-session` and `retrieval-result`, or
- force a retrieval execution that cannot produce a valid result after index creation

The failure should be chosen based on which path yields the clearest diagnostic coverage with the least runtime complexity.

## Acceptance Criteria
The thin runtime MVP is ready only when all of the following are true:

1. One local deterministic text-first run creates a valid `knowledge-source` to `retrieval-result` chain.
2. The run uses one explicit `embedding-provider` and one explicit `embedding-job`.
3. The run creates one valid `retrieval-index`.
4. The run records one valid `knowledge-retrieval`.
5. The run records one valid `retrieval-session`.
6. The run records one valid `retrieval-result`.
7. The run emits `observability-event` records for the full path.
8. The run emits ordered `trace-step` records for the full path.
9. The run derives valid `debug-node-view`, `pipeline-view`, and `debug-panel` projections from formal records.
10. A controlled failure run produces `failure-report` plus degraded projections.
11. The slice remains local-first, single-process, text-first, and limited to one vertical scenario.
12. No bridge-specific behavior, autonomy layer, or scaling behavior is introduced.

## Testing Approach
Testing should stay narrow and verification-oriented.

Required testing layers:

1. Contract verification
   - continue running shared contract verification
   - keep contract semantics unchanged unless intentionally evolved later
2. Acceptance checklist coverage
   - add a happy-path checklist for the thin runtime vertical slice
   - add a failure-path checklist for the controlled failure scenario
3. Runtime stub verification
   - verify deterministic fixture input and normalized text output
   - verify explicit contract creation order
   - verify linkage integrity across the full chain
4. Observability verification
   - verify required `observability-event` emission per stage
   - verify event linkage to domain records
5. Trace verification
   - verify ordered `trace-step` creation
   - verify event-to-step linkage
6. Debug projection verification
   - verify `debug-node-view`, `pipeline-view`, and `debug-panel` can be built from formal records alone
7. Failure-path verification
   - verify forced failure produces `failure-report`
   - verify failure state is visible in events, steps, and debugger projections

## Follow-On Work
After this plan is executed, the next work should remain staged and conservative:

1. implement the Paperclip runtime stubs for the approved thin slice
2. add acceptance skeletons and verification helpers in this repository
3. validate debugger projections against formal observability contracts
4. only then consider expanding provider coverage, bridge integration, or broader runtime scenarios

What comes after this plan should be obvious:

- first executable thin runtime slice
- then validated observability-backed debugger flow
- then broader retrieval/runtime coverage

What must not come next:

- autonomy before observability
- bridge complexity before local runtime validation
- scale work before one vertical scenario is stable
- generalized architecture before the thin slice proves itself
