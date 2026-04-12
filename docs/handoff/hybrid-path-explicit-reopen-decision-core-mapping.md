# Hybrid Path Explicit Reopen Decision: Architecture/Planning Core Mapping

## Status Note (Governance Decision, Scope-Limited)
This recorded governance decision authorizes only the explicitly scoped reopen defined below.
It does not authorize any broader or technical reopen by implication.
Scenario-01 remains the only authoritative implemented runtime path unless separately changed by a future explicit decision.

## Title
Hybrid Path explicit reopen decision: architecture/planning core mapping

## Status
- approved

## Authority
Authority: project operator approval

## Baseline
- branch: `codex/docs/thin-runtime-mvp-plan`
- checkpoint: `67fa9741ed62ffbd2ad47da12c10c9e142002f8b`
- working tree: clean

## Approved Reopen Scope
- architecture/planning core mapping only
- mapping Paperclip-like company-scoped control-plane core principles to the project's target core architecture
- defining the core-vs-extension boundary
- recommending the first technical reopen track
- exact files/directories/surfaces: `docs/roadmap/**`, `docs/runbooks/**`, and `docs/handoff/**` limited strictly to Hybrid Path core-mapping planning/governance artifacts for core-principles mapping, core-vs-extension boundary definition, and first technical reopen-track recommendation
- first and only track reopened in this decision: architecture/planning core mapping

## Not Reopened
- runtime implementation
- blocked-track activation
- contract changes
- acceptance expansion
- any scope outside the exact architecture/planning core-mapping surfaces named above
- Scenario-01 runtime authority

## Allowed Actions
- planning/governance analysis and documentation within the exact reopened scope above
- production of core-mapping artifacts that align Hybrid Path to the project's target core architecture
- explicit definition of the core-vs-extension boundary
- recommendation of a first technical reopen track without activating it

## Still-Forbidden Actions
- no runtime implementation is authorized
- no blocked-track activation is authorized
- no contract changes are authorized
- no acceptance expansion is authorized
- no work in `packages/**`
- no work in `tests/runtime/**`
- no implicit expansion to adjacent tracks or surfaces
- all blocked tracks not individually and explicitly reopened remain blocked

## Review Checkpoint
- explicit governance review of the completed core-mapping output before any further reopen decision, including confirmation that one-track-only discipline, exact-scope boundaries, and Scenario-01 authority were preserved

## Rollback Rule
- if reopened work exceeds the named scope, weakens governance boundaries, loses clean authority limits, or fails the review checkpoint, return the track to parked-state and record a new checkpoint decision

## Safety Note
- this approval is limited to architecture/planning core mapping only
- parked-state governance otherwise remains active
- Scenario-01 remains the only authoritative implemented runtime path unless separately changed later
- any broader or technical reopen requires a separate explicit governance decision with exact scope naming
