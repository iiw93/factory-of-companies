#!/usr/bin/env python3

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

COMMAND_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "command.schema.json"
RESPONSE_SCHEMA_PATH = REPO_ROOT / "packages" / "shared-contracts" / "response.schema.json"

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

EXPECTED_CHANNEL_ENUM = [
    "telegram",
    "dashboard",
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

    if errors:
        print("Shared contracts verification: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Shared contracts verification: PASSED")
    for check in checks:
        print(f"- {check}")
    print("- OK: required fields and target enums match the current shared contract expectations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
