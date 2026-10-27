# TASK-006 — Markdown editorial content collection
**Sprint:** SPRINT-001 | **Depends on:** 002
**SRS References:** SRS-FR-008, SRS-DAT-001, SRS-DAT-002
**Single responsibility:** Create a validated Markdown editorial collection with stable slugs and one draft example article.

## Allowed changes
src/content and required editorial route only

## Prohibited / boundaries
Draft text is NOT approved publication content; no hard-coded final essays.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Use content schema compatible with pinned Astro version. Add required metadata and render Markdown as static HTML. Example must be marked DRAFT and excluded from public production until editorial approval.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-006.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-006.audit.json`.

## Acceptance
Content validation rejects missing metadata, route is predictable, static page builds; no user input collection.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
