# Hybrid Path Explicit Reopen Decision: Scenario-01 Core Boundary Enforcement Implementation Track 01

## Status Note (Governance Decision, Scope-Limited)
This document records explicit governance authorization for exactly one bounded implementation-track candidate.
It does not start implementation by itself.
All work outside the named track remains blocked unless separately and explicitly authorized.

## Title
Hybrid Path explicit reopen decision: Scenario-01 Core Boundary Enforcement Implementation Track 01

## Status
- approved (authorization package only; not started)

## Authority
Authority: project operator approval

## Baseline
- branch: `codex/docs/thin-runtime-mvp-plan`
- checkpoint: `813615efc61402d3e2d7e4300e5deef9fc4994c4`
- working tree: clean

## Authorized Candidate Scope Boundary
- implement only the already-specified core-to-runtime boundary rules for Scenario-01 on the existing authoritative execution chain
- limit implementation to enforcing approved boundary/interface behavior at runtime entry and orchestration handoff points defined by:
  - `docs/handoff/hybrid-path-explicit-reopen-decision-core-boundary-spec.md`
  - `docs/runbooks/hybrid-path-core-boundary-interface-spec-track-01.md`
- no new tracks, no adjacent surfaces, no cross-scenario behavior

## Explicit Non-Goals
- no schema changes
- no contract shape changes
- no acceptance-surface expansion beyond this track's verification set
- no Scenario-02 or multi-scenario support
- no bridge/dashboard/router/model-routing/company-builder/deploy-platform work
- no adjacent-track activation
- no alternate identity authority source

## Required Acceptance Surface (for this candidate only)
- runtime verification that Scenario-01 continues to enforce:
  - `scenario-01.execution-request->boundary-edge.mediation-binding`
  - `execution-request.mediation-identity+trace.carrier`
  - required carrier fields: `mediation_identity`, `trace`
  - no alternate identity source is authoritative
  - orchestration-handoff alignment intact
- negative-path verification that non-conforming boundary/interface conditions are rejected
- one implementation-track checkpoint artifact documenting scope adherence and invariant preservation

## Still-Blocked Surfaces
- all blocked tracks and adjacent surfaces remain blocked
- no Scenario-02 reopen
- no bridge/dashboard/router-model-routing/company-builder/deploy-platform reopen
- no multi-scenario reopen

## Frozen Authority Invariants (Unchanged)
- binding name remains `scenario-01.execution-request->boundary-edge.mediation-binding`
- carrier path remains `execution-request.mediation-identity+trace.carrier`
- required carrier fields remain `mediation_identity` and `trace`
- no alternate identity source is authoritative
- orchestration-handoff alignment remains intact
- Scenario-01-only authority remains in force unless separately changed by explicit governance decision

## Review Checkpoint Gate
Before any execution-start authorization can be issued, governance review must confirm:
- implementation scope is exactly limited to this single track
- non-goals and blocked surfaces are preserved
- frozen invariants remain unchanged in planned implementation intent
- acceptance surface is exact and non-expanded
- rollback rule is pre-accepted

## Rollback Rule
If execution planning or implementation intent exceeds this scope, touches blocked surfaces, weakens frozen invariants, or implies adjacent-track activation, this authorization is revoked and governance returns to parked-state at a new checkpoint decision.

## Start-Authorization Boundary
This document authorizes only the bounded implementation-track candidate package.
It does not authorize code changes or runtime execution start.
A separate explicit "start implementation" decision is required before any code changes begin.
