# d-App.Store × uTxO.Store

> the trust replenishing, privacy-preserving secure way to prove who you are, what you can do, and who you are becoming. in a human-centric, automation-augmented accountable way of living.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 26
- **Proposer:** `stake1u86mdkgvtdkgdjzzjth9cz9q9nerzatfqzxqfprnel78g0qusvc0y`
- **Funding requested:** ₳88,888
- **Last finalized:** 2026-08-19T19:09:56.564000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Listing credentials as proxies for professional proficiency risks the social capital of everyone involved. While we fully recognise the need for strict accountability within the Catalyst, this proposal says such methods are obsolete.

The demand for exhaustive disclosure exposes contributors to unnecessary risk and stifles creativity. In the digital commons, accountability must be balanced with interpersonal relationships and individual privacy. This is critical given the programme's history of communication issues, delays, and fund cancellations. A purely binary approach to oversight erodes trust and alienates the diverse talent required to innovate.

The limited grant amount available through this renewed Catalyst pilot informs our operational approach. Because this programme is structured around milestone-based disbursements and standard KYC/KYB processes, the risk of absconding is structurally mitigated before we begin.

Rather than relying on conventional full-time hires, which limited funds make financially untenable, we are leveraging a flexible interdisciplinary collective. As the lead proposer undergoing these compliance processes and responsible for the budget, my background spans film, theatre, architecture, and public service. This allows me to combine creative storytelling with systems thinking.

Our network brings together expertise across law, accounting, healthcare, diplomacy, science, education, the arts+ many more. This allows us to protect our contributors.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

As our endowment as protocol grows, it will complement the treasury by providing a stable resource base insulated from broader market volatility. \
\
This creates a mutually beneficial feedback loop, allowing us to continue to foster human-centric technology-mediated multi-polar governance, whilst nurturing long-termed invention-minded individuals, independent of short-termed funding contentions. 

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Usage justification: Settlement is batched by design — each on-chain transaction represents a resolved batch of off-chain attestation activity. Usage comes from the committed expert cohort: initial identity issuance at launch, then ongoing attestation settling every epoch. The wallet minimum is cleared by the cohort itself — \[15–20\] distinct wallets against a floor of 5.

First two weeks after mainnet: Week one, sovereigns.institute issues the first batch of expert attestations. Week two, the full cohort completes onboarding, putting the first epoch's floor within reach.

Long-term sustainability: Beyond launch, genuine usage will be driven by the continuous lifecycle of digital identity management. We anticipate a steady increase in volume driven by credential renewals, trust scoring updates, and onboarding new ecosystem partners.

Fee correlation: Our 1 ADA per transaction target reflects the reality that large script transactions for off-chain proofs carrying CIP-0170 metadata are not the same as regular transfers. This buffer ensures sustainability against larger byte sizes and complex on-chain validation, keeping the network secure without passing unexpected costs to users. 

### How will you reach and onboard real users - and what evidence backs your channels?

Current tech services silo personal context, locking users into proprietary platforms. To truly benefit from automation, individuals need a portable "mind model" that evolves to navigate increasing complexity.

We are building this through mind.multi-model.store, a fast feedback loop rooted in lifelong learning. Integrating Apple’s ClassKit, we enable a portable record of comprehension while dynamically proving verifiable competency. Over time, these models will augment the individual and become securely queryable by others, creating rich, attributable human experiences as automation advances.

Our approach is validated by the rapid growth of global education communities and the demand for accountable humans in the loop. As automation expands, the need for continuous up-skilling is paramount. The industry shift toward on-device compute and individual data ownership, championed by accessible hardware and student programs, proves the market is ready for tools that empower the individual.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Traditional verification confirms identity as a static, one-time event. We connect verified identity to an ongoing, privacy-preserving record of competency, ensuring your reputation remains under your control rather than locked in a proprietary silo.

We will operate as a certified Digital Verification Services (DVS) provider. As a compliant institutional anchor, we will legally verify identities and skills under emerging global trust frameworks. This includes acting as an Identity Service Provider (IDSP) for core identities, an Attribute Service Provider (ASP) for specific skills, a Holder Service Provider (HSP) to securely store reusable credentials, and an Orchestration Service Provider (OSP) to coordinate the verification workflow.

### Please provide details about the Technology Readiness Level selected for your existing product

*Existing product TRL details:* The coordination platform currently runs live on Apple TestFlight with six fully working surfaces. The zero-knowledge proving infrastructure—which serves as the core trust mechanism behind attestation—is already built and actively generating proofs. This demonstrates a validated technology ready for the next phase of integration. Current TestFlight access requires the iOS 27 beta, but September's public OS release will significantly widen testable reach to any current device during the grant window itself. This ensures that our testing pool can scale rapidly without hardware or software barriers, allowing for robust real-world feedback and continuous validation of the platform's capabilities as we move steadily toward our future full mainnet deployment phase

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Our on-chain architecture balances digital identity privacy with a verifiable public footprint. Attestations settle via a declared batching address distinct from private keys. Off-chain activity collapses into periodic on-chain proofs, preserving unlinkability while providing a public footprint. Epoch-based settlement ensures proofs land regularly. This aligns privacy with rhythm requirements, fitting an identity category valued for verification quality over transaction frequency.

\
Our core infrastructure issues CIP-0170 adjacent attestations via sovereigns.institute on Cardano, proven by cryptographically signed attestations. Our full footprint, including batching address, message tag, and team wallet is publicly declared. For fast verifiability, we implement the starstream/nightstream zkVM with advanced folds and proofs, alongside a WASM-based, Hydra-like off-chain mirror of Leios endorsers.

We are also exploring the Model Context Protocol (MCP), which is now stateless like the UTXO model, opening avenues for personal governance explorations via delegated stake and representation (dRep). Building on the Starstream DSL within the Nightstream zkVM, this enables us to securely verify attributes without disclosing underlying data.

Fundamentally, we are laying the technical foundations to operate as a certified Digital Verification Services (DVS) provider across trust roles, including Identity (IDSP), Attribute (ASP), Holder (HSP), and Orchestration (OSP) Service Providers. 

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

Large-scale, globally distributed funding programmes often struggle to find enough qualified reviewers. Traditional curation methods simply cannot verify domain expertise at the scale required, leaving a critical gap in their decision-making processes.

As AI automation increasingly handles complex tasks, the need to reliably verify the human in the loop—and their specific competency—becomes paramount. Any distributed organisation faces this exact hurdle: how to prove participant expertise without relying on a slow, centralised authority.

We provide the infrastructure to solve this. We are currently in a watershed moment where digital assets have gained formal legal recognition through the UK's Property (Digital Assets etc 2025) Bill. This, alongside the upcoming Data Use and Access Bill—which modernises data sharing and digital verification services—mirrors a broader global shift toward legally recognising digital frameworks.

While our development is rooted in the UK's progressive regulatory environment, we are building this as a not-for-profit initiative. The primitives we are creating are designed as a public commons, ensuring that organisations worldwide can utilise our platform to meet emerging global standards, while simultaneously building a privacy-preserving, on-chain record of their reviewers' expertise.

### Applicant name

TRVST

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

We are evolving into an Alternative Business Structure (ABS) via sovereigns.institute, uniting legal and domain experts for grounded accountability. To ensure long-term independence, we are establishing an endowment through a Donor.Advised.Fund (DAF) to create a sustainable philanthropic ecosystem that operates independently of traditional grant cycles.

Long-term, we will sustain this infrastructure through Digital Verification Services (DVS) certification. Opening in September 2026, institutional demand for certified identity attestations will provide steady, predictable usage. Because attestations represent ongoing relationships rather than one-time verification events, this creates a durable, recurring revenue model. This approach ensures the infrastructure remains fully operational and self-sustaining long after the initial pilot phase ends, ultimately reducing reliance on external funding while scaling trust across the ecosystem.

### On-chain identity (CIP-0170) - expected transaction count

69

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, immediate revenue work will outrank long-term identity infrastructure, meaning this critical layer simply does not get built this year. This capital accelerates our core timelines to deliver a compliant, privacy-preserving architecture. The budget is allocated as follows:

\[\~85%\] Engineering: Focused on core development, including attestation issuance, epoch-based batching settlement, and agent commissioning under bounded capabilities.

\[\~10%\] Certification & Onboarding: Establishing the institutional pathways required to operate as a certified Digital Verification Services (DVS) provider.

\[\~5%\] Audit & Documentation: Ensuring our zkVM infrastructure and smart contracts are fully secure, verifiable, and thoroughly documented for the entire Cardano ecosystem.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Identity/KYC Layer: Establishing core identity infrastructure. We will issue CIP-0170 attestations via sovereigns.institute on Cardano mainnet. Evidence: Live product URL and at least one real-user mainnet transaction hash mapped to flow steps. Our full footprint (batching address, message tag, team wallets) will be declared openly.

Technical Infrastructure: Implementing starstream/nightstream (zkVM) and deploying a WebAssembly-based, off-chain mirror of Leios endorsers alongside our mainnet launch. Evidence: Short technical walkthrough video, release notes covering architecture/limitations, and repo URL with commit tag.

Governance & DVS Framework: Exploring the stateless Model Context Protocol (MCP) for personal subsidiarity governance. Preparing to operate as a certified Digital Verification Services (DVS) provider to legally verify identities. Evidence: Test evidence bundle (checklist, bug log) + show at Demo Day, Q&A. All deliverables are fully aligned with our strategic roadmap.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

69

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Catalyst faces a scarcity of domain experts because reviewers rely on static, unverifiable claims like LinkedIn profiles. Amid emerging frameworks like the UK's Data Use and Access Bill, this creates friction around legally compliant, privacy-preserving identity verification. Traditional models fail, creating cognitive overload for the individual when attempting to prove their ongoing competency.

To solve this, we are moving away from scalar currency and open-loop architectures. Instead, we are building an institutional anchor that acts as a trusted root to enable accountable, distributed branches. By operating as a certified Digital Verification Services (DVS) provider, we are establishing the technical roots and primitives to preserve genuine human discernment, ensuring that human insight and judgment remain the ultimate arbiters of value and values over algorithmic arbitrage in an automation-augmented age.

Our infrastructure provides the legal and technical scaffolding for individuals to securely verify their identity, validate their specific skills, and hold their own reusable proofs. We are building this using zero-knowledge infrastructure, including the starstream/nightstream zkVM, to provide privacy-preserving attestations. This delivers cryptographically anchored identity proof alongside a verifiable record of expertise. Our approach combines a personalised memory model with Self-Sovereign proofs, defining a new standard for portable, context-dependent reputation.

### Supporting links (repo, site, demo)

- https://d-App.Store

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

MiT

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Proposed integration TRL details: While the foundational architecture is established, CIP-0170 adjacent attestation issuance is fully designed but not yet implemented. This represents genuinely new, incremental work rather than retroactive funding for past development. The core proving primitives, our device-level security model, and the necessary Digital Verification Services (DVS) certification pathway all currently exist, which materially de-risks the build. This funding specifically enables us to bridge the gap between our validated environment and a fully operational mainnet deployment, ensuring that the final integration meets both rigorous security standards and practical usability requirements for all end-users without compromising on the core principles of decentralised identity
