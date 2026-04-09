#!/usr/bin/env bash
set -euo pipefail

BRANCH="${1:-}"

git fetch origin >/dev/null 2>&1

CURRENT_BRANCH="$(git branch --show-current)"
if [ -z "$BRANCH" ]; then
  BRANCH="$CURRENT_BRANCH"
fi

HEAD_HASH="$(git rev-parse HEAD)"
ORIGIN_HASH="$(git rev-parse "origin/$BRANCH")"
STATUS="$(git status --short || true)"

echo "Repo           : $(pwd)"
echo "Current branch : $CURRENT_BRANCH"
echo "Target branch  : $BRANCH"
echo "HEAD           : $HEAD_HASH"
echo "origin/$BRANCH : $ORIGIN_HASH"
echo

if [ -n "$STATUS" ]; then
  echo "Working tree is NOT clean:"
  echo "$STATUS"
else
  echo "Working tree is clean."
fi

echo
if [ "$HEAD_HASH" = "$ORIGIN_HASH" ]; then
  echo "HEAD is synchronized with origin/$BRANCH."
else
  echo "HEAD differs from origin/$BRANCH."
fi
