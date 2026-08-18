# ATLAS: Stablecoin Perpetuals on Cardano

> Launching Cardano’s fully on-chain perpetuals DEX with verified USDCx and USDM collateral, unified liquidity and transparent on-chain usage.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1u9wrkyze58nzwfs4av8nxrr2lpfk0yd2pwh2ff4yxpvdvsgccegq2`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-18T11:31:28.455000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Atlas is led by Oliver “Apex” Radivojevic, a veteran Cardano-native founder and hands-on operator who has been building in the ecosystem since 2021. He founded House of Titans and developed it from an idea into a revenue-generating Web3 and DePIN organisation, deploying and managing infrastructure across BTC mining, Cardano staking, enterprise nodes, treasury investments and recurring community distributions.

Apex has raised and allocated capital, launched products, negotiated ecosystem partnerships, assembled international contractor teams, managed infrastructure and built active communities. He has continued executing through multiple bear markets, demonstrating resilience, commercial judgement and long-term commitment to Cardano.

LinkedIn: <https://www.linkedin.com/in/o-r-893341136/>\
X: <https://x.com/Apex_333>

Vata is Atlas’s contracted CTO, a Korea-based blockchain engineer experienced in DEX architecture, blockchain infrastructure, node operations and production deployment. 

X: <https://x.com/vataops>\
GitHub: <https://github.com/vataops>

Alexandru “Sic” Campurean is Atlas’s Marketing Manager and a Web3 operator since 2019. His experience includes marketing leadership, community management and business development.

X: <https://x.com/Sic2336>\
Professional links: <https://linktr.ee/sic236>

 Together, we have delivered three testnets, attracted 500+ users, processed over $165M in simulated volume and completed the internal Mainnet build.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Atlas generates genuine usage whenever users deposit stablecoins, open or adjust leveraged positions, close trades, settle liquidations or withdraw funds. Trading actions consume oracle pricing and use stablecoins as collateral and settlement assets, creating measurable Cardano transactions and network fees.

These targets are supported by three testnets that attracted 500+ users and processed over $165 million in simulated volume. Reaching 8,000 transactions requires an average of only 16 transactions per existing testnet user, before accounting for new users recruited at Mainnet launch.

At an estimated average network fee of 0.25 ADA per transaction, 8,000 transactions would generate approximately 2,000 ADA in fees. Only genuine, labelled Mainnet activity from external wallets will be counted.

### How will you reach and onboard real users - and what evidence backs your channels?

Atlas will onboard users through three proven channels: its existing X, Discord and staking community; Cardano ecosystem, wallet and stablecoin communities; and product-led campaigns including trading competitions, points, referrals and guided deposits.

The funnel is simple: educational content and partner promotion → connect a Cardano wallet → deposit USDM/USDCx → place a first trade → return through new markets, points and competitions. Tutorials, demonstrations and Discord support will reduce friction for first-time perpetual traders.

These channels already convert. Atlas testnets attracted 500+ users and produced over $165M in simulated trading volume through community campaigns. 

At Mainnet launch, we will reactivate testnet users, coordinate campaigns with Cardano and stablecoin communities, and measure distinct wallets, labelled transactions, network fees and repeat usage. Incentives encourage initial trials; useful markets and ongoing trading support retention.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralised exchanges, external-chain perpetual DEXs such as Hyperliquid and GMX, and Cardano protocol Strike. Atlas differentiates through a stablecoin-first unified vault: one shared pool supports every market, improving capital efficiency and enabling new markets without fragmenting liquidity. Collateral, trading and settlement remain on Cardano, while fees and payouts are denominated in stablecoins. This creates recurring utility for USDM and USDCx alongside measurable Cardano transactions. Atlas also has a working testnet, an existing user and staking community, and an internally completed mainnet build, reducing delivery risk compared with an early-stage concept.

### Please provide details about the Technology Readiness Level selected for your existing product

Atlas is currently at TRL 7. The complete protocol has been demonstrated through three public Cardano testnets, attracting 500+ users and processing over $165 million in simulated trading volume. Core functions—including Cardano smart contracts, wallet connectivity, oracle pricing, stablecoin-based collateral, the unified liquidity vault, leveraged trading, fees, liquidations and withdrawals—have been validated. The internal Mainnet build and initial security review are complete. Remaining findings are being addressed before the formal audit and Public Mainnet release. We are therefore not claiming TRL 8 or 9, as formal qualification and live production deployment remain pending.

Evidence:\
<https://www.atlasdefi.org/>\
<https://github.com/atlas-perp/atlas>

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Atlas uses Cardano’s eUTxO model with protocol state represented on-chain and enforced by Aiken validators. Whitelisted Cardano-native stablecoins such as USDM and USDCx are deposited into validator-controlled UTxOs within a unified liquidity vault. This shared vault acts as the counterparty across multiple perpetual markets, improving capital efficiency without fragmenting liquidity into separate pools.

Positions, collateral, fees, liquidations and settlements are governed by deterministic validator rules. Authenticated oracle prices provide the market data required to open, value, liquidate and settle positions. Market-specific state is separated so trading pairs can process activity independently, reducing contention and supporting future expansion.

Off-chain services construct transactions, index blockchain state and provide the user interface, but cannot override validator rules or move protocol funds without satisfying on-chain conditions. This architecture is well suited to stablecoins and oracles because it keeps collateral native to Cardano, makes trading activity verifiable and produces measurable transactions and network fees. The modular design also allows new stablecoins, oracle providers and markets to be added without redesigning the entire protocol.

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

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Atlas targets Cardano users who currently trade perpetuals on centralised exchanges or other blockchains, stablecoin holders seeking productive utility, and liquidity providers seeking stablecoin-denominated fee exposure.

Demand is already established. On-chain perpetual DEXs process close to $1 trillion in 30-day volume, making perpetuals one of DeFi’s largest fee-generating categories. Cardano users have also demonstrated demand for native perpetuals: Strike has approximately $2.5 million in TVL and generated around $32,700 in fees over the past 30 days.

Atlas has demonstrated direct interest through its own testnet, attracting more than 500 users and processing over $165 million in simulated trading volume. Additionally, 4.06 million ATLAS—nearly 80% of its reported circulating supply—is currently staked.

Atlas is designed to retain more of this activity on Cardano. Users deposit verified stablecoins into one shared vault, trade multiple markets and settle positions on-chain. Deposits, trades, settlements and withdrawals create measurable Cardano transactions and network fees instead of exporting users and economic activity to other chains.

The timing is strong: Cardano’s stablecoin infrastructure is growing, but recurring utility remains limited. Atlas converts stablecoin liquidity into trading infrastructure, protocol fees and stablecoin payouts—strengthening stablecoin circulation, Cardano DeFi and the network’s long-term fee economy.

### Applicant name

Oliver Radivojevic

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Atlas is targeting Public Mainnet within weeks, subject to the remaining fixes and formal audit. Development has already been financed through completed ATLAS token sales and founder/community capital; Catalyst funding accelerates stablecoin integration and adoption rather than creating dependency.

Traders pay trading and borrowing fees. Revenue grows with trading volume and open positions. A share supports the unified liquidity vault and liquidity providers, while the protocol share funds infrastructure, security, development and stablecoin-denominated payouts.

Usage continues because perpetuals are 24/7, repeat-use products: traders open, adjust and close positions, while liquidity providers benefit from activity. New markets can also be added without separate liquidity pools.

Atlas does not need a large global market share to be sustainable. Even a small share of existing demand can generate recurring revenue, allowing the protocol to continue after grant funding ends.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Atlas has privately funded the core protocol and internal Mainnet build. Catalyst funding would expand this into a production-grade stablecoin and oracle integration with stronger security, monitoring and measurable Cardano adoption. Without funding, Atlas would still launch, but the integration scope and adoption programme would progress more slowly.

High-level allocation:

• 40% – USDM/USDCx integration, vault engineering and oracle resilience\
• 25% – independent security audit and integration testing\
• 20% – Mainnet infrastructure, monitoring and on-chain analytics\
• 15% – documentation, user onboarding and adoption campaigns

This funding accelerates a secure Public Mainnet launch while creating recurring stablecoin usage, transactions and fees on Cardano.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, Atlas will deliver:

• Production USDM and USDCx integration within the unified liquidity vault.\
• Production oracle feeds for the initial markets, including price validation, freshness checks and failure protections.\
• Completion of remaining smart-contract fixes, an independent security audit and remediation of material findings.\
• Public Mainnet deployment of the protocol, frontend and supporting infrastructure.\
• End-to-end functionality covering deposits, trades, liquidations, settlements and withdrawals.\
• On-chain labelling and analytics to measure distinct wallets, transactions and network fees.\
• Public documentation covering trading, collateral, vault participation, fees and risks.

Delivery will be evidenced by the live application, contract addresses, Mainnet transaction IDs, audit report and public documentation.

### Oracles - expected transaction count

8000

### How far along is the integration you're proposing, today?

TRL 7 - System prototype demonstrated in operational environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano’s stablecoin ecosystem is growing, but it still lacks enough products that create recurring, productive demand. Stablecoins can be held or transferred, yet limited trading utility and fragmented liquidity reduce how frequently that capital is actively used on-chain.

Atlas is building a stablecoin-first, fully on-chain perpetuals exchange designed to become a stablecoin utility engine for Cardano.

Liquidity providers deposit verified stablecoins such as USDM and USDCx into one unified vault. This shared pool powers multiple perpetual markets without dividing capital across separate liquidity pools. Traders use stablecoins as collateral, gain synthetic leveraged exposure to different assets and settle positions through Cardano smart contracts.

Atlas creates a continuous loop: stablecoins are deposited, used to power markets, generate trading and borrowing fees, and are paid back to participants in stablecoins. Those payouts can then be traded, redeposited or used elsewhere across Cardano.

This serves traders, stablecoin holders, liquidity providers and issuers. It addresses two connected problems: limited native perpetual-trading infrastructure and insufficient recurring stablecoin utility. The result is measurable wallet activity, transactions and network fees on Cardano.

### Supporting links (repo, site, demo)

- https://www.atlasdefi.org/
- https://github.com/atlas-perp/atlas

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

2000

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

### Stablecoins - expected transaction count

8000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

2000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Atlas’s oracle and stablecoin integrations are at TRL 7. Oracle-driven market pricing and stablecoin-based collateral, trading and settlement logic have been demonstrated across three public Cardano testnets, attracting 500+ users and processing over $165 million in simulated volume. The internal Mainnet system is complete and undergoing security remediation. Catalyst funding will support production integration of verified Cardano stablecoins, strengthen oracle reliability and failover protections, complete the formal audit and deploy the integrations to Public Mainnet. The integrations are therefore operational at testnet level but are not yet being claimed as fully qualified or proven in live production.
