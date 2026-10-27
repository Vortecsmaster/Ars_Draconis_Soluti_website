# Architecture Decision Record — Deploy Without Application Backend or Identity

**Product:** Ars Draconis Soluti  
**Document ID:** ADR-ADS-003  
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

**Decision:** Ship static public assets only, without application servers, database, authentication, payment endpoints or AI inference for Alpha 1.

**Scope:** Alpha 1 visitor-facing experience and its release workflow. Does not authorize features excluded by the PRD.

## 2. Context and Problem

The approved Alpha 1 scope excludes accounts, storage, user submissions and personalized services.

**Drivers / references:** PRD FR-001, FR-013; SRS-FR-001, SRS-FR-018, SRS-SEC-001–004.

**Assumptions:** The Product Owner-approved scope remains static and anonymous. Implementation versions will be pinned and maintained in the repository.

## 3. Options Considered

| Option | Benefits | Costs / drawbacks |
|---|---|---|
| A — Static hosting only | Directly supports approved requirements and minimizes scope | Must uphold specific quality constraints |
| B — Serverless API + database | Could support future or alternative products | Adds complexity or conflicts with Alpha 1 constraints |
| C — CMS-hosted dynamic website | Common alternative implementation model | Weak fit for current product requirements |

## 4. Decision and Rationale

**Selected:** Static hosting only. Reduces attack surface, operations and privacy obligations while meeting approved scope.

The decision must be revisited if approved product requirements change; future-proofing alone does not authorize added runtime infrastructure.

## 5. Consequences and Trade-offs

**Positive:** Reduces attack surface, operations and privacy obligations while meeting approved scope.

**Negative / risk:** Future membership or AI functions require a separately approved architecture change.

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
