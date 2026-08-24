# Multi-Source Chorus Aggregation for Cardano

> One standard interface, many chorus sources verified on-chain, per transaction.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 29
- **Proposer:** `stake1uxps8zkp98wtp77cnzl0g6eya50qf4svjn03l78klhvyfts46n73h`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-24T02:29:26.428000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Our team has hands-on experience building Cardano DeFi infrastructure, including smart contracts, off-chain services, indexers, backend systems and Oracle integrations. We have already implemented and tested the Oracle architecture on Cardano Preprod, with real transactions covering loan creation, repayment and liquidation.

Phan Phung Hai previously served as Project Lead for Nio, a Fund12-funded Cardano DeFi investment tracking application that was successfully completed. His work included on-chain transaction monitoring, DeFi protocol integration and analysis of assets locked in Cardano smart contracts.

Team roles:

- **Phan Phung Hai — Project Lead / Product & Integration**\
  Responsible for project delivery, Oracle architecture coordination, protocol integration, adoption tracking and developer outreach.\
  <https://www.linkedin.com/in/hairphan/>
- **Truong Quang Chu — Smart Contract Engineer**\
  Responsible for Aiken and Plutus smart contracts, aggregation validator implementation, source integration, on-chain testing and deployment.\
  <https://www.linkedin.com/in/truongquangchu/>
- **Nguyen Thi Kim Chi — Backend & Off-chain Engineer**\
  Responsible for indexers, backend services, source adapters, monitoring, SDK support and off-chain integration.\
  <https://www.linkedin.com/in/chi-nguyen-773871288>

The team has experience with Plutus and Aiken, testnet and mainnet deployments, external price feeds, aggregation logic, indexers and production backend systems.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Dano Finance is the anchor source of real user activity. Cardano’s public app directory recorded **6,340 Dano Finance on-chain transactions in the latest 30-day snapshot**. Our target of 1,125 Oracle-consuming transactions represents about **17.7%** of that existing monthly activity.

Only price-dependent Lending V2 actions will execute Chorus, so we do not assume every Dano transaction will count. Relevant flows include borrowing, collateral valuation, repayment flows requiring revaluation and liquidation checks.

Target assumptions:

- 1,125 external Oracle-consuming transactions
- 45 distinct external wallets
- \~0.80 ADA average network fee
- 900 ADA counted fees

Week 1 targets are 150 transactions and 20 wallets. Week 2 cumulative targets are 300 transactions and 30 wallets. Activity will then be tracked against per-epoch floors and the daily cap toward the final target.

Fees are paid by end users. We neither sponsor nor receive them.

### How will you reach and onboard real users - and what evidence backs your channels?

Our users are protocols, not retail wallets, so onboarding focuses on developer experience and direct protocol integration.

Dano Finance is the anchor integration. Dano has publicly committed that Lending Smart Contract V2 will use Chorus for all collateral valuation and liquidation checks from launch: <https://docs.dano.finance/news/lending-v2-will-price-your-collateral-from-many-sources-not-one>

Dano already has measurable mainnet activity. Cardano’s public app directory recorded **6340 Dano Finance on-chain transactions in the latest 30-day snapshot**. Our final target of 1125 Oracle-consuming transactions is about 18% of that existing activity, although only price-dependent Lending V2 actions will count.

**Week 1 target:** 150 Oracle-consuming transactions, 20 external wallets and about 120 ADA in counted fees.

**Week 2 cumulative target:** 300 transactions, 30 external wallets and about 240 ADA in counted fees, plus direct outreach to at least 3 additional Cardano DeFi teams.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The main alternatives are individual oracle providers or integrating a single source directly. Charli3, Orcfax, Pyth, and DEXs such as Minswap, SundaeSwap, and Splash are not competitors; they are the sources we aggregate.

Today, protocols either depend on one source or build aggregation themselves, repeating the same work: adapters, freshness checks, deviation rules, fallback logic, and maintenance.

Our advantage is a shared aggregation layer with one standard interface. A protocol integrates once and can use multiple current and future sources, with price validation performed inside its own transaction instead of relying on a trusted external publisher.

### Please provide details about the Technology Readiness Level selected for your existing product

The technology has been validated in a relevant Cardano testnet environment. SC have been deployed and tested on Preprod, with Liqwid integrations implemented for retrieving and validating on-chain price data.

Oracle Script Hash on Preprod: `3158c9a7ba551eb3b6b9aa578e7995dec5ce34e272fde0bda76b46d1`

\
Create Loan: <https://preprod.cardanoscan.io/transaction/66cc67785fb786173118241ed230a24b7ea6f4f7103082fc62eceab7e95c834b>\
Repay Loan: <https://preprod.cardanoscan.io/transaction/5e20812df32068bd7b5571a1c1af3966b368b7addd1be260e54977ff7a898f86>

These deployments demonstrate that the core architecture and Oracle integration work in a realistic blockchain environment. The next stage is broader source integration, optimization, testing and mainnet deployment.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Aggregation runs inside the consumer’s transaction rather than through a separate price publishing step.

When a protocol needs a price, the transaction includes the required Oracle reference inputs and triggers the Oracle Price Calculate validator through a zero-withdrawal. The validator reads the configured Oracle sources and price paths, validates the referenced price data and calculates the conversion price before the protocol can use it.

Source configuration is kept separate from protocol logic through Oracle Source and Oracle Path data. This allows different sources such as Liqwid, Minswap and future integrations to be added without embedding source-specific logic into every consumer contract.

Price validation and aggregation happen on chain. If the configured price conditions are not satisfied, the consumer transaction fails.

This fits the Oracle category directly: protocols consume multiple on-chain price sources through one common validation layer, with the result verified as part of their own transaction.

Diagram: <https://drive.google.com/file/d/1kLrdMQxS_8lVz1g1kwHBRIAYHCduhXfZ/view?usp=sharing>

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The market is any Cardano protocol whose logic depends on price data: lending and borrowing, liquidations, collateral valuation, perpetuals, synthetic assets, stablecoin reserve ratios, and routing.

Demand is already visible in how fragmented pricing is today. Protocols such as Liqwid, FluidToken, Surf, Orcfax, and Indigo use their own price sources and validation methods. In one live observation, Surf returned ADA at **$0.1749503**, while Liqwid returned **$0.1748**, a difference of about **0.086%**. The gap is small, but it shows that the same asset can have different valid reference prices depending on the protocol and source being used.

This matters because relying on a single source creates exposure to stale data, downtime, or manipulation, especially when liquidity is thin. At the same time, every team currently has to build its own adapters, freshness checks, deviation rules, and fallback logic.

Our goal is to provide that missing shared layer: multiple independent sources combined under one transparent, on-chain methodology, so protocols can use a consistent and independently verifiable reference price.

### Applicant name

Phan Phung Hai

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Free access during the pilot is a deliberate adoption strategy, not the absence of a business model. Early integrations are valuable because once the aggregator is integrated into on-chain logic and tested in production, switching later requires contract changes.

After the pilot, revenue comes from three areas: subscriptions for protocols needing source coverage, freshness targets and support; custom feed configuration, including new asset pairs, quorum rules and adapters; and integration/support services.

Protocols pay to avoid maintaining several Oracle integrations and the risks of single-source dependency. Our main costs are adapter maintenance, indexing, monitoring, contract upkeep, support and security reviews.

Usage is recurring because integrated protocols use the aggregator during actions such as borrowing, repayment and liquidation checks. We do not reward users for transactions, and protocols cover their own network fees.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Shared infrastructure is difficult to fund because every protocol can benefit, but no single protocol wants to build and maintain it for the ecosystem. This grant funds the first production-ready version so teams can focus on integration.

Allocation of 120,000 ADA:

- Aggregation validator and feed registry: 42,000
- Source adapters and configurations: 26,000
- Indexer, monitoring and dashboard: 16,000
- External audit and remediation: 22,000
- Documentation, integration support and launch: 12,000
- Contingency: 2,000

The external auditor has not yet been selected. We will appoint an independent Cardano security auditor before mainnet release. The 22,000 ADA budget covers the audit, issue review and remediation, with engagement evidence published before the audit begins.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery is month 2 of the 3-month window to allow additional time for adoption measurement.

**M1 outputs:**

- Production-ready aggregation layer on Cardano mainnet
- Aiken Aggregation Validator
- Source adapters for Liqwid, Minswap, SundaeSwap and Splash
- Source configuration, indexing and monitoring
- Dano Finance Lending Smart Contract V2 as the anchor integration

**Mainnet evidence:**

- At least one real end-to-end user transaction
- Independent repeated runs of the same flow


- Transaction hashes mapped to user flow steps
- Declared script hashes and addresses
- Registered message tag
- Live product URL
- Release notes
- Repository tag/commit
- Test evidence and security notes
- Technical walkthrough video

We will demonstrate the same mainnet integration, identifiers and transaction flows used for acceptance.

After M1, adoption will be measured against the declared target of **1,125 transactions and 900 ADA in counted fees**.

### Oracles - expected transaction count

1125

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano already has several sources of price data, including Charli3, Orcfax, Pyth, and DEX pools. However, these sources use different data formats, update rules, trust models, and integration methods. As a result, each DeFi protocol has to choose its own sources and build its own pricing logic.

This creates several problems. Different protocols may value the same asset differently, relying on a single source increases the risk of downtime or price manipulation, and every new protocol has to repeat much of the same Oracle integration work.

We are building an on-chain Oracle aggregation layer that combines multiple independent price sources into one standardized and verifiable price.

Instead of operating a centralized price publisher, aggregation happens directly when a protocol uses the price in its own transaction. The validator checks that enough sources are available, verifies data freshness, filters out prices that deviate beyond a configured range from the median, and validates that the final price used by the protocol matches the aggregated result.

This means there is no trusted publisher or privileged party controlling the final price. Protocols can run and verify the open-source validator directly on-chain.

The solution is designed for lending protocols, perpetuals and derivatives, DEX aggregators, stablecoins, synthetic assets, and other Cardano applications that need reliable and manipulation-resistant price data.

### Supporting links (repo, site, demo)

- https://github.com/hairphan/Multi-Source-Oracle
- https://nioapp.io/

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

900

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

Yes. The aggregation validator, source adapters and consumer integration\
documents will be published under an open-source licence at Milestone 1, with the\
tagged commit matching the deployed mainnet script hashes. An oracle that DeFi\
protocols are asked to trust with liquidation decisions has to be readable.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed multi-source integration is at TRL 3. The aggregation methodology, including source quorum, freshness checks and deviation filtering, has been defined and tested against recorded price data from Liqwid and Minswap.\
\
Existing Oracle contracts are already deployed on Cardano Preprod, but the expanded multi-source architecture is not yet complete.\
\
This grant funds the Aiken aggregation validator, adapters for Liqwid, Minswap, SundaeSwap and Splash, the integration library, testing, and deployment for live protocol consumption on Cardano mainnet.
