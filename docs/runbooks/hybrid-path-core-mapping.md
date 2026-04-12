# Hybrid Path Core Mapping

## 1. Purpose
Map Paperclip-like company-scoped control-plane core principles to the project's target core architecture in planning/governance terms only.
This artifact is non-authorizing and does not activate runtime implementation.

## 2. Paperclip Core Principles (abstracted)
- Company-scoped control-plane: each company is operated through a company-level control boundary.
- Per-company isolation: company context, state boundaries, and control decisions are isolated per company.
- Runtime as execution engine: runtime executes approved work; control-plane defines intent, policy, and guardrails.
- Governance vs execution separation: governance and planning decisions are separated from execution and implementation.

## 3. Target Core Architecture (Factory-of-Companies)
The target core architecture is a company-scoped control-plane model aligned to Hybrid Path, where governance and planning define boundaries, policies, and reopen discipline, and execution remains constrained by explicit approvals.
Scenario-01 remains the only authoritative implemented runtime path until a separate explicit decision changes runtime authority.
Factory-of-Companies-specific multi-company and shared-infrastructure coordination remains outside core as an extension-layer concern.

## 4. Mapping Table
| Paperclip principle | Our implementation | Gap | Decision |
| --- | --- | --- | --- |
| Company-scoped control-plane | Governance artifacts define company-scoped planning and control boundaries (`docs/handoff/**`, `docs/runbooks/**`, `docs/roadmap/**`). | No consolidated core-mapping runbook existed before this artifact. | Keep company-scoped control-plane as core target and document canonical mapping rules. |
| Per-company isolation | Scenario-01 remains sole runtime authority; reopen discipline requires exact scope naming and one-track-only control. | Isolation is governed by policy text but not yet represented in technical boundary interfaces. | Preserve isolation as governance invariant; defer technical interface design to future explicitly reopened track. |
| Runtime as execution engine | Runtime remains constrained to implemented Scenario-01 path; no runtime expansion authorized in current scope. | Core mapping to a future technical control-plane track is not yet formalized. | Keep runtime execution-only posture; use mapping output to recommend first technical reopen track. |
| Governance vs execution separation | Explicit reopen decisions, templates, and prerequisites separate approval/planning from implementation actions. | Wrapper-level documentation alignment can still evolve as governance docs grow. | Enforce governance-first gates; block execution beyond approved reopened scope. |

## 5. Core vs Extension Boundary
Core:
- Company-scoped control-plane principles.
- Governance rules for reopen discipline (exact scope naming, one-track-only, clean baseline).
- Scenario-01 runtime authority guardrails.

Extension layer:
- Factory-of-Companies-specific multi-company coordination.
- Shared-infrastructure orchestration across companies.
- Any cross-company control surfaces not required for core company-scoped control-plane mapping.

## 6. Identified Gaps
- Missing technical specification for how core control-plane decisions bind to future implementation interfaces.
- Missing explicit technical boundary contract between core control-plane and extension-layer coordination.
- Missing approved technical reopen track artifact that converts this mapping into actionable technical scope without activating implementation.

## 7. First Technical Reopen Track Recommendation
Recommendation only (not activated):
- Reopen one technical track to draft a core control-plane boundary/interface specification that translates this mapping into explicit technical contracts between governance/control-plane concerns and runtime execution surfaces, while preserving Scenario-01 authority and leaving extension-layer activation blocked.
