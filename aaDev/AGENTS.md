# AI Development Agent Instructions — ADS Alpha 1
**Version:** 0.1.0 | **Authority:** Supporting implementation policy; subordinate to approved PRD v0.2, SRS v0.2.1, accepted ADRs and SAD v0.1.0.

## Read order, every task
1. `AA Dev/AGENTS.md`, `AA Dev/TESTING.md`, `AA Dev/TASKS.md` and the assigned `AA Dev/prompts/TASK-XXX.md`.
2. The applicable approved `docs/` PRD, SRS, SAD and ADRs **at their actual paths**. If unavailable or inconsistent, STOP and report `blocked`; do not silently reconstruct the requirements.
3. Existing repository structure, scripts, tests, package manager, and task dependencies.

## Authority
- Product Owner (human): product scope, philosophical copy and artwork approval, material expenses, release acceptance.
- Verse (off-device lead architect): task contracts, architectural interpretation, technical review, summaries; **not** an automatically connected tool.
- Development agent: implement **only** the assigned task and write evidence.
- Independent review agent: inspect changes and verify, without acting as the builder for the same task.
- Operator (human): transfers prompts/repo ZIP between devices. Never claim Verse saw a report until the operator uploaded it.

## Architectural invariants
Static Astro with Markdown editorial content; minimal React islands only for interaction; TypeScript; English Alpha 1; no backend, database, auth, external AI, telemetry, search, payment, visitor uploads or persistence of reflection text. Reading content works with JavaScript disabled. User-entered reflection never transmitted or stored in localStorage/sessionStorage/IndexedDB/cookies. No coercive/recruitment language. Avoid new dependencies absent demonstrated task need; log any requested exception and STOP if it affects approved scope.

## Execution contract
- Before modifying: record UTC start, Git HEAD, `git status --porcelain`, relevant repository scripts, baseline checks. A non-clean working tree is a **hold** until the operator resolves it; do not discard changes.
- Work on a dedicated task branch where feasible; no force pushes, destructive resets, secret exposure, or remote pushes without explicit instruction. Do not rewrite unrelated files or install global utilities.
- Single-responsibility: preserve test IDs, requirements, and boundaries. Add tests for changed behavior in the same task. Do not create unapproved philosophical prose as final published material: use clearly marked draft/placeholder content and flag Product Owner acceptance pending.
- After: run focused and available full checks defined in `TESTING.md`. Record exact commands, exit codes, evidence/log paths and relevant limitations. Inspect diff and no forbidden imports/network/persistence.
- Write `AA Dev/reports/tasks/TASK-XXX.result.json` matching `schemas/task-result.schema.json`. Use `not_run`/`unknown` for unavailable checks, never invent successes. Missing evidence means no verified claim.
- Request independent audit and do not label task `accepted` until external review passes and required gates are satisfied.
- If unable to proceed, report `blocked` with reason and a concrete next action; do not silently expand scope.

## Reports
JSON Schema files under `AA Dev/schemas/` are canonical. Human-readable prose is optional; evidence-rich JSON is required. Paths should be repository-relative. Sanitise logs; never publish secrets or visitor reflection. Agent recommendations remain recommendations until accepted by the appropriate authority.
