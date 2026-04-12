# Hybrid Path Explicit Reopen Decision Template

## Status Note (Template-Only, Non-Authorizing)
This file is a governance template only and does not itself grant reopen.
Parked-state governance remains active unless a separate explicit decision is recorded.
Scenario-01 remains the only authoritative implemented runtime path unless a separate explicit decision changes that authority.

## Hybrid Path Direction Context
- Hybrid Path is the accepted architecture/governance direction.
- Paperclip-like company-scoped control-plane principles are the target core architecture direction.
- Factory-of-Companies-specific multi-company and shared-infrastructure coordination remains a separate extension layer.

## 1. Title
- Reopen decision title:

## 2. Decision Status
- Status: proposed / approved / rejected

## 3. Decision Date
- Date:

## 4. Authorizing Authority
- Authority:

## 5. Current Baseline Reference
- Branch:
- Checkpoint:
- Working tree expectation: clean before any reopen action begins

## 6. Reopen Purpose
- Purpose:

## 7. Exact Scope Being Reopened
- Exact scope:
- Exact files/directories/surfaces:

## 8. Scope Explicitly Not Reopened
- Not reopened:

## 9. First and Only Track Reopened In This Decision
- Reopened track:

## 10. Protected Surfaces That Remain Blocked
- `packages/**` unless explicitly named above
- `tests/runtime/**` unless explicitly named above
- all blocked tracks not explicitly named above remain blocked

## 11. Preconditions Checklist
- [ ] branch and checkpoint are explicitly recorded
- [ ] working tree is clean
- [ ] exact reopened scope is named
- [ ] exact non-reopened scope is named
- [ ] contract/runtime/acceptance boundaries are explicitly named if affected
- [ ] blocked tracks not named remain blocked
- [ ] one-track-only reopen discipline is preserved

## 12. Allowed Actions After Reopen
- Allowed actions are limited to the exact reopened scope named above.

## 13. Still-Forbidden Actions After Reopen
- no work outside the exact reopened scope
- no implicit expansion to adjacent tracks or surfaces
- no contract changes, runtime changes, or acceptance expansion unless explicitly named above
- no blocked-track activation unless individually and explicitly reopened

## 14. Success Criteria
- Success criteria:

## 15. Review Checkpoint
- Review checkpoint:

## 16. Rollback-to-Parked-State Rule
- If reopened work exceeds the named scope, loses clean authority boundaries, or fails the review checkpoint, return the track to parked-state and record a new checkpoint decision.

## 17. Non-Authorization Reminder For Any Future Broader Work
- This decision template does not authorize broader work by implication.
- Any future broader reopen requires a separate explicit governance decision with exact scope naming.
