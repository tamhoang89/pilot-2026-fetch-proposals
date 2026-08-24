# Verifiable provenance & authorship via on-chain attestations

> Supply-chain traceability applied to the research lifecycle addressing the reproducibility crisis in Science and Journalism.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 95
- **Proposer:** `stake1uxnuuh3h9ppxh9ru9zqs044fendnahp84afcrwelpsfxalqjv9mhr`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-24T11:58:00.472000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

We are the team who developed [PubWeave](https://www.pubweave.com/), a Cardano mainnet dApp with a smart contract-enabled peer-review module.

Intellart and Thespian have handled smart contracts and full stack, interchangeably.

Puzzlewood will now manage marketing and communication (the missing piece).

Albert Feghaly (Intellart) — <https://www.linkedin.com/in/albert-feghaly-28060a113/>

- Intellart Project lead

- 4 years as a Cardano blockchain developer

- 12 years as a bioinformatician

- Design architect and developer of PubWeave's treasury Plutus smart contracts

Rebecca Johnston (Puzzlewood) — <https://www.linkedin.com/in/puzzlewood/>

- Principal at Puzzlewood Communication Inc. since 2008
- Specializes in science and technology communication
- Co-author of PubWeave's positioning narrative

Megan Helmer (Puzzlewood) — <https://www.linkedin.com/in/meganhelmer/>

- Partner at Puzzlewood Communication Inc. since 2021
- MA in Professional Communication
- Co-author of PubWeave's positioning narrative

Thespian d.o.o. — <https://www.linkedin.com/company/thespian-eu/>

- Full-cycle software development: product dev, modernization, staff augmentation, consulting
- Tech stack: JavaScript, React.js, Ruby on Rails, Node.js, Elixir, Haskell, Cardano smart contracts
- Intellart's partner since 2022
- Specifically, Dominik Sipic (<https://www.linkedin.com/in/dominiksipic/>) is a senior software engineer at Thespian and the main backend dev on the PubWeave build

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**N/A**

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

PubWeave supports blog\[s\] → preprint → final (optional stages); bloggers, journalists, academics all fit.

Timestamping recurs throughout creation for:

- founders: notes/drafts/pitch decks
- researchers: datasets/analyses/revisions

creating multiple txs/user/week, not just at publication.

Our success metric is sustained use: users with an existing need for provenance generate recurring transactions as they develop, revise, and finalize content.

The advantages:

- Provable authorship (priority disputes, patent claims)
- Verifiable peer review trail
- Reputation anchored in KERI, traveling with the writer

This provides a credible path to reach 750 transactions in three months while generating feedback to support broader adoption.

Assuming a paper generates &gt;50 attestations; 2 per year, &gt;100/y. Journalists and bloggers have a more dynamic writing style; let's estimate 200/y. On average 3 CIP-0170 attestations per week.

First 14 days: onboarding \~5 new writers each week @ 3/week coming back regularly. Weeks 1 and 2 would see 12 and 24 attestations, with a total of 36.

Ramping to 30 researchers and 30 writers over a 12-week window would produce \~936 attestations.

### How will you reach and onboard real users - and what evidence backs your channels?

Adoption channels:

1. Day 1: Albert Feghaly's biotech consulting network. 2-3 actionable networks to target.
2. Week 1: Blockchain/innovation communities. Targets wallet-holding founders, analysts, writers whose workflows naturally generate timestampable events.
3. Weeks 1-2: Puzzlewood conversion machine. Messaging workshop, landing page conversion design, 2-min explainer video, content blitz (2–3 articles), early-adopter webinar, real-life event attendance. Drives funnel: visit → sign up → bind ORCID → first attestation.
4. Weeks 2-4:  Targeted LinkedIn campaigns outreach to biotech/research connections and beyond.
5. Month 2 and beyond: Iterate on feedback.

Funnel: identify communities → recruit cohort → onboard → feedback loop → expand via referrals.

Timeline: Blockchain-native users (wallets, low friction) convert first; Albert's network provides trust anchor; Puzzlewood optimizes conversion; academic onboarding deferred to weeks 3–4 as lower-priority/high-upside channel.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Web 3 competitors**

- ResearchHub: token-incentivized publishing
- Molecule: research IP tokenization
- Open Science Chain: research provenance prototype on Hyperledger Fabric
- DeSci Labs: open-access publishing infra

None ship full lifecycle provenance as a product (and none are Cardano-native, not that it matters much to users).

ResearchHub and Molecule solve a related but separate problem: incentivizing research.

OSC is a data-integrity API for institutional research platforms. It doesn't touch authorship, publishing, or identity, and it's permissioned.

DeSci Labs is open-access publishing infrastructure. Our scope is more focused: a provenance-as-a-service layer where the researcher owns the proof, applicable to any domain (although Science is our primary target).

### Please provide details about the Technology Readiness Level selected for your existing product

PubWeave is a publishing platform on Cardano mainnet.

**Evidence:**

- **Live platform:** <https://www.pubweave.com/> — operational since 2023

- **Treasury smart contracts (OpShin/Python):** <https://github.com/Intellart/pandao-treasury-sc> — peer-review escrow, moderation, bounty mechanism, live on mainnet since 2025

- **Close-out report:** <https://www.pubweave.com/blog/pubweave-close-out-report-catalyst-fund-9>

- **Demo video:** <https://youtu.be/Ecga56irC38>

Notes

1. Intellart's YouTube channel is not promotional, it only contains close-out videos.
2. PubWeave is pending a marketing campaign for user acquisition.
3. TRL 7 was chosen based on technical maturity, not user count.
4. The close-out report contains validator addresses and txs up to the official mainnet address.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Layer 1: Content addressing & timestamping**

Users timestamp a digital piece with a cryptographic hash anchored onchain via the CIP-0170 ATTEST transaction. The record binds what, when, and who, enabling verification without exposure.

**Layer 2: Article lifecycle**

*We will use zenGate Global's open source Winter Protocol supply chain traceability toolset to port PubWeave's article-lineage state machine.*

Winter's `object_event` maps 1:1 to article lineage (blog\[s\] → preprint → final) with stateful datum transitions. We will fork and adapt the `object_event` spend validator and `singleton` minting policy. Forking vs. dependency: the datum schema requires research-specific extensions for version chaining, role-based authority for signers, and linking reviews to articles.

**Layer 3: Identity & attestation** (CIP-0170-based)

Portable, cryptographically verifiable identity anchored in KERI:

- AUTH_BEGIN: publish the author's credential chain, establishing signer authority
- ATTEST: anchor a content digest into the author's Key Event Log (KEL) at a specific time
- AUTH_END: revoke authority

Each Layer 2 article (singleton) is the Layer 3 attestation subject. Every object_event transition emits an ATTEST to the author's KEL. Layer 1's hashes are the data_reference in Layer 2's datum and the digest in Layer 3's ATTEST. The author's attestations travel with their KERI identifier, verifiable by any third party via the open-source SDK/API, and are not locked to PubWeave.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

**Target market**. Global R&D to GDP ratio was 1.92% at &gt;$2T (UNESCO Institute for Statistics, 2023). More than 8M active researchers publish &gt;3M articles a year in &gt;42,500 peer-reviewed journals (The STM Report, 2018). In addition to authors, funders, journal editors, and ethics boards must also verify claims. Capturing only 0.01% of this market translates to: 3M papers/year × 0.0001 × 50 claims over the lifetime of a paper = 15K events/year.

**The reproducibility crisis**. &gt;70% of researchers failed to reproduce others work and &gt;50% failed to reproduce their own (Baker, Nature, 2016); &gt;50% of preclinical research is irreproducible resulting in $28B/year wasted in the US alone (Freedman et al., PLOS Biology, 2015); &gt;10,000 research papers were retracted in 2023 (Van Noorden, Nature, 2023).

**Product-market fit**. Researchers already adopt identity and provenance infrastructure at scale:

- ORCID reached 15M registrations

- Horizon Europe mandates FAIR data plans

- NIH 2023 Data Management & Sharing Policy requires documented data plans

- MIT uses blockchain to issue Digital Diplomas proving institutional trust in on-chain credentials.

**Media**. Gallup reported in 2022 a catastrophic 34% trust in media.

**The AI problem**. AI-generated fake research factories are proliferating: \~10% of cancer papers show signs of paper-mill fabrication (Scancar et al., BMJ, 2026).

**The demand for timestamped, author-anchored provenance is undeniably growing.**

### Applicant name

Neurocan Inc. (DBA: Intellart)

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

At a very conservative 15K attestations/year (because bloggers, writers, journalists, etc. were not counted), a 1 ADA platform service fee generates \~15K ADA/year, covering baseline maintenance (no server fees yet, and maintainer is the project lead working on his own time). The Pilot's fee target reflects Cardano *network* fees (distinct from platform revenue).

At scale we drop the per-attestation fee. Open-source tools drive adoption while revenue comes from institutions: publishers and (bio-)tech startups needing verification, audit trails, and compliance dashboards. They would pay for enterprise features and support. This is a popular business model around open source tooling adopted by the likes of Red Hat, Seqera, GitLab and Grafana. We estimate around a year before popularity starts attracting enterprise players.

Funders like Horizon Europe and NIH already mandate FAIR data and data management plan. Trustless provenance compliance is the logical next step.

### On-chain identity (CIP-0170) - expected transaction count

750

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The plugin module (CIP-0170 client library and verification SDK) is designed but there is no mainnet path without this funding. PubWeave will host the first integration.

**Part 1 -- Build**. Intellart: 50k ADA

- Smart contracts, CIP-0170 client, verification SDK, architecture, PubWeave integration, mainnet launch, testing, dashboard

**Part 2 -- Adoption.**

A. Puzzlewood: 25k ADA

- Messaging, explainer video, content blitz, funnel, user acquisition

B. Thespian and Intellart: 25k ADA

- Frontend, backend, funnel wiring, analytics instrumentation

**Part 3 -- Kicker**. Sustaining fuel: 25k ADA

- Outreach, social, maintenance, bug fixes, contract updates, feedback loops

*Note: Intellart will fund adoption out-of-pocket and absorb losses if target is not met or CIP-0170  is not ready.*

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. CIP-0170 client library: DID creation, ATTEST transaction construction, key management.
2. Verification SDK: validates attestation chains, checks KEL sequence numbers, label-scoped metadata indexing; exposed via an API under api.pubweave.com.
3. Forked & extended Winter validators: singleton + object_event with research-specific datum. Specifically:
   - role-based authority (author/reviewer/editor)
   - version chaining
   - review to article relational links
4. ORCiD to wallet binding: onchain with cryptographic proof of ownership (PubWeave already does this offchain).
5. Self-anchored attestation flow: users create ATTEST transactions anchoring authorship/provenance to their KEL.
6. PubWeave integration: researchers author articles with onchain provenance and verify attestations.
7. Test evidence: preprod results, test coverage report, security review notes.
8. Real-time metrics dashboard: live transaction feed, attestation counts, fee totals, external wallet counter.

### How far along is the integration you're proposing, today?

TRL 1 - Basic principles observed

### On-chain identity (CIP-0170) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

All communication carries some authority with it, regardless of proof. Humans have a tendency to delegate authority to respected bodies because (1) not everyone has expertise in everything and (2) time is limited. In academia, journalism and other fields, we tend to trust highly respected journals and news agencies because of their heightened due-diligence. This process, however, is far from infallible, causing the all-too-familiar reproducibility crisis in science, unreliable journalism, and intellectual property (IP) disputes in research and tech.

We propose a verifiable provenance and authorship layer for research outputs via a supply-chain attestation system that anchors who created what, and when, to Cardano's tamper-resistant public ledger, where authors self-publish their own signed attestations via CIP-0170 identity credentials.

This technology would enable researchers, funders, reviewers and journal editors to prove authorship and priority using an audit trail they don't have to take anyone's word for. Moreover, ethics boards investigating misconduct, and judicial systems attributing IP rights, would have a tamper-proof, universally verifiable timestamped source to validate their assessments, especially in cross-border or adversarial collaborations where no single institution's record is accepted as authoritative.

In practice, a writer self-anchors a signed authorship record via their own irrevocable receipt.

### Supporting links (repo, site, demo)

- https://www.pubweave.com
- https://github.com/Intellart

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

This modular plug-in integration will have its own GitHub repo open-sourced under an MIT license.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The verifiable provenance & authorship module described in this proposal will first be deployed as an integration to PubWeave, gathering feedback then eventually evolving into its own pluggable module.

It is designed to become platform-agnostic, with an on-chain validator component and an off-chain SDK that integrates with a publishing tool allowing users to timestamp their writing/research efforts.

This deliberate separation of concerns is what leads to a TRL of 1.

Architecture design: researchers bind their ORCiD account to their wallet and self-anchor authorship / provenance attestations via ATTEST transactions.

What this grant covers:

- CIP-0170 client library (open-source)
- Verification SDK (open-source)
- Mainnet deployment by Milestone 1 (TRL 7)
