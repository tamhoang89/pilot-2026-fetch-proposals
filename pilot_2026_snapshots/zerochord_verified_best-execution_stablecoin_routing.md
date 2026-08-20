# Zerochord: verified best-execution stablecoin routing

> A non-custodial router for Cardano's five verified stablecoins: the best price across five venues, the quoted minimum enforced on chain, Pyth price-integrity checks, and a saving anyone can audit.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1ux7wcc580qm4aypf5aqy2v5vaujrv2pywt8xmr9wujfytfc25e2fz`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T05:00:46.099000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Salih Toruner is Zerochord's solo developer. An infrastructure engineer who builds across blockchain ecosystems, with a degree in Electrical and Electronics Engineering, he is a three-time ecosystem grantee (SCF #44, SCF #29, Arbitrum) and a Senior Linux System Administrator at one of Turkey's national banks.

Selected projects:

- [Account Demolisher](https://demolisher.app/): cleanly closes Stellar accounts: unwinds classic entries and Soroban DeFi positions, converts balances to XLM and merges to a destination wallet or exchange, all signing client-side. Stellar Community Fund (SCF #44, RFP track).
- [Stellar Command Insights](https://github.com/bytemaster333/Soroban-ELK): developer-analytics platform for Stellar/Soroban, a CLI/RPC log pipeline on the ELK stack with real-time dashboard, Telegram/Slack alerts and one-line installers. Stellar Community Fund (SCF #29).
- [Hashirama](https://github.com/bytemaster333/Hashirama): production-grade Kubernetes operator that deploys and manages Starknet Madara L3 appchains from a single YAML, with a built-in UI dashboard.
- [StylusVerify](https://github.com/bytemaster333/StylusVerify): deterministic source-verification tooling for Arbitrum Stylus (Rust/WASM) contracts, proving on-chain WASM bytecode matches its GitHub source.
- [SentinelBag](https://github.com/bytemaster333/SentinelBag): on-chain integrity engine for Solana tokens, sybil attacks and inorganic volume, using "Proof of Ecosystem" heuristics and unique-sender analysis.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Zerochord introduces any protocol or routing fee after this project completes, I pledge 10% of that fee revenue to the Cardano treasury for its first 12 months, accounted against the published on-chain footprint so the amounts are independently checkable.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: mainnet holders rotating between the five verified stablecoins. The highest-cadence segment is peg-alignment traders, whose repeat flow exists because prices for one pair drift apart across five venues. Why: every trade carries an on-chain floor and an auditable saving, and the honest direct-route comparison means using Zerochord never costs more than the obvious trade. Cadence: many small and mid-size swaps rather than a few large ones, which matches the per-epoch floors and the daily cap.

The targets are evidence-based. The audited preprod two-hop swap paid 601,501 lovelace in network fees, so 0.5 to 0.6 ADA per routed swap is measured, not assumed. 1,800 stablecoin transactions over the window is about 60 a day, reachable with a few dozen active external wallets yet ambitious for a newly launched solo-built product. Oracle transactions are the Kernel-class subset carrying the Pyth withdrawal, budgeted at half of activity with a higher per-transaction fee from the added script execution. Own-wallet activity is declared and excluded from every count.

### How will you reach and onboard real users - and what evidence backs your channels?

My channels are specific, and I claim no partnerships or letters of intent I do not have.

First, the receipt is the channel. Every swap produces an explorer-linked receipt showing the enforced minimum and the realised saving, and a public audit command lets a sceptic recompute the claim from chain data alone. DeFi users trust chain data over advertising, and a verifiable saving is the artefact they share.

Second, the traders already active on the five routed venues: Zerochord's tagged transactions appear beside theirs in the same explorers, and launch is announced where Cardano DeFi users and developers already gather, with the audit and a public analytics dashboard on Dune as proof.

No paid acquisition exists or is planned: the budget is development-only, and nothing in the product pays anyone to transact. To meet the distinct-wallet minimum, mainnet goes live ahead of Demo Day, so real external users are swapping before the measurement window opens.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The default alternative is each venue's own interface: Minswap, SundaeSwap and Dano Finance, including the two dedicated stableswap products. Minswap also runs an aggregator, which Zerochord deliberately uses as an independent cross-check of its arithmetic, so the competition is real and measured. Off chain, users can route through a centralised exchange.

Zerochord wins on four things no single venue offers together: one quote comparing all five venues and three curve types, a minimum enforced on chain for every route class, an oracle guard that refuses quotes from mispriced pools, and honesty as a feature: when a direct pool beats routing, the product says so and offers that pool. A venue cannot copy that last property, and it is what makes every published saving credible.

### 

### Please provide details about the Technology Readiness Level selected for your existing product

The complete product runs on the Cardano preprod testnet: web app and CLI quote, build, sign and submit. Swaps of three shapes, each settling inside the user's own transaction (single pool, split across two pools, two hops through ADA), landed on chain and were reconstructed by the public audit; orders were placed, one filled by the venue's batcher, one cancelled; the settlement validator is deployed on preprod (tx 8e066c7d…, hash 12edd011…), its claim and refund paths exercised, each beside a refused adversarial twin: a claim one base unit short, a refund one slot early, a double-satisfaction attempt.

A dated reading (2026-08-20, block 5,076,337) shows 15 measured product transactions and 6 reconstructed swaps, and the interface passes a read-only end-to-end test against mainnet.

### 

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Zerochord is five TypeScript libraries, a web app, a CLI, and an on-chain project in Aiken, Cardano's smart-contract language; every network-specific value lives in one validated configuration file. Venue adapters reduce five venues and three curve types to one interface with an execution class: Kernel venues are spent directly in the user's own transaction; Commitment venues take an order a permissioned batcher fills later, with a cancel path. The quote engine enumerates paths exhaustively, collapses each to an exact effective pool, solves the split, then requotes the winner in each venue's own integer arithmetic, so the on-chain minimum matches what venue validators check; a final floor keeps the route at least as good as the best single path considered.

Stablecoins need exactly this: cross-curve routing with binding minima over fragmented pegged liquidity, and the settlement validator (Plutus V3, 1,384 bytes, one-script-input rule against double satisfaction) extends the all-or-refund guarantee to mixed-class routes. The oracle side follows Pyth's own Cardano design: signatures checked against trusted signers read from Pyth's on-chain state, freshness (120 s) and a 200-basis-point deviation guard enforced by the consumer as Pyth specifies, and a zero-lovelace withdrawal through Pyth's published script proving the price inside the transaction. CIP-20 transaction messages and the footprint, measure, audit and integrity commands make every claim checkable from public data.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins
- Oracles

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The target market is holders of Cardano's dollar-pegged stablecoins who need to move between them: individual traders, arbitrageurs who keep the pegs aligned across venues, and organisations spreading treasury risk across issuers. The arbitrage segment matters most for adoption because its flow is repetitive by nature: it exists precisely because prices for the same pair drift apart across five venues, which is the same spread Zerochord measures on every quote.

I will not quote a market-size figure I cannot source. The evidence I can point to is structural and verifiable on chain. Five stablecoins carry signed Cardano Token Registry entries, meaning five issuers maintain live products on mainnet. Two of the largest venues, Minswap and SundaeSwap, each operate a dedicated stableswap product alongside their general pools; purpose-built stable-pair infrastructure only exists where those pairs actually trade. The same pairs also sit in constant-product and concentrated-liquidity pools, and that spread of one pair across incompatible pool designs is the fragmentation this proposal addresses.

Demand for this exact product is what the adoption window tests; user-count evidence cannot exist before a mainnet launch. What does exist is a complete product exercised end to end on the preprod testnet with real on-chain transactions, and mainnet pools that already answer this router's read-only quotes today.

### 

### Applicant name

Salih Toruner

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Zerochord charges no fee of its own. Users pay only venue fees and the Cardano network fee from their own wallet, and the network fees the program measures are generated by that ordinary usage; an included integrity scanner proves in code that nothing pays, rewards or rebates anyone to transact, so measured demand is real demand.

Sustainability is engineered on the cost side. The web application is a static build quoting through a credential-free public chain provider, so operating cost is close to zero: hosting, one small rate-limit proxy, and monitoring, all within a solo maintainer's reach. Usage persists after the grant because the value is durable: a binding floor and a checkable saving are worth more than any single venue's quote. Continuity does not depend on me: the code is Apache-2.0 open source and any operator can run a deployment from one configuration file. If a routing fee is ever introduced later, the section 9 pledge applies.

### 

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding takes Zerochord from a validated testnet system to mainnet; none of it funds completed work. It covers: hardening and deploying the settlement validator and publishing its footprint; wiring the Pyth guards into the serving path and attaching the on-chain price proof to Kernel swaps, with budget tests for the combined transaction; verifying every mainnet venue reference against live pools; launching [zerochord.com](http://zerochord.com) on mainnet behind a rate-limit proxy; public measurement and the Demo Day evidence bundle; then operating the adoption window. The 200,000 ADA splits into 168,000 development labour (16 weeks, one developer, both phases), 24,000 infrastructure (hosting, provider, proxy, monitoring, CI), and 8,000 for on-chain deployment and verification.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Settlement validator deployed on Cardano mainnet as a reference script; footprint published and checking clean; claim and refund demonstrated on mainnet.
2. Zerochord serving mainnet: connect a CIP-30 browser wallet, quote, sign once, submit, for the five verified stablecoins across all five venues; receipts read the net received amount from the chain; pending-order tracking with on-chain cancel.
3. Oracle enforcement live: every served mainnet quote passes the Pyth freshness and deviation guards; Kernel-class swaps carry the zero-lovelace Pyth withdrawal proving the price on chain.
4. Verified mainnet transactions by real external users for each declared integration flow, with hashes mapped to flow steps.
5. Public measurement: audit and measure reproducible by anyone; a mainnet Dune dashboard over the registered tag; daily chart live from delivery.
6. Release notes, walkthrough video, test evidence bundle, Demo Day. Target delivery: week 10, to earn extra adoption epochs.

### Oracles - expected transaction count

1800

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano has five stablecoins with signed Cardano Token Registry entries (USDM, USDCx, USDA, iUSD, DJED), but their liquidity is fragmented across five trading venues using three different pool designs: constant product, stableswap (a curve specialised for pegged pairs), and concentrated liquidity. Anyone moving between two stablecoins must check each venue by hand, cannot see whether splitting the trade or hopping through ADA pays more, and signs against numbers an interface promises rather than numbers the chain enforces. The people with this problem are Cardano stablecoin holders: traders rotating between issuers, users bridging one issuer's off-ramp to another's, and anyone rebalancing a treasury across pegged assets.

Zerochord solves this as a non-custodial routing layer. It reads every venue's pools at one chain state, computes the best route, including splits and ADA hops, in each venue's own integer arithmetic, and writes the quoted minimum output into the single transaction the user signs, so a fill below the quote is impossible rather than merely unlikely. Every quote is measured against the best single direct pool; when that pool wins, Zerochord says so and offers it. A Pyth price feed guards quotes against depegged or manipulated pools, and the price used can be proven inside the transaction itself. Every transaction carries a public metadata tag, so activity, fees and claimed savings are reproducible by anyone from chain data alone.

### 

### Supporting links (repo, site, demo)

- https://web.zerochord.com
- https://zerochord.com
- https://docs.zerochord.com
- https://www.linkedin.com/in/salih-toruner-4919b3212/
- https://github.com/bytemaster333/Zerochord

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

950

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

The entire codebase, including the Aiken validator, is released under the Apache License 2.0, which grants a perpetual, irrevocable licence for the project's lifetime.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

900

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

600

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed work is deploying both integrations to mainnet, and its parts sit at different levels. The stablecoin side is at TRL 5: adapters for all five venues decode live pools, the mainnet configuration carries the five registry-verified stablecoins, and read-only quoting against mainnet works today; but no project script is deployed on mainnet and no mainnet transaction has been built. The oracle side is at TRL 4: the Pyth Lazer client parses signed updates and verifies their Ed25519 signatures against the trusted-signer state Pyth publishes on chain (checked against Pyth's test vector), the guards are tested, and the on-chain proof builder exists; but the guard is not yet wired into the serving path and no price proof has been submitted on chain. TRL 4 is the honest overall floor.
