# ATLAS: Stablecoin Perpetuals on Cardano

> A measured mainnet Pilot of verified USDM/USDCx collateral and Pyth Pro pricing for on-chain perpetuals.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 14
- **Proposer:** `stake1u9wrkyze58nzwfs4av8nxrr2lpfk0yd2pwh2ff4yxpvdvsgccegq2`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T14:06:07.947000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Atlas is led by Oliver “Apex” Radivojevic, a Cardano-native founder and hands-on operator building in the ecosystem since 2021. He founded House of Titans and has led treasury operations, infrastructure deployment, contractor coordination, product launches and community growth across Cardano staking, enterprise nodes and Web3 infrastructure.

For this Pilot, Apex is responsible for strategy, delivery coordination, treasury oversight, ecosystem communication, reporting and operations.

LinkedIn: <https://www.linkedin.com/in/o-r-893341136/>\
X: <https://x.com/Apex_333>

Jinhyeong “Vata” Lee is Atlas’s contracted technical lead for the existing codebase, handover and remediation of technical findings. His experience includes DEX architecture, blockchain infrastructure, node operations and production deployment.

X: <https://x.com/vataops>\
GitHub: <https://github.com/vataops>

Alexandru “Sic” Campurean leads marketing, community operations, educational content and organic onboarding. He has worked in Web3 marketing, community management and business development since 2019.

X: <https://x.com/Sic2336>\
Professional links: <https://linktr.ee/sic236>

The team has delivered three public testnets involving 500+ users and more than $165 million in simulated volume. The Pilot funds post-award integration hardening, independent security validation, monitoring and reporting.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Atlas targets 1,200 qualifying transactions across 180 unique funded wallets. Each transaction uses both Pyth Pro price data and verified USDM or USDCx collateral, and is counted once within each applicable integration metric.

480 transactions will come from 60 reactivated users drawn from 500+ former Atlas testers, averaging eight each. 360 will come from 60 additional, non-overlapping users reached through Atlas’s 300 token holders and House of Titans’ community of 1,200+ TITAN token holders, NFT investors and stake-pool participants, averaging six each. The remaining 360 will come from 60 new users reached through tutorials, X Spaces, Discord support and organic Cardano outreach, averaging six each.

House of Titans is an applicant-operated community channel, not an external adoption partner. All audiences will be deduplicated by stake key.

Users transact to deposit, trade, settle and withdraw—not to obtain rewards. No incentives, referrals or transaction subsidies will be offered. At the programme reference average of ₳0.33, 1,200 transactions generate approximately ₳396, exceeding the ₳350 oracle and ₳370 stablecoin targets.

### How will you reach and onboard real users - and what evidence backs your channels?

Atlas will use organic, non-incentivised adoption only. No points, rebates, referral rewards, competitions or transaction incentives will operate during the measurement period.

Days 1–7: Atlas will contact 500+ former testers through X and Discord, reach Atlas stakers and House of Titans’ existing 1,500+ holder and investor community, publish a launch guide and video, and host two onboarding sessions. Target: 40 funded wallets and 120 trading or settlement transactions.

Days 8–14: Atlas will follow up with users, publish stablecoin and market tutorials, host two X Spaces and support sessions, and share educational content through Cardano DeFi communities. Target: 30 additional funded wallets and 180 additional transactions.

By Day 14, Atlas targets 70 unique funded wallets and 300 cumulative transactions. House of Titans is an applicant-operated communication channel, not an external adoption partner, and no third-party commitments are assumed.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralised exchanges, external-chain perpetual DEXs such as Hyperliquid and GMX, and Cardano protocol Strike.

Atlas differentiates through a stablecoin-first unified vault: one shared pool supports multiple markets, improving capital efficiency and allowing new markets to be added without fragmenting liquidity across separate pools. Collateral, trading and settlement remain on Cardano, while fees and payouts are denominated in stablecoins. This creates recurring utility for USDM and USDCx alongside measurable Cardano transactions.

Atlas also has a working testnet and an existing user and staking community, reducing delivery risk compared with an early-stage concept.

### Please provide details about the Technology Readiness Level selected for your existing product

Atlas’s privately funded core protocol is assessed at TRL 7. Three public Cardano testnets demonstrated Aiken smart contracts, wallet connectivity, the unified vault, leveraged trading, pricing, fees, liquidations and withdrawals with 500+ users and over $165 million in simulated volume. An internal mainnet candidate has been developed but review findings are being remediated before formal audit and public deployment, so Atlas does not claim TRL 8 or 9. This assessment covers only the core protocol. The proposed USDM/USDCx and Pyth Pro production integration is separately assessed at TRL 6. Catalyst will not reimburse completed work.

Evidence:\
<https://www.atlasdefi.org/>\
<https://github.com/atlas-perp/atlas>

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Atlas uses Cardano’s eUTxO model, with protocol state represented on-chain and enforced through Aiken validators. Verified USDM and USDCx policy IDs will ensure that only authentic stablecoins can be accepted as collateral. Collateral is held in validator-controlled UTxOs within a unified liquidity vault, allowing multiple perpetual markets to share liquidity without separate, fragmented pools.

The production oracle dependency is Pyth Pro. State-changing trades will consume signed Pyth price updates through Cardano’s zero-withdrawal script pattern. Atlas validators will verify the feed ID, signature, price freshness and applicable market before permitting positions to open, close, liquidate or settle.

Positions, collateral, fees and settlements are controlled by deterministic validator rules. Market-specific state is separated so trading pairs can process independently and reduce eUTxO contention. Off-chain services may construct transactions, relay data and provide analytics, but cannot independently alter balances, positions or settlement outcomes.

This architecture is appropriate because stablecoin custody, trading logic and settlement remain verifiable on Cardano, while Pyth supplies authenticated external prices at transaction execution. Production hardening, monitoring, external security validation and the measured mainnet Pilot remain outstanding.

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

Atlas targets users who trade perpetuals on centralised exchanges or other blockchains, stablecoin holders seeking productive on-chain utility, and liquidity providers seeking stablecoin-denominated fee exposure.

Demand for perpetual trading is well established: on-chain perpetual DEXs process hundreds of billions of dollars in monthly volume, making perpetuals one of DeFi’s largest trading and fee-generating categories. Cardano users have also demonstrated demand for native perpetuals. Strike has approximately $2.5 million in TVL, generated around $32,700 in fees and processed approximately $117 million in perpetual volume over the previous 30 days.

Atlas has demonstrated direct testnet interest through three public testnets involving 500+ users and over $165 million in simulated trading volume. More than 4 million ATLAS, over 80% of reported circulating supply, is staked. These are testnet and community indicators rather than claims of guaranteed mainnet conversion.

Atlas enables users to deposit verified stablecoins into a shared vault, trade multiple markets and settle on-chain. Deposits, trades, settlements and withdrawals create measurable Cardano transactions and network fees rather than exporting activity to other chains.

Cardano’s stablecoin infrastructure is growing, but recurring utility remains limited. Atlas converts stablecoin liquidity into trading infrastructure, protocol fees and stablecoin payouts, supporting stablecoin circulation and Cardano DeFi.

### Applicant name

Oliver Radivojevic

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Atlas targets Public Mainnet within the Pilot’s three-month Milestone 1 window, subject to remediation and formal audit. Core development has already been privately financed. Catalyst funding will support only post-award USDM, USDCx and Pyth Pro integration hardening, independent validation, monitoring and organic onboarding; it will not reimburse completed work.

Traders pay trading and borrowing fees. A share supports the unified liquidity vault and liquidity providers, while protocol revenue funds infrastructure, security, development and stablecoin-denominated payouts.

Perpetuals generate recurring usage because traders continually open, adjust and close positions. New markets can be added without separate liquidity pools. Atlas requires only a small share of existing demand to generate sustainable recurring revenue and continue operating after Catalyst funding ends.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Atlas privately funded the core protocol; Catalyst will not reimburse completed or pre-award work. The ₳200,000 funds a distinct post-award USDM/USDCx and Pyth Pro mainnet Pilot: ₳60,000 for production integration, hardening and testing; ₳75,000 for independent security review, remediation and verification; ₳30,000 for three months of infrastructure, monitoring and operational support; ₳20,000 for on-chain analytics and public milestone reporting; and ₳15,000 for technical documentation, user support and final reporting. Without funding, Atlas will continue its core launch, but the dedicated Pilot, external validation and public measurement will be delayed or reduced. No funds will cover historical costs, liquidity, incentives, trading rewards or referrals.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, Atlas will deliver a post-award mainnet Pilot of verified USDM and USDCx collateral with Pyth Pro oracle flows for initial markets. Deliverables include stablecoin policy validation, signed price-update verification, freshness and failure protections, integration hardening, automated testing, independent security validation and remediation verification.

The Pilot will support end-to-end deposits, trades, position closure, liquidation where applicable, settlement and withdrawals. Atlas will provide monitoring, on-chain analytics for wallets, transactions, fees and network activity, plus public documentation, risk guidance, release notes and Pilot reporting.

Evidence will include the live product, contract addresses, policy IDs, mainnet transaction hashes, security evidence, analytics outputs and a Demo Day walkthrough. Catalyst funds only these post-award Pilot deliverables, not prior testnets, historical development or the pre-existing core protocol.

### Oracles - expected transaction count

1200

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

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

350

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

1200

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

370

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Atlas’s proposed USDM/USDCx collateral and Pyth Pro oracle integration is assessed at TRL 6. Oracle-driven pricing, stablecoin collateral, trading and settlement have been demonstrated across three public Cardano testnets involving 500+ users and over $165 million in simulated volume.

The production integration will use verified USDM and USDCx policy IDs and signed Pyth Pro price updates through Cardano’s zero-withdrawal script pattern. However, it has not yet completed production hardening, external security validation, monitoring or a measured mainnet pilot.

Catalyst will fund only this outstanding post-award integration work. The privately funded core protocol and previous testnets are excluded. This is why the integration is not claimed as TRL 7 or higher.
