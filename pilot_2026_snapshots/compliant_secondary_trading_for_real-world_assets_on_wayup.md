# Compliant Secondary Trading for Real-World Assets on Wayup

> Anyone can tokenise an asset. Almost nobody can legally trade it. Wayup is building the venue where the rules travel with the token.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1u80mnpaqq2jtz9cd64y88zfyx0g3dyhzq4v9c87vptc4yfc0x6rwq`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T13:51:20.543000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Anvil is a Cardano development company. We build and operate the infrastructure this integration extends, and Wayup is our own marketplace running on it. Anvil has successfully completed 6 Catalyst proposals over 4 years, most of which are public goods that are actively being used. 

Delivery evidence, all public: Wayup, live on Cardano mainnet, built entirely on our own API and indexer. Anvil serves 200 clients across 30 countries, with 457k assets minted and ATH \~₳50M total value staked through our infrastructure. \
\
Zachary Soesbee - CEO - Responsible for Catalyst Milestone and processes. \
<https://www.linkedin.com/in/zachary-soesbee-4a5ab317a/>\
\
Patrick Bernard - COO - Responsible for employee management, UI/UX decisions, and deliverables on the platform. \
<https://www.linkedin.com/in/patrick-b-436a3621/>\
<https://github.com/invalidcredentials>\
\
David Desjardins - CTO - Responsible for technical progress, architecture, and development. \
<https://www.linkedin.com/in/david-desjardins-a7b930120/>\
<https://github.com/tqueri>

Every named participant's role is disclosed above, and no individual on this team is named on any other proposal in this round.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: external holders and buyers, from their own wallets, paying their own fees. Anvil never submits or subsidizes on a user's behalf. Team wallets are declared and excluded.

What counts: transfers under our declared CIP-0113 policies (marketplace purchases and holder-to-holder transfers), holder allowlist enrollment, and issuer rule updates. One-time registry and protocol-parameter setup is team-paid and excluded from the counted target.

Model: 4-8 RWA issuers from Anvil's client base/new clients; \~220 distinct external wallets, against an 18-wallet minimum at this award level; one enrolment plus \~3.5 transfers each on average, giving \~500 qualifying transactions. At an average ₳0.48 per CIP-0113 transfer, higher than a simple send because each spends programmable_logic_base, runs the global validator, and executes a registry lookup plus transfer script, that is ₳240 against a ₳200 floor.

Pace: marketplace volume is bursty and the daily cap is 20% of the period total. We therefore stagger issuer launches roughly one per epoch instead of a single launch event, so enrolment carries the early epochs and recurring trading carries the rising late-epoch floors. 

### How will you reach and onboard real users - and what evidence backs your channels?

Named channels, with no commitments claimed that we do not have.

1. [Anvil's](https://x.com/AnvilDevAgency) existing client base, 200+ projects already minting on Cardano through our API across 30 countries. Target: 4-8 live RWA issuers. 

2. Spreading Awareness: Currently there is only 1 project we could find that is using CIP-113 ([X Post](https://x.com/lavanetxyz/status/2085335188712849684?s=20)). 

3. Wayup's existing trader base and our own channels ([Wayup](http://x.com/wayupio), [Discord](https://discord.gg/84P7TteHge)) , the demand side, already holding wallets and already transacting.

**First two weeks after M1:**

Days 1–3: first issuer live, policy verified on Wayup and open for trading. 

Days 4–7: hands-on onboarding for issuers two and three, first external purchases, verify the epoch-1 floor. 

Days 8–12: fix what real users hit , we expect wallet and eligibility edge cases, not protocol failures. 

Days 13–14: publish the per-epoch table and counting methodology.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/4tz8dgGq_gg

### Who else solves this today - competitors/alternatives, and why does your approach win?

Issuer-run portals. How RWA trades today: the issuer runs the only venue and checks eligibility in its own database. It works, and it produces a captive, illiquid market with no price discovery.

Existing Cardano NFT marketplaces. They can list a token but cannot read, enforce or even display its transfer rules. A restricted asset either fails silently at settlement or trades in breach of its own terms.

Ethereum permissioned-token platforms (ERC-3643 / T-REX and peers). Proof the model works at scale, and evidence of exactly what Cardano lacks.

Off-chain compliance in a spreadsheet. Still the honest default for most issuers.

We win because we are the only party with a live Cardano marketplace and the issuance stack. Every competitor has to build or borrow the half they are missing.

### Please provide details about the Technology Readiness Level selected for your existing product

Wayup is a production Cardano marketplace operating on mainnet, not a prototype or testnet deployment. It is publicly accessible at [wayup.io](http://wayup.io) and supports live trading today: native listings with a 2% trading fee, cross-collection cart purchases spanning multiple policy IDs, offers, bundles, royalty enforcement, aggregated third-party listings, collection analytics, and CIP-30 wallet connection.

It runs on Anvil's own production API and indexer, the same infrastructure serving 200 client projects across 30 countries , and its live market activity, trade history and top-collection data are publicly visible on the platform.

The Pilot does not fund Wayup. It funds a new CIP-0113 programmable-token layer built inside this existing production system.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Wayup is a Next.js marketplace on Anvil's API. All transaction building lives server-side; the frontend never builds transactions or holds keys. The CIP-0113 work follows that split.

Issuance (Anvil API): a new programmable-token service wrapping the Cardano Foundation's CIP-0113 reference validators , issuance_mint under the issuer's own credential, a registry entry binding the policy to its transfer logic, and a transfer substandard selected per asset (allowlist/KYC-gated, jurisdiction, lockup, holder cap). Issuers mint and update rules from their own wallet. Anvil never takes custody.

Indexing: Wayup's indexer learns the registry , resolving each registered policy to its transfer logic and tracking programmable-token UTXOs at programmable_logic_base, where ownership is the stake credential, not the address.

Settlement: the marketplace trade composes with the CIP-0113 spend path. The token leg spends from programmable_logic_base, programmable_logic_global runs once per transaction via withdraw-zero, the registry lookup selects the transfer script, and the token returns to the shared address under the buyer's stake credential.

Eligibility pre-flight: a CIP-0113 transfer can legitimately fail validation. Wayup evaluates the transfer logic off-chain before the user signs and surfaces the reason , the difference between a usable RWA market and a wall of failed transactions.

All qualifying activity carries the Pilot's registered message tag. Footprint declared at M1.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Two sides, and we already touch both.

Supply , issuers. Organizations that want to tokenize an asset carrying real transfer restrictions: fractional property, revenue shares, private credit, regulated collectibles, and membership or access rights with resale limits. Anvil's existing client base of 200+ projects across 30 countries is our direct pipeline. These are organizations already paying us to put assets on Cardano who today have no compliant route to a secondary market.

Wayup's existing user base of Cardano traders, already transacting on mainnet with connected wallets and real fee-paying behavior.

Evidence of demand. The pattern is proven elsewhere and absent here. On Ethereum, permissioned-token standards for regulated assets (ERC-3643 and peers) underpin a live tokenized-asset market precisely because transfer rules are enforced by the token. Cardano has no equivalent venue. CIP-0113 exists as a standard with a Cardano Foundation reference implementation and, to our knowledge, no production secondary market using it. The gap is infrastructure, not appetite.

What we do not claim: we have no signed issuer commitments at submission. Converting existing Anvil clients into live RWA issuers is the declared principal risk of this proposal, and the usage plan is sized against it rather than around it. This is a long term play to accommodate CIP-113 assets and give them a place to safely trade.

### Applicant name

Anvil Development Agency, Inc.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Wayup already charges a 2% trading fee on native listings. RWA trades settle through that same fee path, so the venue side is revenue-generating from the first trade and no new business model is required.

On the issuer side, Anvil's existing commercial relationship covers minting and API access. CIP-0113 issuance with configurable transfer rules becomes part of that paid offering.

Users pay their own Cardano network fees. Anvil never pays fees on a user's behalf, never takes custody of assets, and is never counterparty to a trade. There is no token and no protocol fee.

Usage continues after the pilot because secondary trading is recurring by nature. An issuer tokenizes once, but holders trade, transfer and re-list continuously, and each of those is a real transaction with a real reason to exist. Nothing here depends on grant money continuing.

### Programmable tokens (CIP-0113) - expected transaction count

500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant, CIP-0113 stays a roadmap item: a programmable-token settlement path is a substantial build with no revenue until issuers exist, so it loses to marketplace features for existing collectors. The grant makes it a funded, dated deliverable.

₳200,000, tied to M1 deliverables:

- ₳60,000, CIP-0113 issuance service in Anvil API (validators, registry, substandards)

- ₳50,000, composed marketplace settlement path

- ₳32,000, indexer: registry awareness, UTxO and stake-credential tracking

- ₳18,000, eligibility pre-flight and compliance UX

- ₳15,000, independent security review of the transaction path

- ₳10,000, preprod validation, QA, test evidence

- ₳15,000, issuer onboarding, docs, Dune tagging, measurement

No user subsidies, fee reimbursement or transaction rewards.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Internal target week 9, deadline week 12.

1. CIP-0113 issuance service live in Anvil API: issuance_mint under the issuer's credential, registry entry, and two transfer substandards (allowlist/KYC-gated and lockup).

2. Wayup indexer registry-aware: resolves registered policies to transfer logic, tracks programmable-token UTxOs by stake credential.

3. Composed settlement path live on mainnet , a CIP-0113 asset bought and settled through Wayup by a wallet not ours.

4. Eligibility pre-flight in the UI, showing pass/fail and reason before signing.

5. At least three external issuers onboarded, minting from their own wallets.

6. Independent security review of the composed transaction path, findings remediated.

7. Declared footprint published: policy IDs, script hashes, addresses, message tag, team wallets; Dune tagging live.

8. Open-source CIP-0113 adapter and eligibility library (Apache-2.0), release notes, test evidence bundle, walkthrough video, Demo Day.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

240

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Tokenising a real-world asset is the easy part. Trading it afterwards is where every Cardano RWA project stops.

The moment a token represents equity, debt, property or a regulated collectible, its transfers carry rules: verified holders only, jurisdiction limits, lockup periods, holder caps, forced transfer under a court order. Today those rules live in the issuer's off-chain database, so the only place the asset can trade is the issuer's own portal , a captive, illiquid, single-venue market. Put that same token on a general marketplace and the rules do not travel with it.

CIP-0113 solves the token half: the rules live in the asset itself. Nobody has built the other half , the venue.

Wayup is our Cardano marketplace, live on mainnet today with real traders, listings, offers, bundles and royalties. We will make it CIP-0113 aware end to end:

- Issuers mint RWA tokens with a chosen transfer policy through Anvil's API, from their own wallet.

- Wayup's indexer recognises registered CIP-0113 policies and resolves their transfer logic.

- Before a buyer signs, Wayup evaluates the token's own rules and states plainly whether the trade will settle, and if not, why.

- Settlement is a real CIP-0113 transfer validated on-chain, not a permission check in our database.

The result is an asset whose compliance is enforced by Cardano, trading on an open secondary market any issuer can list into. Buyers and sellers pay their own network fees. We are the venue, never the counterparty.

### Supporting links (repo, site, demo)

- https://ada-anvil.io
- https://github.com/Cardano-Forge
- https://dev.ada-anvil.io/

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

The CIP-0113 integration is at TRL 2: architecture and transaction flows are defined, no code is written. We state that plainly rather than inflating it.

What lowers delivery risk is that every surrounding component already exists in production: transaction building in Anvil API, the marketplace indexer, CIP-30 wallet flows, listing, offer and settlement logic, and royalty handling. The funded work is the programmable-token layer that plugs into them , issuance service, registry-aware indexing, the composed settlement path, and eligibility pre-flight.

We will freeze and publish a pre-development baseline commit before funded work begins, so no existing Wayup or Anvil code can be mistaken for grant-funded delivery.
