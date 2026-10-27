# Software Architecture Document (SAD)

**Product:** Ars Draconis Soluti — The Art of the Unleashed Dragon  
**Document ID:** SAD-ADS-001  
**Version:** 0.1.0  
**Date:** 2026-10-25  
**Author / Lead Architect:** Lead Software Architect (AI-assisted)  
**Product Owner:** Roberto Cerrud  
**Status:** Architecture baseline — ready for implementation planning; release evidence pending  
**Source PRD:** PRD-ADS-001 v0.2 (Approved)  
**Source SRS:** SRS-ADS-001 v0.2.1 (Approved baseline)  
**ADRs:** ADR-ADS-001–005 v0.1.0  
**Release:** Alpha 1

> This SAD is an architect-authored implementation baseline. Approval of its direction does not imply that code, deployment, privacy policy, editorial content, or artwork has been delivered or independently audited.

---

# 1. Introduction

## 1.1 Purpose

Define the structural and operational design for a static, anonymous public philosophical site with optional ephemeral reflection. PRD specifies intent, SRS specifies verifiable behavior, ADRs record decisions, and this SAD organizes implementation.

## 1.2 Scope

**Includes:** static pages, editorial publishing, curated navigation, philosophy/pillars, reflection UI, privacy/about content, automated quality gates, static deployment. **Excludes:** API, server-side state, database, identity, personalized AI, payments, search, analytics, community, Web3, native apps.

## 1.3 Applicable Documents

| ID | Document | Version |
|---|---|---|
| PRD-ADS-001 | Product Requirements Document | 0.2 |
| SRS-ADS-001 | Software Requirements Specification | 0.2.1 |
| ADR-ADS-001–005 | Architecture decisions | 0.1.0 |

## 1.4 Definitions and Conventions

**Island:** JavaScript-hydrated component within an otherwise static page. **Build time:** content compilation before deployment. **Release gate:** mandatory check before production publishing. `shall` denotes normative architectural constraint; `should` denotes preference subject to documented review.

# 2. Architectural Drivers and Constraints

## 2.1 Goals

1. Philosophical fidelity under Product Owner control (SRS-FR-026–027; UX-005).
2. Anonymous open access without remote reflection submission (SRS-FR-001, 018; SEC-003).
3. Mobile-first clarity, WCAG 2.2 AA on critical journeys, and Lighthouse mobile ≥90 (SRS-UX-001–002; PER-001).
4. Maintainable content publishing and testable, low-complexity static delivery.

## 2.2 Non-negotiable Boundaries

- No runtime backend, hosted database, authentication, external AI service, payment integration or analytics in Alpha 1.
- Reflection text shall not be serialized to network, persistent browser storage, URLs, logs, or caches.
- Visitor-facing content is English only in Alpha 1, and curated navigation excludes search.
- Actual final copy and visual symbol shall be signed off by Product Owner prior to release.

## 2.3 Trade-offs

The chosen architecture favors minimal runtime complexity over immediate online editorial editing or synchronized user state. Future service features require a new PRD/SRS baseline and ADRs, not placeholder implementation today.

# 3. Architecture Overview

## 3.1 System Context

```text
Content editor --(Markdown in Git)--> build pipeline --(static output)--> static host/CDN
                                                                    |
Visitor browser <--(HTTPS static HTML/CSS/JS/assets)-----------------+
       | 
       +-- reads pages without React hydration
       +-- activates React reflection island (memory-only local text)
       +-- no visitor-submitted content endpoint
```

External actors include Git hosting/build CI and static delivery infrastructure; hosts may log HTTP metadata but receive no reflection text via app features.

## 3.2 Runtime Components

| Component | Ownership | Implementation | Requirement mapping |
|---|---|---|---|
| Static page router and layouts | Astro | Pre-rendered routes, shared shell, headings, metadata | FR-001–005, 009, 011 |
| Editorial content | Astro content collections / Markdown | Validated text, metadata, slug generation | FR-006–010, DAT-001–002 |
| Pillar/philosophy navigation | Astro by default | Deep links and curated access to concepts | FR-004, 006–009 |
| Reflection interface | React island | Prompt selection, text entry, clear confirmation | FR-012–022 |
| Privacy and about pages | Astro | Actual verified disclosure and principles | FR-023–025; UX-005 |
| Design system | CSS custom properties + component styles | Consistent typography, responsive layouts, motion controls | UX-001–003, INT-001–005 |
| Build and verification | Node toolchain / CI | Static generation, lint/type/test/audit | SRS §11 |

No separate API boundary is implemented.

# 4. Component Architecture and Boundaries

## 4.1 Dependency Rules

- `src/pages` composes public routes; no business data collection.
- `src/layouts` owns document structure, metadata, landmarks and navigation chrome.
- `src/content` owns editorial Markdown and collection metadata; rendering components must not hardcode long-form articles.
- `src/components/astro` contains presentational pieces that do not require visitor state.
- `src/components/react` contains only components that need interaction; isolate reflection state here.
- `src/lib` may contain pure typed domain utilities and content helpers; no server-client transport adapter is needed.
- Components shall not import secrets, access unknown third-party tracking services or introduce storage of reflection text.

## 4.2 Proposed Repository Layout

```text
/
  docs/product/PRD.md
  docs/requirements/SRS.md
  docs/architecture/SAD.md
  docs/architecture/adr/ADR-ADS-*.md
  docs/development/{TESTING,AUDIT,TASKS}.md
  src/pages/{index,philosophy,pillars,reflect,about,privacy,404}.astro
  src/content/{config.ts,essays/,concepts/}
  src/layouts/BaseLayout.astro
  src/components/{astro/,react/ReflectionExperience.tsx}
  src/lib/
  src/styles/{tokens.css,global.css}
  public/
  tests/{unit,component,e2e}/
  AGENTS.md
  astro.config.mjs
  package.json
```

Paths are design targets, not a representation of an existing repository. Astro-specific content-collection configuration placement shall match the pinned Astro version at implementation time.

## 4.3 Hydration and Navigation

- Landing, about, privacy, essays, philosophy and five pillars should render as static HTML.
- Only interactive React reflection subtree hydrates, preferably on visibility/load as necessary to avoid impaired usability.
- Use standard anchors for shareable pages/sections; no JS-only routing requirement.
- Missing routes provide a comprehensible 404 page; host rewrite/fallback behavior must be verified on deployment preview.

# 5. Data Architecture

## 5.1 Data Classification

| Data | Lifecycle | Storage / exposure |
|---|---|---|
| Public editorial content | Authored → reviewed → built → published | Versioned in Git; distributed publicly |
| Navigation/pillar metadata | Built → served | Public compiled build assets |
| Reflection prompts | Authored → built → served | Public; no personal information |
| Typed reflection text | Created → edited → cleared/unmounted | React memory only; never persisted or transmitted |
| Host HTTP metadata | Host-managed | Verify actual host policy and disclose accurately |

## 5.2 Reflection State Machine

```text
INITIAL -> PROMPT_SELECTED -> EDITING
EDITING --clear--> CONFIRM_CLEAR --cancel--> EDITING
CONFIRM_CLEAR --confirm--> INITIAL
EDITING --reload/navigation/unmount--> DISCARDED
```

When input is empty, clear may reset without confirmation. Do not attach text to prompt identifiers, URLs, storage APIs, crash reporting or telemetry. Avoid implicit auto-save. If hydration fails, the content pages remain readable and the reflection interaction reports an accessible unavailable state (rather than pretending to save/submit).

## 5.3 Content Integrity

Every published essay must have valid metadata and unique stable slug; broken references fail validation. Final approved copy and images are release artifacts; content correctness does not follow merely from successful compilation.

# 6. Interface Architecture

- HTML semantic anchors, buttons and labeled textarea form the visitor interface.
- No feature-level third-party API or form-submission contract exists.
- External links must be visibly distinguishable and reviewed against current privacy disclosures.
- On narrow devices, navigation and controls shall remain keyboard reachable, focus-visible and without unintended horizontal page overflow.

# 7. Security and Privacy Architecture

## 7.1 Threats and Mitigations

| Threat | Mitigation | Evidence |
|---|---|---|
| Leakage of reflection content | Memory-only UI; browser-network assertions; storage checks; dependency review | E2E privacy test + code inspection |
| Secret in public bundle | Secret scan and build artifact inspection | CI security check |
| Insecure delivery | Enforce HTTPS and mixed-content checks | Deployment smoke test |
| Third-party tracking or remote fonts | Prefer self-hosted assets, disclose any verified exception | Asset inventory + privacy review |
| Injection through rendered content | Build-time content validation; avoid untrusted raw HTML and dynamic HTML injection | Dependency/content audit |
| Supply-chain compromise | Lockfile, version pinning, dependency review | CI logs and audit notes |

## 7.2 Privacy Statement Boundaries

No application submission of reflection does not imply that host HTTP request logs are absent. Privacy copy must be validated against the actual hosting service, external resource list, cookies and any access logs. No visitor identity is required.

# 8. Deployment and Operations

## 8.1 Static Build and Delivery

Build output is deployable static assets. Use a static host that supports HTTPS, deep links, cache-control, custom domain and 404. Hosting vendor is **not yet selected**; do not present availability as guaranteed.

## 8.2 Delivery Pipeline

```text
Pull request -> formatting/lint -> type check -> unit/component tests
             -> production build -> link/content validation -> E2E
             -> accessibility automated scan -> bundle/Lighthouse review
             -> independent diff audit -> review/merge -> preview smoke test
             -> Product Owner editorial/visual approval -> production publish
```

A complete manual WCAG audit must supplement automated checks on critical journeys; automated axe-style checks alone are not equivalent to WCAG conformance.

## 8.3 Rollback and Recovery

All site releases are versioned static builds. Rollback should redeploy a known-good commit/artifact, with DNS/domain/host operations documented once provider is selected. No server-side reflection data requires recovery.

# 9. Quality Requirements Implementation

| Quality attribute | Architecture control | Verification |
|---|---|---|
| Mobile performance ≥90 | Static pages, minimal hydration, compressed assets | Three Lighthouse mobile runs; median ≥90 |
| Accessible critical journeys | Semantic HTML, focus management, contrast, reduced motion | Playwright + a11y checks + manual WCAG review |
| Browser/device compatibility | Progressive enhancement; standards-compliant CSS/DOM | Latest stable Chrome, Firefox, Safari, Edge test matrix |
| Readability with JS disabled | Static HTML for editorial content | Disable JS and test content journeys |
| Reflection privacy | No persistence/network calls containing input | Storage and network assertions |
| Provisional asset budget | Avoid unnecessary dependencies, prioritize compression | Build stats; revise budget with architecture rationale if needed |
| Availability proposed 99.5% | Vendor evaluation and host configuration | Verify provider characteristics after selection |

The PRD does not approve exact bundle size or promise 99.5% SLA; those remain engineering/provider checks.

# 10. Architectural Verification and Agent Audit

- Each task shall cite SRS IDs, files allowed to change, dependencies, and pre/post checks.
- Before work: verify clean Git status, tests baseline and prerequisite tasks; capture baseline results.
- After work: run targeted tests, full checks as relevant, inspect diff, detect unauthorized dependencies/network/storage usage; save evidence.
- An independent review role shall examine the actual diff and execute checks where feasible rather than accepting the builder agent's self-report.
- Failed gates block task completion; material ambiguity escalates to Product Owner rather than silently changing philosophy.
- Human review after approximately ten tasks is a planning convention, not permission to ignore failures.
- Test and review reports shall map implementation and verification back to stable SRS IDs.

# 11. Architecture-to-Requirements Traceability

| Architectural element | SRS baseline | ADR |
|---|---|---|
| Astro static page rendering | FR-001–011, PER-002 | 001, 002 |
| React reflection island | FR-012–022; SEC-003 | 001, 004 |
| Content collections/Markdown | FR-006–010; DAT-001–002 | 002 |
| Static hosting/no identity | FR-001, 018; SEC-001–004 | 003 |
| Mobile/accessibility verification | UX-001–003, 006; INT-001–005 | 001, 005 |
| Philosophical review | FR-002, 026–027; UX-005 | 005 |

# 12. Architectural Risks and Controls

| Risk | Consequence | Mitigation / gate |
|---|---|---|
| React hydration extends beyond necessary interactions | Slow initial mobile load | Bundle and hydration audit |
| Reflection accidentally stored or transmitted | Breach of core privacy promise | Negative network/storage regression tests |
| Incorrect editorial or visual motif | Violates philosophical intent | Explicit Product Owner sign-off |
| Static deep-link deployment failures | Broken shareable URLs | Host preview deep-link smoke test |
| Third-party resource drift | Undisclosed data exchange | Dependency and external-host inventory |
| AI agents over-build architecture | Scope creep | ADR and SRS policy checks, independent diff audit |

# 13. Open Implementation Decisions and Release Preconditions

These do **not** invalidate approved product decisions, but should be settled by the architect or actual hosting evidence before their affected implementation tasks or release.

| ID | Item | Owner / action | Gate |
|---|---|---|---|
| IMP-001 | Select static hosting provider and confirm domain, deployment, HTTPS, availability characteristics | Architect recommends; Product Owner approves material cost | Before deployment |
| IMP-002 | Confirm exact package versions, CSS organization and CI runner | Architect | Before first implementation task |
| IMP-003 | Validate provisional page transfer budgets against meaningful mobile profile | Architect/QA | Before performance gate freezes |
| IMP-004 | Approve actual article text, dragon artwork and imagery licenses | Product Owner | Before release |
| IMP-005 | Verify hosting/resource privacy wording and applicable obligations | Architect + appropriate legal review when needed | Before release |
| IMP-006 | Record exact browser/OS/device test matrix and manual accessibility evidence | QA/Architect | Before release |

# 14. Document Control

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1.0 | 2026-10-25 | Lead Software Architect (AI-assisted) | Initial project-specific SAD from approved PRD/SRS and ADR decisions |

**Architecture recommendation:** Accepted as the planning baseline for Alpha 1, pending implementation and release verification. Material changes to framework, runtime services or visitor data handling require new/superseding ADR and PRD/SRS impact assessment.
