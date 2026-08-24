# Zerochord: Oracle-Guarded Stablecoin Routing on Cardano

> One quote across five venues and three pool designs, a minimum the blockchain enforces on every swap, a Pyth guard against depegged pools, and savings anyone can recompute from public chain data.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 11
- **Proposer:** `stake1ux7wcc580qm4aypf5aqy2v5vaujrv2pywt8xmr9wujfytfc25e2fz`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-24T11:26:53.174000+00:00

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

## 

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: holders moving between the five verified stablecoins because venues, counterparties or redemption paths demand different issuers. The flow repeats because dispersion across venues recurs; every trade carries an on-chain floor and an auditable saving, and honest comparison means Zerochord never costs more than the direct trade. Cadence: many small and mid-size swaps, not bursts, fitting per-epoch floors and the daily cap.

The targets: oracle transactions are the Kernel-class swap subset carrying the Pyth proof, budgeted at half of activity, contained within the stablecoin totals. Stablecoins, 1,800 transactions, is about 60 a day over the minimum 30-day window; 40 external wallets at 1.5 swaps a day reach it, above the award's 36-wallet minimum. The deployment is new and unannounced, so projected usage is new external adoption, not an existing base: hence targets in the published Credible band. Fees: the audited preprod two-hop swap paid 601,501 lovelace, so 1,000 ADA over 1,800 transactions at a 0.56 average is measured; proof-carrying swaps cost more from added script execution: 650 ADA over 900 at 0.72. Own wallets are declared and excluded from every count.

### How will you reach and onboard real users - and what evidence backs your channels?

My channels are specific; I claim no partnerships or letters of intent I do not have. zerochord.com already serves mainnet in a quiet soft launch; the public announcement lands at delivery, when counting starts and the daily chart goes live.

First, the receipt is the channel: every swap shows the enforced minimum and realised saving, and a public audit command lets a sceptic recompute the claim from chain data; launch threads on the Cardano Forum and X open with that challenge. Second, the communities of the five routed venues, where users who trade these pairs gather. Third, public surfaces: the registered tag feeds the program's Dune dashboard from day one, and a DefiLlama submission.

First-two-weeks targets after the announcement: week one, at least 15 external wallets and 150 tagged swaps; week two, 36 or more wallets, past this award's external-wallet minimum, at 40 or more swaps a day. No paid acquisition exists or is planned; own wallets are declared and excluded.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The default alternative is each venue's own interface: Minswap, SundaeSwap and Dano Finance, including the two dedicated stableswap products. Minswap also runs an aggregator, which Zerochord deliberately uses as an independent cross-check of its arithmetic, so the competition is real and measured. Off chain, users can route through a centralised exchange.

Zerochord wins on four things no single venue offers together: one quote comparing all five venues and three curve types; a minimum enforced on chain for every route class, extended to mixed routes by its own settlement validator; an oracle guard that refuses quotes from mispriced pools; and honesty as a feature: when a direct pool beats routing, the product says so and switches to it. A venue cannot credibly copy that last property.

### Please provide details about the Technology Readiness Level selected for your existing product

Zerochord is live on Cardano mainnet: [zerochord.com](http://zerochord.com) serves mainnet in an unannounced soft launch, and the settlement validator is deployed there with a provenance-checked footprint. I rate the product TRL 6, up from the prior review's TRL 5.

The validation record sits on preprod, where destructive tests belong: web app and CLI quote, build, sign and submit; swaps of three shapes settled on chain; orders placed, filled and cancelled; the validator's claim and refund paths each exercised beside a refused adversarial twin: a claim one base unit short, a refund one slot early, a double-satisfaction attempt. The validator carries 31 Aiken tests, including property tests. Security testing remains self-conducted; the one project-owned script is 1,384 bytes.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Zerochord is five TypeScript libraries, a web app, a CLI and an on-chain project in Aiken, Cardano's smart-contract language, with one validated configuration per network. Venue adapters reduce five venues and three curve types to one interface with an execution class. Kernel venues settle atomically inside the user's own transaction through the withdraw-zero pattern; Commitment venues take an order carrying a binding minimum a permissioned batcher fills later, with a cancel path. The quote engine enumerates paths exhaustively, reduces each to an effective pool, solves the split, then requotes the winner in each venue's own integer arithmetic, so the on-chain minimum matches what venue validators check; a floor keeps the route at least as good as any single candidate path.

Stablecoins need exactly this: cross-curve routing with binding minima over fragmented pegged liquidity. The settlement validator (Plutus V3, 1,384 bytes, one-script-input rule against double satisfaction, deployed on mainnet and preprod) extends the all-or-refund guarantee to mixed routes. The oracle side follows Pyth's Cardano design: Ed25519 signatures checked against trusted signers read from the on-chain Pyth state, 120-second freshness and 200-basis-point deviation guards on every quote, and a zero-lovelace withdrawal through Pyth's published script proving the price in-transaction. CIP-20 tags and the footprint, measure, audit and integrity commands make every claim checkable from public data.

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

The target market is holders of Cardano's dollar-pegged stablecoins who need to move between them: users bridging one issuer's rails to another's, treasuries spreading exposure across issuers, and anyone needing a specific coin for a venue or redemption path. The need recurs because prices for the same pair drift apart across five venues, so anyone who swaps without comparing them pays that dispersion; Zerochord measures it on every quote. The product automates nothing, holds no funds and takes no positions; every counted transaction is one a user signed.

I will not quote a market-size figure I cannot source. The evidence I can point to is structural and verifiable on chain. Five issuers maintain signed Cardano Token Registry entries: five live dollar products on mainnet. Minswap and SundaeSwap each run a dedicated stableswap product beside their general pools; purpose-built stable-pair infrastructure only exists where those pairs actually trade. The same pairs also sit in constant-product and concentrated-liquidity pools; reading mainnet today, the router enumerates about 224 candidate routes for one pair and quotes for the same trade differ measurably across venues at one block.

Demand at scale is what the adoption window tests; I claim no user counts I cannot evidence. What exists now: zerochord.com already serving mainnet in an unannounced soft launch, the settlement validator deployed on mainnet, and a complete end-to-end validation record on preprod.

### Applicant name

Salih Toruner

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Zerochord charges no fee of its own. Users pay only venue fees and the Cardano network fee from their own wallet, so the network fees the program measures are generated by ordinary usage; an included integrity scanner proves in code that nothing pays, rewards or rebates anyone to transact, so measured demand is real demand.

Sustainability is engineered on the cost side. The web application is a static build reading Koios through a small token-holding proxy, and the Pyth Pro key is free for Cardano projects under the Intersect and Pyth offer, so operating cost stays near zero: hosting, the proxy and monitoring, within a solo maintainer's reach. Usage persists after the grant because the value is durable: a binding floor and a checkable saving are worth more than any single venue's quote. Continuity does not depend on me: the code is Apache-2.0 and any operator can run a deployment from one configuration file. If a routing fee is ever introduced, the section 9 pledge applies.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding takes Zerochord from a quiet soft launch into oracle-enforced public operation; none funds completed work: the settlement deployment and soft-launch serving were paid before this proposal. It covers: the token-holding oracle service live once the Pyth Pro key lands, so every served quote carries a verified Pyth reference; the price proof attached to Kernel swaps with budget tests for the combined transaction; hardening, monitoring and the public launch, venue references verified against live pools; claim and refund demonstrated on mainnet; public measurement, Dune tagging and the Demo Day bundle, then the adoption window.

The 200,000 ADA: 168,000 development labour (16 weeks, one developer), 24,000 infrastructure, 8,000 on-chain verification and launch transactions.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Oracle enforcement live on mainnet: the token-holding service gives every quote a verified Pyth reference under freshness and deviation guards, and Kernel-class swaps carry the zero-lovelace Pyth withdrawal proving the price on chain, with budget tests for the combined transaction.
- zerochord.com publicly launched from soft launch: connect a CIP-30 wallet, quote the five verified stablecoins across all venues, sign once, submit; receipts read the net amount from the chain; pending-order tracking with on-chain cancel.
- Settlement claim and refund demonstrated on the already-deployed mainnet validator; footprint published and checking clean.
- Verified mainnet transactions by real external users for each declared flow, hashes mapped to steps.
- Public measurement: audit and measure reproducible; the registered tag feeding the program's Dune tracking; daily chart live from delivery.
- Release notes, video, evidence bundle, Demo Day. Target: week 10, earning extra adoption epochs.

### Oracles - expected transaction count

900

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano has five stablecoins with signed Cardano Token Registry entries (USDM, USDCx, USDA, iUSD, DJED), but their liquidity is fragmented across five trading venues built on three incompatible pool designs: constant product, stableswap and concentrated liquidity. Anyone moving between two stablecoins must check each venue by hand, cannot see whether splitting the trade or hopping through ADA pays more, and signs against numbers an interface promises rather than numbers the chain enforces. The people with this problem are Cardano stablecoin holders: users bridging one issuer's rails to another's, organisations spreading treasury risk across issuers, and anyone who needs a specific coin for a specific venue or redemption path.

Zerochord solves this as a non-custodial routing layer. It reads every venue's pools at one chain state, computes the best route, including splits and ADA hops, in each venue's own integer arithmetic, and writes the quoted minimum into the single transaction the user signs, so a fill below the quote is impossible rather than merely unlikely. Every quote is measured against the best single direct pool; when that pool wins, Zerochord says so and switches to it in one press. A Pyth price guard refuses quotes from depegged or manipulated pools, and the price used can be proven inside the transaction itself. Every transaction carries a public metadata tag, so activity, fees and claimed savings are reproducible from chain data alone.

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

650

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

1800

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration is serving on Cardano mainnet: adapters for all five venues decode live pools, the configuration carries the five registry-verified coins, zerochord.com runs mainnet in a soft launch, and the settlement validator is deployed there with claim and refund proven on preprod.

The oracle integration is built and validated: freshness and deviation guards run inside every quote, signed Pyth Lazer updates verify against trusted signers read from the on-chain Pyth state (checked on Pyth's test vector), the zero-lovelace withdrawal proof ran end to end on preprod, and the production token-holding service is written, the Pyth Pro key pending. TRL 6 overall. This grant covers what remains: live oracle enforcement, the price proof on Kernel swaps, the public launch.
