# MarketMarkets: Cardano Marketplace for Real-World Utility

> Turn ADA into everyday utility: discover, buy and verify experiences, memberships and digital goods on Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 16
- **Proposer:** `stake1uy9y2zuz4pyysct0d3k63mxya959wa3cmuqkknph6re6qsqymcgqw`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-23T13:13:09.260000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Kush Innovation Labs is delivering MarketMarkets through a four-person engineering team led by Shashwat S — Project Lead / Lead Engineer.

LinkedIn: <https://www.linkedin.com/in/shashwat-s-54235b39a/>

Team roles: Backend Developer, Frontend Developer, Cardano/CIP-113 & Smart Contract Developer, Testing & Infrastructure Developer.

Shashwat leads architecture, technical decisions, Cardano integration and delivery coordination.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

MarketMarkets will onboard 5 participating merchants with a combined target of 20 active programmable offers. We will target 50 distinct external Cardano wallets during the adoption period through Cardano community outreach, merchant/creator outreach and direct promotion.

The 250 qualifying CIP-113 transactions target is based on an average of 5 qualifying transactions per external wallet (50 × 5 = 250) across purchases, transfers and redemptions. Transactions will be counted from on-chain transaction identifiers and linked external wallets, excluding internal or sponsored activity.

Merchant and consumer onboarding will be tracked through participating merchants, active programmable offers, external wallets and qualifying CIP-113 transaction IDs.

### How will you reach and onboard real users - and what evidence backs your channels?

We will acquire users through Cardano community channels, ecosystem social media, direct outreach, merchant communities, creator communities and participating merchants.

The first two weeks after launch will focus on onboarding initial merchants, publishing real listings, sharing the marketplace with Cardano communities and directly recruiting external users to make genuine purchases.

We will not use ADA giveaways, transact-to-earn schemes or sponsored wallets to manufacture adoption. The target activity will come from independent external users purchasing real marketplace offerings with their own wallets.

Merchant onboarding will focus on simple listing creation, clear pricing, wallet-based checkout and transparent transaction confirmation.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Users currently buy goods and services through individual crypto-accepting merchants, NFT marketplaces, crypto payment providers and conventional e-commerce platforms. These options are fragmented and do not provide a Cardano-focused marketplace combining discovery, ADA payments and programmable utility.

MarketMarkets focuses on practical ADA spending rather than speculative trading. It provides one discovery layer for real products, services and digital goods, with Cardano used for transparent settlement.

The initial advantage is Cardano-native discovery, simple ADA checkout and verifiable on-chain settlement, followed by merchant and consumer network effects.

### Please provide details about the Technology Readiness Level selected for your existing product

MarketMarkets is a publicly deployed marketplace prototype validated through a live Cardano public testnet environment. The product provides marketplace discovery, seller listings, Cardano wallet connection and transaction submission, with successful testnet transactions producing verifiable transaction identifiers. This demonstrates that the core marketplace and Cardano payment flow operates in a relevant blockchain environment. The proposed grant will extend this validated product with CIP-0113 programmable-token functionality, production hardening, expanded testing, merchant onboarding and mainnet deployment.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

MarketMarkets uses a non-custodial Cardano architecture. Users connect their Cardano wallet through CIP-30 and sign transactions themselves; private keys are never held by the platform. The marketplace frontend handles discovery, listings, checkout and transaction status, while the backend manages merchants, products, orders and transaction records.

Cardano provides the settlement and verification layer. ADA payments are recorded on-chain and linked to marketplace orders through transaction identifiers. The proposed CIP-0113 integration adds programmable marketplace utilities such as memberships, vouchers, access rights and redeemable digital benefits.

CIP-0113 is a suitable fit because these utilities require programmable token behaviour rather than simple transfers. Token policies will control issuance and lifecycle rules, while the marketplace associates each asset with its corresponding product or service. On-chain state is used where verifiability and ownership matter, while normal marketplace data remains off-chain for efficiency.

This architecture combines Cardano-native settlement, user-controlled wallets, programmable utility and independently verifiable transactions while keeping the consumer experience simple.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

The initial target market is Cardano wallet users who already hold ADA and are interested in using it for purchases rather than only holding or trading it. A second target group is merchants, creators and service providers looking for a simple way to accept ADA from Cardano users.

MarketMarkets addresses an existing Cardano ecosystem gap: consumer spending utility. Cardano already has wallets, exchanges, DeFi, NFTs and developer infrastructure, but consumer marketplaces that focus on practical ADA spending remain limited.

Our initial adoption strategy will focus on Cardano communities, ecosystem social channels, direct merchant outreach, developer and creator communities, and recruiting merchants willing to list real products or services.

Demand will be validated through actual external users making marketplace purchases with their own wallets. We will measure unique external wallets, completed marketplace transactions, transaction volume and repeat usage.

### Applicant name

Kush Innovation Labs

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

MarketMarkets will use a marketplace transaction fee on completed purchases, with optional merchant services and premium marketplace functionality as the platform grows.

Consumers will not be charged simply for browsing or creating a wallet connection. Revenue will primarily come from successful marketplace transactions, aligning platform revenue with genuine economic activity.

After the grant, transaction fees, merchant services and additional marketplace functionality will fund infrastructure, maintenance, security, customer support and continued development. The grant funds the initial Cardano integration and adoption pilot rather than permanent operating costs.

### Programmable tokens (CIP-0113) - expected transaction count

250

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding will take the existing validated MarketMarkets marketplace from Cardano testnet validation to a production-ready marketplace with CIP-0113 programmable utility, mainnet deployment and genuine external-user adoption.

Funding will be used for CIP-0113 implementation and integration, Cardano transaction infrastructure, security and automated testing, production engineering, merchant onboarding, infrastructure, user acquisition and adoption measurement.

The existing marketplace and testnet payment work provide the foundation; the grant specifically enables the new programmable-token functionality, production hardening and external adoption activities required to establish sustainable real-world ADA usage.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

 1. Production-ready MarketMarkets marketplace deployed on Cardano mainnet.
 2. CIP-30 Cardano wallet connection and non-custodial checkout.
 3. CIP-0113 programmable-token functionality integrated into marketplace products and user flows.
 4. End-to-end purchase and programmable-utility flows producing verifiable mainnet transactions.
 5. Merchant listing, product purchase and programmable utility redemption flows.
 6. On-chain transaction verification and declared footprint documentation.
 7. Security, integration and end-to-end test evidence.
 8. Public open-source repository with release notes and tagged implementation.
 9. Live production URL and technical walkthrough demonstrating the complete integration.
10. Mainnet-ready monitoring and documentation for the subsequent adoption measurement phase.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Programmable tokens (CIP-0113) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

MarketMarkets is a Cardano-based marketplace designed to turn ADA into practical everyday utility. It allows real users to discover products, services and digital goods, view transparent listings, connect a Cardano wallet and complete purchases using ADA.

The problem is that Cardano users can hold ADA but have limited simple, consumer-facing ways to spend it on useful goods and services. Existing blockchain marketplaces are often focused on NFTs, trading or developer-oriented activity rather than recurring real-world consumer transactions.

MarketMarkets provides a simple marketplace experience where merchants can publish offers and consumers can discover and purchase them using Cardano. The platform will also support programmable utility assets using CIP-0113 where appropriate, enabling merchants to represent memberships, vouchers, access rights or other programmable marketplace utilities.

The primary users are Cardano consumers who want to spend ADA and merchants who want to reach Cardano users with useful products and services.

### Supporting links (repo, site, demo)

- https://marketmarkets.shop
- https://kushinnovationlabs.com/
- https://www.linkedin.com/in/shashwat-s-54235b39a/
- https://preprod.cardanoscan.io/transaction/444b27a7714352980790309301fc35d167a622c56889cdce0dca6627db0d5667
- https://preprod.cardanoscan.io/transaction/0e794d480af6fb7b3368274e47e3eec9aaddb058cae2167deeae1ed3596e912e

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

MarketMarkets will be developed as an open-source project. The source code, technical documentation and integration components will be published under a permissive open-source license. Kush Innovation Labs retains ownership of its brand, trademarks and other proprietary assets while making the funded software implementation openly available according to the published license.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed CIP-0113 integration has been implemented and validated in a controlled environment. The implementation establishes the programmable-token architecture, token policy, marketplace integration and transaction flows required for programmable memberships, vouchers, access rights and redeemable digital benefits. The existing MarketMarkets application and Cardano wallet transaction flow have also been validated on public testnet. The funded work will validate the CIP-0113 implementation on public testnet, strengthen security and testing, integrate it fully into the marketplace, and prepare it for production mainnet deployment.
