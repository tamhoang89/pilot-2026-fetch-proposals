# Vendano x USDCx: Intuitive Digital-Dollar Payments on iOS

> Turn an iPhone into a simple Cardano checkout: merchants request payment in ADA or USDCx, customers pay directly on-chain, and Vendano makes the stablecoin experience easily understandable.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1uxlrwkwcyese8dh5nxar7mwr4yy90gdfmaat7ysdshxtqwcvp4qhk`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-18T14:48:44.050000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

I am the sole delivery owner. I work as a Senior Software Engineer in enterprise technology innovation; my employer is not a participant and no employer resources are claimed. I designed Vendano and led it through Cardano mainnet operation, Store Mode, Apple review and App Store release.

The existing product is the strongest capability evidence. Apple's listing distributes a signed production iPhone/iPad app with wallet creation/import, local self-custody keys, ADA transfers, contact payments, history and Store Mode. Customers install that binary directly.

The GitHub repository is source for developers and reviewers. It intentionally excludes production Firebase configuration, Blockfrost credentials, signing material and Apple entitlements. Developers compiling a fork supply their own configuration; App Store users do not.

This proposal requires no custom Cardano smart contract. USDCx is an existing native asset. The funded Swift/iOS work constructs, signs, submits and displays standard multi-asset transfers. Vendano already provides keys, addresses, UTxO/native-asset discovery, ADA transaction construction/signing/submission, history, Store Mode and App Store deployment. Remaining work is USDCx values, coin selection, minimum ADA/change, checkout UX, testing, localized UI/onboarding/help, App Store metadata/screenshots and release. Much of the scope is user documentation and explanation. No additional developer or uncommitted partner is required.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Target: 800 genuine USDCx payments and 475 ADA in counted fees, the scaled floor for a 125,000-ADA request. The provable acquisition baseline is 11 App Store units in 30 days, with zero USDCx transactions and no committed merchants.

External customers use self-custody wallets to pay independent merchants for real goods/services, supplying their own ADA, USDCx and fees.

Acquisition: publish localized App Store metadata/screenshots in Spanish, French, German, Korean, Japanese, Simplified Chinese and Traditional Chinese; contact at least 30 Cardano-community merchants; seek 6 substantive conversations, 3 pilot acceptances, 2 active merchants before Demo Day and 4-6 during adoption. Public content is supplemental, not committed demand.

First 14 days: target 2-3 merchants, 20-30 customer wallets and 50 genuine payments. Full model: 4-6 merchants and 50-75 wallets. Across 35 days, 800 payments average 22.9/day; this is aggressive from zero volume and is the main risk.

Team wallets, tests, circular or metric-only payments, subsidies, rewards, refunds and reimbursed fees are excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

Vendano recorded 11 App Store units in 30 days, the only acquisition volume claimed. If that rate continues, it would add roughly 30 units before M1; I assume only 5-10 become active USDCx users.

I will screen Rare Evo's exhibitor directory and other Cardano businesses and contact at least 30 merchants selling online or at recurring events. Targets: 6 substantive conversations, 3 pilot acceptances, 2 active merchant wallets before Demo Day and 4-6 during adoption. None is committed today.

The App Store, X, YouTube, Medium/Coinmonks, r/Cardano and Cardano Forum will share the release; no conversion is assumed.

Days 1-3: activate M1 merchants, verify requests and publish the walkthrough. 

Days 4-7: target 15-20 customer wallets and 25 genuine payments. 

Days 8-14: target 2-3 merchants, 20-30 wallets and 50 cumulative payments.

Only external purchases for real goods/services count. Team wallets, tests, circular transfers, subsidies, rewards and reimbursed fees are excluded.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Merchants can already use conventional processors such as Stripe or Square for fiat payments. Cardano users can already transfer ADA and native assets through general-purpose wallets, and USDCx users can use separate bridge and wallet interfaces.

Vendano sits between those experiences.

It does not attempt to replace a full merchant processor or compete on the number of advanced wallet features. The product is intentionally focused on a simple Cardano checkout.

The differentiator is a payment-first iOS experience combined with self-custody. Funds move directly between customer and merchant wallets on Cardano rather than through a Vendano-controlled account.

### Please provide details about the Technology Readiness Level selected for your existing product

Vendano is TRL 7 because it is packaged, publicly distributed by Apple and operating on Cardano mainnet. Apple's listing identifies Vendano LLC and distributes the signed iPhone/iPad binary. The app supports wallet creation/import, local self-custody keys, ADA transactions, contact payments, history and Store Mode.

GitHub is source for developers, not customer distribution. Production configuration, secrets and Apple signing material are intentionally excluded. Customers install the App Store binary; they do not clone the repository, open Xcode or provide keys.

USDCx is new work and is separately declared TRL 3.

Evidence:\
<https://apps.apple.com/us/app/vendano-cardano-wallet/id6751762014>\
<https://vendano.net/>\
<https://github.com/vendano/vendano-ios>

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

There is no custom smart contract or on-chain script in this proposal.

USDCx is an existing Cardano native asset. Vendano is a self-custody light wallet: keys remain on the user's device; iOS constructs and signs a standard Cardano multi-asset transaction; a Cardano API provider supplies chain data and accepts the signed transaction for submission. Settlement is directly between customer and merchant addresses.

Vendano already manages Cardano addresses and keys on-device, queries UTxOs/native assets, constructs/signs/submits ADA transactions, monitors confirmation/history and provides Store Mode.

The funded extension adds the verified USDCx policy ID, asset name and decimals; USDCx balances; multi-asset outputs/change; ADA preservation for fees and minimum output values; a dollar-denominated merchant request; guided customer confirmation; the registered Catalyst transaction tag; and production error, confirmation and history states.

No Aiken, Plutus or OpShin code is required because no validator executes and no token is minted. Vendano does not operate the bridge, hold funds or settle off-chain.

The mainnet footprint is the verified USDCx policy, Catalyst tag, disclosed application/team addresses required by the Standard, and independently signed external customer-to-merchant transactions.

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

Within three months Vendano will deliver:

 1. Production App Store release with USDCx.

 2. Verified USDCx policy, decimals, balances and history.

 3. Self-custody standard native-asset USDCx send/receive.

 4. Store Mode checkout for ADA or exact dollar-denominated USDCx.

 5. Customer review of merchant, amount, fee, minimum ADA and confirmation.

 6. Localized UI, onboarding, help and funding/cash-out guidance in Spanish, French, German, Korean, Japanese, Simplified Chinese and Traditional Chinese.

 7. Matching localized App Store metadata/screenshots and Catalyst tagging.

 8. Reproducible policy/address/team-wallet footprint.

 9. At least 2 external merchant wallets active before Demo Day.

10. At least 5 external customers completing 10 genuine mainnet USDCx payments without subsidy or reimbursed fees.

11. Release notes, no-smart-contract architecture, QA evidence, bug log and security note.

12. Live Demo Day walkthrough using the App Store build and measured flow.

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
- https://linkedin.com/in/jeffreality

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

800

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

475

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The funded USDCx integration has not been implemented, and no retroactive work is being requested.

Technical feasibility has been evaluated against Vendano's existing architecture. Vendano already reads Cardano native assets from UTxOs, and its underlying Cardano transaction library supports multi-asset values and multi-asset coin selection.

Vendano itself has not yet generated or submitted a USDCx payment transaction.

The remaining work includes USDCx-specific balance and decimal handling, multi-asset transaction construction, fee/minimum-ADA handling, merchant and customer UX, funding/cash-out guidance, transaction status and error states, Catalyst transaction tagging, testing, documentation, and production release.
