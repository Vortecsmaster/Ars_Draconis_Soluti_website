# Architecture Decision Record — Use Astro Static Generation with React Islands

**Product:** Ars Draconis Soluti  
**Document ID:** ADR-ADS-001  
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

**Decision:** Use Astro static site generation for routes, layouts and editorial rendering, with React islands exclusively for interactions requiring client-side state.

**Scope:** Alpha 1 visitor-facing experience and its release workflow. Does not authorize features excluded by the PRD.

## 2. Context and Problem

Static content must be readable with minimal client JavaScript; the reflection view requires interactivity.

**Drivers / references:** PRD FR-004–007, FR-009–011; SRS-FR-004–009, SRS-PER-002.

**Assumptions:** The Product Owner-approved scope remains static and anonymous. Implementation versions will be pinned and maintained in the repository.

## 3. Options Considered

| Option | Benefits | Costs / drawbacks |
|---|---|---|
| A — Astro static generation + React islands | Directly supports approved requirements and minimizes scope | Must uphold specific quality constraints |
| B — Full React single-page application | Could support future or alternative products | Adds complexity or conflicts with Alpha 1 constraints |
| C — Traditional server-rendered CMS | Common alternative implementation model | Weak fit for current product requirements |

## 4. Decision and Rationale

**Selected:** Astro static generation + React islands. Lower shipped JavaScript for reading pages and clear separation of static and interactive responsibilities.

The decision must be revisited if approved product requirements change; future-proofing alone does not authorize added runtime infrastructure.

## 5. Consequences and Trade-offs

**Positive:** Lower shipped JavaScript for reading pages and clear separation of static and interactive responsibilities.

**Negative / risk:** A React island can still introduce excess bundle size; limit hydration and test production artifacts.

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
