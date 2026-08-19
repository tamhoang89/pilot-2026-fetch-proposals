# Regulated BRL Settlement on Cardano

> This submission extends PagFinance’s existing settlement infrastructure into the Cardano Ecosystem as a regulated BRL settlement layer.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 2
- **Proposer:** `stake1u8aa69fce89s9hwrhl7rqk3xuvlag0ntruwvw2kp347z0squyrl2m`
- **Funding requested:** ₳185,000
- **Last finalized:** 2026-08-19T17:19:17.742000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Andre Straube, Founder & CEO: developer with 20+ years of experience. Former Tech Lead and Partner at Mottu, where he also served the Fintech Division and scaled the company from pre-seed to Series C. Ex-Siemens, also founded iDooh Media, with a successful exit.\
\
Alexandre Bencz, Partner & CTO: deep experience building scalable technology major financial institutions. Ex-Google and Ex-Mottu, Alexandre developed critical systems for banks including Itaú, Bradesco and Santander, operating in highly regulated environments and working closely with regulatory authorities.\
\
Matheus Almeida, Co-founder & CTO: Six years of experience across financial governance and regulatory compliance, with a strong track record of working directly with leading ecosystems such as Polygon, Canton Network and Ripple, driving ecosystem expansion.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**N/A**

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Usage is organic because users and businesses have an ongoing need to convert digital assets into BRL and settle locally via PIX. \
\
300 transactions averages roughly 10 per day, and we want to be transparent: Cardano's stablecoin capitalisation is still small and we have no historical data of our own on this network. We set targets we can defend under the daily cap rather than targets that only look better on paper.\
\
We will not incentivise transactions with giveaways or airdrops, consistent with programme rules. Growth comes from direct onboarding of the two recurring segments, documentation, and our existing distribution: web, mobile, and Partner API.

### How will you reach and onboard real users - and what evidence backs your channels?

We will acquire users through the Cardano community, ecosystem partners, direct B2B integrations and also retail marketing. Projects can embed BRL payouts through our B2B Partner API, creating a distribution channel directly to their existing users.

PagFinance already operates crypto-to-BRL settlement infrastructure in Brazil, with live partners and clients that can port their transactions over to Cardano. This gives us an existing distribution base and a clear path to real transaction volume from launch.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, Cardano users must bridge to another chain, use a centralized exchange such as Binance or OTC desk, and then withdraw BRL. Existing on/off-ramp providers solve parts of this flow, but none offer a native Cardano → BRL route.

PagFinance wins because it removes all these steps. Users sign one transaction from their own wallet and receive BRL directly in their bank account via PIX, with no exchange account, order book, or custody. For Cardano projects, our B2B API provides the same BRL payout infrastructure without requiring them to become a regulated entity.

### Please provide details about the Technology Readiness Level selected for your existing product

PagFinance is a revenue-generating payment business processing live customer money daily, not a prototype.

\- **Regulatory readiness:** operating under the Brazilian Central Bank's VASP framework for virtual asset service providers, with ongoing compliance and reporting obligations

\- **Volume traction:** 40k+ settled transactions, US$ 5M+ processed

\- **Sustainability:** cash-flow positive in year one, without external funding

\- **Multi-chain readiness:** twelve networks live across both account-based and UTXO ledgers, so our settlement, treasury and reconciliation layers are already model-agnostic

\- **Full stack:** KYC pipeline, transaction monitoring, internal treasury console, web and mobile apps, and a B2B Partner API used by external partners

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Flow:** Users connect a CIP-30 wallet (Lace, Eternl, Vespr, Typhon, Yoroi) or our mobile app and sign one transaction sending ADA/USDCx to a per-user CIP-1852 deposit address with a registered metadata payment reference. Our indexer validates the asset via CIP-26, applies value-tier confirmation rules, and releases BRL via PIX through our regulated banking partner.

**Data layer:** A managed provider is backed by an independent community provider behind one internal interface. This allows migration to Ogmios/Kupo or Dolos without application changes. Reconciliation checks block hash and slot against the last known tip.

**Treasury:** Deposits sweep into a denominated UTXO pool. Workers atomically reserve UTXOs before construction, preventing concurrent selection. Collateral is kept in a separate ADA-only pool. Signing is isolated so application services never access keys.

**Why eUTXO fits:** Deterministic fees allow exact BRL quotes before execution. Atomic transactions eliminate partial settlement states. Native USDCx avoids approvals, allowances, and token-contract risk, requiring one signature. Native metadata provides an auditable reconciliation reference without a separate program.

We deliberately keep a custom validator out of scope for the pilot. We have specified a future payment-receiver validator, but shipping an audited, revenue-generating offramp is more valuable than an unaudited validator within the programme window.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

PagFinance is live, in production, and revenue-generating. We are not looking for product-market fit, we are extending an existing one to a new chain. Traction:

\- More than US$ 5M processed across more than 40,000 settled transactions.

\- Approximately 11% compounded month-over-month growth.

\- Cash-flow positive within our first year.

\- Operating under Brazil's BCB PSAV framework, with KYC, onboarding and transaction monitoring already in production.

\- B2B Partner API in production, letting third parties embed BRL settlement without holding a license.

Core segments: freelancers and contractors converting crypto income, expatriates in Brazil, traders realising gains locally, businesses paying suppliers in BRL and traditional businesses using Cardano for cross-border transactions and FX settlement into Brazil. We are the inverse of a USD neobank: instead of helping Brazilians hold dollars, we help globally-earned digital dollars land as local currency.

### Applicant name

PagFinance

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

PagFinance generates revenue from FX spreads and transaction fees on crypto-to-BRL settlement. End users pay for the conversion, while Cardano projects can integrate our B2B Partner API and pay for BRL payout infrastructure.

The pilot funds initial integration and ecosystem adoption, but the underlying infrastructure is already part of PagFinance’s core business. Once live, usage continues because users and businesses have an ongoing need to convert digital assets into BRL and settle locally via PIX. As Cardano transaction volume grows, PagFinance earns recurring revenue from every settlement.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

We are profitable and self-funding; this grant accelerates sequencing. Without it, Cardano would be a 2027 integration. With it, we ship it this quarter.

The larger impact is shared infrastructure: an embedded BRL payout rail, abstracting the Brazilian regulatory and banking complexity. With USDCx now live on Cardano, the ecosystem has the stablecoin liquidity needed for this use case, while PagFinance provides the missing local settlement layer.

**Budget:** 60% engineering, 15% security, 10% infrastructure, 10% compliance, 5% documentation/ecosystem.

Granted ADA will be converted to operating currency on receipt, consistent with our treasury policy for non-BRL inflows.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1.  **Cardano offramp live in production**, supporting ADA and USDCx with BRL settlement over PIX.

2. **Cardano onramp live in production**, supporting ADA and USDCx with BRL deposits via PIX.

3. **Cardano support in the B2B Partner API**, publicly documented.

4. **Public technical documentation** covering architecture, assets, confirmations and API.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

PagFinance is crypto-to-fiat payment infrastructure in Brazil. We convert stablecoins to Brazilian reais and settle to any bank account over PIX, Brazil's instant payment rail, operating under the Central Bank of Brazil's PSAV framework.

We are building a native Cardano offramp: a user signs one transaction from their own wallet with ADA or USDCx and receives BRL in their bank account, with no exchange account and no order book.

The problem is specific and currently unsolved. Brazilians holding value on Cardano have no direct path to local currency. They must bridge to another chain, deposit to a centralised exchange, sell into a BRL book, and withdraw. That is multiple hours, several counterparty risks, and compounding spread at each hop. It is also a common reason Brazilian users leave a chain: liquidity that cannot reach the local economy is not liquidity.

Who this serves: Brazilian freelancers and businesses receiving USDCx from international clients; Cardano projects that need to offer BRL payouts to their users through our B2B Partner API without becoming a regulated entity themselves; Brazilian users holding ADA or USDCx who need to pay local expenses in BRL; and traditional businesses using Cardano for cross-border transactions and FX settlement into Brazil.

### Supporting links (repo, site, demo)

- https://pag.finance/pt
- https://pag.finance/pt/businesses
- https://github.com/PagCrypto

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

250

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

347

### Current funded commitments

We're currently shipping a funded BRL settlement layer on Stellar as well.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We completed a full technical assessment and architecture specification covering eUTXO, CIP-30 wallet connection, provider selection, treasury UTXO management, minimum-ADA handling, CIP-26 decimals, and confirmation-depth policies. Components were validated on Cardano testnets; nothing is deployed to mainnet.

Key risks are already designed against:

1. **UTXO contention:** denominated UTXO pools, pessimistic reservation and bounded chaining.

2. **Minimum ADA:** explicitly accounted for in the ledger.

3. **Finality:** tiered confirmation-depth policy by transaction value.

4. **Signing:** BIP32-Ed25519/CIP-1852 requires an isolated offline signing service with independent review.

We assess this as **TRL 4**.
