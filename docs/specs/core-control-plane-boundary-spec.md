# Core Control-Plane Boundary Specification

## 1. Purpose
Define the core control-plane boundary as a strict technical specification under the currently approved single technical reopen track.
This specification is documentation-only and non-authorizing for implementation.

## 2. Core Control-Plane Definition
The core control-plane is the specification-level authority layer that defines policy, boundary rules, interface intent, and governance constraints for controlled runtime interaction.
It is not a runtime execution surface, not an orchestration executor, and not a direct command plane for triggering runtime actions.
It defines what is allowed to be specified, validated, and governed before any separately approved implementation work exists.

## 3. Runtime Boundary
Direct runtime control is forbidden.
Direct execution triggering is forbidden.
Any bypass of Scenario-01 authority is forbidden.
The control-plane may define boundary/interface specifications only; it may not invoke runtime behavior, mutate runtime state, or authorize execution paths.

## 4. Interface Model
Abstract model: Control Plane -> Interface Layer -> Runtime.

What may flow across the boundary:
- Specification-level interface intent.
- Policy constraints and boundary invariants.
- Validation criteria for compliance checks.

What may not flow across the boundary:
- Direct runtime execution commands.
- Execution hooks, runtime adapters, or implementation bindings.
- Cross-track activation intent outside the approved single track.

What remains specification-only at this stage:
- Interface contracts are design-time artifacts only.
- Boundary enforcement logic is documented, not implemented.
- Compliance checks are specification-level review procedures, not runtime mechanisms.

## 5. Core vs Extension Enforcement
Core scope remains limited to company-scoped control-plane boundary/interface specification concerns.
Extension concerns (multi-company coordination, shared-infrastructure orchestration, cross-company control surfaces) must not be introduced into core by implication.
Any extension-facing concern requires explicit classification as extension and remains out of this core boundary-spec track unless separately reopened.

## 6. Allowed Surfaces (technical view)
Allowed surfaces for this track are limited to specification/governance artifacts in:
- `docs/specs/**`
- `docs/runbooks/**`
- `docs/handoff/**`
and only where content is strictly required for the single core boundary/interface specification track.

## 7. Forbidden Surfaces
This track does not authorize work in:
- `packages/**`
- `tests/runtime/**`
- runtime adapters
- execution hooks
- blocked-track implementation areas

## 8. Boundary Invariants
- Scenario-01 authority invariant: Scenario-01 remains the only authoritative implemented runtime path unless separately changed by explicit governance decision.
- No implicit execution invariant: no specification artifact may be interpreted as execution authorization.
- No cross-track leakage invariant: this track cannot activate or imply activation of adjacent tracks.
- No silent scope expansion invariant: scope changes require separate explicit recorded reopen decisions.

## 9. Validation Rules
Boundary compliance is checked at specification level by verifying:
- Surface compliance: changed files remain within approved `docs/specs/**`, `docs/runbooks/**`, `docs/handoff/**` scope for this track.
- Scope compliance: content remains limited to core boundary/interface specification and excludes runtime implementation detail.
- Authority compliance: Scenario-01 authority and non-authorization language remain explicit and unweakened.
- Track compliance: no wording implies blocked-track activation, contract change, or acceptance expansion.
- Decision traceability: specification updates map back to recorded reopen decision constraints.

## 10. Constraint Note
This file does not authorize implementation, runtime control, blocked-track activation, contract changes, or acceptance expansion.
