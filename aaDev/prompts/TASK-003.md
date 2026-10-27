# TASK-003 — Global design tokens and responsive base
**Sprint:** SPRINT-001 | **Depends on:** 002
**SRS References:** SRS-UX-001, SRS-UX-002
**Single responsibility:** Establish minimal global typography, spacing, colors, focus and reduced-motion styling consistent with approved UX requirements.

## Allowed changes
src/styles and layout imports only

## Prohibited / boundaries
Do not finalize dragon artwork or invent philosophical copy.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Implement tokens/global CSS, sensible mobile baseline and accessible focus visibility. Add lightweight verification where available.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-003.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-003.audit.json`.

## Acceptance
Core layout has no primary horizontal overflow at 320/375/768/1280 widths; focus is visible; reduced motion respected.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
