# Thin Indexing MVP Plan

## 1. Goal
Deliver the first thin indexing MVP that can:

- take one or more knowledge sources
- pass them through one embedding provider
- create an embedding job
- create a retrieval index
- execute a knowledge retrieval
- record a retrieval session
- produce a retrieval result

This MVP is intended to prove one narrow vertical indexing flow end to end without introducing production runtime infrastructure.

## 2. Scope
This MVP is explicitly bounded to:

- text-first flow only
- one provider path only
- one index backend path only
- one retrieval path only
- no production dashboard
- no multi-agent autonomy
- no distributed infra

## 3. Recommended First Provider
Recommended first provider strategy:

- start with a local simple baseline provider as the safest initial path
- keep Gemini Embedding 2 as the next cloud-capable provider path inside the embedding layer

Reasoning:

- first establish a reproducible thin vertical scenario
- then extend provider coverage after the narrow path is stable and observable

## 4. Minimal Runtime Components
The minimal future runtime pieces for this MVP are:

- source loader
- chunker
- embedding adapter
- embedding job recorder
- retrieval index writer
- retrieval query stub
- retrieval result recorder

## 5. Proposed Execution Flow
Proposed MVP pipeline:

1. input knowledge source selected
2. normalized text chunks prepared
3. embedding provider selected
4. embedding job recorded
5. retrieval index recorded
6. test retrieval query executed
7. retrieval session recorded
8. retrieval result recorded
9. quality sanity check captured

## 6. Required Future Runtime Contracts or Reuse
Direct reuse from existing contracts:

- knowledge source contract for source identity and source linkage
- embedding provider contract for provider identity and capability declaration
- embedding job contract for embedding run recording
- retrieval index contract for retrieval-facing index recording
- knowledge retrieval contract for retrieval request/result declaration
- retrieval session contract for retrieval run/session capture
- retrieval result contract for final retrieval outcome capture

Potential later extension, but not required for this MVP:

- optional stronger chunk-level traceability
- optional richer quality sanity evidence linkage
- optional more explicit runtime observability fields if the narrow path proves stable

## 7. Risks
Primary MVP risks:

- chunking drift
- provider lock-in
- mismatched dimensions
- stale index state
- retrieval result without clear provenance
- multimodal expansion too early

## 8. Engineering Policy For This MVP
Engineering policy:

- text-first
- deterministic sample dataset
- explicit traceability
- no hidden background logic
- no scale before observability
- no multimodal rollout before text path is stable

## 9. Next Step After MVP
Next step after the MVP:

- observability for indexing
- embedding job runtime stub
- retrieval index runtime stub
- debug visual trace later

## 10. Status
- current stage: contracts for embedding and retrieval chain are already formalized
- done: source, provider, job, index, retrieval, session, and result contracts exist
- next: implement the first thin text-only indexing path against a deterministic sample dataset
- blocked by: selection of the exact baseline local provider path and first sample dataset
- acceptance target: one reproducible text-first indexing run with explicit recorded artifacts across the full contract chain
