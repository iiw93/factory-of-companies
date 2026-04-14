# Hybrid Path Core Gaps and Decisions

## 1. Purpose
Identify confirmed core-alignment gaps and the governance-level decisions required before any future technical reopen can be considered.
This artifact is planning/governance-only and non-authorizing.

## 2. Current Core Alignment Summary
Hybrid Path core direction is documented as company-scoped control-plane principles with Scenario-01 retained as the only authoritative implemented runtime path.
Core-vs-extension boundary intent is documented, and a single specification-only technical reopen track is explicitly approved for boundary/interface definition.
Reopen discipline remains one-track-only and specification-only under approved docs surfaces.

## 3. Resolved Preconditions and Remaining Gaps
Resolved precondition:
- Governance-to-technical authorization is explicitly approved for `Core Control-Plane Boundary/Interface Specification Track 01` in specification-only form.

Remaining gaps:
- Core-to-runtime interface completeness gap: interface boundaries are approved in scope but still need complete specification artifacts.
- Core-to-extension separation completeness gap: separation concerns are approved in scope but still need complete enforceable specification rules.
- Reopen-governance execution quality gap: checkpoint evidence and rollback-ready specificity must be completed for review closure.

## 4. Decision Table
| Gap | Why it matters | Current constraint | Recommended decision |
| --- | --- | --- | --- |
| Core-to-runtime interface completeness gap | Without complete interface boundaries, runtime scope can drift later. | Specification-only track is active; runtime expansion remains blocked. | Complete minimal interface-boundary specification artifacts inside this single track. |
| Core-to-extension separation completeness gap | Blurred separation risks extension leakage into core assumptions. | Extension tracks remain blocked unless explicitly reopened. | Complete explicit separation criteria and technical demarcation rules in specification form. |
| Reopen-governance execution quality gap | Incomplete checkpoint evidence can allow implicit reopen-by-inertia. | One-track-only discipline and explicit implementation gate remain in force. | Produce review-ready checkpoint evidence and rollback-ready criteria for closure. |

## 5. Non-Gaps
- Scenario-01 runtime authority is not a gap; authority remains explicit and intact.
- Parked-state discipline outside reopened scope is not a gap; it remains active and binding.
- Blocked-track protection is not a gap; blocked tracks remain non-authorized unless individually and explicitly reopened.
- Governance-to-technical authorization is not a gap; single-track specification authorization is explicit and active.

## 6. Active Track 01 Specification Completion Inputs
- Draft boundary/interface specification scope candidates derived from core mapping and boundary artifacts.
- Explicit list of in-scope/out-of-scope technical surfaces for active single-track specification completion.
- Governance acceptance criteria for technical-boundary documentation quality and review checkpoint readiness.
- Rollback conditions and stop criteria if proposed technical scope exceeds core-mapping constraints.

No implementation is authorized by these inputs; they are specification-completion inputs only.

## 7. Constraint Note
This file does not authorize any technical reopen, runtime implementation, blocked-track activation, contract change, or acceptance expansion.
It only prepares decision basis within the current approved architecture/planning core-mapping scope.

## 8. Review Checkpoint and Rollback Criteria (Track 01)
Review checkpoint:
- confirm outputs remain specification-only
- confirm one-track-only discipline remains intact
- confirm frozen Scenario-01 authority invariants remain unchanged
- confirm no forbidden surfaces were touched
- confirm no contract/schema/runtime/acceptance expansion occurred

Rollback criteria:
- revoke Track 01 and return to parked-state outside approved scope if scope extends beyond boundary/interface specification
- revoke if any forbidden surfaces are touched
- revoke if one-track-only discipline is violated
- revoke if Scenario-01 authority is weakened
