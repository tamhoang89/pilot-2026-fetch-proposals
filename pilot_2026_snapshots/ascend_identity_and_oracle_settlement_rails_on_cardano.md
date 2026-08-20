# Ascend: Identity and Oracle Settlement Rails on Cardano

> A CIP-0170 identity layer and Pyth-anchored stablecoin settlement for FX, rates and macro exposure on Cardano. Fully collateralised, no leverage, no liquidity pool, open source.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1u8hw2us3hg84nacemj64870vkasq5trj8puaznzr6rkaqeqm66q7e`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T00:25:03.789000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Uzair Khan, founder and CEO, Ascend (BVI). <https://www.linkedin.com/in/uzair-khan-58b2472b5> · <https://x.com/Ascend_Uzi>. Shipped the Ascend venue, live on Midnight public mainnet beta at 485 registered users and over 1M transactions. Leads market design, jurisdiction gating policy and Cardano integration architecture.

Vigneshwaran B, protocol engineer. <https://www.linkedin.com/in/vigneshwaran-b-9963b1317>. Owns the collateral escrow and settlement validators and the Pyth consumption module, including the withdraw-script price-update pattern.

Gowtham, engineer. <https://linkedin.com/in/gowtham-dev-b72a7b403>. Owns the CIP-0170 identity registry and gating via signify-ts, and the gateway contracts.

Both are allocated from Ascend's five-person engineering team, which built and operates the live Midnight venue; the other three stay on that product and no part of their cost is billed here.

Security audit: shortlisted Anastasia Labs, TxPipe and MLabs, all established Cardano Plutus auditors. Engagement is signed on award and the firm named in the Statement of Milestones before any mainnet deployment.

Compliance counsel: BVI corporate counsel for the perimeter opinion and jurisdiction gating list, engaged on award and named at KYB.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Give-back pledge: once cumulative settled collateral across Ascend markets exceeds US$25M on mainnet, Ascend will return 10% of this grant to the Cardano treasury; a further 10% at US$100M. Both thresholds are measurable from our declared on-chain footprint.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

The three tallies overlap by construction: one settlement transaction consumes the Pyth feed, moves the stablecoin and carries the CIP-0170 attestation, counting once in each. They are not additive. Distinct on-chain transactions across the window are \~5,000.

Who transacts: traders and institutions, every action submitted and paid from their own wallet, unbatched. Opening posts full stablecoin collateral with a Pyth update consumed in the same transaction. Settlement executes at the attested price and the payout is claimed by the user, carrying their attestation. Users self-anchor credentials at onboarding; the gateway runs from M1.

Derived from \~320 active wallets at 1.6 settlement-class transactions per wallet per epoch. No rebates, yield or paid market making.

Our plan for the first two weeks after going live: floors bind per epoch, so we ramp rather than spike. Waitlisting, jurisdiction pre-screening and institutional KYB run pre-launch. The unfloored entry epoch is onboarding, two markets open so matching concentrates. Epochs 1-3 run 12/14/16% of target against 8.33% floors; steady state from epoch 4. Session-spread flow, no day near the cap.

### How will you reach and onboard real users - and what evidence backs your channels?

Wallet plan, derived rather than asserted. We model 35% of the 485 Midnight users converting to Cardano, roughly 170 wallets, on the basis that they are already wallet-native and self-custodial, so the switching cost is a wallet, not a behaviour. Community and Cardano trader channels add \~130, and 15–40 institutional accounts require gated access. That gives \~320 active wallets in the 250–450 range, against minimums of 30 / 36 / 10.

Frequency: \~2,900 settlement-class transactions over a 6-epoch window across \~300 traders is 1.6 per wallet per epoch, roughly one position opened and closed every six days. Collateral and gateway movements add \~5 per wallet, and each onboarded wallet anchors one credential.

Onboarding is gated: users self-anchor a CIP-0170 credential (jurisdiction checks pass or onboarding stops) and fund collateral by CEX withdrawal or issuer on-ramp, documented with the program early. Every transaction is user-submitted, user-paid and unbatched.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Strike Finance is the Cardano incumbent for on-chain derivatives: live since May 2025, 10x–100x leverage, oracle-priced, a board spanning crypto, equities, commodities and indices. We are not competing with them and we are not building a leveraged venue. Our twelve settlement markets have zero overlap with their board: four FX pairs, three US Treasury rates, three economic prints, GMCI30 and ACRED. Their board is our evidence, since their non-crypto markets trade heaviest. The deeper gap is identity: Strike sells trading without identity verification, a legitimate choice and the opposite of ours, so no Cardano application today can obtain a verified, jurisdiction-gated counterparty. We are shipping that as open infrastructure rather than as a private feature.

### Please provide details about the Technology Readiness Level selected for your existing product

Ascend is an oracle-settled venue for FX and macro exposure. TRL 5 and beyond, validated with real users in live operation: the venue runs on Midnight public mainnet beta, a Cardano partner chain, with 485 registered users and over 1M transactions processed, batched into 41k+ on-chain transactions, inspectable in our explorer at [beta.trade.ascend.market](http://beta.trade.ascend.market). The full lifecycle operates there: collateral posted from an external wallet, a position opened against an oracle price reference, settlement at that price, payout to the user. This grant funds the Cardano rails only: CIP-0170 identity, Pyth attestation, and fully collateralised stablecoin settlement. The leveraged product stays on Midnight and is not part of this scope.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

One settlement spine, three integrations riding it, all newly deployed and MIT licensed.

Oracle provider: Pyth, via Pyth Pro on Cardano, in production since May 2026. Declared feeds: four FX pairs, three US Treasury rates, three economic indicators, GMCI30, ACRED NAV. Consumption follows the documented Cardano pattern: our backend subscribes to the Pyth Pro websocket and the user's transaction includes the signed price update via a zero-withdrawal from the Pyth withdraw script, verifying price on-chain in the transaction that opens or settles.

Each market is a collateral escrow validator plus a settlement validator. Two counterparties each post full notional in USDM or USDCx; neither borrows and there is no pool. Settlement executes at the attested price; the payout is claimed by the winner's own wallet, each claim carrying their CIP-0170 attestation. The gateway moves USDM/USDCx between users' wallets and Ascend accounts.

Counted: Oracles = user transactions consuming the declared feeds. Stablecoins = user transactions moving USDM/USDCx in the footprint. Identity = self-anchors plus the attestation on every settlement. Treasury and ops wallets declared own-wallet by stake key. Message tag on every tx from M1.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

Yes

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Demand for outside-world exposure on Cardano is proven by a competitor. Strike Finance has run leveraged perps here since May 2025, its board now spanning equities, commodities and indices alongside crypto, with the non-crypto markets trading heaviest. Traders here pay real money for exposure beyond crypto. What no Cardano venue offers is the macro layer underneath, and none offers identity: not one currency pair, not one Treasury rate, not one CPI print, and no jurisdiction-gated counterparty anywhere on the chain.

We measured the same pull ourselves. Our Midnight venue is live on public mainnet beta with 485 registered users and over 1M transactions, independently verifiable in our public explorer rather than self-reported.

The identity layer is its own demand story, independent of us. Every Cardano application needing a verified, jurisdiction-gated counterparty has nothing to build on today. We ship that as open infrastructure, and prop desks and OTC participants in conversation with us have said plainly they cannot touch anonymous venues.

Conversion channels: the 485-strong Midnight cohort, already wallet-native and holding self-custody wallets; the Ascend community across Discord, X and Telegram; Cardano trader communities; and institutional counterparties requiring gated access.

### Applicant name

Uzair Khan

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Who pays: (1) a flat settlement fee per settled position, denominated in stablecoins, charged on full collateral rather than on leveraged notional; (2) an attestation service fee for institutions requiring credentialed counterparty verification; (3) a 10 bps gateway fee on stablecoin deposits and withdrawals; (4) support and integration contracts for third parties building on the open-source SDK. There is no borrow rate, no funding rate, no LP yield and no revenue derived from leverage.

Why usage persists after the window: settlement and attestation are the rails working, so every position settled, every credential anchored and every gateway movement is a fee-bearing transaction for as long as the infrastructure operates. Each additional market from the Pyth catalog, and each third party adopting the identity registry, adds flow with zero grant incentive attached. Network fees here are the byproduct of infrastructure being used, which is what the kicker measures.

### On-chain identity (CIP-0170) - expected transaction count

1600

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

What exists is a Preview prototype with fixtures and test-policy stand-ins. What is funded is production, priced against two allocated engineers over three months plus external audit.

Spend (ADA): escrow and settlement validators (2 validator pairs, 4 markets at M1 scaling to 12), Pyth module across 12 declared feeds, third-party audit and remediation, 70,000; CIP-0170 registry covering issuance, verification, revocation, gating and the institutional tier, 45,000; gateway engineering and USDM/USDCx integration, permissionless and carrying no partnership fee, 25,000; terminal, onboarding and explorer, 30,000; SDK and docs, post-M1, 15,000; compliance ops, 8,000; deployment and launch, 5,000; contingency, 2,000.

Not funded by design: leverage, margin, pools, yield, funding rates.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, live on Cardano mainnet and shown at Demo Day. Scope is narrow by design, sized to two engineers plus external audit:

1. Four settlement markets live on Pyth Pro feeds (EUR/USD, USD/JPY, GMCI30, US10Y), fully collateralised in USDM/USDCx. The other eight launch through the adoption window as footprint additions.
2. CIP-0170 identity registry live: self-anchored credentials gating onboarding for users and institutions, jurisdiction checks enforced, attestations on every settlement.
3. Escrow and settlement validators live, third-party audited, report published.
4. Stablecoin flows live on declared policies: collateral posts, settlements, payout claims, gateway deposits and withdrawals, user-paid and unbatched.
5. Message tag on all transactions and the footprint declared: script hashes, addresses, identifiers, team and treasury stake keys.
6. Demo Day: an external user opens and settles EUR/USD on mainnet, Pyth update consumed, stablecoin settled, attestation carried.

### Oracles - expected transaction count

2900

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

380

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano has verified stablecoins and, since May 2026, Pyth Pro in production with FX, US Treasury rate, GDP, WAGEGROWTH, CPIINDEX, index and NAV feeds. Nothing consumes them. Cardano also has no on-chain identity layer for financial applications: counterparties are anonymous, so institutions and any jurisdiction-gated use case cannot operate here.

Ascend operates two separate products. Our leveraged perpetuals venue runs on Midnight, is privately funded, and is not part of this proposal. What this grant funds is separate and new: settlement rails on Cardano, fully collateralised, with no leverage, no margin, no liquidity pool and no yield.

Three components, all newly deployed and MIT licensed:

1. A CIP-0170 identity registry. Traders and institutions self-anchor credentials; jurisdiction checks gate access; a verification attestation rides every settlement.
2. Pyth price attestation. The signed update is consumed inside the user's own transaction via the documented withdraw-script pattern, putting a verifiable settlement price on-chain.
3. Fully collateralised settlement. Peer-matched positions on FX, rates, macro prints, an index and NAV; each side posts full notional in USDM or USDCx into escrow; settled at the attested price; payouts claimed by the user's own wallet.

Nothing funded lends, borrows or provides leverage. The rails are use-case neutral and open source. Ascend is the first consumer, not the only one.

### Supporting links (repo, site, demo)

- https://www.ascend.market/
- https://cardano-pre.ascend.market/

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

1050

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

Yes, MIT. The entire funded layer is open source: the collateral escrow and settlement validators, the Pyth consumption module, the CIP-0170 identity registry and gating, the attestation tooling, the gateway contracts and the SDK. Nothing in the funded scope is proprietary

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

4400

### Funder, status, and what it covers

Ascend raised public capital for $ASCEND token to build an institutional-grade perpetuals venue on Midnight. We disclose it here for completeness: it is a private raise, not a grant, treasury or accelerator program, and no institutional grant funder is involved.

Status: raised and deployed. The Midnight venue is live on public mainnet beta with 485 registered users and over 1M transactions.

What it covers: the Midnight implementation only, matching, risk, settlement and the trading front end on Midnight's stack. It funded no Cardano work, and none of the integrations declared here.

What this grant would fund: Pyth Pro consumption via the documented withdraw-script pattern, settlement in verified USDM and USDCx, the CIP-0170 identity and gating layer, and gateway contracts, third-party audit and mainnet deployment. No deliverable overlaps and no cost is billed twice.

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1200

### Current funded commitments

No member of the team is delivering a milestone for Project Catalyst, the Cardano treasury, Intersect, Builder DAO, an accelerator, a public or institutional funder, or a grant program on any other chain. Ascend has no prior or current Catalyst project and nothing in arrears.

The one commitment worth naming: Ascend's investors backed the institutional-grade perpetuals venue on Midnight. Role: Uzair as founder and CEO, with the five in-house engineers. That product is built and live on public mainnet beta, so what remains is operation and iteration, not milestone delivery against a funder's schedule, and it carries no external reporting obligations competing with this grant.

Expected completion: the Midnight venue is delivered and in live operation. Engineers from same team are assigned to the Cardano build funded here, which is separate, new work on newly deployed identifiers, with no shared deliverables and no double-billed cost.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

All three integrations are validated end-to-end on Cardano public testnet. Oracle leg: settlement transactions carry a signed price update in the documented Pyth shape, a zero-withdrawal from the withdraw script, user-submitted and user-paid; mainnet swaps the fixture for live Pyth updates. Stablecoin leg: escrow, settlement, payout claim and gateway flows run on Preview against a test-policy stand-in. Identity leg: credentials self-anchored via signify-ts, gating at onboarding, attestations on every settlement.

What exists is a Preview prototype. What this grant funds is production: audit and remediation, hardening, live feeds replacing fixtures, verified policies replacing stand-ins, mainnet deployment. Nothing is on mainnet and no declared identifier has carried traffic.
