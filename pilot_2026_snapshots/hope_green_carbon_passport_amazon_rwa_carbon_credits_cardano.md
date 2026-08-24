# Hope Green Carbon Passport Amazon RWA Carbon Credits Cardano

> Turning 6,152 verified Amazon seedlings into CIP-0113 compliant carbon-credit RWA tokens, anchored by CIP-0170 farmer identity, bringing Amazon family-farmer carbon credits fully on-chain on Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1ux9es7nq4wfegwxtenvxna5ern60zvp6xtqp4lwcmh4gcsqf7j4ry`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-24T04:22:07.738000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Our team combines proven blockchain execution with Amazon field reach and a track record of monetizing this product category.

Expedito Belmont (Founder & CEO - <https://www.linkedin.com/in/expeditofernandes/>) and Marcio Pessoa (Founder & CMO - <https://www.linkedin.com/in/marcio-pessoa/>) built Hope Green from concept into an active B2B platform with paying institutional clients and recurring revenue.

Wesley Sousa (Head of Blockchain - <https://www.linkedin.com/in/wesley-sousa-e-sousa-83a5811a5/>), formerly at Greener and Sansa Labs, leads CIP-0113 and CIP-0170 integration—this is not our first blockchain implementation.

Marcelo Chamy (VP Software Engineer - <https://www.linkedin.com/in/marcelo-chamy-machado-320134/>) and Harlison Costa (UX/UI - <https://www.linkedin.com/in/harlisoncosta/>) complete our execution team.

Gabriel Maia (CIO - <https://www.linkedin.com/in/maia-gabriel/>) brings direct ties to FAEMG, SENAR, INAES and rural unions. Fabiano Nagamatsu (Advisor, Osten Move/FEA Angels/Inovativa Brasil - <https://www.linkedin.com/in/fabianonagamatsu/>) provides direct access to our largest institutional buyer, Osten BMW.

Field credibility is independently validated by Ana Paula Paiva, Forest Engineer at IDAM (<https://www.linkedin.com/in/ana-paulapaiva/>), who supported the agroforestry verification behind it.

In short: we already operate the farmer network, buyer relationships and core product this grant will extend—we are scaling a team that already delivers.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Institutional buyer (Osten BMW) mint and hold Carbon Rights Tokens as verifiable ESG/net-zero assets, then burn them upon retirement — creating a recurring annual corporate obligation. Osten already holds 1,288 NFTs under the current Polygon model, proving willingness to transact at this scale.

Family farmers receive a CIP-0170 credential once, then trigger new CRT mints as new plots or harvests are verified — tied to Hope Green’s existing annual photo-based verification cycle. This means there is no new behavior to teach, only a new chain destination for an existing habit.

The targets are reasonable but ambitious: our 2,500 CIP-0113 transactions represent converting \~800 of the 6,152 already-verified seedlings into production (\~13% of the existing base). Our 300 CIP-0170 transactions cover \~250 farmers, a credible subset of the 50,000 already mapped through our field partner (IDAM). Both targets are grounded in usage that already exists off-chain.

### How will you reach and onboard real users - and what evidence backs your channels?

We are not building acquisition channels from scratch—we are converting channels already in use.

**Buyer side:** migrate Hope Green’s existing institutional buyer, Osten BMW (already holding 1,288 NFTs), to the CRT flow as soon as it goes live on mainnet. Advisor Fabiano Nagamatsu, connected to Osten Move, provides a direct line to this buyer relationship.

**Farmer side:** onboard the 6 farmers who received the first payments from Osten and begin registering the 50,000 family farmers already mapped through our government institutional partner, IDAM.

**Evidence:** these are not prospective partnerships; they are signed pilots and an active paying customer. CIP-0170 credentials can be issued in batches as farmer onboarding progresses through these existing channels, while CRT minting is tied to the annual verification cycle already in operation—not to a new user acquisition effort.

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

Two-layer architecture matching our two selected areas.

Identity (CIP-0170, KERI-backed): each farmer gets a self-certifying Autonomic Identifier (AID) from a KERI inception event with pre-rotation. A 3-of-5 witness set (Hope Green + IDAM + neutral party) countersigns each Key Event Log entry (KERL), enabling duplicity detection. Verified plot data becomes an ACDC (KERI's verifiable credential), signed by the farmer's AID and countersigned by IDAM's; only its SAID (digest) is anchored on Cardano via CIP-0170 metadata - raw KERI state stays off-chain.

Programmable tokens (CIP-0113): a Carbon Rights Token minted per verified plot. The Plutus validator requires a valid, witnessed, non-revoked SAID before minting (Sybil resistance via identity layer), restricts receiving addresses to KYC'd wallets, allows freeze-on-dispute, and enforces burn-on-retire, preventing double counting.

Why this fits: CIP-0113 gives ledger-native compliance (KYC/AML, freeze, jurisdiction control) that institutional RWA buyers require and off-chain wrappers can't audit. CIP-0170's KERI foundation solves originator identity and Sybil resistance without a centralized farmer database, keeping custodial risk minimal - exactly what dispersed-smallholder carbon credits need.

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

Target market: institutional buyers with net-zero/ESG commitments seeking auditable, fraud-resistant carbon credits (TAM — Global: US$323M/year; SAM — Brazil: ≈R$7M/year; SOM — Amazonas: ≈US$700k/year), plus 50,000 family farmers already mapped by Hope Green, each with an average potential of 700 seedlings (TAM: 608M family farmers worldwide; SAM: 3.9M in Brazil; SOM: 330k in Amazonas).

**Demand is already proven:**

- 6,152 seedlings planted and verified across \~30 species, impacting 75 people and restoring 51 acres.
- Recurring institutional buyer: Osten BMW has acquired 1,288 NFTs.
- Approved acceleration and funding programs in the Amazon, providing institutional and corporate validation.
- Validated B2B revenue model: R$18/NFT annual subscription, 5-year contracts, with 40% of revenue going directly to family farmers.
- 60% of Amazonas’ 330,000 family farmers were affected by the historic 2023/24 drought, reinforcing urgency: this is climate-resilience income, not “greenwashing.”

Competitors ([re.green](http://re.green), Mombak, Carbonext) focus on restoring degraded land, with high entry costs and limited family-farmer inclusion. Hope Green uniquely combines traceable NFTs, active smallholder inclusion, and low entry costs. Cardano integration adds the compliance layer institutional buyers require.

### Applicant name

Btracer Hope Green

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

By the end of the 3-month window, we deliver:

1\. CIP-0113 Carbon Rights Token contract on Preview testnet: KYC/AML-gated addresses, freeze-on-dispute, burn-on-retire.

2\. CIP-0170/KERI identity layer: farmer AIDs, witnessed KEL, ACDC attestations anchored on-chain via SAID.

3\. Data bridge from Polygon verification records (geolocation, species, farmer, photos) to Cardano, piloted on a real subset of 6,152 verified seedlings.

4\. Public open-source repository for both contracts.

5\. Mainnet launch (Weeks 10-12) with a dated Week 1-2 post-launch ramp: Days 1-3, 5 CRT mints + 5 farmer credentials, 2 institutional wallets live; Days 4-7, 35 cumulative transactions, 15 farmers, 3 wallets; Week 2, \~95 cumulative transactions, 35 farmers, 4 wallets (Osten BMW, Nestle, Rumo, Hope Green treasury).

6\. Dune Analytics dashboard tracking real transactions/fees against declared targets.

7\. Demo Day showing the full flow live.

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

### Hope Green — Carbon Passport

Hope Green operates a live Payment for Ecosystem Services platform: NFTs on Polygon represent 6,152 verified saplings planted and maintained by Amazonian family farmers. We already have an institutional buyer, Osten BMW, holding 1,288 NFTs, plus a partnership with IDAM, an Amazonas government institute.

**The problem:** family farmers are key to fighting deforestation but face floods, wildfires, and droughts that can destroy up to 60% of crops. Meanwhile, companies seek credible ESG and carbon projects. Agroforestry can sequester significantly more CO₂ than conventional forests, but farmers lack funding and affordable, reliable MRV (Measurement, Reporting & Verification).

Hope Green connects both sides by financing plantations with carbon-credit potential. We already capture MRV data—geolocation, species, farmer, growth metrics, and annual verification photos—but today this remains NFT metadata, without a compliance-ready financial asset structure.

**Our solution: Carbon Passport**, built on Cardano. Each verified plot issues a programmable Carbon Rights Token (CIP-0113) with KYC/AML logic, dispute freezing, and burning upon retirement, reducing fraud and double-counting. Each farmer receives an on-chain identity (CIP-0170) linked to their plot.

Farmers gain an auditable reputation and access to the carbon market, while institutional buyers receive a traceable, compliance-ready RWA that can be securely retired on-chain.

### Supporting links (repo, site, demo)

- https://www.hopegreenagro.com/
- https://www.linkedin.com/company/b-tracer/
- https://drive.google.com/drive/folders/1lXC8xGhu3nLyWMt8ScxRtin-UDKO8vTS?usp=sharing
- https://www.youtube.com/watch?v=SQOurpCkITY
- https://www.fapeam.am.gov.br/wp-content/uploads/2026/01/Decisao-CD-061-2026-Proc.-2969.2023-53-Resultado-Final-TECNOVA-III-FAPEAM-ANEXO1.pdf

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

The Cardano integration is currently TRL 2-3 (concept formulated / early proof of concept).

Design defined but unbuilt: CIP-0113 Carbon Rights Token rules (KYC/AML, freeze-on-dispute, burn-on-retire) are specified; the CIP-0170/KERI identity layer (AID inception, witness set, ACDC attestations, SAID anchoring) is architected but no Aiken contracts or KERI witness infrastructure exist yet.

No testnet or mainnet deployment for either primitive.

Proven today is the input data only: live geolocation, species, farmer and verification-photo data from 6,152 real seedlings on Hope Green's Polygon platform.

Technical ownership assigned (Wesley Sousa, Head of Blockchain). The 3-month grant takes this to TRL 7-8: testnet build, then mainnet mint with real institutional transactions.
