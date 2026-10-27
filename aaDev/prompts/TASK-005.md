# TASK-005 — Public navigation and stable route skeleton
**Sprint:** SPRINT-001 | **Depends on:** 004
**SRS References:** SRS-FR-004, SRS-FR-005, SRS-FR-009
**Single responsibility:** Implement curated accessible navigation and route skeletons for all required sections.

## Allowed changes
src/pages, navigation component and its tests

## Prohibited / boundaries
Do not create final unapproved content, no client-side router.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Provide routes for home/philosophy/pillars/reflect/about/privacy and 404; use anchors; show active destination where applicable. Route copy remains clearly provisional.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-005.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-005.audit.json`.

## Acceptance
All routes build and deep links work in static preview; keyboard navigation works and links are predictable.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
