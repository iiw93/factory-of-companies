#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

COMMAND_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "command.schema.json"
RESPONSE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "response.schema.json"
COMMAND_STATE_RULES_PATH = REPO_ROOT / "packages" / "shared-contracts" / "command-state-rules.json"
TRACEABILITY_ENVELOPE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "traceability-envelope.schema.json"
SESSION_CONTEXT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "session-context.schema.json"
PROJECT_CONTEXT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "project-context.schema.json"
COMPANY_CONTEXT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "company-context.schema.json"
OWNER_IDENTITY_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "owner-identity.schema.json"
ARTIFACT_REFERENCE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "artifact-reference.schema.json"
PLANNING_ARTIFACT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "planning-artifact.schema.json"
QUALITY_GATE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "quality-gate.schema.json"
EVIDENCE_BUNDLE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "evidence-bundle.schema.json"
GOVERNANCE_DECISION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "governance-decision.schema.json"
APPROVAL_ACTION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "approval-action.schema.json"
EXECUTION_REQUEST_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "execution-request.schema.json"
EXECUTION_RESULT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "execution-result.schema.json"
RELEASE_DECISION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "release-decision.schema.json"
DELIVERY_PACKAGE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "delivery-package.schema.json"
DEPLOYMENT_TARGET_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "deployment-target.schema.json"
ORCHESTRATION_HANDOFF_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "orchestration-handoff.schema.json"
AGENT_ROLE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "agent-role.schema.json"
ACTION_TYPE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "action-type.schema.json"
RUNTIME_CAPABILITY_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "runtime-capability.schema.json"
TOOL_INVOCATION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "tool-invocation.schema.json"
BUDGET_HINT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "budget-hint.schema.json"
PRIORITY_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "priority.schema.json"
TIMEOUT_POLICY_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "timeout-policy.schema.json"
EXECUTION_REQUEST_DOC_PATH = REPO_ROOT / "docs" / "specs" / "execution-request-contract.md"
AGENT_ROLE_DOC_PATH = REPO_ROOT / "docs" / "specs" / "agent-role-contract.md"
ACTION_TYPE_DOC_PATH = REPO_ROOT / "docs" / "specs" / "action-type-contract.md"
PRIORITY_DOC_PATH = REPO_ROOT / "docs" / "specs" / "priority-contract.md"
BUDGET_HINT_DOC_PATH = REPO_ROOT / "docs" / "specs" / "budget-hint-contract.md"
TIMEOUT_POLICY_DOC_PATH = REPO_ROOT / "docs" / "specs" / "timeout-policy-contract.md"

EXPECTED_COMMAND_REQUIRED = [
    "command_id",
    "channel",
    "user_id",
    "intent",
    "message",
    "created_at",
]

EXPECTED_RESPONSE_REQUIRED = [
    "response_id",
    "command_id",
    "channel",
    "user_id",
    "status",
    "message",
    "created_at",
]

EXPECTED_TRACEABILITY_REQUIRED = [
    "trace_id",
    "command_id",
    "session_id",
    "user_id",
    "channel",
    "created_at",
    "current_state",
]

EXPECTED_SESSION_CONTEXT_REQUIRED = [
    "session_id",
    "user_id",
    "channel",
    "session_status",
    "created_at",
]

EXPECTED_PROJECT_CONTEXT_REQUIRED = [
    "project_id",
    "project_name",
    "project_status",
    "created_at",
    "owner_user_id",
]

EXPECTED_COMPANY_CONTEXT_REQUIRED = [
    "company_id",
    "company_name",
    "company_status",
    "created_at",
    "owner_user_id",
]

EXPECTED_OWNER_IDENTITY_REQUIRED = [
    "user_id",
    "display_name",
    "identity_type",
    "created_at",
    "primary_channel",
]

EXPECTED_ARTIFACT_REFERENCE_REQUIRED = [
    "artifact_id",
    "artifact_name",
    "artifact_type",
    "artifact_uri",
    "created_at",
]

EXPECTED_PLANNING_ARTIFACT_REQUIRED = [
    "planning_artifact_id",
    "artifact_id",
    "project_id",
    "trace_id",
    "planning_type",
    "source_role",
    "created_at",
    "planning_status",
    "planning_horizon",
    "artifact_uri",
]

EXPECTED_QUALITY_GATE_REQUIRED = [
    "quality_gate_id",
    "gate_name",
    "gate_type",
    "gate_status",
    "created_at",
]

EXPECTED_EVIDENCE_BUNDLE_REQUIRED = [
    "evidence_bundle_id",
    "bundle_name",
    "bundle_status",
    "created_at",
]

EXPECTED_GOVERNANCE_DECISION_REQUIRED = [
    "governance_decision_id",
    "trace_id",
    "command_id",
    "user_id",
    "decision_type",
    "decision_scope",
    "created_at",
]

EXPECTED_APPROVAL_ACTION_REQUIRED = [
    "approval_action_id",
    "trace_id",
    "command_id",
    "user_id",
    "session_id",
    "decision",
    "created_at",
]

EXPECTED_EXECUTION_REQUEST_REQUIRED = [
    "execution_request_id",
    "trace_id",
    "command_id",
    "session_id",
    "user_id",
    "target_role",
    "action_type",
    "priority",
    "created_at",
]

EXPECTED_EXECUTION_RESULT_REQUIRED = [
    "execution_result_id",
    "execution_request_id",
    "trace_id",
    "command_id",
    "session_id",
    "user_id",
    "outcome",
    "created_at",
]

EXPECTED_RELEASE_DECISION_REQUIRED = [
    "release_decision_id",
    "decision_name",
    "release_status",
    "created_at",
]

EXPECTED_DELIVERY_PACKAGE_REQUIRED = [
    "delivery_package_id",
    "package_name",
    "package_status",
    "created_at",
]

EXPECTED_DEPLOYMENT_TARGET_REQUIRED = [
    "deployment_target_id",
    "target_name",
    "target_type",
    "target_status",
    "created_at",
]

EXPECTED_ORCHESTRATION_HANDOFF_REQUIRED = [
    "handoff_id",
    "trace_id",
    "command_id",
    "source_role",
    "target_role",
    "action_type",
    "handoff_status",
    "created_at",
    "priority",
]

EXPECTED_AGENT_ROLE_REQUIRED = [
    "role_id",
    "role_name",
    "role_type",
    "description",
]

EXPECTED_ACTION_TYPE_REQUIRED = [
    "action_type_id",
    "action_name",
    "action_type",
    "description",
]

EXPECTED_RUNTIME_CAPABILITY_REQUIRED = [
    "capability_id",
    "capability_name",
    "capability_status",
    "created_at",
    "role_type",
]

EXPECTED_TOOL_INVOCATION_REQUIRED = [
    "tool_invocation_id",
    "tool_name",
    "tool_type",
    "invocation_status",
    "created_at",
]

EXPECTED_BUDGET_HINT_REQUIRED = [
    "budget_hint_id",
    "trace_id",
    "command_id",
    "budget_amount",
    "budget_unit",
    "created_at",
    "scope",
]

EXPECTED_PRIORITY_REQUIRED = [
    "priority_id",
    "priority_name",
    "priority_level",
    "description",
]

EXPECTED_TIMEOUT_POLICY_REQUIRED = [
    "timeout_policy_id",
    "trace_id",
    "command_id",
    "timeout_seconds",
    "created_at",
    "scope",
    "timeout_strategy",
]

EXPECTED_CHANNEL_ENUM = [
    "telegram",
    "dashboard",
]

EXPECTED_SESSION_STATUS_ENUM = [
    "active",
    "paused",
    "closed",
]

EXPECTED_PROJECT_STATUS_ENUM = [
    "draft",
    "active",
    "paused",
    "archived",
]

EXPECTED_COMPANY_STATUS_ENUM = [
    "draft",
    "active",
    "paused",
    "archived",
]

EXPECTED_IDENTITY_TYPE_ENUM = [
    "human_owner",
    "human_operator",
    "service_account",
]

EXPECTED_PRIMARY_CHANNEL_ENUM = [
    "telegram",
    "dashboard",
    "system",
]

EXPECTED_ARTIFACT_TYPES = [
    "document",
    "schema",
    "script",
    "repository",
    "report",
    "binary",
    "other",
]

EXPECTED_PLANNING_TYPES = [
    "request_analysis",
    "work_plan",
    "architecture_plan",
    "execution_plan",
    "release_plan",
]

EXPECTED_PLANNING_STATUS_ENUM = [
    "draft",
    "active",
    "superseded",
    "archived",
]

EXPECTED_PLANNING_HORIZONS = [
    "immediate",
    "short_term",
    "mid_term",
    "long_term",
]

EXPECTED_QUALITY_GATE_TYPES = [
    "requirement_check",
    "schema_check",
    "quality_check",
    "acceptance_check",
    "release_check",
]

EXPECTED_QUALITY_GATE_STATUS_ENUM = [
    "pending",
    "passed",
    "failed",
    "waived",
]

EXPECTED_EVIDENCE_BUNDLE_STATUS_ENUM = [
    "draft",
    "collected",
    "reviewed",
    "accepted",
    "rejected",
]

EXPECTED_GOVERNANCE_DECISION_TYPES = [
    "allow",
    "deny",
    "escalate",
    "defer",
]

EXPECTED_GOVERNANCE_DECISION_SCOPES = [
    "request",
    "session",
    "project",
    "company",
]

EXPECTED_APPROVAL_DECISION_ENUM = [
    "approve",
    "reject",
]

EXPECTED_EXECUTION_PRIORITY_ENUM = [
    "low",
    "normal",
    "high",
    "critical",
]

EXPECTED_EXECUTION_OUTCOME_ENUM = [
    "completed",
    "failed",
    "cancelled",
    "timed_out",
]

EXPECTED_RELEASE_STATUS_ENUM = [
    "approved",
    "blocked",
    "deferred",
    "requires_review",
]

EXPECTED_RELEASE_SCOPE_ENUM = [
    "artifact",
    "project",
    "bundle",
]

EXPECTED_DELIVERY_PACKAGE_STATUS_ENUM = [
    "draft",
    "assembled",
    "approved",
    "published",
    "archived",
]

EXPECTED_DEPLOYMENT_TARGET_TYPE_ENUM = [
    "local_server",
    "container_host",
    "vm",
    "bare_metal",
    "cloud_service",
    "other",
]

EXPECTED_DEPLOYMENT_TARGET_STATUS_ENUM = [
    "draft",
    "ready",
    "active",
    "paused",
    "retired",
]

EXPECTED_ENVIRONMENT_NAME_ENUM = [
    "dev",
    "staging",
    "prod",
    "test",
    "other",
]

EXPECTED_HANDOFF_STATUS_ENUM = [
    "prepared",
    "dispatched",
    "accepted",
    "rejected",
    "cancelled",
]

EXPECTED_AGENT_ROLE_TYPES = [
    "ceo_agent",
    "planner_agent",
    "architect_agent",
    "repo_generator_agent",
    "developer_agent",
    "qa_agent",
    "devops_agent",
    "documentation_agent",
]

EXPECTED_ACTION_TYPES = [
    "analyze_request",
    "plan_work",
    "design_architecture",
    "generate_repository",
    "write_code",
    "run_checks",
    "deploy_service",
    "update_documentation",
]

EXPECTED_RUNTIME_CAPABILITY_STATUS_ENUM = [
    "available",
    "limited",
    "unavailable",
    "deprecated",
]

EXPECTED_TOOL_TYPES = [
    "script",
    "cli",
    "api",
    "agent_tool",
    "system_tool",
    "other",
]

EXPECTED_INVOCATION_STATUS_ENUM = [
    "prepared",
    "running",
    "succeeded",
    "failed",
    "cancelled",
]

EXPECTED_BUDGET_UNITS = [
    "usd",
    "credits",
    "tokens",
    "seconds",
]

EXPECTED_BUDGET_SCOPES = [
    "request",
    "session",
    "project",
]

EXPECTED_TIMEOUT_POLICY_SCOPES = [
    "request",
    "session",
    "project",
]

EXPECTED_TIMEOUT_STRATEGIES = [
    "fail",
    "cancel",
    "escalate",
    "mark_timed_out",
]

EXPECTED_STATUS_ENUM = [
    "accepted",
    "rejected",
    "requires_approval",
    "routed",
    "planned",
    "executing",
    "completed",
    "failed",
    "cancelled",
]

EXPECTED_INTENT_ENUM = [
    "create_project",
    "update_project",
    "request_status",
    "approve_action",
    "reject_action",
    "ask_question",
]

EXPECTED_COMMAND_STATES = [
    "received",
    "validated",
    "rejected",
    "accepted",
    "requires_approval",
    "approved",
    "routed",
    "planned",
    "executing",
    "completed",
    "failed",
    "cancelled",
]

EXPECTED_ALLOWED_TRANSITIONS = [
    ("received", "validated"),
    ("received", "rejected"),
    ("validated", "accepted"),
    ("validated", "rejected"),
    ("accepted", "requires_approval"),
    ("accepted", "routed"),
    ("requires_approval", "approved"),
    ("requires_approval", "cancelled"),
    ("approved", "routed"),
    ("routed", "planned"),
    ("planned", "executing"),
    ("executing", "completed"),
    ("executing", "failed"),
]

EXPECTED_FORBIDDEN_TRANSITIONS = [
    ("received", "executing"),
    ("accepted", "completed"),
]


def load_json_file(path):
    if not path.exists():
        return None, [f"Missing schema file: {path.relative_to(REPO_ROOT)}"]

    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as error:
        location = f"line {error.lineno}, column {error.colno}"
        return None, [f"Invalid JSON in {path.relative_to(REPO_ROOT)} at {location}: {error.msg}"]


def load_text_file(path):
    if not path.exists():
        return None, [f"Missing documentation file: {path.relative_to(REPO_ROOT)}"]

    try:
        return path.read_text(encoding="utf-8"), []
    except OSError as error:
        return None, [f"Unable to read {path.relative_to(REPO_ROOT)}: {error}"]


def ensure_required_fields(schema_name, schema, expected_fields):
    errors = []
    required_fields = schema.get("required")

    if not isinstance(required_fields, list):
        return [f"{schema_name}: 'required' must be a list"]

    for field_name in expected_fields:
        if field_name not in required_fields:
            errors.append(f"{schema_name}: missing required field '{field_name}'")

    return errors


def ensure_fields_not_required(schema_name, schema, field_names):
    errors = []
    required_fields = schema.get("required")

    if not isinstance(required_fields, list):
        return [f"{schema_name}: 'required' must be a list"]

    for field_name in field_names:
        if field_name in required_fields:
            errors.append(f"{schema_name}: field '{field_name}' must remain optional")

    return errors


def ensure_schema_type(schema_name, schema, expected_type):
    schema_type = schema.get("type")
    if schema_type != expected_type:
        return [f"{schema_name}: top-level 'type' must be '{expected_type}'"]
    return []


def ensure_top_level_value(schema_name, schema, property_name, expected_value):
    actual_value = schema.get(property_name)
    if actual_value != expected_value:
        return [f"{schema_name}: top-level '{property_name}' must be '{expected_value}'"]
    return []


def ensure_property_type(schema_name, schema, property_name, expected_type):
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return [f"{schema_name}: missing property definition for '{property_name}'"]

    property_type = property_schema.get("type")
    if property_type != expected_type:
        return [f"{schema_name}: '{property_name}.type' must be '{expected_type}'"]

    return []


def ensure_property_defined(schema_name, schema, property_name):
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return [f"{schema_name}: missing property definition for '{property_name}'"]

    return []


def ensure_string_min_length(schema_name, schema, property_name, expected_minimum):
    errors = ensure_property_type(schema_name, schema, property_name, "string")
    if errors:
        return errors

    properties = schema.get("properties")
    property_schema = properties.get(property_name)
    min_length = property_schema.get("minLength")

    if min_length != expected_minimum:
        return [f"{schema_name}: '{property_name}.minLength' must be {expected_minimum}"]

    return []


def ensure_numeric_minimum(schema_name, schema, property_name, expected_minimum):
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return [f"{schema_name}: missing property definition for '{property_name}'"]

    minimum = property_schema.get("minimum")
    if minimum != expected_minimum:
        return [f"{schema_name}: '{property_name}.minimum' must be {expected_minimum}"]

    return []


def ensure_property_format(schema_name, schema, property_name, expected_format):
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return [f"{schema_name}: missing property definition for '{property_name}'"]

    property_format = property_schema.get("format")
    if property_format != expected_format:
        return [f"{schema_name}: '{property_name}.format' must be '{expected_format}'"]

    return []


def ensure_array_items_type(schema_name, schema, property_name, expected_type):
    errors = ensure_property_type(schema_name, schema, property_name, "array")
    if errors:
        return errors

    properties = schema.get("properties")
    property_schema = properties.get(property_name)
    items_schema = property_schema.get("items")

    if not isinstance(items_schema, dict):
        return [f"{schema_name}: '{property_name}.items' must be an object"]

    item_type = items_schema.get("type")
    if item_type != expected_type:
        return [f"{schema_name}: '{property_name}.items.type' must be '{expected_type}'"]

    return []


def ensure_array_items_min_length(schema_name, schema, property_name, expected_minimum):
    errors = ensure_array_items_type(schema_name, schema, property_name, "string")
    if errors:
        return errors

    properties = schema.get("properties")
    property_schema = properties.get(property_name)
    items_schema = property_schema.get("items")
    min_length = items_schema.get("minLength")

    if min_length != expected_minimum:
        return [f"{schema_name}: '{property_name}.items.minLength' must be {expected_minimum}"]

    return []


def ensure_schema_uses_identifier(schema_name, schema, identifier_name):
    errors = ensure_property_defined(schema_name, schema, identifier_name)
    if errors:
        return errors

    return ensure_string_min_length(schema_name, schema, identifier_name, 1)


def ensure_enum_contains(schema_name, schema, property_name, expected_values):
    errors = []
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return [f"{schema_name}: missing property definition for '{property_name}'"]

    enum_values = property_schema.get("enum")
    if not isinstance(enum_values, list):
        return [f"{schema_name}: '{property_name}.enum' must be a list"]

    for value in expected_values:
        if value not in enum_values:
            errors.append(f"{schema_name}: missing enum value '{value}' in '{property_name}'")

    return errors


def ensure_enum_matches(schema_name, schema, property_name, expected_values):
    errors = ensure_enum_contains(schema_name, schema, property_name, expected_values)
    if errors:
        return errors

    properties = schema.get("properties")
    property_schema = properties.get(property_name)
    enum_values = property_schema.get("enum")

    unexpected_values = [value for value in enum_values if value not in expected_values]
    for value in unexpected_values:
        errors.append(f"{schema_name}: unexpected enum value '{value}' in '{property_name}'")

    return errors


def get_property_enum(schema_name, schema, property_name):
    properties = schema.get("properties")

    if not isinstance(properties, dict):
        return None, [f"{schema_name}: 'properties' must be an object"]

    property_schema = properties.get(property_name)
    if not isinstance(property_schema, dict):
        return None, [f"{schema_name}: missing property definition for '{property_name}'"]

    enum_values = property_schema.get("enum")
    if not isinstance(enum_values, list):
        return None, [f"{schema_name}: '{property_name}.enum' must be a list"]

    return enum_values, []


def ensure_property_enum_alignment(left_schema_name, left_schema, left_property_name, right_schema_name, right_schema, right_property_name):
    left_enum, left_errors = get_property_enum(left_schema_name, left_schema, left_property_name)
    if left_errors:
        return left_errors

    right_enum, right_errors = get_property_enum(right_schema_name, right_schema, right_property_name)
    if right_errors:
        return right_errors

    left_values = set(left_enum)
    right_values = set(right_enum)
    errors = []

    for value in sorted(right_values - left_values):
        errors.append(
            f"{left_schema_name}: missing enum value '{value}' in '{left_property_name}' compared to {right_schema_name}.{right_property_name}"
        )

    for value in sorted(left_values - right_values):
        errors.append(
            f"{left_schema_name}: unexpected enum value '{value}' in '{left_property_name}' compared to {right_schema_name}.{right_property_name}"
        )

    return errors


def ensure_doc_contains(doc_name, content, required_fragments):
    errors = []

    for fragment in required_fragments:
        if fragment not in content:
            errors.append(f"{doc_name}: missing required text '{fragment}'")

    return errors


def ensure_doc_mentions_values(doc_name, content, expected_values, context_label):
    errors = []

    for value in expected_values:
        if value not in content:
            errors.append(f"{doc_name}: missing {context_label} '{value}'")

    return errors


def ensure_example_values_match(doc_name, content, field_name, expected_values):
    errors = []
    pattern = re.compile(rf'"{re.escape(field_name)}"\s*:\s*"([^"]+)"')
    values = pattern.findall(content)

    for value in values:
        if value not in expected_values:
            errors.append(f"{doc_name}: example value '{value}' for '{field_name}' is not declared in role model")

    return errors


def ensure_string_list(rules_name, rules, property_name):
    values = rules.get(property_name)
    if not isinstance(values, list):
        return None, [f"{rules_name}: '{property_name}' must be a list"]

    invalid_values = [value for value in values if not isinstance(value, str)]
    if invalid_values:
        return None, [f"{rules_name}: '{property_name}' must contain only strings"]

    return values, []


def collect_transition_pairs(rules_name, rules, property_name):
    transitions = rules.get(property_name)
    if not isinstance(transitions, list):
        return None, [f"{rules_name}: '{property_name}' must be a list"]

    errors = []
    pairs = set()

    for index, transition in enumerate(transitions):
        label = f"{rules_name}: '{property_name}[{index}]'"

        if not isinstance(transition, dict):
            errors.append(f"{label} must be an object")
            continue

        source_state = transition.get("from")
        target_state = transition.get("to")

        if not isinstance(source_state, str) or not source_state:
            errors.append(f"{label}.from must be a non-empty string")
        if not isinstance(target_state, str) or not target_state:
            errors.append(f"{label}.to must be a non-empty string")

        if isinstance(source_state, str) and source_state and isinstance(target_state, str) and target_state:
            pairs.add((source_state, target_state))

    return pairs, errors


def ensure_states_contain(rules_name, states, expected_states):
    errors = []
    for state in expected_states:
        if state not in states:
            errors.append(f"{rules_name}: missing required state '{state}'")
    return errors


def ensure_transitions_contain(rules_name, transition_name, pairs, expected_pairs):
    errors = []
    for source_state, target_state in expected_pairs:
        if (source_state, target_state) not in pairs:
            errors.append(
                f"{rules_name}: missing transition '{source_state} -> {target_state}' in '{transition_name}'"
            )
    return errors


def ensure_terminal_states_declared(rules_name, states, terminal_states):
    errors = []

    for state in terminal_states:
        if state not in states:
            errors.append(f"{rules_name}: terminal state '{state}' must also exist in 'states'")

    return errors


def main():
    errors = []
    checks = []

    command_schema, command_load_errors = load_json_file(COMMAND_SCHEMA_PATH)
    errors.extend(command_load_errors)
    if not command_load_errors:
        checks.append(f"OK: {COMMAND_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {COMMAND_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "command.schema.json",
                command_schema,
                EXPECTED_COMMAND_REQUIRED,
            )
        )
        errors.extend(
            ensure_enum_contains(
                "command.schema.json",
                command_schema,
                "channel",
                EXPECTED_CHANNEL_ENUM,
            )
        )
        errors.extend(
            ensure_enum_contains(
                "command.schema.json",
                command_schema,
                "intent",
                EXPECTED_INTENT_ENUM,
            )
        )

    response_schema, response_load_errors = load_json_file(RESPONSE_SCHEMA_PATH)
    errors.extend(response_load_errors)
    if not response_load_errors:
        checks.append(f"OK: {RESPONSE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {RESPONSE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "response.schema.json",
                response_schema,
                EXPECTED_RESPONSE_REQUIRED,
            )
        )
        errors.extend(
            ensure_enum_contains(
                "response.schema.json",
                response_schema,
                "status",
                EXPECTED_STATUS_ENUM,
            )
        )

    state_rules, state_rules_load_errors = load_json_file(COMMAND_STATE_RULES_PATH)
    errors.extend(state_rules_load_errors)
    state_rules_states = None
    if not state_rules_load_errors:
        checks.append(f"OK: {COMMAND_STATE_RULES_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {COMMAND_STATE_RULES_PATH.relative_to(REPO_ROOT)} contains valid JSON")

        states, state_errors = ensure_string_list(
            "command-state-rules.json",
            state_rules,
            "states",
        )
        errors.extend(state_errors)
        state_rules_states = states

        terminal_states, terminal_state_errors = ensure_string_list(
            "command-state-rules.json",
            state_rules,
            "terminal_states",
        )
        errors.extend(terminal_state_errors)

        allowed_transitions, allowed_transition_errors = collect_transition_pairs(
            "command-state-rules.json",
            state_rules,
            "allowed_transitions",
        )
        errors.extend(allowed_transition_errors)

        forbidden_transitions, forbidden_transition_errors = collect_transition_pairs(
            "command-state-rules.json",
            state_rules,
            "forbidden_transitions",
        )
        errors.extend(forbidden_transition_errors)

        if states is not None:
            errors.extend(
                ensure_states_contain(
                    "command-state-rules.json",
                    states,
                    EXPECTED_COMMAND_STATES,
                )
            )

        if terminal_states is not None and states is not None:
            errors.extend(
                ensure_terminal_states_declared(
                    "command-state-rules.json",
                    states,
                    terminal_states,
                )
            )

        if allowed_transitions is not None:
            errors.extend(
                ensure_transitions_contain(
                    "command-state-rules.json",
                    "allowed_transitions",
                    allowed_transitions,
                    EXPECTED_ALLOWED_TRANSITIONS,
                )
            )

        if forbidden_transitions is not None:
            errors.extend(
                ensure_transitions_contain(
                    "command-state-rules.json",
                    "forbidden_transitions",
                    forbidden_transitions,
                    EXPECTED_FORBIDDEN_TRANSITIONS,
                )
            )

    traceability_schema, traceability_load_errors = load_json_file(TRACEABILITY_ENVELOPE_SCHEMA_PATH)
    errors.extend(traceability_load_errors)
    if not traceability_load_errors:
        checks.append(f"OK: {TRACEABILITY_ENVELOPE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {TRACEABILITY_ENVELOPE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "traceability-envelope.schema.json",
                traceability_schema,
                EXPECTED_TRACEABILITY_REQUIRED,
            )
        )
        errors.extend(
            ensure_property_defined(
                "traceability-envelope.schema.json",
                traceability_schema,
                "trace_id",
            )
        )
        errors.extend(
            ensure_property_defined(
                "traceability-envelope.schema.json",
                traceability_schema,
                "company_id",
            )
        )
        errors.extend(
            ensure_property_defined(
                "traceability-envelope.schema.json",
                traceability_schema,
                "project_id",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "traceability-envelope.schema.json",
                traceability_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "traceability-envelope.schema.json",
                traceability_schema,
                "company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "traceability-envelope.schema.json",
                traceability_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "traceability-envelope.schema.json",
                traceability_schema,
                "session_id",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "traceability-envelope.schema.json",
                traceability_schema,
                ["response_id"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "traceability-envelope.schema.json",
                traceability_schema,
                "channel",
                EXPECTED_CHANNEL_ENUM,
            )
        )

        if state_rules_states is not None:
            errors.extend(
                ensure_enum_matches(
                    "traceability-envelope.schema.json",
                    traceability_schema,
                    "current_state",
                    state_rules_states,
                )
            )

    session_context_schema, session_context_load_errors = load_json_file(SESSION_CONTEXT_SCHEMA_PATH)
    errors.extend(session_context_load_errors)
    if not session_context_load_errors:
        checks.append(f"OK: {SESSION_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {SESSION_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "session-context.schema.json",
                session_context_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "session-context.schema.json",
                session_context_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "session-context.schema.json",
                session_context_schema,
                EXPECTED_SESSION_CONTEXT_REQUIRED,
            )
        )
        errors.extend(
            ensure_property_defined(
                "session-context.schema.json",
                session_context_schema,
                "project_id",
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "session-context.schema.json",
                session_context_schema,
                [
                    "updated_at",
                    "active_trace_id",
                    "project_id",
                    "company_id",
                    "context_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "session_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "user_id",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "session-context.schema.json",
                session_context_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "session-context.schema.json",
                session_context_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_property_type(
                "session-context.schema.json",
                session_context_schema,
                "updated_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "session-context.schema.json",
                session_context_schema,
                "updated_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "active_trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "session-context.schema.json",
                session_context_schema,
                "context_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "session-context.schema.json",
                session_context_schema,
                "channel",
                EXPECTED_CHANNEL_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "session-context.schema.json",
                session_context_schema,
                "session_status",
                EXPECTED_SESSION_STATUS_ENUM,
            )
        )

    project_context_schema, project_context_load_errors = load_json_file(PROJECT_CONTEXT_SCHEMA_PATH)
    errors.extend(project_context_load_errors)
    if not project_context_load_errors:
        checks.append(f"OK: {PROJECT_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {PROJECT_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "project-context.schema.json",
                project_context_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "project-context.schema.json",
                project_context_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "project-context.schema.json",
                project_context_schema,
                EXPECTED_PROJECT_CONTEXT_REQUIRED,
            )
        )
        errors.extend(
            ensure_property_defined(
                "project-context.schema.json",
                project_context_schema,
                "project_id",
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "project-context.schema.json",
                project_context_schema,
                [
                    "updated_at",
                    "company_id",
                    "active_session_id",
                    "active_trace_id",
                    "project_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "project_name",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "project-context.schema.json",
                project_context_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "project-context.schema.json",
                project_context_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_property_type(
                "project-context.schema.json",
                project_context_schema,
                "updated_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "project-context.schema.json",
                project_context_schema,
                "updated_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "active_session_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "active_trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "owner_user_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "project-context.schema.json",
                project_context_schema,
                "project_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "project-context.schema.json",
                project_context_schema,
                "project_status",
                EXPECTED_PROJECT_STATUS_ENUM,
            )
        )

    company_context_schema, company_context_load_errors = load_json_file(COMPANY_CONTEXT_SCHEMA_PATH)
    errors.extend(company_context_load_errors)
    if not company_context_load_errors:
        checks.append(f"OK: {COMPANY_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {COMPANY_CONTEXT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "company-context.schema.json",
                company_context_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "company-context.schema.json",
                company_context_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "company-context.schema.json",
                company_context_schema,
                EXPECTED_COMPANY_CONTEXT_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "company-context.schema.json",
                company_context_schema,
                [
                    "updated_at",
                    "active_project_id",
                    "active_session_id",
                    "active_trace_id",
                    "company_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "company_name",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "company-context.schema.json",
                company_context_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "company-context.schema.json",
                company_context_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_property_type(
                "company-context.schema.json",
                company_context_schema,
                "updated_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "company-context.schema.json",
                company_context_schema,
                "updated_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "owner_user_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "active_project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "active_session_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "active_trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "company-context.schema.json",
                company_context_schema,
                "company_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "company-context.schema.json",
                company_context_schema,
                "company_status",
                EXPECTED_COMPANY_STATUS_ENUM,
            )
        )

    owner_identity_schema, owner_identity_load_errors = load_json_file(OWNER_IDENTITY_SCHEMA_PATH)
    errors.extend(owner_identity_load_errors)
    if not owner_identity_load_errors:
        checks.append(f"OK: {OWNER_IDENTITY_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {OWNER_IDENTITY_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "owner-identity.schema.json",
                owner_identity_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "owner-identity.schema.json",
                owner_identity_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "owner-identity.schema.json",
                owner_identity_schema,
                EXPECTED_OWNER_IDENTITY_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "owner-identity.schema.json",
                owner_identity_schema,
                [
                    "updated_at",
                    "telegram_user_id",
                    "dashboard_user_id",
                    "default_company_id",
                    "default_project_id",
                    "identity_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "user_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "display_name",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "owner-identity.schema.json",
                owner_identity_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "owner-identity.schema.json",
                owner_identity_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_property_type(
                "owner-identity.schema.json",
                owner_identity_schema,
                "updated_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "owner-identity.schema.json",
                owner_identity_schema,
                "updated_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "telegram_user_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "dashboard_user_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "default_company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "default_project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "owner-identity.schema.json",
                owner_identity_schema,
                "identity_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "owner-identity.schema.json",
                owner_identity_schema,
                "identity_type",
                EXPECTED_IDENTITY_TYPE_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "owner-identity.schema.json",
                owner_identity_schema,
                "primary_channel",
                EXPECTED_PRIMARY_CHANNEL_ENUM,
            )
        )

    artifact_reference_schema, artifact_reference_load_errors = load_json_file(ARTIFACT_REFERENCE_SCHEMA_PATH)
    errors.extend(artifact_reference_load_errors)
    if not artifact_reference_load_errors:
        checks.append(f"OK: {ARTIFACT_REFERENCE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {ARTIFACT_REFERENCE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                EXPECTED_ARTIFACT_REFERENCE_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                [
                    "trace_id",
                    "project_id",
                    "company_id",
                    "produced_by_execution_result_id",
                    "artifact_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_id",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_id",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_name",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_uri",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "company_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "produced_by_execution_result_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "artifact-reference.schema.json",
                artifact_reference_schema,
                "artifact_type",
                EXPECTED_ARTIFACT_TYPES,
            )
        )

    planning_artifact_schema, planning_artifact_load_errors = load_json_file(PLANNING_ARTIFACT_SCHEMA_PATH)
    errors.extend(planning_artifact_load_errors)
    if not planning_artifact_load_errors:
        checks.append(f"OK: {PLANNING_ARTIFACT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {PLANNING_ARTIFACT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                EXPECTED_PLANNING_ARTIFACT_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                ["planning_note"],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "planning_artifact_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "artifact_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "source_role",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "artifact_uri",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "planning_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "planning_type",
                EXPECTED_PLANNING_TYPES,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "planning_status",
                EXPECTED_PLANNING_STATUS_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "planning-artifact.schema.json",
                planning_artifact_schema,
                "planning_horizon",
                EXPECTED_PLANNING_HORIZONS,
            )
        )

    quality_gate_schema, quality_gate_load_errors = load_json_file(QUALITY_GATE_SCHEMA_PATH)
    errors.extend(quality_gate_load_errors)
    if not quality_gate_load_errors:
        checks.append(f"OK: {QUALITY_GATE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {QUALITY_GATE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "quality-gate.schema.json",
                quality_gate_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "quality-gate.schema.json",
                quality_gate_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "quality-gate.schema.json",
                quality_gate_schema,
                EXPECTED_QUALITY_GATE_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "quality-gate.schema.json",
                quality_gate_schema,
                [
                    "trace_id",
                    "project_id",
                    "artifact_id",
                    "execution_result_id",
                    "linked_governance_decision_id",
                    "evidence_uri",
                    "gate_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "quality_gate_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "gate_name",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "quality-gate.schema.json",
                quality_gate_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "quality-gate.schema.json",
                quality_gate_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "artifact_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "execution_result_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "linked_governance_decision_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "evidence_uri",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "quality-gate.schema.json",
                quality_gate_schema,
                "gate_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "quality-gate.schema.json",
                quality_gate_schema,
                "gate_type",
                EXPECTED_QUALITY_GATE_TYPES,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "quality-gate.schema.json",
                quality_gate_schema,
                "gate_status",
                EXPECTED_QUALITY_GATE_STATUS_ENUM,
            )
        )

    evidence_bundle_schema, evidence_bundle_load_errors = load_json_file(EVIDENCE_BUNDLE_SCHEMA_PATH)
    errors.extend(evidence_bundle_load_errors)
    if not evidence_bundle_load_errors:
        checks.append(f"OK: {EVIDENCE_BUNDLE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {EVIDENCE_BUNDLE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                EXPECTED_EVIDENCE_BUNDLE_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                [
                    "trace_id",
                    "project_id",
                    "linked_quality_gate_id",
                    "linked_execution_result_id",
                    "linked_governance_decision_id",
                    "artifact_ids",
                    "evidence_summary",
                    "bundle_note",
                ],
            )
        )
        for property_name in [
            "evidence_bundle_id",
            "bundle_name",
            "trace_id",
            "project_id",
            "linked_quality_gate_id",
            "linked_execution_result_id",
            "linked_governance_decision_id",
            "evidence_summary",
            "bundle_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "evidence-bundle.schema.json",
                    evidence_bundle_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_array_items_min_length(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "artifact_ids",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "evidence-bundle.schema.json",
                evidence_bundle_schema,
                "bundle_status",
                EXPECTED_EVIDENCE_BUNDLE_STATUS_ENUM,
            )
        )

    governance_decision_schema, governance_decision_load_errors = load_json_file(GOVERNANCE_DECISION_SCHEMA_PATH)
    errors.extend(governance_decision_load_errors)
    if not governance_decision_load_errors:
        checks.append(f"OK: {GOVERNANCE_DECISION_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {GOVERNANCE_DECISION_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "governance-decision.schema.json",
                governance_decision_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "governance-decision.schema.json",
                governance_decision_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "governance-decision.schema.json",
                governance_decision_schema,
                EXPECTED_GOVERNANCE_DECISION_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "governance-decision.schema.json",
                governance_decision_schema,
                [
                    "execution_request_id",
                    "rationale",
                    "linked_approval_action_id",
                    "linked_budget_hint_id",
                    "linked_timeout_policy_id",
                    "decision_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "governance_decision_id",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "governance-decision.schema.json",
                governance_decision_schema,
                "governance_decision_id",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "command_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "execution_request_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "user_id",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "governance-decision.schema.json",
                governance_decision_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "governance-decision.schema.json",
                governance_decision_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "rationale",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "linked_approval_action_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "linked_budget_hint_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "linked_timeout_policy_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "governance-decision.schema.json",
                governance_decision_schema,
                "decision_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "governance-decision.schema.json",
                governance_decision_schema,
                "decision_type",
                EXPECTED_GOVERNANCE_DECISION_TYPES,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "governance-decision.schema.json",
                governance_decision_schema,
                "decision_scope",
                EXPECTED_GOVERNANCE_DECISION_SCOPES,
            )
        )

    approval_action_schema, approval_action_load_errors = load_json_file(APPROVAL_ACTION_SCHEMA_PATH)
    errors.extend(approval_action_load_errors)
    if not approval_action_load_errors:
        checks.append(f"OK: {APPROVAL_ACTION_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {APPROVAL_ACTION_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "approval-action.schema.json",
                approval_action_schema,
                EXPECTED_APPROVAL_ACTION_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "approval-action.schema.json",
                approval_action_schema,
                ["reason", "comment"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "approval-action.schema.json",
                approval_action_schema,
                "decision",
                EXPECTED_APPROVAL_DECISION_ENUM,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "approval-action.schema.json",
                approval_action_schema,
                "approval_action_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "approval-action.schema.json",
                approval_action_schema,
                "user_id",
                1,
            )
        )

    priority_schema, priority_load_errors = load_json_file(PRIORITY_SCHEMA_PATH)
    errors.extend(priority_load_errors)
    if not priority_load_errors:
        checks.append(f"OK: {PRIORITY_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {PRIORITY_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_schema_type(
                "priority.schema.json",
                priority_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "priority.schema.json",
                priority_schema,
                EXPECTED_PRIORITY_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "priority.schema.json",
                priority_schema,
                "priority_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "priority.schema.json",
                priority_schema,
                "priority_name",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "priority.schema.json",
                priority_schema,
                "description",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "priority.schema.json",
                priority_schema,
                ["recommended_use_cases"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "priority.schema.json",
                priority_schema,
                "priority_level",
                EXPECTED_EXECUTION_PRIORITY_ENUM,
            )
        )
        errors.extend(
            ensure_array_items_type(
                "priority.schema.json",
                priority_schema,
                "recommended_use_cases",
                "string",
            )
        )

    execution_request_schema, execution_request_load_errors = load_json_file(EXECUTION_REQUEST_SCHEMA_PATH)
    errors.extend(execution_request_load_errors)
    if not execution_request_load_errors:
        checks.append(f"OK: {EXECUTION_REQUEST_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {EXECUTION_REQUEST_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "execution-request.schema.json",
                execution_request_schema,
                EXPECTED_EXECUTION_REQUEST_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-request.schema.json",
                execution_request_schema,
                "execution_request_id",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "execution-request.schema.json",
                execution_request_schema,
                "execution_request_id",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-request.schema.json",
                execution_request_schema,
                "project_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-request.schema.json",
                execution_request_schema,
                "session_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-request.schema.json",
                execution_request_schema,
                "target_role",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "execution-request.schema.json",
                execution_request_schema,
                ["project_id", "timeout_seconds", "budget_hint", "payload"],
            )
        )
        errors.extend(
            ensure_property_defined(
                "execution-request.schema.json",
                execution_request_schema,
                "project_id",
            )
        )
        errors.extend(
            ensure_property_defined(
                "execution-request.schema.json",
                execution_request_schema,
                "timeout_seconds",
            )
        )
        errors.extend(
            ensure_property_type(
                "execution-request.schema.json",
                execution_request_schema,
                "timeout_seconds",
                "integer",
            )
        )
        errors.extend(
            ensure_numeric_minimum(
                "execution-request.schema.json",
                execution_request_schema,
                "timeout_seconds",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "execution-request.schema.json",
                execution_request_schema,
                "budget_hint",
            )
        )
        errors.extend(
            ensure_enum_matches(
                "execution-request.schema.json",
                execution_request_schema,
                "priority",
                EXPECTED_EXECUTION_PRIORITY_ENUM,
            )
        )
        if not priority_load_errors:
            errors.extend(
                ensure_property_enum_alignment(
                    "execution-request.schema.json",
                    execution_request_schema,
                    "priority",
                    "priority.schema.json",
                    priority_schema,
                    "priority_level",
                )
            )

    orchestration_handoff_schema, orchestration_handoff_load_errors = load_json_file(ORCHESTRATION_HANDOFF_SCHEMA_PATH)
    errors.extend(orchestration_handoff_load_errors)
    if not orchestration_handoff_load_errors:
        checks.append(f"OK: {ORCHESTRATION_HANDOFF_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {ORCHESTRATION_HANDOFF_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                EXPECTED_ORCHESTRATION_HANDOFF_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                [
                    "execution_request_id",
                    "linked_governance_decision_id",
                    "linked_artifact_id",
                    "handoff_note",
                ],
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "handoff_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "command_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "execution_request_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "source_role",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "target_role",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "action_type",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "linked_governance_decision_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "linked_artifact_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "handoff_note",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "handoff_status",
                EXPECTED_HANDOFF_STATUS_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "orchestration-handoff.schema.json",
                orchestration_handoff_schema,
                "priority",
                EXPECTED_EXECUTION_PRIORITY_ENUM,
            )
        )
        if not priority_load_errors:
            errors.extend(
                ensure_property_enum_alignment(
                    "orchestration-handoff.schema.json",
                    orchestration_handoff_schema,
                    "priority",
                    "priority.schema.json",
                    priority_schema,
                    "priority_level",
                )
            )

    budget_hint_schema, budget_hint_load_errors = load_json_file(BUDGET_HINT_SCHEMA_PATH)
    errors.extend(budget_hint_load_errors)
    if not budget_hint_load_errors:
        checks.append(f"OK: {BUDGET_HINT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {BUDGET_HINT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_schema_type(
                "budget-hint.schema.json",
                budget_hint_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "budget-hint.schema.json",
                budget_hint_schema,
                EXPECTED_BUDGET_HINT_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "budget-hint.schema.json",
                budget_hint_schema,
                "budget_hint_id",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "budget-hint.schema.json",
                budget_hint_schema,
                "budget_unit",
                EXPECTED_BUDGET_UNITS,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "budget-hint.schema.json",
                budget_hint_schema,
                "scope",
                EXPECTED_BUDGET_SCOPES,
            )
        )
        errors.extend(
            ensure_property_format(
                "budget-hint.schema.json",
                budget_hint_schema,
                "created_at",
                "date-time",
            )
        )

    timeout_policy_schema, timeout_policy_load_errors = load_json_file(TIMEOUT_POLICY_SCHEMA_PATH)
    errors.extend(timeout_policy_load_errors)
    if not timeout_policy_load_errors:
        checks.append(f"OK: {TIMEOUT_POLICY_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {TIMEOUT_POLICY_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_schema_type(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                EXPECTED_TIMEOUT_POLICY_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "timeout_policy_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "trace_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "command_id",
                1,
            )
        )
        errors.extend(
            ensure_property_type(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "timeout_seconds",
                "integer",
            )
        )
        errors.extend(
            ensure_numeric_minimum(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "timeout_seconds",
                1,
            )
        )
        errors.extend(
            ensure_property_format(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                ["note"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "scope",
                EXPECTED_TIMEOUT_POLICY_SCOPES,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "timeout-policy.schema.json",
                timeout_policy_schema,
                "timeout_strategy",
                EXPECTED_TIMEOUT_STRATEGIES,
            )
        )

    execution_result_schema, execution_result_load_errors = load_json_file(EXECUTION_RESULT_SCHEMA_PATH)
    errors.extend(execution_result_load_errors)
    if not execution_result_load_errors:
        checks.append(f"OK: {EXECUTION_RESULT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {EXECUTION_RESULT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_property_defined(
                "execution-result.schema.json",
                execution_result_schema,
                "execution_result_id",
            )
        )
        errors.extend(
            ensure_required_fields(
                "execution-result.schema.json",
                execution_result_schema,
                EXPECTED_EXECUTION_RESULT_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-result.schema.json",
                execution_result_schema,
                "execution_result_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "execution-result.schema.json",
                execution_result_schema,
                "session_id",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "execution-result.schema.json",
                execution_result_schema,
                [
                    "completed_at",
                    "status_message",
                    "result_payload",
                    "error_code",
                    "error_message",
                ],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "execution-result.schema.json",
                execution_result_schema,
                "outcome",
                EXPECTED_EXECUTION_OUTCOME_ENUM,
            )
        )
        errors.extend(
            ensure_enum_contains(
                "execution-result.schema.json",
                execution_result_schema,
                "outcome",
                ["timed_out"],
            )
        )

    release_decision_schema, release_decision_load_errors = load_json_file(RELEASE_DECISION_SCHEMA_PATH)
    errors.extend(release_decision_load_errors)
    if not release_decision_load_errors:
        checks.append(f"OK: {RELEASE_DECISION_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {RELEASE_DECISION_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "release-decision.schema.json",
                release_decision_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "release-decision.schema.json",
                release_decision_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "release-decision.schema.json",
                release_decision_schema,
                EXPECTED_RELEASE_DECISION_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "release-decision.schema.json",
                release_decision_schema,
                [
                    "trace_id",
                    "project_id",
                    "execution_result_id",
                    "artifact_id",
                    "linked_quality_gate_id",
                    "linked_evidence_bundle_id",
                    "linked_governance_decision_id",
                    "release_scope",
                    "release_note",
                ],
            )
        )
        for property_name in [
            "release_decision_id",
            "decision_name",
            "trace_id",
            "project_id",
            "execution_result_id",
            "artifact_id",
            "linked_quality_gate_id",
            "linked_evidence_bundle_id",
            "linked_governance_decision_id",
            "release_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "release-decision.schema.json",
                    release_decision_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "release-decision.schema.json",
                release_decision_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "release-decision.schema.json",
                release_decision_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_enum_matches(
                "release-decision.schema.json",
                release_decision_schema,
                "release_status",
                EXPECTED_RELEASE_STATUS_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "release-decision.schema.json",
                release_decision_schema,
                "release_scope",
                EXPECTED_RELEASE_SCOPE_ENUM,
            )
        )

    delivery_package_schema, delivery_package_load_errors = load_json_file(DELIVERY_PACKAGE_SCHEMA_PATH)
    errors.extend(delivery_package_load_errors)
    if not delivery_package_load_errors:
        checks.append(f"OK: {DELIVERY_PACKAGE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {DELIVERY_PACKAGE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "delivery-package.schema.json",
                delivery_package_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "delivery-package.schema.json",
                delivery_package_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "delivery-package.schema.json",
                delivery_package_schema,
                EXPECTED_DELIVERY_PACKAGE_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "delivery-package.schema.json",
                delivery_package_schema,
                [
                    "project_id",
                    "trace_id",
                    "artifact_ids",
                    "linked_evidence_bundle_id",
                    "linked_release_decision_id",
                    "linked_execution_result_id",
                    "package_uri",
                    "package_note",
                ],
            )
        )
        for property_name in [
            "delivery_package_id",
            "package_name",
            "project_id",
            "trace_id",
            "linked_evidence_bundle_id",
            "linked_release_decision_id",
            "linked_execution_result_id",
            "package_uri",
            "package_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "delivery-package.schema.json",
                    delivery_package_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "delivery-package.schema.json",
                delivery_package_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "delivery-package.schema.json",
                delivery_package_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_array_items_type(
                "delivery-package.schema.json",
                delivery_package_schema,
                "artifact_ids",
                "string",
            )
        )
        errors.extend(
            ensure_array_items_min_length(
                "delivery-package.schema.json",
                delivery_package_schema,
                "artifact_ids",
                1,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "delivery-package.schema.json",
                delivery_package_schema,
                "package_status",
                EXPECTED_DELIVERY_PACKAGE_STATUS_ENUM,
            )
        )

    deployment_target_schema, deployment_target_load_errors = load_json_file(DEPLOYMENT_TARGET_SCHEMA_PATH)
    errors.extend(deployment_target_load_errors)
    if not deployment_target_load_errors:
        checks.append(f"OK: {DEPLOYMENT_TARGET_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {DEPLOYMENT_TARGET_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "deployment-target.schema.json",
                deployment_target_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "deployment-target.schema.json",
                deployment_target_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "deployment-target.schema.json",
                deployment_target_schema,
                EXPECTED_DEPLOYMENT_TARGET_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "deployment-target.schema.json",
                deployment_target_schema,
                [
                    "project_id",
                    "company_id",
                    "linked_delivery_package_id",
                    "linked_release_decision_id",
                    "environment_name",
                    "target_uri",
                    "target_note",
                ],
            )
        )
        for property_name in [
            "deployment_target_id",
            "target_name",
            "project_id",
            "company_id",
            "linked_delivery_package_id",
            "linked_release_decision_id",
            "target_uri",
            "target_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "deployment-target.schema.json",
                    deployment_target_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "deployment-target.schema.json",
                deployment_target_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "deployment-target.schema.json",
                deployment_target_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_enum_matches(
                "deployment-target.schema.json",
                deployment_target_schema,
                "target_type",
                EXPECTED_DEPLOYMENT_TARGET_TYPE_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "deployment-target.schema.json",
                deployment_target_schema,
                "target_status",
                EXPECTED_DEPLOYMENT_TARGET_STATUS_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "deployment-target.schema.json",
                deployment_target_schema,
                "environment_name",
                EXPECTED_ENVIRONMENT_NAME_ENUM,
            )
        )

    runtime_capability_schema, runtime_capability_load_errors = load_json_file(RUNTIME_CAPABILITY_SCHEMA_PATH)
    errors.extend(runtime_capability_load_errors)
    if not runtime_capability_load_errors:
        checks.append(f"OK: {RUNTIME_CAPABILITY_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {RUNTIME_CAPABILITY_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                EXPECTED_RUNTIME_CAPABILITY_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                [
                    "deployment_target_id",
                    "supported_action_types",
                    "supports_local_execution",
                    "supports_remote_execution",
                    "supports_file_artifacts",
                    "supports_deployment",
                    "supports_validation",
                    "capability_note",
                ],
            )
        )
        for property_name in [
            "capability_id",
            "capability_name",
            "deployment_target_id",
            "capability_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "runtime-capability.schema.json",
                    runtime_capability_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_enum_matches(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "capability_status",
                EXPECTED_RUNTIME_CAPABILITY_STATUS_ENUM,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "role_type",
                EXPECTED_AGENT_ROLE_TYPES,
            )
        )
        errors.extend(
            ensure_array_items_type(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "supported_action_types",
                "string",
            )
        )
        errors.extend(
            ensure_array_items_min_length(
                "runtime-capability.schema.json",
                runtime_capability_schema,
                "supported_action_types",
                1,
            )
        )
        for property_name in [
            "supports_local_execution",
            "supports_remote_execution",
            "supports_file_artifacts",
            "supports_deployment",
            "supports_validation",
        ]:
            errors.extend(
                ensure_property_type(
                    "runtime-capability.schema.json",
                    runtime_capability_schema,
                    property_name,
                    "boolean",
                )
            )

    tool_invocation_schema, tool_invocation_load_errors = load_json_file(TOOL_INVOCATION_SCHEMA_PATH)
    errors.extend(tool_invocation_load_errors)
    if not tool_invocation_load_errors:
        checks.append(f"OK: {TOOL_INVOCATION_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {TOOL_INVOCATION_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_top_level_value(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "$schema",
                "https://json-schema.org/draft/2020-12/schema",
            )
        )
        errors.extend(
            ensure_schema_type(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                EXPECTED_TOOL_INVOCATION_REQUIRED,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                [
                    "trace_id",
                    "execution_request_id",
                    "execution_result_id",
                    "handoff_id",
                    "role_type",
                    "action_type",
                    "input_reference",
                    "output_reference",
                    "tool_note",
                ],
            )
        )
        for property_name in [
            "tool_invocation_id",
            "tool_name",
            "trace_id",
            "execution_request_id",
            "execution_result_id",
            "handoff_id",
            "role_type",
            "action_type",
            "input_reference",
            "output_reference",
            "tool_note",
        ]:
            errors.extend(
                ensure_string_min_length(
                    "tool-invocation.schema.json",
                    tool_invocation_schema,
                    property_name,
                    1,
                )
            )
        errors.extend(
            ensure_property_type(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "created_at",
                "string",
            )
        )
        errors.extend(
            ensure_property_format(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "created_at",
                "date-time",
            )
        )
        errors.extend(
            ensure_enum_matches(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "tool_type",
                EXPECTED_TOOL_TYPES,
            )
        )
        errors.extend(
            ensure_enum_matches(
                "tool-invocation.schema.json",
                tool_invocation_schema,
                "invocation_status",
                EXPECTED_INVOCATION_STATUS_ENUM,
            )
        )

    identifier_checks = [
        ("quality-gate.schema.json", quality_gate_schema, quality_gate_load_errors, "quality_gate_id"),
        ("evidence-bundle.schema.json", evidence_bundle_schema, evidence_bundle_load_errors, "evidence_bundle_id"),
        ("execution-request.schema.json", execution_request_schema, execution_request_load_errors, "execution_request_id"),
        ("execution-result.schema.json", execution_result_schema, execution_result_load_errors, "execution_result_id"),
        ("release-decision.schema.json", release_decision_schema, release_decision_load_errors, "release_decision_id"),
        ("governance-decision.schema.json", governance_decision_schema, governance_decision_load_errors, "governance_decision_id"),
        ("artifact-reference.schema.json", artifact_reference_schema, artifact_reference_load_errors, "artifact_id"),
        ("traceability-envelope.schema.json", traceability_schema, traceability_load_errors, "trace_id"),
        ("project-context.schema.json", project_context_schema, project_context_load_errors, "project_id"),
        ("company-context.schema.json", company_context_schema, company_context_load_errors, "company_id"),
        ("delivery-package.schema.json", delivery_package_schema, delivery_package_load_errors, "delivery_package_id"),
        ("deployment-target.schema.json", deployment_target_schema, deployment_target_load_errors, "deployment_target_id"),
        ("orchestration-handoff.schema.json", orchestration_handoff_schema, orchestration_handoff_load_errors, "handoff_id"),
        ("runtime-capability.schema.json", runtime_capability_schema, runtime_capability_load_errors, "capability_id"),
        ("tool-invocation.schema.json", tool_invocation_schema, tool_invocation_load_errors, "tool_invocation_id"),
    ]

    for schema_name, schema, load_errors, identifier_name in identifier_checks:
        if load_errors:
            continue

        identifier_errors = ensure_schema_uses_identifier(schema_name, schema, identifier_name)
        errors.extend(identifier_errors)
        if not identifier_errors:
            checks.append(f"OK: {schema_name} uses {identifier_name}")

    agent_role_schema, agent_role_load_errors = load_json_file(AGENT_ROLE_SCHEMA_PATH)
    errors.extend(agent_role_load_errors)
    if not agent_role_load_errors:
        checks.append(f"OK: {AGENT_ROLE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {AGENT_ROLE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_schema_type(
                "agent-role.schema.json",
                agent_role_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "agent-role.schema.json",
                agent_role_schema,
                EXPECTED_AGENT_ROLE_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "agent-role.schema.json",
                agent_role_schema,
                "role_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "agent-role.schema.json",
                agent_role_schema,
                "role_name",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "agent-role.schema.json",
                agent_role_schema,
                "role_type",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "agent-role.schema.json",
                agent_role_schema,
                "description",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "agent-role.schema.json",
                agent_role_schema,
                ["allowed_action_types"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "agent-role.schema.json",
                agent_role_schema,
                "role_type",
                EXPECTED_AGENT_ROLE_TYPES,
            )
        )
        errors.extend(
            ensure_array_items_type(
                "agent-role.schema.json",
                agent_role_schema,
                "allowed_action_types",
                "string",
            )
        )
        role_type_identifier_errors = ensure_property_type(
            "agent-role.schema.json",
            agent_role_schema,
            "role_type",
            "string",
        )
        errors.extend(role_type_identifier_errors)
        if not role_type_identifier_errors:
            checks.append("OK: agent-role.schema.json uses role_type")
        if not traceability_load_errors and not project_context_load_errors and not artifact_reference_load_errors:
            checks.append(
                "OK: trace_id, project_id, artifact_id, and role_type remain explicitly defined in their source contracts"
            )

    action_type_schema, action_type_load_errors = load_json_file(ACTION_TYPE_SCHEMA_PATH)
    errors.extend(action_type_load_errors)
    if not action_type_load_errors:
        checks.append(f"OK: {ACTION_TYPE_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {ACTION_TYPE_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_schema_type(
                "action-type.schema.json",
                action_type_schema,
                "object",
            )
        )
        errors.extend(
            ensure_required_fields(
                "action-type.schema.json",
                action_type_schema,
                EXPECTED_ACTION_TYPE_REQUIRED,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "action-type.schema.json",
                action_type_schema,
                "action_type_id",
                1,
            )
        )
        errors.extend(
            ensure_string_min_length(
                "action-type.schema.json",
                action_type_schema,
                "action_name",
                1,
            )
        )
        errors.extend(
            ensure_property_defined(
                "action-type.schema.json",
                action_type_schema,
                "action_type",
            )
        )
        errors.extend(
            ensure_string_min_length(
                "action-type.schema.json",
                action_type_schema,
                "description",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "action-type.schema.json",
                action_type_schema,
                ["recommended_roles"],
            )
        )
        errors.extend(
            ensure_enum_matches(
                "action-type.schema.json",
                action_type_schema,
                "action_type",
                EXPECTED_ACTION_TYPES,
            )
        )
        errors.extend(
            ensure_array_items_type(
                "action-type.schema.json",
                action_type_schema,
                "recommended_roles",
                "string",
            )
        )
        action_type_identifier_errors = ensure_property_type(
            "action-type.schema.json",
            action_type_schema,
            "action_type",
            "string",
        )
        errors.extend(action_type_identifier_errors)
        if not action_type_identifier_errors:
            checks.append("OK: action-type.schema.json uses action_type")

    execution_request_doc, execution_request_doc_errors = load_text_file(EXECUTION_REQUEST_DOC_PATH)
    errors.extend(execution_request_doc_errors)
    if not execution_request_doc_errors:
        checks.append(f"OK: {EXECUTION_REQUEST_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "execution-request-contract.md",
                execution_request_doc,
                [
                    "`target_role` определяет логическую роль исполнителя.",
                    "docs/specs/action-type-contract.md",
                    "docs/specs/agent-role-contract.md",
                ],
            )
        )
        errors.extend(
            ensure_example_values_match(
                "execution-request-contract.md",
                execution_request_doc,
                "target_role",
                EXPECTED_AGENT_ROLE_TYPES,
            )
        )
        errors.extend(
            ensure_example_values_match(
                "execution-request-contract.md",
                execution_request_doc,
                "action_type",
                EXPECTED_ACTION_TYPES,
            )
        )

    agent_role_doc, agent_role_doc_errors = load_text_file(AGENT_ROLE_DOC_PATH)
    errors.extend(agent_role_doc_errors)
    if not agent_role_doc_errors:
        checks.append(f"OK: {AGENT_ROLE_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "agent-role-contract.md",
                agent_role_doc,
                [
                    "execution-request.target_role",
                    "не является runtime registry.",
                    "не является org chart implementation.",
                    "не является permission system.",
                    "не является scheduling layer.",
                ],
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "agent-role-contract.md",
                agent_role_doc,
                EXPECTED_AGENT_ROLE_TYPES,
                "role type",
            )
        )

    action_type_doc, action_type_doc_errors = load_text_file(ACTION_TYPE_DOC_PATH)
    errors.extend(action_type_doc_errors)
    if not action_type_doc_errors:
        checks.append(f"OK: {ACTION_TYPE_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "action-type-contract.md",
                action_type_doc,
                [
                    "execution-request.action_type",
                    "agent-role.allowed_action_types",
                    "не является runtime queue taxonomy.",
                    "не является scheduler.",
                    "не является permission system.",
                    "не является execution engine.",
                ],
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "action-type-contract.md",
                action_type_doc,
                EXPECTED_ACTION_TYPES,
                "action type",
            )
        )

    priority_doc, priority_doc_errors = load_text_file(PRIORITY_DOC_PATH)
    errors.extend(priority_doc_errors)
    if not priority_doc_errors:
        checks.append(f"OK: {PRIORITY_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "priority-contract.md",
                priority_doc,
                [
                    "`execution-request.priority`",
                    "relative importance and urgency",
                    "advisory routing",
                    "planning and orchestration hints",
                    "future linkage с approvals, budget и execution",
                    "не является scheduler.",
                    "не является queue engine.",
                    "не является SLA engine.",
                    "не является runtime enforcement policy.",
                ],
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "priority-contract.md",
                priority_doc,
                EXPECTED_EXECUTION_PRIORITY_ENUM,
                "priority level",
            )
        )

    budget_hint_doc, budget_hint_doc_errors = load_text_file(BUDGET_HINT_DOC_PATH)
    errors.extend(budget_hint_doc_errors)
    if not budget_hint_doc_errors:
        checks.append(f"OK: {BUDGET_HINT_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "budget-hint-contract.md",
                budget_hint_doc,
                [
                    "`execution-request.budget_hint`",
                    "advisory budget signal",
                    "не является budget enforcement runtime.",
                    "не является accounting system.",
                ],
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "budget-hint-contract.md",
                budget_hint_doc,
                EXPECTED_BUDGET_SCOPES,
                "scope",
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "budget-hint-contract.md",
                budget_hint_doc,
                EXPECTED_BUDGET_UNITS,
                "budget unit",
            )
        )

    timeout_policy_doc, timeout_policy_doc_errors = load_text_file(TIMEOUT_POLICY_DOC_PATH)
    errors.extend(timeout_policy_doc_errors)
    if not timeout_policy_doc_errors:
        checks.append(f"OK: {TIMEOUT_POLICY_DOC_PATH.relative_to(REPO_ROOT)} exists")
        errors.extend(
            ensure_doc_contains(
                "timeout-policy-contract.md",
                timeout_policy_doc,
                [
                    "`execution-request.timeout_seconds`",
                    "`trace_id`",
                    "`command_id`",
                    "advisory ограничения по времени",
                    "не является runtime worker timeout handler.",
                    "не является scheduler.",
                    "не является queue engine.",
                    "не является orchestration runtime.",
                    "advisory planning",
                    "execution-request guidance",
                    "future linkage with execution_result.outcome = timed_out",
                ],
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "timeout-policy-contract.md",
                timeout_policy_doc,
                EXPECTED_TIMEOUT_POLICY_SCOPES,
                "scope",
            )
        )
        errors.extend(
            ensure_doc_mentions_values(
                "timeout-policy-contract.md",
                timeout_policy_doc,
                EXPECTED_TIMEOUT_STRATEGIES,
                "timeout strategy",
            )
        )

    if errors:
        print("Shared contracts verification: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Shared contracts verification: PASSED")
    for check in checks:
        print(f"- {check}")
    print(
        "- OK: required fields, target enums, command state rules, traceability envelope, session context contract, project context contract, company context contract, owner identity contract, artifact reference contract, planning artifact contract, quality gate contract, evidence bundle contract, governance decision contract, approval action contract, execution request contract, orchestration handoff contract, priority contract, budget hint contract, timeout policy contract, execution result contract, release decision contract, delivery package contract, deployment target contract, agent role contract, action type contract, runtime capability contract, and tool invocation contract match the current shared contract expectations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
