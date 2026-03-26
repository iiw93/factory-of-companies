# SRS — Software Requirements Specification

## 1. System Name
Factory of Companies

## 2. Goal
Система должна принимать идею пользователя, превращать её в план, репозиторий, код, тесты, деплой и дальнейшее развитие через управляемую компанию агентов.

## 3. Actors
- Owner / CEO (пользователь)
- Telegram Bridge
- Dashboard Bridge
- ChatGPT
- Codex
- Paperclip Runtime
- Company Builder Agents
- Deploy Agent
- Local LLM
- Cloud LLM

## 4. Main Functional Requirements
1. Пользователь может отправить задачу через Telegram.
2. Пользователь может отправить задачу через Dashboard.
3. Система нормализует запрос в единый command contract.
4. CEO Agent формирует project charter.
5. Planner Agent создаёт план.
6. Architect Agent формирует архитектуру.
7. Developer Agent готовит тесты и код.
8. QA Agent проверяет соответствие критериям.
9. DevOps Agent выполняет deploy.
10. Система ведёт аудит, статус и историю решений.

## 5. Non-Functional Requirements
- Local-first execution
- Controlled cloud escalation
- Test-first development
- Documentation as code
- Upstream update policy
- Traceability
- Auditability
- Rollback capability

## 6. Model Policy
- local llama.cpp by default
- RunPod only when justified
- cloud usage must be logged and explainable

## 7. Acceptance Criteria for MVP
- Можно создать проект из одного текстового запроса
- Есть Telegram или Dashboard вход
- Есть план, репозиторий, тесты, deploy
- Есть журнал решений и статусов
