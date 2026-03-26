# Command State Machine

## Goal
Определить жизненный цикл команды от момента получения до завершения или отказа.

## Purpose
Команда в системе должна иметь предсказуемые состояния и допустимые переходы.

## States
- received
- validated
- rejected
- accepted
- requires_approval
- approved
- routed
- planned
- executing
- completed
- failed
- cancelled

## State Meanings

### received
Команда принята каналом связи, но ещё не прошла валидацию.

### validated
Команда успешно прошла проверку формата и обязательных полей.

### rejected
Команда отклонена из-за ошибки формата, отсутствия данных или недопустимых значений.

### accepted
Команда признана корректной и может быть передана дальше.

### requires_approval
Команда требует подтверждения перед дальнейшим исполнением.

### approved
Команда подтверждена пользователем или policy layer.

### routed
Команда направлена в orchestration layer или соответствующему агенту.

### planned
По команде сформирован план выполнения.

### executing
По команде выполняются действия в системе.

### completed
Команда успешно завершена.

### failed
Команда завершилась ошибкой.

### cancelled
Команда остановлена пользователем или policy layer.

## Allowed Transitions
- received -> validated
- received -> rejected
- validated -> accepted
- validated -> rejected
- accepted -> requires_approval
- accepted -> routed
- requires_approval -> approved
- requires_approval -> cancelled
- approved -> routed
- routed -> planned
- planned -> executing
- executing -> completed
- executing -> failed
- accepted -> cancelled
- routed -> failed
- planned -> failed

## Rules
1. Команда не может перейти в executing без routed.
2. Команда не может перейти в completed напрямую из accepted.
3. rejected является конечным состоянием.
4. completed является конечным состоянием.
5. failed является конечным состоянием.
6. cancelled является конечным состоянием.
7. Все переходы должны логироваться.

## Validation Examples

### Valid Example
received -> validated -> accepted -> routed -> planned -> executing -> completed

### Approval Example
received -> validated -> accepted -> requires_approval -> approved -> routed -> planned -> executing -> completed

### Invalid Example
received -> executing -> completed

## Notes
Bridge Layer работает только с ранними состояниями:
- received
- validated
- rejected
- accepted
- requires_approval
- routed
