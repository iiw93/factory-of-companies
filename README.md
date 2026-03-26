# Factory of Companies

## Mission
Построить управляемую систему генерации и развития AI-проектов.

## Principles
1. Системность превосходит импровизацию.
2. Главная ценность любого инструмента — снижение энтропии и сложности.
3. Доказательства вместо заявлений.
4. Сначала тесты, потом основной код.
5. Документация поддерживается вместе с кодом.

## Architecture
- Paperclip = runtime engine
- Company Builder Layer = логика создания и развития проектов
- Bridge Layer = Telegram + Dashboard
- Model Router = llama.cpp local-first, RunPod as burst
- Codex = внешний инженерный инструмент
- ChatGPT = стратегический и архитектурный контур

## Main Modules
- apps/bridge-gateway
- apps/dashboard-web
- apps/telegram-bot
- apps/orchestrator-api
- packages/company-builder
- packages/paperclip-adapter
- packages/model-router
- packages/codex-adapter
- packages/deploy-agent
- packages/memory-rag
- packages/shared-contracts
- vendor/paperclip

## Development Rules
- Любая новая функция начинается с требования.
- Затем user story и acceptance criteria.
- Затем тесты.
- Затем реализация.
- Затем обновление документации.

