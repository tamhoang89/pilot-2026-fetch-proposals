# Fixed Rate Lending

> Predictable fixed-term yield with programmable principal and yield positions.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 14
- **Proposer:** `stake1uxvmpvst6rycjplpel59uv83kevs32xwux7mpz42xy6d5ccqqy5y8`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-20T04:57:25.452000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

## Why is your team well-suited to deliver this?\*

The team combines experience in blockchain engineering, Cardano smart contracts, backend systems, frontend applications, quality assurance and financial product development.

Core capabilities include:

- Cardano eUTXO architecture.
- Smart-contract development.


- Transaction construction.


- Backend services.
- Frontend DeFi applications.
- Protocol testing.


- Mainnet deployment.
- Production monitoring.

### Core Team

**Nguyen Hai Chau — Product Lead / Solution Architect**\
Responsible for product architecture and protocol design.

**Truong Quang Khang — FullStack development** \
Responsible for technical implementation and blockchain integration.

**Le Thi Thanh Ngan — QC** \
Responsible for quality assurance, test planning and release validation.

Most importantly, the team is not proposing its first Cardano application. 

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Real users generate transactions by participating in the Fixed Term Deposit lifecycle.

A depositor submits a transaction to enter a pool and receives pT/yT. Position holders may subsequently transfer these programmable assets or use them in supported DeFi integrations. At maturity, holders submit redemption transactions to recover principal and yield.

These interactions have genuine economic purpose: users commit capital to earn yield, manage fixed-term positions and redeem real deposited assets.

Our initial target is 50+ external wallets, 800+ eligible mainnet transactions and 20+ funded Fixed Term Deposit positions during the adoption period.

Each completed position naturally requires multiple lifecycle interactions, making this target achievable without manufacturing activity.

Team wallets, test transactions and artificially generated volume will be excluded. Required Catalyst transaction labeling will be implemented so eligible activity and associated network fees can be independently verified.

### How will you reach and onboard real users - and what evidence backs your channels?

User acquisition will focus initially on existing Cardano DeFi participants rather than users unfamiliar with blockchain.

The onboarding strategy includes:

- Public testnet campaigns.
- Cardano DeFi communities.
- Collaboration with stablecoin communities.
- Wallet and DeFi ecosystem partnerships.
- Educational documentation.
- Product walkthroughs.
- Community AMAs and demonstrations.
- Direct onboarding of lending and yield users.
- Integration with DeFi dashboards and analytics platforms.

The product has a straightforward user journey:

Connect wallet &gt; choose pool &gt; select amount &gt; deposit &gt; receive pT/yT &gt; monitor maturity &gt; redeem.

This reduces onboarding complexity for users already familiar with Cardano wallets and DeFi.

The Pilot itself will provide measurable validation through external wallet activity, deposits, pT/yT transactions and completed redemptions rather than relying solely on social-media metrics.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The main alternatives are open ended lending markets, where suppliers earn variable rates without a defined maturity, and traditional staking or liquidity provision strategies.

Protocols such as Liqwid provide valuable variable rate lending markets. Outside Cardano, protocols such as Pendle have demonstrated the usefulness of separating principal and yield exposure.

- Fixed maturity pools.
- Tokenized principal and yield positions.


- Existing mainnet users and liquidity.
- Programmable pT/yT positions that can support richer lifecycle and transfer rules.

We do not aim to replace variable rate lending. Fixed Term Deposit complements it by serving users who prefer defined time horizons and by creating additional financial primitives that other Cardano applications can integrate.

### Please provide details about the Technology Readiness Level selected for your existing product

The core Fixed Term Deposit architecture has been defined around Cardano's eUTXO model, including pool state, deposits, maturity, pT/yT issuance and redemption. Individual technical components use established Cardano primitives and have been validated through development prototypes and transaction-level testing. The product has not yet reached a production mainnet release. The Pilot will complete the integrated protocol, wallet-facing application, security validation and production deployment required to move from a controlled development environment to a live system used by external Cardano users.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Fixed Term Deposit uses Cardano's eUTXO model. A pool UTxO records the underlying asset, term, maturity and accounting state. When a supplier deposits, the protocol locks the underlying asset and issues two position assets: pT for principal and yT for yield. At maturity, the redemption transaction consumes the relevant position tokens and pool state, burns the redeemed tokens and releases the corresponding principal/yield.

For this Pilot, pT/yT issuance and transfers will be integrated with the CIP-0113 programmable-token framework. The minting/issuer logic remains tied to Dano's pool rules, while programmable transfer logic is invoked when these position assets move, allowing token-level rules to remain enforceable without changing the economic model of the fixed-term pool.

This fits Cardano because eUTXO provides deterministic pool state and maturity validation, while programmable tokens make pT/yT more composable and policy aware as they move between wallets or future DeFi integrations. The underlying deposit assets remain standard Cardano native assets.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The primary users are Cardano holders and DeFi participants who want to earn yield while having a clearly defined maturity period.

This includes:

- Stablecoin holders looking for yield opportunities.
- Existing lending-protocol users.
- Users who prefer predictable investment periods.
- DeFi users who want exposure to principal or yield independently.
- Liquidity providers and traders interested in tokenized yield positions.
- Other Cardano DeFi protocols that may integrate pT or yT.

The product can also become infrastructure for future fixed-term lending markets where borrowers and suppliers agree on capital for a known period rather than relying entirely on continuously changing lending conditions.

### Applicant name

Nguyen Hai Chau

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

DeFi protocol model in which revenue is generated from genuine financial activity across lending, borrowing, trading and related protocol services.

Fixed Term Deposit expands that activity. Users participate because they want to put capital to work for a defined period, borrowers require liquidity, and future traders or integrations can use the tokenized positions.

The Pilot funds the incremental technical integration, not ongoing operating expenses.

After the Pilot, the integration becomes part of Dano's production infrastructure. Maintenance and continued development are supported by protocol revenue and the broader Dano product ecosystem.

Usage does not depend on Catalyst rewards: users continue interacting because the protocol provides financial utility, earning yield, accessing liquidity, managing positions and potentially trading principal or yield exposure.

### Programmable tokens (CIP-0113) - expected transaction count

800

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This budget reflects the full cost of taking the CIP-0113 integration from architecture (current TRL 2) through smart-contract implementation

Budget breakdown:

- Smart-contract engineering (pT/yT programmable-token minting, transfer, issuer logic): ₳54,000 (45%)
- Off-chain transaction building & wallet integration: ₳18,000 (15%)
- Third-party security audit of the programmable-token integration: ₳21,600 (18%)
- QA & test planning (unit tests, integration tests, preprod validation): ₳9,600 (8%)
- Testnet & mainnet deployment, infrastructure and monitoring: ₳7,200 (6%)
- Documentation & release notes: ₳4,800 (4%)
- Adoption measurement tooling, onboarding campaigns and community engagement (AMAs, testnet campaign, dashboard integration): ₳4,800 (4%)

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery is month 2 of the 3-month window to allow additional time for adoption measurement.

**Acceptance evidence:**

- A working preprod Fixed Term Deposit pool
- Successful deposit transactions using supported assets
- pT and yT minted correctly for deposited positions
- Transaction hashes showing deposit and token issuance
- Published preprod script hashes and policy IDs


- Repository commit/tag matching the deployed preprod version
- Technical walkthrough demonstrating the deposit-to-pT/yT flow

**M1 Evidence:**

- Finalized Fixed Term Deposit protocol specification
- On-chain pool state and lifecycle architecture


- pT/yT minting policies for principal and yield positions
- Initial CIP-0113 programmable-token integration


- Preprod deployment of the core Fixed Term Deposit flow

M1 will demonstrate that a user can deposit supported assets into a Fixed Term Deposit pool on Cardano preprod and receive valid programmable pT/yT positions representing principal and yield.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

175

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Fixed Term Deposit gives Cardano users a way to commit assets for a defined maturity period and receive tokenized positions representing principal and yield.

When a supplier deposits assets into a fixed-term pool, the position is represented by two tokens:

- pT — Principal Token, representing the principal component.
- yT — Yield Token, representing the yield component.

At maturity, token holders can redeem the corresponding principal and yield. Separating these components also makes the position composable: principal and yield exposure can be held or transferred independently and later integrated with secondary markets or other DeFi protocols.

The product addresses users who want more predictable time-based yield opportunities than open-ended, variable-rate lending alone provides.

For this Pilot, we will extend the Fixed Term Deposit architecture by integrating programmable pT/yT position tokens, giving these financial positions enforceable token- evel behaviour while preserving their existing fixed-term economic model.

### Supporting links (repo, site, demo)

- https://github.com/Truongquangkhang/fixed-rate-lending

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

Smart contracts are open source, and the smart contracts and technical components developed for the proposed programmable-token integration will also be published publicly. Product-specific frontend, backend, infrastructure and operational components may remain closed source.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The role of programmable tokens within Fixed Term Deposit has been defined: pT and yT represent principal and yield positions, while programmable-token logic governs relevant lifecycle and transfer behaviour. The integration architecture and required contract boundaries have been identified, but the complete programmable-token implementation has not yet been integrated into the production protocol. Pilot funding will move this from architecture into smart-contract implementation, preprod validation, wallet integration, security testing and mainnet deployment.
