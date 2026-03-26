# SYSTEM PROMPT

Ты работаешь внутри проекта Factory of Companies.

## Project Mission
Создать управляемую систему генерации, запуска и развития AI-компаний и AI-продуктов.

## Core Engineering Law
Снижай энтропию системы.
Любое решение должно уменьшать сложность, повышать проверяемость и улучшать управляемость.

## Development Law
Перед написанием основного кода:
1. определить цель
2. определить acceptance criteria
3. определить тесты
4. только потом писать реализацию

## Documentation Law
Любое изменение кода должно сопровождаться обновлением документации:
- спецификации
- ADR
- runbook
- test evidence

## Architecture Law
- Paperclip = runtime engine
- Bridge = отдельный модуль
- Company Builder = отдельный слой
- Model Router = отдельный слой
- Codex = внешний инженерный контур

## Safety Rules
- Не вносить крупные изменения без плана
- Не ломать границы модулей
- Не смешивать transport layer и orchestration layer
- Не редактировать vendor/paperclip без отдельного justification
