# Upstream Update Policy

## Goal
Обновлять Paperclip управляемо, без автоматического принятия изменений в main.

## Repositories
- origin = наш основной репозиторий Factory of Companies
- upstream-paperclip = официальный Paperclip

## Core Rule
Никогда не вливать изменения из upstream-paperclip напрямую в main.

## Update Process
1. Выполнить fetch из upstream-paperclip
2. Создать отдельную review-ветку
3. Изучить diff
4. Проверить совместимость adapters и bridge layer
5. Выполнить integration tests
6. Выполнить system tests
7. Только после этого принимать решение о merge

## Allowed
- fetch upstream
- review branches
- compatibility testing
- staging verification

## Forbidden
- auto-merge from upstream
- direct merge to main
- update without tests
- update without documentation

## Required Evidence
Для каждого обновления должны быть:
- ссылка на upstream commit или release
- описание влияния на наш проект
- результаты тестов
- решение: accept / postpone / reject
