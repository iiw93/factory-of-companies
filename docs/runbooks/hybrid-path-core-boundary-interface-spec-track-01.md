# Hybrid Path Core Boundary/Interface Specification - Track 01

## 1. Purpose
Finalize the single approved specification-only technical track by defining explicit technical boundary/interface rules without authorizing implementation.

## 2. Core Control-Plane Boundary Rules
- Core control-plane scope is limited to company-scoped control intent, boundary rules, and governance-aligned interface definitions.
- Scenario-01 remains the only authoritative implemented runtime path unless separately and explicitly authorized.
- Any concern that crosses company boundaries is extension-layer by default unless explicitly classified otherwise in governance artifacts.
- One-track-only discipline is mandatory; no adjacent-track work is implied or allowed.

## 3. Core-to-Runtime Interface Boundaries (Specification-Only)
- Interface definitions in this track are specification artifacts only and do not authorize runtime code or behavior changes.
- Core-to-runtime boundary definitions must specify:
  - interface intent and control-plane ownership
  - runtime-side boundary obligations (descriptive, non-executable)
  - forbidden coupling points that would collapse governance and execution boundaries
- No alternate identity source is authoritative; identity authority remains bound to the existing Scenario-01 mediation chain.
- Orchestration-handoff alignment constraints remain binding and unchanged.

## 4. Core-to-Extension Demarcation Rules
- Core layer includes company-scoped control-plane boundary rules and governance discipline.
- Extension layer includes cross-company coordination, shared platform orchestration, and any surfaces beyond single-company control scope.
- Demarcation rule: if a surface requires cross-company or shared-platform orchestration semantics, classify as extension and keep blocked unless separately reopened.
- Demarcation rule: no extension concern may be introduced into core by implication or documentation drift.

## 5. Track 01 Implementation Surfaces: In-Scope / Out-of-Scope
In-scope for this specification-only track:
- Technical boundary/interface specification text in `docs/runbooks/**` and `docs/handoff/**` needed to formalize:
  - core control-plane boundary rules
  - core-to-runtime interface boundaries (specification-only)
  - core-to-extension demarcation rules
  - review and rollback criteria

Out-of-scope for this specification-only track:
- Any runtime implementation or behavior change
- Any change under `packages/**`
- Any change under `tests/runtime/**`
- Any contract or schema change
- Any acceptance expansion
- Any blocked-track or adjacent-track activation
- Any Scenario-02, bridge, dashboard, router/model-routing, company-builder, deploy/platform, or multi-scenario reopen

## 6. Review Checkpoint Evidence Requirements
Review must confirm all of the following:
- Outputs remain specification-only and non-implementing.
- One-track-only discipline is preserved.
- Frozen Scenario-01 authority invariants remain unchanged:
  - `scenario-01.execution-request->boundary-edge.mediation-binding`
  - `execution-request.mediation-identity+trace.carrier`
  - required fields `mediation_identity` and `trace`
  - no alternate identity source is authoritative
  - orchestration-handoff alignment remains intact
- Exact in-scope/out-of-scope surfaces are explicitly declared and respected.
- No forbidden surfaces were touched and no scope expansion occurred.

## 7. Rollback Criteria
Revoke Track 01 completion state and return to parked-state outside approved scope if any of the following occur:
- Scope expands beyond boundary/interface specification.
- Any forbidden surface is touched.
- One-track-only discipline is violated.
- Frozen Scenario-01 authority invariants are weakened or altered.
- Documentation implies implementation authority, blocked-track activation, or adjacent-track activation.

## 8. Non-Authorization Constraint
This runbook does not authorize implementation.
It does not authorize runtime/package/schema/contract/acceptance changes.
It does not authorize opening any adjacent track.
Any implementation requires a separate explicit governance authorization step.
