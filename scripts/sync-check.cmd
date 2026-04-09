@echo off
setlocal

cd /d C:\PAPERCLIP\factory-of-companies

set BRANCH=codex/docs/thin-runtime-mvp-plan

echo.
echo === Sync check for %BRANCH% ===
echo.

git fetch origin

echo.
echo Current branch:
git branch --show-current

echo.
echo Working tree:
git status --short

echo.
echo HEAD:
git rev-parse HEAD

echo.
echo origin/%BRANCH%:
git rev-parse origin/%BRANCH%

echo.
echo Recent commits:
git log --oneline --decorate -3

echo.
echo Sync check complete.
echo Press any key to close this window...
pause >nul
exit /b 0
