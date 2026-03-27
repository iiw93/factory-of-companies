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
APPROVAL_ACTION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "approval-action.schema.json"
EXECUTION_REQUEST_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "execution-request.schema.json"
EXECUTION_RESULT_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "execution-result.schema.json"
AGENT_ROLE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "agent-role.schema.json"
ACTION_TYPE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "action-type.schema.json"
EXECUTION_REQUEST_DOC_PATH = REPO_ROOT / "docs" / "specs" / "execution-request-contract.md"
AGENT_ROLE_DOC_PATH = REPO_ROOT / "docs" / "specs" / "agent-role-contract.md"
ACTION_TYPE_DOC_PATH = REPO_ROOT / "docs" / "specs" / "action-type-contract.md"

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

EXPECTED_CHANNEL_ENUM = [
    "telegram",
    "dashboard",
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
                "target_role",
                1,
            )
        )
        errors.extend(
            ensure_fields_not_required(
                "execution-request.schema.json",
                execution_request_schema,
                ["timeout_seconds", "budget_hint", "payload"],
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

    execution_result_schema, execution_result_load_errors = load_json_file(EXECUTION_RESULT_SCHEMA_PATH)
    errors.extend(execution_result_load_errors)
    if not execution_result_load_errors:
        checks.append(f"OK: {EXECUTION_RESULT_SCHEMA_PATH.relative_to(REPO_ROOT)} exists")
        checks.append(f"OK: {EXECUTION_RESULT_SCHEMA_PATH.relative_to(REPO_ROOT)} contains valid JSON")
        errors.extend(
            ensure_required_fields(
                "execution-result.schema.json",
                execution_result_schema,
                EXPECTED_EXECUTION_RESULT_REQUIRED,
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

    if errors:
        print("Shared contracts verification: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Shared contracts verification: PASSED")
    for check in checks:
        print(f"- {check}")
    print(
        "- OK: required fields, target enums, command state rules, traceability envelope, approval action contract, execution request contract, execution result contract, agent role contract, and action type contract match the current shared contract expectations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
