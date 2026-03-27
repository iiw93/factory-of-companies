# Agent Role Contract

## Goal
Определить единый контракт допустимых логических ролей агентов без реализации agent runtime.

## Purpose
Agent role contract описывает допустимые логические роли в системе.

Он задаёт общий семантический словарь ролей для docs, orchestration-level handoff и future machine-readable validation.

Этот контракт связан с `execution-request.target_role`: поле `target_role` должно ссылаться на допустимую логическую роль из объявленной role model.

## Declared Role Model
### `ceo_agent`
Логическая роль верхнеуровневого целеполагания, приоритизации и принятия решений по направлению работы.

### `planner_agent`
Логическая роль декомпозиции целей в план, шаги исполнения и согласованные work items.

### `architect_agent`
Логическая роль определения архитектурных ограничений, интерфейсных границ и технической структуры решения.

### `repo_generator_agent`
Логическая роль первичной генерации репозитория, каркаса проекта или стартовых артефактов.

### `developer_agent`
Логическая роль реализации согласованных изменений в коде и связанных engineering artifacts.

### `qa_agent`
Логическая роль проверки корректности, сценариев верификации и acceptance-level соответствия.

### `devops_agent`
Логическая роль operational and delivery concerns, включая окружения, выкладку и сопутствующие delivery workflow.

### `documentation_agent`
Логическая роль поддержки документации, спецификаций и traceability-related текстовых артефактов.

## Contract Boundaries
Этот контракт не является runtime registry.

Этот контракт не является org chart implementation.

Этот контракт не является permission system.

Этот контракт не является scheduling layer.

## Expected Usage
- валидация `target_role`
- согласование docs и execution request
- future linkage с orchestration и company builder

## Source Alignment
`docs/specs/agent-role-contract.md` остаётся смысловым источником agent role semantics.

`packages/shared-contracts/agent-role.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs, execution request contract и acceptance checklist.
