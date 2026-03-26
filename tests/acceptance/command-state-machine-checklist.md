# Acceptance Checklist — Command State Machine

## AC-101
Command starts in received state.

## AC-102
Invalid command can transition to rejected.

## AC-103
Valid command can transition to validated.

## AC-104
Validated command can transition to accepted.

## AC-105
Accepted command can transition to requires_approval.

## AC-106
Approved command can transition to routed.

## AC-107
Routed command can transition to planned.

## AC-108
Planned command can transition to executing.

## AC-109
Executing command can transition to completed.

## AC-110
Executing command can transition to failed.

## AC-111
Transition accepted -> completed is forbidden.

## AC-112
Transition received -> executing is forbidden.

## AC-113
Final states are logged and not re-opened automatically.
