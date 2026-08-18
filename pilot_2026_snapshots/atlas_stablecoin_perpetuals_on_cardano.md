# ATLAS: Stablecoin Perpetuals on Cardano

> Launching Cardano’s fully on-chain perpetuals DEX with verified USDCx and USDM collateral, unified liquidity and transparent on-chain usage.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1u9wrkyze58nzwfs4av8nxrr2lpfk0yd2pwh2ff4yxpvdvsgccegq2`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-18T19:27:38.859000+00:00

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

Atlas targets 8,000 qualifying transactions and 2,000 ADA in counted fees for each integration.

• 5,000 transactions (62.5%) from 200 reactivated users drawn from 500+ former Atlas testers, averaging 25 each.\
• 1,200 (15%) from 75 additional, non-overlapping users drawn from Atlas’s 152 stakers and House of Titans’ 616 stake-pool delegators, averaging 16 each.\
• 1,800 (22.5%) from 100 new users reached through non-incentivised tutorials, X Spaces, Discord support and Cardano DeFi/stablecoin communities, averaging 18 each.

Total: 375 unique external wallets and 8,000 transactions. Existing communities contribute 77.5% of projected usage and new users 22.5%. Users deposit, trade, settle and withdraw—not to earn rewards. Qualifying trades consume the declared oracle feed and move verified stablecoins. At the program reference average of 0.33 ADA per transaction, 8,000 transactions generate about 2,640 ADA, giving the 2,000 ADA target an execution buffer. Activity will be labelled and deduplicated by stake key.

### How will you reach and onboard real users - and what evidence backs your channels?

Atlas will rely solely on organic, non-incentivised adoption. No points, rebates, referral rewards, competitions or transaction incentives will operate during the measurement period.

Days 1–7: announce Mainnet to 500+ former testers through Atlas X and Discord; reach Atlas’s 152 stakers and the House of Titans community, including 616 stake-pool delegators; publish a launch guide and video; and host two onboarding sessions. Target: 125 external wallets, 125 deposits and 625 trading/settlement transactions.

Days 8–14: follow up with former testers, publish stablecoin and market tutorials, host two X Spaces and support sessions, and distribute educational content through Cardano DeFi communities. Target: 110 additional wallets, 110 deposits and 1,140 trading/settlement transactions.

By day 14, Atlas targets 235 external wallets and 2,000 cumulative transactions. Weekly education, product updates and support will continue without transaction-linked rewards.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralised exchanges, external-chain perpetual DEXs such as Hyperliquid and GMX, and Cardano protocol Strike. Atlas differentiates through a stablecoin-first unified vault: one shared pool supports every market, improving capital efficiency and enabling new markets without fragmenting liquidity. Collateral, trading and settlement remain on Cardano, while fees and payouts are denominated in stablecoins. This creates recurring utility for USDM and USDCx alongside measurable Cardano transactions. Atlas also has a working testnet, an existing user and staking community, and an internally completed mainnet build, reducing delivery risk compared with an early-stage concept.

### Please provide details about the Technology Readiness Level selected for your existing product

Atlas is currently at TRL 7. The protocol has been demonstrated through three public Cardano testnets, attracting 500+ users and processing over $165 million in simulated trading volume. Validated functions include Aiken smart contracts, wallet connectivity, stablecoin-based collateral, the unified liquidity vault, leveraged trading, pricing, fees, liquidations and withdrawals.

The internal Mainnet build and initial independent security review are complete. Remaining findings are being remediated before the formal audit and Public Mainnet release. Atlas is therefore not claiming TRL 8 or 9, as formal qualification and live production deployment remain pending.

Evidence:\
<https://www.atlasdefi.org/>\
<https://github.com/atlas-perp/atlas>

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Atlas uses Cardano’s eUTxO model, with protocol state represented on-chain and enforced by Aiken validators. Verified Cardano-native stablecoins, initially USDM and USDCx, are held in validator-controlled UTxOs within a unified liquidity vault. The vault supports multiple perpetual markets without fragmenting liquidity across separate pools.

The named oracle dependency is Pyth Pro. Atlas will consume signed Pyth price updates for supported markets, initially including ADA/USD, BTC/USD and ETH/USD. Each qualifying user trade includes the price update through Pyth’s Cardano zero-withdrawal script pattern. Atlas validators verify the feed ID, signature and price freshness before permitting positions to open, close, liquidate or settle.

Positions, collateral, fees and settlements are governed by deterministic validator rules. Market-specific state is separated so trading pairs can process independently, reducing contention. Off-chain services construct transactions, index state and provide the interface, but cannot override validators or move vault funds without satisfying on-chain conditions.

This architecture keeps collateral native to Cardano and makes stablecoin movement and oracle consumption verifiable. External-user transactions can therefore be labelled and measured through contract identifiers, stablecoin policy IDs and Pyth feed consumption.

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

Atlas targets users who trade perpetuals on centralised exchanges or other blockchains, stablecoin holders seeking productive utility, and liquidity providers seeking stablecoin-denominated fee exposure.

Demand is established. On-chain perpetual DEXs process hundreds of billions of dollars in monthly volume, making perpetuals one of DeFi’s largest trading and fee-generating categories. Cardano users have also demonstrated demand for native perpetuals: Strike currently has approximately $2.5 million in TVL, generated around $32,700 in fees and processed approximately $117 million in perpetual volume over the past 30 days.

Atlas has demonstrated direct interest through three public testnets, attracting 500+ users and processing over $165 million in simulated trading volume. Additionally, 4 million ATLAS nearly 80% of its reported circulating supply is currently staked.

Atlas is designed to retain this activity on Cardano. Users deposit verified stablecoins into one shared vault, trade multiple markets and settle positions on-chain. Deposits, trades, settlements and withdrawals create measurable Cardano transactions and network fees rather than exporting users and economic activity to other chains.

Cardano’s stablecoin infrastructure is growing, but recurring utility remains limited. Atlas converts stablecoin liquidity into trading infrastructure, protocol fees and stablecoin payouts, strengthening stablecoin circulation, Cardano DeFi and the network’s long-term fee economy.

### Applicant name

Oliver Radivojevic

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Atlas is targeting Public Mainnet within the Pilot’s three-month Milestone 1 window, subject to completing remediation and the formal audit. Core development has already been financed through ATLAS token sales and founder/community capital. Catalyst funding accelerates production integration of USDM, USDCx and Pyth Pro, alongside security, monitoring and organic onboarding, without creating grant dependency.

Traders pay trading and borrowing fees. A share supports the unified liquidity vault and liquidity providers, while protocol revenue funds infrastructure, security, development and stablecoin-denominated payouts.

Perpetuals generate recurring usage because traders continually open, adjust and close positions. New markets can be added without separate liquidity pools. Atlas requires only a small share of existing demand to generate sustainable recurring revenue and continue operating after Catalyst funding ends.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Atlas has privately funded the core protocol and internal Mainnet build. Catalyst funding would accelerate production integration of verified USDM and USDCx policies with Pyth Pro oracle feeds, while strengthening security and monitoring.

High-level allocation:

• 40% – USDM/USDCx integration, vault engineering and Pyth Pro implementation\
• 25% – independent security audit and remediation\
• 20% – Mainnet infrastructure, monitoring and on-chain analytics\
• 15% – documentation, user education and organic onboarding

Without funding, Atlas would still pursue launch, but the integration scope and onboarding programme would progress more slowly. Funding enables a broader, independently audited deployment that creates recurring stablecoin usage, external transactions and Cardano network fees

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

Atlas’s oracle and stablecoin integrations are at TRL 7. Oracle-driven pricing and stablecoin collateral, trading and settlement logic have been demonstrated across three public Cardano testnets, attracting 500+ users and processing over $165 million in simulated volume.

For production, Atlas will integrate verified USDM and USDCx policies and use Pyth Pro as its oracle provider. User trading transactions will consume signed Pyth price updates through its Cardano zero-withdrawal script pattern.

The internal Mainnet system is complete and undergoing security remediation before the formal audit and Public Mainnet deployment. The integrations are operational at testnet level but are not being claimed as fully qualified or proven in live production.
