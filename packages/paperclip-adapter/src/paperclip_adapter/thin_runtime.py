from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Any


SCENARIO_ID = "thin-runtime-mvp-scenario-01"
CONTRACT_VERSION = "0.1.0"
APPROVED_SOURCE_TYPE = "document"
APPROVED_PROVIDER_NAME = "gemini-embedding-2"
APPROVED_PROVIDER_TYPE = "gemini_embedding"
APPROVED_MODALITY_SCOPE = "text_only"
APPROVED_INDEX_BACKEND = "local_file_index"
APPROVED_RETRIEVAL_QUERY_TEXT = "Second line"
EXECUTION_REQUEST_CARRIER_FIELD = "execution-request.mediation-identity+trace.carrier"
MEDIATION_BINDING_NAME = "scenario-01.execution-request->boundary-edge.mediation-binding"
ALLOWED_EXECUTION_MODES = {"happy_path", "forced_failure"}
DEFAULT_SOURCE_ROLE = "planner_agent"
DEFAULT_TARGET_ROLE = "developer_agent"
DEFAULT_ACTION_TYPE = "write_code"
DEFAULT_PRIORITY = "normal"
DEFAULT_HANDOFF_STATUS = "prepared"
DEFAULT_USER_ID = "scenario-01-runtime"
DEFAULT_BOUNDARY_EDGE_STATUS = "prepared"


class SourceIntakeValidationError(ValueError):
    pass


@dataclass(frozen=True)
class FailureReport:
    stage_name: str
    reason: str

    def as_dict(self) -> dict[str, str]:
        return {"stage_name": self.stage_name, "reason": self.reason}


def stable_id(prefix: str, *parts: Any) -> str:
    digest = sha256("::".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def validate_source_input(source_input: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(source_input, dict):
        raise SourceIntakeValidationError("source_input must be a dictionary")
    if source_input.get("source_type") != APPROVED_SOURCE_TYPE:
        raise SourceIntakeValidationError("scenario-01 only accepts document source_type")
    if not str(source_input.get("source_text") or "").strip():
        raise SourceIntakeValidationError("source_text is required")
    return source_input


def validate_execution_mode(execution_mode: str) -> str:
    if execution_mode not in ALLOWED_EXECUTION_MODES:
        raise SourceIntakeValidationError(f"unsupported execution_mode: {execution_mode}")
    return execution_mode


def validate_authoritative_carrier(
    carrier: dict[str, Any] | None,
    *,
    expected_mediation_identity: str,
    expected_trace: str,
    context: str,
) -> dict[str, str]:
    if not isinstance(carrier, dict):
        raise SourceIntakeValidationError(f"{context} carrier must be a dictionary")
    mediation_identity = carrier.get("mediation_identity")
    if not mediation_identity:
        raise SourceIntakeValidationError(f"{context} carrier must include mediation_identity")
    trace = carrier.get("trace")
    if not trace:
        raise SourceIntakeValidationError(f"{context} carrier must include trace")
    if mediation_identity != expected_mediation_identity:
        raise SourceIntakeValidationError(f"{context} carrier mediation_identity must remain authoritative")
    if trace != expected_trace:
        raise SourceIntakeValidationError(f"{context} carrier trace must remain authoritative")
    return {"mediation_identity": mediation_identity, "trace": trace}


def intake_source(source_input: dict[str, Any], trace_id: str, created_at: str) -> dict[str, Any]:
    return {
        "knowledge_source_id": stable_id("knowledge-source", trace_id, source_input.get("source_name"), created_at),
        "contract_version": CONTRACT_VERSION,
        "scenario_id": SCENARIO_ID,
        "source_type": source_input["source_type"],
        "source_name": source_input.get("source_name") or "scenario-01-source",
        "source_uri": source_input.get("source_uri"),
        "source_text": source_input["source_text"],
        "created_at": created_at,
        "trace_id": trace_id,
    }


def normalize_text(source_text: str) -> str:
    return "\n".join(line.rstrip() for line in source_text.replace("\r\n", "\n").split("\n")).strip()


def normalize_source_text(knowledge_source: dict[str, Any], created_at: str) -> dict[str, Any]:
    normalized_text = normalize_text(knowledge_source["source_text"])
    return {
        "normalized_artifact_id": stable_id("normalized-artifact", knowledge_source["knowledge_source_id"], normalized_text),
        "contract_version": CONTRACT_VERSION,
        "knowledge_source_id": knowledge_source["knowledge_source_id"],
        "normalized_text": normalized_text,
        "line_count": len(normalized_text.splitlines()) if normalized_text else 0,
        "created_at": created_at,
        "trace_id": knowledge_source["trace_id"],
    }


def resolve_embedding_provider(trace_id: str, created_at: str) -> dict[str, Any]:
    provider_id = stable_id("embedding-provider", APPROVED_PROVIDER_NAME, trace_id)
    return {
        "embedding_provider_id": provider_id,
        "contract_version": CONTRACT_VERSION,
        "provider_name": APPROVED_PROVIDER_NAME,
        "provider_type": APPROVED_PROVIDER_TYPE,
        "modality_scope": APPROVED_MODALITY_SCOPE,
        "created_at": created_at,
        "trace_id": trace_id,
    }


def create_embedding_job(normalized_source: dict[str, Any], embedding_provider: dict[str, Any], created_at: str) -> dict[str, Any]:
    return {
        "embedding_job_id": stable_id("embedding-job", normalized_source["normalized_artifact_id"], embedding_provider["embedding_provider_id"]),
        "contract_version": CONTRACT_VERSION,
        "normalized_artifact_id": normalized_source["normalized_artifact_id"],
        "embedding_provider_id": embedding_provider["embedding_provider_id"],
        "created_at": created_at,
        "trace_id": normalized_source["trace_id"],
    }


def build_stub_embedding_vector(normalized_text: str) -> list[float]:
    digest = sha256(normalized_text.encode("utf-8")).digest()[:8]
    return [round(byte / 255, 6) for byte in digest]


def execute_embedding_stub(embedding_job: dict[str, Any], normalized_source: dict[str, Any], created_at: str) -> dict[str, Any]:
    return {
        "embedding_output_id": stable_id("embedding-output", embedding_job["embedding_job_id"], normalized_source["normalized_artifact_id"]),
        "contract_version": CONTRACT_VERSION,
        "embedding_job_id": embedding_job["embedding_job_id"],
        "normalized_artifact_id": normalized_source["normalized_artifact_id"],
        "vector": build_stub_embedding_vector(normalized_source["normalized_text"]),
        "created_at": created_at,
        "trace_id": embedding_job["trace_id"],
    }


def create_retrieval_index(embedding_output: dict[str, Any], created_at: str) -> dict[str, Any]:
    return {
        "retrieval_index_id": stable_id("retrieval-index", embedding_output["embedding_output_id"]),
        "contract_version": CONTRACT_VERSION,
        "index_backend": APPROVED_INDEX_BACKEND,
        "embedding_output_id": embedding_output["embedding_output_id"],
        "created_at": created_at,
        "trace_id": embedding_output["trace_id"],
    }


def build_next_retrieval_input(knowledge_source: dict[str, Any], normalized_source: dict[str, Any], embedding_provider: dict[str, Any], embedding_job: dict[str, Any], retrieval_index: dict[str, Any], trace_id: str) -> dict[str, Any]:
    return {
        "knowledge_source_id": knowledge_source["knowledge_source_id"],
        "normalized_artifact_id": normalized_source["normalized_artifact_id"],
        "embedding_provider_id": embedding_provider["embedding_provider_id"],
        "embedding_job_id": embedding_job["embedding_job_id"],
        "retrieval_index_id": retrieval_index["retrieval_index_id"],
        "retrieval_query_text": APPROVED_RETRIEVAL_QUERY_TEXT,
        "trace_id": trace_id,
    }


def execute_retrieval_stub(next_retrieval_input: dict[str, Any], created_at: str) -> dict[str, Any]:
    trace_id = next_retrieval_input["trace_id"]
    execution_request_id = stable_id(
        "execution-request",
        trace_id,
        next_retrieval_input["knowledge_source_id"],
        next_retrieval_input["normalized_artifact_id"],
        next_retrieval_input["embedding_provider_id"],
        next_retrieval_input["embedding_job_id"],
        next_retrieval_input["retrieval_index_id"],
        next_retrieval_input["retrieval_query_text"],
    )
    context_selection_id = stable_id(
        "context-selection",
        trace_id,
        next_retrieval_input["knowledge_source_id"],
        next_retrieval_input["normalized_artifact_id"],
        next_retrieval_input["retrieval_index_id"],
    )
    carrier = {
        "mediation_identity": execution_request_id,
        "trace": trace_id,
    }
    return {
        "knowledge_retrieval_id": stable_id("knowledge-retrieval", execution_request_id, context_selection_id),
        "contract_version": CONTRACT_VERSION,
        "retrieval_status": "completed",
        "retrieval_mode": "stubbed-local",
        "query_text": next_retrieval_input["retrieval_query_text"],
        "created_at": created_at,
        "trace_id": trace_id,
        "execution_request_id": execution_request_id,
        "context_selection_id": context_selection_id,
        "selected_source_ids": [next_retrieval_input["knowledge_source_id"]],
        "retrieved_artifact_ids": [next_retrieval_input["normalized_artifact_id"]],
        "retrieval_constraints": {"scenario_scope": "scenario-01-only"},
        "ranking_hint": "authoritative-carrier-ready",
        "token_budget_hint": 512,
        EXECUTION_REQUEST_CARRIER_FIELD: carrier,
        "mediation_binding_name": MEDIATION_BINDING_NAME,
    }


def create_retrieval_session(knowledge_retrieval: dict[str, Any], created_at: str) -> dict[str, Any]:
    return {
        "retrieval_session_id": stable_id("retrieval-session", knowledge_retrieval["knowledge_retrieval_id"]),
        "contract_version": CONTRACT_VERSION,
        "session_name": "scenario-01 retrieval session",
        "session_status": "completed",
        "knowledge_retrieval_id": knowledge_retrieval["knowledge_retrieval_id"],
        "created_at": created_at,
        "trace_id": knowledge_retrieval["trace_id"],
        "context_selection_id": knowledge_retrieval["context_selection_id"],
        "linked_knowledge_retrieval_id": knowledge_retrieval["knowledge_retrieval_id"],
        "selected_source_ids": knowledge_retrieval["selected_source_ids"],
        "retrieval_outcome": "sufficient",
        "session_note": "Scenario-01 retrieval session stays aligned with orchestration handoff preparation.",
    }


def create_retrieval_result(knowledge_retrieval: dict[str, Any], retrieval_session: dict[str, Any], created_at: str) -> dict[str, Any]:
    return {
        "retrieval_result_id": stable_id("retrieval-result", retrieval_session["retrieval_session_id"]),
        "contract_version": CONTRACT_VERSION,
        "knowledge_retrieval_id": knowledge_retrieval["knowledge_retrieval_id"],
        "retrieval_session_id": retrieval_session["retrieval_session_id"],
        "created_at": created_at,
        "trace_id": knowledge_retrieval["trace_id"],
        EXECUTION_REQUEST_CARRIER_FIELD: knowledge_retrieval[EXECUTION_REQUEST_CARRIER_FIELD],
    }


def create_execution_request(knowledge_retrieval: dict[str, Any], retrieval_session: dict[str, Any], created_at: str) -> dict[str, Any]:
    command_id = stable_id("command", knowledge_retrieval["trace_id"], knowledge_retrieval["knowledge_retrieval_id"])
    carrier = validate_authoritative_carrier(
        knowledge_retrieval.get(EXECUTION_REQUEST_CARRIER_FIELD),
        expected_mediation_identity=knowledge_retrieval["execution_request_id"],
        expected_trace=knowledge_retrieval["trace_id"],
        context="runtime-entry",
    )
    return {
        "execution_request_id": knowledge_retrieval["execution_request_id"],
        "trace_id": knowledge_retrieval["trace_id"],
        "command_id": command_id,
        "session_id": retrieval_session["retrieval_session_id"],
        "user_id": DEFAULT_USER_ID,
        "target_role": DEFAULT_TARGET_ROLE,
        "action_type": DEFAULT_ACTION_TYPE,
        "priority": DEFAULT_PRIORITY,
        "created_at": created_at,
        EXECUTION_REQUEST_CARRIER_FIELD: carrier,
        "payload": {
            "mediation_binding_name": MEDIATION_BINDING_NAME,
            "context_selection_id": knowledge_retrieval["context_selection_id"],
            "selected_source_ids": knowledge_retrieval["selected_source_ids"],
        },
    }


def create_orchestration_handoff(execution_request: dict[str, Any], knowledge_retrieval: dict[str, Any], created_at: str) -> dict[str, Any]:
    carrier = validate_authoritative_carrier(
        execution_request.get(EXECUTION_REQUEST_CARRIER_FIELD),
        expected_mediation_identity=execution_request["execution_request_id"],
        expected_trace=execution_request["trace_id"],
        context="orchestration-handoff",
    )
    return {
        "handoff_id": stable_id("handoff", execution_request["execution_request_id"], execution_request["command_id"]),
        "trace_id": execution_request["trace_id"],
        "command_id": execution_request["command_id"],
        "execution_request_id": execution_request["execution_request_id"],
        "source_role": DEFAULT_SOURCE_ROLE,
        "target_role": execution_request["target_role"],
        "action_type": execution_request["action_type"],
        "handoff_status": DEFAULT_HANDOFF_STATUS,
        "created_at": created_at,
        "priority": execution_request["priority"],
        "linked_artifact_id": knowledge_retrieval["knowledge_retrieval_id"],
        EXECUTION_REQUEST_CARRIER_FIELD: carrier,
        "handoff_note": "Scenario-01 runtime seed prepares the mediation-binding handoff surface only.",
    }


def create_boundary_edge_mediation_binding(execution_request: dict[str, Any], orchestration_handoff: dict[str, Any], created_at: str) -> dict[str, Any]:
    execution_request_carrier = validate_authoritative_carrier(
        execution_request.get(EXECUTION_REQUEST_CARRIER_FIELD),
        expected_mediation_identity=execution_request["execution_request_id"],
        expected_trace=execution_request["trace_id"],
        context="boundary-edge",
    )
    handoff_carrier = validate_authoritative_carrier(
        orchestration_handoff.get(EXECUTION_REQUEST_CARRIER_FIELD),
        expected_mediation_identity=execution_request["execution_request_id"],
        expected_trace=execution_request["trace_id"],
        context="boundary-edge handoff",
    )
    if handoff_carrier != execution_request_carrier:
        raise SourceIntakeValidationError("boundary-edge handoff carrier must remain aligned with execution-request carrier")
    return {
        "boundary_edge_binding_id": stable_id("boundary-edge-binding", orchestration_handoff["handoff_id"], execution_request["execution_request_id"]),
        "binding_name": MEDIATION_BINDING_NAME,
        "binding_status": DEFAULT_BOUNDARY_EDGE_STATUS,
        "created_at": created_at,
        "trace_id": execution_request["trace_id"],
        "execution_request_id": execution_request["execution_request_id"],
        "handoff_id": orchestration_handoff["handoff_id"],
        EXECUTION_REQUEST_CARRIER_FIELD: execution_request_carrier,
    }


def build_observability_events(runtime_status: str, terminal_stage_name: str, trace_id: str, created_at: str) -> list[dict[str, str]]:
    return [{"event_name": "scenario-01.runtime", "runtime_status": runtime_status, "terminal_stage_name": terminal_stage_name, "trace_id": trace_id, "created_at": created_at}]


def build_trace_steps(runtime_status: str, terminal_stage_name: str, trace_id: str, created_at: str) -> list[dict[str, str]]:
    return [{"step_name": "runtime-entry", "runtime_status": runtime_status, "terminal_stage_name": terminal_stage_name, "trace_id": trace_id, "created_at": created_at}]


def build_failure_reports(failure_report: FailureReport | None) -> list[dict[str, str]]:
    return [] if failure_report is None else [failure_report.as_dict()]


def build_debug_node_views(knowledge_retrieval: dict[str, Any] | None) -> list[dict[str, Any]]:
    return [] if knowledge_retrieval is None else [{"node_name": "execution-request", "view": knowledge_retrieval}]


def build_pipeline_view(runtime_status: str, terminal_stage_name: str) -> dict[str, str]:
    return {"runtime_status": runtime_status, "terminal_stage_name": terminal_stage_name}


def build_debug_panel(knowledge_retrieval: dict[str, Any] | None) -> dict[str, Any]:
    return {"authoritative_carrier_present": bool(knowledge_retrieval and knowledge_retrieval.get(EXECUTION_REQUEST_CARRIER_FIELD))}


def run_thin_runtime_intake_normalization(source_input: dict[str, Any], trace_id: str, created_at: str, execution_mode: str = "happy_path") -> dict[str, Any]:
    validate_source_input(source_input)
    validate_execution_mode(execution_mode)

    knowledge_source = intake_source(source_input, trace_id, created_at)
    normalized_source = normalize_source_text(knowledge_source, created_at)
    embedding_provider = resolve_embedding_provider(trace_id, created_at)
    embedding_job = create_embedding_job(normalized_source, embedding_provider, created_at)
    embedding_output = execute_embedding_stub(embedding_job, normalized_source, created_at)
    retrieval_index = create_retrieval_index(embedding_output, created_at)
    next_embedding_input = {
        "normalized_artifact_id": normalized_source["normalized_artifact_id"],
        "embedding_provider_id": embedding_provider["embedding_provider_id"],
        "trace_id": trace_id,
    }
    next_retrieval_input = build_next_retrieval_input(knowledge_source, normalized_source, embedding_provider, embedding_job, retrieval_index, trace_id)
    knowledge_retrieval = execute_retrieval_stub(next_retrieval_input, created_at)
    retrieval_session = create_retrieval_session(knowledge_retrieval, created_at)
    execution_request = create_execution_request(knowledge_retrieval, retrieval_session, created_at)
    retrieval_session["execution_request_id"] = execution_request["execution_request_id"]
    orchestration_handoff = create_orchestration_handoff(execution_request, knowledge_retrieval, created_at)
    boundary_edge_mediation_binding = create_boundary_edge_mediation_binding(execution_request, orchestration_handoff, created_at)

    retrieval_result = None
    runtime_status = "completed"
    terminal_stage_name = "retrieval_result_creation"
    failure_report = None
    if execution_mode == "happy_path":
        retrieval_result = create_retrieval_result(knowledge_retrieval, retrieval_session, created_at)
    else:
        runtime_status = "failed"
        failure_report = FailureReport(stage_name="retrieval-result-creation", reason="forced_failure")

    observability_events = build_observability_events(runtime_status, terminal_stage_name, trace_id, created_at)
    trace_steps = build_trace_steps(runtime_status, terminal_stage_name, trace_id, created_at)
    failure_reports = build_failure_reports(failure_report)
    debug_node_views = build_debug_node_views(knowledge_retrieval)
    pipeline_view = build_pipeline_view(runtime_status, terminal_stage_name)
    debug_panel = build_debug_panel(knowledge_retrieval)

    return {
        "scenario_id": SCENARIO_ID,
        "created_at": created_at,
        "trace_id": trace_id,
        "execution_mode": execution_mode,
        "runtime_status": runtime_status,
        "terminal_stage_name": terminal_stage_name,
        "knowledge_source": knowledge_source,
        "normalized_source": normalized_source,
        "embedding_provider": embedding_provider,
        "embedding_job": embedding_job,
        "embedding_output": embedding_output,
        "retrieval_index": retrieval_index,
        "execution_request": execution_request,
        "knowledge_retrieval": knowledge_retrieval,
        "orchestration_handoff": orchestration_handoff,
        "boundary_edge_mediation_binding": boundary_edge_mediation_binding,
        "retrieval_session": retrieval_session,
        "retrieval_result": retrieval_result,
        "observability_events": observability_events,
        "trace_steps": trace_steps,
        "failure_reports": failure_reports,
        "debug_node_views": debug_node_views,
        "pipeline_view": pipeline_view,
        "debug_panel": debug_panel,
        "next_embedding_input": next_embedding_input,
        "next_retrieval_input": next_retrieval_input,
    }
