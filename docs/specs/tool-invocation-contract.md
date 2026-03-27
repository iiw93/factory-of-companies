# Tool Invocation Contract

## Goal
Определить отдельный контракт единичного вызова инструмента без внедрения runtime tool runner.

## Purpose
Tool invocation contract описывает единичный вызов инструмента, утилиты или скрипта в рамках execution flow.

Он связывает факт вызова с `trace_id`, `execution_request_id`, `execution_result_id`, `handoff_id`, `role_type`, `action_type` и runtime capability, чтобы linkage между execution flow и фактическим использованием инструмента оставался явным и формализованным.

## Tool Invocation Object

```json
{
  "tool_invocation_id": "tool-0001",
  "tool_name": "verify_shared_contracts.py",
  "tool_type": "script",
  "invocation_status": "succeeded",
  "created_at": "2026-03-27T15:10:00Z",
  "trace_id": "trace-0001",
  "execution_request_id": "exec-0001",
  "execution_result_id": "result-0001",
  "handoff_id": "handoff-0001",
  "role_type": "developer_agent",
  "action_type": "run_checks",
  "input_reference": "artifact://contracts/check-input",
  "output_reference": "artifact://reports/shared-contracts-verification",
  "tool_note": "Schema verification script executed for shared contracts"
}
```

## Required Fields
- `tool_invocation_id`
- `tool_name`
- `tool_type`
- `invocation_status`
- `created_at`

## Optional Fields
- `trace_id`
- `execution_request_id`
- `execution_result_id`
- `handoff_id`
- `role_type`
- `action_type`
- `input_reference`
- `output_reference`
- `tool_note`

## Field Semantics
### tool_invocation_id
Уникальный идентификатор отдельного tool invocation.

### tool_name
Человекочитаемое имя инструмента, утилиты, API operation или скрипта.

### tool_type
`tool_type` определяет тип вызванного инструмента.

Допустимые значения:
- `script`
- `cli`
- `api`
- `agent_tool`
- `system_tool`
- `other`

### invocation_status
`invocation_status` фиксирует текущее состояние или итог единичного вызова.

Допустимые значения:
- `prepared`
- `running`
- `succeeded`
- `failed`
- `cancelled`

### created_at
Момент фиксации tool invocation в формате ISO 8601 date-time.

### trace_id
`trace_id` является опциональной ссылкой на traceability envelope, если вызов уже связан с trace context.

### execution_request_id
`execution_request_id` является опциональной ссылкой на execution request, если вызов выполняется в рамках нормализованного запроса на исполнение.

### execution_result_id
`execution_result_id` является опциональной ссылкой на execution result, если вызов фиксируется как часть результата исполнения.

### handoff_id
`handoff_id` является опциональной ссылкой на orchestration handoff, если вызов связан с конкретной передачей работы.

### role_type
`role_type` является опциональной ссылкой на логическую роль исполнителя, от имени которой был инициирован вызов.

Значение `role_type` должно оставаться согласованным с `docs/specs/agent-role-contract.md`.

### action_type
`action_type` является опциональной ссылкой на нормализованный тип работы, в рамках которого был выполнен вызов.

Значение `action_type` должно оставаться согласованным с `docs/specs/action-type-contract.md`.

### input_reference
`input_reference` является опциональной строковой ссылкой на входной артефакт, payload snapshot или иной источник входных данных.

### output_reference
`output_reference` является опциональной строковой ссылкой на результат, артефакт или output snapshot, произведённый вызовом.

### tool_note
`tool_note` является опциональным пояснением.

## Rules
1. Tool invocation contract должен описывать только единичный вызов инструмента, утилиты, API operation или скрипта.
2. `trace_id`, `execution_request_id`, `execution_result_id`, `handoff_id`, `role_type` и `action_type`, если переданы, используются только как опциональные ссылки на уже существующие контракты.
3. `tool_type` должен фиксировать форму вызванного инструмента, а не orchestration intent.
4. `invocation_status` должен отражать lifecycle отдельного вызова, а не aggregate execution flow state.
5. `input_reference` и `output_reference`, если переданы, должны оставаться строковыми ссылками без встраивания runtime payload semantics.
6. `tool_note`, если передан, должен оставаться кратким пояснением.
7. Runtime capability linkage допустим на смысловом уровне для проверки tool availability и feasibility, но этот контракт не описывает capability engine.

## Boundaries
Этот контракт не является runtime executor.

Этот контракт не является process manager.

Этот контракт не является tool sandbox.

Этот контракт не является job queue.

## Expected Usage
- фиксация факта вызова инструмента
- linkage between execution flow and actual tool use
- future observability, debugging and audit views

## Source Alignment
`docs/specs/tool-invocation-contract.md` остаётся смысловым источником tool invocation semantics.

`packages/shared-contracts/tool-invocation.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
