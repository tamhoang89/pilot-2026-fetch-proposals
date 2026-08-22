# Rvess: Stablecoins to African Mobile Mone

> A new Cardano mainnet integration converting verified stablecoins into local mobile-money payouts, starting in Uganda and expanding across Africa.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 23
- **Proposer:** `stake1uyqe7s205xndy8l4c32pakhldsmp0wrpj75lzhpfmw79ntck5hhzr`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-22T17:14:39.857000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Mwijusya Oliseh: Founder and Product Lead. \
Created Rvess Pay and built [SovAds](https://sovads.org). Leads product strategy, Cardano integration, backend development, infrastructure, and delivery.\
GitHub: <https://github.com/Olisehgenesis/> · LinkedIn: <https://www.linkedin.com/in/olisehgenesis/>

Atwebembeire Samuel :Software Developer. \
Supports implementation, testing, technical documentation, and mainnet readiness.\
GitHub: <https://github.com/sam-thetutor>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A. Rvess is prioritizing sustainable operations, regulatory compliance, liquidity, and continued product development after the pilot. We do not want to make a repayment or revenue-share commitment before production unit economics are verified.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Target: 80 users, 240 transactions, 60 ADA fees. 

Current active users: \~30 from [rvess.xyz](http://rvess.xyz) beta

New external users: \~50 from Week 1 campus activations

Week 1: Campus partnerships with:

\- Mukasa Web3 (@web3_muk) — Makerere/Kyambogo campus activation

Week 2: DevFest Uganda

\- Blockchain Dev Fest Uganda (@BChainDevFest) — developer community outreach

Each user expected \~3 transactions = 240 total transactions

Dune Analytics verification: distinct wallets, fee tracking, retentionUsers are Ugandan freelancers, students, remote workers, and Cardano contributors who transact to convert stablecoins into UGX via MarzPay. Only independent external-user transactions count; no team-controlled wallets.

Verification: Dune Analytics dashboard tracks distinct wallets, transaction volume per user, and retention.

### How will you reach and onboard real users - and what evidence backs your channels?

Rvess is operated by Buildfi Tech UG Ltd (URSB ERN 80034893783008, registered, status: Compliant). We hold a live Relworx merchant account (RELC479A9A03C), covering MTN MoMo/Airtel payout across Kenya, Uganda, and East Africa - already integrated into the pilot. We also hold a MarzPay account (251757317597, merchant 323175), a lower-rate Uganda-only gateway not yet wired in; that integration is new work funded here.

Channels: (1) Planned campus activations at Makerere and Kyambogo University, Kampala, targeting tech/CS/blockchain-adjacent students. (2) Kampala Cardano and freelancer communities via demonstrations, meetups, referrals. (3) Field events at both in weeks one and two.

Target: 400 users, 1,150 transactions, 400 ADA fees. Week 1: campus activations. Week 2: Kampala/Cardano expansion. Dune tracks external wallets; no scripted usage.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralized exchanges, Binance P2P, Yellow Card, Kotani Pay, OTC brokers, and manual mobile-money exchanges.

Rvess provides a Cardano-native workflow with verified stablecoin checks, transparent quotes and fees, mobile-money payouts, on-chain attribution, and transaction tracking. Wallets and dApps will also be able to embed this settlement route.

### Please provide details about the Technology Readiness Level selected for your existing product

Rvess Pay is **live** at <https://rvess.xyz> as a working Cardano payment product for African markets. The deployed system includes Cardano wallet connectivity, live exchange-rate quoting, country and mobile-money provider selection, transaction creation, deposit monitoring, payout routing, status tracking, receipts, and an operations dashboard. The architecture supports Uganda, Kenya, and Tanzania, with integrations for MTN MoMo, Airtel Money, and M-Pesa. The product has been demonstrated in its intended web environment. The proposed stablecoin settlement capability is new work and is assessed separately below.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Rvess uses a Cardano-first settlement architecture. A user connects a Cardano wallet, selects an approved stablecoin and mobile-money destination, and receives a transparent local-currency quote. Each transaction receives a unique reference and expected asset amount.

The integration will maintain an allowlist of verified stablecoin policy IDs and asset names. Deposit monitoring will verify the policy ID, quantity, sender wallet, destination address, transaction reference, and required mainnet confirmations before allowing payout. Confirmation-time rates will determine the final local settlement amount.

A state machine records each transition from quote and deposit detection through confirmation, payout processing, and completion. Append-only ledger entries prevent duplicate accounting, while idempotent workers and signed provider callbacks protect against repeated payouts.

Catalyst transactions will include the required standardized label. Dune Analytics will measure network fees, distinct external wallets, transaction frequency, and retained usage. This architecture fits stablecoin settlement because it verifies the native Cardano asset on-chain while connecting confirmed value to familiar African mobile-money rails.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Our initial users are Ugandan freelancers, remote workers, Cardano contributors, merchants, and families receiving cross-border payments through mobile money. Rvess will first convert verified Cardano stablecoins into UGX payouts through Relworx (which handles MTN MoMo and Airtel Money on our behalf), then expand to Kenya and Tanzania.

GSMA reports over one billion registered mobile-money accounts in Sub-Saharan Africa, demonstrating the importance of these payment rails. Rvess has a public beta at <https://rvess.xyz> but has not processed production payouts, so we do not yet claim product-market fit. Pilot registrations, interviews, and partner commitments will provide direct validation.

Reference: <https://www.gsma.com/sotir/>

### Applicant name

Oliseh Genesis

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Rvess will earn a disclosed transaction fee and exchange spread on completed settlements. Users pay for a single tracked conversion from Cardano stablecoins to mobile money.

Wallets, dApps, and payment businesses may also pay per API settlement or through volume pricing. After the pilot, transaction revenue will cover provider charges, infrastructure, compliance, liquidity, and support. Repeated remittances, freelance earnings, rewards, and merchant payments create continuing demand.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Rvess's Cardano pilot already has a live Relworx account (RELC479A9A03C): payout, deposit monitoring, ledger, state machine, webhooks, dashboard.

It funds: (1) stablecoin-specific work quoting, rate locking, ledger extensions, new trigger into existing Relworx payout; \
(2) new MarzPay integration (251757317597, merchant 323175), a lower-rate Uganda-only gateway not yet wired in.\
policy/quoting: 26,000 ADA (35%)\
Ledger extension: 11,000 ADA (15%)\
MarzPay integration+routing: 13,000 ADA (17%)\
Security audit: 7,500 ADA (10%)\
Compliance & Uganda onboarding: **11,250 ADA** (15%)\
monitoring: 4,750 ADA (6%)\
Demo Day: 1,500 ADA (2%)

Total: 75,000 ADA\
Mobile-money settlement (fiat reserve for payout timing gaps) is funded separately by team and is not included in this grant request.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

**M1 Outputs**

1\. Deploy a live Cardano mainnet flow at <https://rvess.xyz> converting approved USDM or USDCx into UGX payouts through MTN MoMo and Airtel Money.

2\. Implement wallet asset detection, verified policy allowlisting, transparent quotes, deposit verification, confirmations, payout reconciliation, transaction tracking, and receipts.

3\. Add the required Catalyst transaction label and a public Dune dashboard tracking fees, transactions, and distinct external wallets.

4\. Complete at least two repeatable end-to-end mainnet settlements initiated by independent real users.

5\. Publish transaction hashes, declared identifiers, architecture documentation, release notes, walkthrough video, test evidence, and present the working product at Demo Day.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

African freelancers, remote workers, merchants, and families receiving cross-border payments often depend on mobile money for everyday spending. Cardano assets cannot currently move directly into services such as MTN MoMo, Airtel Money, and M-Pesa through a simple, locally focused experience. Users must rely on fragmented exchanges, intermediaries, and manual conversions with unclear fees and settlement times.

Rvess Pay will build a new Cardano mainnet integration that enables users to convert verified Cardano stablecoins, initially USDM or USDCx, into local mobile-money payouts. The first production market will be Uganda, supporting UGX settlement to MTN MoMo and Airtel Money, followed by expansion into other supported African markets.

A user will connect a Cardano wallet, select a supported stablecoin, view the exchange rate, fees, and expected local payout, provide the recipient’s mobile-money number, and submit the stablecoin transaction. Rvess will verify the asset policy, amount, sender, transaction label, and mainnet confirmation before initiating the corresponding mobile-money payout. Rvess already has a deployed public beta at [rvess.xyz](http://rvess.xyz) demonstrating wallet connectivity, quoting, transaction tracking, and the intended payout journey. This proposal funds the new stablecoin integration, production controls, mainnet deployment, and initial Uganda pilot. It does not seek retroactive funding for the existing beta.

### Supporting links (repo, site, demo)

- https://rvess.xyz

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1150

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

400

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration has been defined technically but has not yet been implemented. Rvess will extend its existing Cardano transaction architecture to accept verified native stablecoins such as USDM or USDCx. The design covers policy-ID allowlisting, wallet asset discovery, stablecoin quoting, deposit verification, accounting, Dune attribution, and mobile-money settlement. Existing wallet, rate, transaction-state, payout, and operations components provide the foundation, but stablecoin-specific code and mainnet transactions remain new work funded by this proposal.
