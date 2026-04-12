# Core Control-Plane Technical Surface Classification

## 1. Purpose
Define how technical surfaces are classified relative to the currently reopened single technical track: core control-plane boundary/interface specification.
This is a specification-only classification artifact and does not authorize implementation.

## 2. Surface Classes
- In-scope now
- Not in scope now
- Conditionally future-scope
- Explicitly forbidden

## 3. In-Scope Now
- `docs/specs/**` artifacts strictly for boundary/interface specification.
- `docs/runbooks/**` artifacts that provide governance/traceability context for this same technical track.
- `docs/handoff/**` decision and checkpoint artifacts tied directly to this track.
- Specification-level definitions of boundary rules, interface contract shape, validation/control protocol, and surface classification logic.

## 4. Not In Scope Now
- Runtime behavior design details that drift into execution planning.
- Implementation-ready technical decomposition for adapters, hooks, or runtime wiring.
- Cross-track technical surfaces not named in this reopened track.
- Any non-doc surface, even if related conceptually.

## 5. Conditionally Future-Scope
- Additional technical surfaces may become eligible only after a separate explicit reopen decision records:
- exact scope naming
- one-track-only discipline for that future scope
- authority and checkpoint constraints preserving Scenario-01 guardrails
- Until such a decision exists, these surfaces remain non-authorized.

## 6. Explicitly Forbidden
- `packages/**`
- `tests/runtime/**`
- runtime adapters
- execution hooks
- blocked-track implementation areas, including scenario-02, bridge, dashboard, model-router, company-builder, deploy, and telegram
- contract implementation changes
- acceptance-scope expansion

## 7. Classification Rules
- Classify a surface as In-scope now only if it is a docs artifact directly required by this single technical boundary/interface-spec track.
- Classify as Not in scope now when related material is technical but not required for current approved scope.
- Classify as Conditionally future-scope only when it could be considered under a future explicit reopen decision.
- Classify as Explicitly forbidden when governance constraints prohibit work regardless of relevance.
- When uncertain, default to more restrictive class and require explicit governance clarification.

## 8. Misclassification Risks
- Silent scope expansion into implementation by incorrectly classifying execution-adjacent surfaces as in-scope.
- Authority weakening if Scenario-01 guardrails are not preserved in classification decisions.
- Cross-track leakage that implicitly reopens blocked areas.
- Governance drift from specification-only outputs toward unauthorized technical activation.

## 9. Constraint Note
This file is specification-only.
It does not authorize runtime edits, blocked-track activation, contract implementation, acceptance expansion, or any work outside the approved single technical track.
