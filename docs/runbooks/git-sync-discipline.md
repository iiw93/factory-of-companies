# Git Sync Discipline

## Purpose

Prevent Windows, Ubuntu, and GitHub from silently drifting apart.

## Authority model

- Primary authoring copy: Windows
- Secondary verification copy: Ubuntu
- Remote authority for synchronization: GitHub

## Core rules

1. Do not edit the same branch concurrently on Windows and Ubuntu.
2. Start work only after:
   - `git fetch origin`
   - branch check
   - clean working tree check
   - `HEAD` comparison with `origin/<branch>`
3. Finish each completed step by:
   - review
   - commit
   - push from Windows
4. After push, Ubuntu only does:
   - `git fetch origin`
   - `git checkout <branch>`
   - `git pull --ff-only origin <branch>`
5. Do not use:
   - `git push --force`
   - `git rebase -i`
   - `git reset --hard`
   - `git commit --amend`
   unless explicitly decided for a recovery procedure.
6. If working tree is not clean, do not switch machine and continue work there.
7. If `HEAD` and `origin/<branch>` differ, understand why before editing.

## Stash Instead Of Risk

Use stash when the working tree is dirty but the current material is not yet ready for a narrow commit.

Typical cases:
- leftover planning/runtime files remain after a completed narrow commit
- you want to pause work without losing local material
- you need a clean working tree before starting a new scoped task
- you are about to switch machines

Recommended workflow:
1. Check state with `git status --short`
2. Save unfinished local material with `git stash push -u -m "WIP <description>"`
3. Confirm a clean tree with `git status --short`
4. Inspect saved content with `git stash list` and `git stash show --stat stash@{0}`

Safe restore workflow:
1. `git stash apply stash@{0}`
2. verify with `git status --short`
3. only then `git stash drop stash@{0}`

Important:
- stash is local only
- stash is not a synchronization mechanism between Windows and Ubuntu
- if work must move across machines, use a proper commit or patch-based transfer instead

## Start-of-work checklist

### Windows
- Open repo
- `git fetch origin`
- confirm branch
- confirm clean working tree
- compare `HEAD` and `origin/<branch>`

### Ubuntu
- `git fetch origin`
- confirm branch
- confirm clean working tree
- compare `HEAD` and `origin/<branch>`

## End-of-step checklist

### Windows
- `git status --short`
- review diff
- commit
- push
- verify `HEAD == origin/<branch>`

### Ubuntu
- `git fetch origin`
- `git checkout <branch>`
- `git pull --ff-only origin <branch>`
- verify `HEAD == origin/<branch>`

## Recovery rule

If Windows, Ubuntu, and GitHub disagree:
1. Stop editing.
2. Identify the intended source of truth.
3. Compare hashes on all three sides.
4. Resume only after explicit re-alignment.
