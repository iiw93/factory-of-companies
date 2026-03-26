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
```

## Required Fields
- `response_id`
- `command_id`
- `channel`
- `user_id`
- `status`
- `message`
- `created_at`

## Optional Fields
- `result_type`
- `payload`
- `errors`
- `metadata`

## Allowed Channel Values
- `telegram`
- `dashboard`

## Allowed Status Values
- `accepted`
- `rejected`
- `requires_approval`
- `routed`
- `planned`
- `executing`
- `completed`
- `failed`
- `cancelled`

## Allowed Result Types
- `acknowledgement`
- `validation_error`
- `approval_request`
- `progress_update`
- `final_result`
- `system_error`

## Rules
1. Каждый response должен ссылаться на исходный `command_id`.
2. `channel` должен отражать Bridge Layer, в который отправляется ответ.
3. `status` описывает текущее состояние обработки команды.
4. `result_type` уточняет смысл ответа, если это требуется для канала.
5. `payload` содержит только структурированные данные ответа.
6. `errors` используется только для структурированных ошибок и может быть пустым массивом.
7. `metadata` может содержать служебный контекст маршрутизации и корреляции.

## Validation Rules
- `response_id` должен быть непустой строкой.
- `command_id` должен быть непустой строкой.
- `channel` должен быть одним из допустимых значений.
- `user_id` должен быть непустой строкой.
- `status` должен быть одним из допустимых значений.
- `result_type`, если передан, должен быть одним из допустимых значений.
- `message` должен быть непустой строкой.
- `created_at` должен быть строкой в формате ISO 8601 date-time.
- `payload`, если передан, должен быть объектом.
- `metadata`, если передан, должен быть объектом.
- `errors`, если передан, должен быть массивом структурированных error object.

## Error Object Example

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Поле message не должно быть пустым",
  "field": "message",
  "details": {
    "reason": "minLength"
  }
}
```

## Output Examples

### Acknowledgement Example

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
    "next_state": "routed"
  },
  "errors": [],
  "metadata": {
    "project_id": "project-001"
  }
}
```

### Approval Request Example

```json
{
  "response_id": "resp-0002",
  "command_id": "cmd-0002",
  "channel": "dashboard",
  "user_id": "owner-001",
  "status": "requires_approval",
  "message": "Требуется подтверждение действия",
  "result_type": "approval_request",
  "created_at": "2026-03-26T00:11:00Z",
  "payload": {
    "approval_required": true
  },
  "errors": [],
  "metadata": {
    "project_id": "project-002"
  }
}
```

### Final Result Example

```json
{
  "response_id": "resp-0003",
  "command_id": "cmd-0003",
  "channel": "telegram",
  "user_id": "owner-001",
  "status": "completed",
  "message": "План проекта сформирован",
  "result_type": "final_result",
  "created_at": "2026-03-26T00:12:00Z",
  "payload": {
    "project_id": "project-003",
    "summary": "Сформирован план запуска"
  },
  "errors": [],
  "metadata": {
    "company_id": "factory-main"
  }
}
```

### Validation Error Example

```json
{
  "response_id": "resp-0004",
  "command_id": "cmd-0004",
  "channel": "dashboard",
  "user_id": "owner-001",
  "status": "failed",
  "message": "Команда отклонена из-за ошибки валидации",
  "result_type": "validation_error",
  "created_at": "2026-03-26T00:13:00Z",
  "payload": {},
  "errors": [
    {
      "code": "VALIDATION_ERROR",
      "message": "Поле intent содержит недопустимое значение",
      "field": "intent",
      "details": {
        "allowed_values": [
          "create_project",
          "update_project",
          "request_status",
          "approve_action",
          "reject_action",
          "ask_question"
        ]
      }
    }
  ],
  "metadata": {
    "company_id": "factory-main"
  }
}
```

## Notes
- Bridge Response Contract описывает только нормализованный формат ответа Bridge Layer.
- Контракт не содержит business logic решений и не определяет внутреннюю orchestration semantics.
- `payload` и `metadata` допускают служебные данные, но не заменяют обязательные поля ответа.
