# Crossrate: Exchange-to-Cardano Stablecoin Onramp on Mainnet

> Live end-to-end pricing of every route from a centralised exchange to USDCx or USDM on Cardano, every fee labelled with its source, and a final conversion the user signs from their own wallet.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1uxaqgj9dt06c9xq473jz6dszlw7qsgn4wyghjmle7m63rsq3hyhg3`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-24T11:26:19.738000+00:00

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

Who: real users converting exchange-held USDC, USDT or ADA into USDM or USDCx, signing order and claim from their own wallet; both carry the label 674 tag, the claim spends from the declared script hash. Why: the unavoidable final step of self-custody entry; cautious users test a tranche first, returning wallets top up.

Derivation: 4,000 counted transactions is 2,000 conversions; at measured 0.17-0.20 ADA per transaction, 680-800 ADA; the target is 720: double the 360 floor, inside the Credible band at this size. Per-epoch plan, ADA/tx: 60/333, 84/467, 108/600, 132/733, 156/867, 180/1000, above base-case floors of 60 then 120 ADA; M1 targets week 10; earlier delivery stretches the window and lowers every floor.

Wallets: 40+ distinct external by day 10, above the 36-wallet program minimum, 400-600 over the window per the funnel; GET /adoption excludes own wallets, discounts concentration and caps days; manufactured volume cannot meet this plan.

Why not Ambitious, as required at this size: solo-built, zero mainnet baseline, every counted transaction needs a real signature, committed ADA and a batcher fill; the only faster lever is paid acquisition, which the program prohibits.

### How will you reach and onboard real users - and what evidence backs your channels?

Channels are built; volumes are estimates; I hold no LOIs. A launch thread plus recurring answered questions on the Cardano Forum, r/cardano and wallet-community channels, with Demo Day and the public daily adoption chart: 20,000-30,000 impressions in the window; at a 4% first-try rate and 50% completion with hands-on support, 400-600 first-converting wallets; at 3-4 conversions per wallet (test tranche, main transfer, recurring top-ups), 1,200-2,400 conversions, bracketing the 2,000-conversion target, lower bound above the floor.

Onboarding is the product: docs cover wallet setup through troubleshooting; I assist each early user directly, a loop continuing past launch.

First two weeks, dated from M1 sign-off: days 1-5, entry ramp, launch posts live, 25-30 assisted conversions, 12+ external wallets; days 6-10, 100+ further conversions, 40+ cumulative wallets, past the 36-wallet minimum; days 11-14, 265+ cumulative conversions, 65+ wallets, exiting at the 60 ADA epoch-floor pace.

## 

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today's alternatives each cover a fragment. Circle's USDCx portal executes the bridge crossing well, for USDC only, with no comparison against selling to ADA and no exchange-side guidance; Crossrate lists both portal paths and recommends them whenever they win. Cardano DEX aggregators compare swaps once value is already on Cardano, but the deciding costs, exchange withdrawal fees and spreads, sit before their first screen. The default alternative is doing it by hand across exchange screens, a bridge portal and a DEX interface, with no total and no arrival tracking.

Crossrate wins by pricing the whole journey end to end, labelling every figure's source, refusing to total unknowns, and being structurally unable to bias the result: ranking cannot read who gets paid, and a test enforces it.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 7: the system is live on Cardano mainnet with real transactions, run 2026-08-23/24 as a controlled self-test. Three Minswap batcher deliveries paid verified USDM into the claim validator, and two user-signed claims moved 2.42 USDM out with the fee paid from the signer's own inputs, the on-chain arithmetic closing exactly. Claim fees measured 195,524 and 195,568 lovelace, within 44 lovelace of the preprod measurement for the same shape.

Before that, the end-to-end suite injected a CIP-30 wallet on preprod, produced real Ed25519 witnesses and submitted to chain; CI verifies the script hash four ways per commit.

Not TRL 8: the claim validator has no independent security audit, and no external user has transacted, so the product's own counter counts zero external fees.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Cardano's deep stablecoin liquidity is batcher-executed: the user's own transaction moves only ADA into a venue's order script, and a third party's transaction delivers the token. The order names my claim validator as the DEX's success receiver, its datum naming the user and a session correlation id; the batcher delivers the swapped stablecoin into the validator; the user signs a second transaction claiming it to their own address, fee paid from their own inputs, a flow now proven on mainnet. Refunds route directly to the user's wallet, never through the script.

The validator is a single Aiken Plutus V3 spend handler enforcing one rule: the beneficiary named in the datum must have signed the spending transaction. It asserts nothing about outputs, so the documented double-satisfaction pattern is inapplicable, and its implicit fallback rejects every non-spend purpose. A compile-time project-id parameter gives each deployment a collision-free hash, so M1 deploys a fresh footprint. Off-chain strictness completes it: outputs are selected by parseable datum, never by address, and an explicit wallet fee input means locked funds never pay the fee.

Program fit is built in: every transaction carries a CIP-20 label 674 tag with project, step, session and network, and GET /adoption applies the Standard's rules to public chain data (declared-hash eligibility, own-wallet exclusion, wallet minimum, concentration discount, daily cap, epoch floors) with a per-transaction audit trail.

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

The target market is every person funding a Cardano wallet from a centralised exchange who wants to hold dollars rather than ADA: new entrants to the ecosystem, and existing holders moving stablecoin balances into self-custody. Exchange accounts are where most people's dollars already sit, and Cardano's stablecoins are reachable from them only through multi-system journeys, making this audience the ecosystem's self-custody stablecoin inflow, not a niche inside it.

Rather than a headline sizing figure, here is measured evidence the problem is real and expensive. Price dispersion: measured live on 2026-08-20 against an ADA/USDC reference, USDM traded 1.37% below peg and USDCx 2.96% below, so destination choice alone moves value by 1.6 points, and the direct ADA to USDCx pool and the two-hop path through USDM priced about 2% apart. Fee asymmetry: Minswap's ADA and USDCx pool charges 2.5% in one direction and 1.5% in the other, which no casual user discovers unaided. Fee opacity: of the twelve exchanges modelled, only KuCoin, Bitget, HTX and Bitfinex publish a withdrawal fee without credentials, and Kraken states its fees are dynamic, so comparing costs by hand is impossible. Irreversible failure: exchanges name Cardano inconsistently (KuCoin says ADA, Bitget says Cardano) and a wrong network selection is unrecoverable. USDT, the most widely held stablecoin, has no bridge path and needs guided conversion first. Demand is the recurring stream of people hitting these walls.

### Applicant name

Mert Köklü

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Today no route carries a Crossrate fee: every cost line is an exchange, network, pool, batcher or bridge cost. The design reserves exactly one place to earn, the conversion route that runs my own contract, which the codebase already distinguishes as the route Crossrate earns from, while a dedicated test keeps the ranking blind to who is paid. After the pilot, a small disclosed service fee is introduced there as its own provenance-labelled cost line, paid by the user inside a transaction they sign, so revenue scales with exactly the mainnet usage this program measures, and the comparison stays honest whether or not that route wins.

Operating costs are low by construction: the primary chain provider needs no credential, the stack is one API, one PostgreSQL and a static front end, and the source is Apache-2.0, so the service stays cheap to run and cannot be orphaned. Usage persists because the need recurs with every new wallet funded from an exchange.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

I built Crossrate alone and unfunded, through to a mainnet self-test completed at my own cost. This grant funds what has never happened and will not on this timeline otherwise: real external users on a production service. Concretely: the fresh M1 footprint deployment (no pre-grant identifiers), production infrastructure and monitoring at [crossrate.app](http://crossrate.app), the declared footprint and floor schedule published via GET /adoption, first external conversions, and per-epoch operation and reporting through the window.

High-level spend: 160,000 ADA for three months of full-time development and hardening to M1, and 40,000 ADA for infrastructure plus the adoption-phase operation through M2. All requested funds are development costs; no marketing spend and nothing retroactive.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Fresh-parameterized claim validator deployed and declared on mainnet: a new project id renews script hash, address and label 674 tag together, so no declared identifier carries pre-grant traffic, per the Standard's §4.1.
- Full conversions executed on mainnet by real external users on the declared footprint: a Minswap V2 order naming the validator as success receiver, batcher delivery, and a user-signed claim, repeated without failure, evidenced by explorer-linked hashes mapped to flow steps.
- Production deployment of the web app and API at crossrate.app: webhook plus reconciliation arrival detection, web push notifications, and live quotes across KuCoin, Bitget, HTX, Bitfinex and the enabled mainnet DEXes.
- Declared footprint served by the public GET /adoption endpoint powering the daily chart from delivery.
- Release notes, a technical walkthrough video, a tagged Apache-2.0 release, and the test evidence bundle (checklist, logs, security note).
- Live demo and Q&A at Demo Day.

### How far along is the integration you're proposing, today?

TRL 7 - System prototype demonstrated in operational environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

An exchange account holds USDC or USDT. Cardano has its own dollar stablecoins, USDCx and USDM. No single button connects the two, and the existing paths do not cost the same on the same day.

The gap hurts in specific ways. Of the twelve exchanges Crossrate models, only four publish a withdrawal fee without credentials, so the cost of leaving is invisible until the final screen. Every exchange names Cardano differently in the withdrawal form, and picking the wrong network loses the funds irreversibly. The destination assets do not trade at par, measured 1.6 points apart on 2026-08-20, so a larger number can be a worse outcome. And the last step is a smart-contract transaction a first-time user cannot safely build by hand.

Crossrate closes that gap for anyone moving dollars from a centralised exchange into self-custody on Cardano. It prices every route at the moment of asking: withdrawal fees and spreads read live from KuCoin, Bitget, HTX and Bitfinex, pool reserves from the four enabled mainnet DEXes, bridge fees from Circle's published schedule, and network costs from live protocol parameters. Every cost is a named line with its source, routes rank on the final holding's live value, and unknowns show as unavailable, never zero. It gives exchange-exact withdrawal steps, watches the chain server-side while the tab is closed, notifies by web push, and builds the two final transactions the user signs from their own wallet. Crossrate holds no keys and never takes custody.

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

4000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

720

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 7, plainly: the integration's defining step, a third-party batcher delivering a stablecoin into my validator, has now executed on mainnet, followed by user-signed claims, all tagged under label 674. It was a self-test: every fee-paying wallet is my declared ops wallet, GET /adoption excludes it as own-wallet, and counted external fees are zero.

Nothing from that footprint will be declared at M1: the Standard's §4.1 bars identifiers that carried pre-grant traffic, and the validator's compile-time project-id parameter makes the M1 deployment a fresh hash, address and message tag with no history.

The grant funds the program's own defined climb from here, TRL 7 to 9: a production service, first real external users, and the measured adoption window. Nothing requested is retroactive.
