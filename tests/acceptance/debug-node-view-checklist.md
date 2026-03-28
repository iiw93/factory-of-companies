# Debug Node View Checklist

## Goal
Validate that the debug node view contract remains aligned across docs, schema, and verification logic.

## Acceptance Checklist

- [ ] AC-5001 debug node view schema exists
- [ ] AC-5002 `debug_node_view_id` is required
- [ ] AC-5003 `node_name` is required
- [ ] AC-5004 `node_type` enum is enforced
- [ ] AC-5005 `node_status` enum is enforced
- [ ] AC-5006 `created_at` is required
- [ ] AC-5007 `trace_id` is required
- [ ] AC-5008 `source_contract` is required
- [ ] AC-5009 `source_id` is required
- [ ] AC-5010 `display_label` is required
- [ ] AC-5011 `sequence_order` is required
- [ ] AC-5012 `is_current_focus` is required boolean
- [ ] AC-5013 `linked_trace_step_id` is optional
- [ ] AC-5014 `linked_event_ids` is optional
- [ ] AC-5015 `linked_failure_report_ids` is optional
- [ ] AC-5016 `linked_embedding_job_id` is optional
- [ ] AC-5017 `linked_retrieval_index_id` is optional
- [ ] AC-5018 `linked_knowledge_retrieval_id` is optional
- [ ] AC-5019 `linked_retrieval_session_id` is optional
- [ ] AC-5020 `linked_retrieval_result_id` is optional
- [ ] AC-5021 `debug_message` is optional
- [ ] AC-5022 `debug_note` is optional
- [ ] AC-5023 node linkage remains aligned with step/event/failure/indexing contracts
- [ ] AC-5024 docs/specs/schema remain aligned

## Notes

- This checklist covers only contract integrity for debug node view.
- It does not introduce UI, graph rendering, dashboard, or runtime state behavior.
