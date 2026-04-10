# Architecture System Map

## Status Note (Guardrail-Only, Non-Authorizing)

This document is architectural context only and does not authorize implementation-planning, coding, or execution.

It describes the current system structure under parked-state governance.

---

## Purpose

Define a clear, layered view of the system:

- governance layer
- Scenario-01 authority layer
- acceptance layer
- guard/interpretation layer
- runtime reference layer
- runtime implementation layer
- blocked-track planning layer

This map is descriptive only and does not change system behavior.

---

## Layer 1 — Governance

Files:
- docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md
- AGENTS.md
- docs/runbooks/git-sync-discipline.md

Function:
- defines parked-state
- defines blocked tracks
- enforces non-authorizing behavior
- controls project movement

Status:
active, authoritative

---

## Layer 2 — Scenario-01 Authority

File:
- docs/handoff/scenario-01-consumer-handoff-pack.md

Function:
- defines narrow Scenario-01 consumer baseline
- defines intake/output interpretation
- represents the only active runtime path

Status:
active, authoritative (Scenario-01 only)

---

## Layer 3 — Acceptance

Files:
- tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md
- tests/acceptance/thin-runtime-mvp-scenario-01-*.md

Function:
- defines acceptance criteria (AC-71xx / AC-72xx)
- defines boundaries and non-goals
- supports validation surface

Status:
active, validation layer

---

## Layer 4 — Guard / Interpretation

File:
- docs/runbooks/thin-runtime-inspection-and-failure-reading-guide.md

Function:
- defines guard categories
- supports failure interpretation
- supports review/triage

Status:
active, operator layer

---

## Layer 5 — Traceability (Crosswalk)

File:
- tests/acceptance/thin-runtime-mvp-scenario-01-checklist.md

Function:
- maps acceptance → guards → runtime tests
- provides traceability only

Constraints:
- does not change semantics
- does not authorize implementation

Status:
active, traceability layer

---

## Layer 6 — Runtime Reference

Path:
- tests/runtime/**

Function:
- contains runtime tests
- referenced by acceptance and crosswalk

Constraints:
- reference-only usage allowed
- no changes without explicit reopen

Status:
restricted

---

## Layer 7 — Runtime Implementation

Path:
- packages/paperclip-adapter/**

Function:
- runtime code
- adapter layer

Constraints:
- no changes without explicit reopen

Status:
restricted

---

## Layer 8 — Blocked Tracks

Examples:
- docs/specs/model-routing-contract.md
- tests/acceptance/model-routing-checklist.md

Function:
- future planning surfaces
- not active

Constraints:
- no changes without explicit reopen

Status:
parked

---

## Layer Relationships

Primary flow:

Governance
→ Scenario-01 Authority
→ Acceptance
→ Guard Interpretation
→ Runtime Reference

Implementation layers remain isolated unless reopened.

---

## Active vs Parked

Active:
- governance
- Scenario-01 authority
- acceptance
- guard layer
- traceability

Parked / restricted:
- runtime implementation
- runtime tests (for editing)
- all blocked tracks

---

## Key Principle

Documentation defines structure and constraints, not execution.

All movement requires explicit architecture gates.

---
