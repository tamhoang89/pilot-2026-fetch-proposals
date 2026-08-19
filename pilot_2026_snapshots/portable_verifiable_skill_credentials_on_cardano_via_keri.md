# Portable, Verifiable Skill Credentials on Cardano via KERI

> SkillSwap upgrades its live on-chain proof anchoring into CIP-0170 verifiable skill credentials, giving every user a portable KERI-backed reputation they carry anywhere beyond the platform.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 51
- **Proposer:** `stake1u8x4lqtk6czqrlhjqyqlp8a8y7u0ekcxytg6796nm2xnxxsrvccyp`
- **Funding requested:** ₳70,000
- **Last finalized:** 2026-08-19T22:59:04.862000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

I'm Daniel Olanrewaju, solo founder.

Links: [LinkedIn](https://www.linkedin.com/in/devfreeguy/), [GitHub](https://github.com/devfreeguy), X (@devfreeguy)

Shipped projects:

- SkillSwap: zero to Cardano mainnet in 12 weeks. Awarded Cardano Pie by Gimbalabs and the Cardano Foundation. Live: [myskillswap.xyz](http://myskillswap.xyz). Repo: [github](https://github.com/devfreeguy/skill-swap). X: @myskillswap
- Tagwise: Solana identity protocol mapping @handles to wallets. On-chain program, published SDK, docs. Site: [tagwise.me](http://tagwise.me). SDK: [tip-sdk](https://www.npmjs.com/package/@tagwise/tip-sdk)

I will implement KERI integration myself, using the CF Reeve reference implementation ([cf-reeve-platform](https://github.com/cardano-foundation/cf-reeve-platform)) as the blueprint. My identity protocol work on Tagwise (AID-like resolution, wallet-derived identity, on-chain state) directly maps to the KERI/ACDC path. If specialized consultation is needed, grant funds allow engaging short-term advisors.

Community partner: Metac ([metacc.online](http://metacc.online)), a tech education nonprofit in Nigeria where I volunteer as instructor. [LOI](https://drive.google.com/file/d/1SJnFSiznZ5LSBzEDNDPmLXHghy2QvnVe/view?usp=sharing)

Confirmed team member: Akindipe Emmanuel George, UI/UX Designer ([LinkedIn](https://www.linkedin.com/in/akindipe-emmanuel-george-5591702a6)), joining for the pilot.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who:** Metac controlled pilot 50 students, Cardano, IOG, Catalyst Discord members, 50 existing users. Reach: 50 Metac, 1200 Discord, 50 existing.

**Why:** Core loop requires a completed swap to issue KERI credential. Each swap creates one anchor tx. Credentials build portable reputation.

**How often:** 145 swaps in 90 days, 0.23/day to 1.6/day. M1 30: Metac 22 plus X launch and re engagement 8. M2 55: Discord 35 plus Metac retention 20. M3 60: workshops 40 plus Metac 20.

**Justification:** Audience x conversion x frequency. Base 7 swaps since July 19 equals 0.23/day. M1 1.0/day is 4.3x with Metac activation 60 percent and existing 20 percent. M3 is 41 percent of total, reducing single point risk. No ADA incentives funded by grant or counted.

**Stretch:** 250 swaps if 2 extra nonprofits confirmed in M2, excluded from base.

**Fee target:** 145 swaps equals about 350 labeled txs with commitment, anchors, refunds. At 0.3 ADA avg, about 105 ADA. Target 110 ADA, 5 percent buffer. 2 ADA commitment fee is treasury revenue, excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

Current channels driving 50+ users and 7 mainnet swaps organically since July 19th:

1. X/Twitter (@myskillswap, @devfreeguy) - 12 weekly build-in-public posts under #gimbalabs #pieceofpie #hackathon
2. Cardano developer communities and Discord channels
3. Metac nonprofit partnership ([metacc.online](http://metacc.online)) - I volunteer as instructor. Proof: [post 1](https://www.instagram.com/p/DYhHzufM5wo/) and [post 2](https://www.instagram.com/p/DR7lVPJDBww/)

Post-grant growth plan:

1. Launch announcement on X when credentials go live
2. Community education in Cardano Community Discord, IOG Technical Discord, and Catalyst Discord via showcase posts, CIP-0170 content, and demo sessions
3. Content marketing: credential portability guides, success stories, demo videos
4. Additional tech education nonprofit partnerships following the Metac template
5. Cardano ecosystem cross-promotion via Veridian and Cardano Foundation channels

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/Umyi-BKyfUY

### Who else solves this today - competitors/alternatives, and why does your approach win?

Direct competitors: Simbi, Barterchain, Barter Bloc, The Barter Shop. All offer peer-to-peer skill exchange without money. All keep reputation locked inside their platforms as star ratings or in-app credits. None issue verifiable credentials.

Adjacent competitors: Fiverr, Upwork, Skillshare, Preply. All require payment for skill access. All lock reputation inside their walled gardens. All charge 5-20% platform fees.

SkillSwap wins on three axes: 1) money-free exchange lowers the barrier for emerging markets, 2) two-way matching engine ensures fair value exchange, and 3) CIP-0170 credentials make reputation portable, cryptographically verifiable, and independent of SkillSwap's continued existence. No competitor combines all three.

### Please provide details about the Technology Readiness Level selected for your existing product

SkillSwap is operational on Cardano mainnet at [myskillswap.xyz](https://myskillswap.xyz) with real users and real ADA transactions. Core systems validated:

- CIP-8 wallet authentication with cryptographic signature verification
- 2 ADA commitment fee payments and automatic on-chain refunds on decline
- End-to-end encrypted messaging (Pusher primary, Ably fallback)
- Multi-provider on-chain proof anchoring (Blockfrost, Koios, Maestro)
- Deliverable submission and dual-party swap confirmation
- Public reputation pages and explorer with verifiable proof records

Current usage: 7 completed mainnet swaps anchored on-chain, 50+ registered users. Live and functional but at early adoption stage, consistent with TRL 7.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

SkillSwap already runs a production-grade Cardano on-chain architecture that CIP-0170 will extend, not replace:

Current architecture (live on mainnet):

1. Wallet auth via CIP-8 signature verification using @cardano-foundation/cardano-verify-datasignature
2. CIP-30 transaction signing in user wallets (Eternl, Nami, Lace) for 2 ADA commitment fees
3. Multi-provider tx submission via Blockfrost (primary), Koios, Maestro (fallback) for redundancy
4. Proof anchoring via Cardano metadata transactions under registered metadata label (5757)
5. Automatic refund path via platform hot wallet with signed CBOR verification before dispatch
6. Public explorer aggregating completed swaps with anchor tx links

CIP-0170 addition:

1. Platform-managed issuer AID with KERI-backed key state via a KERIA agent
2. ACDC credential schema for skill attestations (subject: user wallet/AID; claim: skill; evidence: swap ID + counterparty confirmation)
3. SAID computation per credential
4. SAID anchored in Cardano tx metadata riding the existing anchoring path
5. Public verifier endpoint resolving anchor, checking issuer KEL, verifying ACDC signature, confirming on-chain timestamp
6. Optional export to Veridian (pending Veridian API availability) for user-owned credential portability

Why this fits: KERI is ledger-independent by design. Cardano provides the tamper-evident, censorship-resistant, publicly verifiable timestamp no off-chain notary can offer.

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
- Metac pilot cohort (<https://www.metacc.online/>) — a tech education nonprofit in Nigeria where I volunteer as instructor. LOI: <https://drive.google.com/file/d/1SJnFSiznZ5LSBzEDNDPmLXHghy2QvnVe/view?usp=sharing> Every user and swap so far is entirely organic, driven by build-in-public content without any paid marketing. Grant funding is the leverage point that turns this traction into scale.

Market signal: platforms like Simbi, Barterchain, and Barter Bloc show demand for money-free skill exchange. None offer portable, on-chain verifiable credentials. SkillSwap is the only platform integrating Cardano-anchored verifiable identity.

### Applicant name

Daniel Olanrewaju

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Fee model: SkillSwap charges a 2 ADA commitment fee on every swap request. This is anti-spam, not a service charge. It filters out low-effort requests and ensures every swap is intentional. Fully refunded if the receiver declines. Live on mainnet today.

Post-grant revenue streams:

1. Premium credential features: verified issuer status, custom credential schemas, bulk issuance for bootcamps and training organizations
2. Institutional partnerships: education nonprofits (like Metac) paying to issue credentials to graduates
3. Enterprise verification API: employers and DAOs paying to verify SkillSwap credentials at scale
4. Premium user features: highlighted profiles, priority matching, analytics for power users

Why usage continues post-grant: the commitment fee alone covers infrastructure at current scale (Vercel, NeonDB, Cloudinary, Blockfrost). Growth is unit-economic positive from day one. Credential portability creates network effects that outlast grant funding.

### On-chain identity (CIP-0170) - expected transaction count

350

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without grant CIP-0170 cannot ship. Bootstrapped alongside contract work. Grant enables full time delivery in pilot window.

\
High level spend tied to deliverables:\
**Development** Daniel 3mo 28,000 ADA KERIA, ACDC, Veridian export, verifier delivers creds.\
**Security MLabs** 10,500 ADA audit zero criticals delivers audited deploy.\
**Infrastructure** 7,000 ADA 3mo only KERIA hosting, witnesses, Blockfrost Koios delivers uptime.\
**Design** Akindipe 3mo 8,400 ADA credential flow UX and verifier UI.\
**Community Education** 10,500 ADA 1 Lagos workshop co hosted with Metac plus 1 online plus guides. No paid ads, no token incentives, no airdrops. Fund Rules Sec 3 compliant.\
**Ops** 5,600 ADA reporting and contingency.

\
Total **70,000 ADA**.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

**Week 1-2: Pilot Launch**

Deliverables: KERIA agent deployed to staging. Metac onboarding for 50 students. X launch + demo video.

Measurable: 20 wallets created, 5 swaps completed.

**Week 3-4: KERI Backend**

Deliverables: signify-ts integrated. SAID pipeline operational. Test suite passes.

Measurable: 100% test credentials generate valid SAID.

**Week 5-6: Testnet**

Deliverables: Credential issuance on swap. Metadata anchoring live. Public verifier at /verify/\[said\].

Measurable: 10 testnet credentials issued and verifiable.

**Week 7-8: Security Audit**

Deliverables: Audit by MLabs Group Ltd. All critical issues resolved.

Measurable: Audit report with 0 criticals.

**Week 9-10: Mainnet**

Deliverables: Audited credential issuance deployed to Cardano mainnet. Public launch.

Measurable: 10 mainnet credentials issued.

Week 11-12: Adoption

Deliverables: 3 workshops: Lagos, Abuja, Online. CIP-0170 docs published.  

Measurable: 20 mainnet credentials. 90-day total: 145 swaps.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

110

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
- https://x.com/myskillswap
- https://www.gimbalabs.com/piece-of-pie-yearbook/projects/skillswap
- https://x.com/gimbalabs/status/2081834226207322382?s=20

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

The core anchoring path SkillSwap already uses (metadata transactions via Blockfrost/Koios/Maestro fallback) is the same path CIP-0170 will ride on. This is proven and mainnet-live.

However, the KERI-specific layer (issuer AID setup, KERIA agent configuration, ACDC credential schema, SAID computation, signify-ts integration, and public verifier endpoint) has not yet been implemented. The Cardano Foundation's Reeve platform ([cf-reeve-platform](https://github.com/cardano-foundation/cf-reeve-platform)) provides the reference implementation I will build against. Concept is fully formulated and architecturally scoped.
