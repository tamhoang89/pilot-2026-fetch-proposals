# Verifiable provenance & authorship via on-chain attestations

> Supply-chain traceability applied to the research lifecycle addressing the reproducibility crisis in Science and Journalism.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 58
- **Proposer:** `stake1uxnuuh3h9ppxh9ru9zqs044fendnahp84afcrwelpsfxalqjv9mhr`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-20T05:43:42.169000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

We are the team that developed [PubWeave](https://www.pubweave.com/), a Cardano mainnet dApp with a smart contract-enabled peer-review module.

Albert Feghaly (Intellart) — <https://www.linkedin.com/in/albert-feghaly-28060a113/>

- Principal at Neurocan Inc.

- Intellart project lead

- Senior software developer

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
- Dominik Sipic (<https://www.linkedin.com/in/dominiksipic/>) is a Senior software developer at Thespian and the main backend dev on the PubWeave build

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**N/A**

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who**:

Any person that wishes to timestamp a paragraph, idea, or result can do so cryptographically on the Cardano blockchain. The infrastructure is optimized for a scientific workflow, but not limited to it. PubWeave's architecture follows an evolutionary model: blog article → collaborative preprint → peer-reviewed article, with each stage optional. Bloggers, journalists, and academics all find their niche within PubWeave. User acquisition targets those who benefit most from time-stamping their work as it progresses.

**Why:**

- Provable authorship before publication (preprint time-stamping — priority disputes, patent claims)
- Verifiable peer review trail (funders and institutions increasingly require it)
- Career incentive: ORCID-bound reputation anchored in KERI, traveling with the researcher — not trapped in a publisher's silo.

**How often:**

A single paper generates \~20 attestations over its lifetime. A researcher publishing 2–3 papers per year generates 40–60 attestations annually. A cohort of 16–20 researchers produces 160–300 attestations over a 3-month window.

This is the bare minimum that a short-term outreach strategy should get us.

### How will you reach and onboard real users - and what evidence backs your channels?

Albert Feghaly, team lead and published researcher with consulting relationships across multiple biotechs, brings a personal network of researchers as the first adoption channel. In parallel, our marcom partner, [Puzzlewood](https://pubweave.com/files/Puzzlewood_Marcom_Catalyst.pdf), builds the conversion machine around that:

- Messaging workshop defining who converts and why
- Landing page copy and conversion design
- A 2-minute founder/explainer video
- A foundational content blitz of 2–3 articles
- An early-adopter webinar giving direct access to the founding team

Regular posting on X/LinkedIn is maintained throughout.

Each channel feeds the same funnel: researcher hears about the platform, signs up, binds ORCiD to their DID, and self-anchors their first attestation. As the product matures and the open-source tools drive wider adoption, the same funnel scales to university partners, open-science communities, and institutional clients.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Web 3 competitors**

- ResearchHub: token-incentivized publishing
- Molecule: research IP tokenization
- Open Science Chain: research provenance prototype on Hyperledger Fabric
- DeSci Labs: open-access publishing infra

*Answer*:

None ship full lifecycle provenance as a product (and none are Cardano-native, not that it matters much to users).

ResearchHub and Molecule solve a related but separate problem: incentivizing research.

OSC is a data-integrity API for institutional research platforms. It doesn't touch authorship, publishing, or identity, and it's permissioned.

DeSci Labs is open-access publishing infrastructure; we are building a provenance-as-a-service layer where the researcher owns the proof, applicable to any domain, not just Science (although it is our primary target).

### Please provide details about the Technology Readiness Level selected for your existing product

PubWeave is a publishing platform on Cardano mainnet.

**Evidence:**

- **Live platform:** <https://www.pubweave.com/> — operational since 2023

- **Treasury smart contracts (OpShin/Python):** <https://github.com/Intellart/pandao-treasury-sc> — peer-review escrow, moderation, bounty mechanism, all live on mainnet

- **Close-out report:** <https://www.pubweave.com/blog/pubweave-close-out-report-catalyst-fund-9>

- **Demo video:** <https://youtu.be/Ecga56irC38>

- **Mainnet tx**: <https://cexplorer.io/address/addr1wx7me8zf6k9qe8zxjjm3c82yms4uvcfgapnnaplzqjsu78su3du9q>

Notes

1. Intellart's YouTube channel is not promotional, it only contains close-out videos.
2. PubWeave is pending a marketing campaign for user acquisition.
3. TRL 7 was chosen based on technical maturity, not user count.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Layer 1: Provenance substrate**

*Proponents of open-source, we set out to find the closest Cardano library for our needs, and settled on zenGate Global's Winter Protocol supply chain traceability toolset.*

Winter's `object_event` was the perfect fit for our implementation of the article-lineage state machine (idea → preprint → final).

Fork two Aiken/Plutus V2 validators:

- `singleton` minting policy: creates the unique on-chain object representing an article
- `object_event` spend validator: stateful transitions on the datum

Extend datum with research-specific fields:

- On-chain contracts are domain-agnostic: all research logic (EPCIS-equivalent for science) lives off-chain in the SDK. This means the validators stay small, auditable, and reusable.

Heavily review and audit the validators on prepod.

**Layer 2: Identity & attestation** (CIP-0170-based)

Portable, cryptographically verifiable identity anchored in KERI:

- AUTH_BEGIN: publish the researcher's credential chain, establishing signer authority
- ATTEST: anchor a content digest into the researcher's Key Event Log (KEL) to prove they signed at a specific KEL sequence number, at a specific time
- AUTH_END: revoke authority

**How the layers compose:** Winter's `object_event` gives script-enforced, stateful on-chain provenance. CIP-0170 sits on top for portable, externally-verifiable identity. The researcher's attestations travel with their KERI identifier, not locked to PubWeave's database.

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

**Target market**. Global R&D to GDP ratio was 1.92% at &gt;$2T (UNESCO Institute for Statistics, 2023). More than 8M active researchers publish &gt;3M articles a year in &gt;42,500 peer-reviewed journals (The STM Report, 2018). In addition to authors, funders, journal editors, and ethics boards must also verify claims. Even if we capture 0.01% of the market only: 3M papers/year × 0.0001 × 20 claims over the lifetime of a paper = 6K events/year.

**The reproducibility crisis**. &gt;70% of researchers failed to reproduce others work and &gt;50% failed to reproduce their own (Baker, Nature, 2016); &gt;50% of preclinical research is irreproducible resulting in $28B/year wasted in the US alone (Freedman et al., PLOS Biology, 2015); &gt;10,000 research papers were retracted in 2023 (Van Noorden, Nature, 2023).

**Product-market fit**. Researchers already adopt identity and provenance infrastructure at scale:

- ORCID reached 15M registrations

- Horizon Europe mandates FAIR data plans

- NIH 2023 Data Management & Sharing Policy requires documented data plans

- MIT uses blockchain to issue Digital Diplomas proving institutional trust in on-chain credentials.

**Media**. Gallup reported in 2022 a low 34% trust in media.

**The AI problem**. AI-generated fake research factories are proliferating: \~10% of cancer papers show signs of paper-mill fabrication (Scancar et al., BMJ, 2026).

**The demand for timestamped, author-anchored provenance is growing fast.**

### Applicant name

Neurocan Inc. (DBA: Intellart)

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

At 6k attestations per year (0.01% of academic market capture, not counting non-scientific writing), a platform fee of 2 ADA per attestation would generate 12k ADA per year or 1.2K ADA per month, which covers core maintenance, negligible at the moment. With scaling, monthly expenses rise, but so do users.

On a bigger scale, the 2 ADA fee is dropped. Open-source tools (CIP-0170 client, verification SDK) stay free (barring network fees): they only drive adoption. Revenue comes from institutions: publishers and (bio-)tech startups who need verification, audit trails, and compliance dashboards, and eventually universities and funders. The free tool becomes the standard, the paid layer captures the institutions.

Comparably, companies like Seqera, GitLab, Grafana and Red Hat sell support and/or enterprise features for their open-source tools.

Funders like Horizon Europe and NIH already mandate FAIR data and data management plan. Trustless provenance compliance is the logical next step.

### On-chain identity (CIP-0170) - expected transaction count

750

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The verifiable provenance module (CIP-0170 client library and verification SDK) is designed but there is no code and no mainnet path without this funding. Mainnet deployment on PubWeave will be the first integration.

**Funds from each part of the grant:**

**Part 1**. Intellart (product): 50k ADA

- Smart contracts, CIP-0170 client, verification SDK, architecture
- Mainnet-ready
- PubWeave integration

**Part 2a**. Puzzlewood (marcom): 25k ADA

- Messaging, explainer video, content blitz, funnel, user acquisitation

**Part 2b**. Intellart or Thespian (full-stack): 25k ADA

- Frontend, backend, coordination with Puzzlewood

**Part 3**. Sustaining fuel: 25k ADA (if received)

- Outreach, social, maintenance, bug fixes, feedback loops

**Note**: Part 2 is aimed at meeting usage targets. 

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. CIP-0170 client library (open-source): DID creation, ATTEST transaction construction, key management.
2. Verification SDK (open-source): validates attestation chains, checks KEL sequence numbers, label-scoped metadata indexing.
3. Forked & extended Winter validators: singleton + object_event with research-specific datum: role-based authority (author/reviewer/editor), version chaining, review to article relational links, ORCiD binding on signers.
4. ORCiD to wallet binding: researchers connect their ORCiD account to a Cardano wallet. One binding per ORCiD, cryptographic proof of ownership.
5. Self-anchored attestation flow: users create ATTEST transactions anchoring authorship/provenance to their KEL.
6. PubWeave integration. Researchers can bind ORCiD, author articles with on-chain provenance, and verify attestations.
7. Verification endpoint — any third party can verify an attestation's validity (KEL sequence, signer authority, timestamp) via the SDK or an API.

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

Communicating information inevitably happens with a degree of authority, whether proof exists or not. Humans have a tendency to delegate authority to respected bodies because (1) not everyone has expertise in everything and (2) time is limited. In academia, journalism and other fields, we tend to trust highly respected journals and news agencies because of their heightened due-diligence. This process, however, is far from infallible, causing the all-too-familiar reproducibility crisis in science, unreliable journalism, and intellectual property (IP) disputes in research and tech.

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
- Mainnet deployment by Milestone 1 (TRL 7).
