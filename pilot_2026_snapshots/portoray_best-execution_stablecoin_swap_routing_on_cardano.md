# Portoray: Best-Execution Stablecoin Swap Routing on Cardano

> A non-custodial router that swaps Cardano dollar tokens across six DEX venues and four curve types, proves the saving against the deepest pool on every quote, and never returns a worse route.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 7
- **Proposer:** `stake1u8mk4a3xtgj3k362zqwn4ud60eq336wutvq2p4me0wr6vnq98wv3s`
- **Funding requested:** ₳175,000
- **Last finalized:** 2026-08-24T11:27:33.831000+00:00

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

Who transacts: Cardano stablecoin holders rebalancing between the six dollar-pegged assets the router serves, USDCx and USDM foremost; DeFi users converting into the token a venue or strategy requires; holders reacting to peg deviations the quote card surfaces. Why through Portoray: no account, no extra fee, and every quote proves the route returns at least as much as the direct swap. Cadence: rotation recurs, and the migration toward USDCx keeps it live. Targets: 2,000 transactions, 1,000 ADA in counted fees. Fees from measured settled swaps: 0.43 ADA at one leg, 0.52 at two, order placements below; a blended 0.5 ADA gives 2,000 x 0.5 = 1,000. Baselines: about 3x my roughly 337 ADA program floor at this request, and about 0.44% of the Standard's 225,000 ADA trailing-30-day network fee denominator. Wallet model: clear the 34-external-wallet minimum in week two, grow to 60-80 active external wallets by mid-window; at about one routed swap per wallet per day that covers the late-epoch pace of 67 per day (33 early), within the 20% daily cap. I aim to deliver M1 early for a longer window, and my reconciliation flags and excludes own-wallet inputs, so self-traffic never counts.

### How will you reach and onboard real users - and what evidence backs your channels?

The channels are built into the product. First, every quote is a shareable link encoding pair, size and slippage, so a good result travels into the threads where Cardano stablecoin users compare prices. Second, the quote service is a keyless public HTTP API, so wallets, dashboards and bots embed routing without an account; I will pitch the interfaces already listing the six dollar-pegged assets. Third, direct presence in the USDCx, USDM and venue communities, where a live quote demonstrates the saving. Fourth, the Apache 2.0 repository. Fifth, Demo Day, the program dashboard and the Cardano leaderboard from M1. Volume anchors: over $60M of Cardano stablecoins sits behind these channels; my target needs about 0.44% of network fees. First two weeks after delivery: day 0, footprint, dashboard and walkthrough published; week 1, 20 distinct external wallets, 150 counted swaps; week 2, 40 wallets and 400 swaps cumulative, a 35-per-day run rate above the 33-per-day early floor pace.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today users swap on a single venue (typically the deepest pool, which is exactly the baseline Portoray measures itself against), use a general-purpose Cardano aggregator such as DexHunter, or use a venue's own routing, such as Minswap's multi-routing across its own pools. General aggregators optimise across all pairs; a stablecoin pair is a hard sub-case they handle generically. Portoray wins that sub-case by pricing each venue exactly as its validator does: per-venue stableswap amplification conventions, single-range concentrated pools filled as sets, per-direction fees, and reserves net of fees accrued inside the pool UTxO. It ranks net of real ADA cost, proves the saving against a named baseline, and takes no cut and no rewards, so the execution result is the whole pitch.

### Please provide details about the Technology Readiness Level selected for your existing product

The product is complete and live in the operational environment. The app at <https://portoray.com> serves quotes against real mainnet pool state across the six read venues, and execution is live on four today: atomic direct-spend on Danogo CLMM, orders on SundaeSwap (both products), Minswap V2 and WingRiders V2 (both families). Real mainnet transactions have settled and are replayed in the test suite: the concentrated-liquidity math reproduces settled mainnet swap legs to the unit, order datums re-encode byte-exact against live orders, and the cost model is checked against settled fees. The full quote-build-sign-settle path, with both pool-contention outcomes, settles real transactions on preprod end to end. I place it at TRL 7, not 8, as it has had no external security review.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Portoray adds no custodial contract and no validator of its own; the on-chain architecture is composition of the six venues' existing validators inside one transaction the user signs. Direct-spend venues (Danogo CLMM, with Splash in scope) settle atomically: the transaction spends the pool UTxO, rewrites the pool datum byte for byte in the form it was read, indexes redeemers against the ledger's sorted input set, and handles the stake-withdrawal branch and validity window. Order venues (SundaeSwap both products, Minswap V2, WingRiders V2 both families, with Minswap Stableswap in scope) receive an order output whose inline datum carries the user's minimum, enforced by the venue's validator at settlement. Both paths fail rather than fill worse. Off chain, a TypeScript workspace prices every pool exactly as its validator does: bigint arithmetic only, exact rationals, per-venue amplification conventions, per-direction fees, and reserves net of accrued pool fees. Pool state is ingested through my own chain stack (cardano-node, Ogmios, Kupo), with keyless Koios secondary. The service holds no keys and no funds and returns unsigned transactions under four structural assertions. Every transaction carries a CIP-20 message tag plus the program label, and the measurement package recomputes counts and fees purely from public data. This fits the Stablecoins area: every routed swap moves verified stablecoin policies, and its fee is independently countable against the declared identifiers.

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

Evidence for the inefficiency itself is reproducible rather than asserted. Every venue's pool state is public on chain, several venues run more than one pool per pair, and the pools disagree on price at real sizes; that disagreement is the product's raw material. Portoray makes the gap measurable on every request: the quote card prints the deepest direct pool's output next to the routed output in the same token, and when routing cannot beat the direct swap the card says so and offers that swap instead. A claim a user can check on every quote, against live mainnet pool state today, is the strongest demand evidence a router can offer.

### Applicant name

Eren Topal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Nobody pays Portoray. There is no take rate, no spread, no token and no rewards mechanic, and the codebase deliberately contains no code path to add one. Users keep the routed saving and pay only venue fees and the Cardano network fee, which is what makes the product credible: the only reason to use it is the measured execution result. What keeps it running is that running it is cheap by design. The service holds no database, no keys and no funds; it reads the chain through its own node stack plus keyless public sources (Koios, DeFiLlama), so operating cost is one mainnet-sized host, which I can sustain beyond the adoption window. Because the code is Apache 2.0 and fully self-hostable, anyone can run the router if I stop, so the integration outlives any single operator. Usage persists because the structural condition it exploits, fragmented multi-curve stablecoin liquidity, persists, and sustained post-window activity is precisely what the program's kicker and bonus reward.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The router is live on mainnet today as a four-venue service run part-time and unfunded; without the grant it stays that. The grant converts it into the program's measurable stablecoin integration and buys about four months of my full-time work: enabling the two remaining venues (Splash direct-spend, a Minswap Stableswap adapter and order path); integrating the program's metadata label and a newly registered message tag so the declared footprint starts clean at M1; productionising the keyless measurement pipeline into public daily and per-epoch reporting; operating and hardening the mainnet chain stack (cardano-node, Ogmios, Kupo) for the term; and running the adoption window. High-level spend: about 90% my engineering time, 10% mainnet infrastructure. No completed work is funded.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Production deployment on mainnet under a newly declared program footprint: registered message tag, the program's metadata label, and team wallets, with submission enabled under that footprint from delivery.
- Execution live on at least five of the six read venues, targeting all six, on both settlement paths: direct-spend (Danogo CLMM, adding Splash) and orders (SundaeSwap V3 and Stableswaps, Minswap V2, WingRiders V2 both families, adding Minswap Stableswap).
- Settled mainnet transactions for each enabled path under the footprint, hashes mapped to the quoted flow steps, repeated without failure.
- Measurement pipeline live: keyless reconciliation of tagged activity against declared identifiers in both directions, per-transaction fee decomposition, publishing daily and per-epoch figures from delivery.
- Release notes, technical walkthrough video, tagged Apache 2.0 repository, test evidence bundle (checklist, bug log, security note), and the Demo Day presentation.

### How far along is the integration you're proposing, today?

TRL 7 - System prototype demonstrated in operational environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano dollar tokens trade across six venues running four different pricing curves: constant product, stableswap, concentrated liquidity and weighted. Liquidity is fragmented, fee schedules differ per venue and per direction, and the same size prices differently everywhere, so anyone swapping on a single venue routinely leaves value on the table. Two further problems bite users directly: tokens share tickers (two distinct mainnet assets carry a USDC-shaped ticker, at different policy ids and different decimals), and tokens meant to be worth a dollar are measurably off peg at times, yet interfaces commonly quote them at 1:1.

Portoray solves this for anyone moving between Cardano dollar tokens: traders, DeFi users rebalancing positions, and treasuries. It reads live pool state at every venue, searches direct, split and multi-hop routes, and ranks them net of the real ADA cost each extra leg adds. The quote card proves the result before signing: the saving against a single swap in the deepest pool holding both tokens, every fee itemised by who charges it, the observed dollar price of both tokens, and the settlement guarantee of every leg. The user signs one transaction in their own wallet, funds pay out to their own address, and the router never returns a route worse than the direct swap. Tokens are identified by policy id and asset name, never by ticker, so the wrong asset cannot be picked by typing the right letters.

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

The integration this grant funds is the complete, program-measurable stablecoin integration: all six venues execution-live on mainnet under a declared footprint with public reporting. Its core already runs in the operational environment, which is why I select TRL 7: four venues execute on mainnet today across both settlement paths, with settled transactions verified against the chain. The grant covers the remainder: Splash direct-spend execution (its adapter reads mainnet pools now, quote-only), a Minswap Stableswap adapter and order path, the program's metadata label plus a newly registered message tag so the declared footprint contains nothing that carried traffic before the grant (Standard 4.1), public daily and per-epoch reporting, and the adoption climb toward TRL 8-9.
