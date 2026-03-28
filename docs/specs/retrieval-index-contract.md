# Retrieval Index Contract

## Goal
Define a standalone retrieval index contract without introducing a runtime vector DB, retrieval engine, storage orchestration runtime, or connector service.

## Purpose
Retrieval index contract describes an index that is available for retrieval.

It records one retrieval-facing index layer that links embedding providers, embedding jobs, and knowledge sources to the retrieval layer without becoming a runtime executor.

This contract is expected to align with:
- `embedding_provider_id`
- `embedding_job_id`
- `knowledge_source_id`
- `knowledge_retrieval_id`
- `retrieval_session_id`

## Retrieval Index Object

```json
{
  "retrieval_index_id": "retrieval-index-0001",
  "index_name": "company-context-main-index",
  "index_status": "ready",
  "created_at": "2026-03-28T08:00:00Z",
  "embedding_provider_id": "embedding-provider-0001",
  "linked_embedding_job_ids": [
    "embedding-job-0001",
    "embedding-job-0002"
  ],
  "knowledge_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "modality_scope": "text_only",
  "dimension": 3072,
  "index_backend": "vector_db",
  "record_count": 128,
  "index_note": "Primary retrieval-facing index contract for company knowledge"
}
```

## Required Fields
- `retrieval_index_id`
- `index_name`
- `index_status`
- `created_at`
- `embedding_provider_id`

## Optional Fields
- `linked_embedding_job_ids`
- `knowledge_source_ids`
- `modality_scope`
- `dimension`
- `index_backend`
- `record_count`
- `index_note`

## Field Semantics
### retrieval_index_id
Unique identifier of the retrieval index contract.

### index_name
Human-readable name of the retrieval index.

### index_status
Contract-level retrieval index lifecycle state.

Allowed values:
- `draft`
- `building`
- `ready`
- `degraded`
- `archived`

### created_at
Creation timestamp in ISO 8601 date-time format.

### embedding_provider_id
Reference to the embedding provider associated with the index.

### linked_embedding_job_ids
Array of references to embedding jobs linked to this index.

### knowledge_source_ids
Array of references to knowledge sources linked to this index.

### modality_scope
Optional contract-level modality scope for the index.

Allowed values:
- `text_only`
- `text_image`
- `text_audio`
- `text_video`
- `multimodal`

### dimension
Optional integer dimension of indexed embeddings with minimum value `1`.

### index_backend
Optional contract-level index backend classification.

Allowed values:
- `local_file_index`
- `vector_db`
- `hybrid_store`
- `other`

### record_count
Optional integer count of indexed records with minimum value `0`.

### index_note
Optional explanatory note for engineering or audit context.

## Engineering Rule
Retrieval index is the layer between embedding jobs and retrieval operations.

Index does not replace retrieval session or retrieval result contracts and is not a runtime executor.

## Rules
1. `linked_embedding_job_ids` is an array of references to embedding jobs.
2. `knowledge_source_ids` is an array of references to knowledge sources.
3. `dimension` is an integer with minimum value `1`.
4. `record_count` is an integer with minimum value `0`.
5. `index_note`, when present, is an optional explanation and not executable configuration.
6. The contract declares retrieval-facing index availability; it does not execute retrieval, embeddings, or storage orchestration.

## Boundaries
This is not a runtime vector search executor.

This is not an embedding engine.

This is not a storage orchestration runtime.

This is not a connector service.

## Expected Usage
- record available retrieval indexes
- link provider/jobs/sources with the retrieval layer
- support future observability, audit and debugging views

## Source Alignment
`docs/specs/retrieval-index-contract.md` defines retrieval index semantics for the knowledge/retrieval layer.

`packages/shared-contracts/retrieval-index.schema.json` is the machine-readable projection of the same contract.
