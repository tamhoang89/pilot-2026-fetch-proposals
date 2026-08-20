# Portoray: Provably Better Stablecoin Swaps on Cardano

> A self-custodial router that reads live pools across six Cardano DEXs, proves its saving against a direct swap before you sign, and settles dollar-token trades in one transaction, at zero added fee.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1u8mk4a3xtgj3k362zqwn4ud60eq336wutvq2p4me0wr6vnq98wv3s`
- **Funding requested:** ₳175,000
- **Last finalized:** 2026-08-20T05:19:51.135000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Eren Topal is a full-stack software developer with hands-on experience building in the blockchain space, including work in the Stellar, Avalanche and other ecosystems. He holds a degree in Computer Systems, Networking, and Telecommunications and remains an active builder in web3. His works on Stellar gave him a working understanding of where users run into friction, and that experience is what led him to build Portoray. He is the sole developer on this proposal and will deliver every part of the project himself.

Recent projects:

- oz-policy-builder (<https://github.com/ErenTopaal/oz-policy-builder>): records a Stellar transaction and derives the minimal OpenZeppelin smart-account policy required to authorize exactly that transaction, producing least-privilege access rules from observed activity.
- Mimir (<https://github.com/ErenTopaal/mimir>): a self-hosted smart contract auditing platform. It accepts Solidity source or a verified contract address and uses an LLM to return vulnerabilities mapped to specific source lines.
- Powdr (<https://github.com/ErenTopaal/powdr>): no-code automation platform for Avalanche that enables on-chain workflows without manual coding.
- Bifrost (<https://github.com/ErenTopaal/bifrost>): automated bug-bounty pipeline that scrapes program scope, retrieves in-scope code, runs analysis agents, and produces verified reports.

GitHub: <https://github.com/ErenTopaal> LinkedIn: <https://www.linkedin.com/in/erentopal/>

---

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: Cardano stablecoin holders rebalancing between Cardano dollar tokens, USDCx and USDM among them; DeFi users converting into the stablecoin a venue or strategy requires; and holders reacting to peg deviations the quote card makes visible. Why through Portoray: switching costs nothing, needs no account, and every quote proves it returns at least as much as the direct swap the user would otherwise make. Cadence: rotation is recurring rather than one-off, and the ongoing migration toward USDCx keeps it live. Targets: 2,000 transactions and 1,000 ADA in network fees over the measurement window: about 330 per epoch, roughly 67 per day, well above the program floor at my requested amount. The fee figure comes from measured settled fees: a two-leg atomic split settles around 0.52 ADA, quoted upper bound near 0.61, single-leg and order routes below that, a conservative blended 0.5 ADA per transaction. Steady daily flow is the plan, which is what the per-epoch floors and daily cap reward, and I aim to deliver M1 early for extra epochs. Team wallets are declared, and my reconciliation report flags transactions with an own-wallet input, so self-traffic is visible and excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

The channels are built into the product rather than bought. Every quote is a shareable link encoding pair, size and slippage, so a good result travels on its own into the Discord and forum threads where Cardano stablecoin users already compare prices. The quote service is a public, keyless HTTP API, so wallets, dashboards and bots can embed routing without an account, and the developer documentation exists for exactly that. The Apache 2.0 repository is the credibility channel for technical users who verify the math before trusting a router. I will pair these with direct presence in the communities of the assets and venues the router serves (USDCx, USDM, the six integrated DEXs), where the saving scale on a live quote is a demonstration rather than a claim. The milestone requires a minimum number of distinct real users; the acquisition argument is that switching costs nothing, needs no signup, and is verifiably never worse than the swap the user would have made anyway.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today users swap on a single venue (typically the deepest pool, which is exactly the baseline Portoray measures itself against), use a general-purpose Cardano aggregator such as DexHunter, or use a venue's own routing, such as Minswap's multi-routing across its own pools. General aggregators optimise across all pairs; a stablecoin pair is a hard sub-case they handle generically. Portoray wins that sub-case by pricing each venue exactly as its validator does: per-venue stableswap amplification conventions, single-range concentrated pools enumerated as sets, per-direction fees, and reserves net of fees accrued inside the pool UTxO. It ranks net of real ADA cost, proves the saving against a named baseline, and takes no cut and no rewards, so the execution result is the whole pitch.

### Please provide details about the Technology Readiness Level selected for your existing product

The product is complete and running. The app at <https://portoray.com> serves live quotes against real mainnet pool state across the six integrated venues, and the quote service, transaction builder and measurement tooling are built and test-covered. The full swap path is validated on the public preprod testnet: an end-to-end suite quotes, builds, signs with a funded key and settles real transactions, and proves both safety properties: a pool that moves between quote and submission rejects the swap rather than filling below the bound, and two transactions racing for one pool settle one and reject the other with funds intact. Mainnet submission is deliberately gated by a built-in guard until the program's metadata label is configured, so the declared footprint starts clean at M1.

### 

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Portoray adds no custodial contract and no validator of its own; the on-chain architecture is composition of the six venues' existing validators inside one transaction the user signs. Direct-spend venues (Danogo CLMM, Splash) settle atomically: the transaction spends the pool UTxO, rewrites the pool datum byte for byte in the CBOR array form it was read in, indexes redeemers against the ledger's sorted input sets, and handles the per-pool stake-withdrawal branch and the validity-window counter the validator derives time from. Order venues (Minswap V2 and Stableswap, SundaeSwap V3 and Stableswaps, WingRiders V2) receive an order output whose inline datum carries the user's minimum, enforced by the venue's validator at settlement. Both paths fail rather than fill worse. Off chain, a TypeScript workspace prices every pool exactly as its validator does: bigint arithmetic only, exact rationals for prices, per-venue stableswap amplification conventions, and reserves net of fees accrued inside pool UTxOs. Pool state is ingested through Ogmios chain-sync and a Kupo index with deterministic rollback handling, with keyless Koios as the secondary path. Every transaction carries a CIP-20 message tag plus the program's label, and the measurement package recomputes settled counts and fee decompositions purely from public data. This fits the Stablecoins area: every routed swap is a genuine stablecoin transaction whose fees anyone can count independently against the declared identifiers.

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

My target market is everyone who holds or moves Cardano dollar tokens: DeFi users entering and exiting positions, traders rotating between stablecoins, and projects managing stablecoin treasuries. The segment is small in absolute terms but growing fast and strategically central to Cardano. DeFiLlama-based reporting puts Cardano's stablecoin market capitalisation above $60M as of July 2026, up from roughly $55M in late May, with Circle's USDCx (launched February 2026) near 59% share alongside USDM, USDA, iUSD and DJED (<https://defillama.com/stablecoins/Cardano>, <https://cardano.org/stablecoins/>). The rapid rise of a new dominant stablecoin is exactly the condition that creates rotation demand: holders move between incumbent tokens and USDCx, and every such move is a stablecoin-to-stablecoin swap.

Evidence for the inefficiency itself is reproducible rather than asserted. Every supported venue's pool state is public on chain, several venues run more than one pool per pair, and the pools disagree on price at real sizes; that disagreement is the product's raw material. Portoray makes the gap measurable on every request: the quote card prints the deepest direct pool's output next to the routed output in the same token, and when routing cannot beat the direct swap the card says so and offers that swap instead. A claim a user can check on every quote is the strongest demand evidence a router can offer.

### Applicant name

Eren Topal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Nobody pays Portoray. There is no take rate, no spread, no token and no rewards mechanic, and the codebase deliberately contains no code path to add one. Users keep the routed saving and pay only venue fees and the Cardano network fee, which is what makes the product credible: the only reason to use it is the measured execution result. What keeps it running is that running it is cheap by design. The service holds no database, no keys and no funds; it reads the chain through its own node stack plus keyless public sources (Koios, DeFiLlama), so operating cost is one mainnet-sized host, which I can sustain beyond the adoption window. Because the code is Apache 2.0 and fully self-hostable, anyone can run the router if I stop, so the integration outlives any single operator. Usage persists because the structural condition it exploits, fragmented multi-curve stablecoin liquidity, persists, and sustained post-window activity is precisely what the program's bonus rewards.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant the router stays a testnet-validated, quote-only tool: mainnet submission is intentionally blocked until the program label exists, and the mainnet-only work is unfunded. The grant buys that remainder plus the adoption phase, about four months of my full-time development: verifying and configuring per-venue mainnet deployments (addresses, script hashes, reference scripts, parameters), each checked against settled transactions; operating the mainnet chain stack (cardano-node, Ogmios, Kupo); recalibrating the cost model against mainnet settled fees; enabling and hardening submission; and running the measurement window with published per-epoch reporting. High-level spend: about 90% my engineering time, 10% mainnet infrastructure for the term. No completed work is funded.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Quote service and web app deployed to production against Cardano mainnet, with transaction submission enabled behind the configured program metadata label.
2. Verified mainnet deployment configuration for the integrated venue set, execution live on both settlement paths: at least one atomic direct-spend venue and two order venues, targeting all six.
3. Settled mainnet transactions for each enabled path, hashes mapped to the quoted flow steps, repeated without failure.
4. Declared on-chain footprint: CIP-20 message tag, program metadata label, team wallets, and per-venue script hashes, policy ids and order addresses.
5. Measurement pipeline live on mainnet: exact-tag reconciliation and per-transaction fee decomposition from keyless public data, publishing daily and per-epoch figures.
6. Release notes, technical walkthrough video, tagged Apache 2.0 repository, test evidence bundle (checklist, bug log, security note), and the Demo Day presentation.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano dollar tokens trade across at least six venues running four different pricing curves: constant product, stableswap, concentrated liquidity and weighted. Liquidity is fragmented, fee schedules differ per venue and per direction, and the same size prices differently everywhere, so anyone swapping on a single venue routinely leaves value on the table. Two further problems bite users directly: several tokens share a ticker (two distinct assets on Cardano both call themselves USDC), and tokens meant to be worth a dollar are measurably off peg at times, yet interfaces commonly quote them at 1:1.

Portoray solves this for anyone moving between Cardano dollar tokens: traders, DeFi users rebalancing positions, and treasuries. It reads live pool state at every supported venue, searches direct, split and multi-hop routes, and ranks them net of the real ADA cost each extra leg adds. The quote card proves the result before signing: the saving against a single swap in the deepest pool holding both tokens, every fee itemised by who charges it, the observed dollar price of both tokens, and the settlement guarantee of every leg. The user signs one transaction in their own wallet, funds pay out to their own address, and the router never returns a route worse than the direct swap. Tokens are identified by policy id and asset name, never by ticker, so the wrong asset cannot be picked by typing the right letters.

### Supporting links (repo, site, demo)

- https://web.portoray.com
- https://portoray.com
- https://docs.portoray.com
- https://github.com/ErenTopaal/portoray

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

The codebase is licensed under Apache 2.0, whose copyright and patent grants are perpetual and irrevocable, so the license holds for the lifetime of the project.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

2000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The integration this grant funds is mainnet execution: dollar-token swaps settling on mainnet under a declared, measurable on-chain footprint. Today it is testnet-complete. Both settlement paths are implemented and demonstrated on preprod: atomic direct pool spends (byte-exact datum rewrites, redeemer indices over the ledger's sorted input sets, the staking branch and validity window) and order placements carrying the user's minimum in the datum. CIP-20 tagging, the program label slot, and the keyless measurement pipeline reading settled activity off public chain data are built and tested. The grant covers the mainnet-only remainder: verified per-venue mainnet deployment configuration, chain-stack operation, cost-model recalibration against mainnet settled fees, and enabling submission.
