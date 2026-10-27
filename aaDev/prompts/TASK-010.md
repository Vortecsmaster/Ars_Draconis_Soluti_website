# TASK-010 — Batch-one integration and quality harness
**Sprint:** SPRINT-001 | **Depends on:** 003,004,005,006,007,008,009
**SRS References:** SRS-UX-001, SRS-UX-002, SRS-PER-002, SRS-FR-027
**Single responsibility:** Integrate minimally sufficient automated browser smoke and accessibility/privacy checks for the built routes.

## Allowed changes
tests/, scripts and CI config only when justified

## Prohibited / boundaries
Do not claim production Lighthouse or WCAG compliance without actual evidence; no unapproved content publication.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Test route navigation, no-JS reading, 320/375/768/1280 viewports, prompt interaction, static build and forbidden-feature smoke checks. Run checks; generate sprint summary only from actual task/audit reports.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-010.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-010.audit.json`.

## Acceptance
Batch smoke runs with evidence; any unexecuted cross-browser/performance/manual WCAG checks explicitly recorded as release gates.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
