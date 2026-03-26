# Bridge Response Contract

## Goal
Определить единый формат ответов системы обратно в Telegram и Dashboard.

## Purpose
Любой результат обработки команды должен быть представлен в одном нормализованном формате, независимо от канала.

## Response Object

```json
{
  "response_id": "resp-0001",
  "command_id": "cmd-0001",
  "channel": "telegram",
  "user_id": "owner-001",
  "status": "accepted",
  "message": "Команда принята в обработку",
  "result_type": "acknowledgement",
  "created_at": "2026-03-26T00:10:00Z",
  "payload": {
    "next_state": "routed",
    "requires_approval": false
  },
  "errors": [],
  "metadata": {
    "project_id": "project-001",
    "company_id": "factory-main"
  }
}
