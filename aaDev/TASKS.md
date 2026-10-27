# ADS — SPRINT-001 Coding Backlog

**Execution:** Sequential by dependencies; operator manually transfers prompts. **Task status:** all proposed, not executed.

| ID | Atomic result | Dependencies | Requirements |
|---|---|---|---|
| TASK-001 | Repository baseline and tooling manifest | none | SRS-OPS-001 |
| TASK-002 | Astro/React TypeScript project baseline | 001 | SRS-PER-002 |
| TASK-003 | Global design tokens and responsive base | 002 | SRS-UX-001, SRS-UX-002 |
| TASK-004 | Shared Astro page shell | 003 | SRS-FR-003, SRS-INT-001 |
| TASK-005 | Public navigation and stable route skeleton | 004 | SRS-FR-004, SRS-FR-005, SRS-FR-009 |
| TASK-006 | Markdown editorial content collection | 002 | SRS-FR-008, SRS-DAT-001, SRS-DAT-002 |
| TASK-007 | Philosophy and five pillars presentation | 005 | SRS-FR-006, SRS-FR-007, SRS-FR-026 |
| TASK-008 | Reflection prompt selector and editor | 005 | SRS-FR-012, SRS-FR-013, SRS-FR-014, SRS-FR-015, SRS-FR-016, SRS-FR-017 |
| TASK-009 | Reflection clear/confirm and privacy checks | 008 | SRS-FR-018, SRS-FR-019, SRS-FR-020, SRS-FR-021, SRS-FR-022, SRS-DAT-003 |
| TASK-010 | Batch-one integration and quality harness | 003,004,005,006,007,008,009 | SRS-UX-001, SRS-UX-002, SRS-PER-002, SRS-FR-027 |

## Required steps
Each assigned prompt points to `AGENTS.md`, `TESTING.md`, its JSON report schema and independent audit. A report file does not imply acceptance. Sprint is ready for architectural review by Grok/Cursor; do not begin execution until repository compatibility review and initial baseline check. If current repo already implements a task, verify it and report that outcome; do not rewrite functioning code solely to generate a diff.

## Checkpoint policy
After approximately 10 independently reviewed tasks, operator uploads repository ZIP (and sanitized evidence as necessary) for Verse to inspect. Halt early on material contradictions, failed quality gates or Product Owner decisions. User-approved SRS remains authoritative.
