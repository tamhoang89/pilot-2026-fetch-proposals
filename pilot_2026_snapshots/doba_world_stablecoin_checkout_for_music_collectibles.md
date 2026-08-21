# Doba World: Stablecoin Checkout for Music Collectibles

> Doba World lets superfans buy song-tokens with USDM. This turns Cardano into a settlement layer for independent music and generates mainnet fees.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 86
- **Proposer:** `stake1uyjvphj6hg3lf9lgq6af09ayprmdwlet2hm2avfd6vskfpg5l0u28`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-21T22:16:46.608000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Ian Njuguna is Lead Engineer & Project Manager. Responsible for end-to-end integrations, and Catalyst reporting. Doba World is live on mainnet.\
\
LinkedIn: [https://linkedin.com/in/ianonjuguna](https://linkedin.com/in/ianonjuguna%5C)\
GitHub: [https://github.com/IanoNjuguna](https://github.com/IanoNjuguna%5C)\
\
No third-party security audit is budgeted or contracted. Review will be internal, plus preprod/mainnet testing and a test-evidence bundle.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who:** Super fans purchasing song-tokens from independent artists.

**Why:** Early access, exclusive collectibles, and a direct relationship with artists.

**How Often:** Each purchase contains generates fees in two ways: USDM transfer, and song-token mint. The conservative baseline needs doba to get 110 users to make 4 transactions each, and assuming the average network fee is ₳0.30 to ₳0.45, doba will generate network fees &gt;₳330.

```markdown
| Source                           |Wallets|
|----------------------------------|-------|
| Artist drops (3 or more)         | 40–60 |
| Micro-CAC + Gimba Labs community | 35–50 |
| Organic                          | 20–35 |
| **Total**                        | ~110**|
```

**Funnel:** 1,000 artists contacted → 100 replies → 10 drops → 2,000 fans reached → 200 wallet connects → 110 buyers → 220 transactions.

**USDM acquisition:** Via Mehen, Minswap/WingRiders, or P2P.

**Rhythm:** one entry-epoch ramp plus six floored 5-day epochs. Epoch floors \~₳27.50 in the first three epochs, \~₳55 in the final three. First drop within the first epoch.

**Integrity:** Team wallets declared; no fee subsidies or rewards.

### How will you reach and onboard real users - and what evidence backs your channels?

1. **The Gimba Labs community.** The connection made with builders during the Piece of Pie hackathon provides a native audience of pioneer adopters who can test the flow and provide feedback during the build phase.
2. **Artist outreach.** Target &gt;1000 phonk and EDM artists via Reddit, cold email, and direct messages in the first month to get &gt;100 to drop during the adoption window. Super fans in tech-forward genres are a fit for crypto culture.
3. **Kick streams + clipped content.** Biweekly live streams with artist drops and Q&A, clipped into YouTube Shorts, Instagram Reels, and TikTok. This builds organic reach that compounds conversion in the long term.

**First two weeks:**

***Week 1:*** Contact 200 artists; post in 5 communities; 2 livestreams | 40 replies, 4 calls, 100 new community members.\
***Week 2:*** Follow up; finalize first drop; launch micro-CAC | 1 committed drop, 150 page visits, 30 wallet connections.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Streaming, Bandcamp, Patreon, Kickstarter, and music-NFT platforms take meaningful cuts and none settles on Cardano. Doba is the first federated music-token-collectible protocol; integrations are open-sourced under AGPL v3.

### Please provide details about the Technology Readiness Level selected for your existing product

**Doba** is a live platform deployed on the Cardano mainnet to facilitate music pre-drops. The platform enables fans to connect and discover upcoming music drops, and purchase tokenized song assets directly on-chain. So far, doba has an organic user base spanning three continents.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Doba is building an Open Source self-custody music checkout.\
\
The architecture:

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

Independent phonk, and EDM artists and their superfans. Direct-to-fan research shows the top 5–10% of an creative's audience generate the majority of creator income on platforms like Patreon and Bandcamp.

A pre-drop is a music token collectible minted using doba world smart contracts. It is a [research-backed](https://doba.world/research) strategy shift in direct artist-to-fan engagement that moves toward selling *scarce digital collectibles with early access & community status* upfront to super fans.

One hundred superfans buying a $5 song token generate $500 immediately, you would need roughly 125,000 Spotify streams to match this motion.

### Applicant name

Ian Njuguna

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Doba takes a fee on song-token sales. This funds ongoing platform development, artist support and community growth.

After the pilot, artist drops, repeat purchases, and secondary trading will sustain activity on the protocol.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding enables Doba to build, audit, and deploy the USDM checkout integration on Cardano mainnet while driving initial artist-led adoption.

**Budget Allocation:**

- **₳9,000** - onchain USDM integration

- **₳8,000** - check-out and USDM acquisition UX

- **₳3,000** - Telemetry and Metadata tracking

- **₳2,000** - Deployment operations

- **₳7,000** - Legal & compliance

- **₳9,000** - Artist acquisition & outreach

- **₳5,000** - Micro-CAC marketing experiments

- **₳2,000** - Project management & Catalyst reporting

- **₳5,000** - Contingency

**Total: ₳50,000**

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

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Independent musicians get paid last and least by streaming platforms. On Cardano, asking a non crypto-native superfan to buy a song-token means asking them to think in ADA and absorb volatility. This friction kills the sale.

With USDM checkout, a fan sees a $5 song-token price, pays from their wallet, and receives a collectible that unlocks early access and community perks. Cardano gains a consumer use case that brings real people to mainnet.

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

220

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

330

### Current funded commitments

Ian Njuguna is a maintainer for DevEx repository under Intersect's Maintainer Retainer Program. The role is scoped to FOSS developer-experience maintenance and does not overlap with the Doba stablecoin integration build, timeline, or adoption activities. Details of the commitment will be disclosed during Catalyst onboarding. 

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The USDM checkout integration has been designed and its feasibility is confirmed by Doba's existing minting, dapp connector, and on-chain transaction infrastructure. No USDM-specific experimental proof of concept has been completed at submission. The funded work will build the TRL 3 to 4 proof of concept on preprod, and deliver the TRL 5+ mainnet integration. Declaring TRL 2 reflects this honest status and avoids claiming validation that does not yet exist.
