# Debug Panel Checklist

## Goal
Validate that the debug panel contract remains aligned across docs, schema, and verification logic.

## Acceptance Checklist
- [ ] AC-7001 debug panel schema exists
- [ ] AC-7002 `debug_panel_id` is required
- [ ] AC-7003 `panel_name` is required
- [ ] AC-7004 `panel_status` enum is enforced
- [ ] AC-7005 `created_at` is required
- [ ] AC-7006 `trace_id` is required
- [ ] AC-7007 `panel_scope` enum is enforced
- [ ] AC-7008 `linked_pipeline_view_id` is required
- [ ] AC-7009 `primary_message` is required
- [ ] AC-7010 `highlight_level` enum is enforced
- [ ] AC-7011 `requires_attention` is required boolean
- [ ] AC-7012 `focused_node_id` is optional
- [ ] AC-7013 `focused_step_id` is optional
- [ ] AC-7014 `focused_event_id` is optional
- [ ] AC-7015 `focused_failure_report_id` is optional
- [ ] AC-7016 `secondary_message` is optional
- [ ] AC-7017 `panel_note` is optional
- [ ] AC-7018 panel linkage remains aligned with pipeline/node/step/event/failure contracts
- [ ] AC-7019 docs/specs/schema remain aligned

## Notes
- This checklist covers only contract integrity for debug panel.
- It does not introduce UI, frontend, live panel rendering, or runtime state behavior.
