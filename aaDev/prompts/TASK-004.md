# TASK-004 — Shared Astro page shell
**Sprint:** SPRINT-001 | **Depends on:** 003
**SRS References:** SRS-FR-003, SRS-INT-001
**Single responsibility:** Create a shared accessible document/layout shell for public routes.

## Allowed changes
src/layouts and minimal usage pages

## Prohibited / boundaries
No React hydration for static reading pages; branding asset provisional.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Implement title, metadata, landmarks and common shell; avoid introducing search or accounts; validate static HTML and landmark structure.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-004.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-004.audit.json`.

## Acceptance
Pages render semantic header/main/footer and functional document title with JavaScript disabled.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
