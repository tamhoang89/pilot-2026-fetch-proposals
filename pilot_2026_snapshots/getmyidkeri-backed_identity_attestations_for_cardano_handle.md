# GetMyID:KERI-Backed Identity Attestations for Cardano Handle

> "Your handle, cryptographically proven to be yours."

## Proposal Metadata

- **Status:** finalized
- **Revision:** 4
- **Proposer:** `stake1ux2nq4qau9sfq55e9pv5phstd945s6fe2pjandat67vme2g5q4dqz`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-14T14:32:31.975000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

**Slavcho Andreevski - Founder & Full-Stack/Blockchain Developer**

- Full-stack development (Flask/PyCardano stack), Cardano wallet integration, on-chain metadata architecture
- Author of CPS-0032 "Handle Provider Interoperability" (merged into the official Cardano CIP repository)
- Currently drafting the follow-on provider-registry CIP


- Administrator of a large Cardano community group
- Role: architecture, CIP-0170 integration, provider-registry CIP authorship, mainnet deployment

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If this integration reaches sustainable commercial revenue, we pledge 5% of net revenue from it to the Cardano treasury, capped at ₳140,000, activating once annual revenue from it exceeds ₳100,000.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

- Target: 400 genuine mainnet attestation transactions.
- Who transacts: existing GetMyID handle holders binding attestations to their handles; new handle holders binding attestations at mint time; our Cardano community group members (real, distinct external wallets).
- Why: creating an initial identity attestation, updating/rotating a KERI identifier, and re-verifying an attestation are each separate qualifying transactions.
- Usage pattern: we estimate roughly 100–120 real users during the adoption window, each generating 3–4 qualifying attestation/update transactions on average - consistent with identity attestations being updated periodically rather than one-off, unlike simple mint-and-done flows.
- Integrity: only genuine external-user activity is counted; no users are paid or incentivized for measured transactions; all activity follows the Transaction Integrity Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

Existing channels: GetMyID's live user base, our Cardano community group (which we administer), and outreach to at least one other handle/identity provider for adoption validation. Usage tracked through distinct wallets performing qualifying CIP-0170 attestation transactions.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives: Other handle providers (Ada Handle) issue handles with no cross-provider verification standard; generic DID/identity frameworks exist off-Cardano but have no native Cardano integration path today. Our advantage: We are not proposing a new identity framework, we are integrating an existing, Foundation-recognized CIP (0170) into a live product, and we already have standing in the exact governance process (CPS-0032) that will decide how handle interoperability works across all Cardano providers, not just ours.

### Please provide details about the Technology Readiness Level selected for your existing product

- GetMyID ([getmyid.today](http://getmyid.today)) is live, publicly accessible, with real users and real mainnet handle-minting transactions today.
- The Pilot does not fund GetMyID's existing handle-minting platform - it builds a new CIP-0170 attestation layer on top of this operational product.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

- **Handle layer** (existing): GetMyID's live `.did` handle-minting flow, unchanged.
- **Attestation layer** (new): KERI identifier generation/linking, CIP-0170-compliant attestation construction, on-chain publication bound to the handle's minting transaction/metadata.
- **Verification layer** (new): independent library allowing any third party (wallet, dApp, other provider) to check attestation validity without trusting GetMyID as an intermediary.
- **Provider-registry layer** (existing, in progress): our in-progress CIP extended to reference CIP-0170 attestations as the interoperability mechanism between providers.
- This architecture is a direct fit for the identity track's technical requirements because it uses CIP-0170 exactly as specified, for persistent, independently verifiable identity claims, rather than for high-frequency or unrelated on-chain activity.

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

Target market: Cardano wallet/dApp developers who need identity verification primitives, and the broader handle/identity-provider ecosystem that stands to benefit from a shared interoperability standard. Evidence: GetMyID is a live product with real users and real mainnet minting transactions today. We authored and got CPS-0032 "Handle Provider Interoperability" merged into the official CIP repository - direct evidence the community already recognizes this exact problem as worth solving. We are currently drafting the follow-on provider-registry CIP.

### Applicant name

Slavcho Andreevski

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Open-source core: The CIP-0170 integration module and verification library remain free and open source to maximize adoption across other providers. Revenue: GetMyID's underlying handle-minting business (fees from `.did` handle minting, paid entirely from the user's wallet - pure-profit model) continues independent of grant funding and funds ongoing maintenance of the attestation layer. Why usage continues: Once live, attestations are permanent on-chain records; new handle mints and identity updates generate ongoing transaction activity with no dependency on continued grant funding.

### On-chain identity (CIP-0170) - expected transaction count

400

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

- ₳40,000 - CIP-0170 attestation-binding module: KERI identifier linking, attestation construction, on-chain publication.
- ₳35,000 - Independent verification library and third-party integration tooling.
- ₳25,000 - Provider-registry CIP updates incorporating CIP-0170 attestations, plus community outreach/adoption validation with at least one other provider.
- ₳20,000 - Testnet validation, security testing (attestation forgery/replay attack testing), mainnet deployment.
- ₳12,000 - Open-source reference implementation, integration documentation.
- ₳8,000 - User onboarding, launch activities, adoption measurement.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- A live CIP-0170 attestation-binding flow on [getmyid.today](http://getmyid.today), integrated into the existing handle-minting product.
- KERI identifier generation/linking and on-chain attestation construction, tested end-to-end on preprod.
- An independent verification library allowing any third party (wallet, dApp, other provider) to check an attestation's validity without trusting GetMyID as an intermediary.
- End-to-end flow live on mainnet: handle holder wallet → KERI identifier → signed CIP-0170 attestation → confirmed Cardano transaction.
- Our in-progress provider-registry CIP updated to reference CIP-0170 attestations as the interoperability mechanism.
- Mainnet deployment with the Pilot-required message tag and declared identifiers.
- Open-source attestation module, verification library, and integration documentation published on GitHub.
- Security testing completed
- Live product, tagged repository release, release notes, transaction evidence

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

140

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Problem: Cardano handle/identity providers currently issue name-to-identity mappings with no cryptographically verifiable, tamper-resistant proof that a handle is actually controlled by the identity it claims to represent - trust rests on the provider's word, not on a portable, independently verifiable credential. This blocks genuine interoperability between providers, wallets, and dApps that want to check "does this handle really belong to this identity" without trusting a central registrar.

Target users: Cardano wallet and dApp developers who need to verify handle-identity ownership; handle holders who want a portable, rotatable identity credential instead of a static claim; other Cardano handle/identity providers seeking a shared interoperability standard.

Solution: Integrate CIP-0170 (KERI-backed metadata attestations) into GetMyID so every `.did` handle can carry a cryptographically verifiable, independently checkable identity attestation, and fold this directly into the provider-registry CIP we are already authoring.

Outcome: A live, mainnet-verifiable identity-attestation layer for Cardano handles, and one of the first real-world reference implementations of CIP-0170 in production - accelerating adoption of a CIP that today has zero production integrations.

### Supporting links (repo, site, demo)

- https://getmyid.today
- https://github.com/cardano-foundation/CIPs/tree/master/CPS-0032

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

- CIP-0170 integration is currently at architecture/use-case design stage.
- Planned flow: handle holder wallet → KERI identifier generation/linking → CIP-0170 attestation → on-chain binding to the handle → independent third-party verification.
- We already have production experience with Cardano metadata architecture (labels 674/675, CIP-30 wallet flows, and CBOR/transaction-building - directly transferable to implementing CIP-0170's attestation format.
