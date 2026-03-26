# Bridge Command Contract

## Goal
Определить единый формат команд, поступающих из Telegram и Dashboard в систему компании агентов.

## Purpose
Любой пользовательский запрос должен быть нормализован в единый объект команды.

## Command Object

```json
{
  "command_id": "cmd-0001",
  "channel": "telegram",
  "user_id": "owner-001",
  "company_id": "factory-main",
  "project_id": "project-001",
  "session_id": "session-001",
  "intent": "create_project",
  "message": "Создай AI SaaS для анализа логов",
  "attachments": [],
  "priority": "normal",
  "approval_required": true,
  "created_at": "2026-03-26T00:00:00Z",
  "metadata": {
    "source_language": "ru",
    "input_mode": "text"
  }
}
