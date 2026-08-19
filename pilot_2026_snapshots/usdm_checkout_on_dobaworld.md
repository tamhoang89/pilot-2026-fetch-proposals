# USDM checkout on doba.world

> An open-source stablecoin settlement rail built for Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 70
- **Proposer:** `stake1uyjvphj6hg3lf9lgq6af09ayprmdwlet2hm2avfd6vskfpg5l0u28`
- **Funding requested:** ₳80,000
- **Last finalized:** 2026-08-19T20:53:13.932000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

**Core Lead & Execution:**

- **Ian Njuguna Chege (Lead Engineer & Project Manager):** Ian brings end-to-end technical execution and dApp architecture capabilities across the Cardano stack. As the sole proposer, Ian is responsible for the smart contract development (Aiken), off-chain transaction orchestration, USDM integration, overall project management and Catalyst milestone reporting.

  - **LinkedIn:** [linkedin.com/in/ianonjuguna](http://linkedin.com/in/ianonjuguna)

  - **GitHub:** [github.com/IanoNjuguna](http://github.com/IanoNjuguna)

**Third-Party Security & External Vendor:**

- **Subcontracted Security Auditor:** To ensure protocol safety and mitigate eUTxO-specific vulnerabilities prior to Mainnet launch, a security vendor (e.g. TxPipe, MLabs, Anastacia Labs) will be contracted to perform an independent, comprehensive smart contract security review. .

  - *Vendor Status Disclaimer:* not a co-proposer, or partner.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who:** Super fans purchasing song-tokens from independent artists.

**Why:** Fans gain early access, exclusive collectibles, and a direct relationship with artists devoid of price action FUD.

**How Often:** A target of &gt;500 monthly average users during the adoption window. This is a requisite deliverable for doba world to hit the fee target. Artist drops will be staggered to maintain continuous transaction velocity without single-day spikes exceeding standard limits.

**Target Metrics:** This target sits above the ₳180 minimum threshold and within the guidance band (₳300–550).

**USDM Acquisition:** Doba world will need external support through Moneta Global's on-ramp APIs so artists and super fans can mint USDM from fiat in the app.

**Integrity Guarantee:** Only authentic, non-custodial external user activity will be counted. Doba will explicitly declare all team-controlled wallets, will not subsidize transaction fees, and will not issue financial rewards for user activity, ensuring full compliance with the Transaction Integrity Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

1. **The Gimba Labs community.** The connection made with builders during the Piece of Pie hackathon provides a native audience of pioneer adopters who can test the flow and provide feedback during the build phase.
2. **Artist outreach.** Target &gt;1000 phonk and EDM artists via Reddit, cold email, and direct messages in the first month to get &gt;100 to drop during the adoption window. Super fans in tech-forward genres are a fit in crypto culture even when not native to it.
3. **Kick streams + clipped content.** Biweekly live streams with artist drops and Q&A, clipped into YouTube Shorts, Instagram Reels, and TikTok. This builds organic reach that compounds conversion in the long term.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Artists use streaming, Bandcamp, Patreon, Kickstarter, and various other centralized platforms. Each takes a meaningful cut and none of the decentralized alternatives settle on Cardano.

doba world is the first to apply a federated approach to music token collectibles. This is a consumer vertical with built-in viral distribution and all integrations done in this pilot will be open-sourced under the AGPL v3 license.

### Please provide details about the Technology Readiness Level selected for your existing product

**doba world** is a live platform deployed on the Cardano mainnet to facilitate music pre-drops. The platform enables fans to connect and discover upcoming music drops, and purchase tokenized song assets directly on-chain. So far, doba world has an organic user base spanning three continents.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Doba is a self-custody music checkout. The architecture:

```
Super Fan (with USDM balance)
    ↓
USDM transfer to Doba contract
    ↓
Song-token mint to fan wallet
```

Each purchase contains generates fees in two ways: USDM transfer, and song-token mint.

The smart contract only accepts the verified USDM policy from [cardano.org](http://cardano.org): `c48cbb3d5e57ed56e276bc45f99ab39abe94e6cd7ac39fb402da47ad` (asset name hex `0014df105553444d`).

Every counted transaction will carry the standardized Catalyst metadata label.

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

A pre-drop is a music token collectible minted on doba world smart contracts. This is a [research-backed](https://doba.world/research) strategy shift in direct artist-to-fan engagement that moves toward selling *scarce digital collectibles with early access & community status* upfront to super fans.

One hundred superfans buying a $5 song token generate $500 immediately, you would need roughly 125,000 Spotify streams to match this motion. For an independent musician releasing records every few weeks, cash flow and income from royalties is a life-and-death matter.

### Applicant name

Ian Njuguna

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

doba world takes a fee on song-token sales. This funds ongoing platform development, artist support and community growth.\
\
doba world does not subsidize or reward transactions.

After the pilot, artist drops, repeat purchases, and secondary trading will sustain activity on the protocol.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding enables Doba to build, audit, and deploy the USDM checkout integration on Cardano mainnet while driving initial artist-led adoption.

**Budget Allocation:**

- **₳9,000** - USDM integration

- **₳38,000** - Third party Security review and audits

- **₳3,000** - Telemetry and Metadata tracking

- **₳2,000** - Deployment operations

- **₳7,000** - Legal & compliance

- **₳9,000** - Artist acquisition & outreach

- **₳5,000** - Micro-CAC marketing experiments

- **₳2,000** - Project management & Catalyst reporting

- **₳5,000** - Contingency

**Total: ₳80,000**

*Note: all marketing allocations (₳9,000 artist outreach and ₳5,000 micro-CAC experiments) are dedicated exclusively to top-of-funnel user discovery, artist onboarding, and organic campaign production.*

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

A. **USDM Integration:** On-chain and off-chain transaction-building logic deployed to mainnet, configured to validate the verified USDM policy ID.

B. **Frontend Checkout UX & Guidance:** Production UI deployed at the live Doba web domain, to enable USDM at checkout, and real-time conversion.

C. **On-Chain Telemetry & Footprint Registration:** Integration of standardized metadata labels into every checkout transaction per the Proof of Adoption & Standard.

D. **Demo Day Presentation & Live Testing:** E2E mainnet transaction tests on a live environment, yielding valid transaction hashes across all steps.

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

With a USDM checkout released under the AGPL v3 license. Super fans will see a $5 song-token price in USDM, pay from their wallet, and receive a song-token that unlocks community perks.

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

Doba world, also known as Doba is an **AGPL v3** licensed protocol where anyone can iterate on the code but they must share improvements so artists and their communities benefit from a network effect. In web2, this federated model has made Mastodon resilient.

The USDM checkout integration will also be published under the **AGPL v3 license** in a public GitHub repository and will remain open source for the full project life cycle.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

330

### Current funded commitments

Ian Njuguna is a maintainer for DevEx repository under Intersect's Maintainer Retainer Program. The role is scoped to FOSS developer-experience maintenance and does not overlap with the Doba stablecoin integration build, timeline, or adoption activities. Details of the commitment will be disclosed during Catalyst onboarding. 

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Implementation comprises the following deliverables:

- **Policy Allowlisting:** Integrating the USDM policy ID into the smart contract and frontend filters to validate genuine USDM tokens during checkout.

- **On-Chain Analytics:** Tagging checkout transactions via standardized metadata formats for indexing on Dune Analytics dashboards.

- **Mainnet Deployment:** Executing testnet end-to-end testing prior to deploying updated smart contracts and off-chain transaction builders.
