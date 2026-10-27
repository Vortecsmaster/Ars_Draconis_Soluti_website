# Verification Policy — ADS Alpha 1
**Version:** 0.1.0

## General gates
Pre-checks: record HEAD/status; identify relevant SRS IDs, baseline scripts, dependencies, existing tests. Run available baseline checks without changing configuration; mark unavailable checks as `not_run`.
Post-checks, as available and appropriate: package-manager lockfile integrity, TypeScript/typecheck, formatter/lint, unit/component tests, static build, route smoke tests, git diff inspection, no forbidden service/storage/network additions. Log exact command + exit code + artifact path (do not paste large logs into JSON). A failing existing baseline is not evidence the task introduced the failure; report both states.

## Quality by stage
- Early scaffold tasks: build/type/lint/test only when corresponding scripts exist. If browser E2E is not yet configured, record `not_run` with reason; it is a milestone gate, not a fabricated per-task pass.
- Interactive reflection: component/E2E assertions that input edits in memory, resets after reload/navigation, cancel/confirm clear works, **no transmission and no browser persistence**; inspect code AND instrument network/storage in test environment.
- Public content: routes, stable anchors, keyboard operation, no-JS readability and correct English labels.
- Accessibility: automated axe-style checks are supplemental; critical journeys additionally need keyboard/focus/contrast/reduced motion and manual review before release. WCAG 2.2 AA is approved; passing axe alone is not proof of full compliance.
- Performance: approved Lighthouse mobile ≥90, 3 repeatable production-profile runs with median ≥90; don't invent numbers or run against `astro dev` and call it production. Run when representative deployment preview is available; interim `not_run` is acceptable with documented milestone/release blocker.
- Browser matrix: current Chrome/Firefox/Safari/Edge; limitations must be recorded. Safari may need a separate environment.
- Editorial wording, official symbol, privacy/hosting disclosure and release sign-off require Product Owner review: automated checks cannot substitute.

## Exit rules
`pass`: observed exit code 0 and evidence path for the check. `fail`: observed nonzero or actual failed assertion. `not_run`: not executed with reason. `unknown`: evidence missing or uninterpretable. Severity `blocker`/`critical` findings stop progression. Reviewer must document coverage gaps.

## Evidence artifacts
Task report at `AA Dev/reports/tasks/TASK-XXX.result.json` + independent audit at `AA Dev/reports/audits/TASK-XXX.audit.json` + optional logs at `AA Dev/.evidence/TASK-XXX/` (gitignored; include sanitized logs in ZIP if needed). Avoid logs containing secrets, personal text, or access tokens.

## Tooling policy
Adopt test tooling consistent with existing repository. Candidates: Vitest, React Testing Library, Playwright, automated accessibility checks, Lighthouse CI. Versions and dependency changes require verified upstream compatibility and an explicit task; do not add tools speculatively. `npm run ...` examples in tasks are illustrative; use actual project scripts and report commands used.
