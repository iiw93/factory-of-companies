# Pipeline View Checklist

## Goal
Validate that the pipeline view contract remains aligned across docs, schema, and verification logic.

## Acceptance Checklist
- [ ] AC-6001 pipeline view schema exists
- [ ] AC-6002 `pipeline_view_id` is required
- [ ] AC-6003 `view_name` is required
- [ ] AC-6004 `view_status` enum is enforced
- [ ] AC-6005 `created_at` is required
- [ ] AC-6006 `trace_id` is required
- [ ] AC-6007 `view_scope` enum is enforced
- [ ] AC-6008 `node_ids` is required
- [ ] AC-6009 `step_ids` is required
- [ ] AC-6010 `event_ids` is required
- [ ] AC-6011 `failure_report_ids` is required
- [ ] AC-6012 `summary_message` is required
- [ ] AC-6013 `active_node_id` is optional
- [ ] AC-6014 `active_step_id` is optional
- [ ] AC-6015 `view_note` is optional
- [ ] AC-6016 pipeline linkage remains aligned with node/step/event/failure contracts
- [ ] AC-6017 docs/specs/schema remain aligned

## Notes
- This checklist covers only contract integrity for pipeline view.
- It does not introduce UI, graph rendering, scheduling, or websocket behavior.
