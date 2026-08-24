# Fixed Rate Lending

> Predictable fixed-term yield with programmable principal and yield positions.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 21
- **Proposer:** `stake1uxvmpvst6rycjplpel59uv83kevs32xwux7mpz42xy6d5ccqqy5y8`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-24T04:48:42.494000+00:00

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
Responsible for product architecture and protocol design.\
<https://www.linkedin.com/in/hai-chau-nguyen-732817174/>

**Truong Quang Khang — FullStack development** \
Responsible for technical implementation and blockchain integration. <https://www.linkedin.com/in/quang-khang-7a96ba279/>

**Le Thi Thanh Ngan — QC** \
Responsible for quality assurance, test planning and release validation.\
<https://www.linkedin.com/in/thi-thanh-ngan-le/>

Most importantly, the team is not proposing its first Cardano application.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Expected transaction count: 800**

Keep **800**.

## Update:

**Fee target**

Change:

**₳175**

to:

**₳300**

## Update field:

**QHow will your product generate genuine usage - who transacts, why, and how often?**

Replace with:

Real usage is generated through economically meaningful PT/YT lifecycle activity.

During the adoption measurement period, the target is:

- 120+ external wallets.
- 250 funded Fixed Term Deposit positions.
- 300 genuine PT/YT owner-transfer transactions.
- 250 completed maturity/redemption transactions.

The 800 eligible mainnet transaction target is therefore based on:

- **250 funded-position / PT-YT issuance transactions**
- **300 genuine PT/YT owner-transfer transactions**
- **250 maturity/redemption transactions**

**250 + 300 + 250 = 800 eligible mainnet transactions.**

Each category represents genuine economic activity rather than manufactured transaction volume.

The fee target is at least **₳300**.

Across 800 transactions, this corresponds to an average network fee of approximately **₳0.375 per eligible transaction**.

The transaction-cost assumption will be validated against measured CIP-0113 execution costs during preprod testing.

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

The existing Fixed Rate Lending / Fixed Term Deposit foundation is assessed at TRL 5. Core Cardano eUTXO components covering Protocol Config, Pool and Loan state, fixed maturity, PT/YT issuance and redemption have been implemented, with versioned Pool and Loan validators (v1.0.0) deployed on a Cardano test network. The deployed Pool validator has script hash `fbfe1688e61ff0e52da1ccbaf1b3a601c66b670272ddb5e197ca39bd` and reference UTxO `8a7b8a548cb04398eaa78e4160046f749e5ba865168489e751a173c3a99266ea#0`. Additional script hashes, addresses, deployment transactions and architecture evidence are published in the project README and HLD. The proposed CIP-0113 integration is a separate new layer currently assessed at TRL 2.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Fixed Term Deposit uses Cardano's eUTXO architecture with separate Pool and Loan state.

A Pool UTxO records the supplied asset, PT/YT accounting, maturity, supported collateral, active-loan state and fee state.

Creating a Pool:

1. validates Pool configuration
2. creates the Pool UTxO
3. mints a unique Pool NFT
4. issues PT representing the principal position
5. issues YT representing the yield position.

Loan UTxOs separately record borrower debt, maturity and collateral.

At maturity, redemption is enforced by the Pool validator. The Pool must have reached maturity, outstanding Pool debt must be resolved, and assets released must correspond to the PT and/or YT burned.

For this Pilot, PT/YT are extended using CIP-0113 programmable-token infrastructure.

### Issuance and burn

PT/YT may only be issued through valid Fixed Term Deposit Pool lifecycle transactions. Arbitrary issuance is rejected.

Burning is permitted as part of valid redemption or other explicitly defined lifecycle operations.

### Ownership and transfer

PT and YT represent quantity-based claims.

A holder may transfer all or part of a PT or YT balance through registered owner-transfer logic.

### Maturity

Maturity remains a property of the originating Pool.

Moving PT or YT between wallets cannot change Pool maturity.

### Redemption

At maturity, redemption burns the relevant PT and/or YT and reduces the Pool's outstanding liability by the corresponding quantity

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

The Pilot does not fund creation of the underlying Fixed Term Deposit economic protocol.

The existing protocol architecture already defines:

- Pool and Loan state.
- Fixed maturity.
- Collateralized borrowing.
- PT and YT economic claims.
- Core redemption rules.

Pilot funding is specifically for the incremental CIP-0113 integration required to make PT/YT programmable.

The funded work includes:

- CIP-0113 token registration.
- PT/YT issuance and burn validation.
- Owner-transfer validation.
- Third-party-transfer policy.
- Integration-specific transaction construction.


- Automated integration testing.


- Test-network and mainnet deployment.
- Transaction labeling and adoption measurement.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery: by the end of Month 2, leaving the remaining period for adoption measurement.

**M1 Outputs**

- Finalized Fixed Term Deposit + CIP-0113 integration specification.

- PT/YT programmable issuance, burn and owner-transfer logic.

- Third-party-transfer policy and CIP-0113 registry integration.

- Off-chain transaction builder and wallet integration.

- Automated unit/integration tests and end-to-end preprod validation.

- Cardano mainnet deployment with Catalyst transaction labeling.

**Acceptance Evidence**

- Public repository release/tag.

- Published mainnet validator hashes, PT/YT policy IDs and registry information.

- Mainnet transaction showing funded-position creation and programmable PT/YT issuance.

- Mainnet PT/YT transfer transaction.

- Mainnet redemption transaction where maturity permits.

- Technical walkthrough and published test/security notes.

Mainnet deployment and verifiable mainnet activity are the M1 acceptance condition.

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

The smart contracts and technical specifications associated with the Fixed Term Deposit protocol and the proposed CIP-0113 programmable-token integration will be published publicly.

This includes the programmable-token validators, integration specifications, deployment references, architecture documentation and integration-specific test artifacts

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
