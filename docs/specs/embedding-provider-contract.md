# Embedding Provider Contract

## Goal
Define a standalone embedding provider contract for the knowledge/retrieval layer without introducing a runtime embedding executor, vector database, retrieval engine, or provider SDK wrapper.

## Purpose
Embedding provider contract describes an available embeddings provider that can be referenced by future retrieval and indexing workflows.

This contract belongs to the knowledge/retrieval layer and must not be treated as part of generative model routing.

It provides a stable declaration of provider identity, provider availability, supported modalities, and dimension-related characteristics for embedding backends.

## Embedding Provider Object

```json
{
  "embedding_provider_id": "embedding-provider-0001",
  "provider_name": "gemini-embedding-2",
  "provider_type": "gemini_embedding",
  "provider_status": "available",
  "created_at": "2026-03-28T06:00:00Z",
  "supports_text": true,
  "supports_image": false,
  "supports_audio": false,
  "supports_video": false,
  "supports_pdf": true,
  "default_dimension": 3072,
  "max_dimension": 3072,
  "provider_note": "Declared as an embedding-layer provider for retrieval workflows"
}
```

## Required Fields
- `embedding_provider_id`
- `provider_name`
- `provider_type`
- `provider_status`
- `created_at`

## Optional Fields
- `supports_text`
- `supports_image`
- `supports_audio`
- `supports_video`
- `supports_pdf`
- `default_dimension`
- `max_dimension`
- `provider_note`

## Field Semantics
### embedding_provider_id
Unique identifier of the embedding provider contract.

### provider_name
Human-readable provider name used for capability declaration and future provider selection.

### provider_type
Contract-level provider classification.

Allowed values:
- `local_embedding`
- `cloud_embedding`
- `gemini_embedding`
- `other`

### provider_status
Contract-level provider availability state.

Allowed values:
- `draft`
- `available`
- `limited`
- `deprecated`

### created_at
Creation timestamp in ISO 8601 date-time format.

### supports_text
Boolean flag declaring whether the provider supports text embeddings.

### supports_image
Boolean flag declaring whether the provider supports image embeddings.

### supports_audio
Boolean flag declaring whether the provider supports audio embeddings.

### supports_video
Boolean flag declaring whether the provider supports video embeddings.

### supports_pdf
Boolean flag declaring whether the provider supports PDF-oriented embedding input.

### default_dimension
Default numeric embedding dimension exposed by the provider.

### max_dimension
Maximum numeric embedding dimension exposed by the provider.

### provider_note
Optional explanatory note for provider-specific engineering context.

## Layer Position
Embedding provider contract is part of the knowledge/retrieval layer.

It is intended to align with:
- `knowledge source` for source-aware embedding preparation
- `knowledge retrieval` for retrieval/index selection context
- `retrieval session` for future session-level embedding linkage
- `retrieval result` for future observability and result provenance

## Engineering Rule
Gemini Embedding 2 must be integrated as a concrete provider inside the embedding layer.

It must not be mixed into the generative model router.

## Rules
1. Boolean support fields describe supported modalities only.
2. `default_dimension` and `max_dimension` are numeric provider characteristics only.
3. `provider_note`, when present, is an optional explanation and not executable provider configuration.
4. The contract declares provider capability and availability; it does not execute embeddings.

## Boundaries
This is not a runtime embedding executor.

This is not a vector DB.

This is not a retrieval engine.

This is not a provider SDK wrapper.

## Expected Usage
- capability declaration for embedding backends
- selection basis for future embedding jobs
- future linkage with retrieval index and observability

## Source Alignment
`docs/specs/embedding-provider-contract.md` defines embedding provider semantics for the knowledge/retrieval layer.

`packages/shared-contracts/embedding-provider.schema.json` is the machine-readable projection of the same contract.
