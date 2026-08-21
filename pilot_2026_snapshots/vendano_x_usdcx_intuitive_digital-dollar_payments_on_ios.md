# Vendano x USDCx: Intuitive Digital-Dollar Payments on iOS

> Turn an iPhone into a simple Cardano checkout: merchants request payment in ADA or USDCx, customers pay directly on-chain, and Vendano makes the stablecoin experience easily understandable.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 36
- **Proposer:** `stake1uxlrwkwcyese8dh5nxar7mwr4yy90gdfmaat7ysdshxtqwcvp4qhk`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-21T20:11:21.902000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

I am Jeffrey Berthiaume, the sole delivery owner. My identity and delivery history are publicly verifiable through the links below. LinkedIn identifies my technology work at Southwest Airlines; GitHub shows my public development identity; the prior official Catalyst proposal names me, describes 15+ years shipping production mobile applications, and assigns me responsibility for Vendano's iOS codebase, UX, analytics, documentation and milestone reporting. Apple's listing verifies that Vendano LLC distributes the production iPhone/iPad app.

LinkedIn: <https://www.linkedin.com/in/jeffreality/>\
GitHub: <https://github.com/jeffreality/>\
Prior Catalyst record: <https://projectcatalyst.io/funds/14/cardano-use-cases-concepts/vendano-contactbased-cardano-wallet-ios-android>\
Production app: <https://apps.apple.com/us/app/vendano-cardano-wallet/id6751762014>

I designed Vendano and led it through Cardano mainnet operation, Store Mode, Apple review and App Store release. Vendano already provides self-custody keys, addresses, UTxO/native-asset discovery, ADA transaction construction/signing/submission, history and production deployment.

No custom Cardano smart contract is required. USDCx is an existing native asset. The funded Swift/iOS work will redesign Vendano's UI, changing the primary focus to merchant payments and USDCx values, multi-asset coin selection and change, minimum ADA handling, checkout UX, testing, localized guidance, App Store assets and release.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Target**: 750 genuine USDCx payments and 275 ADA in counted fees for a 75,000-ADA request. The linkage is 275/750 = 0.367 ADA per standard multi-asset payment, within the Standard's 0.33-0.40 range. No unusual transaction design is assumed. The fee target is about 25% above the 220-ADA floor and remains a stretch from zero.

**Baseline**: 11 App Store units in 30 days, zero USDCx payments and no committed merchants. The model requires 8 active merchants and 120-160 distinct customer wallets, above the 22-wallet minimum. That is about 94 per merchant and 4.7-6.3 per customer over 35 days - roughly weekly. At the modeled 0.367 average, all six floored blocks clear their fee floors.

**Before Demo Day**: 4 external merchants, 15 customers and 25 mainnet payments. The 35-day schedule after M1 by 5-day block is 25 entry-ramp payments, then 70, 80, 90, 150, 160 and 175. This totals 750. Daily pace rises from 5 to 35 as merchants grow from 4 to 8 and wallets from 15 to 160, rather than through an unexplained late jump.

Only independent purchases using customer funds count. Tests, team wallets, circular/metric transfers, subsidies, rewards, refunds and reimbursed fees are excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

Vendano recorded 11 App Store units in 30 days. At that rate, about 30 more arrive before M1; I assume 5-10 become active USDCx users.

I will contact 50 recurring-use Cardano merchants via Rare Evo's exhibitor list. Targets: 15 conversations, 8 pilot acceptances, 4 active by Demo Day and 8 during adoption. None is committed. Eight merchants are forecast to refer 100-125 wallets (about 13-16 each); 5-10 pre-M1 conversions and 15-25 additional launch-channel wallets bring the total to 120-160.

The App Store, X, YouTube, Medium/Coinmonks, r/Cardano and Cardano Forum will share the release. Partnerships and Android add no forecast usage.

Post-M1 days 1-5: 4 merchants, 15 wallets and 25 payments.\
Days 6-10: 4-5 merchants, 35-50 wallets and 95 cumulative payments.\
Days 11-14: 5-6 merchants, 60-80 wallets and 155 cumulative payments.

Only real external purchases count. Team wallets, tests, circular transfers, subsidies, rewards and reimbursed fees are excluded.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/b3G6GJPCles

### Who else solves this today - competitors/alternatives, and why does your approach win?

Merchants can already use conventional processors such as Stripe or Square for fiat payments. Cardano users can already transfer ADA and native assets through general-purpose wallets, and USDCx users can use separate bridge and wallet interfaces.

Vendano sits between those experiences.

It does not attempt to replace a full merchant processor or compete on the number of advanced wallet features. The product is intentionally focused on a simple Cardano checkout.

The differentiator is a payment-first iOS experience combined with self-custody. Funds move directly between customer and merchant wallets on Cardano rather than through a Vendano-controlled account.

### Please provide details about the Technology Readiness Level selected for your existing product

Vendano is TRL 7 because it is packaged, publicly distributed by Apple and operating on Cardano mainnet. Apple's listing identifies Vendano LLC and distributes the signed iPhone/iPad binary. The app supports wallet creation/import, local self-custody keys, ADA transactions, contact payments, history and Store Mode.

GitHub is source for developers, not customer distribution. Production configuration, secrets and Apple signing material are intentionally excluded. Customers install the App Store binary; they do not clone the repository, open Xcode or provide keys.

USDCx is new work and is separately declared TRL 2.

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

Vendano is substantially self-funded; this 75,000-ADA request funds future USDCx work, not reimbursement.

Deliverable: a production iOS App Store release with USDCx balances, transfers and merchant checkout.

Allocation:\
22,000 - multi-asset engineering: balances, transactions, coin selection, minimum ADA and history.\
13,000 - merchant/customer checkout UX.\
8,000 - funding/cash-out onboarding, fees/minimums, help and FAQ.\
12,000 - QA and App Store release.\
7,000 - Catalyst tagging, evidence and technical documentation.\
13,000 - merchant outreach, onboarding and launch support.

Android is outside the funded milestone and contributes no assumed usage. USDCx must feel like understandable digital cash, not merely another token.

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

 9. At least 4 external merchant wallets active by Demo Day.

10. At least 15 external customers completing 25 genuine mainnet USDCx payments without subsidy or reimbursed fees.

11. Release notes, no-smart-contract architecture, QA evidence, bug log and security note.

12. Live Demo Day walkthrough using the App Store build and measured flow.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

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
- https://www.youtube.com/watch?v=sg9nyvCmUQ4
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

750

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

275

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The funded USDCx integration is TRL 2: the concept and implementation path are defined, but Vendano has not generated or submitted a USDCx payment transaction. No retroactive work is requested.

Feasibility is supported by Vendano's mainnet wallet and Cardano.swift. Vendano identifies and displays HOSKY, the same ledger asset type as USDCx, and preserves tokens in change during ADA sends, but does not create a native-asset payment output. This is enabling architecture, not a USDCx proof of concept.

Funded work covers verified USDCx identifiers/decimals; balances; multi-asset outputs, selection and change; fees/minimum ADA; merchant/customer UX; funding/cash-out guidance; transaction status/errors; Catalyst tagging; tests, documentation and App Store release.
