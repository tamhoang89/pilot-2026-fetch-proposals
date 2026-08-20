# Institutional Grade KYC/AML Rules for RWA CIP-0113 Tokens

> On-chain identity CIP-0113 tokens that comply with U.S. and global KYC / AML standards that can be legally accepted by institutions

## Proposal Metadata

- **Status:** finalized
- **Revision:** 13
- **Proposer:** `stake1u9nzx5rkh2k0y07gnn09pagy5uwtfzpum034ytczahtzk9cgk86fr`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T02:57:35.565000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Our team operates one of the only blockchain-enabled U.S. broker-dealers and carries all the regulatory required licenses to verify and transfer KYC credentials on-chain.

This can be verified at:

<https://files.brokercheck.finra.org/firm/firm_45500.pdf>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

As the first U.S. compliant RWA compliance infrastructure on Cardano, it can help ease the requirements for other RWA issuers. For the transaction fees generated, up to 10% can be shared back the Cardano Treasury or help support other Cardano projects.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Integration fees for issuers and per KYC request fees to qualified issuers and institutions. This will dramatically reduce the costs for firms that need access to KYC.

Institutional KYC Sharing via Section 314(b)

○ The Safe Harbor: SOMA utilizes Section 314(b) of the USA PATRIOT Act to legally share the underlying rich KYC data with other 314(b)-registered institutions (e.g., Broker, Bank or Institution).

○ The Flow: When a second institution needs the full PII for its own records, it sees the SOMA "Verified" tag on-chain. It then requests the data from SOMA off-chain via the 314(b) secure sharing protocol.

○ Benefit: This eliminates redundant KYC checks across the Cardano ecosystem, drastically reducing onboarding friction for users.

### How will you reach and onboard real users - and what evidence backs your channels?

To date, directly and through affiliates, SOMA has successfully done KYC on several hundred thousand retail investors, accredited investors and institutions globally through its existing systems. 

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

While there are on-chain identity providers, there are none being done at a regulatory standard that institutions can actually accept and use.

### Please provide details about the Technology Readiness Level selected for your existing product

KYC / AML system is built and operational, just needs to be integrated with the CIP-0113 programmable token. 

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Three parts: 

1. build an on-chain credential smart contract for on-chain verification 
2. issuance token to wallets for wallet verification
3. Section 314(b) of the USA PATRIOT Act to legally share the underlying rich KYC data with other 314(b)-registered institutions (e.g., Broker, Bank or Institution).

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

RWAs are one of the fastest-growing categories, but lack of an acceptable integrated regulatory standard forces issuers to assume the cost and burdens of doing AML / KYC themselves. This leads to a high fragmentation. 

### Applicant name

SOMA.finance

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Each KYC costs over $50,000 to build or license for one-off implementations and millions for institutional-grade systems. Each individual KYC costs $2-5 each currently.

Once done properly, costs can drop over 99%. Each individual KYC can then be requested on-chain and accepted for a nominal fee, including secure credentials transfer.

### Programmable tokens (CIP-0113) - expected transaction count

500000

### On-chain identity (CIP-0170) - expected transaction count

500000

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Cardano integration with existing onboarding workflow, integration of Cardano-specific on-chain AML analytics, secure KYC rich data request and transfer

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Integrate Cardano wallets and protocols into the existing onboarding system.
2. Migrate the central KYC wallet repository to Cardano.
3. Issuance of KYC verification token to individual users' wallets. 

### How far along is the integration you're proposing, today?

TRL 9 - Actual system proven in operational environment

### Programmable tokens (CIP-0113) - fee target (ADA)

300

### On-chain identity (CIP-0170) - fee target (ADA)

200

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

To leverage SOMA Finance’s unique status as a FINRA-regulated Broker-Dealer and Transfer Agent, the following plan outlines how to operationalize on-chain AML / KYC credentials on Cardano using the latest CIP-0113 standards.

This approach creates a "Compliance-as-a-Service" layer where SOMA performs the heavy lifting of identity verification, and other institutions (brokers, banks, Cardano DeFi protocols, or institutions) can trust and consume those credentials on-chain under existing regulatory frameworks.

### Supporting links (repo, site, demo)

- https://www.soma.finance/

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

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Anyone can onbord currently and use the operational KYC / AML system:

<https://onboard.soma.finance/home>
