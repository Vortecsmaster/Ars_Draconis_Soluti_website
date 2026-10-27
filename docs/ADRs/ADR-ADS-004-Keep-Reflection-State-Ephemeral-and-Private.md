# Architecture Decision Record — Keep Reflection State Ephemeral and Private

**Product:** Ars Draconis Soluti  
**Document ID:** ADR-ADS-004  
**Version:** 0.1.0  
**Date:** 2026-10-25  
**Author:** Lead Software Architect (AI-assisted)  
**Product Owner:** Roberto Cerrud  
**Status:** Accepted as architecture baseline (subject to revision control)  
**Related PRD:** PRD-ADS-001 v0.2  
**Related SRS:** SRS-ADS-001 v0.2.1  
**Related SAD:** SAD-ADS-001 v0.1.0  
**Supersedes:** None

## 1. Decision Summary

**Decision:** Hold typed reflection text only in in-memory React component state; never write to browser persistence, URLs, requests or service workers; clear on page navigation/reload.

**Scope:** Alpha 1 visitor-facing experience and its release workflow. Does not authorize features excluded by the PRD.

## 2. Context and Problem

User approved no persistence and no transmission; clear action must confirm when non-empty.

**Drivers / references:** PRD FR-009–014; SRS-FR-012–022, SRS-SEC-003.

**Assumptions:** The Product Owner-approved scope remains static and anonymous. Implementation versions will be pinned and maintained in the repository.

## 3. Options Considered

| Option | Benefits | Costs / drawbacks |
|---|---|---|
| A — In-memory component state | Directly supports approved requirements and minimizes scope | Must uphold specific quality constraints |
| B — localStorage or IndexedDB persistence | Could support future or alternative products | Adds complexity or conflicts with Alpha 1 constraints |
| C — Remote sync | Common alternative implementation model | Weak fit for current product requirements |

## 4. Decision and Rationale

**Selected:** In-memory component state. Matches approved privacy behavior with the fewest moving parts.

The decision must be revisited if approved product requirements change; future-proofing alone does not authorize added runtime infrastructure.

## 5. Consequences and Trade-offs

**Positive:** Matches approved privacy behavior with the fewest moving parts.

**Negative / risk:** Reload/navigation intentionally loses text; disclose and test that loss.

**Reversibility:** Review through a new superseding ADR; do not silently alter accepted architectural constraints.

## 6. Implementation and Verification

- Verify implemented code and deployment match the decision, with traceability to cited SRS requirements.
- Execute applicable build, automated interaction, security, and privacy tests.
- Verify architecture constraints during independent diff review; preserve evidence in milestone reports.
- Any unresolved operational provider or exact tool/version selection is tracked in SAD §13, not misrepresented as a product approval.

## 7. Review and Approval

| Role | Decision | Date |
|---|---|---|
| Product Owner | Architecture direction authorized in project discussion; actual source/artwork reviewed separately | 2026-10-25 |
| Lead Architect (AI-assisted) | Recommended and documented | 2026-10-25 |

## 8. Document Control

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-25 | Initial architecture decision record |
