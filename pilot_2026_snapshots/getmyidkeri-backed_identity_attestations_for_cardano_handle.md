# GetMyID:KERI-Backed Identity Attestations for Cardano Handle

> The first live implementation of CIP-0170 on a production Cardano handle platform.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 31
- **Proposer:** `stake1ux2nq4qau9sfq55e9pv5phstd945s6fe2pjandat67vme2g5q4dqz`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-19T09:19:38.178000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

**Slavcho Andreevski - Founder & Full-Stack/Blockchain Developer**

- LinkedIn: [linkedin.com/in/slavcho-andreevski-120b3b233](http://linkedin.com/in/slavcho-andreevski-120b3b233)

- GitHub: [github.com/kingslavcho](http://github.com/kingslavcho)

- YouTube: kingotkingovski (500 subscribers)

- Full-stack development (Flask/PyCardano stack), Cardano wallet integration, on-chain metadata architecture

- Author of CPS-0032 "Handle Provider Interoperability" (merged into the official Cardano CIP repository)

- Currently drafting the follow-on provider-registry CIP

- Member of a Cardano/crypto community reach spanning a 3,900+ member Facebook closed group, a 400-member Instagram community with 30,000+ monthly views, a 500-subscriber YouTube channel, and a 200-follower X account

- Role: architecture, CIP-0170 integration, provider-registry CIP authorship, mainnet deployment

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If this integration reaches sustainable commercial revenue, we pledge 7% of net revenue from it to the Cardano treasury, capped at ₳140,000, activating once annual revenue from it exceeds ₳100,000.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Target: 195 genuine mainnet attestation transactions, generating at least ₳100 in network fees, above the ₳84 program floor. Based on a two-week funnel: 

- Facebook group ([facebook.com/share/g/1Ami4Am2HK/](http://facebook.com/share/g/1Ami4Am2HK/)), 3,900+ members × 1% = 39 users. 
- Instagram ([instagram.com/cr_revolucija](http://instagram.com/cr_revolucija)) + YouTube (youtube.com/@kingotkingovski) + X ([x.com/MakedonKing](http://x.com/MakedonKing)) = 1,100 combined × 1% = 11 users. 
- Of 24 existing handle holders (5 mainnet, 19 preprod), \~15 expected to re-engage. Total: 39 + 11 + 15 = 65 users.

Who transacts: existing handle holders binding attestations; new holders at mint time; community members from direct outreach.

Why: initial attestation plus one rotation/re-verification per user = 3 qualifying transactions each. 65 × 3 = 195.

Integrity: only genuine external activity counted; no self-minting to inflate figures.

### How will you reach and onboard real users - and what evidence backs your channels?

Channels: 

- Facebook group ([facebook.com/share/g/1Ami4Am2HK/](http://facebook.com/share/g/1Ami4Am2HK/)), 3,900+ members; 
- Instagram ([instagram.com/cr_revolucija](http://instagram.com/cr_revolucija)), 400 members, 30k+ monthly views; 
- YouTube (youtube.com/@kingotkingovski), 500 subscribers; 
- X ([x.com/MakedonKing](http://x.com/MakedonKing)), 200 followers; existing GetMyID handle holders, 24 (5 mainnet, 19 preprod).

Day 1–3: announce to Facebook group, reach out to existing holders. Week 1: \~39 users (Facebook × 1%).

Days 8–14: cross-post to Instagram, publish a YouTube walkthrough (extending my cyber-hygiene content — verifying identity without checking every wallet-address character), post to X. 

Week 2: \~11 users (IG+YT+X = 1,100 × 1%), plus \~15 of 24 existing holders re-engaging.

Cumulative 2-week: 39 + 11 + 15 = 65 real users, at 3 qualifying transactions each, supporting a 195-transaction target.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives: Other handle providers (e.g. ADA Handle) issue handles with no cross-provider verification standard; generic DID/identity frameworks exist off-Cardano but have no native Cardano integration path today. 

Our advantage: We are integrating an existing, Foundation-recognized CIP (0170) into a live product, and we already have standing in the governance process (CPS-0032) that will decide how handle interoperability works across all Cardano providers, not just ours.

### Please provide details about the Technology Readiness Level selected for your existing product

- GetMyID ([getmyid.today](http://getmyid.today)) is live and publicly accessible, with real mainnet handle-minting transactions today - 24 handles minted to date (5 mainnet, 19 preprod).
- The Pilot does not fund GetMyID's existing handle-minting platform. It builds a new CIP-0170 attestation layer on top of this operational product.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Handle layer** (existing): GetMyID's live `.did` handle-minting flow, unchanged.

**Attestation layer** (new): KERI identifier generation/linking, CIP-0170-compliant attestation construction, on-chain publication bound to the handle's minting transaction/metadata.

**Verification layer** (new): independent library allowing any third party to check attestation validity without trusting GetMyID as an intermediary.

**Provider-registry layer** (existing, in progress): our in-progress CIP extended to reference CIP-0170 attestations as the interoperability mechanism between providers.

This fits the identity track directly: CIP-0170 is used exactly as specified, for persistent, independently verifiable identity claims, rather than unrelated high-frequency activity.

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

Target market: Cardano wallet/dApp developers needing identity-verification primitives, and the broader handle/identity-provider ecosystem benefiting from a shared interoperability standard.

Evidence: GetMyID has minted 24 handles to date (5 mainnet, 19 preprod). Mainnet volume is modest because wallets can't yet resolve a `.did` handle from its name alone, they need the full policy ID, a gap our in-progress provider-registry CIP is designed to close. We authored CPS-0032 "Handle Provider Interoperability," merged into the official Cardano CIP repository - evidence the community recognizes this problem.

Reach: 

- Facebook group ([facebook.com/share/g/1Ami4Am2HK/](http://facebook.com/share/g/1Ami4Am2HK/)), 3,900+ members; 
- Instagram @cr_revolucija ([instagram.com/cr_revolucija](http://instagram.com/cr_revolucija)), 400 members, 30k+ monthly views; 
- YouTube (youtube.com/@kingotkingovski), 500 subscribers, covering crypto cyber-hygiene; 
- X @MakedonKing ([x.com/MakedonKing](http://x.com/MakedonKing)), 200 followers.

Beyond Cardano: CIP-0170 is built on KERI, a chain-agnostic identity standard with real-world adoption outside crypto (GLEIF's vLEI framework, Trust over IP). Our verification library targets any KERI witness network, not Cardano-only, positioning this as a reference case for the wider identity-standards community.

### Applicant name

Slavcho Andreevski (publicly known as Slavcho King / Makedon King, channel handle "kingotkingovski")

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Open-source core: The CIP-0170 integration module and verification library remain free and open source to maximize adoption across other providers. Revenue: GetMyID's underlying handle-minting business (fees paid entirely from the user's wallet - pure-profit model) continues independent of grant funding and funds ongoing maintenance of the attestation layer. 

Why usage continues: Attestations are permanent on-chain records once created; new handle mints and identity updates generate ongoing transaction activity with no dependency on continued grant funding. Resolution improvements from the provider-registry CIP are also expected to grow the underlying handle base over time.

### On-chain identity (CIP-0170) - expected transaction count

195

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

- ₳40,000 - CIP-0170 attestation-binding module: KERI identifier linking, attestation construction, on-chain publication.
- ₳35,000 - Independent verification library and third-party integration tooling.
- ₳25,000 - Provider-registry CIP updates incorporating CIP-0170 attestations, plus published integration documentation enabling third-party providers to independently adopt the standard
- ₳20,000 - Testnet validation, security testing (attestation forgery/replay attack testing), mainnet deployment.
- ₳12,000 - Open-source reference implementation, integration documentation.
- ₳8,000 - User onboarding, launch activities, adoption measurement.

Total: ₳140,000. No funding allocated to GetMyID's already-live handle-minting platform.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- CIP-0170 attestation-binding module built and tested on preprod.
- Independent verification library complete and tested.
- End-to-end flow:
  - handle holder wallet
  - KERI identifier
  - signed CIP-0170 attestation
  - confirmed Cardano mainnet transaction.
- Provider-registry CIP draft updated to incorporate CIP-0170 attestations.
- Mainnet deployment with the Pilot-required message tag and declared identifiers.
- Direct outreach executed per the two-week onboarding plan: Facebook group announcement, existing handle-holder outreach, Instagram/YouTube/X cross-posting (including a short walkthrough video).
- Open-source reference implementation, verification library, and integration documentation.
- Security testing completed (attestation forgery, replay-attack resistance).
- Live product, tagged repository release, release notes, transaction evidence, and Demo Day demonstration.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

100

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Problem: Cardano handle/identity providers currently issue name-to-identity mappings with no cryptographically verifiable, tamper-resistant proof that a handle is actually controlled by the identity it claims to represent - trust rests on the provider's word, not a portable, independently verifiable credential. This blocks genuine interoperability between providers, wallets, and dApps that want to verify handle-identity ownership without trusting a central registrar.

Target users: Cardano wallet and dApp developers who need to verify handle-identity ownership; handle holders who want a portable, rotatable identity credential; other Cardano handle/identity providers seeking a shared interoperability standard.

Solution: Integrate CIP-0170 (KERI-backed metadata attestations) into GetMyID so every `.did` handle can carry a cryptographically verifiable, independently checkable identity attestation, folded directly into the provider-registry CIP we are already authoring.

Outcome: A live, mainnet-verifiable identity-attestation layer for Cardano handles, and one of the first real-world reference implementations of CIP-0170 in production.

### Supporting links (repo, site, demo)

- https://getmyid.today
- https://github.com/cardano-foundation/CIPs/tree/master/CPS-0032
- https://linkedin.com/in/slavcho-andreevski-120b3b233
- https://github.com/kingslavcho
- https://facebook.com/share/g/1Ami4Am2HK/

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

MIT for all open-sourced components.

KERI/CIP-0170 attestation-binding module, independent verification library, integration documentation.

This covers the new attestation-integration module built under this grant; the broader GetMyID commercial handle-minting platform remains closed-source.

Koios/Ogmios and wallet-connector integrations retain their original licenses.

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
- Planned flow:
  - handle holder wallet
  - KERI identifier generation/linking
  - CIP-0170 attestation
  - on-chain binding to the handle
  - independent third-party verification.
- We already have production experience with Cardano metadata architecture, CIP-30 wallet flows, and CBOR/transaction-building, directly transferable to implementing CIP-0170's attestation format.
