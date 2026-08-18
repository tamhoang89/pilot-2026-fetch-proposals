# Hardware-Attested Real-World Oracle for Cardano, via x402

> A working oracle system, brought natively to Cardano: x402 pay-per-call, CIP-0113 compliant tokens, CIP-0170 identity. A port, not a from-zero build.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1uy285ltjnjpumfvxlju8kww2wa633rmdpqy5t26ddf85w3s00k2n4`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-18T20:41:50.349000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Malama Labs is three co-founders, not a hired team.

Dominick Garey, CTO - owns protocol direction end to end: sensor and pipeline architecture, and the on-chain contract build for this integration. [linkedin.com/in/dominick-garey-878a65117](http://linkedin.com/in/dominick-garey-878a65117), [github.com/dgarey](http://github.com/dgarey)

Tyler Malin, CEO - leads business direction and partnerships, including outreach to FiDa, a Catalyst-funded parametric-insurance project already live on Cardano. [linkedin.com/in/tylermalin](http://linkedin.com/in/tylermalin), [github.com/tylermalin](http://github.com/tylermalin)

Jeffrey Wise - leads the land and operator side, owning the sensor deployment network. [linkedin.com/in/jeffrey-wise-4036a639](http://linkedin.com/in/jeffrey-wise-4036a639)

Org: [github.com/MalamaLabs](http://github.com/MalamaLabs)

Track record: the team won Catalyst Fund 12 in 2024 to build the original u-dMRV MVP, now running in controlled pilots ahead of what was originally scoped. The Cardano delivery record is public and checkable: a Merkle root has anchored to mainnet every day, without a miss, since 10 July 2026, independently recomputable by anyone at [api.dagwelldev.com/ops](http://api.dagwelldev.com/ops).

Skill gap: CIP-0113 and CIP-0170 are both new standards for the team. If Month 1 testnet work shows either behind pace, a short-term on-chain contract specialist is already budgeted, keeping Dominick focused on the oracle and x402 path.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Malama Labs closes a priced equity or token financing round of $1,000,000 USD or more within 24 months of grant disbursement, we pledge to repay 100% of the grant's value at time of disbursement, not its future or appreciated value, to the Catalyst treasury within 90 days of that round closing.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Three different user types transact, for three different reasons. Oracles: agents and developers pay per call through the x402 gateway for verified environmental data, priced at the low end of Ambitious because our five-week, unbroken mainnet anchor cadence already proves we can sustain that volume — expect near-daily calls once the gateway is live, seeded by a fixed-prize bounty (not a per-transaction reward) for the first three external integrations, then direct outreach to FiDa and other Cardano-native parametric-insurance and event-settlement projects from Month 2. CIP-0113: independent sensor-site operators mint or transfer site-rights tokens as new sites onboard, roughly weekly. CIP-0170: attestations issue alongside each new site or operator onboarding, a similar weekly cadence. Both sit mid-Credible, deliberately conservative given both standards are still pre-production. All targets assume genuinely independent, unfunded wallets under the Standard's own-wallet exclusion — our existing anchor activity doesn't count toward them, and we're not presenting it as if it does.

### How will you reach and onboard real users - and what evidence backs your channels?

Three named channels, not a generic plan. (1) The x402 gateway itself is the funnel: any AI agent or Cardano dApp starts paying per call with no signup, live infrastructure Malama is plugging into, not building. (2) A fixed-prize developer bounty for the first three third-party oracle integrations, paid on delivered integration work, not transaction volume, compliant with the Standard's anti-gaming rules. (3) Direct outreach to FiDa, a Catalyst-funded Cardano parametric-insurance project already live with weather-triggered payouts, a concrete, warm conversation starting Month 2, timed so integrators are ready to transact at mainnet launch rather than cold. Milestone 1's minimum of three external organizations, each transacting from its own wallet, is targeted directly by these three channels combined, not assumed.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Pyth Pro solves price data on Cardano - nothing solves real-world-event data with a hardware-attested source. Charli3 and similar oracle relays move external feeds, but without the ATECC hardware-signature chain, cross-validation, and Merkle/mainnet-anchor audit trail underneath, independently recomputable rather than just trusted. Off-chain alternatives (a spreadsheet, a centralized weather API, a PDF report) exist for every use case here, but none are on-chain verifiable or smart-contract consumable. Users switch because this is the only source that's hardware-attested, cross-validated, and natively payable per-call via x402 - auditability plus compliance is the actual product, not a claim about one.

### Please provide details about the Technology Readiness Level selected for your existing product

A Merkle root has been anchored to Cardano mainnet once a day, every day, since 10 July 2026 - five weeks straight, no missed day. Each anchor carries the raw-readings root and the daily model-accuracy scorecard root from a hardware-signed sensor network (ATECC secure-element signatures), cross-validated against independent weather APIs. Recent days: 9,000+ signed leaves, 100% hardware-signature coverage on physical readings. Every root is independently recomputable from public reads alone, no admin token required, at [api.dagwelldev.com/ops](http://api.dagwelldev.com/ops). This is the same u-dMRV infrastructure built and proved out under Catalyst Fund 12, now anchoring to Cardano specifically.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

A new on-chain contract publishes Malama's live, hardware-signed environmental readings in the same consumption pattern Pyth Pro already proved on Cardano: a signed data update that a consuming contract includes in its own transaction, paying its own fee. An x402 gateway sits in front of the same data for off-chain and agent consumers: an HTTP 402 challenge, a signed payment, ADA settlement on Cardano, then data delivery. Every paid call is a real, countable network-fee transaction, whatever the size of the underlying payment. Raw reading payloads are stored on Arweave, permanent and content-addressed; Cardano carries only the compact daily Merkle roots and the oracle consumption pattern, keeping on-chain cost low while the underlying data stays permanently retrievable and independently verifiable. A minimal reference consumer contract and an open-source SDK ship alongside both paths, so a third-party Cardano developer can integrate without reverse-engineering our internal data model. This is the right fit because it reuses a pattern the ecosystem has already validated (Pyth) rather than inventing a new consumption model, and it puts the hardware-attestation chain we already run into a form another Cardano application can actually read and pay to consume.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Programmable tokens (CIP-0113)
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Real-world-event data consumers on Cardano: parametric-insurance products needing a weather trigger to settle payouts, prediction/event-settlement contracts needing a real-world outcome, and RWA/agricultural products needing field-condition verification. This category exists today, not hypothetically: FiDa, a Catalyst-funded parametric-insurance project, is already building weather-triggered payouts on Cardano via Charli3/WolframBlockchainLabs oracle data. A second, larger market: AI agents and dApps paying per API call via x402, live on Cardano since October 2025, with the Cardano Foundation now a formal member of the x402 Foundation alongside Google, Visa, and AWS - a real, growing category of machine-to-machine payment volume Malama's oracle plugs directly into.

Evidence of Malama's own reach: a hardware-signed sensor network (2 physical field nodes plus 6 cross-validated third-party weather-API streams) has anchored to Cardano mainnet daily, unbroken, for 5+ weeks, generating 9,000+ verifiable readings per day. That's production-scale data, ready to be consumed the moment the oracle contract ships. The dMRV pipeline underneath was proved out and funded once already, in Catalyst Fund 12.

### Applicant name

	Mālama Labs, Inc.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Consumers pay their own transaction fees, via direct oracle-contract consumption (Pyth pattern) or x402 pay-per-call, to read Malama's live data; Malama never subsidizes usage. The underlying sensor/attestation network is core infrastructure, already operating and already commercialized elsewhere (proved out under Catalyst Fund 12); it doesn't depend on this grant to keep running. x402 turns the API into a standing, no-subscription revenue channel - every metered call is real income independent of the measurement window. CIP-0113 token holders (site-rights, data-credits) pay their own mint/transfer fees. Because the revenue model has zero marginal cost to Malama beyond what's already running, usage has no reason to drop once the kicker period starts - exactly the sustained-pace signal this program rewards with a larger bonus share.

### Programmable tokens (CIP-0113) - expected transaction count

860

### On-chain identity (CIP-0170) - expected transaction count

620

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant, our attestation layer stays an internal integrity tool: real and verifiable, but not something another Cardano application can read, pay to consume, or hold a compliant claim against. This grant builds the three pieces that change that: the on-chain oracle contract and x402 gateway, the CIP-0113 token policy and its compliance wiring, and the CIP-0170 attestation flow. Spend: engineering time on the oracle contract, gateway, and token/identity build (most of the build budget); documentation and a reference consumer so third parties can integrate without reverse-engineering our data model; a fixed-prize bounty paid only on delivered integrations; and a budgeted contractor contingency for CIP-0113/CIP-0170 if Month 1 testnet work runs behind pace.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Month 1 - Oracle contract + x402 gateway to testnet (priority path). CIP-0113/CIP-0170 design and testnet spikes in parallel. Benchmark real per-transaction fees. Go/no-go checkpoint on CIP-0113/0170 scope at month end.\
\
Month 2 - Reference oracle consumer + docs + bounty live. If CIP-0113/0170 stayed in scope: compliance-rule wiring to testnet. Direct outreach to FiDa and other named conversations begins.\
\
Month 3 - Mainnet deployment of everything still in scope. Footprint declaration per integration. Milestone 1 demo.

### Oracles - expected transaction count

2290

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

380

### On-chain identity (CIP-0170) - fee target (ADA)

180

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

800

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

All three are designed but not built. Oracles + x402: the contract and gateway reuse patterns already proven on Cardano (Pyth Pro's consumption pattern, x402 live since October 2025) - what's new is wiring our feed into them. CIP-0113: a token policy is designed (site-rights and data-credit instruments, gated by CIP-0170), but CIP-0113 itself is an open, unmerged CIP PR with a testnet-only reference implementation, so this starts near zero on a standard that's still moving. CIP-0170: KERI-backed attestation issuance is designed but not built; our existing did:malama identifiers aren't yet CIP-0170-compliant, which specifically requires KERI attestations via signify-ts. No code exists for any of the three yet - Month 1 is design and testnet deployment across all.
