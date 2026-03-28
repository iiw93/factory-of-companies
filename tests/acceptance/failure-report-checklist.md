# Acceptance Checklist - Failure Report Contract

## AC-4001
Failure report schema exists.

## AC-4002
`failure_report_id` is required.

## AC-4003
`failure_name` is required.

## AC-4004
`failure_type` enum is enforced.

## AC-4005
`failure_status` enum is enforced.

## AC-4006
`created_at` is required.

## AC-4007
`trace_id` is required.

## AC-4008
`severity` enum is enforced.

## AC-4009
`source_contract` is required.

## AC-4010
`source_id` is required.

## AC-4011
`failure_message` is required.

## AC-4012
`requires_manual_review` is required boolean.

## AC-4013
`linked_event_id` is optional.

## AC-4014
`linked_trace_step_id` is optional.

## AC-4015
`linked_embedding_job_id` is optional.

## AC-4016
`linked_retrieval_index_id` is optional.

## AC-4017
`linked_knowledge_retrieval_id` is optional.

## AC-4018
`linked_retrieval_session_id` is optional.

## AC-4019
`linked_retrieval_result_id` is optional.

## AC-4020
`failure_root_cause` is optional.

## AC-4021
`failure_note` is optional.

## AC-4022
Failure linkage remains aligned with event, step, and indexing pipeline.

## AC-4023
Docs/specs/schema remain aligned.
