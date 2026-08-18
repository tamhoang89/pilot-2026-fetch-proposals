# doba world USDM Checkout for Collectibles

> Stablecoin checkout for collectible tokens on Cardano. Payments via USDM. Pricing via Pyth.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 33
- **Proposer:** `stake1uyjvphj6hg3lf9lgq6af09ayprmdwlet2hm2avfd6vskfpg5l0u28`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-18T16:55:15.864000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

**Ian Njuguna Chege** (publicly Ian Njuguna) is the liable delivery owner in product, strategy & engineering.\
\
*SOCIALS:*

(<https://www.linkedin.com/in/ianonjuguna/>),

(<https://github.com/IanoNjuguna>)          \
\
The existing doba world product is the strongest capability evidence. It is live on Cardano mainnet at \[[app.doba.world](http://app.doba.world)\], with wallet connection, native-asset minting (song tokens), and on-chain purchase of song tokens. Ian deployed this product to mainnet during the Gimba Labs Piece of Pie hackathon and has been iterating on it since  

The GitHub repository at [\[github.com/IanoNjuguna/bookish-worm\]](http://github.com/IanoNjuguna/bookish-worm%5D\(https://github.com/IanoNjuguna/bookish-worm\)) is the source for developers and reviewers. It  contains the platform code under an open-source license; production configuration, credentials, and signing material are excluded.

This proposal will build on proven infrastructure. The funded work adds:

- USDM policy allowlisting.
- Pyth ADA/USD price feed consumption inside the purchase smart contract.
- multi-asset transaction construction, checkout UX quoting in USDM.
- in-app USDM acquisition guidance, and
- Dune Analytics tagging.

Ian will complete Catalyst identity verification and sanctions screening.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

null

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who:** Super fans purchasing song-tokens from independent artists.

**Why:** Fans gain early access, exclusive collectibles, and a direct relationship with artists devoid of price action FUD.

**How Often:** Target of 2 transactions per paying wallet across the adoption window: initial song-token purchase plus a repeat purchase or secondary market transaction.

**Target Metrics:** 110 paying wallets × 2 transactions × 3 fee-generating steps × ₳0.50 average fee = **₳330 total transaction fees generated**.

**Feasibility & Alignment:** This target sits comfortably above the ₳180 minimum threshold and within the Credible guidance band (₳300–550) for a ₳50,000 Catalyst Stablecoins proposal.

**USDM Acquisition:** We will implement a USDM on-ramp so artists and super fans don't leave the app to source for USDM prior to checkout. Doba provides direct, in-app onboarding guidance.

**Integrity Guarantee:** Only authentic, non-custodial external user activity will be counted. Doba will explicitly declare all team-controlled wallets, will not subsidize transaction fees, and will not issue financial rewards for user activity, ensuring full compliance with the Transaction Integrity Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

1. **The Gimba Labs community.** The connection we made with builders during the Piece of Pie hackathon provides a native audience of pioneer adopters who can test the flow and provide feedback.
2. **Artist outreach (funded, no LOIs at submission).** Target &gt;100 phonk and EDM artists via Reddit, cold email, and direct messages in the first month to get &gt;3 committed artists for the first drop within two weeks of M1, scaling to &gt;10 during the adoption window. We will provide hands-on setup support to each committed artist.
3. **Customer Acquisition on TikTok.** Run paid and organic A/B campaigns targeting phonk and EDM listeners. We start with ₳500 tests, and double down on viral hits exclusive to doba world. TikTok is the primary discovery channel for these genres.
4. **Kick streams + clipped content.** Biweekly live streams with artist drops and Q&A, clipped into YouTube Shorts, Instagram Reels, and TikTok. This builds organic reach and social proof, not direct conversions.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Artists use streaming, Bandcamp, Patreon, Kickstarter, and various other centralized platforms. Each takes a meaningful cut and none of the decentralized alternatives settle on Cardano.

doba world is the first to apply a federated approach to music pre-drops. This is a consumer vertical with built-in viral distribution and all integrations done in this pilot will be open-sourced under the AGPL v3 license.

We generate higher network fee density per transaction. Each purchase contains three fee-generating steps: Pyth price validation, USDM transfer & a song-token mint. This is impossible in single-step stablecoin settlements typical in payment rails.

### Please provide details about the Technology Readiness Level selected for your existing product

**doba world** is a live platform deployed on the Cardano mainnet to facilitate music pre-drops. The platform enables fans to connect and discover upcoming music drops, and purchase tokenized song assets directly on-chain. So far, doba world has an organic user base spanning three continents.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Doba is a self-custody music checkout. The architecture:

```
Super Fan (with USDM balance)
    ↓
Pyth ADA/USD price feed (`0x2a01deaec9e51a579277b34b122399984d0bbf57e2458a7e42fecd2829867a0d`)
    ↓
USDM transfer to Doba contract
    ↓
Song-token mint to fan wallet
```

Each purchase contains three fee-generating steps: Pyth price validation, USDM transfer, and song-token mint. 

The smart contract only accepts the verified USDM policy from [cardano.org](http://cardano.org): `c48cbb3d5e57ed56e276bc45f99ab39abe94e6cd7ac39fb402da47ad` (asset name hex `0014df105553444d`). 

Every counted transaction carries the standardized Catalyst metadata label.

This fits the Stablecoins Area of Interest because it moves verified stablecoin policies on mainnet through real, user-paid transactions.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Direct-to-fan research shows the top 5–10% of an creative's audience generate the majority of creator income on platforms like Patreon and Bandcamp.

A pre-drop on doba world is a [research-backed](https://doba.world/research) strategy shift in direct artist-to-fan engagement that moves toward selling *scarce digital collectibles with early access & community status* upfront to super fans.

One hundred superfans buying a $5 song token generate $500 immediately, you would need roughly 125,000 Spotify streams to match this motion. For an independent musician releasing records every few weeks, cash flow and income from royalties is a life-and-death matter.

### Applicant name

Ian Njuguna

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

doba world takes a fee on song-token sales. This funds ongoing platform development, artist support and community growth. doba world does not subsidize or reward transactions.

After the pilot, artist drops, repeat purchases, and secondary trading will sustain activity on the protocol.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding enables Doba to build, audit, and deploy the USDM checkout integration on Cardano mainnet while driving initial artist-led adoption.

**Budget Allocation:**

- **₳9,000** - USDM & Pyth integration

- **₳8,000** - Security review and audits

- **₳3,000** - Telemetry & Metadata tagging

- **₳2,000** - Deployment operations

- **₳7,000** - Legal & compliance

- **₳9,000** - Artist acquisition & outreach

- **₳5,000** - Micro-CAC marketing experiments

- **₳2,000** - Project management & Catalyst reporting

- **₳5,000** - Contingency

**Total: ₳50,000**

*Note: Budget explicitly excludes liquidity provision, user rebates, promotional giveaways, and retroactive costs.*

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

A. **USDM & Pyth Integration:** On-chain and off-chain transaction-building logic deployed to mainnet, configured to validate the verified USDM policy ID and consume real-time Pyth Network ADA/USD price feed data.

B. **Frontend Checkout UX & Guidance:** Production UI deployed at the live Doba web domain, to enable USDM at checkout, and real-time conversion.

C. **On-Chain Telemetry & Footprint Registration:** Integration of standardized metadata labels into every checkout transaction per the Proof of Adoption & Standard.

D. **Security Audit & Codebase Documentation:** Completed security audit report covering USDM checkout contracts, accompanied by an open-source GitHub repository.

E. **Demo Day Presentation & Live Testing:** E2E mainnet transaction tests on a live environment, yielding valid transaction hashes across all steps (Pyth price validation, USDM transfer, and song-token mint).

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Independent musicians release music into a system that pays them last and least. Streaming platforms can take long to approve a track, then return fractions of a cent per stream after months because of outdated bureaucratic processes. And not all artists qualify for these payouts :(

All settlement on doba world is finalized on Cardano, but requiring a non-crypto native super fan to collect these tokens means *asking them to think in ADA, and price action volatility*. **Friction kills the sale**. Stablecoin settlements feel more natural in this regard.

With a USDM checkout released under the AGPL v3 license. Super fans will see a $5 song-token price in USDM, pay from their wallet, and receive a song-token that unlocks community perks. Pyth will provide us with live ADA/USD price feeds for use in the purchase smart contract.

### Supporting links (repo, site, demo)

- https://doba.world
- https://app.doba.world
- https://github.com/IanoNjuguna/bookish-worm
- https://x.com/gimbalabs/status/2067996074661314904
- https://x.com/doba_DAO/status/2089326796504232384

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

doba world is an **AGPL v3** licensed, federated protocol where anyone can iterate on the code but they must share improvements so artists and their communities benefit from a network effect. In web2, this model has made Mastodon resilient.

The USDM checkout integration will also be published under the **AGPL v3 license** in a public GitHub repository and will remain open source for the full project life cycle.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

220

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

330

### Current funded commitments

Ian Njuguna is a maintainer for DevEx repository under Intersect's Maintainer Retainer Program. The role is scoped to FOSS developer-experience maintenance and does not overlap with the Doba stablecoin integration build, timeline, or adoption activities. Details of the commitment will be disclosed during Catalyst onboarding. 

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The USDM checkout integration architecture is fully designed. Implementation comprises six core deliverables:

- **Policy Allowlisting:** Integrating the USDM policy ID into the smart contract and frontend filters to validate genuine USDM tokens during checkout.

- **Oracle Consumption:** Integrating the Pyth Network pull-oracle to ingest real-time price feeds and dynamic conversion rates for multi-asset pricing.

- **On-Chain Analytics:** Tagging checkout transactions via standardized metadata formats for indexing on Dune Analytics dashboards.

- **Mainnet Deployment:** Executing testnet end-to-end testing prior to deploying updated smart contracts and off-chain transaction builders.
