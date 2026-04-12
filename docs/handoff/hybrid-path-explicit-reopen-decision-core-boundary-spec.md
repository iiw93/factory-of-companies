# Hybrid Path Explicit Reopen Decision: Core Boundary/Interface Specification

## Title
Hybrid Path explicit reopen decision: core control-plane boundary/interface specification (first technical track)

## Status
- approved

## Authority
Authority: project operator approval

## Baseline
- branch: `codex/docs/thin-runtime-mvp-plan`
- checkpoint: `c5730a648e8e37f5a48193aa06dafffe2341212c`
- working tree: clean

## Approved Reopen Scope
- exactly one technical track is reopened: core control-plane boundary/interface specification only
- scope is limited to drafting and refining technical boundary/interface specification artifacts that formalize:
  - core control-plane boundary rules
  - core-to-runtime interface definition boundaries (specification only)
  - core-to-extension separation criteria and interface demarcation
  - in-scope/out-of-scope technical surface declarations for this single track
  - review and rollback criteria for this track
- no implementation authorization is included in this scope

## Not Reopened
- runtime implementation
- Scenario-02
- bridge
- dashboard
- model-router
- company-builder
- deploy
- telegram
- contract changes
- acceptance expansion
- any second technical track or adjacent scope beyond this one reopened track

## Allowed Actions
- create/update technical boundary/interface specification documents for the single reopened track
- define explicit boundary contracts and separation rules in specification form only
- perform governance/architecture traceability updates required to keep this track internally consistent
- prepare review-ready decision outputs for checkpoint validation

## Still-Forbidden Actions
- implementing runtime code or behavior changes
- activating blocked tracks, including Scenario-02, bridge, dashboard, model-router, company-builder, deploy, and telegram
- modifying contracts
- expanding acceptance scope or acceptance criteria
- broadening reopen scope beyond one-track-only discipline

## Review Checkpoint
- a formal governance checkpoint must confirm all outputs remain specification-only, remain within the exact single-track scope, preserve Scenario-01 as the only authoritative implemented runtime path, and preserve core-vs-extension boundary discipline before any further reopen is considered

## Rollback Rule
- if scope expands beyond boundary/interface specification, if forbidden surfaces are touched, if one-track-only discipline is violated, or if Scenario-01 authority is weakened, this reopen is revoked and governance returns to parked-state outside approved scope at a new recorded checkpoint

## Safety Note
- this decision is strictly limited to one technical specification track; it does not authorize runtime implementation, blocked-track activation, contract changes, or acceptance expansion, and Scenario-01 authority remains intact unless changed by a separate explicit decision
