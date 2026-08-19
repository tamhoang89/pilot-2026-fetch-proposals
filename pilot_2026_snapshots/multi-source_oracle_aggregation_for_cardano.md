# Multi-Source Oracle Aggregation for Cardano

> One standard interface, many oracle sources verified on-chain, per transaction.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 15
- **Proposer:** `stake1uxps8zkp98wtp77cnzl0g6eya50qf4svjn03l78klhvyfts46n73h`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-19T06:43:26.111000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Our team combines the smart-contract, off-chain infrastructure, and Oracle/data-integration experience required to deliver the Multi-Source Oracle Aggregation.\
\
Phan Phung Hai - <https://www.linkedin.com/in/hairphan/>\
\
Truong Quang Chu -<https://www.linkedin.com/in/truongquangchu/>\
\
Nguyen Thi Kim Chi - [www.linkedin.com/in/chi-nguyen-773871288](http://www.linkedin.com/in/chi-nguyen-773871288)\
\
The team has experience with Plutus and Aiken, testnet and mainnet deployments, off-chain code, indexers, backend services, external price feeds, and aggregation logic.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Declared fee target: 900 ADA** in counted Cardano network fees under the Oracles category, above the 232 ADA programme floor for a 120,000 ADA award.

Fees are paid by end users of integrated protocols. Borrowing, repayment, liquidation or other price-dependent actions execute the aggregation validator inside the user’s transaction. We neither sponsor nor receive these fees.

The target assumes:

- 1 protocol live by M1
- About 1,125 external transactions
- About 0.80 ADA average network fee
- 45 distinct external wallets

Usage is recurring because the aggregator is called whenever an integrated protocol performs a price-dependent action. At a lower 0.65 ADA average fee, around 1,385 transactions would still reach the 900 ADA target.

The 900 ADA target is about 3.9x the programme minimum, making it ambitious while still tied to real protocol activity.

### How will you reach and onboard real users - and what evidence backs your channels?

Our users are protocols, not retail wallets, so onboarding focuses on business development and developer experience before Milestone 1.

Dano Finance is the anchor integration and will integrate the aggregator into its Lending Smart Contract V2 within M1. Lending is a strong first use case because prices are needed continuously for borrowing, repayment, collateral checks and liquidations. Network fees are paid by end users; we do not sponsor or receive them.

Integration is designed to be lightweight: an Aiken library, TypeScript SDK, examples, deterministic error codes and test vectors for stale sources, quorum failures, deviation handling and fallback. The Dano integration will also serve as the reference implementation.

Adoption will be supported through Cardano developer channels, direct outreach and published methodology documentation. Retention depends on reliability, source coverage and responsive support once the aggregator becomes part of a protocol’s core transaction flow.

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

The audit is essential because protocols may use this validator in critical paths such as collateral valuation and liquidation. Security review is therefore a direct requirement for production adoption.

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
