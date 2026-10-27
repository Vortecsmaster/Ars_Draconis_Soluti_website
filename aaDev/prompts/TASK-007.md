# TASK-007 — Philosophy and five pillars presentation
**Sprint:** SPRINT-001 | **Depends on:** 005
**SRS References:** SRS-FR-006, SRS-FR-007, SRS-FR-026
**Single responsibility:** Implement semantic, static rendering of LOGOS→LEGGOS→DRAGON and five named pillars.

## Allowed changes
philosophy/pillars route components and content references

## Prohibited / boundaries
Philosophical copy and dragon art not approved by coding agent.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Use clearly labeled draft editorial strings or verified approved source text; structure five pillars and synthesis in static HTML; attach product-owner editorial acceptance flag.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-007.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-007.audit.json`.

## Acceptance
All 5 named pillars and 3 synthesis stages render, accessible and no JS needed; final copy remains approval-blocked.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
