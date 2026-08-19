# Hardware-Attested Real-World Oracle for Cardano, via x402

> A working oracle system, brought natively to Cardano: x402 pay-per-call, CIP-0113 compliant tokens, CIP-0170 identity. A port, not a from-zero build.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1uy285ltjnjpumfvxlju8kww2wa633rmdpqy5t26ddf85w3s00k2n4`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-19T16:07:18.922000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Dominick Garey, CTO - owns protocol direction end to end: sensor and pipeline architecture, and the on-chain contract build for this integration. [linkedin.com/in/dominick-garey-878a65117](http://linkedin.com/in/dominick-garey-878a65117), [github.com/dgarey](http://github.com/dgarey). Tyler Malin, CEO - leads business direction and partnerships, including outreach to FiDa, a Catalyst-funded parametric-insurance project already live on Cardano. [linkedin.com/in/tylermalin](http://linkedin.com/in/tylermalin), [github.com/tylermalin](http://github.com/tylermalin). Jeffrey Wise - leads the land and operator side, owning the sensor deployment network. [linkedin.com/in/jeffrey-wise-4036a639](http://linkedin.com/in/jeffrey-wise-4036a639). Org: [github.com/MalamaLabs](http://github.com/MalamaLabs). The team won Catalyst Fund 12 in 2024 to build the original u-dMRV MVP, now running in controlled pilots ahead of what was originally scoped. The Cardano delivery record is public and checkable: a Merkle root has anchored to mainnet every day, without a miss, since 10 July 2026, independently recomputable by anyone at [api.dagwelldev.com/ops](http://api.dagwelldev.com/ops). Dominick already owns the sensor pipeline, identifier scheme, and Merkle-anchor system this proposal ports onto Cardano. CIP-0113 and CIP-0170 are new standards, not new skills. This grant funds full-time, dedicated engineering hours on the build for the three-month window.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary give-back pledge (optional): If Malama Labs closes a priced equity or token financing round of $1,000,000 USD or more within 24 months of grant disbursement, we pledge to repay 100% of the grant's value at time of disbursement, not its future or appreciated value, to the Catalyst treasury within 90 days of that round closing.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Our oracle system already runs on Cardano mainnet: five weeks of unbroken, daily, hardware-signed anchors, independently verifiable at [api.dagwelldev.com/ops](http://api.dagwelldev.com/ops). Malama is a data attestation company, not a weather-data company - CIP-0170 lets any organization create a DID and get its own sensor data validated, not just consume our environmental feed. Oracles/x402 sells the one dataset we have live today (weather) to agents and developers, seeded by a bounty and direct FiDa/insurance outreach from Week 1 - roughly 30 unique wallets, \~1,150 transactions. CIP-0113/CIP-0170's \~25-wallet cohort (76/43 transactions) is independent sensor-site operators attesting their own data through our identity layer, a second, distinct customer type from day one. We're deliberately conservative on all three: without prior external usage data to calibrate against, every target sits near the low end of Credible rather than assumed at Ambitious.

### How will you reach and onboard real users - and what evidence backs your channels?

(1) The x402 gateway itself is the funnel: any AI agent or Cardano dApp starts paying per call with no signup, promoted across Cardano developer channels (forum, Discord, x402 developer directory) from Week 1. (2) A fixed-prize developer bounty for the first three third-party oracle integrations, posted Week 1 (three 2,000 ADA slots), targeting a first claim by Week 6 and all three by Week 10, paid on delivered integration work, not transaction volume. (3) Direct outreach to FiDa, a Catalyst-funded Cardano parametric-insurance project already live with weather-triggered payouts - an active conversation starting Week 1, not yet a signed commitment, giving integrators the full three-month window to be ready to transact at mainnet launch rather than cold. Milestone 1's minimum of three external organizations, each transacting from its own wallet, is what these three channels are built to deliver.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Pyth Pro solves price data on Cardano - nothing solves real-world-event data with a hardware-attested source. Charli3 and similar oracle relays move external feeds, but without the ATECC hardware-signature chain, cross-validation, and Merkle/mainnet-anchor audit trail underneath, independently recomputable rather than just trusted. Off-chain alternatives (a spreadsheet, a centralized weather API, a PDF report) exist for every use case here, but none are on-chain verifiable or smart-contract consumable. Teams switch to us because we're the only source that's hardware-attested, cross-validated, and natively payable per-call via x402 - auditability plus compliance is the product.

### Please provide details about the Technology Readiness Level selected for your existing product

A Merkle root has been anchored to Cardano mainnet once a day, every day, since 10 July 2026 - five weeks straight, no missed day. Each anchor carries the raw-readings root and the daily model-accuracy scorecard root from a hardware-signed sensor network (ATECC secure-element signatures), cross-validated against independent weather APIs. Recent days: 9,000+ signed leaves, 100% hardware-signature coverage on physical readings. Every root is independently recomputable from public reads alone, no admin token required, at [api.dagwelldev.com/ops](http://api.dagwelldev.com/ops). This is the same u-dMRV infrastructure built and proved out under Catalyst Fund 12, now anchoring to Cardano specifically.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Oracles + x402: a new on-chain contract publishes Malama's live, hardware-signed environmental readings in the same pattern Pyth Pro already proved on Cardano - a signed update a consuming contract includes in its own transaction, paying its own fee. An x402 gateway sits in front of the same data for off-chain/agent consumers: HTTP 402 challenge, signed payment, ADA settlement, data delivery - every paid call is a real, countable transaction regardless of size. Raw readings live on Arweave; Cardano carries only the compact daily Merkle roots, keeping on-chain cost low. A reference consumer contract and SDK ship alongside both paths. CIP-0113: one token policy, two use cases - a site-rights instrument (a verified sensor site's data rights) and a data-credit instrument (a prepaid unit metering x402 access). Compliance rule: only CIP-0170-attested wallets may mint, hold, or transfer either token. Built on the closest existing reference substandard rather than a new one. CIP-0170: KERI-backed attestations anchored on mainnet for verified sensor operators and verified token counterparties, anchored by the party being verified, not by us, so fees count as genuine usage. This is the standards-compliant, KERI-backed form of the attributable, signed-claim pattern our product already runs on, and the piece that makes the CIP-0113 compliance rule check something real.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Programmable tokens (CIP-0113)
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

Yes

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Real-world-event data consumers on Cardano: parametric-insurance products needing a weather trigger to settle payouts, prediction/event-settlement contracts needing a real-world outcome, and RWA/agricultural products needing field-condition verification. This category exists today: FiDa, a Catalyst-funded parametric-insurance project, is already building weather-triggered payouts on Cardano via Charli3/WolframBlockchainLabs oracle data. A second, larger market: AI agents and dApps paying per API call via x402, live on Cardano since October 2025, with the Cardano Foundation now a formal member of the x402 Foundation alongside Google, Visa, and AWS - a real, growing category of machine-to-machine payment volume our oracle plugs directly into. Evidence of our own reach: our hardware-signed sensor network (2 physical field nodes plus 6 cross-validated third-party weather-API streams) has anchored to Cardano mainnet daily, unbroken, for 5+ weeks, generating 9,000+ verifiable readings per day. That's production-scale data, ready to be consumed the moment the oracle contract ships. We proved out and funded the dMRV pipeline underneath once already, in Catalyst Fund 12.

### Applicant name

	Mālama Labs, Inc.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Consumers pay their own transaction fees, via direct oracle-contract consumption (Pyth pattern) or x402 pay-per-call, to read our live data; we never subsidize usage. Our sensor and attestation network is core infrastructure, already operating and already commercialized elsewhere (proved out under Catalyst Fund 12); it doesn't depend on this grant to keep running. x402 turns the API into a standing, no-subscription revenue channel - every metered call is real income independent of the measurement window. CIP-0113 token holders (site-rights, data-credits) pay their own mint/transfer fees. Because the revenue model has zero marginal cost to us beyond what's already running, usage has no reason to drop once the kicker period starts - exactly the sustained-pace signal this program rewards with a larger bonus share.

### Programmable tokens (CIP-0113) - expected transaction count

290

### On-chain identity (CIP-0170) - expected transaction count

43

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Build tranche (48,000 ADA, guaranteed on milestone delivery) breaks down: 40,000 ADA in-house engineering (Dominick, full-time across all three integrations - oracle contract, x402 gateway, CIP-0113 policy, CIP-0170 attestation flow); 6,000 ADA across three fixed-prize bounties (2,000 ADA each), paid only on delivered third-party oracle integrations; 2,000 ADA for testnet/mainnet deployment costs, KERI tooling integration, and an external security review. Adoption (up to 48,000 ADA) and Kicker (24,000 ADA) aren't spent up front - they're earned directly against the 2,450 transactions and 1,360 ADA in fees targeted across all three integrations, per the blended formula.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Oracle contract live on Cardano mainnet, publishing our declared feed in a third-party-consumable pattern, evidenced by a transaction from a wallet that isn't ours. x402 gateway live, with at least one real paid call. CIP-0113 token policy live, with compliance enforced against CIP-0170 attestations, evidenced by an external mint or transfer. CIP-0170 attestation issuance live, with at least one attestation anchored by a wallet that isn't ours. Reference consumer contract and SDK published. Documentation covering hexes, data types, token mechanics, and the identity flow. Declared footprint published per integration: script hashes, policy IDs, registered tag, our own wallets. At least three external organizations onboarded across the three integrations combined. Demo Day walkthrough covering all three. Funded by the 48,000 ADA Build tranche: 40,000 ADA engineering (all three integrations), 6,000 ADA bounty (delivered integrations only), 2,000 ADA deployment/tooling/security.

### Oracles - expected transaction count

1150

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

160

### On-chain identity (CIP-0170) - fee target (ADA)

130

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano has a live oracle for prices (Pyth Pro, mainnet since May 2026) but none for real-world physical events: weather, environmental conditions, or field-verified data a contract needs to settle a payout, price an RWA policy, or resolve a prediction market. Nothing on Cardano today can check what happened at a location, tokenize the rights that data generates under compliant rules, or verify who's transacting.

Malama already operates the hardware side of this gap - the same u-dMRV infrastructure proved out under Catalyst Fund 12, now applied to Cardano. Hardware-signed sensors (ATECC secure-element), H3-indexed, cross-validated against independent weather APIs. Raw readings live on Arweave; a Merkle root anchors daily to Cardano mainnet, unbroken since 10 July 2026, independently recomputable, no admin token required. Recent days: 9,000+ signed leaves, 100% hardware-signature coverage.

Three connected moves, not a from-scratch build: (1) wire the existing attestation system for third-party consumption, a new Aiken contract in the pattern Pyth already proved on Cardano. (2) Put x402 in front as the pay-per-call gate, live on Cardano since Oct 2025, with the Cardano Foundation now a formal x402 Foundation member; every metered read becomes a real, countable transaction. (3) Convert the token and identity concepts into Cardano's own standards, CIP-0113 and CIP-0170, native and compliance-aware rather than generic wrappers.

### Supporting links (repo, site, demo)

- https://www.malamalabs.com/
- https://launch.malamalabs.com/
- https://api.dagwelldev.com/ops
- https://dagwelldev.com/experiments

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

400

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

### Funder, status, and what it covers

Project Catalyst - Fund 12 (2024). Status: completed, successfully, in full. Funder covered: the original u-dMRV MVP, focused on on-chain carbon credits (Distributed Hawaii Carbon Credits on Cardano) - the sensor-and-attestation infrastructure this proposal builds on. What this grant covers instead: data attestation for that same information, moved beyond carbon-credit tokenization specifically - a new oracle contract, x402 gateway, and CIP-0113/CIP-0170 conversion. New, additional work, not a continuation of Fund 12's deliverables.

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

All three are designed but not built. Oracles + x402: the contract and gateway reuse patterns already proven on Cardano (Pyth Pro's consumption pattern, x402 live since October 2025) - what's new is wiring our feed into them. CIP-0113: a token policy is designed (site-rights and data-credit instruments, gated by CIP-0170), but CIP-0113 itself is an open, unmerged CIP PR with a testnet-only reference implementation, so this starts near zero on a standard that's still moving. CIP-0170: KERI-backed attestation issuance is designed but not built; our existing did:malama identifiers aren't yet CIP-0170-compliant, which specifically requires KERI attestations via signify-ts. No code exists for any of the three yet - Month 1 is design and testnet deployment across all.
