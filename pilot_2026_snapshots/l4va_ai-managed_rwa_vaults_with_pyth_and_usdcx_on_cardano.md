# L4VA: AI-Managed RWA Vaults with Pyth and USDCx on Cardano

> L4VA shipped RWA backed vault tokens with decentralized governance on Cardano mainnet in Q1 2026. This proposal enables AI vault configuration and AI market actions driven by decentralized governance.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 18
- **Proposer:** `stake1uxxzr3kdrltfpgwx8zf7vh0jj44c6rdut4rjsegpcnzcw7gayt263`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T04:18:45.582000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

L4VA is a proven Catalyst delivery team, not a new team assembling around a grant. Engineering is led by **Vladyslav Koshevoi**, with **Anton Hrabarchuk** and **Ihor Kordiukov**, supported by veteran architects/engineers **Aric Fedida** and **Nick Goehner** and Cardano advisor **Adrian Fanatiu**.

Most importantly, we have already delivered for Catalyst. Our **Fund 12 proposal successfully closed out** after 100,000 ADA helped take L4VA from design and testnet through completion of the full RWA vault dApp on Cardano mainnet. The team subsidized substantial development costs beyond the grant and has demonstrated additional fundraising capability.

That infrastructure has already reached approximately **350,000 ADA in TVL** through early adoption. This pilot extends a shipped, funded and adopted Cardano product rather than starting from zero—giving Catalyst high leverage on a team and infrastructure it has already helped validate.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

L4VA pledges **5% of Cardano protocol fee revenue for 24 months** after mainnet deployment, capped at **100% of the original grant amount**. This excludes token sales, fundraising proceeds, treasury assets, and revenue from other networks.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

L4VA will generate genuine usage from **existing and new Vault participants interacting with real RWA-backed strategies**. Users will transact when they acquire or trade Vault Tokens, provide liquidity, contribute assets, vote on governance actions, or when approved Vault strategies execute allocation or market actions.

We currently have approximately **1,500 assets locked and 350,000 ADA in TVL**, so the pilot begins with an existing base of economic activity rather than hypothetical demand.

Our targets of **5,000 oracle-enabled transactions and 10,000 stablecoin transactions** are reasonable but ambitious. Pyth will be used for RWA pricing, NAV calculations and AI strategy decisions, while USDCx will support settlement, liquidity, acquisitions and portfolio allocation.

That equates to only a few oracle and stablecoin interactions per existing locked asset over the pilot period, while still requiring meaningful growth in Vault usage. Transactions will be driven by real users, governance decisions and strategy activity—not artificial or circular volume created to satisfy grant metrics.

### How will you reach and onboard real users - and what evidence backs your channels?

We will start with the audience L4VA already reaches: Cardano vault creators, token holders, DeFi users, RWA issuers and ecosystem partners. Onboarding will happen through existing L4VA channels, direct issuer partnerships, Cardano ecosystem integrations and simple strategy templates that let creators configure AI-enabled Vaults without building AI or smart-contract infrastructure from scratch.

Our strongest channel evidence is the protocol itself: L4VA has already launched on Cardano mainnet and attracted real vault creation, asset contributions, governance participation and liquidity. That gives us an existing product, community and partner base to convert into pilot users rather than starting from zero.

The pilot will launch a small number of real AI-enabled Vaults first, publish transparent governance and performance data, then use those working examples to onboard additional issuers, communities and developers across Cardano.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives exist in pieces: tokenization platforms issue RWAs, DeFi vaults automate crypto strategies, centralized robo-advisors manage portfolios, and AI trading agents execute trades. Few combine all four functions L4VA brings together: RWA fractionalization, liquid Vault Tokens, decentralized governance and AI actions constrained by on-chain mandates.

L4VA’s advantage is that this is not a new AI wrapper. The underlying Vault infrastructure is already live on Cardano mainnet. AI becomes an execution layer inside an existing governance and asset-management primitive, creating transparent limits, auditable actions and community control instead of handing unrestricted discretion to a black-box agent.

### Please provide details about the Technology Readiness Level selected for your existing product

L4VA is already live on Cardano mainnet as a functioning dApp. Users can create asset-backed Vaults, contribute assets, fractionalize those assets into fungible Vault Tokens, acquire and trade Vault Tokens, provide liquidity and participate in decentralized governance.

The platform was delivered following L4VA’s successful Fund 12 Catalyst closeout. The 100,000 ADA grant helped fund development, while the team subsidized substantial additional development and operating costs through its own capital and other fundraising.

Early adoption has already resulted in approximately **350,000 ADA in TVL** across L4VA Vaults.

This proposal therefore extends an operational protocol rather than funding a new product from scratch.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

L4VA uses a **hybrid on-chain/off-chain architecture** designed to combine transparent token ownership and governance with flexible market execution.

Vault ownership and voting power are represented by Vault Tokens on Cardano. Governance proposals are submitted to Vault communities, with voting power determined by wallet holdings. Vote collection and tallying can occur through L4VA’s off-chain infrastructure, which reads verifiable on-chain token balances and triggers approved actions through authenticated APIs.

AI agents operate within this same framework. They consume **Pyth price data**, Vault state and market information to recommend or initiate actions permitted by the Vault’s governance mandate. Approved actions—such as rebalancing, trading or liquidity management—may be executed through off-chain APIs that interact with Cardano markets and protocols.

**USDCx** provides stable settlement, liquidity and portfolio allocation, while Pyth supplies trusted pricing for RWA valuation, NAV and AI decisions.

This architecture keeps **ownership, assets and voting power verifiable on Cardano**, while using off-chain APIs for computation, vote tallying and efficient market execution.

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

L4VA’s target market is RWA issuers, on-chain asset managers, DAOs and Cardano users who want to create and participate in programmable investment strategies without relying on a centralized manager.

Demand is already visible in the product we have shipped. L4VA is live on Cardano mainnet with RWA-backed Vault Tokens, fractional ownership, decentralized governance and secondary-market liquidity. The protocol has already supported multiple live vaults and real assets, proving users will create, hold, trade and govern vault-based products.

The AI pilot addresses the next need from that market: once assets are tokenized, they still require monitoring, allocation, liquidity management and ongoing decisions. Today that work is manual or centralized. L4VA enables creators to encode objectives and risk limits, then let AI agents execute or propose actions inside governance-defined boundaries.

The opportunity is not simply “AI for crypto trading.” It is an intelligent management layer for Cardano’s growing tokenized-asset economy.

### Applicant name

L4VA Technologies inc.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

L4VA is designed to sustain itself through usage-based protocol fees rather than grant funding or a percentage of assets under management. Vault creators, issuers and users pay infrastructure fees when they use fee-generating protocol functions such as creating and expanding vaults, trading through L4VA interfaces and executing supported strategy actions.

The AI pilot adds new utility to infrastructure that is already deployed, rather than creating a standalone grant-dependent product. As more assets and strategies use L4VA, recurring management, governance, trading and liquidity activity creates ongoing protocol usage.

This aligns incentives: issuers gain distribution and programmable strategy infrastructure; users gain access to transparent, governable strategies; and L4VA earns revenue when the infrastructure is actually used. Grant funding accelerates the AI layer, but long-term sustainability comes from protocol activity.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Catalyst funding will accelerate L4VA from **active R&D into a working AI-enabled RWA Vault pilot on Cardano**. The underlying protocol is already live on mainnet, and the team has already begun Pyth Oracle and USDCx integration work using its own resources.

Funding will support **AI agent development, Pyth and USDCx integration, governance and execution logic, API infrastructure, smart-contract updates, security testing, UI/UX and pilot deployment**.

Catalyst is therefore not funding a new dApp or initial feasibility research. It is leveraging an operational Cardano protocol and existing team-funded R&D to accelerate a new capability toward production.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, L4VA will deliver a **working first version of AI-enabled Vault functionality** integrated into its existing Cardano mainnet protocol.

- Implement initial **Pyth Oracle support** for selected asset pricing, Vault valuation and AI inputs.

- Implement **USDCx support** for selected settlement, liquidity and allocation use cases.

- Deliver an initial **AI Vault configuration interface** for objectives, allocation parameters and permitted actions.

- Extend governance so approved Vault votes can authorize selected **AI/API-driven market actions**.

- Build and test at least **one pilot AI-enabled Vault strategy**.

- Test core permissions, transaction execution, monitoring and error handling.

- Deliver required UI/UX and technical documentation.

- Deploy supported functionality to **Cardano mainnet** and demonstrate a live workflow using oracle data, USDCx and governance-directed execution.

### Oracles - expected transaction count

500

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

L4VA is building an **AI-powered RWA investment strategy primitive for Cardano** that turns tokenized real-world assets from static tokens into liquid, programmable and intelligently managed on-chain strategies.

L4VA has already shipped **RWA-backed Vault Tokens with decentralized governance on Cardano mainnet**, enabling fractional ownership, liquidity and community-controlled asset management.

The problem is that **tokenization alone does not solve asset management**. Once an RWA is on-chain, issuers and communities still need to manage allocation, liquidity, risk and changing market conditions. Today, those functions are often manual, fragmented or dependent on centralized managers.

This Catalyst pilot adds **AI-directed execution within governance-defined boundaries**. Vault creators can define objectives, risk limits, allocation rules and governance mandates. AI agents can then analyze oracle, market and on-chain data and take or propose permitted actions such as rebalancing, liquidity management and allocation changes.

The AI remains constrained by transparent on-chain rules and decentralized governance.

The result: **Cardano-native infrastructure for RWA issuers, communities and developers to create adaptive investment strategies without surrendering control to a centralized asset manager.**

**Tokenization makes assets digital. L4VA makes them programmable. AI makes the strategy adaptive.**

### Supporting links (repo, site, demo)

- https://github.com/L4VA-Technologies-Inc/
- https://l4va.com
- https://app.l4va.org

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

### Licensing / IP details

### **GNU General Public License v3.0**

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

L4VA is already conducting **R&D on Pyth Oracle and USDCx integrations** for its Cardano Vault architecture, so this work is beyond initial technical discovery.

We classify the proposed integration at approximately **TRL 5**. The underlying L4VA protocol is already live on Cardano mainnet at TRL 9, while Pyth and USDCx are progressing through technical design, development and validation.

Pyth will support RWA pricing, NAV calculations and AI strategy decisions, while USDCx will provide stable settlement, liquidity and portfolio allocation. Catalyst funding will accelerate this existing work and connect it to the AI strategy layer, moving from active R&D toward working AI-enabled Vault pilots and production deployment.
