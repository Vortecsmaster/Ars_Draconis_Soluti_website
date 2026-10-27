# TASK-008 — Reflection prompt selector and editor
**Sprint:** SPRINT-001 | **Depends on:** 005
**SRS References:** SRS-FR-012, SRS-FR-013, SRS-FR-014, SRS-FR-015, SRS-FR-016, SRS-FR-017
**Single responsibility:** Implement one React island offering at least 3 selectable prompts and editable multiline text in memory only.

## Allowed changes
src/components/react/ReflectionExperience.tsx and reflect route/tests

## Prohibited / boundaries
No backend, AI replies, analytics, browser persistence or network transfer.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Prompt selection and controlled textarea; explicit local/ephemeral notice; add unit/component tests for selecting and editing. Do not implement clear-confirm behavior yet (TASK-009).

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-008.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-008.audit.json`.

## Acceptance
Tests verify selection, editing, accessible labels and no fake AI output; no storage/network API added.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
