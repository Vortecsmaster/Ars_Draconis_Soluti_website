# Product Requirements Document (PRD)

**Product:** Ars Draconis Soluti — **The Art of the Unleashed Dragon** 
**Document ID:** PRD-ADS-001 
**Document Version:** 0.2.2 
**Date:** 2026-10-16 
**Author:** Product Architecture Working Draft 
**Product Owner:** Roberto Cerrud 
**Status:** Approved

---

# 1. Purpose

## 1.1 Objective

This document defines product-level requirements for **Ars Draconis Soluti**, an independent digital expression of a philosophical vision and a space for voluntary contemplation. It defines the project's intention, intended visitor experience, Alpha 1 scope, functional and non-functional requirements, quality criteria, risks, and acceptance conditions.

The purpose of the product is **to express the philosophy faithfully and make it freely accessible**, whether or not it attracts an audience. Audience size, adoption, traction, conversion, and market validation are not measures of the project's worth or grounds for changing its principles.

This document does **not** prescribe a framework, repository structure, data schema, architecture, or implementation details. Those belong in the SRS and SAD.

---

# 2. Product Overview

## 2.1 Product Summary

Ars Draconis Soluti is a mobile-first public website giving form to a philosophy of conscious freedom, inner alignment, and disciplined expression. It presents the conceptual progression LOGOS → LEGGOS → DRAGON and five pillars (Will, Wisdom, Honor, Freedom, Confidence) through essays, symbolism, and optional self-guided reflection. Here, freedom arises through living in alignment with one's true self and the deeper order of existence, rather than being granted by an external authority or defined solely as resistance to constraints. The project offers an invitation to contemplation among equals, not teaching, initiation, recruitment, diagnosis, or guidance from a superior position. Alpha 1 is publicly accessible without accounts or identification.

## 2.2 Problem Statement

Many philosophy, self-development, and spiritual websites adopt teacher/follower relationships or direct visitors into communities, funnels, and personal-data collection. Ars Draconis Soluti deliberately offers a different form: clear philosophical expression and optional contemplation, without implying authority over the visitor.

**This project is not a market hypothesis to validate.** Its reason for existing is to express a philosophical vision authentically and make it available to whomever encounters it. It does not depend on demand, adoption, present or future traction, or external approval.

Whether the ideas resonate widely, with a few people, or with no one does not establish their value. The guiding commitment is to remain aligned with the philosophy, express it with integrity, and trust the process of its unfolding without attachment to an outcome.

The design challenge is therefore **faithful expression without imposing a path**, while maintaining clarity, accessibility, and visitor autonomy.

## 2.3 Target Users

### Primary Visitor Perspective — Independent Explorer

- **Description:** A visitor curious about alignment with their true self, discipline, meaning, freedom, and reflection.
- **Pain points:** Prescriptive advice; claims of spiritual authority; confusing navigation; forced registration; opaque data collection.
- **Goals:** Explore ideas freely; find resonant language; reflect without pressure or external judgment.

### Secondary Visitor Perspective — Returning Reader

- **Description:** A visitor who revisits particular philosophical essays or prompts.
- **Goals:** Quickly reach relevant ideas; navigate consistently on a mobile device; optionally revisit their own reflection **without assuming the service saves it**.

### Internal / Administrative Users

- **Content owner/editor:** Authors and revises public philosophical material outside the visitor-facing experience.
- **Site maintainer:** Verifies publishing quality and operational availability. No public administrative account or dashboard is required for Alpha 1.

---

# 3. Business Context

## 3.1 Business Objectives

The objectives below are **mission and stewardship objectives**, not growth or commercial objectives. Identifiers remain stable for traceability.

- **BO-001 — Give the philosophy a coherent public form:** Establish a recognizable Ars Draconis Soluti identity on its chosen public domain, consistent across writing, symbols, and experience.
- **BO-002 — Express without hierarchy:** Publish clear, thoughtful material that offers reflection among equals, without required fees, registration, pressure, or claims of authority.
- **BO-003 — Preserve philosophical integrity:** Ensure that language, symbolism, and interactions reflect inner alignment, conscious freedom, and personal discovery; do not revise doctrine to maximize engagement or external approval.
- **BO-004 — Sustain the expression without compromising it:** Preserve the option to add content, languages, opt-in functions, AI-assisted tools, or voluntary support only when those additions genuinely serve the philosophy and remain optional. Neither expansion nor monetization is a success requirement.

## 3.2 Revenue Model (If Applicable)

**Alpha 1:** No required payment, subscription, product purchase, token, donation, or commercial relationship. Potential later models (e.g., voluntary support, publications, merchandise) require separate product approval and must preserve the site's ethos. **No monetization mechanism is in scope for Alpha 1.**

## 3.3 Success Metrics (KPIs)

**Success means faithful expression and responsible execution, not popularity.** These are release quality and mission-alignment checks rather than audience KPIs. Their thresholds are proposed where specified.

- **KPI-001 — Release completeness:** 100% of approved High-priority Alpha 1 requirements verified before release.
- **KPI-002 — Philosophical fidelity:** Product Owner reviews and approves core texts, imagery, and calls to action for consistency with the founding principles, especially equality, inner alignment, and non-coercion.
- **KPI-003 — Usability and accessibility:** Visitors can independently discover core material and optional reflection on supported mobile and desktop layouts; verify through functional and accessibility checks. Optional usability testing may identify clarity problems, **not validate the philosophy**.
- **KPI-004 — Privacy integrity:** Zero required visitor accounts, remote reflection submissions, or undisclosed persistent storage in Alpha 1.

**Explicit non-metrics:** Traffic, sign-ups, retention, conversion, social reach, audience growth, and revenue are not release success criteria or reasons to alter the philosophical message. Anonymous operational signals, if ever approved, may assist maintenance and usability but must not turn engagement into the project's objective.

---

# 4. Scope Definition

## 4.1 In Scope (Alpha 1)

- Public landing page expressing the project's philosophy, symbolic language, and central invitation.
- Navigable public sections covering the philosophy, LOGOS → LEGGOS → DRAGON, and the five pillars.
- Public written content including essays or equivalent editorial pieces and coherent navigation between them.
- Optional, self-guided reflection interface with predefined prompts and a visitor-controlled text entry area.
- Explicit explanation that reflection is **not** analyzed by an AI, evaluated by a teacher, submitted to another person, or saved to an account.
- Mobile-first, responsive presentation with usable desktop layouts.
- Clear site identity and appropriate informational/privacy disclosures.
- Visitor access without registration, login, payment, or identity verification.

## 4.2 Out of Scope

- Registration, authentication, social sign-in, membership, user profiles, or personal dashboards.
- Servers, databases, user-submitted content services, synchronization, or cloud persistence of reflections.
- Conversational AI, personalized AI guidance, model inference, or external AI APIs.
- Payment flows, e-commerce, donations, subscriptions, or advertising features.
- Public forums, social feeds, user messaging, moderation consoles, or community accounts.
- Blockchain, wallets, tokens, NFTs, or smart contracts.
- Native iOS or Android applications.
- Automatic translation or multilingual publishing for Alpha 1 (future option; see open questions).
- Treating the experience as therapy, diagnosis, professional advice, or spiritual instruction.

---

# 5. Functional Requirements

Requirements are product-level and use stable identifiers. Detailed preconditions, failures, and verification procedures belong in the SRS.

## 5.1 Public Experience and Identity

### FR-001 — Public access

**Statement:** The product shall allow visitors to access the public experience without account creation, login, or payment. 
**Priority:** High 
**Rationale:** Autonomy and open access are central to the product.

### FR-002 — Philosophical positioning

**Statement:** The product shall clearly communicate that Ars Draconis Soluti offers reflection rather than teaching, authority, or recruitment. 
**Priority:** High 
**Rationale:** Establishes the relationship of equals.

### FR-003 — Identity and invitation

**Statement:** The landing experience shall convey the project's name, **The Art of the Unleashed Dragon**, a recognizable dragon/flame identity, and an invitation to explore one's own path. 
**Priority:** High 
**Rationale:** Defines the site's public identity.

### FR-004 — Coherent navigation

**Statement:** The product shall enable visitors to reach core philosophy, pillars, reflections, and informational pages through predictable navigation. 
**Priority:** High 
**Rationale:** Supports self-directed exploration.

## 5.2 Philosophical Content

### FR-005 — Foundational synthesis

**Statement:** The product shall publish an understandable treatment of LOGOS → LEGGOS → DRAGON, with distinctions between principle, embodiment, and awakened expression. 
**Priority:** High 
**Rationale:** Establishes the conceptual structure.

### FR-006 — Five pillars

**Statement:** The product shall present the five pillars—Will, Wisdom, Honor, Freedom, and Confidence—with a meaningful description for each. 
**Priority:** High 
**Rationale:** Gives visitors distinct lenses for contemplation.

### FR-007 — Public editorial content

**Statement:** The product shall make at least one substantive public editorial piece discoverable and readable from the main navigation or philosophy area. 
**Priority:** High 
**Rationale:** The experience must offer more than a visual landing page.

### FR-008 — Content attribution and distinction

**Statement:** The product shall distinguish philosophical statements and interpretations from factual or professional advice when ambiguity could mislead visitors. 
**Priority:** Medium 
**Rationale:** Supports transparency without diluting the philosophy.

## 5.3 Self-Guided Reflection

### FR-009 — Reflection entry

**Statement:** The product shall offer visitors a voluntary reflection experience that can be started without an account. 
**Priority:** High 
**Rationale:** Turns contemplation into an optional personal practice.

### FR-010 — Prompt selection

**Statement:** The reflection experience shall offer at least three distinct starting prompts and allow a visitor to choose one. 
**Priority:** High 
**Rationale:** Supports visitors who do not know where to begin.

### FR-011 — Personal expression

**Statement:** The reflection experience shall provide a space where visitors can type their own thoughts and revise them during the current interaction. 
**Priority:** High 
**Rationale:** Visitor expression must remain under visitor control.

### FR-012 — No simulated intelligence

**Statement:** The product shall not imply that reflection text is interpreted, answered, judged, or processed by an intelligent assistant when no such service exists. 
**Priority:** High 
**Rationale:** Prevents deceptive expectations.

### FR-013 — Reflection data choice

**Statement:** The product shall clearly state what happens to entered reflection text and shall not transmit it to Ars Draconis Soluti or any third-party service in Alpha 1. 
**Priority:** High 
**Rationale:** Privacy and trust are product principles.

### FR-014 — Clear/restart reflection

**Statement:** The product shall allow a visitor to clear the current text and start another reflection, with an explicit confirmation before discarding entered text. 
**Priority:** Medium 
**Rationale:** Protects against accidental loss.

## 5.4 Communication and Informational Pages

### FR-015 — About and principles

**Statement:** The product shall offer a discoverable explanation of the project, its guiding principles, and its non-hierarchical posture. 
**Priority:** High 
**Rationale:** Clarifies intentions and boundaries.

### FR-016 — Privacy disclosure

**Statement:** The product shall provide a plainly written explanation of any data collection, processing, storage, and external resources relevant to visitors. 
**Priority:** High 
**Rationale:** Enables informed participation.

### FR-017 — Stable content sharing

**Statement:** Public essays and principal conceptual sections shall have navigable, shareable locations. 
**Priority:** Medium 
**Rationale:** Allows a reader to return to or share an idea freely; discovery volume is not a success criterion.

## 5.5 Web3-Specific Requirements

**Not applicable to Alpha 1.** No wallet connection or blockchain operations.

## 5.6 AI-Enabled Features

**Not applicable to Alpha 1.** AI-assisted reflection may be considered in future only if it supports self-directed inquiry without assuming the role of teacher, authority, or arbiter of a visitor’s inner life.

---

# 6. Non-Functional Requirements

## 6.1 Performance

- **NFR-P-001:** The public landing page should achieve a **proposed** mobile Lighthouse performance score of at least 90 under the agreed repeatable test profile. **Priority:** Medium; target pending approval.
- **NFR-P-002:** Core content shall remain usable on an average mobile connection without requiring large interactive downloads for reading. **Priority:** High; measurable page-budget target to be finalized in the SRS.

## 6.2 Availability

- **NFR-A-001:** Public pages shall remain available through the selected hosting service with a **proposed** monthly availability objective of 99.5%, subject to the hosting provider's service characteristics. **Priority:** Medium.

## 6.3 Security

- **NFR-S-001:** Public access shall use HTTPS. **Priority:** High.
- **NFR-S-002:** The product shall not expose deployment credentials, private keys, or secret configuration in publicly delivered resources. **Priority:** High.
- **NFR-S-003:** No reflection content shall be submitted to a remote processing or storage endpoint in Alpha 1. **Priority:** High.
- **NFR-S-004:** External links and third-party resources shall not silently undermine the privacy disclosure. **Priority:** High.

## 6.4 Compliance (If Applicable)

- Publish accurate disclosures appropriate to actual data handling, cookies, fonts, third-party resources, and hosting.
- Review privacy and intellectual-property obligations relevant to publication from Panama and visitors' applicable jurisdictions before release.
- Do not assert GDPR applicability, exemption, or legal compliance without a separate determination.

---

# 7. External Interfaces

## 7.1 Third-Party Integrations

No feature-level integration with payments, social identity, AI providers, blockchain, or CRM is needed in Alpha 1. Infrastructure-hosting and any approved external assets are operational dependencies rather than application features.

## 7.2 Supported Platforms

- Responsive web: phones, tablets, and desktops.
- Current stable versions of major browsers: Chrome, Firefox, Safari, and Edge; exact support policy to be defined in the SRS.
- No native mobile application in Alpha 1.

---

# 8. User Experience Requirements

## 8.1 Design Principles

The product shall:

- Prioritize mobile experience without diminishing desktop readability.
- Maintain a contemplative, confident tone without coercion, claims of authority, or appeals engineered to secure agreement.
- Use legible typography, strong contrast, clear hierarchy, and disciplined animation.
- Preserve accessible navigation and visible feedback on interactive actions.
- Avoid manipulative engagement mechanics, conversion funnels, popularity cues used as validation, and registration gates.
- Treat visitors as equals: **No masters. No followers. Fellow dragons.**

## 8.2 Accessibility

- Keyboard-accessible core navigation and reflection interactions.
- Clear labels and screen-reader semantics for interactive controls.
- Reduced-motion accommodation for decorative animation.
- Target: WCAG 2.2 AA for critical user journeys;
- Initial editorial language: **English**. Future localization remains out of scope for Alpha 1.

---

# 9. Data Requirements

## 9.1 Data Handling

- **Public content:** Project-controlled text, imagery, and navigation metadata.
- **Visitor reflection text:** Entered and manipulated locally for the current interaction; no requirement for persistent retention.
- **Accounts and user profiles:** None.
- **Analytics:** None required. Any future analytics collection requires explicit scope and privacy review.
- **Hosting records:** Web hosts may independently process ordinary request metadata; disclose confirmed practices rather than promising none exist.

## 9.2 Data Privacy

The product shall:

- Explain clearly that the Alpha 1 reflection feature is local to the visitor's browsing interaction.
- Not represent browser content as confidential against people or extensions with access to the visitor's device.
- Not require identification to access content or reflect.
- Make privacy statements consistent with implemented behavior and any third-party hosting/resource processing.

---

# 10. Risks & Assumptions

## 10.1 Product Risks

| Risk ID | Risk | Mitigation |
|---|---|---|
| RISK-001 | Visitors perceive a teacher/follower hierarchy | Review every key message against the equality principle |
| RISK-002 | Reflection UI is mistaken for an AI chatbot or therapy | Explicitly label interaction and boundaries |
| RISK-003 | Heavy visuals reduce mobile performance | Apply a mobile performance budget |
| RISK-004 | Ambiguous saving behavior causes privacy confusion or data loss | State non-persistence; confirm before clearing |
| RISK-005 | Growth, feedback, or monetization pressures displace the philosophical intention | Evaluate proposed changes against mission fidelity; require Product Owner approval for material shifts |
| RISK-006 | Symbolic imagery suggests domination, external control, or hierarchy rather than awakening and inner alignment | Define identity acceptance criteria and review artwork |

## 10.2 Assumptions

- The Alpha 1 product is a public website, not a private community.
- The visitor-facing editorial language is English initially.
- Visitors need a modern browser to use the interactive reflection feature.
- Reflection is primarily prompted writing; no AI response is promised.
- The Product Owner will supply or approve final editorial text and visual identity.

---

# 11. Acceptance Criteria

Alpha 1 is eligible for Product Owner acceptance when:

1. Every approved High-priority functional requirement has passing verification evidence.
2. The landing page, core philosophy, all five pillars, and at least one editorial piece are publicly navigable.
3. Reflection can be initiated, typed into, and safely cleared without a login or remote text submission.
4. The reflection interaction does not imitate or imply unavailable AI capabilities.
5. Mobile, keyboard, privacy, and security checks meet the approved thresholds.
6. No out-of-scope account, backend, payment, AI, or blockchain feature is introduced.
7. Final philosophical language and brand presentation are approved by the Product Owner for alignment with the founding vision, not for market appeal.

---

# 12. Open Questions

| ID | Question | Proposed Default | Owner |
|---|---|---|---|
| OQ-001 | Is the visitor-facing editorial language English only for Alpha 1? | Yes | Product Owner |
| OQ-002 | Should reflection text disappear on refresh/navigation, or should opt-in local persistence be added? | Disappear; no persistent saving | Product Owner |
| OQ-003 | What exact initial editorial titles and text are approved? | Approve before release | Product Owner |
| OQ-004 | Which dragon symbol/visual identity is the release baseline? | Uncoiled dragon, open wings, inner flame; artwork pending | Product Owner |
| OQ-005 | Should any voluntary contact method be exposed publicly? | No interactive contact collection in Alpha 1 | Product Owner |
| OQ-006 | Are proposed Lighthouse/WCAG/accessibility targets accepted? | Pending; quality tests are not audience validation | Product Owner |
| OQ-007 | Does the scope include an editorial index/search, or only navigation and curated links? | Curated links; no search | Product Owner |

---

# 13. Document Control

## 13.1 Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-13 | Product Architecture Working Draft | Initial product requirements for review |
| 0.2 | 2026-10-16 | Product Architecture Working Draft | Reoriented objectives and success criteria around philosophical expression rather than traction; replaced former autonomy terminology with inner alignment; preserved Alpha 1 scope and requirement IDs |

## 13.2 Review and Approval

| Role | Reviewer | Status | Date |
|---|---|---|---|
| Product Owner | Roberto Cerrud | Approved | 2026-10-21 |
| Lead Software Architect | AI-assisted architecture role | Draft prepared | 2026-10-13 |

## 13.3 Change Control

After approval, changes shall identify impacted FR/NFR identifiers and trigger downstream SRS, architecture, test, and task impact assessment. Requirement IDs remain stable across revisions.