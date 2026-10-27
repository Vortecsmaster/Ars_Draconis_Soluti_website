# TASK-009 — Reflection clear/confirm and privacy checks
**Sprint:** SPRINT-001 | **Depends on:** 008
**SRS References:** SRS-FR-018, SRS-FR-019, SRS-FR-020, SRS-FR-021, SRS-FR-022, SRS-DAT-003
**Single responsibility:** Add clear/restart confirmation and verify ephemeral privacy lifecycle.

## Allowed changes
Reflection component and its tests

## Prohibited / boundaries
Do not add autosave or text export.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Confirm before clearing non-empty input; cancel retains text; confirm clears; reload and route navigation discard text; inspect/instrument storage and network for any reflection text payload.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-009.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-009.audit.json`.

## Acceptance
Automated tests cover cancel, confirm, reload/no persistence and no outbound reflection text; caveats if network interception unavailable.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
