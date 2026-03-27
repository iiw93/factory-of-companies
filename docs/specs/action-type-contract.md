# Action Type Contract

## Goal
Определить единый контракт допустимых типов исполняемой работы без реализации runtime orchestration.

## Purpose
Action type contract описывает допустимые типы исполняемой работы.

Он задаёт общий семантический словарь действий для `execution-request.action_type` и `agent-role.allowed_action_types`.

## Declared Action Type Model
### `analyze_request`
Тип действия для анализа входящего запроса, его контекста, ограничений и исходных условий.

### `plan_work`
Тип действия для декомпозиции задачи в план, шаги выполнения и согласованные work items.

### `design_architecture`
Тип действия для определения архитектурных границ, интерфейсных решений и технической структуры.

### `generate_repository`
Тип действия для первичной генерации репозитория, стартового каркаса проекта или базовых артефактов.

### `write_code`
Тип действия для реализации согласованных изменений в коде и связанных engineering artifacts.

### `run_checks`
Тип действия для запуска проверок, верификации, acceptance-level validation и review-oriented checks.

### `deploy_service`
Тип действия для operational and delivery work, связанной с выкладкой сервиса или изменением окружения.

### `update_documentation`
Тип действия для обновления документации, спецификаций и traceability-related текстовых артефактов.

## Contract Boundaries
Этот контракт не является runtime queue taxonomy.

Этот контракт не является scheduler.

Этот контракт не является permission system.

Этот контракт не является execution engine.

## Expected Usage
- валидация `execution-request.action_type`
- согласование `target_role` и `allowed_action_types`
- future linkage с orchestration rules

## Source Alignment
`docs/specs/action-type-contract.md` остаётся смысловым источником action type semantics.

`packages/shared-contracts/action-type.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs, execution request contract, agent role contract и acceptance checklist.
