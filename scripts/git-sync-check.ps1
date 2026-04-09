param(
    [string]$Branch = ""
)

$ErrorActionPreference = "Stop"

$repo = Get-Location
Write-Host "Repo: $repo"

git fetch origin | Out-Null

$currentBranch = git branch --show-current
$currentBranch = $currentBranch.Trim()

if ([string]::IsNullOrWhiteSpace($Branch)) {
    $Branch = $currentBranch
}

$head = (git rev-parse HEAD).Trim()
$originHead = (git rev-parse "origin/$Branch").Trim()
$status = git status --short

Write-Host "Current branch : $currentBranch"
Write-Host "Target branch  : $Branch"
Write-Host "HEAD           : $head"
Write-Host "origin/$Branch : $originHead"

if ($status) {
    Write-Host ""
    Write-Host "Working tree is NOT clean:" -ForegroundColor Yellow
    $status
} else {
    Write-Host ""
    Write-Host "Working tree is clean." -ForegroundColor Green
}

if ($head -eq $originHead) {
    Write-Host "HEAD is synchronized with origin/$Branch." -ForegroundColor Green
} else {
    Write-Host "HEAD differs from origin/$Branch." -ForegroundColor Red
}
