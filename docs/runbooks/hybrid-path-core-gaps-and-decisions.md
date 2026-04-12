# Hybrid Path Core Gaps and Decisions

## 1. Purpose
Identify confirmed core-alignment gaps and the governance-level decisions required before any future technical reopen can be considered.
This artifact is planning/governance-only and non-authorizing.

## 2. Current Core Alignment Summary
Hybrid Path core direction is documented as company-scoped control-plane principles with Scenario-01 retained as the only authoritative implemented runtime path.
Core-vs-extension boundary intent is documented, but translation into explicit technical scope and interfaces remains pending a separate explicit decision.
Reopen discipline is active and limited to architecture/planning core-mapping artifacts under approved docs surfaces.

## 3. Confirmed Gaps
- Governance-to-technical boundary gap: governance intent is defined, but technical boundary artifacts are not yet explicitly approved.
- Core-to-runtime interface gap: the way core control-plane decisions bind to runtime interfaces is not yet specified in technical form.
- Core-to-extension separation gap: extension concerns are named, but enforceable technical separation points are not yet decisioned.
- Reopen-governance execution gap: criteria and sequencing for moving from planning outputs to a narrowly scoped technical reopen decision are not yet finalized.

## 4. Decision Table
| Gap | Why it matters | Current constraint | Recommended decision |
| --- | --- | --- | --- |
| Governance-to-technical boundary gap | Prevents converting governance direction into bounded technical work safely. | No technical reopen is authorized; planning scope only. | Record an explicit decision artifact defining exact technical boundary deliverables before any implementation reopen. |
| Core-to-runtime interface gap | Without a defined interface boundary, runtime scope can drift. | Scenario-01 remains sole runtime authority; no runtime expansion allowed. | Decide a minimal interface-spec scope that remains documentation-only unless separately reopened. |
| Core-to-extension separation gap | Blurred separation risks extension leakage into core assumptions. | Extension tracks remain blocked unless explicitly reopened. | Decide explicit separation criteria and ownership boundaries to enforce core/extension demarcation. |
| Reopen-governance execution gap | Ambiguous progression can create implicit reopen by inertia. | One-track-only discipline and explicit reopen requirement remain in force. | Decide a checkpointed governance workflow for proposing, reviewing, and explicitly approving any next technical reopen. |

## 5. Non-Gaps
- Scenario-01 runtime authority is not a gap; authority remains explicit and intact.
- Parked-state discipline outside reopened scope is not a gap; it remains active and binding.
- Blocked-track protection is not a gap; blocked tracks remain non-authorized unless individually and explicitly reopened.

## 6. Candidate Next Technical Track Inputs
- Draft boundary/interface specification scope candidates derived from core mapping and boundary artifacts.
- Explicit list of in-scope/out-of-scope technical surfaces for a potential single-track technical reopen proposal.
- Governance acceptance criteria for technical-boundary documentation quality and review checkpoint readiness.
- Rollback conditions and stop criteria if proposed technical scope exceeds core-mapping constraints.

No track is activated by these inputs; they are decision preparation only.

## 7. Constraint Note
This file does not authorize any technical reopen, runtime implementation, blocked-track activation, contract change, or acceptance expansion.
It only prepares decision basis within the current approved architecture/planning core-mapping scope.
