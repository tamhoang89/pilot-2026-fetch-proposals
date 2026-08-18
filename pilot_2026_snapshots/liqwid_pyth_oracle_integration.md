# Liqwid Pyth Oracle Integration

> Pyth-verified prices for Liqwid V2 and Liqwid V3’s ADA and NIGHT markets.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 13
- **Proposer:** `stake1u880z6jcpa0ed2u87ruez7s4cavpqdh7d5x4qyffnzpmessqsd2ce`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-18T16:52:19.415000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Liqwid Labs will deliver this integration, with Kylix and Gustavo leading the technical work.

Gustavo will lead the implementation, including validator changes, transaction-building work, integration testing and preparation for mainnet deployment.

Kylix, will lead the product design and quality assurance of the Pyth integration.

Kylix:

- LinkedIn: <https://www.linkedin.com/in/kylix>
- GitHub: <https://github.com/kylixafonso>

Gustavo:

- LinkedIn: <https://www.linkedin.com/in/gustavo-roscoe>
- GitHub: <https://github.com/groscoe>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Genuine usage is defined as user lending activity: Supplies, Withdrawals, CreateLoan transactions, LoanModifications that change collateral or debt, and Liquidations. These are actions initiated by actual protocol users or liquidators for an economic purpose; oracle-update and batch transactions are not counted toward the target.

Pyth will be integrated into Liqwid’s ADA and NIGHT markets, so usage is generated naturally whenever users open, modify or close lending positions that depend on those prices (whether through ADA/NIGHT debt or collateral usage). We are therefore not relying on incentives, scripted wallets or transactions created solely to meet the target.

Liqwid is already a live protocol with approximately $12.4M TVL and $5.27M in active loans. The transaction target of 2,000 represents continued production activity during the adoption measurement period, with usage verifiable directly on-chain by classifying qualifying Liqwid transactions - this number alongside the fee target are based on conservative interpolation based on recent historical figures. We target ₳1,000+ in network fees from this genuine activity.

### How will you reach and onboard real users - and what evidence backs your channels?

Our go-to-market starts with an existing distribution channel rather than acquiring users individually: Liqwid’s live lending markets. Integrating Pyth into ADA and NIGHT markets immediately exposes the infrastructure to Liqwid borrowers, suppliers and liquidators whenever those markets use Pyth pricing.

The initial milestone is therefore real production usage, not testnet wallets or marketing sign-ups. We will work directly with the Liqwid team to integrate, test and deploy the price feeds, then monitor update activity and reliability after launch. From there, the same integration can expand to additional Liqwid markets and V3 with substantially less engineering work. Adoption can be evidenced through on-chain price updates, unique interacting addresses/contracts and the lending activity of markets using the feeds.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Liqwid can continue using its existing V2 oracle infrastructure, while Cardano-native alternatives include Orcfax and Charli3. Liqwid already aggregates multiple price sources and applies safeguards, so Pyth is not asking the protocol to replace a working system.

Our advantage is an additional independent, institution-grade pricing layer. Pyth Pro provides market data that can be verified on Cardano, while its pull-based model lets applications submit updates when needed. The integration is therefore complementary: add Pyth for ADA and NIGHT in V2, then carry the infrastructure into V3. Liqwid gains greater oracle diversity and resilience without discarding existing safeguards, and future markets can reuse the integration with much lower marginal engineering cost.

### Please provide details about the Technology Readiness Level selected for your existing product

Liqwid is a non-custodial Aave-style lending protocol live on Cardano mainnet, serving real users and real capital continuously since its launch in 2023. It currently secures approximately $12M TVL across 20+ markets and has been independently audited by VacuumLabs, mLabs and Anastasia Labs.

The protocol has operated through multiple periods of extreme market volatility, with liquidations executing as designed. Oracle price feeds, the component this proposal targets, are already running in production and are relied upon by every borrow, collateral withdrawal and liquidation on the protocol.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Today, Liqwid relies on an in-house off-chain system controlled by a single key, operated by Liqwid, to handle price discovery for every market supported by the protocol, meaning that the on-chain validators trust whatever said key publishes. This represents a single point of failure and high risk in case the private key is compromised.

The proposed integration moves verification on-chain. When a transaction needs a price (eg. a borrow, a withdrawal, a liquidation), it carries a signed Pyth update with it. Pyth’s own verification script checks that signature against Pyth’s published state inside that transaction, and Liqwid’s validators read the verified price in the same transaction. For assets with a supported Pyth feed, this price is used directly, while in-house system remains only for risk-capped CNTs that Pyth does not cover.

Liqwid’s trust assumption becomes Pyth’s publisher network and its signatures alongside Liqwid's operational guardrails rather than a single key held by Liqwid, considerably improving protocol security and decentralization.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Our initial target market is Liqwid’s live lending protocol and the users and contracts that depend on accurate asset pricing: suppliers, borrowers, liquidators and protocol infrastructure. This is an immediately addressable market rather than a hypothetical future audience. Liqwid is the leading Cardano lending protocol, with about $17.49M in liquidity and $5.3M in active loans, and its markets require reliable prices for collateral valuation, borrowing limits and liquidations.

The first production use case is Pyth pricing for ADA and NIGHT on Liqwid V2, with the integration designed to carry into V3 and expand to additional supported assets. Demand is therefore measurable on-chain through price updates, contracts/addresses consuming those updates, and lending activity in markets using Pyth.

Pyth Pro is already live on Cardano, with Cardano smart-contract integration documented by Pyth, so the core pricing infrastructure exists today. This proposal closes the remaining adoption gap by integrating that infrastructure into Liqwid, where it can serve real lending activity from launch.

### Applicant name

Liqwid Labs, LLC

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The grant funds the one-time integration work required to make Pyth production-ready for Liqwid. After launch, the integration does not depend on continued grant funding: Pyth’s pull-based architecture allows price updates to be submitted when applications need them, while Liqwid can retain Pyth as part of its long-term oracle infrastructure across V2 and V3.

The economic value comes from continued lending activity rather than a temporary incentive. Reliable, fresher pricing supports collateral valuation, borrowing and liquidations, so oracle usage grows with Liqwid’s markets. Once integrated, adding further Pyth-supported assets has a much lower marginal cost than the initial implementation. Our role is to deliver and maintain the Cardano integration; Liqwid benefits from stronger oracle resilience, while Pyth gains sustained on-chain usage from one of Cardano’s largest DeFi protocols.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Seeing that this is contract-level work on one of the protocol’s most safety-critical components and that the current oracle system works, it loses prioritisation over more pressing roadmap items. Funding is what would move it from “To Do” status to “In Progress”.

This funding will be spent on paying:

- Aiken contracts engineering to add the Pyth verification path to validators
- Off-chain rework of transaction building and update subscription
- A migration plan that switches live mainnet markets over without downtime or disruption to open loans
- An independent security audit of the new validator path

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of the 3-month window we will have Pyth price verification live on Cardano mainnet, in use by real users. Concretely:

- On-chain: a new version of Liqwid’s price-consuming validators that accepts a signed Pyth update within the transaction and verifies it through Pyth’s verification script.
- Off-chain: Liqwid’s transaction builders extended to subscribe to Pyth price feeds, attach the signed update to every price-dependent transaction, and fall back to the existing feed only for assets Pyth does not cover.
- Testnet:  end-to-end tests on Preview covering the price-dependent user flows - borrow, withdraw collateral and liquidation.
- Audit: Security review by an independent auditor, with the report and any resulting fixes included in the evidence.
- Mainnet: new validators deployed, ADA and NIGHT markets functioning properly, with open positions migrated without disruption. Evidence is a set of tx hashes from independent real-user runs of the protocol flows.

### Oracles - expected transaction count

2000

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Liqwid currently uses a permissioned oracle setup. A Liqwid-controlled key updates the oracle UTxO whose price the contracts accept. Our bot pulls market data off-chain, including Pyth prices via Hermes, and applies a 30min EMA before publishing the result. The contract can verify that an authorised wallet made an update, but not where the price came from.

This concentrates price integrity in a Liqwid-held key and service. If the key or system were compromised or failed, a bad price could be published and accepted by the protocol, affecting collateral, borrowing and liquidations.

We propose adopting onchain-witnessed Pyth prices via Pyth Pro. Borrow and liquidation transactions will use Pyth signed price updates, which are verified on chain by Pyth Pro’s Cardano integration and Liqwid validators. Liqwid will use Pyth prices as provided.

Liqwid no longer needs to only trust its private key to set the price, moving that assurance to Pyth’s signed publisher data. This removes a key single point of failure and makes the oracle path more decentralised and safer for users.

### Supporting links (repo, site, demo)

- https://github.com/Liqwid-Labs/liqwid-pyth-oracle
- https://app.liqwid.finance/
- https://x.com/LiqwidFinance

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

1000

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

Liqwid V2 will be source-available under BUSL by December 2026. Additionally, the Pyth oracle Plutus validators whose development is proposed for Liqwid V2 and V3 in this Catalyst proposal will be fully open-source under MIT.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Current funded commitments

Kylix and the Artifi Labs team are currently delivering the Fund 14 Catalyst project [Open Djed: Maintenance, Development and Infrastructure](https://projectcatalyst.io/funds/14/cardano-open-developers/open-djed-maintenance-development-and-infrastructure). Kylix is CEO of Artifi Labs and Technical Lead in Liqwid Labs. The Open Djed project is on track and in its maintenance phase from the team’s side.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

At this point, the integration is at the technical conceptualization/planning step. We have mapped how Pyth price feed updates would flow into Liqwid’s validators: a signed price update gets published only when verified on-chain by Pyth’s own verification scripts, and is read by Liqwid’s validators in that same transaction. However, this is limited to assets available in Pyth’s feeds, meaning this integration would only substitute price data for ADA and NIGHT, while maintaining the current architecture for CNTs.
