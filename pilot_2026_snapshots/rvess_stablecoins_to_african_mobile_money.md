# Rvess: Stablecoins to African Mobile Money

> A new Cardano mainnet integration converting verified stablecoins into local mobile-money payouts, starting in Uganda and expanding across Africa.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 10
- **Proposer:** `stake1uyqe7s205xndy8l4c32pakhldsmp0wrpj75lzhpfmw79ntck5hhzr`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-15T05:55:03.108000+00:00

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

Rvess targets 1,150 genuine stablecoin settlement transactions generating 400 ADA in Cardano network fees, from 400 external users completing roughly 3 transactions each during the adoption period.

Users include Ugandan freelancers, remote workers, Cardano contributors, merchants, and families receiving cross-border payments, plus the Bidi Bidi refugee settlement community. They transact to convert verified Cardano stablecoins into UGX through MTN MoMo or Airtel Money via our Relworx and MarzPay integrations. Usage is expected to repeat as users receive earnings, remittances, and payments.

Week 1 focuses on Bidi Bidi field visits and community onboarding. Week 2 expands to Kampala Cardano/freelancer communities and wallet/dApp outreach. Only transactions from independent external users count; Rvess will not use team-controlled wallets, circular transfers, or subsidized self-transactions. Dune Analytics verifies fees, distinct wallets, and retained usage.

### How will you reach and onboard real users - and what evidence backs your channels?

Rvess is operated by Buildfi Tech UG Ltd (URSB ERN 80034893783008, registered 29 Jun 2026, status: Compliant). We hold a payment integration license with Relworx ([relworx.com](http://relworx.com)), covering MTN MoMo and Airtel Money disbursement, plus a wallet/settlement integration with MarzPay ([wallet.wearemarz.com](http://wallet.wearemarz.com)).

Channels: (1) Bidi Bidi refugee settlement, one of Uganda's largest refugee settlements - early-stage community contact established; reachable population to be confirmed via week-one field visits. (2) Kampala Cardano and freelancer communities, reached through demonstrations, meetups, and referrals. (3) In-person field events at both locations in weeks one and two, run by the founding team.

Target: 400 external users, 1,150 transactions, 400 ADA in counted fees. Week 1: Bidi Bidi outreach. Week 2: Kampala expansion and wallet/dApp partner outreach. Dune Analytics tracks genuine external wallets; no circular or scripted usage.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include centralized exchanges, Binance P2P, Yellow Card, Kotani Pay, OTC brokers, and manual mobile-money exchanges.

Rvess provides a Cardano-native workflow with verified stablecoin checks, transparent quotes and fees, mobile-money payouts, on-chain attribution, and transaction tracking. Wallets and dApps will also be able to embed this settlement route.

### Please provide details about the Technology Readiness Level selected for your existing product

Rvess Pay is live at <https://rvess.xyz> as a working Cardano payment product for African markets. The deployed system includes Cardano wallet connectivity, live exchange-rate quoting, country and mobile-money provider selection, transaction creation, deposit monitoring, payout routing, status tracking, receipts, and an operations dashboard. The architecture supports Uganda, Kenya, and Tanzania, with integrations for MTN MoMo, Airtel Money, and M-Pesa. The product has been demonstrated in its intended web environment. The proposed stablecoin settlement capability is new work and is assessed separately below.

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

Our initial users are Ugandan freelancers, remote workers, Cardano contributors, merchants, and families receiving cross-border payments through mobile money. Rvess will first convert verified Cardano stablecoins into UGX payouts through MTN MoMo and Airtel Money, then expand to Kenya and Tanzania.

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

Funding enables the new stablecoin settlement integration rather than work already completed. Requested amount: 75,000 ADA. 

- Stablecoin integration dev (policy allowlisting, wallet asset support, quoting): 27,000 ADA (36%)
- Deposit monitoring,labeling: 12,000 ADA (16%)
- Mobile-money settlement integration (Relworx/MarzPay): 10,500 ADA (14%)
- Security testing & audit: 7,500 ADA (10%)
- Compliance & Uganda onboarding: 6,000 ADA (8%)
- Infrastructure & monitoring: 5,250 ADA (7%)
- Initial liquidity operations: 6,750 ADA (9%)

Without this funding, we would remain focused on current Cardano payment experience and the route would develop more slowly. The grant accelerates delivery of a verified mainnet integration within three months and its transition into sustained use.

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

TRL 5 - Technology validated in relevant environment

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
