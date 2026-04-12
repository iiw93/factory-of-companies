# Acceptance Checklist — Bridge Command Contract

## Status Note (Guardrail-Only, Non-Authorizing)
This checklist is historical/planning context and is not evidence of current bridge, Telegram, or Web Dashboard availability.

Canonical authority is:
- `docs/handoff/global-project-checkpoint-after-scenario-02-no-go.md`
- historical spec reference unavailable; use current authoritative scenario-01 acceptance and handoff surfaces

Current enforced posture:
- bridge, Telegram, and Web Dashboard remain blocked/parked unless explicitly reopened
- scenario-01 remains the only authoritative implemented runtime path

This checklist does not authorize implementation-planning or coding.

## AC-001
Telegram message can be normalized into command contract.

## AC-002
Dashboard message can be normalized into command contract.

## AC-003
Both channels produce the same field structure.

## AC-004
Empty message is rejected.

## AC-005
Missing user_id is rejected.

## AC-006
Unknown channel is rejected.

## AC-007
Accepted command receives command_id.

## AC-008
Accepted command receives a processing status.

## AC-009
Bridge Layer does not execute business logic.

## AC-010
Bridge Layer only validates and routes commands.
