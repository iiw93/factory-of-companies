# Priority Contract

## Goal
Определить единый контракт advisory priority signal для execution request без внедрения scheduler или queue engine.

## Purpose
Priority contract описывает нормализованный объект priority.

Он связывает priority semantics с `execution-request.priority`, а также с future orchestration и scheduling layers.

Priority описывает relative importance and urgency of work, а не гарантию исполнения.

## Priority Object

```json
{
  "priority_id": "priority-0001",
  "priority_name": "Default planning priority",
  "priority_level": "normal",
  "description": "Standard orchestration priority for regular execution requests.",
  "recommended_use_cases": [
    "Routine planning work",
    "Non-urgent implementation tasks"
  ]
}
```

## Required Fields
- `priority_id`
- `priority_name`
- `priority_level`
- `description`

## Optional Fields
- `recommended_use_cases`

## Field Semantics
### priority_id
Уникальный идентификатор отдельного priority contract record.

### priority_name
Человекочитаемое имя приоритета.

### priority_level
`priority_level` определяет нормализованный уровень относительной важности и срочности.

Допустимые значения:
- `low`
- `normal`
- `high`
- `critical`

Краткий смысл уровней:
- `low` — работа с низкой срочностью и пониженной относительной важностью.
- `normal` — стандартный уровень для обычной плановой работы.
- `high` — повышенная важность или срочность, требующая более раннего внимания.
- `critical` — максимально высокий относительный приоритет для наиболее срочной и важной работы.

### description
`description` кратко фиксирует смысл выбранного priority record.

### recommended_use_cases
`recommended_use_cases`, если передан, описывает типовые сценарии применения уровня приоритета.

## Rules
1. Priority contract должен описывать только относительную важность и срочность работы.
2. Значение `priority_level` должно оставаться согласованным с `execution-request.priority`.
3. Priority contract должен использоваться как advisory signal для orchestration и planning layers.
4. `recommended_use_cases`, если передан, должен оставаться списком кратких текстовых сценариев.
5. Контракт должен сохранять совместимость с future orchestration / scheduling layers без внедрения runtime scheduling behavior.
6. Future linkage с approvals, budget и execution допускается только как семантическая связка контракта.

## Boundaries
Этот контракт не является scheduler.

Этот контракт не является queue engine.

Этот контракт не является SLA engine.

Этот контракт не является runtime enforcement policy.

## Expected Usage
- advisory routing
- planning and orchestration hints
- future linkage с approvals, budget и execution

## Source Alignment
`docs/specs/priority-contract.md` остаётся смысловым источником priority semantics.

`packages/shared-contracts/priority.schema.json` является формальной машиночитаемой проекцией этого контракта и должен оставаться согласованным с docs и acceptance checklist.
