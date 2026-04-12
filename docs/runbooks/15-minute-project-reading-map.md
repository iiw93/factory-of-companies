# 15-Minute Project Reading Map

## Status Note (Guardrail-Only, Non-Authorizing)

This document is historical/operational context only and does not authorize implementation-planning, coding, or execution.

It defines a safe reading order for understanding the current project state under parked-state governance.

---

## Hybrid Path Reading Note

Hybrid Path is the accepted architecture/governance direction.
- Paperclip-like company-scoped control-plane principles are the target core architecture direction.
- Factory-of-Companies-specific multi-company and shared-infrastructure coordination remains a separate extension layer.
- This note is governance direction only and does not grant reopen.
- Parked-state governance remains active.
- Scenario-01 remains the only authoritative implemented runtime path unless a separate explicit reopen decision is recorded.

---

## Goal

Allow a new participant to understand in ~15 minutes:

- current authoritative project state
- what is implemented vs parked
- where Scenario-01 authority lives
- how acceptance and guard surfaces are structured
- how to safely interact with the project without reopening blocked tracks

---

## Step 1 — Global Project State (START HERE)

File:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`

Focus:
- current authoritative runtime status
- parked-state constraints
- blocked tracks
- non-authorizing nature of documentation

Key takeaway:
Scenario-01 is the only authoritative implemented runtime path.

---

## Step 2 — Scenario-01 Consumer Authority

File:
- `docs/handoff/scenario-01-consumer-handoff-pack.md`

Focus:
- narrow consumer baseline
- intake/output contract shape
- stable vs dynamic boundaries

Key takeaway:
This file defines how Scenario-01 is interpreted by downstream consumers.

---

## Step 3 — Acceptance Surface

File:
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

Focus:
- acceptance criteria (AC-71xx / AC-72xx)
- explicit non-goals
- boundary constraints

Key takeaway:
Acceptance defines validation, not implementation.

---

## Step 4 — Guard Map and Runtime Interpretation

File:
- `docs/runbooks/thin-runtime-inspection-and-failure-reading-guide.md`

Focus:
- guard-map categories
- failure interpretation
- review/triage flow

Key takeaway:
Guard categories explain how runtime behavior is evaluated.

---

## Step 5 — Crosswalk (Acceptance → Guards → Runtime Tests)

File:
- `tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md`

Focus:
- Acceptance-to-Guard Crosswalk (Scenario-01, review-only)

Key takeaway:
Traceability layer only; does not change semantics or authorize implementation.

---

## Step 6 — Process Rules (How to Work Safely)

Files:
- `AGENTS.md`
- `docs/runbooks/git-sync-discipline.md`

Focus:
- scope control
- sync discipline
- stash-first rule
- restricted zones

Key takeaway:
Always validate scope before making changes.

---

## Step 7 — Optional: Scenario-01 Roadmap Context

File:
- `docs/roadmap/scenario-01-post-checkpoint-micro-track-candidates.md`

Focus:
- potential micro-track directions

Key takeaway:
Roadmap is non-authorizing planning context only.

---

## Do Not Start With

Avoid reading first:

- `docs/specs/model-routing-contract.md`
- `tests/acceptance/model-routing-checklist.md`
- `packages/**`
- `tests/runtime/**`

Reason:
These are blocked-track or restricted surfaces.

---

## 5-Minute Minimal Path

If time is limited, read only:

1. global-project-checkpoint-after-scenario-02-no-go.md
2. scenario-01-consumer-handoff-pack.md
3. thin-runtime-mvp-scenario-01-checklist.md

---

## Summary

The project is governed by:

- parked-state constraints
- split authority (global + Scenario-01)
- acceptance-driven validation
- strict non-authorizing documentation

Safe movement requires explicit architecture gates.

---
