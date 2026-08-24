# Pay by Cexplorer: Stablecoin Checkout for Any Business

> Create one link or QR code, set the price in USD and receive USDM or USDCx directly to your wallet without custody, middlemen or coding.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 34
- **Proposer:** `stake1u8s9hfdektcafcqzgj7pcz2hh57wmpjgrfqsmruj7yf5m3gujfpue`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-24T08:13:52.250000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Pay by Cexplorer will be delivered by the established three-person Cexplorer core team:

- **Josef Taborsky: Backend, Data and Architecture:** responsible for transaction building, blockchain indexing, infrastructure, DevOps, QA and security.\
  <https://github.com/josef0xb>
- **Filip Balas: Product, UI/UX and Frontend:** responsible for the merchant dashboard, checkout flow, wallet integration and mobile experience.\
  <https://github.com/FilipBala>
- **Michal Urbanek: Project Management and Business Development:** responsible for delivery coordination, partnerships, merchant onboarding, reporting and administration.\
  <https://www.linkedin.com/in/michal-urbanek-734a3387/>

The team has operated Cexplorer for several years, completed previous Catalyst-funded projects and already launched Pay by Cexplorer on mainnet.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

We declare a target of 1,500 genuine stablecoin payments and 300 ADA in counted network fees, based on an estimated average fee of 0.20 ADA per transaction. Users will pay Cardano projects, creators, freelancers and community initiatives through USDM and USDCx payment links, QR codes and embedded checkout. We target at least 300 distinct external payer wallets; team wallets and sponsored transactions are excluded.

The minimum-window plan is:

• Entry epoch: 50 transactions / 10 ADA; launch ramp, no floor.\
• Epoch 1: 150 / 30 ADA.\
• Epoch 2: 175 / 35 ADA.\
• Epoch 3: 200 / 40 ADA.\
• Epoch 4: 275 / 55 ADA.\
• Epoch 5: 300 / 60 ADA.\
• Epoch 6: 350 / 70 ADA.

Total: 1,500 transactions and 300 ADA. The plan exceeds the required epoch floors of 25 ADA in epochs 1–3 and 50 ADA in epochs 4–6. Campaigns will run throughout the window rather than as one launch spike. No single day is planned to contribute more than 20% of the total. We will report transactions, fees, unique wallets, active recipients and repeat usage per epoch.

### How will you reach and onboard real users - and what evidence backs your channels?

CPay is live but not actively promoted and recorded 89 mainnet transactions between April and July 2026. At launch, distribution will combine [Cexplorer.io](http://Cexplorer.io) header and in-product placement (\~15,000 monthly unique users), Cexplorer’s X, TG and DC channels, and Cardanians’ X account (71,000 followers) and newsletter. Cardanians is the only distribution partner; all counted transactions must come from external wallets and none will be team-funded.

The 1,500-payment target is allocated as 500 from Cexplorer placement, 250 from Cexplorer social channels, 725 from Cardanians distribution and 25 from organic usage. Tagged links, source-specific QR codes and unique-wallet tracking will limit channel overlap.

Days 1–3: launch placements and onboarding content. Days 4–7: publish payment use cases and support recipients. Days 8–10: repeat Cardanians and Cexplorer campaigns. Days 11–14: address friction and retarget users who created links but have not received a payment.

### Is the underlying project open source?

No

### Short Video Pitch

https://vimeo.com/1218837107 

### Who else solves this today - competitors/alternatives, and why does your approach win?

Cardano payment alternatives include NMKR’s ADA payment links, the open-source Adalicious starter kit, Begin Wallet deep links, PayADA payment links and embeds, and the CardanoCoffee payment-button example.

These products validate the use case, but most focus on ADA transfers, wallet deep links or developer-managed deployments. Adalicious includes expiring ADA links and basic webhook notifications, but requires merchants to deploy and operate their own instance.

Pay by Cexplorer will provide a hosted, non-custodial stablecoin checkout with verified assets, invoice lifecycle management, exact-payment validation, reconciliation, embeddable checkout and signed merchant webhooks. It combines payment creation, TX construction and on-chain verification within one maintained service.

### Please provide details about the Technology Readiness Level selected for your existing product

Pay by Cexplorer is live on Cardano mainnet and has processed real ADA payments. Users can create payment links, connect a wallet, complete payments and verify transactions on-chain. The product operates on Cexplorer’s production infrastructure, but has not yet reached the sustained volume required for TRL 9.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

USDM and USDCx are Cardano native assets, allowing direct non-custodial settlement without a custom smart contract. The transaction builder creates an exact stablecoin output to the recipient together with the required minimum ADA, Catalyst tag and unique payment reference.

Cexplorer’s backend maintains the invoice state, while its indexer independently verifies the policy ID, asset amount, recipient, reference and confirmation. Incorrect, underpaid or overpaid transactions are detected and assigned the appropriate payment status. Confirmed payments trigger signed merchant webhooks.

This architecture builds on Cardano’s native multi-asset model and Cexplorer’s existing indexing infrastructure while keeping funds under the control of the payer and recipient.

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

Our initial market is Cardano projects, creators, freelancers, event organizers and online merchants that need stable pricing and direct wallet settlement.

The existing ADA version recorded 89 on-chain transactions between April and July 2026. This proves that the product works on mainnet, but it does not yet represent product-market fit. Cexplorer’s monthly active users provide a relevant and directly reachable audience of active Cardano users, projects and developers.

USDM and USDCx provide the required stable settlement assets. The pilot will validate commercial demand through real merchant integrations, external wallets and repeat stablecoin payments.

### Applicant name

Michal Urbanek

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Basic payment links will remain accessible without a mandatory per-transaction service fee, keeping small payments economically viable.

Revenue will come from paid merchant features such as higher usage limits, signed webhooks, embeddable checkout, payment history and exports, custom branding and integration support. Pricing and tier limits will be validated with pilot merchants. Optional donations to the Cexplorer team will remain available.

The product uses Cexplorer’s existing infrastructure, indexer and core team, keeping incremental operating costs low. Merchant subscriptions and integrations can therefore sustain the service after grant funding ends.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The grant funds a new stablecoin invoicing and merchant-integration layer—not maintenance of the existing ADA payment flow. Without it, the team would continue prioritizing Cexplorer’s core infrastructure, leaving CPay as an early ADA-only product.

The 50,000 ADA budget covers the invoice engine, stablecoin transaction builder and indexer integration (18,000); merchant checkout, dashboard and embed (10,000); signed webhooks and integration tooling (7,000); QA, security and mainnet monitoring (6,000); merchant onboarding and adoption (5,000); and documentation, reporting and project management (4,000).

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Month 1 – Core integration\
• Add verified USDM and USDCx policies to the transaction builder.\
• Implement invoices, expiry, single-use links, exact-amount validation and under/overpayment protection.\
• Complete automated and preprod tests.

Month 2 – Merchant integration\
• Add indexer confirmation, reconciliation and payment history.\
• Deliver embeddable checkout, signed webhooks and merchant configuration.\
• Begin end-to-end testing, monitoring and security review.

Month 3 – Mainnet delivery\
• Resolve QA and security findings and deploy the production release.\
• Publish documentation, release notes and the declared on-chain footprint.\
• Complete independent mainnet payments with USDM and USDCx.\
• Provide the live URL, transaction hashes, test evidence, walkthrough video and Demo Day presentation.

M1 is complete only when the stablecoin flow is live, repeatable and independently verifiable on Cardano mainnet.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Merchants, creators, freelancers and event organizers need a simple way to accept Cardano payments without exposing customers to wallet addresses, manual reconciliation or volatile ADA pricing. Stablecoins solve price volatility, but Cardano still lacks an accessible, hosted invoicing tool with reliable payment verification and merchant integrations.

Pay by Cexplorer is an existing non-custodial payment-link product operating on Cardano mainnet. The proposed project will extend it into a stablecoin invoicing and checkout platform supporting verified USDM and USDCx assets.

Recipients will create fixed or flexible payment requests denominated in USD and share them as links, QR codes or embedded payment buttons. New invoice functionality will include expiration, single-use payment requests, exact-amount validation, and detection of underpaid or overpaid transactions.

A merchant integration layer will add signed webhooks, persistent payment statuses and transaction reconciliation. This allows businesses to connect confirmed payments to orders, tickets, subscriptions or services.

Funds always move directly from the payer to the recipient’s wallet. Cexplorer provides the checkout, transaction construction, on-chain verification and integration infrastructure without taking custody of customer assets.

### Supporting links (repo, site, demo)

- https://pay.cexplorer.io/

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

1500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

300

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration is currently at the design stage. The user flow, verified USDM and USDCx policies, transaction structure and direct-settlement model are defined, but stablecoin-specific code has not yet been implemented. The existing ADA payment product provides the technical foundation.
