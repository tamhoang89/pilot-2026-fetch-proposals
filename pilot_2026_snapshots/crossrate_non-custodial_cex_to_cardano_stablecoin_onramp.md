# Crossrate: Non-Custodial CEX to Cardano Stablecoin Onramp

> Compare every route from a centralised exchange to USDCx or USDM on Cardano, priced live with every cost named, then sign the final step from your own wallet. No custody, no server-side keys.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1uxaqgj9dt06c9xq473jz6dszlw7qsgn4wyghjmle7m63rsq3hyhg3`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T04:45:38.178000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Mert Köklü, software engineer and sole developer, delivering the full scope: the Aiken validator, the API and route engine, the web app, deployment and the adoption-phase operation.

He brings over five years of blockchain engineering across developer tooling, wallets, SDKs, smart contracts and integrations, holds a BSc in Computer Engineering, and has led engineering teams in both AI and blockchain. He has built, shipped and been funded to deliver work across the Stellar, Arbitrum, Cardano, Internet Computer and StarkNet ecosystems through contracts, partnerships, grants and open-source contributions. Earlier he built StarkNet plugins and Cairo-language compiler tooling at ApeWorX, and led large-scale computer-vision projects as AI Video Analytics Team Lead at an NVIDIA partner company. SoroPass, his passkey SDK that turns a device passkey into the signer of a Soroban smart account, won a Stellar Community Fund award (SCF #44, RFP track).

Selected works:

- Pocket: self-custody Stellar wallet with confidential, amount-hiding transfers (<https://github.com/justmert/pocket>)
- SoroPass: passkey SDK and UI components for Stellar smart accounts (<https://github.com/justmert/soropass>)
- Sluby: decentralized video streaming with adaptive HLS on the Sia network (<https://github.com/justmert/Sluby>)

Links: <https://mertkoklu.com>, <https://github.com/justmert>, <https://www.linkedin.com/in/mertkoklu>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: real users converting exchange-held USDC or ADA into USDM or USDCx, each signing two transactions from their own wallet, the order and the claim. Both carry the registered label 674 tag, and the claim also spends from the declared script hash. Why: this is the unavoidable final step of every self-custody entry, so volume comes from a stream of new users rather than repeat loops. Cadence and derivation: 2,500 counted transactions is about 1,250 full conversions, roughly 42 per day across the six floored epochs; at the measured mainnet fee of 0.17 to 0.20 ADA per transaction that yields 425 to 500 ADA, so 450 ADA is the fee target, a quarter above the 360 ADA program floor at this requested amount. Distinct wallets track conversions by construction, since every conversion requires that user's own signatures, and I target at least the Standard's external-wallet minimum. For a newly launched, solo-built product this is ambitious but not artificial: each counted transaction needs a real user's signature, real committed ADA and a real batcher-delivered swap. M1 delivery by week 10 earns extra epochs of headroom.

### How will you reach and onboard real users - and what evidence backs your channels?

The channels are concrete and mostly already built, not a marketing plan. First, the product's own user documentation covers the complete journey for first-time users: wallet setup, route comparison, per-exchange withdrawal steps, signing and troubleshooting. Onboarding is the product. Second, the open-source repository and a public technical walkthrough give the Cardano developer community reasons to inspect, link and recommend the tool, which is how infrastructure spreads in this ecosystem. Third, Demo Day and the public daily adoption chart put verifiable usage in front of the community during the measurement window. Fourth, direct presence where new users already ask how to get dollars onto Cardano: the forum, subreddit and wallet-community channels, answered with a working tool rather than a pitch. I hold no letters of intent and claim none. The milestone's distinct-user minimum is addressed by making the first conversion genuinely easy and by supporting early users directly.

## 

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today's alternatives each cover a fragment. Circle's USDCx portal executes the bridge crossing well, for USDC only, with no comparison against selling to ADA and no exchange-side guidance; Crossrate lists that portal as a route and recommends it whenever it wins. Cardano DEX aggregators compare swaps once value is already on Cardano, but the deciding costs, exchange withdrawal fees and spreads, sit before their first screen. The default alternative is doing it by hand across exchange screens, a bridge portal and a DEX interface, with no total and no arrival tracking. Crossrate wins by pricing the whole journey end to end, labelling every figure's source, refusing to total unknowns, and being structurally unable to bias the result: ranking cannot read who gets paid, and a test enforces it.

### Please provide details about the Technology Readiness Level selected for your existing product

The complete system prototype operates in an operational environment: the public preprod network and live production upstreams. The end-to-end suite injects a CIP-30 wallet backed by a funded preprod key, produces real Ed25519 witnesses and submits to the preprod chain; arrival detection is proven by the real reconciliation sweep reading the real chain and by browserless CLI proofs that pay a watched address on-chain and observe detection. The validator's execution units are measured on a real evaluated transaction (22,917 memory, 7,488,318 steps, about 0.1 percent of budget), not estimated. The quote engine already runs on live data: KuCoin, Bitget and HTX fees, mainnet Minswap and SundaeSwap reserves, live protocol parameters. CI verifies the deployed script hash four ways per commit.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Cardano's deep stablecoin liquidity is batcher-executed: the user's own transaction moves only ADA into a venue's order script, and a third party's transaction delivers the token. The architecture works with that reality. The order names my claim validator as the DEX's success receiver, with a datum naming the user and a per-session correlation id; the batcher delivers the swapped stablecoin into the validator; the user signs a second transaction claiming it to their own address, fee paid from their own inputs. Refunds route to the user's wallet directly, never through the script.

The validator is a single Aiken Plutus V3 spend handler enforcing one rule: the beneficiary named in the datum must have signed the spending transaction. It asserts nothing about outputs, which makes the documented double-satisfaction pattern inapplicable, and its implicit fallback rejects every non-spend purpose, verified on a real evaluator. A compile-time parameter gives it a collision-free hash, identical on every network: fcda4f62512db8af046a1bce3177dca7eb1ea91aa041a519070668cb. Off-chain strictness completes it: outputs are selected by parseable datum, never by address, and a wallet fee input is added explicitly so locked funds never pay the fee.

The fit with the program is direct: every transaction carries a CIP-20 label 674 tag with project identifier, step and session id, so adoption is natively measurable against the declared script hash and message tag, exactly as the Standard requires.

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

The target market is every person funding a Cardano wallet from a centralised exchange who wants to hold dollars rather than ADA: new entrants to the ecosystem, and existing holders moving stablecoin balances into self-custody. Exchange accounts are where most people's dollars already sit, and Cardano's stablecoins are reachable from them only through multi-system journeys, so this audience is the ecosystem's self-custody stablecoin inflow itself rather than a niche inside it.

Rather than a headline sizing figure, here is measured evidence that the problem is real and expensive. Price dispersion: at the reserves measured on 2026-08-20, the direct ADA to USDCx pool and the two-hop path through USDM priced USDCx about 2 percent apart, so route choice moves real money on ordinary amounts. Fee asymmetry: Minswap's ADA and USDCx pool charges 2.5 percent in one direction and 1.5 percent in the other, which no casual user discovers unaided. Fee opacity: OKX, Bybit, MEXC and [Crypto.com](http://Crypto.com) expose no public withdrawal-fee endpoint and Kraken sets its fee only at withdrawal time, so comparing costs by hand is impossible. Irreversible failure: exchanges name Cardano inconsistently (KuCoin says ADA, Bitget says Cardano) and a wrong network selection is unrecoverable. Finally, holders of USDT, the most widely held stablecoin, have no direct path at all and need guided conversion first. Demand is the recurring stream of people hitting these walls.

### Applicant name

Mert Köklü

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Today no route carries a Crossrate fee: every cost line is an exchange, network, pool, batcher or bridge cost. The design reserves exactly one place to earn, the conversion route that runs my own contract, which the codebase already distinguishes as the route Crossrate earns from, while a dedicated test keeps the ranking blind to who is paid. After the pilot, a small disclosed service fee is introduced there as its own provenance-labelled cost line, paid by the user inside a transaction they sign, so revenue scales with exactly the mainnet usage this program measures, and the comparison stays honest whether or not that route wins. Operating costs are low by construction: the primary chain provider needs no credential, the stack is one API, one PostgreSQL and a static front end, and the source is Apache-2.0, so the service stays cheap to run and cannot be orphaned. Usage persists because the need recurs with every new wallet funded from an exchange.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

I build Crossrate alone and unfunded, and only the launch itself remains. This grant funds the step that will not otherwise happen on this timeline: taking the system from preprod verification to a production mainnet service with real users. Concretely: exercising the real batcher-delivered order path on mainnet, deploying and recording the validator, production infrastructure and monitoring, adoption instrumentation with the declared footprint, and operating and reporting through the measurement window. High-level spend: 160,000 ADA for three months of full-time development and hardening to M1, and 40,000 ADA for infrastructure plus the adoption-phase operation, monitoring and per-epoch reporting through M2. All requested funds are development costs; no marketing spend is included.

## 

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Claim validator live on mainnet at the declared script hash and address, with the deployment recorded in the network descriptor.
- Full conversions executed on mainnet by real external users: a Minswap V2 order naming the validator as success receiver, batcher delivery, and a user-signed claim, all tagged under label 674, repeated without failure and evidenced by explorer-linked transaction hashes mapped to flow steps.
- Production deployment of the web app and API at [crossrate.app](http://crossrate.app), with webhook plus reconciliation arrival detection and live quotes across KuCoin, Bitget, HTX and the enabled mainnet DEXes.
- Declared on-chain footprint per the Proof of Adoption & Standard: script hash, addresses, registered message tag and team wallets, with the public daily chart counting from delivery.
- Release notes, a short technical walkthrough video, a tagged Apache-2.0 release, and the test evidence bundle (checklist, logs, security note).
- Live demo, Q&A at Demo Day.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

An exchange account holds USDC on Ethereum, Base or Solana. Cardano has its own dollar stablecoins, USDCx and USDM. There is no single button between the two, and the paths that do exist do not cost the same amount on the same day.

The gap hurts in specific ways. Several major exchanges publish no withdrawal fee, so the cost of leaving is invisible until the final screen. Every exchange names Cardano differently in its withdrawal form, and picking the wrong network loses the funds irreversibly. The destination assets do not trade at par, so a larger number can be a worse outcome. And the last step, a smart-contract transaction on Cardano, is one a first-time user cannot safely build by hand.

Crossrate closes that gap for anyone moving dollars from a centralised exchange into self-custody on Cardano. It prices every route at the moment of asking: withdrawal fees and spreads read live from KuCoin, Bitget and HTX, pool reserves from the enabled Cardano DEXes, bridge fees from Circle's published schedule, and network costs from live protocol parameters. Every cost is a named line with its source, routes rank purely on what the user ends up holding, outputs are valued in the starting asset, and an unknown figure is shown as unavailable rather than zero. It then gives exchange-exact withdrawal steps, watches the chain server-side while the tab is closed, and builds the two final transactions the user signs from their own wallet. Crossrate holds no keys and never takes custody.

### Supporting links (repo, site, demo)

- https://github.com/justmert/crossrate
- https://web.crossrate.app/
- https://crossrate.app/
- https://docs.crossrate.app/
- https://mertkoklu.com

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

The source is public and released under the Apache 2.0 license.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

2500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

450

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration is built and testnet-proven, not yet launched. Done: the Aiken Plutus V3 claim validator with property tests and a parameterised, collision-free script hash; both transaction builders with datum-filtered UTxO selection, explicit fee inputs and post-reassembly metadata checks; the Minswap V2 order datum verified against a real on-chain order; analysis of 923 resting mainnet orders confirming the script-receiver delivery pattern is live practice; mainnet addresses declared in every network descriptor. Not done, and what this grant covers: no mainnet transaction exists yet, the real batcher-delivered order path is unexercised on mainnet, the descriptor deployment fields are still null, and there is no production deployment, monitoring or declared adoption footprint.
