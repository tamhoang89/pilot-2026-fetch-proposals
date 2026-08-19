# Ascend: Oracle-Settled FX and Macro Markets on Cardano

> Trade FX, rates, indices and macro prints against stablecoins, priced by Pyth, settled on Cardano. Every trader and institution carries a CIP-0170 identity; access is jurisdiction-gated by design.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1u8hw2us3hg84nacemj64870vkasq5trj8puaznzr6rkaqeqm66q7e`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T05:06:52.705000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Uzair, founder and CEO of Ascend (BVI), <https://x.com/Ascend_Uzi>: designed and shipped the Ascend venue, live on Midnight public mainnet beta at 485 registered users and over 1M transactions processed, and leads market design, pool risk parameters and the DID gating policy directly.

Five in-house engineers, employed by Ascend and dedicated full-time to this build, covering the market and settlement validators, the Pyth consumption module and price pipeline, the CIP-0170 identity layer via signify-ts, the liquidity pool and gateway contracts, and the terminal and onboarding. That team built and operates the live Midnight venue behind those numbers, so delivery evidence is a running product with real users, not a claim.

Engaged from award: security auditor for the third-party review; compliance counsel for the venue perimeter and jurisdiction gating list; Pyth Pro developer subscription, free for Cardano builders via Intersect; and issuer integrations for USDM and USDCx. We have no separate quant or compliance hire and state that rather than padding the roster.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Give-back pledge: once cumulative settled notional across Ascend markets exceeds US$25M on mainnet, Ascend will return 10% of this grant to the Cardano treasury; a further 10% at US$100M. Both thresholds are measurable from our declared on-chain footprint.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: traders, LPs, institutions and gateway users, every counted action submitted and paid from the acting party's own wallet. Opens and closes move stablecoin margin with a Pyth update consumed in the same transaction, daily across FX and index markets. Payouts are claimed by the trader, each carrying their CIP-0170 attestation. LPs deposit and withdraw, users self-anchor credentials at onboarding, and the gateway runs from M1.

That gives \~2,900 settlement-class transactions plus \~1,500 lighter movements and \~600 anchors, from 250–450 trader wallets, 20–50 LPs and 5–15 institutions, against minimums of 30/36/10. Econ-print days ladder under the 20% daily cap. No rebates or paid market making in any measured period.

### How will you reach and onboard real users - and what evidence backs your channels?

Named channels: 250–450 trader wallets, converted first from the 485 registered users on our Midnight testnet, already wallet-native, then from the Ascend community and Cardano trader channels; 20–50 external LP wallets; 5–15 institutional accounts from prop desk and OTC conversations. Minimums: 30 / 36 / 10 external wallets.

Onboarding is wallet-native and gated by design: each user self-anchors a CIP-0170 credential (jurisdiction checks pass or onboarding stops), sets up self-custody, and funds gas and margin via CEX withdrawal or issuer on-ramp, the pattern the stablecoin guide expects and asks us to document early, which we will. Every open, settle, claim, LP movement and gateway transaction is submitted and paid by the user's wallet, unbatched by design. First two weeks: 6 markets and the gateway live at Demo Day, LP deposits in tranches, settlements daily from epoch 1.

Concentration: large traders and LPs expected, documented pre-window, §6.2, &gt;35% wallet fees at half-count.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Strike Finance is the Cardano incumbent and the real comparison: live since May 2025, 10x–100x leverage, oracle-priced, a board spanning crypto, equities, commodities and indices. We compete for none of it. Our twelve have zero overlap with their board: four FX pairs, three US Treasury rates, three economic prints, GMCI30 and ACRED. Their board is also our evidence, since their non-crypto markets trade heaviest. Two further gaps: Strike sells trading without identity verification, while we gate every account behind a CIP-0170 credential with jurisdiction checks, the only form an institution can clear internally; and Strike collateralises in ADA, while we denominate in verified stablecoins, which makes FX quoting coherent. Off-Cardano, Ostium proves the asset class but is anonymous.

### Please provide details about the Technology Readiness Level selected for your existing product

Ascend is an oracle-settled venue for FX and macro markets. TRL 5 and beyond, validated with real users in live operation: the venue runs on Midnight public mainnet beta, a Cardano partner chain, with 485 registered users and over 1M transactions processed, batched into 41k+ on-chain transactions, all inspectable in our explorer at [beta.trade.ascend.market](http://beta.trade.ascend.market). The trade lifecycle operates end to end there: margin posted from an external wallet, a position opened against an oracle price reference, settlement at that price, and payout to the user. This grant builds the Cardano layer for that venue: audited, consuming live Pyth feeds via the documented withdraw-script pattern, settling in USDM and USDCx, with CIP-0170 gating, the liquidity pool and the gateway.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Oracle provider: Pyth, via Pyth Pro on Cardano, in production since May 2026. Declared feeds: four FX pairs, three US Treasury rates, three economic indicators, GMCI30, ACRED NAV. Consumption follows the documented Cardano pattern: our backend subscribes to the Pyth Pro websocket and the user's transaction includes the signed price update via a zero-withdrawal from the Pyth withdraw script, verifying price on-chain in the transaction that opens or settles.

Each market is a margin/position validator plus a settlement validator, settled in USDM/USDCx against the pool. Opening posts margin carrying the signed update; closing does the same; payouts are claimed by the trader's own wallet, each claim carrying their CIP-0170 attestation. LP deposits and withdrawals move stablecoins through the pool; the gateway moves USDM/USDCx between users' wallets and Ascend accounts.

Counted: Oracles = user transactions consuming the declared feeds; updates we or Pyth push count zero. Stablecoins = user transactions moving USDM/USDCx in the footprint. Identity = self-anchors plus the attestation on every claim. Treasury, pool-seed and ops wallets declared own-wallet by stake key. Message tag on every tx from M1.

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

Demand for outside-world exposure on Cardano is already proven, by a competitor. Strike Finance has run leveraged perps here since May 2025, and its board now spans equities, commodities and equity indices alongside crypto, with the non-crypto markets trading heaviest. Traders here pay real money for exposure beyond crypto. What no Cardano venue quotes is the macro layer underneath: not one currency pair, not one Treasury rate, not one CPI or GDP print.

We measured the same pull ourselves. Our venue on Midnight testnet has 485 registered users and has processed over 1M testnet transactions, with equity and index markets drawing the heaviest usage. We present testnet activity as a demand signal, never as revenue.

The category is proven off-chain too: Ostium built this exact shape, oracle-settled FX and indices against a pool, into real volume on Arbitrum. Both prerequisites are already live on Cardano: verified stablecoins (USDM, USDCx) and Pyth Pro in production since May 2026, carrying the precise catalog we list.

Conversion channels: the 485-strong Midnight testnet cohort, already wallet-native; the Ascend community across Discord, X and Telegram; Cardano trader communities and existing DEX user bases; and prop desks and OTC participants who need jurisdiction-gated venues before they can touch on-chain macro exposure.

### Applicant name

Uzair Khan

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Who pays: (1) traders pay a flat 8 bps taker fee on notional at open and close, settled in stablecoins; no maker rebates, no fee holidays, no points, during any measured period or after; (2) external LPs earn the pool's share of trading fees, protocol takes 10% of pool fees; (3) a funding rate on open positions, accrued and settled in stablecoins; (4) a 10 bps gateway fee on deposits and withdrawals. The grant funds only the chain integration; venue economics fund operations.

Why usage persists after the window: settlement is the product working, so every open, close, claim and LP movement is a fee-bearing transaction for the venue's operating life; each new market from the Pyth catalog (12 at launch, the catalog is deeper) opens new flow with zero grant incentive attached. Network fees here are the byproduct of a venue functioning, which is exactly what the kicker measures.

### On-chain identity (CIP-0170) - expected transaction count

1600

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Validated on public testnet at our own cost; without this grant it does not reach mainnet. Unfunded today: third-party audit and hardening, live Pyth Pro integration across 12 feeds, verified-policy integration, the pool and gateway contracts, the terminal, DID gating, and adoption operations. Nothing is retroactive; every deliverable is new work on newly deployed identifiers. No grant ADA is ever trading capital, and none seeds the pool, which is proprietary capital in declared own wallets, counting zero.

Spend (ADA): validators, Pyth module and security review 65,000; CIP-0170 identity layer 35,000; platform and terminal 40,000; pool contracts 15,000; gateway 15,000; issuer integrations 15,000; compliance ops 8,000; deployment and launch 5,000; contingency 2,000.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, live on Cardano mainnet and demonstrated at Demo Day:

1. Venue live with 6 markets on Pyth Pro feeds (EUR/USD, USD/JPY, GBP/USD, AUD/USD, GMCI30, US10Y), settled in USDM/USDCx against the pool.
2. CIP-0170 identity live: self-anchored credentials gating onboarding for users and institutions, jurisdiction checks enforced, attestations riding every claim.
3. Liquidity pool live: external LP deposits and withdrawals, pro-rata fee accrual, user-submitted.
4. Stablecoin flows live on the declared policies: margin, settlement, payout claim, LP movements, gateway deposits and withdrawals, all user-paid and unbatched.
5. Message tag on all transactions and the footprint declared: script hashes, addresses, identifiers, team, treasury and pool-seed stake keys.
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

FX is the largest market on earth and it does not exist on Cardano. Cardano has a derivatives venue, Strike Finance, listing crypto, equities, commodities and indices, and its non-crypto markets trade heaviest, which tells you traders here want outside-world exposure. But no venue here quotes a currency pair, a Treasury rate or an economic print. Pyth Pro has run in production on Cardano since May 2026 carrying exactly those feeds. The macro data layer shipped; nothing trades it.

Ascend is that venue. Oracle-settled markets margined and settled in verified stablecoins (USDM, USDCx), priced by Pyth against a liquidity pool: four FX pairs, three US Treasury rates, three economic prints, a crypto index and tokenized-fund NAV. Every trader and institution self-anchors a CIP-0170 credential gating access by jurisdiction, and a verification attestation rides every settlement claim.

Who has this problem: traders who leave Cardano for macro exposure; institutions needing jurisdiction-gated, verifiable counterparties before touching on-chain markets; and Cardano itself, with live stablecoins and Pyth feeds and nothing connecting them.

What exists today: the venue runs live on Midnight testnet with 485 registered users and over 1M testnet transactions. This grant builds the Cardano settlement layer, audited, on live Pyth feeds and verified stablecoin policies, with the pool and gateway.

### Supporting links (repo, site, demo)

- https://www.ascend.market/
- https://pub.beta.ascend.market/

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

4400

### Funder, status, and what it covers

Ascend raised capital to build an institutional-grade perpetuals venue on Midnight. We disclose it here for completeness: it is a private raise, not a grant, treasury or accelerator program, and no public, ecosystem or institutional grant funder is involved.

Status: raised and deployed. The Midnight venue is live on public mainnet beta with 485 registered users and over 1M transactions.

What it covers: the Midnight implementation only, matching, risk, settlement and the trading front end on Midnight's stack. It funded no Cardano work, and none of the integrations declared here.

What this grant would fund: Pyth Pro consumption via the documented withdraw-script pattern, settlement in verified USDM and USDCx, the CIP-0170 identity and gating layer, liquidity pool and gateway contracts, third-party audit and mainnet deployment. No deliverable overlaps and no cost is billed twice.

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1200

### Current funded commitments

No member of the team is delivering a milestone for Project Catalyst, the Cardano treasury, Intersect, Builder DAO, an accelerator, a public or institutional funder, or a grant program on any other chain. Ascend has no prior or current Catalyst project and nothing in arrears.

The one commitment worth naming: Ascend's investors backed the institutional-grade perpetuals venue on Midnight. Role: Uzair as founder and CEO, with the five in-house engineers. That product is built and live on public mainnet beta, so what remains is operation and iteration, not milestone delivery against a funder's schedule, and it carries no external reporting obligations competing with this grant.

Expected completion: the Midnight venue is delivered and in live operation. The same five engineers are assigned to the Cardano build funded here, which is separate, new work on newly deployed identifiers, with no shared deliverables and no double-billed cost.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

All three integrations are validated end-to-end on Cardano public testnet. Oracle leg: settlement transactions carry a signed price update in the documented Pyth shape, a zero-withdrawal from the withdraw script, user-submitted and user-paid; mainnet swaps the fixture for live Pyth Pro updates on the declared feed IDs. Stablecoin leg: margin, settlement, payout claim, LP movements and gateway flows run on Preview against a test-policy stand-in. Identity leg: credentials self-anchored via signify-ts, jurisdiction gating at onboarding, attestations riding every claim. Every counted transaction is user-submitted and unbatched by design. Nothing is on mainnet and no declared identifier has carried prior traffic, so the footprint is §4.1 clean. Path: audit by week 6, TRL 8 mainnet at M1.
