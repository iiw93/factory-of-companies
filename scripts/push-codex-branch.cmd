@echo off
setlocal

cd /d C:\PAPERCLIP\factory-of-companies

echo.
echo === Pushing codex/docs/thin-runtime-mvp-plan ===
echo If your SSH key requires a passphrase, enter it in this terminal when prompted.
echo.

git push origin codex/docs/thin-runtime-mvp-plan
set EXITCODE=%ERRORLEVEL%

echo.
if %EXITCODE% EQU 0 (
    echo Push completed successfully.
) else (
    echo Push failed with exit code %EXITCODE%.
)

echo.
echo Recent commits:
git log --oneline --decorate -3

echo.
echo HEAD:
git rev-parse HEAD

echo.
echo origin/codex/docs/thin-runtime-mvp-plan:
git rev-parse origin/codex/docs/thin-runtime-mvp-plan

echo.
echo Working tree:
git status --short

echo.
echo Press any key to close this window...
pause >nul
exit /b %EXITCODE%
