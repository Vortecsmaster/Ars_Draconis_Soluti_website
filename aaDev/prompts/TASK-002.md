# TASK-002 — Astro/React TypeScript project baseline
**Sprint:** SPRINT-001 | **Depends on:** 001
**SRS References:** SRS-PER-002
**Single responsibility:** Make the existing repository able to produce a static Astro build with TypeScript and React integration, if not already configured.

## Allowed changes
Build config and package manifests; minimal starter routes if necessary

## Prohibited / boundaries
No service, auth or data collection; preserve existing code.

## Before actions (must record evidence)
1. Read approved PRD/SRS/SAD/ADRs, `AA Dev/AGENTS.md`, `TESTING.md`, and this task.
2. Confirm prerequisite task audit approvals, clean Git status, Git HEAD and actual tooling/scripts. If not true, STOP with `blocked` JSON rather than assume.
3. Record baseline build, lint/typecheck and targeted tests **if available**; capture exact commands, exit codes and logs.
4. Inspect existing files to avoid duplicate or destructive scaffolding.

## Implementation instructions
Reuse compatible existing framework if already present. Pin versions/lockfile as appropriate and verify Astro static output. Establish scripts for build/check/test where available. Do not overwrite existing prototype.

## After actions (must record evidence)
1. Run targeted tests and any available build/type/lint checks; record failures as failures, not omissions.
2. Inspect `git diff --check`, changed file list and dependency changes, and scan affected code for unauthorized backend, identity, telemetry, user-text storage or text transmission.
3. Verify acceptance criteria against evidence. **Do not** claim success if required checks could not run; record `not_run` and limitations.
4. Write `AA Dev/reports/tasks/TASK-002.result.json` following `AA Dev/schemas/task-result.schema.json`; include prechecks/postchecks, commit refs, evidence paths and outstanding issues.
5. Submit changed files/diff and JSON to independent reviewer using `AA Dev/REVIEW-AGENT.md`. Review agent writes `AA Dev/reports/audits/TASK-002.audit.json`.

## Acceptance
Static build succeeds, output contains HTML entry, no backend runtime or unexpected dependencies.

**Task status:** Not started. This prompt is a specification, not proof of execution. A reviewer pass and required gates are necessary before treating it as accepted.
