# The Grid Protocol: USDCx-to-USD for Local Businesses

> Metro Atlanta has real ADA/stablecoin holders with no local businesses to spend at. The Grid Protocol builds the missing supply side: USDCx to real fiat, no crypto exposure for the business.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 37
- **Proposer:** `stake1u9pql8dvjfvym2zjhnm5x7fk2sv9l4zfv8xhmjkx444q80qkqty7f`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-24T10:15:54.908000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Alonzo G. founder and operator, brings 20 years as an L3 Support Analyst and IT infrastructure consultant, plus 4 years of Azure/Microsoft 365 cloud solutions experience — the same systems-reliability discipline this integration depends on, since a payout pipeline touching real business funds needs to be built and monitored like production infrastructure. Alonzo has also been an active Cardano community member for 6 years, and is an active member of the ABC Atlanta Black Chambers, connecting this work directly to the local business community it's designed to reach.

More importantly, this isn't a team proposing to build from a standing start: we already operate The Grid Protocol as a live product — registration and moderation pipeline, KYB verification via Didit, Stripe-based booking and payments with real refund handling, and an owner-facing dashboard with CSV/PDF export — all shipped and running with 40 real business sign-ups. This proposal adds Cardano-specific integration on top of infrastructure we've already proven we can build and operate reliably.

For the parts outside our core expertise, we're not overreaching: Saqib Shoukat — Top Rated on Upwork, 100% Job Success score, 19 completed jobs, 1,400+ hours delivered, with production Stripe payment integration experience — is contracted to build the Transak Stream and MoonPay off-ramp integration, and an independent third-party security firm (Cyberscope or Zealynx Security) audits it before launch.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Customers are Cardano/stablecoin holders paying for real goods and services at Grid Protocol businesses — not wash transactions. The pilot activates 18 of our 40 sign-ups (45%), reaching \~153 payments across the declared window: one entry epoch plus six floored 5-day epochs, \~35 days. Recruitment runs through the ABC Atlanta Black Chambers network.

Demand is not only local. Four to five businesses ship via EasyPost, US domestic: books nationally, wine within permitted states. That widens the buyer pool to US Cardano holders anywhere and adds volume not capped by foot traffic or appointment slots. Outreach splits accordingly — Cardano channels for shippable goods, geo-targeted Atlanta outreach for services.

Circle publishes no standing per-transaction xReserve fee, so this derives from documented Cardano network costs. Simple transfers run \~0.17–0.20 ADA; script interactions add execution fees, with IOG examples putting dApp flows near 1.5 ADA. We model each payment as two counted transactions — USDCx transfer plus burn/redemption — at \~1.7 ADA combined: \~306 transactions, \~260 ADA. Estimate pending confirmation in Tranche 1; actuals replace it in reporting.

### How will you reach and onboard real users - and what evidence backs your channels?

We're not starting from zero — reach and onboarding channels are already proven, not hypothetical. Our existing 40-business cohort is the recruitment pool for the pilot: they're already signed up, already KYB-verified, and already using the platform, so onboarding them to a new payout option is a feature announcement to an existing user base, not cold outreach.

For business-side growth, the ABC Atlanta Black Chambers network — where our operator is an active member — gives direct, warm access to member businesses.

For consumer/holder-side awareness, we use Cardano's own community channels where crypto holders already gather looking for ways to use their holdings, alongside geo-targeted metro Atlanta outreach. Because four to five businesses in the base ship goods nationally via EasyPost, the Cardano channel reaches buyers who can actually transact rather than only those in Atlanta. Evidence backing these channels: the 40 existing sign-ups themselves.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Crypto debit cards (Coinbase Card, [Crypto.com](http://Crypto.com)) let holders spend crypto via Visa rails, but offer no local discovery and no Cardano-specific focus. Crypto-payment processors (BitPay, Strike) let individual businesses accept crypto, but each must integrate and market it separately — no existing audience already browsing to find them.

The Grid Protocol combines both: a live, already-used local directory (40 sign-ups, real bookings) plus built-in USDCx acceptance with zero setup burden — no wallet, no integration, funds arrive as USD automatically. Businesses get discovery and payment together; customers get a map of real, KYB-verified businesses that accept what they hold. No competitor pairs Cardano-native stablecoin acceptance with an active local discovery platform.

### Please provide details about the Technology Readiness Level selected for your existing product

The Grid Protocol itself is TRL 9 — an actual system proven in an operational environment, not a lab result or pilot claim. It is live in production at [thegridprotocol.com](http://thegridprotocol.com) with 40 real business sign-ups, a working registration and moderation pipeline, KYB verification via Didit processing real approvals, a live Stripe-based booking and payments system handling real transactions and refunds, and an owner-facing sales/payments dashboard with CSV/PDF export already in daily use. This proposal does not build a new product; it adds a Cardano-specific payment integration onto infrastructure that has already been operating since July 2026.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Our on-chain architecture deliberately avoids building or deploying any new smart contracts on Cardano. Each participating business receives a standard Cardano wallet address (UTXO-based, generated via standard Cardano tooling), displayed on their Grid Protocol profile. Incoming USDCx transactions to that address are monitored off-chain via a Cardano data provider (Blockfrost or Koios), triggering our dashboard to reflect activity in near-real time.

Conversion itself happens through Circle's existing xReserve smart contract system, which redeems USDCx 1:1 for USDC non-custodially — we do not write or operate any conversion logic on-chain ourselves. The final USDC-to-USD off-ramp is handled by a licensed money-services provider — Transak Stream as primary, MoonPay as named fallback — via their off-ramp APIs.

This architecture is the right fit for a stablecoin-integration pilot because it composes already-audited, already-live Cardano and cross-chain infrastructure rather than introducing new on-chain code and its associated security surface. Our engineering effort goes entirely into integration and UX — the off-chain dashboard, monitoring, and business onboarding — which matches both our team's actual expertise and the pilot's preference for low-risk, real-world integrations onto existing working products rather than novel protocol development.

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

Our target market has two sides. Businesses: local, community-facing businesses in Atlanta, with an initial focus on Black-owned businesses through the ABC Atlanta Black Chambers network our operator is an active member of. Customers: Atlanta's ADA and stablecoin holders who want to spend crypto locally instead of only trading or holding it.

Evidence of demand splits similarly. On the business side, we have direct, measurable traction: 40 real business sign-ups on a live platform, a working KYB verification pipeline, and an operating Stripe-based booking and payments system — not projections, a working product. On the consumer side, we're relying on strong proxy evidence rather than pilot data, since the USDCx flow itself hasn't launched yet: roughly one in four American adults now own cryptocurrency nationally, Atlanta has an active, established Cardano and broader crypto community, and 87% of crypto holders report active usage (up from 80% the prior year), with 40% already using crypto to pay for goods and services.

We see this pilot's usage-tracked disbursement structure as the actual product-market-fit test: real conversion volume and payout activity from our existing 40-business base will be the first hard evidence, not a survey.

### Applicant name

TheGridProtocol LLC

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The Grid Protocol already runs as a real business independent of this grant: revenue comes from paid Spotlight/Sponsor placements, booking fees on Stripe transactions, and business subscriptions — all live today, funding hosting, KYB, and operations regardless of Catalyst funding.

The USDCx integration adds a small transaction-based revenue stream: a modest platform margin on converted volume, similar to the fee already applied to Stripe bookings, so it's self-sustaining rather than a permanent cost center.

Who pays and why it continues: businesses pay for visibility and payment infrastructure they already value enough to sign up for (40 have, before any crypto feature existed); customers pay for goods and services as normal, just with crypto now usable locally. Once live, no ongoing Catalyst funding is needed — maintenance is a founder-led, low-cost task on infrastructure already paid for by the existing business.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, the integration doesn't happen on any near-term timeline a bootstrapped local platform can't self-fund a contracted blockchain developer, an independent security review before live business funds move through the pipeline, or the outreach needed to bring customers to participating businesses.

At a high level: contracted developer (25%) builds the off-ramp integration and payout dashboard; security review (28%) covers the integration and dashboard only; consumer acquisition (28%) funds metro-Atlanta and national Cardano-holder outreach, since the pilot needs paying customers as well as businesses; education & reporting (12%) covers documentation, the case study, and Catalyst reporting; contingency (7%) covers ADA/fiat risk. Founder-led work is contributed, not funded.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month window: off-ramp integration built and connected to a licensed provider account — Transak Stream as primary, MoonPay as named fallback; per-business USDCx receiving addresses provisioned for the pilot cohort; dashboard integration live, surfacing payout status alongside existing Stripe history; footprint declared (per-business receiving addresses, registered message tag on provider-triggered transactions, no team-controlled wallets counted); at least one verified end-to-end mainnet transaction completed by a real user, with the flow repeating without failure across independent runs; release notes documenting architecture, scope, and limitations; independent security review completed on the integration and dashboard display; live demo delivered at Demo Day using the declared identifiers and flows.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

The Grid Protocol is a live directory platform ([thegridprotocol.com](http://thegridprotocol.com)) connecting Atlanta businesses with customers via an interactive map  40 business sign-ups, a working KYB pipeline, and a live Stripe-based booking and payments system.

We're building a licensed USDCx-to-USD conversion and payout pipeline, integrated into our existing business dashboard, so local ADA and stablecoin holders can pay for real goods and services at Grid Protocol businesses, while the business receives predictable US dollars in their bank account no wallet or crypto literacy required.

The problem: roughly one in four American adults now own cryptocurrency, and Atlanta has an active Cardano and crypto community, but holders currently have no way to spend it at local businesses they already support. Meanwhile, local businesses — particularly Black-owned businesses, a meaningful share of our sign-ups  have limited low-friction ways to reach new customers or get paid without cash handling or middleman fees.

USDCx is dollar-pegged and backed 1:1 by USDC, removing price volatility for the business. Conversion and payout are handled by a licensed third-party off-ramp provider — Transak Stream as primary, MoonPay as named fallback, so no party ever holds custody or signing keys, and no money-transmitter burden falls on our platform.

This gives Cardano a real, documented example of a stablecoin becoming spendable money in the local physical economy.

### Supporting links (repo, site, demo)

- https://thegridprotocol.com
- https://www.linkedin.com/in/alonzo-green-989581303
- https://github.com/saqibshoukat1?tab=overview&from=2025-12-01&to=2025-12-31

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

The USDCx-to-USD conversion and payout integration module built under this grant will be released under the MIT License and made publicly available on GitHub, with the repository opened in Tranche 1. The core Grid Protocol platform (directory, KYB pipeline, booking and payments system) is proprietary to TheGridProtocol LLC and is not part of the open-source release.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

306

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

260

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 2 — concept formulated, not yet built or tested. Defined architecture: a customer-signed USDCx burn redeemed to plain USDC via Circle's xReserve, off-ramped to USD via a licensed provider — Transak Stream primary, MoonPay fallback — surfaced in our dashboard. No integration code exists yet. xReserve resolves USDCx to plain USDC before any off-ramp provider is involved, so the provider needs only USDC support — both Transak and MoonPay have shipped production USDC off-ramp support for years, removing the unconfirmed dependency an earlier draft carried.

These building blocks are each mature, live technologies (xReserve, licensed off-ramp providers, Cardano wallets) — this integrates proven components rather than new on-chain mechanisms, lowering technical risk.
