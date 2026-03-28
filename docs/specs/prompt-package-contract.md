# Prompt Package Contract

## Goal
Определить отдельный контракт prompt package без внедрения runtime prompt builder, model gateway, chat transcript store или inference engine.

## Purpose
Prompt package contract описывает собранный пакет инструкций и контекста для конкретного выполнения.

Он связывает package-level reference с `trace_id`, `execution_request_id`, `context_selection_id`, `knowledge_source_id`, `tool_invocation_id`, `role_type` и `action_type`, чтобы собранный prompt/context package можно было согласованно привязывать к context selection и фактическому execution flow.

## Prompt Package Object

```json
{
  "prompt_package_id": "prompt-package-0001",
  "package_name": "planner-context-package",
  "package_status": "prepared",
  "created_at": "2026-03-28T01:30:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "context_selection_id": "context-selection-0001",
  "role_type": "planner_agent",
  "action_type": "plan_work",
  "instruction_text": "Use the selected context and produce a scoped work plan.",
  "selected_source_ids": [
    "knowledge-source-0001",
    "knowledge-source-0002"
  ],
  "linked_tool_invocation_id": "tool-0001",
  "package_note": "Prepared prompt/context package for planning execution"
}
```

## Required Fields
- `prompt_package_id`
- `package_name`
- `package_status`
- `created_at`
- `instruction_text`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `context_selection_id`
- `role_type`
- `action_type`
- `selected_source_ids`
- `linked_tool_invocation_id`
- `package_note`

## Field Semantics
### prompt_package_id
Уникальный идентификатор prompt package.

### package_name
Человекочитаемое имя собранного prompt/context package.

### package_status
`package_status` фиксирует текущее состояние prompt package.

Допустимые значения:
- `draft`
- `prepared`
- `applied`
- `superseded`
- `archived`

### created_at
Момент фиксации prompt package в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request.

### context_selection_id
`context_selection_id` является опциональной ссылкой на context selection contract.

### role_type
`role_type` является опциональной ссылкой на логическую роль исполнителя, для которой был собран пакет.

Значение `role_type` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### action_type
`action_type` является опциональной ссылкой на нормализованный тип работы, для которого был собран пакет.

Значение `action_type` должно оставаться согласованным с `docs/specs/action-type-contract.md`.

### instruction_text
`instruction_text` является обязательным текстом инструкций.

### selected_source_ids
`selected_source_ids` является опциональным массивом ссылок на knowledge sources.

### linked_tool_invocation_id
`linked_tool_invocation_id` является опциональной ссылкой на tool invocation.

### package_note
`package_note` является опциональным пояснением.

## Rules
1. Prompt package contract должен описывать только собранный пакет инструкций и контекста для конкретного выполнения, а не runtime prompt builder implementation.
2. `trace_id`, `execution_request_id`, `context_selection_id`, `role_type`, `action_type` и `linked_tool_invocation_id`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `instruction_text` должен содержать собственно текст инструкций, а не runtime model response.
4. `selected_source_ids`, если передан, должен содержать только ссылки на knowledge source contract.
5. `package_note`, если передан, должен оставаться кратким пояснением.

## Boundaries
Этот контракт не является runtime prompt builder.

Этот контракт не является model gateway.

Этот контракт не является chat transcript store.

Этот контракт не является inference engine.

## Expected Usage
- фиксация собранного prompt/context package
- linkage between context selection and actual execution
- future dashboard, audit and debugging views

## Source Alignment
`docs/specs/prompt-package-contract.md` остаётся смысловым источником prompt package semantics.

`packages/shared-contracts/prompt-package.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
