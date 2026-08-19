# Olympus on Cardano: Identity, Oracles & USDCx

> Olympus on Cardano: stake-key identity and oracle-backed markets, unlocking USDCx for predict & swaps as real ADA mainnet fees scale.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 17
- **Proposer:** `stake1uyetkdjk9axd54yafd5n8fww0ufx39yr52c3l9ehrrcw70sr4enfs`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T13:31:24.882000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

Ian leads Cardano growth and partnerships for Olympus, and is the sole owner of OmegaLabs Protocol OÜ, the legal entity behind the product.

Team URLs:\
Ian Gaertner LinkedIn: <https://www.linkedin.com/in/ian-gaertner>\
Project GitHub (open source): <https://github.com/OmegaNetwork-source/Olympus_Cardano>\
Team intro: <https://www.youtube.com/watch?v=\_XWKD-u-2Io>\
Business registry: <https://ariregister.rik.ee/eng/company/17418123/OmegaLabs-Protocol-OÜ>

We're proud to have already shipped at chain level, with a live beta serving real users on ClearBook, and we're grateful for the public collaboration we've had with the Aptos and Avalanche teams, shown here rather than offered on request: <https://x.com/Aptos/status/2077749689722487255> and <https://x.com/Team1KOR/status/2084186786679722059>. A few additional partner conversations are underway but aren't public yet, so we've chosen not to claim them until they are. We don't assume Cardano works the same way other chains do; its technical character and community expectations are different, and we're approaching it as a stack worth learning properly rather than something to copy-paste from elsewhere.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary give-back: after the pilot, once Cardano product fees exceed ₳25,000 cumulative net revenue, Olympus will share 5% of Cardano-attributable net fee revenue with the Cardano treasury / Catalyst-designated recipient for 24 months, capped at 100% of grant ADA received. Below that threshold: N/A until crossed. Terms finalized in Statement of Milestones if awarded.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Olympus (<https://olympus.omeganetwork.co/cardano>) is our live product; Cardano is a new rail, not yet proven at TRL 9. Genuine usage is Lace users paying their own fees, not scripts or subsidised txs. Budget includes 0 ADA for incentives; incentivised volume isn't counted.

Current base: thousands of monthly connected wallets, hundreds of repeat Predict/swap users. Assumption: \~8% of repeat users (roughly 320 wallets) try Cardano during the window, averaging 12 txs each across Oracles/USDCx/CIP-0170, covering about two-thirds of the 5,700 target (\~3,800 txs). Remaining third (\~1,900 txs) comes from Lace/Minswap referrals: \~475 new wallets averaging 4 txs each.

Targets: Oracles 2,500/750 ADA; USDCx 2,000/900 ADA; CIP-0170 1,200/250 ADA.

CIP-0170: user signs a KERI-backed metadata attestation; Olympus anchors it on mainnet. Oracles price live Predict/market; USDCx settles predict/swap.

Requested 200,000 ADA, engineering-first: 50,000 CIP-0170, 50,000 oracles, 40,000 USDCx (70%); 40,000 QA/footprint/Demo Day (20%); 20,000 Lace/Minswap docs post-hashes (10%).

Declared identifiers, external wallets, daily caps enforced; no team wash volume.

### How will you reach and onboard real users - and what evidence backs your channels?

We onboard via channels we already run—as a dApp aggregator, partnerships and project integrations are how we grow.

1. Aggregator UX: Cardano modules in one hub—Lace connect → identity → oracle markets → USDCx predict/swaps as fees rise. More actions, more mainnet txs.
2. Project integrations: partner oracles, USDCx rails, identity, DEXes/predict venues via CIP-30—each brings that project’s users into fee-paying Olympus flows.
3. Partnerships (proven): co-launches, ambassadors, joint drops—the playbook that scaled us—retargeted to Cardano with a clear first fee-paying action.
4. Discovery: Lace/Eternl + Cardano dApp directories once mainnet-live.
5. First 2 weeks: integration demos, partner shoutouts, guided first-trade sprints.

Evidence: Olympus retains users via aggregated swaps, claims, predictions, and partner integrations. We point that aggregator + partnership engine at Cardano with Dune-tagged fees from external wallets (no wash scripts).

### Is the underlying project open source?

Yes

### Short Video Pitch

https://www.youtube.com/watch?v=_YRAq_cZJOQ

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today users stitch **Lace/Eternl + DexHunter/Minswap + oracle dashboards + separate predict apps + USDCx rails**. Each piece works; none owns the full loop: **identity → trusted price → predict/trade → dollar settle**.

**Alternatives:** wallet-only (Lace), DEX-only (Minswap), data-only (oracle UIs), payments-only (checkout apps), identity-only (attest/KERI tools). Strong alone; fragmented together — users bounce, fees leak off-product, no shared identity.

**Why Olympus wins:** one Cardano product ships **CIP-0170 identity + oracle-backed markets first**, then **USDCx for predict/swaps as real fees rise**. We’re a live product adding Cardano mainnet usage (Dune-tagged), not a research demo — so adoption is sticky UX + measurable fees, not vanity volume.

### Please provide details about the Technology Readiness Level selected for your existing product

Olympus is a live production product in operational use today. Real users already connect wallets, complete swaps/claims/predictions, and return through our dApp aggregator UX. Partner integrations and fee-paying flows run in a real environment—not a lab prototype.

What is proven: production app, wallet connect, market/oracle-style price tooling, identity-linked product surfaces, and partnership-driven onboarding. What this grant funds is new Cardano mainnet work (CIP-0170 identity, oracle-backed markets, USDCx rails)—incremental integration on a TRL 9 base, not research from scratch. Milestone 1 takes that proven stack to Cardano mainnet with verified, repeatable user transactions.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Olympus is a dApp aggregator using CIP-30 (Lace/Eternl). On-chain pieces stay minimal, auditable, and mapped to our three integrations:

1. Identity (CIP-0170): stake-key attestations/registrations bind product identity to Cardano credentials—verifiable “who transacts” for integrity and partner access, not a custodial DB.

2. Oracles: Cardano-ready feeds (e.g. Pyth-class) drive market/predict UX; fee-paying actions that depend on those prices settle on mainnet so counted fees = real oracle-backed usage.

3. Stablecoins: policy-verified USDCx for accept/settle; predict/swap settlement deepens as adoption rises. We integrate approved policies—we don’t launch a new stablecoin—so activity is standard and countable.

4. Aggregator: one CIP-30 session coordinates identity, oracle-priced actions, USDCx, and partner hooks. Catalyst txs use a registered message tag + declared footprint (scripts, policies, addresses, team wallets) for Dune / Proof of Adoption.

Fit: CIP-0170 → identity AoI; oracles → price AoI; USDCx → stablecoin AoI. Compose Cardano primitives for a fast Milestone 1 path, clear fee identifiers, and partnership-friendly design—no wash-volume architecture.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

 Cardano users who already hold ADA and want to *do more on-chain* — traders, prediction participants, and identity-aware wallets — plus teams that need trusted prices and clean dollar settlement without leaving Cardano UX.

Primary segments:

1. **ADA traders & power users** who need oracle-backed live markets (not screenshots or delayed CEX tabs).
2. **Prediction / event users** who want to stake outcomes with clear pricing and, as volume grows, **USDCx** settlement.
3. **Identity-first users & apps** that need stake-key / CIP-0170 style identity so “wallet = reputation,” not anonymous wash volume.

**Evidence of demand / PMF:**\
Olympus is already a **live, production product** with real users connecting wallets, running swaps/claims/predictions, and returning for market tools — so we are not inventing demand from a whitepaper. Crypto users repeatedly ask for the same loop: *identity → trusted price → trade/predict → settle in dollars*. Cardano’s Catalyst Pilot areas (oracles, identity, stablecoins) map exactly onto that loop, and public Cardano activity around USDCx/USDM, oracle feeds, and on-chain identity shows the gap is *integration + UX*, not “does anyone want this.”

Our go-to-market is not “hope ADA users appear.” We convert an existing product audience into **Cardano mainnet transactions** (tagged for Dune), then unlock USDCx predict/swaps as fee volume trends up — so adoption payments track real network fees from real external wallets, not vanity metrics.

### Applicant name

Omega Labs

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Olympus earns from real Cardano mainnet usage—not the grant. Revenue: (1) trading/swap fees on oracle-backed markets; (2) prediction market fees as volume grows; (3) USDCx settlement/rails take-rate once unlocked; (4) optional premium identity/analytics for power users. Who pays: end users and counterparties already paying network + product fees to trade, predict, and settle. The grant only kickstarts Cardano mainnet delivery and early adoption; the pilot’s fee-based adoption payments already prove the model. After funding: identity + oracles create a daily habit (check price → act), USDCx deepens dollar liquidity for predict/swaps, and retained users keep generating tagged on-chain fees. We stay live by shipping utility users need without Catalyst—grants accelerate launch; product fees fund the runway.

### Programmable tokens (CIP-0113) - expected transaction count

800

### On-chain identity (CIP-0170) - expected transaction count

1200

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding lets us bring Olympus to Cardano with the speed and care the ecosystem deserves—pairing a focused mainnet integration with a real growth engine.

It enables: (1) Milestone 1 delivery of identity, oracles, and USDCx rails so ADA users have something excellent to use; (2) primary spend on marketing and partnerships—wallet co-promotion, project integrations, ambassadors, Demo Day, and post-launch campaigns that welcome users into fee-paying flows; (3) discovery and partner BD so predict/swaps deepen as traction grows.

Spend (high level): Cardano marketing & partnerships first, plus targeted engineering to ship mainnet and Dune-tagged usage. The grant accelerates a Cardano launch and adoption push we’re excited to make—turning integration into lasting, genuine network activity.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

M1 (≤3 mo): Cardano mainnet live in Olympus. Budget is engineering-first, 1:1 to three integrations—not marketing-first.

1) CIP-0170 identity: Lace/Eternl connect; stake-key bind/attest in-product; ≥1 real-user mainnet identity tx (repeatable).

2) Oracles: feeds power live market/Predict UI; ≥1 fee-paying mainnet flow using those prices (≥2 independent runs).

3) USDCx stablecoin: policy-verified accept/settle path live; ≥1 real-user mainnet USDCx tx.

Shared: Cardano aggregator module + partner hooks docs; footprint (scripts/policies/addresses/wallets/tags); explorer hashes mapped to each flow; release notes; walkthrough video; test/security bundle; Demo Day demo+Q&A.

Exit: product URL + explorer proofs for all three + Demo Day sign-off → adoption window.

### Oracles - expected transaction count

2500

### How far along is the integration you're proposing, today?

TRL 9 - Actual system proven in operational environment

### Programmable tokens (CIP-0113) - fee target (ADA)

400

### On-chain identity (CIP-0170) - fee target (ADA)

250

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Olympus is building a Cardano-native trading and prediction experience where users get three things in one place: **who they are** (stake-key / CIP-0170 style on-chain identity), **what the market is really doing** (oracle-backed live prices and signals), and **how they settle** (verified USDCx rails for predict and swaps as usage grows).

**The problem:** Cardano users still bounce between wallets, price tools, prediction apps, and stablecoin rails that don’t share identity or trust. Prices feel fragmented, identity is just an address, and dollar liquidity for everyday trading/prediction is hard to use without leaving the chain’s UX. Builders get vanity metrics; users get friction.

**Who it’s for:** ADA holders, traders, and prediction users who want a single Cardano mainnet product they can actually use — connect once, prove identity, trade and predict on trusted oracle feeds, then settle in USDCx when traction justifies deeper dollar rails — generating **real network fees from real wallets**, not scripts.

### Supporting links (repo, site, demo)

- https://olympus.omeganetwork.co/cardano
- https://github.com/OmegaNetwork-source/Olympus_Cardano
- https://docs.google.com/presentation/d/1W9ogG7xV5wYysq7xu80-qn_u12ua2YSWGBo-gDcKq8k/edit?usp=sharing

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

750

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

The on-chain Solidity contract sources in /contracts include SPDX-License-Identifier: MIT at the top of each contract file, meaning those contract sources are MIT-licensed. All other third-party dependencies used by the project are subject to their respective upstream licenses.

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

900

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Cardano work is new mainnet delivery on a proven Olympus base. Architecture is defined: CIP-30 (Lace/Eternl), CIP-0170 identity, oracle price feeds into market/predict UX, then USDCx rails. Components are validated in our live product patterns; Cardano-specific scripts, policies, and fee flows are not yet proven on Cardano mainnet (that is Milestone 1).

Relevant environment: staging/test paths and existing aggregator UX ready to host the module. Operational proof = first real-user, repeatable mainnet txs + declared footprint (identifiers, Dune tags) by Demo Day. Grant funds that jump from validated design to mainnet adoption—not retroactive work.
