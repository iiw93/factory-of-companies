# Hybrid Path First Technical Reopen Recommendation

## 1. Purpose
Synthesize current architecture/planning artifacts into one strictly bounded recommendation for the first technical reopen track.
This document is planning/governance-only and non-implementing.

## 2. Selected Technical Reopen Track
Core Control-Plane Boundary/Interface Specification Track 01 (documentation-first technical boundary definition only).

## 2A. Track Status
Single specification-only technical track is explicitly approved and active at governance level.
This status does not authorize runtime implementation.

## 3. Why This Track
- Core mapping (`hybrid-path-core-mapping.md`) identifies the unresolved translation from governance-defined core principles to explicit technical boundary interfaces.
- Core-vs-extension boundary (`hybrid-path-core-vs-extension-boundary.md`) requires enforceable technical demarcation points so extension concerns do not leak into core by implication.
- Core gaps and decisions (`hybrid-path-core-gaps-and-decisions.md`) confirms the governance-to-technical boundary gap and core-to-runtime interface gap as highest-priority blockers before any broader technical work.

## 4. Exact Reopened Scope (specification-only)
- Produce a technical boundary/interface specification artifact set that maps core control-plane governance decisions to explicit interface boundaries.
- Define explicit in-scope/out-of-scope technical surfaces for core boundary enforcement.
- Define core-to-extension separation criteria as technical decision rules.
- Define review and rollback checkpoints for this single technical track.

## 5. What Will NOT Be Reopened
- Runtime implementation work.
- Blocked-track activation (including adjacent technical tracks).
- Contract changes.
- Acceptance expansion.
- Any surface outside the explicitly named single technical boundary/interface specification track.

## 6. Preconditions for That Reopen
- Separate explicit governance decision recorded with exact scope naming and one-track-only discipline. (satisfied)
- Clean baseline checkpoint captured before reopen execution. (satisfied)
- Explicit statement preserving Scenario-01 as the only authoritative implemented runtime path unless separately changed. (satisfied)
- Explicit confirmation that extension-layer implementation remains blocked unless separately reopened. (satisfied)
- Review checkpoint and rollback rule pre-declared in the reopen decision. (satisfied)

## 7. Risks
- Scope creep from boundary specification into implicit implementation tasks.
- Core/extension boundary drift if separation rules are underspecified.
- Authority weakening if Scenario-01 guardrails are not restated in reopen text.
- Reopen-by-inertia if adjacent tracks are not explicitly excluded.

## 8. Final Recommendation Statement
Recommend one explicit, tightly scoped technical reopen for core control-plane boundary/interface specification only, with no implementation authorization and no adjacent track activation.

## 9. Review Checkpoint and Rollback Criteria
Review checkpoint:
- confirm all outputs remain specification-only
- confirm one-track-only discipline remains intact
- confirm Scenario-01 remains the only authoritative implemented runtime path
- confirm core-vs-extension boundary discipline is preserved
- confirm no forbidden surfaces were touched

Rollback criteria:
- revoke the track and return to parked-state outside approved scope if scope expands beyond boundary/interface specification
- revoke if forbidden surfaces are touched
- revoke if one-track-only discipline is violated
- revoke if Scenario-01 authority is weakened

## 10. Constraint Note
This file does not authorize runtime implementation, blocked-track activation, contract changes, schema changes, or acceptance expansion.
Any implementation requires a separate explicit governance decision.
