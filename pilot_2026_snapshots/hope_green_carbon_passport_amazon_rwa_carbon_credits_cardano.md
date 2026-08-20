# Hope Green Carbon Passport Amazon RWA Carbon Credits Cardano

> Turning 6,152 verified Amazon seedlings into CIP-0113 compliant carbon-credit RWA tokens, anchored by CIP-0170 farmer identity, bringing Amazon family-farmer carbon credits fully on-chain on Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1ux9es7nq4wfegwxtenvxna5ern60zvp6xtqp4lwcmh4gcsqf7j4ry`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-20T02:14:43.777000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Our team pairs proven blockchain execution with real, on-the-ground Amazon reach, plus a track record of already shipping and monetizing this exact product category.

Expedito Belmont (Founder & CEO) and Marcio Pessoa (Founder & CMO) built Hope Green from concept to a live B2B platform with paying institutional customers and recurring revenue - not a whitepaper.

Wesley Sousa, Head of Blockchain, with prior experience at Greener and Sansa Labs, leads the technical build of the CIP-0113 and CIP-0170 integration - this is not our first blockchain implementation. Marcelo Chamy (VP Software Engineer) and Harlison Costa (UX/UI) round out execution capacity.

Gabriel Maia (CIO) brings direct institutional ties to FAEMG, SENAR, INAES, and rural unions, and Fabiano Nagamatsu (Advisor, Osten Move/FEA Angels/Inovativa Brasil) is the direct channel to our largest institutional buyer, Osten BMW.

Field credibility is independently verified: Ana Paula Paiva, Forestry Engineer at IDAM, has directly supported the agroforestry verification work this proposal builds on.

In short: we already run the farmer network, the buyer relationships, and the underlying product this grant extends - we are not assembling a team to start from scratch, we are extending one that already delivers.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: two user groups already active in Hope Green's business today, not new users we need to invent.

Institutional buyers (Osten BMW, plus pipeline partners Nestle and Rumo) mint and hold Carbon Rights Tokens as verifiable ESG/net-zero assets, then burn them on retirement - a recurring annual corporate obligation. Osten alone already holds 1,288 NFTs under the existing Polygon model, proving willingness to transact at this scale.

Family farmers receive a CIP-0170 credential once, then trigger fresh CRT mints as new plots or harvests are verified - tied to Hope Green's existing annual photo-verification cycle, so it's not new behavior, just a new destination chain for an existing habit.

Targets are reasonable but ambitious: our 2,500 CIP-0113 transactions represent converting \~800 of the 6,152 seedlings already verified in production (\~13% of the existing base). Our 300 CIP-0170 transactions cover \~250 farmers, a credible subset of the 50,000 already mapped through field partners (IDAM, SEBRAE-AM, ADAF). Both are grounded in usage that already exists off-chain, not hypothetical growth.

### How will you reach and onboard real users - and what evidence backs your channels?

We are not building acquisition channels from zero - we are converting channels already in use.

Buyer side: migrate Hope Green's existing institutional buyers - Osten BMW (already 1,288 NFTs), Nestle, and Rumo - into the CRT flow as soon as it is live on mainnet. Advisor Fabiano Nagamatsu, linked to Osten Move, is a direct line into that buyer relationship.

Farmer side: onboard from the 50,000 family farmers already mapped through active institutional partners - IDAM, SEBRAE-AM, ADAF, and SENAI - the same partners already supporting Hope Green's field operations today, with technical endorsement from Ana Paula Paiva, Forestry Engineer at IDAM.

Evidence: these are not prospective partnerships, they are signed pilots and a live paying customer. CIP-0170 credentials can be issued in batches as farmer registration progresses through these existing channels, and CRT minting is tied to Hope Green's already-operating annual verification cycle - not a new user-acquisition effort.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/CViwfeigv10

### Who else solves this today - competitors/alternatives, and why does your approach win?

Direct alternatives: [re.green](http://re.green), Mombak, and Carbonext - large-scale ecological restoration on degraded land, high entry cost, little or no active family-farmer inclusion, and no live NFT-based traceability layer.

Indirect alternative: traditional off-chain carbon registries (e.g. Verra), which institutional buyers are actively fleeing after double-counting and greenwashing scandals eroded trust.

Why we win: Hope Green is the only player combining a traceable NFT platform, active smallholder inclusion, and very low entry cost, already proven with 6,152 seedlings and a recurring institutional buyer (Osten BMW). No competitor offers CIP-0113 compliance (KYC/AML, freeze, burn-on-retire) or CIP-0170 farmer identity - the missing trust layer institutional buyers require.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 9 evidence: Hope Green is not a demo - it is a live production system with real, paying customers.

\- 6,152 seedlings planted and verified in the field across \~30 species, tracked via geolocation, species, and responsible farmer.

\- Live NFT issuance on Polygon, with an annual photo-verification cycle that gates continued farmer payment - an operating compliance mechanism, not a concept.

\- Recurring institutional revenue: Osten BMW has purchased 1,288 NFTs under the R$18/NFT, 5-year subscription model.

\- Active commercial partnerships/pilots: Nestle, Rumo, IDAM, SEBRAE-AM, SENAI, ADAF.

\- 75 people impacted, 51 acres restored - measured real-world outcomes.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Architecture: a two-layer on-chain design mapping directly onto the two selected integration areas.

Layer 1 - Farmer Identity (CIP-0170): each participating family farmer receives an on-chain identity credential bound to their stake key, attesting a georeferenced plot, family-farming program enrollment, and planting history. Issued once per farmer, then referenced (not re-verified) by every subsequent token mint.

Layer 2 - Carbon Rights Token (CIP-0113): a programmable native token minted per verified plot/harvest, representing tCO2e rights. Minting requires a valid CIP-0170 credential from the originating farmer (Sybil resistance) and restricts receiving addresses to KYC'd wallets. Built-in rules allow freezing in a verification dispute, and retirement is enforced via mandatory burn, eliminating on-chain double counting - the exact failure mode of legacy off-chain registries.

Why this fits: CIP-0113 is purpose-built for regulated RWA, giving compliance (KYC/AML, freeze, jurisdictional control) natively at the ledger level rather than in an off-chain wrapper institutional buyers cannot audit. CIP-0170 solves originator identity without a centralized KYC database for farmers, keeping custodial risk minimal. Off-chain data (photos, geolocation) stays off-chain as source evidence; only compliance-critical state - rights, identity, lifecycle - lives on Cardano, directly matching what the Pilot's two chosen areas require.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

Yes

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Target market: institutional buyers with net-zero/ESG commitments seeking auditable, fraud-resistant carbon credits (TAM 608M family farmers worldwide, SAM 3.9M in Brazil, SOM 330K in Amazonas state alone), plus the 50,000 family farmers Hope Green already has mapped access to, each with average potential of 700 seedlings.

Evidence of demand is not hypothetical - it is live:

\- 6,152 seedlings already planted and verified across \~30 species, 75 people impacted, 51 acres restored.

\- A recurring institutional buyer already purchasing at scale: Osten BMW has acquired 1,288 NFTs.

\- Signed partnerships and pilots with Nestle, Rumo, IDAM, SEBRAE-AM, SENAI, ADAF, AHK Mercosul, Capital Empreendedor, and Inova Amazonia - corporate and institutional validation beyond a single buyer.

\- A validated B2B revenue model already generating recurring payments: R$18/NFT annual subscription, 5-year contracts, with 40% of revenue flowing directly to the family farmer.

\- 60% of Amazonas' 330,000 family farmers were hit by the 2023/2024 historic drought, reinforcing urgency: this is climate resilience income, not vanity ESG.

Competitors ([re.green](http://re.green), Mombak, Carbonext) restore degraded land at high entry cost with little or no active family-farmer inclusion. Hope Green uniquely combines a traceable NFT platform, active smallholder inclusion, and low entry cost - the Cardano integration adds the compliance layer institutional buyers require.

### Applicant name

Btracer

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Hope Green already has a proven, self-sustaining revenue model, independent of grant funding: an R$18/NFT annual subscription with 5-year contracts, split 40% to the family farmer, plus a transaction fee, taxes, infrastructure, and operations. Institutional buyers (Osten BMW, Nestle, Rumo) already pay for this today.

The Cardano layer adds a second recurring revenue stream: institutional buyers pay to mint Carbon Rights Tokens (CIP-0113) against verified SAF plots, and pay again on retirement, since retiring a credit for ESG/net-zero reporting is a recurring annual corporate obligation, not a one-time purchase.

Usage continues post-grant because it is tied to Hope Green's existing B2B cycle: farmers already update verification photos annually to unlock payment, naturally triggering fresh CRT mints and FIC issuance every year, funded by buyer subscriptions already contracted for 5 years - not by grant capital.

### Programmable tokens (CIP-0113) - expected transaction count

2500

### On-chain identity (CIP-0170) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding enables Hope Green's first blockchain-compliance layer - without it, the 6,152 verified seedlings and 50,000 mapped farmers stay locked in off-chain NFT metadata, unable to reach institutional buyers who require auditable, KYC-compliant, double-counting-proof credits. The core business is self-funded and continues on Polygon regardless; this specific compliance layer would not get built without dedicated technical funding.

Spend, at a high level: engineering time for the CIP-0113 and CIP-0170 contract build (Aiken development, audits), the data bridge from existing Polygon verification records to Cardano, Dune Analytics integration, and KYC/KYB onboarding - taking the integration from TRL 2-3 to a live mainnet mint in 3 months.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of the 3-month window, we will deliver:

1\. CIP-0113 Carbon Rights Token contract on Preview testnet, enforcing KYC/AML-gated addresses, freeze-on-dispute, and burn-on-retire.

2\. CIP-0170 Farmer Identity Credential service, issuing credentials bound to farmer stake keys, tested against real registered farmers.

3\. Data bridge connecting existing Polygon verification records (geolocation, species, farmer, photo updates) to Cardano, piloted on a real subset of the 6,152 verified seedlings.

4\. Public open-source repository for both contracts, reusable for other environmental RWA projects.

5\. Live mainnet mint: at least one real CRT and one real FIC, backed by a genuine verified plot and farmer.

6\. Standardized Dune Analytics dashboard tracking transactions and fees against our declared targets.

7\. Demo Day showing the full flow: farmer verification to on-chain CRT held by a KYC'd buyer.

8\. Completed team KYC/KYB with Catalyst.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

1500

### On-chain identity (CIP-0170) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Hope Green already runs a live Payment-for-Environmental-Services platform: NFTs on Polygon representing 6,152 verified seedlings planted and maintained by Amazon family farmers, with an active institutional buyer (Osten BMW, 1,288 NFTs) and partners including Nestle and Rumo.

The problem: dispersed family-farmer carbon credits lack trustworthy, low-cost MRV. Institutional buyers avoid this market after double-counting scandals at traditional registries, and smallholders are locked out of a space dominated by large corporate restoration projects with high entry costs.

Hope Green already captures the raw MRV data - geolocation, species, farmer, growth stage, annual verification photos - but it lives as off-chain NFT metadata, not as a compliant financial asset.

Our solution: Carbon Passport, a new Cardano integration. Each verified plot mints a CIP-0113 programmable Carbon Rights Token with built-in KYC/AML, freeze-on-dispute, and burn-on-retire logic preventing double counting. Each farmer receives a CIP-0170 on-chain identity anchoring their plot and blocking Sybil fraud.

This serves two users: family farmers in the Amazon, who gain an auditable reputational passport and access to a market previously closed to them, and institutional carbon-credit buyers, who gain a compliant, fraud-resistant RWA they can trust and retire on-chain.

### Supporting links (repo, site, demo)

- https://www.hopegreenagro.com/
- https://www.linkedin.com/company/b-tracer/
- https://www.instagram.com/hopegreenagro/

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

### Funder, status, and what it covers

Funder: TecNova III (Amazonas state innovation program)

Status: In contracting (not yet disbursed/active)

Covers: Expansion of work with family farmers - field onboarding and agricultural operations, not the Cardano integration proposed here.

Funder: Inova Amazonia

Status: Completed

Covers: Development of the Hope Green platform (the existing Polygon-based NFT/PSA system). This funding built the base product that this Catalyst proposal extends with a new, separately-funded Cardano compliance layer (CIP-0113/CIP-0170) - it did not cover any blockchain work beyond Polygon, and does not overlap with the integration proposed here.

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The Cardano integration is currently at TRL 2-3 (concept formulated / early proof of concept).

\- Design is defined but unbuilt: CIP-0113 Carbon Rights Token rules (KYC/AML, freeze-on-dispute, burn-on-retire) and the CIP-0170 Farmer Identity Credential schema are specified, but no smart contract code exists yet.

\- No testnet or mainnet deployment exists for either primitive.

\- What is already proven is the input data: live geolocation, species, farmer, and verification-photo data from 6,152 real seedlings on Hope Green's Polygon platform.

\- Technical ownership is assigned (Wesley Sousa, Head of Blockchain), building on Cardano Foundation reference implementations.

\- The 3-month grant takes this to TRL 7-8: testnet build, then mainnet mint with real institutional transactions.
