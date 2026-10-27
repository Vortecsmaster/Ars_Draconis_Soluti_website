# AA Dev — Ars Draconis Soluti
**Batch:** SPRINT-001 (10 scoped coding tasks) | **State:** Proposed for external agent feasibility review; no code executed.

This folder is our source-controlled AI-assisted development process. `AA Dev/AGENTS.md` is the authoritative instruction for any agent assigned a task **after** the operator gives it the task. Some tools only automatically detect a root-level `AGENTS.md`; see `ROOT-AGENTS-SHIM.md` for a minimal optional pointer. We do not depend on any vendor-specific auto-discovery.

## Quick start
1. Put this `AA Dev/` directory in the repository root. Place approved PRD, SRS, SAD and ADRs under `docs/` using the actual repository layout; update paths in `AGENTS.md` if needed. These were **not** included in this package to avoid accidentally overwriting originals.
2. Give Grok/Cursor `AA Dev/REVIEW-REQUEST-GROK.md` for a **review only**, not execution. Receive feedback before launching the batch.
3. For execution, give the development agent `AA Dev/AGENTS.md`, `AA Dev/TESTING.md`, `AA Dev/TASKS.md`, and the chosen `AA Dev/prompts/TASK-XXX.md` (or ensure it reads them), one task at a time.
4. Give a distinct review agent `AA Dev/REVIEW-AGENT.md`, the task report, changed files/diff, and the applicable specifications. Reviews must inspect evidence, not copy builder claims.
5. Agent writes conforming JSON reports into `AA Dev/reports/tasks/` and `AA Dev/reports/audits/`; store sanitized logs outside Git or under gitignored evidence. Use `python 'AA Dev/scripts/validate_reports.py'` to check required report shape (lightweight validation; **not** a full JSON-Schema validator).
6. After 10 accepted tasks, collect the repository ZIP including reports, diffs/commits and relevant logs, and upload it to Verse for an executive briefing. Verse has no live access to remote agents or machines.

## Files
- `AGENTS.md`: mandatory agent behavior and decision authority.
- `TESTING.md`: minimum verification gates and evidence requirements.
- `REVIEW-AGENT.md`: independent audit instructions.
- `TASKS.md`: backlog, order and dependencies.
- `prompts/`: atomic coding task contracts.
- `schemas/`: JSON Schema Draft 2020-12 contracts (source of truth for reporting formats).
- `reports/`: agent output; do not fabricate or pre-fill successful results.
- `sprints/`: sprint definition and checkpoint policy.

**No forced requirement to run 10 tasks without intervention.** Stop on blockers. Never overwrite existing project work merely to match this scaffold.
