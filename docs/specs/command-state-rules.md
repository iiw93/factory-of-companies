# Command State Rules

## Purpose
`packages/shared-contracts/command-state-rules.json` фиксирует машиночитаемый слой правил для состояний команды.

## Source of Meaning
`docs/specs/command-state-machine.md` остаётся смысловым источником жизненного цикла команды.

`packages/shared-contracts/command-state-rules.json` является простой машиночитаемой проекцией этого документа для локальной автоматической проверки согласованности.

## Structure
Rules-файл intentionally остаётся простым и читаемым. Верхний уровень содержит:

- `states`
- `allowed_transitions`
- `forbidden_transitions`
- `terminal_states`

Такой формат выбран для будущей автоматической проверки без превращения rules-файла в orchestration model.

## Boundaries
Этот rules-файл не является runtime enforcement layer.

Этот rules-файл не является orchestration engine.

Он не исполняет переходы и не добавляет бизнес-логику исполнения. Он только формализует текущую документацию в машиночитаемом виде.

## Alignment Rule
При изменении `docs/specs/command-state-machine.md` соответствующая машиночитаемая проекция в `packages/shared-contracts/command-state-rules.json` должна обновляться синхронно.
