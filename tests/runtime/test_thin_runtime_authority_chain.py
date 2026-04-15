from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_MODULE_PATH = REPO_ROOT / "packages" / "paperclip-adapter" / "src" / "paperclip_adapter" / "thin_runtime.py"
CARRIER_FIELD = "execution-request.mediation-identity+trace.carrier"
BINDING_NAME = "scenario-01.execution-request->boundary-edge.mediation-binding"


def load_runtime_module():
    spec = importlib.util.spec_from_file_location("thin_runtime_authority_chain", RUNTIME_MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ThinRuntimeAuthorityChainTest(unittest.TestCase):
    def test_scenario_01_authority_chain_is_aligned_end_to_end(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-001",
            "2026-04-14T00:00:00Z",
            "happy_path",
        )

        execution_request = result["execution_request"]
        knowledge_retrieval = result["knowledge_retrieval"]
        orchestration_handoff = result["orchestration_handoff"]
        boundary_edge_mediation_binding = result["boundary_edge_mediation_binding"]

        execution_request_carrier = execution_request[CARRIER_FIELD]
        orchestration_handoff_carrier = orchestration_handoff[CARRIER_FIELD]
        boundary_edge_carrier = boundary_edge_mediation_binding[CARRIER_FIELD]

        self.assertEqual(result["runtime_status"], "completed")
        self.assertIn("execution_request", result)
        self.assertEqual(sorted(execution_request_carrier.keys()), ["mediation_identity", "trace"])
        self.assertEqual(
            execution_request_carrier["mediation_identity"],
            execution_request["execution_request_id"],
        )
        self.assertEqual(execution_request_carrier["trace"], result["trace_id"])

        self.assertIn("orchestration_handoff", result)
        self.assertEqual(
            orchestration_handoff["execution_request_id"],
            execution_request["execution_request_id"],
        )
        self.assertEqual(orchestration_handoff["command_id"], execution_request["command_id"])
        self.assertEqual(orchestration_handoff["trace_id"], execution_request["trace_id"])
        self.assertEqual(orchestration_handoff["target_role"], execution_request["target_role"])
        self.assertEqual(orchestration_handoff["action_type"], execution_request["action_type"])
        self.assertEqual(orchestration_handoff["priority"], execution_request["priority"])
        self.assertEqual(orchestration_handoff["linked_artifact_id"], knowledge_retrieval["knowledge_retrieval_id"])
        self.assertEqual(orchestration_handoff["handoff_status"], "prepared")
        self.assertEqual(orchestration_handoff_carrier, execution_request_carrier)

        self.assertIn("boundary_edge_mediation_binding", result)
        self.assertEqual(boundary_edge_mediation_binding["binding_name"], BINDING_NAME)
        self.assertEqual(
            boundary_edge_mediation_binding["execution_request_id"],
            execution_request["execution_request_id"],
        )
        self.assertEqual(
            boundary_edge_mediation_binding["handoff_id"],
            orchestration_handoff["handoff_id"],
        )
        self.assertEqual(boundary_edge_mediation_binding["trace_id"], orchestration_handoff["trace_id"])
        self.assertEqual(boundary_edge_carrier, execution_request_carrier)

        self.assertEqual(
            execution_request["payload"]["mediation_binding_name"],
            BINDING_NAME,
        )
        self.assertNotIn("mediation_identity", orchestration_handoff)
        self.assertNotIn("mediation_identity", boundary_edge_mediation_binding)


    def test_scenario_01_forced_failure_orchestration_alignment_is_preserved(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-failure-001",
            "2026-04-14T00:00:00Z",
            "forced_failure",
        )

        execution_request = result["execution_request"]
        knowledge_retrieval = result["knowledge_retrieval"]
        orchestration_handoff = result["orchestration_handoff"]
        boundary_edge_mediation_binding = result["boundary_edge_mediation_binding"]

        execution_request_carrier = execution_request[CARRIER_FIELD]
        orchestration_handoff_carrier = orchestration_handoff[CARRIER_FIELD]
        boundary_edge_carrier = boundary_edge_mediation_binding[CARRIER_FIELD]

        self.assertEqual(result["runtime_status"], "failed")
        self.assertIsNone(result["retrieval_result"])
        self.assertEqual(orchestration_handoff["command_id"], execution_request["command_id"])
        self.assertEqual(orchestration_handoff["trace_id"], execution_request["trace_id"])
        self.assertEqual(orchestration_handoff["target_role"], execution_request["target_role"])
        self.assertEqual(orchestration_handoff["action_type"], execution_request["action_type"])
        self.assertEqual(orchestration_handoff["priority"], execution_request["priority"])
        self.assertEqual(orchestration_handoff["linked_artifact_id"], knowledge_retrieval["knowledge_retrieval_id"])
        self.assertEqual(orchestration_handoff["handoff_status"], "prepared")
        self.assertEqual(orchestration_handoff_carrier, execution_request_carrier)
        self.assertEqual(
            boundary_edge_mediation_binding["execution_request_id"],
            execution_request["execution_request_id"],
        )
        self.assertEqual(
            boundary_edge_mediation_binding["handoff_id"],
            orchestration_handoff["handoff_id"],
        )
        self.assertEqual(boundary_edge_mediation_binding["trace_id"], orchestration_handoff["trace_id"])
        self.assertEqual(boundary_edge_carrier, execution_request_carrier)
        self.assertEqual(boundary_edge_mediation_binding["binding_name"], BINDING_NAME)

    def test_runtime_entry_rejects_carrier_missing_mediation_identity(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-missing-mediation-identity",
            "2026-04-14T00:00:00Z",
            "happy_path",
        )
        knowledge_retrieval = dict(result["knowledge_retrieval"])
        knowledge_retrieval[CARRIER_FIELD] = {"trace": result["trace_id"]}

        with self.assertRaisesRegex(runtime_module.SourceIntakeValidationError, "mediation_identity"):
            runtime_module.create_execution_request(
                knowledge_retrieval,
                result["retrieval_session"],
                "2026-04-14T00:00:01Z",
            )

    def test_runtime_entry_rejects_carrier_missing_trace(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-missing-trace",
            "2026-04-14T00:00:00Z",
            "happy_path",
        )
        knowledge_retrieval = dict(result["knowledge_retrieval"])
        knowledge_retrieval[CARRIER_FIELD] = {"mediation_identity": knowledge_retrieval["execution_request_id"]}

        with self.assertRaisesRegex(runtime_module.SourceIntakeValidationError, "trace"):
            runtime_module.create_execution_request(
                knowledge_retrieval,
                result["retrieval_session"],
                "2026-04-14T00:00:01Z",
            )

    def test_orchestration_handoff_rejects_carrier_mutation(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-carrier-mutation",
            "2026-04-14T00:00:00Z",
            "happy_path",
        )
        execution_request = dict(result["execution_request"])
        execution_request[CARRIER_FIELD] = {
            "mediation_identity": "execution-request-mutated",
            "trace": result["trace_id"],
        }

        with self.assertRaisesRegex(runtime_module.SourceIntakeValidationError, "mediation_identity"):
            runtime_module.create_orchestration_handoff(
                execution_request,
                result["knowledge_retrieval"],
                "2026-04-14T00:00:01Z",
            )

    def test_boundary_edge_rejects_handoff_carrier_misalignment(self) -> None:
        runtime_module = load_runtime_module()
        result = runtime_module.run_thin_runtime_intake_normalization(
            {
                "source_type": "document",
                "source_name": "Scenario 01 source",
                "source_text": "First line\nSecond line",
                "source_uri": None,
            },
            "trace-authority-chain-handoff-misalignment",
            "2026-04-14T00:00:00Z",
            "happy_path",
        )
        orchestration_handoff = dict(result["orchestration_handoff"])
        orchestration_handoff[CARRIER_FIELD] = {
            "mediation_identity": result["execution_request"]["execution_request_id"],
            "trace": "trace-authority-chain-handoff-misalignment-mutated",
        }

        with self.assertRaisesRegex(runtime_module.SourceIntakeValidationError, "handoff carrier"):
            runtime_module.create_boundary_edge_mediation_binding(
                result["execution_request"],
                orchestration_handoff,
                "2026-04-14T00:00:01Z",
            )


if __name__ == "__main__":
    unittest.main()
