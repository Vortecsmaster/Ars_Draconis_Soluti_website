# ADR-ADS-006 — File-Based Human-Mediated AI Development Orchestration
**Status:** Proposed — pending formal architecture baseline incorporation
**Date:** 2026-10-26
**Decision owners:** Lead Architect, Product Owner (operating model accepted in conversation)

## Context
Development agents operate on devices/platforms not directly accessible to Verse. The Product Owner already uses a directory named `AA Dev` and transfers repository ZIPs for review.

## Decision
Use repository-local `AA Dev` Markdown policies/prompts, JSON Schema-validated task/audit/sprint reports and Git references as a portable interface. The Product Owner initiates external agents and transfers repository ZIPs to Verse. Verse interprets reports and supporting source evidence and produces concise executive summaries; no claim of live orchestration.

## Alternatives
Vendor-specific orchestration platform (more setup and lock-in); relying solely on chat history (nonreproducible); unstructured text reports (difficult to validate).

## Consequences
Explicit manual handoffs; robust traceability with few dependencies; logs and privacy require sanitization. Different agent clients may need an optional root AGENTS.md shim.

## Verification
Run one coding task and one genuinely independent audit; check JSON report validation and successful ZIP review before considering process operational.
