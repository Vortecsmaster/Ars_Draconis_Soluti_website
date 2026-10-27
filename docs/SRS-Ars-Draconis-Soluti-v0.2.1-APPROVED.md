# Software Requirements Specification (SRS)

**Product:** Ars Draconis Soluti  
**Document ID:** SRS-ADS-001  
**Version:** 0.2.1  
**Date:** 2026-10-25  
**Author:** Product Architecture Working Draft  
**Product Owner:** Roberto Cerrud  
**Technical Lead:** Lead Software Architect (AI-assisted role)  
**Status:** Approved — requirements baseline (Product Owner decisions confirmed; technical sign-off recorded as architecture recommendation)  
**Source PRD:** PRD-ADS-001 v0.2 (Approved)

> **Baseline status:** Approved PRD v0.2 and Product Owner confirmation of the seven decision defaults on 2026-10-25. SRS v0.2.1 is the accepted Alpha 1 requirements baseline. Editorial artwork/text, final provider disclosures and technical verification remain release deliverables, not approvals already completed. SRS-UX-004 remains retired.

---

# 1. Introduction

## 1.1 Purpose

Specify externally observable and verifiable behavior for the Ars Draconis Soluti Alpha 1 website. The PRD explains intended product outcomes; this SRS describes the behavioral, interface, data, quality, and operational obligations to be verified. Architecture and detailed design are documented separately.

## 1.2 Scope

**Product:** Ars Draconis Soluti  
**Description:** A public, anonymous philosophical expression and self-guided contemplation experience whose purpose is faithful expression, not market validation or growth.  
**Software boundaries:** Public content navigation and rendering; guided reflection prompt selection; client-side text entry/clear operations; informational disclosures.  
**External dependencies:** Browser, hosting infrastructure, and network for loading the site.  
**Excluded responsibilities:** User accounts, server-side business functions, database, AI processing, payment, Web3, user messaging, cross-device persistence, and public administration workflows.

## 1.3 Applicable Documents

| Document ID | Document | Version | Status |
|---|---|---|---|
| PRD-ADS-001 | Ars Draconis Soluti PRD | 0.2 | Approved |
| ADR-ADS-001–005 | Architecture decisions | 0.1.0 | Accepted architecture baseline |
| SAD-ADS-001 | Software Architecture Document | 0.1.0 | Architecture draft; implementation guidance |
| UX-ADS-001 | Final brand/content and UX materials | — | Product Owner approval required before release |

## 1.4 Definitions and Acronyms

| Term | Definition |
|---|---|
| PRD | Product Requirements Document |
| SRS | Software Requirements Specification |
| SAD | Software Architecture Document |
| FR / NFR | Functional / Non-Functional Requirement |
| Reflection | Visitor-directed interaction consisting of chosen prompt and visitor-entered text, without automated interpretation |
| Alpha 1 | Initial public website release addressed here |
| Persistent storage | Storage surviving reloads, such as browser storage or remote storage |
| Verification | Test, analysis, inspection, or demonstration showing a requirement is satisfied |

## 1.5 Document Conventions

Requirements are singular and use stable IDs, **shall** statements, priority, source, observable criteria, and verification. The functional catalogue in §3 contains a compact requirements table; detailed preconditions, triggers, expected/failure behavior and acceptance examples are specified for interaction-critical groups in §3.4. Active SRS requirements form the **approved Alpha 1 baseline**. Provisional engineering budgets and final publishing/hosting evidence remain separately subject to verification. Retired IDs are not reused.

---

# 2. System Overview

## 2.1 System Perspective

A publicly accessible website is loaded through the visitor's browser. Editorial content is available without a visitor identity. A limited interactive reflection area handles locally entered text; no product-owned submission service is included. Hosting and browser network operations remain external to application-level reflection handling.

## 2.2 System Capabilities

| Capability ID | Description | PRD Reference |
|---|---|---|
| CAP-001 | Public identity, principles and navigation | FR-001–004, FR-015 |
| CAP-002 | Philosophical material and five pillars | FR-005–008, FR-017 |
| CAP-003 | Anonymous self-guided reflection | FR-009–014 |
| CAP-004 | Privacy, compatibility, accessibility and release quality | FR-016, NFRs |
| CAP-005 | Philosophical fidelity and non-coercive communication | BO-002–003; KPI-002; PRD §8 |

## 2.3 User Classes

| User Class | Description | Relevant Capabilities |
|---|---|---|
| Anonymous visitor | Reads public pages | CAP-001, CAP-002, CAP-004 |
| Reflecting visitor | Uses prompts and text entry anonymously | CAP-001–004 |
| Content editor / maintainer | Updates public content through approved publishing workflow outside visitor UI | CAP-002, CAP-004 |

No application account roles or privileged visitor functions are specified. Visitor adoption, engagement and popularity are not system objectives or product success measurements.

## 2.4 Operating Environment

Modern standards-capable phone, tablet, and desktop browsers. Initial language English. Viewing published pages requires network connectivity; interaction after loading may operate locally, but offline availability is **not guaranteed**. The tested browser versions and platforms will be documented by QA at release.

## 2.5 Assumptions and Dependencies

| ID | Assumption / Dependency | Impact if Invalid |
|---|---|---|
| AD-001 | Approved editorial content exists before publication | Publishing cannot be accepted |
| AD-002 | Approved visual identity exists before release | Branding acceptance is blocked |
| AD-003 | Hosting offers HTTPS access | Security acceptance is blocked |
| AD-004 | Reflection text is ephemeral by default | Requires change control if persistence requested |

## 2.6 Constraints

No Alpha 1 accounts, remote reflection submission, AI, blockchain, payments, or backend business services. Visitors must retain voluntary control of reflection text. These exclusions are confirmed in approved PRD v0.2. This SRS becomes a development baseline only upon separate approval.

---

# 3. Functional Requirements

## 3.1 Requirement Specification Format

Each requirement specifies its **ID**, shall-statement, **source**, **priority**, **verification**, and **status**. Unless noted, **Precondition:** the corresponding page has loaded; **Trigger:** the indicated navigation or visitor action; **Failure behavior:** no misleading confirmation or unexpected transmission, and the visitor receives readable feedback when a requested action cannot complete. Complex workflows are elaborated in §3.4.

## 3.2 Identity and Authentication

**Not applicable.** Alpha 1 contains no registration, login, recovery, identity provider, or authenticated session. **SRS-FR-001** establishes public access without such gates.

## 3.3 Authorization and User Management

**Not applicable.** No user roles or management interface exist in the deployed public application. Publishing permissions and repository security are operational concerns outside visitor functionality.

## 3.4 Core Business Functions

### 3.4.1 Public Identity and Navigation

| SRS ID | Normative statement (system shall...) | Source | Priority | Verification |
|---|---|---|---|---|
| SRS-FR-001 | Display the public landing experience without requiring authentication or payment. | FR-001 | High | Test |
| SRS-FR-002 | Include visibly readable wording on the landing/about experience establishing reflection, equality, and non-recruitment. | FR-002 | High | Inspection |
| SRS-FR-003 | Display the product name and an approved dragon/inner-flame visual motif on the landing page. | FR-003 | High | Inspection |
| SRS-FR-004 | Provide interactive navigation from the landing page to philosophy, pillars, reflection, and about/privacy information. | FR-004 | High | Test |
| SRS-FR-005 | Indicate the currently focused navigation destination or content heading so visitors can orient themselves. | FR-004 | Medium | Test |
| SRS-FR-006 | Publish separate distinguishable descriptions of LOGOS, LEGGOS, and DRAGON in a connected conceptual sequence. | FR-005 | High | Inspection |
| SRS-FR-007 | Present all five named pillars with a descriptive passage for each. | FR-006 | High | Test + Inspection |
| SRS-FR-008 | Expose at least one substantive essay/article accessible from a core navigation path. | FR-007 | High | Test |
| SRS-FR-009 | Give each primary editorial piece or principal concept an addressable location that can be reopened directly. | FR-017 | Medium | Test |
| SRS-FR-010 | Distinguish interpretive philosophy from professional advice wherever copy otherwise implies clinical or authoritative guidance. | FR-008 | Medium | Inspection |
| SRS-FR-011 | Provide a discoverable about/principles page or section stating that no instructor/follower relationship is offered. | FR-015 | High | Test + Inspection |
| SRS-FR-026 | Describe freedom in the core philosophy as arising through alignment with one's true self and deeper order, rather than merely external permission or resistance; use Product Owner-approved wording. | PRD §§2.1, 3.1 (BO-003) | High | Editorial inspection + Product Owner acceptance |
| SRS-FR-027 | Avoid compulsory engagement prompts, agreement-seeking calls to action, recruitment, registration funnels, or popularity/traction counters framed as proof of philosophical value in public journeys. | PRD §§2.2, 3.3, 8.1 | High | Inspection + journey test |

**Editorial fidelity constraint:** Published content and visitor-facing prompts must reflect the Product Owner-approved philosophy of inner alignment, conscious freedom, and voluntary contemplation among equals. Presenting the site as a program of instruction, initiation, spiritual authority, or coercive recruitment would violate PRD §§2.1–2.2 and 8.1. This is verified by Product Owner editorial acceptance, not audience response.

**Workflow example — public reading:** Precondition: URL opened in supported browser. Trigger: visitor selects Philosophy or Pillars. Expected behavior: requested material becomes readable and page orientation is clear. Failure behavior: a missing route displays a comprehensible not-found state rather than a blank screen. Acceptance: direct links work after page reload.

### 3.4.2 Self-Guided Reflection

| SRS ID | Normative statement (system shall...) | Source | Priority | Verification |
|---|---|---|---|---|
| SRS-FR-012 | Provide a discoverable entry into the optional reflection experience without a user identity. | FR-009 | High | Test |
| SRS-FR-013 | Display at least three selectable, distinct starting prompts. | FR-010 | High | Test |
| SRS-FR-014 | After the visitor selects a prompt, display its text as the context for reflection. | FR-010 | High | Test |
| SRS-FR-015 | Allow the visitor to enter, edit, and remove text in a labeled multiline input. | FR-011 | High | Test |
| SRS-FR-016 | Keep entered reflection text available while the relevant component remains active during normal typing and editing. | FR-011 | High | Test |
| SRS-FR-017 | Describe reflection as visitor-directed and not present any automatic text interpretation or simulated AI-generated replies. | FR-012 | High | Inspection + Test |
| SRS-FR-018 | Avoid network requests whose payload includes visitor reflection text. | FR-013 | High | Test + Inspection |
| SRS-FR-019 | Disclose clearly before or within the reflection interaction that the entered text is not submitted and is discarded on reload or navigation. | FR-013 | High | Inspection |
| SRS-FR-020 | Provide an explicit clear/restart action with confirmation if text is non-empty. | FR-014 | Medium | Test |
| SRS-FR-021 | Preserve the existing text when the visitor cancels the clear confirmation. | FR-014 | Medium | Test |
| SRS-FR-022 | Remove the current text when the visitor confirms clear/restart. | FR-014 | Medium | Test |

**Workflow — prompt selection:** Precondition: reflection view opened. Trigger: choose a prompt. Expected: the selected prompt is identifiable and writing can begin. Failure: if no prompt is selected, Alpha 1 provides selection of at least three starting prompts; freeform without prompt is not a committed workflow.

**Workflow — text entry:** Precondition: reflection view active. Trigger: typing or editing. Expected: entered content remains visible during the active interaction. Failure: if browser page unloads or crashes, recovery is **not promised**. Acceptance: text does not appear in request bodies, URL parameters, browser persistence stores, or analytics payloads under standard usage.

**Workflow — clear/restart:** Precondition: text field non-empty. Trigger: select Clear. Expected: explicit confirmation. If canceled, text remains; if accepted, text becomes empty. If input is already empty, a clear action may operate without confirmation.

### 3.4.3 Information and Privacy

| SRS ID | Normative statement (system shall...) | Source | Priority | Verification |
|---|---|---|---|---|
| SRS-FR-023 | Provide discoverable information about actual site data handling and external resources. | FR-016 | High | Inspection |
| SRS-FR-024 | State accurately whether reflection text is transmitted, persisted, or collected. | FR-013, FR-016 | High | Inspection + Test |
| SRS-FR-025 | Avoid claiming that the host collects no request metadata unless verified for the selected hosting arrangement. | FR-016 | High | Inspection |

## 3.5 Notifications and Communications

**Not applicable.** There are no email, push, transactional, or user-specific alerts in Alpha 1. In-page feedback for actions is specified under reflection and interface requirements.

## 3.6 Reporting and Administration

**No visitor-facing administration, dashboard, analytics, or business reporting is required. Engagement, conversion, traction, and adoption metrics are expressly not Alpha 1 success criteria.** Publishing and build verification are controlled outside the deployed application.

---

# 4. Web3 Requirements (If Applicable)

Not applicable. No wallet, transaction, digital asset, smart contract, custody or chain-failure behavior exists in Alpha 1.

---

# 5. AI Requirements (If Applicable)

No AI capability is authorized in Alpha 1. Specifically, no generated recommendations, response interpretation, external model processing, AI decision authority, or AI output audit log. The reflection feature is a writing interaction and **shall not imply AI processing** (SRS-FR-017). Future AI requirements require PRD approval and a revised SRS.

---

# 6. External Interface Requirements

## 6.1 User Interfaces

| ID | Statement (the system shall...) | Source | Verification |
|---|---|---|---|
| SRS-INT-001 | Expose a usable navigation interface at mobile, tablet, and desktop sizes. | FR-004, UX §8 | Test |
| SRS-INT-002 | Provide keyboard-operable interactive controls with visible focus. | UX §8.2 | Test |
| SRS-INT-003 | Provide discernible labels for all reflection input and actions. | UX §8.2 | Test |
| SRS-INT-004 | Present readable error/not-found information for invalid public routes. | FR-004 (derived) | Test |
| SRS-INT-005 | Respect user preference for reduced motion in nonessential animated elements. | UX §8.2 | Test |

## 6.2 External Software Interfaces

| Interface ID | External System | Purpose | Required Capabilities |
|---|---|---|---|
| INT-001 | Hosting/CDN | Deliver public resources | HTTPS, static resource delivery |
| INT-002 | Visitor web browser | Render pages and enter local text | HTML, CSS, JavaScript capabilities as supported |

No feature-level third-party API is required; usage analytics, AI inference, identity, payment, and submission endpoints are excluded from Alpha 1.

## 6.3 Blockchain Interfaces

Not applicable.

## 6.4 Communication Requirements

Public resources shall load using HTTPS on production hosting. Reflection text shall not be sent to any external endpoint (SRS-FR-018). Degraded connectivity must not cause fabricated successful submission messages; there is no submission operation.

---

# 7. Data Requirements

## 7.1 Data Entities

| Entity | Description | Owner / Authority | Classification |
|---|---|---|---|
| EditorialContent | Public philosophy, articles, and editorial metadata | Product Owner | Public |
| Pillar | Name and description of philosophical pillar | Product Owner | Public |
| ReflectionPrompt | Available optional writing prompts | Product Owner | Public |
| CurrentReflection | Visitor-entered text in current interface | Visitor | Private/local |
| SiteDisclosure | Explanations of actual privacy and usage behavior | Product Owner | Public |

## 7.2 Data Lifecycle

- Public content is authored, reviewed, published, superseded, and removed by project maintainers.
- Reflection text is created and edited locally while the interaction is active and cleared by visitor action or page lifecycle. No retention guarantee is made.
- No server-side reflection history, recovery, synchronization, backup, archival, or deletion requests are required because the product does not collect the text.

## 7.3 Data Integrity

| ID | Requirement | Source | Verification |
|---|---|---|---|
| SRS-DAT-001 | Public pillar names shall be unique within the five-pillar presentation. | FR-006 | Test |
| SRS-DAT-002 | Published content links shall resolve to intended published destinations or an explicit not-found experience. | FR-004, FR-017 | Test |
| SRS-DAT-003 | Reflection text shall not be automatically persisted to a remote store or browser persistent-storage API. | FR-013; Alpha assumption | Test + Inspection |

## 7.4 Privacy and Data Protection

| ID | Requirement | Source | Verification |
|---|---|---|---|
| SRS-DAT-004 | Reflection content shall not be included in network transmissions initiated by the application. | FR-013 | Test |
| SRS-DAT-005 | Privacy disclosure shall accurately describe any cookies, hosting request logs, or externally loaded assets after deployment configuration is known. | FR-016 | Inspection |

## 7.5 On-Chain and Off-Chain Data

Not applicable. All product content is off-chain and public; visitor reflection is local and uncollected.

---

# 8. Quality Requirements

> **Quality baseline:** The Product Owner approved mobile Lighthouse ≥90, WCAG 2.2 AA on critical journeys, English-only, and non-persistence. Architectural numeric budgets beyond these approvals are labeled provisional and must not be represented as Product Owner-approved.

## 8.1 Performance

| ID | Statement | Source | Target / Verification |
|---|---|---|---|
| SRS-PER-001 | The production landing page shall achieve the approved minimum mobile Lighthouse performance score. | NFR-P-001 | **Approved ≥90**, three runs, median; repeatable documented profile; Test |
| SRS-PER-002 | Critical public reading content shall render without requiring successful execution of reflection-specific JavaScript. | NFR-P-002 (derived) | JS disabled reading check; Test |
| SRS-PER-003 | Production assets shall comply with an approved mobile transfer budget. | NFR-P-002 | **Provisional engineering budget: ≤250 KiB initial page transferred (compressed first-load HTML/CSS/JS, excluding imagery/fonts), and ≤500 KiB total initial page assets excluding user-initiated media; verify and adjust by documented architecture review before release**; Analysis |

## 8.2 Availability

| ID | Statement | Source | Target / Verification |
|---|---|---|---|
| SRS-REL-001 | Production public resources shall be hosted under an availability objective agreed with the hosting provider. | NFR-A-001 | **PRD proposed ≥99.5% monthly**, only if contractually measurable; Analysis |

## 8.3 Scalability

No personalized server workload or concurrent-session quota is specified. Hosting capacity and delivery quotas shall be evaluated before production release; no unsupported numerical concurrency guarantee is asserted.

## 8.4 Security

| ID | Statement | Source | Verification |
|---|---|---|---|
| SRS-SEC-001 | All production public page and asset requests shall be served through HTTPS. | NFR-S-001 | Test |
| SRS-SEC-002 | Client-delivered resources shall contain no private credentials, tokens, or secret configuration. | NFR-S-002 | Inspection + automated scan |
| SRS-SEC-003 | The reflection experience shall not send typed text to any remote endpoint. | NFR-S-003 | Network test |
| SRS-SEC-004 | Approved third-party resources, if any, shall be reflected in privacy disclosures and reviewed for unnecessary data sharing. | NFR-S-004 | Inspection |

## 8.5 Reliability and Recovery

No server-side visitor state exists. A browser reload discards active text; the interface must disclose this. Editorial content recovery and version history are operational publishing concerns, to be specified in the SAD/operations documents.

## 8.6 Usability and Accessibility

| ID | Statement | Source | Verification |
|---|---|---|---|
| SRS-UX-001 | Core navigation and reflection flows shall function at widths of **320, 375, 768, and 1280 CSS pixels** without horizontal overflow of primary content. | UX §8 | Test; engineering verification widths |
| SRS-UX-002 | Critical journeys shall meet the **approved WCAG 2.2 AA** acceptance checklist, including labels, focus, contrast, and keyboard operation. | UX §8.2 | Audit + Test |
| SRS-UX-003 | The site shall use English for all Alpha 1 visitor-facing control labels and approved editorial content. | UX §8.2 | Inspection |
| SRS-UX-004 | **RETIRED in v0.2.0:** The mandatory pilot success threshold derived from v0.1 KPI-002 is withdrawn. | Superseded by PRD v0.2 KPI-003 | Not a release gate |
| SRS-UX-005 | Core philosophical copy, visual identity, and visitor calls to action shall be reviewed for fidelity to equality, inner alignment, non-coercion, and reflective rather than instructional posture. | BO-001–003; KPI-002; RISK-001, RISK-005–006 | Product Owner inspection and recorded approval |
| SRS-UX-006 | Core content and optional reflection shall be independently discoverable and navigable on approved mobile and desktop test profiles. No audience-research sample-size or conversion target is required. | KPI-003; PRD §8 | Functional journey tests + accessibility inspection |

## 8.7 Maintainability and Supportability

Published pages and critical interactions shall be verifiable against stable requirement IDs. Detailed module structure and development tooling are SAD and testing-strategy decisions, not SRS requirements.

## 8.8 Compatibility and Interoperability

Core journeys shall be verified against the then-current stable Chrome, Firefox, Safari, and Edge, recording tested versions and platforms at release. Physical-device coverage and browser versions will be documented in the test plan; unsupported exact-version promises are not implied.

---

# 9. Security and Regulatory Requirements

## 9.1 Security Requirements

SRS-SEC-001 through SRS-SEC-004 (§8.4) and SRS-DAT-003 through SRS-DAT-005 (§7) define the security and privacy obligations; references are not duplicated as new normative identifiers.

## 9.2 Regulatory Compliance

| Regulation / Obligation | Applicability | SRS Requirements |
|---|---|---|
| Data privacy / hosting disclosures | Applicable obligations require legal assessment | SRS-FR-023–025; SRS-DAT-005 |
| Intellectual-property permission for published materials | Editorial review required | Editorial release process (to be detailed operationally) |

No legal compliance certification is asserted by this draft. Applicability of Panama and visitor-jurisdiction privacy and intellectual-property obligations requires separate review; no blanket GDPR claim is made.

## 9.3 Auditability

Alpha 1 has no visitor action log or server-side user activity audit. Development/release verification records and approved content change history are operational artifacts, not product collection of visitor reflections.

## 9.4 Web3-Specific Security

Not applicable.

---

# 10. Operational Requirements

## 10.1 Deployment Constraints

The public runtime shall not depend on a product-specific application backend, account service, database, AI service, or blockchain network. Hosting strategy and build/deployment details belong in the SAD.

## 10.2 Configuration Requirements

Site identity, external links, and navigation destinations must be reviewable before release. Actual environment/configuration design is deferred to the SAD.

## 10.3 Monitoring Requirements

No visitor tracking is mandated or required to assess mission success. Anonymous hosting health checks, if later authorized, must not ingest reflection text or contradict the privacy disclosure.

## 10.4 Maintenance Requirements

Editorial corrections and software updates must be releasable without changing visitor accounts or migrating private reflection records, because none exist. Rollback criteria and release runbooks belong in operational design.

---

# 11. Verification and Acceptance

## 11.1 Verification Methods

**Test:** Execute defined scenarios. **Analysis:** Examine measurements/evidence. **Inspection:** Review content, configuration, code, or output. **Demonstration:** Observe representative journeys.

## 11.2 Verification Matrix

| SRS ID / Range | Verification Method | Acceptance Criterion | Verification ID |
|---|---|---|---|
| SRS-FR-001–011 | E2E + editorial inspection | Public journeys, named pillars and philosophy accessible | VER-PUBLIC-001 |
| SRS-FR-012–022 | Component + E2E | Prompt/text/clear behavior works without submission | VER-REF-001 |
| SRS-FR-023–025 | Inspection + network test | Disclosure matches observed behavior | VER-PRIV-001 |
| SRS-INT-001–005; SRS-UX-001–003 | Browser/accessibility tests | Approved compatibility and a11y checks pass | VER-UX-001 |
| SRS-DAT-001–005 | Unit + network tests | Data contracts and non-storage verified | VER-DATA-001 |
| SRS-PER-001–003; SRS-REL-001 | Performance and hosting review | Approved numeric baselines met | VER-OPS-001 |
| SRS-SEC-001–004 | Static inspection + integration tests | No secrets or reflection transmission; HTTPS | VER-SEC-001 |
| SRS-UX-004 | Retired / no active verification | Not a release gate | — |
| SRS-FR-026–027; SRS-UX-005 | Product Owner editorial and interaction audit | Approved wording, artwork and calls to action reflect inner alignment, equality and non-coercion | VER-FIDELITY-001 |
| SRS-UX-006 | Mobile/desktop journey tests and accessibility review | Core philosophical material and optional reflection are independently discoverable | VER-UX-002 |

A task-level verification manifest may split these groups into individual automated test IDs; each mandatory requirement must retain at least one explicit verification mapping.

## 11.3 Acceptance Conditions

All approved High-priority requirements verified; approved quality targets met; no unresolved critical/high defects; privacy/network checks pass; editorial material, calls to action and brand approved by Product Owner for **philosophical fidelity**, not audience appeal; release authorization recorded. **The PRD v0.2 is approved; unresolved PRD open questions and derived SRS targets must be answered, accepted as explicit defaults, or formally deferred before the SRS is baselined.** No traffic, sign-up, retention, conversion, or adoption measure is a release criterion.

---

# 12. Requirements Traceability

## 12.1 PRD-to-SRS Matrix

| PRD ID | SRS ID | Relationship | Status |
|---|---|---|---|
| FR-001 | SRS-FR-001 | Direct | Proposed |
| FR-002 | SRS-FR-002 | Direct | Proposed |
| FR-003 | SRS-FR-003 | Direct | Proposed |
| FR-004 | SRS-FR-004–005; SRS-INT-004 | Direct / Derived | Proposed |
| FR-005 | SRS-FR-006 | Direct | Proposed |
| FR-006 | SRS-FR-007; SRS-DAT-001 | Direct / Derived | Proposed |
| FR-007 | SRS-FR-008 | Direct | Proposed |
| FR-008 | SRS-FR-010 | Direct | Proposed |
| FR-009 | SRS-FR-012 | Direct | Proposed |
| FR-010 | SRS-FR-013–014 | Direct | Proposed |
| FR-011 | SRS-FR-015–016 | Direct | Proposed |
| FR-012 | SRS-FR-017 | Direct | Proposed |
| FR-013 | SRS-FR-018–019; SRS-FR-024; SRS-DAT-003–004 | Direct / Derived | Proposed |
| FR-014 | SRS-FR-020–022 | Direct | Proposed |
| FR-015 | SRS-FR-011 | Direct | Proposed |
| FR-016 | SRS-FR-023–025; SRS-DAT-005 | Direct / Derived | Proposed |
| FR-017 | SRS-FR-009; SRS-DAT-002 | Direct / Derived | Proposed |
| NFR-P-001–002 | SRS-PER-001–003 | Direct / Derived | Approved / engineering budget provisional |
| NFR-A-001 | SRS-REL-001 | Direct | Proposed |
| NFR-S-001–004 | SRS-SEC-001–004 | Direct | Proposed |
| PRD §8 | SRS-INT-001–003,005; SRS-UX-001–003, SRS-UX-005–006; SRS-FR-027 | Direct / Derived | Approved |
| PRD §§2.1–2.2; BO-003 | SRS-FR-026; SRS-UX-005 | Derived: philosophical fidelity | Approved |
| KPI-002 | SRS-UX-005 | Direct: Product Owner editorial acceptance | Approved requirement; content pending |
| KPI-003 | SRS-UX-001–003, SRS-UX-006 | Direct: usability/accessibility without adoption testing | Approved |

## 12.2 SRS-to-Verification Matrix

Mapped by requirement family in §11.2. Before approval, a machine-readable verification register shall enumerate each SRS identifier individually.

## 12.3 Derived Requirements

| SRS ID | Derivation Rationale | Source / Constraint | Approval |
|---|---|---|---|
| SRS-FR-005 | Orientation makes navigation usable | FR-004 | Accepted derivation |
| SRS-INT-004 | Missing routes need explicit response | FR-004 | Accepted derivation |
| SRS-DAT-001–002 | Structural correctness of public content | FR-006, FR-017 | Accepted derivation |
| SRS-PER-002 | Static readable content supports low bandwidth/robustness | NFR-P-002 | Accepted derivation |
| SRS-UX-001 | Establish repeatable responsive test widths | PRD §8 | Accepted derivation |
| SRS-FR-026 | Translate inner alignment and deeper-order concept into reviewable core copy | PRD §§2.1, 3.1 | Accepted derivation |
| SRS-FR-027 | Make non-coercive interaction posture enforceable | PRD §§2.2, 8.1 | Accepted derivation |
| SRS-UX-005 | Replace old audience-pilot threshold with Product Owner fidelity approval | PRD KPI-002; BO-003 | Accepted derivation |
| SRS-UX-006 | Verify independent navigation without audience validation KPI | PRD KPI-003 | Accepted derivation |

## 12.4 Coverage Review

Every PRD FR-001–017 is mapped in §12.1. Outstanding implementation/release evidence: editorial content inventory, actual dragon/inner-flame artwork approval, tested browser-version matrix, hosting-specific privacy language, and individual test traceability. Product Owner confirmed curated navigation without search, English-only, transient reflection, Lighthouse target, accessibility target and visual direction. PRD v0.2 no longer requires market validation or a moderated pilot. No unapproved feature is authorized by the mapping.

---

# 13. Risks, Assumptions, and Open Issues

## 13.1 Technical Risks

| Risk ID | Description | Impact | Mitigation |
|---|---|---|---|
| TR-001 | Client code/third-party script leaks reflection text | High | Explicit network and storage audit |
| TR-002 | Visual effects impair mobile performance/accessibility | Medium | Representative mobile testing and reduced motion |
| TR-003 | Static routing behaves differently in deployment | Medium | Test deep links on deployed preview |
| TR-004 | Ambiguous privacy claims conflict with host logs | High | Verify deployed dependencies and disclosures |

## 13.2 Assumptions Requiring Validation

| ID | Assumption | Owner | Status |
|---|---|---|---|
| AV-001 | English-only public content | Product Owner | Confirmed 2026-10-25 |
| AV-002 | Reflection state exists only within the active browser interaction; refresh/navigation discards it | Product Owner | Confirmed 2026-10-25 |
| AV-003 | One substantive editorial piece minimum | Product Owner | Confirmed in approved PRD |
| AV-004 | Product Owner approves final editorial material and final dragon artwork | Product Owner | Release approval pending actual materials |

## 13.3 Decisions and Open Issues

**Resolved product decisions (2026-10-25):** English only; no reflection persistence; mobile Lighthouse ≥90; WCAG 2.2 AA on critical journeys; editorial approval by Product Owner; uncoiled dragon/open wings/inner flame visual direction; curated links/no search.

**Remaining implementation questions (not blockers to the SRS baseline):** final content/artwork; exact host and truthful hosting/resource disclosure; actual browser test versions; whether freeform reflection is desired in a later scope change. The proposed 99.5% hosting objective and the provisional asset budget require verification against an actual deployment, not an implied hosting guarantee. Any different behavior requires change control.

## 13.4 Unresolved Requirements

No unresolved Product Owner decision blocks the approved Alpha 1 functional baseline. Editorial approvals, hosting-specific disclosures, detailed quality-budget validation, and verification evidence remain mandatory before release.

---

# 14. Document Control

## 14.1 Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-10-13 | Product Architecture Working Draft | Initial SRS proposed from draft PRD |
| 0.2.0 | 2026-10-21 | Lead Software Architect (AI-assisted) | Align with approved PRD v0.2; retire pilot acceptance; add fidelity checks |
| 0.2.1 | 2026-10-25 | Lead Software Architect (AI-assisted) | Incorporate seven approved decisions; establish requirements baseline; distinguish open release evidence from product decisions |

## 14.2 Review and Approval

| Role | Name | Approval | Date |
|---|---|---|---|
| Product Owner | Roberto Cerrud | Accepted derivation | — |
| Technical Lead | Lead Software Architect | Accepted derivation | — |
| QA Lead | To be assigned | Accepted derivation | — |
| Security / Compliance | To be assigned as needed | Accepted derivation | — |

## 14.3 Change Control

An approved change must identify rationale, source PRD IDs, affected SRS IDs, acceptance criteria, verification coverage, and release impact.

## 14.4 Baseline Reference

**Approved PRD Version:** PRD-ADS-001 v0.2 (approved 2026-10-21)  
**SRS Baseline Version:** 0.2.1  
**Baseline Date:** 2026-10-25  
**Approval Status:** Approved for architecture planning; release evidence and actual editorial materials outstanding

---

# Appendix A — Requirement Quality Checklist

Approve only requirements that are necessary, clear, singular, feasible, verifiable, traceable, internally consistent, bounded, and free of unnecessary implementation details.

# Appendix B — Requirement Identification

| Prefix | Category |
|---|---|
| SRS-FR | Functional |
| SRS-PER | Performance |
| SRS-SEC | Security |
| SRS-DAT | Data |
| SRS-INT | Interfaces |
| SRS-REL | Reliability / availability |
| SRS-UX | Usability / accessibility |

Identifiers shall remain stable across revisions. SRS-OPS, SRS-W3 and SRS-AI may be introduced in later versions when applicable.

# Appendix C — Source References

- PRD-ADS-001 v0.2 (approved 2026-10-21); supersedes v0.1 for this SRS.
- Project philosophy and scope decisions recorded in Ars Draconis Soluti discussions, October 2026.
- Supplied generic SRS template, v0.1.0.

---

**End of Software Requirements Specification**
