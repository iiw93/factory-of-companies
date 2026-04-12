# Hybrid Path Proposed Reopen Decision - Core Mapping

## Status Note (Proposed Draft Only, Non-Authorizing)
This file is a proposed decision draft only and does not itself grant reopen.
Parked-state governance remains active unless a separate explicit approval is recorded.
Scenario-01 remains the only authoritative implemented runtime path unless a separate explicit decision changes that authority.

## Hybrid Path Direction Context
- Hybrid Path is the accepted architecture/governance direction.
- Paperclip-like company-scoped control-plane principles are the target core architecture direction.
- Factory-of-Companies-specific multi-company and shared-infrastructure coordination remains a separate extension layer.

## 1. Title
- Hybrid Path proposed explicit reopen decision: architecture/planning core mapping

## 2. Decision Status
- Status: proposed

## 3. Decision Date
- Date: `<YYYY-MM-DD>`

## 4. Authorizing Authority
- Authority: `<record approving authority>`

## 5. Current Baseline Reference
- Branch: `codex/docs/thin-runtime-mvp-plan`
- Checkpoint: `0bbafd9d80d4767968251e7b6020ab7fcb4a7b2c`
- Working tree expectation: clean

## 6. Reopen Purpose
- Architecture/planning reopen for Hybrid Path core mapping.

## 7. Exact Scope Being Reopened
- Mapping Paperclip-like company-scoped control-plane core principles to the project's target core architecture.
- Defining the core-vs-extension boundary.
- Recommending the first technical reopen track.

## 8. Scope Explicitly Not Reopened
- Runtime implementation.
- Blocked-track activation.
- Contract changes.
- Acceptance expansion.

## 9. First and Only Track Reopened In This Decision
- Architecture/planning core mapping.

## 10. Protected Surfaces That Remain Blocked
- `packages/**` unless explicitly approved in a future decision.
- `tests/runtime/**` unless explicitly approved in a future decision.
- All blocked tracks not individually and explicitly reopened remain blocked.

## 11. Preconditions Checklist
- [ ] branch and checkpoint are explicitly recorded
- [ ] working tree is clean
- [ ] exact reopened scope is named
- [ ] exact non-reopened scope is named
- [ ] one-track-only reopen discipline is preserved
- [ ] blocked tracks not named remain blocked
- [ ] contract/runtime/acceptance boundaries remain unchanged unless explicitly approved in a future decision

## 12. Allowed Actions After Reopen
- Allowed actions are limited strictly to the architecture/planning scope named above.

## 13. Still-Forbidden Actions After Reopen
- No runtime implementation.
- No blocked-track activation.
- No contract changes.
- No acceptance expansion.
- No scope growth outside the exact reopened architecture/planning track.

## 14. Success Criteria
- Paperclip-like company-scoped control-plane core principles are mapped to the project's target core architecture.
- The core-vs-extension boundary is explicitly defined.
- A first technical reopen track is recommended without activating it.

## 15. Review Checkpoint
- Review checkpoint: explicit governance review of the completed core-mapping output before any further reopen decision.

## 16. Rollback-to-Parked-State Rule
- If work exceeds the named scope, weakens governance boundaries, or fails the review checkpoint, return the track to parked-state and record a new checkpoint decision.

## 17. Non-Authorization Reminder For Any Broader Work
- This proposed draft does not authorize broader work by implication.
- Any broader reopen requires a separate explicit governance decision with exact scope naming.
