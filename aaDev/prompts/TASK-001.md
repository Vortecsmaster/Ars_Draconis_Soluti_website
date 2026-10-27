# TASK-001 — Repository baseline and tooling manifest
**Sprint:** SPRINT-001 | **Depends on:** none
**SRS References:** SRS-OPS-001
**Single responsibility:** Inspect the current repository and establish a reproducible baseline without changing application functionality.

## Allowed changes
AA Dev/reports/ and optionally AA Dev/BASELINE.md

## Prohibited / boundaries
Existing source, lockfiles and scripts only; do not reorganize.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Record repository tree, available commands/versions, baseline test/build status, missing specifications, package manager, Git HEAD. Add AA Dev/BASELINE.md documenting observable facts only.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-001.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-001.audit.json`.

## Acceptance
Baseline document identifies actual repo state and can be used for all subsequent task execution.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
