# HOLD-STABLE Scenario-01 Acceptance Invariants Checkpoint

- Governing authority: frozen `HOLD-STABLE` anchor
- Project: `factory-of-companies`
- Branch: `codex/docs/thin-runtime-mvp-plan`

## Relevant committed checkpoints

- `b02e02b` — docs(handoff): record HOLD-STABLE checkpoint for scenario-01 carrier-link acceptance
- `d893e61` — acceptance(scenario-01): add carrier-link checklist seed under HOLD-STABLE boundary authority
- `027b040` — docs(handoff): add HOLD-STABLE post-acceptance consolidation checkpoint

## Fixed scenario-01 acceptance invariants

- Authoritative carrier name is fixed.
- Required carrier fields are fixed:
  - `mediation_identity`
  - `trace`
- Orchestration-handoff alignment is fixed.
- Scenario-01 boundary behavior must treat this carrier as authoritative.

## Governance boundaries

- Runtime/package scope remains blocked unless explicitly authorized.
- Implementation source remains unconfirmed.
- Archival/governance-only note: this checkpoint does not authorize any further coding unit by itself.
