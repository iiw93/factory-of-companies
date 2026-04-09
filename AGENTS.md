# AGENTS.md

## Project operating mode

This repository is governed by a strict narrow-scope workflow.

Primary goals:
- preserve parked-state governance unless the user explicitly reopens a blocked track
- avoid silent scope expansion
- prefer small, reviewable, low-risk changes
- keep documentation, contracts, and acceptance materials aligned

## Repository authority and sync rules

- Primary authoring copy: Windows
- Secondary verification copy: Ubuntu
- Remote synchronization authority: GitHub
- Never edit the same branch concurrently on Windows and Ubuntu
- Before editing, always check:
  - current branch
  - working tree cleanliness
  - HEAD vs origin/<branch>
- After a completed step on Windows:
  - review
  - commit
  - push
- After push, Ubuntu only:
  - fetches
  - checks out the same branch
  - pulls with --ff-only
- Do not continue work on a second machine if the first machine has uncommitted changes

## Git safety rules

Always prefer:
- git fetch origin
- git status --short
- git branch --show-current
- git rev-parse HEAD
- git rev-parse origin/<branch>
- fast-forward only pull behavior

Do not use without explicit user approval:
- git push --force
- git rebase -i
- git reset --hard
- git commit --amend
- destructive delete operations
- cross-machine recovery rewrites

## Stash Instead Of Risk Rule

If the working tree is not clean and the current material is not ready for a narrow commit, prefer stash before continuing.

Apply this rule when:
- untracked planning/runtime files accumulate
- a completed narrow scope is followed by unrelated leftover material
- switching between Windows and Ubuntu
- pausing work for later continuation

Preferred commands:
- `git status --short`
- `git stash push -u -m "WIP <description>"`
- `git stash list`
- `git stash show --stat stash@{0}`

When restoring, prefer:
- `git stash apply stash@{0}`
- verify with `git status --short`
- then `git stash drop stash@{0}`

Do not treat stash as a cross-machine sync mechanism.

## Scope control rules

Default mode is narrow-scope and non-authorizing.

When reviewing or editing:
- prefer docs-only changes first
- preserve existing governance wording
- do not silently reopen blocked tracks
- do not broaden implementation scope unless explicitly instructed
- separate guardrail alignment from implementation work
- treat packages/** and tests/runtime/** as restricted zones unless the user explicitly opens that scope

## Safe zones

Preferred edit zones:
- docs/adr/
- docs/roadmap/
- docs/specs/
- docs/test-strategy/
- docs/use-cases/
- tests/acceptance/

Restricted zones unless explicitly authorized:
- packages/
- tests/runtime/
- deployment/infrastructure scripts
- anything outside the repository root

## Working style

- Use PowerShell-safe command forms on Windows
- Keep changes minimal and localized
- Summarize planned scope before large edits
- After edits, show verification commands and results
- Stop before commit unless the user asked for commit
- Stop before push unless the user asked for push

## Validation discipline

Before claiming sync or completion, verify with commands.
Before staging, confirm that only intended files are included.
Before commit, review staged diff.
Before push, confirm branch and target.

## Output expectations

When asked to perform a task:
1. State the current stage briefly
2. State the exact narrow scope you will touch
3. Perform only the approved changes
4. Show verification output
5. Stop at the requested boundary
