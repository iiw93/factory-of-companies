# Acceptance Checklist — Timeout Policy Contract

## AC-1101
Timeout policy schema exists.

## AC-1102
`timeout_policy_id` is required.

## AC-1103
`trace_id` is required.

## AC-1104
`command_id` is required.

## AC-1105
`timeout_seconds` is required.

## AC-1106
`scope` enum is enforced.

## AC-1107
`timeout_strategy` enum is enforced.

## AC-1108
`created_at` is required.

## AC-1109
`note` is optional.

## AC-1110
Execution request `timeout_seconds` stays aligned conceptually.

## AC-1111
Execution result `timed_out` outcome stays aligned conceptually.

## AC-1112
Docs/specs/schema remain aligned.
