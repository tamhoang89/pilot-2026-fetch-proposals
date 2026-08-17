# SALIS: Cardano's Decentralized Care Platform

> Building everyday Cardano utility through decentralized care, provider-owned profiles, and Smart Booking Contracts that connect independent providers directly with people seeking care.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 39
- **Proposer:** `stake1u996wjw2a9sqjd2k3c7mddv8330xmaan3axy4xst3zk9njsnmcn6e`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-17T16:01:19.098000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

SALIS is independently founded and led by Amber Morris, who has directed the project from concept through development of a live Cardano-native Decentralized Care Platform. As a solopreneur, I lead product strategy, platform architecture, user experience, Smart Booking Contract design, provider research, business planning, outreach, and ecosystem development.

SALIS has been primarily self-funded and already operates with provider discovery, provider-owned care profiles, onboarding workflows, CIP-30 wallet connectivity, and non-custodial Smart Booking Contract infrastructure configured for Cardano mainnet.

This existing production foundation provides the environment for implementing and validating the proposed CIP-0170 Verifiable Provider Authority integration. I am the sole project team member, developer, project lead, and accountable delivery owner for this proposal. No additional developers, security specialists, or KERI/CIP-0170 contributors are currently part of the proposed team. If specialized technical advice or services are required during implementation, they will be procured after award based on demonstrated project needs and are not represented as existing team members or confirmed contributors in this proposal. I remain responsible for product direction, implementation oversight, provider onboarding, adoption, milestone delivery, and evidence.\
\
GitHub: <https://github.com/ambercodes>\
LinkedIn: <https://www.linkedin.com/in/amber-m-400365113/>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

SALIS currently has approximately 250 seeded, unclaimed provider profiles forming an established acquisition pipeline. These are prospects, not users or counted adoption, and SALIS will continue identifying additional providers during the adoption period.

The 500-transaction target is a planning model, not guaranteed user behavior. Across the existing and expanding prospect pool, the model assumes approximately 100 external providers voluntarily become active and average five qualifying CIP-0170 transactions. Activity may include an initial provider-authority attestation plus attestations associated with genuine booking confirmations. Actual participation and frequency depend on independent provider choices and platform use.

The modeled path is direct outreach → profile claim/create → optional authority activation → normal SALIS booking activity. The corresponding ₳130 fee target is an aggregate target across qualifying activity. Seeded listings, SALIS-controlled wallets, testing, and transactions created solely to increase metrics will not count; only independently initiated external-user activity qualifies.

### How will you reach and onboard real users - and what evidence backs your channels?

SALIS has approximately 250 seeded, unclaimed provider profiles demonstrating an established provider research and outreach process; these are prospects, not users or Catalyst adoption. During adoption, SALIS will continue researching new providers, conducting direct outreach, and inviting providers to claim or create profiles and optionally establish Verifiable Provider Authority.

Channels include indexed SALIS provider pages, LinkedIn, and Facebook. Cardano and podcast outreach may supplement acquisition but is not included in the baseline. No partner commitments are counted.

First 2 weeks after M1: Days 1–3 launch and outreach; Days 4–7 onboard and measure claims, authority activations, external wallets and CIP-0170 activity; Days 8–10 expand outreach; Days 11–14 follow up and refine onboarding.

Only independently initiated external-user activity counts toward Catalyst adoption.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Existing alternatives include provider directories, booking platforms, payment processors, and practice-management tools such as Psychology Today, Jane App, Practice Better, Google Business Profiles, and Calendly. These services solve parts of the care experience but remain centralized.

SALIS combines Provider-Owned Profiles, Smart Booking Contracts, and non-custodial ADA payments in a Cardano-native platform. The proposed CIP-0170 Verifiable Provider Authority integration further allows participating providers to independently attest authority over their profiles while keeping sensitive information off-chain. This uses Cardano not only for payment, but for transparent agreements, provider sovereignty, and independently verifiable authority.

### Please provide details about the Technology Readiness Level selected for your existing product

SALIS is a live decentralized care platform deployed in a production environment. The existing product supports provider discovery, provider-owned care profiles, onboarding workflows, CIP-30 wallet connectivity, and an Aiken-compiled Plutus V3 Smart Booking Contract configured for Cardano mainnet.

The existing production platform constitutes the pre-Catalyst baseline and will be recorded before funded development begins. It excludes CIP-0170 provider authority, KERI verification, and CIP-0170 booking attestations. Those capabilities are the proposed integration and are separately assessed at TRL 4.

The production platform at [https://www.salis.care/ ](https://www.salis.care/)and supporting technical documentation provide evidence of the existing operational product.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

SALIS’s existing production architecture is configured for Cardano mainnet using CIP-30 wallet connectivity, Lucid transaction construction, Koios and Blockfrost blockchain services, and an Aiken-compiled Plutus V3 validator for non-custodial ADA Smart Booking Contract escrow. Funds remain under smart-contract control until booking settlement conditions are met.

The proposed CIP-0170 Verifiable Provider Authority integration adds a separate identity and authority layer without replacing or disrupting the existing booking architecture. Participating providers will associate a KERI Autonomic Identifier (AID) with their SALIS profile and use CIP-0170 transaction metadata to anchor privacy-safe attestations of profile authority.

Verification occurs off-chain through KERI Key Event Logs, credential chains, and a SALIS verifier/indexer. Sensitive credentials, member identity, care details, communications, and other private information remain off-chain.

This hybrid architecture is appropriate for SALIS because Cardano provides an independently verifiable record of provider authority while KERI supports portable identity, key rotation, delegation, and revocation. The integration remains optional and feature-flagged, allowing existing booking flows to continue unchanged for nonparticipating providers.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

SALIS serves two primary markets: Independent Care Providers and people seeking self-pay care, including holistic, wellness, integrative, and traditional practitioners who often operate as independent businesses.

These providers already rely on digital profiles, booking platforms, payment processors, and institutional relationships to establish their public presence and conduct business. SALIS currently maintains a seeded directory of approximately 250 provider profiles, demonstrating an established provider research and outreach process. These seeded listings are not counted as SALIS users until providers independently claim or create profiles.

The proposed CIP-0170 integration addresses a specific trust gap within this model: a wallet signature can prove control of a Cardano wallet, but not the real-world authority of the person acting for the provider or institution represented by a public profile.

Verifiable Provider Authority allows participating providers to establish portable, privacy-preserving proof of profile authority while creating a foundation for future institutional delegation and revocation.

Initial adoption will focus on inviting identified providers to claim their profiles and offering CIP-0170 authority attestation as an optional trust feature. Real usage will be measured only from independent external users who elect to use the integration.

### Applicant name

Amber Morris

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

SALIS is designed as a sustainable decentralized care platform with revenue built into its Cardano Smart Booking Contracts.

SALIS generates revenue through a 5% platform fee on completed bookings. Before a booking is accepted, the Smart Booking Contract transparently defines fund distribution. ADA is held in non-custodial smart contract escrow and released to designated wallets when settlement conditions are met.

The proposed Verifiable Provider Authority integration strengthens the existing platform by adding optional, independently verifiable provider authority without requiring sensitive care information on-chain. The architecture also establishes a foundation for future institutional authority workflows. Its continued use is supported by SALIS’s existing booking ecosystem rather than grant funding.

As SALIS grows, a portion of platform fees is intended for a community growth pool governed through the future SALIS DAO, supporting continued platform and ecosystem development.

### On-chain identity (CIP-0170) - expected transaction count

500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Catalyst request: ₳125,000. Preliminary budget uses a $25,500 USD planning basis: $14,000 CIP-0170/KERI architecture, backend/frontend development, wallet/identity integration, testing, deployment, documentation and technical evidence; $8,500 provider outreach, onboarding materials, user education, activation support and external-user validation; $3,000 project management, Catalyst reporting and Demo Day delivery. Existing SALIS infrastructure is excluded from funded work. Amber Morris is the sole project team member and delivery owner.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month M1 window, SALIS will deliver a limited, optional CIP-0170 Provider Authority pilot on Cardano mainnet behind production feature flags.

Deliverables include provider KERI AID association and proof of control, privacy-safe profile manifests, CIP-0170 profile authority attestations, off-chain KERI verification, authority/revocation status, audit receipts, and an “Authority Attested” profile status. A second vertical slice will add optional provider-authority attestations to existing booking-confirmation transactions without modifying the escrow validator.

The integration will remain nonblocking so identity-service failure cannot trap or prevent ADA settlement. M1 includes Preview validation, privacy/security review, documentation, monitoring, and kill-switch procedures.

Completion will demonstrate repeatable end-to-end CIP-0170 mainnet attestations by external users and the same authority flows at Demo Day.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### On-chain identity (CIP-0170) - fee target (ADA)

130

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

SALIS is a live Cardano-native decentralized care platform connecting people seeking self-pay care directly with independent providers. It reduces reliance on centralized directories, booking services, and payment processors while expanding Cardano utility into everyday care.

SALIS integrates Cardano infrastructure, CIP-30 wallets, and Smart Booking Contracts configured for Cardano mainnet for transparent booking agreements and non-custodial ADA payment workflows. However, while a wallet signature proves control of a wallet, it does not independently prove that the person controlling it has authority to act for the provider or institution represented by a SALIS profile.

This proposal adds **Verifiable Provider Authority using CIP-0170**. Participating providers will be able to use KERI-backed Cardano attestations to establish verifiable authority over public profiles and optional care-agreement confirmation attestations. The architecture also establishes a foundation for future institutional authority workflows.

The integration preserves privacy by keeping member identity, care information, and credentials off-chain while anchoring only privacy-safe authority attestations to Cardano.

Catalyst funding will support implementation, mainnet deployment, and real-user validation of this new trust layer within the existing SALIS platform, beginning with provider profile authority.

### Supporting links (repo, site, demo)

- https://www.salis.care/
- https://github.com/ambercodes/salis-whitepaper

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed CIP-0170 Verifiable Provider Authority integration is currently at TRL 4. SALIS has defined the architecture for adding KERI-backed provider authority attestations to its existing Cardano production environment while preserving its privacy model.

Participating providers will associate a KERI identifier with their SALIS profile and use CIP-0170 metadata to attest profile authority. Verification will occur off-chain, while sensitive member, care, and credential information remains off-chain.

SALIS’s existing booking infrastructure is configured for Cardano mainnet. The next stage is implementing and validating the CIP-0170 verifier and provider-authority workflow before progressive production deployment behind feature flags.
