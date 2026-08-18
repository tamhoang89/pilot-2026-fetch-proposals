# LendADA: ADA Pooled Lending with USDCx, USDM & Pyth

> Launch separate, audited ADA-collateral lending markets for USDCx and USDM, using signed Pyth price data and conservative risk controls.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 21
- **Proposer:** `stake1u9k6f967jnq3jn766k8x9jznqd0mx99hsep0yqksupx6jksynrqzt`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-18T15:06:03.557000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

LendADA is delivered by a focused two-person technical team that has already built the working Cardano Preprod MVP.

**Jaromír Tesař — frontend, backend and delivery lead**\
Jaromír builds the user-facing application and wallet flows, and is responsible for backend services, batcher and infrastructure, oracle-update integration, indexer/API, monitoring, deployment, release coordination and Catalyst reporting.

Links: <https://github.com/Satuchac> | <https://www.linkedin.com/in/jaromir-tesar-43b59817a/>

**Martin Miksaník — Aiken smart-contract developer**\
Martin is responsible for Aiken/Plutus V3 validators, pooled-market accounting, collateral and liquidation rules, USDCx/USDM market configuration, Pyth transaction validation, test coverage and audit remediation.

Link: <https://www.linkedin.com/in/martin-miksanik/>

The team has delivered a functional Preprod product: supply, withdrawal, borrowing, repayment, collateral management, position health, liquidations and batch settlement are operational and under active testing. Work is bounded to ADA collateral lending with separate USDCx/USDM asset accounting and an independent audit before mainnet. The external security reviewer will be independent of the delivery team.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Counted activity will come only from external wallets using the live mainnet product. Team, related-party, team-funded, relay, batcher and keeper wallets are excluded.

The forecast is 600 oracle-consuming lending actions and 800 actions moving verified USDCx or USDM. The targets assume approximately 0.83 ADA for a Pyth-consuming risk transaction and 0.75 ADA across stablecoin actions. A user transaction that consumes the declared Pyth feed and moves a declared stablecoin is eligible under each declared integration footprint; it is not artificial activity.

Initial usage will come from experienced Cardano DeFi suppliers and borrowers reached through public documentation, walkthroughs, team channels and fixed-scope educational campaigns. The target is 100 distinct external wallets, including at least 30 suppliers and 30 borrowers, with repeat supply, borrow, repayment and withdrawal activity. Users continue because suppliers earn variable interest and ADA holders obtain stablecoin liquidity without selling ADA.

No deposit, borrowing, transaction or token incentive will be offered.

### How will you reach and onboard real users - and what evidence backs your channels?

LendADA will use a product-led launch backed by fixed-scope education, not user incentives. I will use my Cardano X account, @jaromirtesar, to publish the audit release, walkthroughs, and launch notice.

₳10,000 of the budget is reserved for at least one, but ideally two or more Cardano creator campaigns. Each delivers a lending walkthrough, X post/thread with tagged landing-page link, and live Q&A or recorded FAQ. Payment is for content and distribution only; never deposits, borrowing or transactions.

Week 1: open capped supply and borrowing, run two onboarding sessions, and target 25 external wallets (10 suppliers, 10 borrowers) and 75 eligible transactions.

Week 2: publish the campaigns, run the public Q&A, onboard a second cohort, and target 50 cumulative external wallets (20 suppliers, 20 borrowers), 10 borrow-repay cycles and 200 eligible transactions.

The full-window target is 100 external wallets. Team, related-party and team-funded wallets are excluded.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/93hxjrrKIMc

### Who else solves this today - competitors/alternatives, and why does your approach win?

Liqwid is the closest direct competitor: a pooled lending protocol with multi-asset markets. Surf and Lenfi V2 also offer pooled lending. Danogo offers fixed and flexible pools. FluidTokens combines liquidity pools with P2P and NFT-collateral lending.

LendADA does not claim that pooled lending, utilisation-based rates or liquidations are new. It competes through separate ADA-collateral markets for USDCx and USDM, signed Pyth data in risk-sensitive transactions, strict oracle checks, published caps, no origination or repayment fee, and an independent review of its Aiken/Plutus V3 contracts before launch.

The capped beta will test whether users value this combination of stablecoin access, transparent controls and a distinct implementation.

### Please provide details about the Technology Readiness Level selected for your existing product

LendADA meets TRL 6 because it is demonstrated end-to-end in Cardano Preprod. The public application shows pool state, utilisation, interest curves, position health, and liquidations.

Using internal test wallets and test assets, the team has completed supply and withdrawal, ADA collateral management, borrowing and repayment, utilisation-based interest accounting, health-factor calculation, liquidations and permissionless batch settlement. The batcher, indexer/API, dashboard, test oracle and liquidation tooling are functional and under active testing.

The product is not yet TRL 7: it has no production USDCx/USDM or Pyth integration, no independent security audit, no mainnet deployment, and no external customers. These gaps are the purpose of this proposal.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

LendADA is an eUTxO pooled-lending protocol in Aiken/Plutus V3. A singleton Pool UTxO holds per-asset accounting for every market (ADA and tUSD live; USDCx/USDM planned): supply/debt totals, dual interest indices and utilisation. A position UTxO holds a user's collateral, debt and state; positions are cross-collateralised, ADA collateral backs stablecoin borrowing, each asset accounted separately. Manager authority is limited to risk parameters, market caps and emergency pauses. It cannot take custody.

Validators bind each asset's declared policy ID and asset name. Supply, withdrawal, borrowing, repayment and liquidation must satisfy balance, interest-accrual, LTV, liquidation-threshold and cap rules on-chain.

For risk-sensitive actions, an off-chain relay fetches a signed Pyth ADA/USD price and posts it to a platform Oracle UTxO validators read as a reference input. On-chain, LendADA enforces freshness (bound to the transaction validity range), a positive price and a staleness limit before valuing collateral and health. Stale or invalid data blocks borrowing, collateral withdrawal and liquidation; repayment and adding collateral stay available. 

This fits Cardano because asset identity, solvency and state changes are enforced atomically. A batcher or keeper can build a transaction but cannot bypass validators or custody funds.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The initial market is Cardano DeFi users on both sides of the market: ADA holders seeking USDCx or USDM liquidity without selling ADA, and stablecoin holders seeking non-custodial yield. It also targets experienced liquidators.

There is proven category demand, but not yet LendADA product-market fit. As of 18 August 2026, DefiLlama reports approximately $12.4m TVL for Liqwid, $3.32m for Surf Lending and $2.18m for FluidTokens. These protocols demonstrate that Cardano users supply assets, borrow against collateral and pay network fees for lending activity. Circle’s USDCx integration brings USDC-backed cross-chain liquidity to Cardano and explicitly identifies lending and borrowing as a use case.

LendADA currently has no external customers. All Preprod use is internal testing. We will therefore measure product-level demand through external, independently funded activity: distinct suppliers and borrowers, supplied USDCx/USDM, ADA collateral, borrow–repay cycles, repeat users and average utilisation. Team and related-party wallets will be declared and excluded from adoption results.

The capped launch is deliberately designed to validate demand safely rather than assume it. USDCx and USDM will use per-asset accounting, allowing the team to compare real usage and liquidity preference while maintaining transparent asset-level parameters.

### Applicant name

Jaromír Tesař

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Borrowers pay variable interest based on each market’s utilisation. Most interest goes to USDCx and USDM suppliers; an audited protocol reserve share finances data access, infrastructure, monitoring, security maintenance, incident response and support. Liquidation penalties compensate independent liquidators and replenish the reserve. There are no loan-origination or repayment fees.

Users remain because suppliers can earn utilisation-based yield and ADA holders can access stablecoin liquidity without selling collateral. Revenue is earned only when there is genuine outstanding borrowing; the project will not use grant-funded liquidity mining, transaction rebates or artificial activity.

Before launch, LendADA will publish its revenue, reserve and operating-risk policy.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without Catalyst funding, LendADA can continue internal Preprod testing but cannot responsibly complete production USDCx/USDM and Pyth integration, an independent security audit. The MVP is not ready for user funds.

High-level allocation:

• ₳55,000 — USDCx/USDM integration, Pyth validation, risk controls and contract hardening.\
• ₳80,000 — independent audit and remediation.\
• ₳25,000 — batcher, keeper, monitoring, indexer/API and infrastructure.\
• ₳20,000 — frontend, testing, deployment and release work.\
• ₳10,000 — documentation, beta support and Catalyst reporting.\
• ₳10,000 — fixed-scope creator education, launch outreach and public Q&As.

Funding is only for future delivery: no protocol liquidity, loans, token rewards, transaction rebates or incentives.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, LendADA ships a capped Cardano mainnet beta, hardening the protocol live on Preprod:

• ADA collateral vs a production stablecoin (USDM/USDCx) via verified policy IDs; per-asset accounting, interest, LTV, liquidations, caps and emergency pause enforced on-chain.

\
• Guardian-verified Pyth ADA/USD posted to an on-chain Oracle UTxO (reference input); validators enforce freshness, positive price and staleness; stale data blocks borrow/withdrawal/liquidation while repay and add-collateral stay available. Trustless on-chain Pyth (feed-ID/confidence) follows.

\
• Published caps, risk parameters, script hashes and addresses.

\
• Kupo indexer/API, dashboard, docs and risk guide on a hardened backend.

• Independent security audit, fixes and regression tests, on four internal rounds.

**Evidence**: live mainnet URL, audit report, tx hashes from external-user supply/withdraw and ADA borrow/repay, plus a Demo Day walkthrough.

### Oracles - expected transaction count

600

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

ADA holders often need dollar liquidity without selling their long-term position, while stablecoin holders need transparent, non-custodial ways to earn yield. Cardano lending remains concentrated in a few protocols, limiting choice in market design, risk controls and operating models.

LendADA is a non-custodial pooled lending protocol. Users will supply USDCx or USDM and earn variable interest, or deposit ADA as collateral and borrow a stablecoin. USDCx and USDM will use separate per-asset accounting, utilisation, interest indices, caps and risk parameters. ADA collateral backs stablecoin borrowing.

A working Cardano Preprod MVP already supports supply and withdrawal, borrowing and repayment, collateral management, utilisation-based rates, position-health tracking, liquidations and permissionless batch settlement. It can be inspected at <https://morfeus.176-102-64-240.sslip.io/>. The deployment uses test assets. It has no external customers and has not been independently audited.

The project will integrate mainnet USDCx and USDM asset policies and signed Pyth ADA/USD data, add strict oracle checks and monitoring, complete an independent security review, and launch a conservatively capped mainnet beta. Grant funding covers this future integration, audit, remediation, deployment and user education, not protocol liquidity, loans, transaction rebates or user incentives.

### Supporting links (repo, site, demo)

- https://github.com/Satuchac?tab=repositories
- https://www.linkedin.com/in/jaromir-tesar-43b59817a/?enhance=null
- https://morfeus.176-102-64-240.sslip.io/
- https://drepdao.176-102-64-240.sslip.io/?view=overview

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

500

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

800

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

600

### Current funded commitments

**Jaromir Tesar**

Cardano Catalyst Fund14: DRep DAO platform - Project ID: #1400048

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed integration is TRL 2: its architecture and delivery scope are defined, but production components are not yet implemented or validated.

LendADA already has a Preprod lending MVP: isolated market accounting, ADA collateral, borrowing, repayment, interest, health checks, liquidations and batch settlement work with test assets and an internal oracle.

The new work is separate USDCx and USDM markets with verified mainnet asset policies; signed Pyth ADA/USD data in risk-sensitive transactions; freshness, confidence and fail-safe checks; monitoring, documentation, independent audit and remediation.

There is no production USDCx/USDM or Pyth integration, audit or mainnet deployment today. The proposal funds the path to a conservatively capped mainnet beta.
