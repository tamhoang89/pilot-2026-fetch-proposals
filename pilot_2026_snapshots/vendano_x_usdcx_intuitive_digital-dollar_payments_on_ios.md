# Vendano x USDCx: Intuitive Digital-Dollar Payments on iOS

> Turn an iPhone into a simple Cardano checkout: merchants request payment in ADA or USDCx, customers pay directly on-chain, and Vendano makes the stablecoin experience easily understandable.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 9
- **Proposer:** `stake1uxlrwkwcyese8dh5nxar7mwr4yy90gdfmaat7ysdshxtqwcvp4qhk`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-17T15:22:02.795000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

I designed Vendano, developed its product direction, and have led it from concept through a production iOS release on Cardano mainnet. My responsibilities for this project include product design, merchant UX, iOS development, Cardano transaction integration, testing, App Store delivery, documentation, and pilot reporting.

Vendano already provides the core infrastructure this project depends on: self-custody wallet creation/import, Cardano mainnet transactions, address and UTxO handling, native-asset discovery, transaction history, and production App Store distribution.

I have also previously self-funded outside engineering assistance to bring Vendano to production. The Catalyst milestone does not depend on an uncommitted external partner. If specialized engineering review or QA support is engaged during delivery, its scope will be supplementary rather than a dependency on reaching mainnet.

<http://linkedin.com/in/jeffreality>

<https://github.com/jeffreality/>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Counted usage comes only from external users making genuine USDCx payments on Cardano; my own/test wallets and subsidized or reimbursed transactions will not be counted.

The 1,300-payment figure is the declared program target, not a claim of existing volume. The first two weeks target 3–5 merchants, 20–30 customers, and at least 50 payments while the flow is stabilized. The broader measured-window target assumes the initial 5 converted Rare Evo exhibitors grow to 8–10 active merchants, supported by roughly 100–150 external customer wallets averaging repeat purchases across the participating merchants.

Before release I will personally contact the businesses in Rare Evo’s published exhibitor directory, prioritizing likely merchandise sellers using the expo map, and seek at least 3 onboarding commitments before launch. No merchant is claimed as committed today. This is an ambitious acquisition target built from a concrete prospect pool, not existing USDCx demand. Hands-on support and rapid fixes during the first two weeks will determine whether the cadence can scale.

### How will you reach and onboard real users - and what evidence backs your channels?

Vendano has established public channels I have used before: the App Store, X, YouTube, Medium/Coinmonks, r/Cardano, and the Cardano Forum. Current organic App Store acquisition is small but measurable: 11 App Store units in the last 30 days.

The primary merchant channel is Rare Evo’s published 2026 exhibitor directory and expo map. I will personally contact the listed exhibitors, prioritizing those most likely to sell merchandise at Cardano events, and present Vendano as an iPhone checkout option. The target is to convert at least 5 exhibitors into pilot merchants; no exhibitor is represented as already committed.

In the first two weeks after release, I will target 3–5 merchants onboarded, 20–30 external customers, and at least 50 genuine USDCx payments. I will publish walkthroughs through the named channels, provide hands-on support, and prioritize fixes found in real transactions.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Merchants can already use conventional processors such as Stripe or Square for fiat payments. Cardano users can already transfer ADA and native assets through general-purpose wallets, and USDCx users can use separate bridge and wallet interfaces.

Vendano sits between those experiences.

It does not attempt to replace a full merchant processor or compete on the number of advanced wallet features. The product is intentionally focused on a simple Cardano checkout.

The differentiator is a payment-first iOS experience combined with self-custody. Funds move directly between customer and merchant wallets on Cardano rather than through a Vendano-controlled account.

### Please provide details about the Technology Readiness Level selected for your existing product

Vendano is a packaged, live, self-custody Cardano wallet distributed publicly through Apple’s App Store and has operated on Cardano mainnet for approximately eight months. It is beyond prototype or testnet validation. 

The production application supports wallet creation/import, ADA transactions, native-asset discovery, transaction history, address-based and simplified payment flows, and an existing Store Mode.

Customers install the production app directly from the App Store; they do not clone the repository, use Xcode, or supply API keys. The repository instructions are solely for developers compiling the open-source code. The public App Store release and live mainnet operation provide independently verifiable evidence of TRL 7.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Vendano is a self-custody iOS wallet. Private keys remain with the user, transactions are constructed and signed on-device, and merchant payments settle directly on Cardano rather than through a Vendano custodial account.

The existing application uses Cardano's UTxO model and already discovers native assets held by the wallet. The funded work extends transaction construction from ADA-only outputs to Cardano multi-asset outputs containing USDCx, while preserving the ADA required for network fees and minimum output values.

USDCx will be identified by its verified Cardano native-asset policy rather than by a Vendano-issued representation.

The merchant flow creates a payment request. The customer authorizes the transaction. USDCx moves directly from the customer's wallet to the merchant's wallet.

The core payment path does not require Vendano to operate a bridge, exchange, custodial account, proprietary stablecoin, smart contract, or off-chain settlement network.

Catalyst-required transaction identification will be added to the funded USDCx payment flow so eligible transactions can be associated with the declared integration footprint.

This architecture keeps the deliverable small enough to ship while solving the part Vendano controls directly: making a stablecoin balance and payment behave like understandable digital cash on an iPhone.

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

The initial market is deliberately narrow: small merchants, independent vendors, event sellers, and Cardano community businesses already willing to accept blockchain payments but lacking a simple point-of-sale experience.

Vendano is already live in the iOS App Store and has operated on Cardano mainnet for approximately eight months. The underlying wallet, transaction, onboarding, and App Store release infrastructure already exists and has been used in production.

Previous go-to-market work focused on broad consumer awareness. That produced a functioning public product but did not establish a strong recurring reason for users to transact.

This proposal changes the usage model rather than assuming that more general wallet promotion will produce a different result. A merchant is a recurring transaction endpoint: one merchant can receive payments from many independent customer wallets, and the reason to use the product is concrete: either paying or getting paid.

The pilot will test whether this narrower merchant utility produces repeat transaction behavior.

### Applicant name

Jeffrey Berthiaume

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Vendano is intended to be sustainable through transaction-based revenue rather than subscriptions or custody of customer funds. Existing qualifying ADA transactions already support an application-level fee model.

The pilot's goal is not to maximize application fees. It is to establish whether a merchant-oriented payment experience creates repeat usage.

Customers pay normal Cardano network fees for transactions they initiate. Catalyst funds will not be used to subsidize, reimburse, or reward transactions counted toward adoption.

If merchants find the workflow useful, usage can continue for the same reason conventional checkout tools continue to be used: accepting payment is part of normal business activity rather than a one-time promotional action.

The USDCx implementation, merchant workflow, and supporting help content will remain part of the production Vendano application after the pilot.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Vendano has already been substantially self-funded; this request funds new USDCx work, not reimbursement.

The primary deliverable is a production Vendano release in Apple's App Store with working USDCx balances, transfers, and merchant checkout. Approximate 125,000 ADA allocation:

35,000 - USDCx/multi-asset engineering: balances, transactions, coin selection, minimum-ADA and history.\
25,000 - merchant/customer checkout UX.\
15,000 - funding/cash-out research, onboarding, fees/minimums, help and FAQ.\
20,000 - QA and production App Store release.\
10,000 - Catalyst tagging, evidence and technical documentation.\
20,000 - merchant recruitment, launch support and adoption.

The UI/UX work is essential: USDCx must feel like understandable digital cash, not merely another token.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, Vendano will deliver:

1. A production iOS release in Apple's App Store containing the funded USDCx integration.
2. Verified USDCx balance recognition/display and self-custody send/receive support.
3. Merchant checkout allowing a merchant to request payment in ADA or USDCx.
4. A guided customer flow to review, authorize and confirm that payment.
5. Multi-asset transaction handling including coin selection, minimum-ADA, change, signing, submission and history.
6. In-app USDCx onboarding/help covering supported funding/cash-out routes, network selection, minimum/fee warnings, processing status and verification.
7. Catalyst-required transaction identification/tagging and reproducible mainnet evidence.
8. Repeatable real-user USDCx payment transactions on Cardano mainnet.
9. Release notes, QA/test evidence and technical walkthrough for Demo Day.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Vendano is an existing self-custody Cardano wallet for iOS built to make everyday transactions easier for people who do not want to think in terms of wallet addresses, UTxOs, policy IDs, or other blockchain terminology.

This project shifts Vendano toward a merchant-first experience and adds native USDCx payments. Think of it as a lightweight Cardano checkout: a merchant enters an amount, chooses ADA or USDCx, and presents a payment request. A customer reviews the amount and completes the payment through a guided flow.

The technical ability to transfer USDCx is only part of the problem. For an ordinary user, a stablecoin needs to feel like digital cash. They need to understand what they have, what they are paying, whether a transaction succeeded, and how to move stable value into or out of their wallet without becoming an expert in exchanges, networks, bridges, or native assets.

Hands-on testing of the current CEX-to-Cardano USDCx flow reinforced that problem. The working route required connecting a supported Cardano wallet, generating a Base deposit address, selecting the correct exchange network, meeting a 21 USDC automatic-forwarding minimum that was only surfaced after the first deposit, waiting through asynchronous processing, and separately confirming the Cardano-side result.

These steps are technically manageable. The product opportunity is making them understandable enough that ordinary customers do not have to understand the machinery underneath.

### Supporting links (repo, site, demo)

- https://apps.apple.com/us/app/vendano-cardano-wallet/id6751762014
- https://vendano.net/
- https://github.com/vendano/vendano-ios
- https://www.youtube.com/watch?v=XtmH3UH9N2g

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

Vendano is open source under the BSD 3-Clause license: <https://github.com/vendano/vendano-ios?tab=BSD-3-Clause-1-ov-file>

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1300

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

475

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The funded USDCx integration has not been implemented, and no retroactive work is being requested.

Technical feasibility has been evaluated against Vendano's existing architecture. Vendano already reads Cardano native assets from UTxOs, and its underlying Cardano transaction library supports multi-asset values and multi-asset coin selection.

Vendano itself has not yet generated or submitted a USDCx payment transaction.

The remaining work includes USDCx-specific balance and decimal handling, multi-asset transaction construction, fee/minimum-ADA handling, merchant and customer UX, funding/cash-out guidance, transaction status and error states, Catalyst transaction tagging, testing, documentation, and production release.
