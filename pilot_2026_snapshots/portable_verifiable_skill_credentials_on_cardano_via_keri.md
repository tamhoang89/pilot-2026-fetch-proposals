# Portable, Verifiable Skill Credentials on Cardano via KERI

> SkillSwap upgrades its live on-chain proof anchoring into CIP-0170 verifiable skill credentials, giving every user a portable KERI-backed reputation they carry anywhere beyond the platform.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 21
- **Proposer:** `stake1u8x4lqtk6czqrlhjqyqlp8a8y7u0ekcxytg6796nm2xnxxsrvccyp`
- **Funding requested:** ₳70,000
- **Last finalized:** 2026-08-17T08:29:25.742000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

I'm Daniel Olanrewaju, solo founder. I've shipped multiple Cardano and Web3 projects in the last 12 months, demonstrating both delivery discipline and ecosystem depth:

- SkillSwap: current project. I built it full-stack from zero to Cardano mainnet in 12 weeks under the Piece of Pie Hackathon. Awarded Cardano Pie by Gimbalabs and the Cardano Foundation.
- Tagwise: Solana-based identity protocol mapping @handles to wallet addresses. I shipped the on-chain program, published SDK, and full documentation site.
- TripFi (Contribution): BCH-powered AI travel booking platform I contributed to. Won Runner Up in the BCH-1 Hackcelerator Application Track.

Technical relevance to this proposal:

- Deep hands-on experience with CIP-8 wallet auth, CIP-30 transaction signing, multi-provider chain infrastructure (Blockfrost, Koios, Maestro), and on-chain metadata anchoring already shipped in SkillSwap
- My prior identity protocol work on Tagwise directly informs the KERI/ACDC integration path
- Consistent public track record of shipping under hackathon deadlines

Part of the 70k ADA grant is explicitly allocated to team expansion (see funding breakdown). I will recruit a KERI-experienced developer and a designer within the first month post-selection.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Genuine usage generation is baked into SkillSwap's core loop, not bolted on.

Who transacts: users completing peer-to-peer skill swaps. Every completed swap generates one credential issuance and one on-chain anchor transaction. Credential revocations and updates generate additional on-chain activity.

Why they transact: users pay the 2 ADA swap fee because it unlocks a skill exchange they want. The credential issued at completion is a permanent, portable proof of that exchange, creating an incentive loop where credential value grows with each swap.

How often: current baseline is 7 completed mainnet swaps and 50+ users since going live July 19th. Realistic projection over the 3-month pilot:

- Month 1: 20-40 swaps (KERI setup + growth push begins)
- Month 2: 80-150 swaps (credential feature live + paid promotion)
- Month 3: 200-350 swaps (network effects from portable credentials)

Fee target: 70,000 ADA grant with committed fee generation of 5,500+ ADA in network fees over the pilot period, driven by anchor, refund, and credential update transactions. Grounded in current organic baseline extrapolated conservatively.

### How will you reach and onboard real users - and what evidence backs your channels?

Current channels driving 50+ users and 7 mainnet swaps organically since going live on July 19th:

1. X/Twitter (@myskillswap, @devfreeguy) — 12 weekly build-in-public posts under #gimbalabs #pieceofpie #hackathon drove community awareness and testnet users
2. Gimbalabs Discord and Cardano developer channels
3. MetaC nonprofit partnership — student onboarding via in-person tech education programs in Nigeria

Post-grant growth and expansion plan:

1. Coordinated growth push aligned with the credential feature going live
2. Paid promotion on X and LinkedIn targeting emerging market developers and career switchers
3. Content marketing: build-in-public case studies, credential portability guides, success stories
4. Additional tech education nonprofit partnerships following the MetaC template
5. Cardano ecosystem cross-promotion via Veridian and Cardano Foundation channels
6. Referral incentives paid in Cardano-native assets

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/Umyi-BKyfUY

### Who else solves this today - competitors/alternatives, and why does your approach win?

Direct competitors: Simbi, Barterchain, Barter Bloc, The Barter Shop. All offer peer-to-peer skill exchange without money. All keep reputation locked inside their platforms as star ratings or in-app credits. None issue verifiable credentials.

Adjacent competitors: Fiverr, Upwork, Skillshare, Preply. All require payment for skill access. All lock reputation inside their walled gardens. All charge 5-20% platform fees.

SkillSwap wins on three axes: 1) money-free exchange lowers the barrier for emerging markets, 2) two-way matching engine ensures fair value exchange, and 3) CIP-0170 credentials make reputation portable, cryptographically verifiable, and independent of SkillSwap's continued existence. No competitor combines all three.

### Please provide details about the Technology Readiness Level selected for your existing product

SkillSwap is fully operational on Cardano mainnet at <https://myskillswap.xyz>. Every core system has been tested and validated with real users paying real ADA:

- CIP-8 wallet authentication with cryptographic signature verification
- 2 ADA swap fee payments and automatic on-chain refunds on decline
- End-to-end encrypted messaging (Pusher primary, Ably fallback)
- Multi-provider on-chain proof anchoring (Blockfrost, Koios, Maestro fallback)
- Deliverable submission and dual-party swap confirmation
- Public reputation pages and public explorer with verifiable proof records

Live evidence: 7 completed mainnet swaps, all anchored on-chain and viewable at <https://myskillswap.xyz/explorer> with 50+ registered users.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

SkillSwap already runs a production-grade Cardano on-chain architecture that CIP-0170 will extend, not replace:

Current architecture (live on mainnet):

1. Wallet auth via CIP-8 signature verification using @cardano-foundation/cardano-verify-datasignature
2. CIP-30 transaction signing in user wallets (Eternl, Nami, Lace) for 2 ADA swap fees
3. Multi-provider tx submission via Blockfrost (primary), Koios, Maestro (fallback) for redundancy
4. Proof anchoring via Cardano metadata transactions under a registered metadata label (5757)
5. Automatic refund path via a platform hot wallet with signed CBOR verification before dispatch
6. Public explorer aggregating completed swaps with anchor tx links

CIP-0170 addition:

1. Platform-managed issuer AID with KERI-backed key state via a KERIA agent
2. ACDC credential schema for skill attestations (subject: user wallet/AID; claim: skill; evidence: swap ID + counterparty confirmation)
3. SAID computation per credential
4. SAID anchored in Cardano tx metadata riding the existing anchoring path
5. Public verifier endpoint resolving the anchor, checking issuer KEL, verifying ACDC signature, and confirming on-chain timestamp
6. Optional export to Veridian for user-owned credential portability

Why this fits: KERI is ledger-independent by design. Cardano provides the tamper-evident, censorship-resistant, publicly verifiable timestamp no off-chain notary can offer. The chain is the notary; KERI is the identity layer.

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

Target market: global knowledge workers and lifelong learners who need verifiable proof of skill but cannot access traditional credentialing. Primary segments:

1. Emerging market professionals (Nigeria, Kenya, Philippines, Brazil) building international careers without formal credentials
2. Career switchers proving new skills without going back to school
3. Bootcamp graduates and self-taught developers needing a portable resume
4. Freelancers reducing platform lock-in on Fiverr, Upwork, and similar marketplaces

Evidence of demand:

- Went live on Cardano mainnet July 19th
- 50+ registered users across multiple countries
- 7 completed mainnet swaps, all anchored on-chain and publicly verifiable at [myskillswap.xyz/explorer](http://myskillswap.xyz/explorer)
- Real user acquisition from MetaC (tech education nonprofit in Nigeria)
- Testnet phase generated 18 additional completed swaps

Every user and swap so far is entirely organic, driven by build-in-public content without any paid marketing. This is early real-world traction, and grant funding is the leverage point that turns organic growth into scale.

Market signal: the skill-exchange space is growing. Platforms like Simbi, Barterchain, and Barter Bloc show demand for money-free skill exchange. None offer portable, on-chain verifiable credentials. SkillSwap is the only platform integrating Cardano-anchored verifiable identity.

### Applicant name

Daniel Olanrewaju

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Current revenue: 2 ADA swap initiation fee paid to the platform treasury on every swap request. Fully refunded if declined, retained on acceptance. This is live on mainnet today.

Post-grant revenue expansion:

1. Premium credential features: verified issuer status, custom credential schemas for institutions, and bulk credential issuance for bootcamps and training organizations
2. Institutional partnerships: MetaC-style education nonprofits paying to issue credentials to their students at graduation
3. Enterprise verification API: employers and DAOs paying to verify SkillSwap credentials at scale
4. Premium user features: highlighted profiles, priority matching, and analytics for power users

Why usage continues post-grant: the 2 ADA fee alone covers infrastructure at current scale (Vercel, NeonDB, Cloudinary, Blockfrost). Growth is unit-economic positive from day one. Every swap generates a fee. Credential portability creates network effects that outlast grant funding.

### On-chain identity (CIP-0170) - expected transaction count

600

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding enables three things that would not happen otherwise:

1. Team expansion. A solo founder can build MVP-quality integrations but cannot deliver production-grade KERI infrastructure, security auditing, and user-facing verification tooling in 3 months alone. Grant funds recruit a KERI-experienced developer and a designer.
2. Dedicated 3-month build focus. Currently SkillSwap is bootstrapped alongside contract work. Grant funding removes that constraint, enabling full-time delivery of the CIP-0170 integration within the pilot window.
3. Infrastructure investment: dedicated KERIA agent hosting, witness node participation, security audits, and user acquisition budget for the coordinated growth push during the pilot period.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Month 1:

- KERIA agent deployed (self-hosted or CF boot infrastructure)
- Issuer AID established for the SkillSwap platform with witnessed KEL
- ACDC credential schema drafted and validated
- Recruit KERI-experienced developer and designer

Month 2:

- signify-ts integration into SkillSwap backend
- Credential issuance triggered on completed swap
- SAID computation and Cardano metadata anchoring integrated into existing anchoring path
- Public verifier endpoint at /verify/\[said\] resolving anchor, KEL, and ACDC signature
- User-facing verified credential badges on public reputation pages
- Coordinated growth push with the credential feature going live

Month 3:

- Veridian export flow enabling user-owned credential portability
- Security audit of KERI integration
- Full documentation and public developer guide for CIP-0170 credential verification
- Marketing push targeting emerging market users and institutional issuers
- Minimum 200 credentials issued on mainnet within pilot window

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

5500

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

SkillSwap is a peer-to-peer skill exchange platform live on Cardano mainnet at <https://myskillswap.xyz>. Users teach what they know and learn what they need without money changing hands. Every completed exchange is anchored on Cardano as proof.

The problem: reputation earned inside any single platform is trapped there. A user who completes 20 skill exchanges on SkillSwap cannot carry that verified history to a job application, a DAO, another marketplace, or a future employer. Their proven expertise dies at the platform boundary. Traditional platforms like Fiverr, Upwork, and Skillshare intentionally lock reputation inside their walls because reputation is their moat.

The solution: this proposal integrates CIP-0170 KERI-backed identity attestations into SkillSwap. When two users complete a swap, the platform issues an ACDC (Authentic Chained Data Container) credential attesting to the skill exchange, computes its SAID, and anchors it on Cardano through the existing multi-provider anchoring path. The user can verify the credential publicly via a resolver, and optionally export it into Veridian (the Cardano Foundation's KERI identity wallet) to carry outside SkillSwap forever.

For whom: developers, designers, writers, tutors, and professionals in emerging markets where formal credentials are inaccessible or expensive. Every completed swap becomes a portable, cryptographically verifiable proof of skill that follows the user across employers, platforms, and borders.

### Supporting links (repo, site, demo)

- https://myskillswap.xyz
- https://github.com/devfreeguy/skill-swap

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

MIT License. Full source available at <https://github.com/devfreeguy/skill-swap>

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

CIP-0170 integration is at experimental proof-of-concept stage. Rationale:

The core anchoring path SkillSwap already uses (metadata transactions via Blockfrost/Koios/Maestro fallback) is the same path CIP-0170 will ride on. This is proven and mainnet-live at TRL 9.

However, the KERI-specific layer (issuer AID setup, KERIA agent configuration, ACDC credential schema, SAID computation, signify-ts integration on the edge, and public verifier endpoint) has not yet been implemented. The Cardano Foundation's Reeve platform (cardano-foundation/cf-reeve-platform) provides the reference implementation to build against. Concept is fully formulated and architecturally scoped. First working prototype is the primary milestone deliverable.
