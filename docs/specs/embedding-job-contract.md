# Embedding Job Contract

## Goal
Define a standalone embedding job contract without introducing a runtime embedding executor.

## Purpose
Embedding job contract describes a single indexing or embedding creation operation in the knowledge and retrieval layer.

It records one embedding-oriented job that links an embedding provider to one or more knowledge sources and can optionally reference retrieval-level context.

## Embedding Job Object

```json
{
  "embedding_job_id": "embedding-job-0001",
  "job_name": "company-context-index-build",
  "job_status": "completed",
  "created_at": "2026-03-28T07:00:00Z",
  "embedding_provider_id": "embedding-provider-0001",
  "knowledge_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "trace_id": "trace-0001",
  "linked_knowledge_retrieval_id": "retrieval-0001",
  "linked_retrieval_session_id": "retrieval-session-0001",
  "modality_scope": "text_only",
  "output_dimension": 3072,
  "chunk_count": 24,
  "job_note": "Embedding job recorded for future retrieval and observability linkage"
}
```

## Required Fields
- `embedding_job_id`
- `job_name`
- `job_status`
- `created_at`
- `embedding_provider_id`

## Optional Fields
- `knowledge_source_ids`
- `trace_id`
- `linked_knowledge_retrieval_id`
- `linked_retrieval_session_id`
- `modality_scope`
- `output_dimension`
- `chunk_count`
- `job_note`

## Field Semantics
### embedding_job_id
Unique identifier of the embedding job contract.

### job_name
Human-readable name of the embedding or indexing operation.

### job_status
Contract-level embedding job lifecycle state.

Allowed values:
- `draft`
- `prepared`
- `running`
- `completed`
- `failed`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### embedding_provider_id
Reference to the embedding provider used by this job.

### knowledge_source_ids
Array of references to knowledge sources included in the embedding job.

### trace_id
Optional reference to traceability envelope context.

### linked_knowledge_retrieval_id
Optional reference to a knowledge retrieval contract.

### linked_retrieval_session_id
Optional reference to a retrieval session contract.

### modality_scope
Optional contract-level modality scope for the embedding job.

Allowed values:
- `text_only`
- `text_image`
- `text_audio`
- `text_video`
- `multimodal`

### output_dimension
Optional output embedding dimension represented as an integer with minimum value `1`.

### chunk_count
Optional chunk count represented as an integer with minimum value `0`.

### job_note
Optional explanatory note for engineering or audit context.

## Linkage
Embedding job contract is expected to link:
- `embedding_provider_id`
- `knowledge_source_id`
- `trace_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`

## Engineering Rule
Embedding job uses an embedding provider, but it does not replace retrieval session or retrieval result contracts.

## Rules
1. `knowledge_source_ids` is an array of references to knowledge sources.
2. `output_dimension` is a numeric characteristic of job output, not runtime execution logic.
3. `chunk_count` is a numeric descriptor of processed chunks, not a worker control field.
4. Linked retrieval fields are optional references only.
5. `job_note`, when present, is an optional explanation and not executable configuration.

## Boundaries
This is not a runtime embedding worker.

This is not a vector DB.

This is not a retrieval engine.

This is not a storage service.

## Expected Usage
- fixation of indexing or embedding creation fact
- linkage between provider and sources
- future observability, audit and index build views

## Source Alignment
`docs/specs/embedding-job-contract.md` defines embedding job semantics for the knowledge and retrieval layer.

`packages/shared-contracts/embedding-job.schema.json` is the machine-readable projection of the same contract.
