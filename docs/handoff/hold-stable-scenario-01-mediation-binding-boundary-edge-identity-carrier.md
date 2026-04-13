# HOLD-STABLE: Scenario-01 Mediation Binding + Boundary-Edge Identity Carrier

Authority: HOLD-STABLE (frozen)

Purpose: Define the minimal, scenario-01-specific mediation binding and identity+trace carrier required to make boundary-edge identity linkage explicit. This note defines naming and required semantics only.

Required Mediation Binding Name:
scenario-01.execution-request->boundary-edge.mediation-binding

Required Carrier Name:
execution-request.mediation-identity+trace.carrier

Required Carrier Fields / Semantics (Identity + Trace Only):
- mediation_identity: Canonical execution-request mediation identity value used for scenario-01 boundary-edge decisions. Opaque and stable across the boundary; MUST NOT be re-derived at the edge.
- trace: Trace-carrying value that MUST be preserved end-to-end across the scenario-01 boundary edge. Opaque; continuity required; MUST NOT be truncated, replaced, or regenerated at the edge.

Boundary-Edge Linkage Assertion:
The scenario-01 boundary edge MUST consume execution-request.mediation-identity+trace.carrier.
No other identity source is authoritative for scenario-01 boundary-edge operational behavior under HOLD-STABLE.

Non-Authorization:
This note does not authorize runtime reopening, implementation/source discovery, code edits, package/runtime scope changes, or execution.

Status:
HOLD-STABLE draft (approved content; inserted as documentation artifact only)
