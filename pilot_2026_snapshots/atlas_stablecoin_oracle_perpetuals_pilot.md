# ATLAS: Stablecoin & Oracle Perpetuals Pilot

> Integrating USDM and USDCx collateral with Pyth Pro price feeds to deliver measurable perpetual trading activity on Cardano mainnet.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 23
- **Proposer:** `stake1u9wrkyze58nzwfs4av8nxrr2lpfk0yd2pwh2ff4yxpvdvsgccegq2`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-24T16:07:08.396000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

HOUSE OF TITANS LTD is the applicant. Oliver “Apex” Radivojevic has built in the Cardano ecosystem since 2021 and founded House of Titans and Atlas. He is accountable for Pilot scope, budget, contractor coordination, reporting and ecosystem communication.

LinkedIn: <https://www.linkedin.com/in/o-r-893341136/>\
X: <https://x.com/Apex_333>

Jinhyeong “Vata” Lee is Atlas’s contracted technical lead, responsible for codebase continuity, remediation, integration support and technical handover. His experience covers DEX architecture, blockchain infrastructure, node operations and production deployment.

GitHub: <https://github.com/vataops>\
X: <https://x.com/vataops>

Alexandru “Sic” Campurean leads educational content, community operations and non-incentivised user onboarding. He has worked in Web3 marketing, community management and business development since 2019.

Portfolio: <https://linktr.ee/sic236>\
X: <https://x.com/Sic2336>

The team has also built and operated House of Titans, a profitable Cardano-based infrastructure and investment business that has generated and reinvested revenue into the ecosystem for more than three years through Bitcoin mining, DeFi participation and enterprise-node investments. This demonstrates sustained experience in treasury management, infrastructure delivery and long-term operations.

No Witness Labs is engaged under contract for the existing protocol audit and technical onboarding: <https://nowitnesslabs.com/>.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Atlas already has 500+ former testnet users, approximately 350 ATLAS holders and House of Titans’ applicant-operated community of 1,500+ token and NFT holders and 600 stake-pool delegators. Audiences may overlap, so wallets will be deduplicated by stake key.

Atlas targets 160 unique funded external wallets: 40 former testers, 40 ATLAS holders, 40 non-overlapping House of Titans members and 40 new Cardano users reached through Atlas and House of Titans X and Discord, guides, tutorials, onboarding sessions and X Spaces.

This assumes 8% conversion from former testers, approximately 11% from ATLAS holders and less than 3% from the wider House of Titans audience. Each wallet averages 10 qualifying transactions during the measurement period—equivalent to opening and closing five positions—producing 1,600 genuine real-capital transactions.

Transactions count only when their use of Pyth Pro and USDM or USDCx is verifiable on-chain. At the programme reference network fee of ₳0.33, 1,600 transactions generate approximately ₳528, supporting a ₳500 target for both Oracles and Stablecoins. Team-controlled, subsidised, incentivised or artificial transactions will not count.

### How will you reach and onboard real users - and what evidence backs your channels?

Atlas already has an existing audience: 350 ATLAS holders and 500 previous testnet users. The Day-14 target of 70 funded wallets equals only 20% of the existing holder base, before considering Atlas Discord/X, House of Titans’ 1,500 holders, 600 stake-pool delegators or the wider Cardano trading community. These audiences overlap, so they are not added together, and no third-party conversion is assumed.

The 300-transaction target averages 4.3 transactions per funded wallet. This is realistic for perpetual trading, where a user may deposit collateral, open a position, adjust it and close or settle it.

Days 1–7: launch guide and video, owned-channel announcements and two live onboarding sessions. Target: 40 wallets and 120 transactions. Days 8–14: trading tutorials, X Spaces and live Discord support. Target: 30 additional wallets and 180 transactions.

Onboarding will focus on Atlas’s Cardano-native on-chain execution. Incentivised activity will not count toward Pilot targets.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralised exchanges, external-chain DEXs such as Hyperliquid and GMX, and Strike Finance. Centralised venues require custody; external-chain DEXs require Cardano users to bridge away.

Strike V2 uses a dedicated execution layer for matching, positions, liquidations and funding, while custody and settlement remain on-chain. Atlas instead has trading positions, liquidations and settlement enforced by Cardano smart contracts, creating directly measurable Cardano transactions and network fees.

Atlas combines USDM/USDCx collateral, Pyth Pro pricing and a unified vault supporting multiple markets without separate pools. Three public testnets validated its core flows; Catalyst funds only post-award integration and hardening.

### Please provide details about the Technology Readiness Level selected for your existing product

Atlas’s privately funded core protocol is assessed at TRL 6. Three public Cardano testnets demonstrated Aiken validators, wallet connectivity, the unified liquidity vault, leveraged trading, pricing, fees, liquidations and withdrawals with 500 users.

A mainnet candidate has been developed, but security findings are still being remediated and the system has not yet completed formal audit or operated publicly with real capital. Atlas therefore does not claim TRL 7–9.

This assessment applies only to the existing core protocol, developed with private funding. The proposed production integration of USDM, USDCx and Pyth Pro is assessed separately at TRL 2. Catalyst will not reimburse any completed or pre-award work.

Evidence\
<https://www.atlasdefi.org/>\
<https://github.com/atlas-perp/atlas>

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Atlas uses Cardano’s eUTxO model, with protocol state held on-chain and enforced through Aiken validators. USDM and USDCx will be recognised using allowlisted policy IDs and asset names, ensuring that only the intended Cardano assets can enter the unified liquidity vault. Validator-controlled UTxOs allow multiple perpetual markets to share liquidity without creating separate pools for every market.

For Pyth Pro, each relevant transaction will include the Pyth state UTxO as a reference input and perform a zero-lovelace withdrawal from Pyth’s verification script. The Pyth script verifies the signed update. Atlas validators then read the verified payload and enforce the supported feed ID, timestamp, freshness window, applicable market and protocol risk rules before allowing a position to open, close, liquidate or settle.

Market-specific state is separated to reduce eUTxO contention. Off-chain services construct transactions, obtain price updates and provide analytics, but cannot independently change collateral, positions, balances or settlement outcomes.

This architecture keeps collateral custody, trading rules and settlement verifiable on Cardano while using authenticated external pricing at transaction execution.

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

Atlas targets Cardano traders seeking leveraged long/short exposure, stablecoin holders seeking recurring on-chain utility, and liquidity providers seeking stablecoin-based vault participation.

Demand for perpetuals is established: decentralised perpetual markets have exceeded $1 trillion in monthly volume. Cardano also has real mainnet evidence. Strike Finance recorded 1,267 on-chain transactions in a 30-day snapshot published by [Cardano.org](http://Cardano.org): <https://cardano.org/apps/strike-finance/>

Atlas has demonstrated product interest through three public testnets involving 500+ users and more than $165 million in simulated volume. Atlas staking currently records over 4.2 million ATLAS across 155 staking wallets. These figures demonstrate reach and engagement, but are not presented as evidence of real-money repeat trading or guaranteed mainnet conversion.

The Pilot will measure funded wallets, qualifying transactions, network fees and repeat usage. Forecasts use only limited conversion from Atlas-owned channels rather than assuming all testers, followers or holders become mainnet traders.

### Applicant name

HOUSE OF TITANS LTD

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Atlas is a fee-generating trading protocol. Traders pay fees when opening and maintaining leveraged positions. Borrowing fees support the unified liquidity vault, while the protocol share funds infrastructure, monitoring, security and continued development.

Perpetuals create recurring usage because traders continually open, adjust and close positions. Atlas begins with owned distribution: 500 previous testnet users, approximately 3,000 Atlas X followers, 10,000 founder followers, Atlas Discord, and the House of Titans community of 1,500 holders and 600 stake-pool delegators. These are acquisition channels, not guaranteed conversion.

Core development was privately financed, and Catalyst funds only post-award integration and validation. After the Pilot, ongoing costs are intended to be covered by protocol revenue. Atlas may pursue private strategic funding after mainnet to expand liquidity, markets and the team, but continued operation will not depend on another grant or funding round.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Atlas privately funded its core protocol, testnets, mainnet candidate and existing audit. Catalyst will reimburse no completed or pre-award work.

The ₳150,000 post-award Pilot budget is:

• ₳45,000 – USDM/USDCx/Pyth Pro engineering, hardening and testing\
• ₳45,000 – independent integration review, remediation and verification\
• ₳25,000 – Pyth connectivity, infrastructure, monitoring and operations\
• ₳20,000 – analytics, measurement and public reporting\
• ₳15,000 – documentation, support and final reporting

Funding advances the provider-specific integration from TRL 2 to TRL 7 mainnet deployment in Milestone 1. Without Catalyst, the Pilot would proceed later or at reduced scope. No funds cover historical costs, liquidity, token purchases or user incentives.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Atlas will advance the USDM, USDCx and Pyth Pro integration from TRL 2 to TRL 7 in three post-award stages.

Month 1 – Build: implement official stablecoin identifiers and signed Pyth Pro updates with feed, freshness and failure controls. Test on pre-production. Outputs: integration build, test report and mapped transactions.

Month 2 – Harden: validate end-to-end trading and settlement; add oracle redundancy, monitoring and analytics. Independently review the integration code, fix findings and verify remediation. Outputs: release candidate, security summary and remediation log.

Month 3 – Mainnet: deploy the Pilot and have external users repeat flows without incentives. Publish contract/script identifiers, supported assets, transaction hashes, release notes and documentation. Demonstrate the live product at Demo Day.

M1 requires a working mainnet Pilot with no unresolved critical/high integration findings. The existing core, testnets, pre-award work and existing audit are excluded.

### Oracles - expected transaction count

1600

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano’s stablecoin ecosystem is growing, but users still have limited ways to put stablecoins to recurring, productive use on-chain. Traders seeking leveraged exposure often need to leave Cardano, while liquidity remains fragmented across assets and markets.

Atlas is an existing, fully on-chain perpetuals protocol with a unified stablecoin vault. Its core architecture and public testnets were privately funded; this proposal does not reimburse completed work.

Catalyst funding will support only forward-looking production integration of USDM and USDCx collateral with Pyth Pro price feeds. Work includes mainnet collateral validation, oracle integration and reliability controls, integration-specific security hardening, monitored deployment and labelled transaction measurement.

Once delivered, traders can use supported Cardano stablecoins as collateral for long and short positions, while liquidity providers supply stablecoins through one vault supporting multiple markets. Pyth Pro feeds support pricing, liquidations and settlement.

The pilot serves Cardano traders, stablecoin holders and liquidity providers, creating recurring stablecoin utility and measurable mainnet activity. USDM, USDCx and Pyth are standard providers; no formal partnership is claimed or required.

### Supporting links (repo, site, demo)

- https://www.atlasdefi.org/
- https://docs.atlasdefi.org/
- https://app-staking.atlasdefi.org/
- https://github.com/atlas-perp/atlas-smart-contracts
- https://github.com/atlas-perp

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

500

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

1600

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

500

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed USDM, USDCx and Pyth Pro integration is at TRL 2. Architecture is defined: Atlas will allowlist official stablecoin identifiers, consume signed Pyth Pro updates and enforce feed, freshness and market rules through Aiken validators.

The exact integration has not been implemented, independently reviewed or deployed on mainnet. Earlier testnets validated the surrounding collateral, oracle and trading architecture, not this provider-specific integration.

Catalyst will fund implementation, pre-production testing and independent validation, advancing it to TRL 7 mainnet deployment in Milestone 1 and toward TRL 8–9 through measured usage. These are standard providers, not adoption partners; no promotional commitments are assumed.
