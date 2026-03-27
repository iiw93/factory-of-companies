# Planning Artifact Contract

## Goal
Определить отдельный контракт planning artifact без внедрения planning engine, task board, project manager runtime или repository manager.

## Purpose
Planning artifact contract описывает артефакт планирования внутри системы.

Он связывает planning artifact с artifact reference, `project_id`, `trace_id`, `source_role` и downstream `action_type`-driven flows, чтобы planning outputs можно было согласованно привязывать к project and trace context и передавать между planner / architect / developer flows.

## Planning Artifact Object

```json
{
  "planning_artifact_id": "plan-artifact-0001",
  "artifact_id": "artifact-0001",
  "project_id": "project-001",
  "trace_id": "trace-0001",
  "planning_type": "work_plan",
  "source_role": "planner_agent",
  "created_at": "2026-03-27T04:00:00Z",
  "planning_status": "active",
  "planning_horizon": "short_term",
  "artifact_uri": "docs/plans/project-001-work-plan.md",
  "planning_note": "Work plan prepared for developer handoff after request analysis"
}
```

## Required Fields
- `planning_artifact_id`
- `artifact_id`
- `project_id`
- `trace_id`
- `planning_type`
- `source_role`
- `created_at`
- `planning_status`
- `planning_horizon`
- `artifact_uri`

## Optional Fields
- `planning_note`

## Field Semantics
### planning_artifact_id
Уникальный идентификатор planning artifact record.

### artifact_id
`artifact_id` является ссылкой на artifact reference.

Значение `artifact_id` должно ссылаться на контракт из `docs/specs/artifact-reference-contract.md`.

### project_id
`project_id` является ссылкой на project context.

### trace_id
`trace_id` является ссылкой на traceability envelope.

### planning_type
`planning_type` фиксирует тип planning artifact.

Допустимые значения:
- `request_analysis`
- `work_plan`
- `architecture_plan`
- `execution_plan`
- `release_plan`

### source_role
`source_role` определяет логическую роль, создавшую planning artifact.

Значение `source_role` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### created_at
Момент создания planning artifact в формате ISO 8601 date-time.

### planning_status
`planning_status` фиксирует текущее состояние planning artifact.

Допустимые значения:
- `draft`
- `active`
- `superseded`
- `archived`

### planning_horizon
`planning_horizon` фиксирует временной горизонт planning artifact.

Допустимые значения:
- `immediate`
- `short_term`
- `mid_term`
- `long_term`

### artifact_uri
`artifact_uri` является строковой ссылкой или путём на сам planning artifact.

### planning_note
`planning_note` является опциональным пояснением planning artifact.

## Rules
1. Planning artifact contract должен описывать planning artifact внутри системы, а не planning engine.
2. `artifact_id` должен использоваться как ссылка на уже определённый artifact reference.
3. `artifact_uri` должен использоваться только как строковая ссылка или путь на сам артефакт.
4. `project_id` и `trace_id` должны обеспечивать контекстное связывание planning outputs с project and trace.
5. `source_role` должен описывать только логическую роль источника, а не runtime implementation detail.
6. `planning_type` должен помогать согласованно связывать planning outputs с downstream `action_type`-driven handoff и execution flows без добавления planning runtime.
7. `planning_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является planning engine.

Этот контракт не является task board.

Этот контракт не является project manager runtime.

Этот контракт не является repository manager.

## Expected Usage
- связывание planning outputs с project and trace
- handoff between planner / architect / developer flows
- future linkage with dashboard and audit views

## Source Alignment
`docs/specs/planning-artifact-contract.md` остаётся смысловым источником planning artifact semantics.

`packages/shared-contracts/planning-artifact.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
