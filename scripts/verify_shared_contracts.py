#!/usr/bin/env python3

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

COMMAND_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "command.schema.json"
RESPONSE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "response.schema.json"
COMMAND_STATE_RULES_PATH = REPO_ROOT / "packages" / "shared-contracts" / "command-state-rules.json"
TRACEABILITY_ENVELOPE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "traceability-envelope.schema.json"
APPROVAL_ACTION_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "approval-action.schema.json"

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

EXPECTED_CHANNEL_ENUM = [
    "telegram",
    "dashboard",
]

EXPECTED_APPROVAL_DECISION_ENUM = [
    "approve",
    "reject",
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

    if errors:
        print("Shared contracts verification: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Shared contracts verification: PASSED")
    for check in checks:
        print(f"- {check}")
    print(
        "- OK: required fields, target enums, command state rules, traceability envelope, and approval action contract match the current shared contract expectations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
