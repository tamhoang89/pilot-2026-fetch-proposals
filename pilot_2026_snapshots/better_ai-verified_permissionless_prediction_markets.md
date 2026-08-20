# BETTER: AI-Verified Permissionless Prediction Markets

> Anyone creates a market in 2 minutes and earns trading fees for life. An AI + optimistic oracle engine makes every question machine-resolvable — open infrastructure for all of Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1u9kqeyf99pm2ezt9ajhjaw6kq37gr4kjkh87u66mctjkwqsju0385`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T03:09:54.134000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Temulun Khongorzul (Hiisver) — Project Lead / Product Designer. Founder of HiiLink, The Mich Khan, and Vism Visual Studio. Experienced Web3 builder, UX strategist and product owner; leads project direction, user flows, interface design, milestone planning and documentation quality ([x.com/hiisver](http://x.com/hiisver)). Previously built and operated a live platform on ApeChain that processed 100,000+ on-chain transactions with 1,000+ active users, and ran the Goblin Market demo that attracted 200,000+ registered users in its test phase — proven viral acquisition and on-chain operations at scale.

Engineering covers the full stack this project needs. [github.com/tksulde](http://github.com/tksulde) — full-stack engineer, 30+ public repos spanning Next.js production apps, AI chatbot/agent systems and AI-driven payment infrastructure, directly applicable to our AI resolution engine and dashboard. [github.com/0xCadeZ](http://github.com/0xCadeZ) — smart-contract engineer, 56 public repos across multiple chains: Web3 gaming platforms, Cairo/StarkNet contracts, Account Abstraction (EIP-4337) and on-chain payment protocols — proven ability to master new contract paradigms fast, exactly what shipping Aiken on Cardano's eUTxO model demands.

Together: proven user acquisition (200k+ registrations), proven on-chain operations (100k+ transactions), and multi-chain engineering depth — what a three-month build-to-mainnet sprint requires.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge 10% of the protocol treasury's trading-fee revenue to the Cardano Treasury, activating once monthly protocol revenue exceeds 5,000 ADA, and continuing until 100% of the grant (200,000 ADA) is repaid. Additionally, our Resolution-as-a-Service oracle remains free for open-source Cardano public-goods projects permanently. Repayment status will be published quarterly on-chain.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Three actor types transact recurrently. Traders swap USDM for outcome tokens through per-market AMM pools  every trade is an on-chain script transaction (Stablecoins count). Creators generate market-creation, bond and claim transactions. The resolution engine generates oracle activity: every market produces a resolution proposal with a hash-anchored evidence memo, plus settlement and occasional challenge transactions (Oracles count). Our launch catalog of Cardano governance markets serves an audience that already holds wallets and debates these outcomes weekly. 150 active markets with a median of 60-70 trades each — modest against Polymarket's long-tail data — yields \~10,000 trades at \~0.4 ADA average script fee = \~4,000 ADA. Each market adds \~15-20 oracle-side transactions plus Resolution-as-a-Service pilot calls = \~3,000 transactions, \~1,200 ADA. Why ambitious but valid: this team has already onboarded 1,000+ users generating 100,000+ transactions on ApeChain, so 13,000 transactions in a window is within demonstrated capability, with governance-event spikes (hard forks, elections) as upside. All usage is organic — real traders paying real fees, no wash incentives.

### How will you reach and onboard real users - and what evidence backs your channels?

Day one: we launch with a seeded catalog of Cardano governance markets (hard fork timing, governance actions, Intersect elections)  topics the community already debates daily on X, the Cardano Forum and Discord. This audience holds wallets, needs no crypto onboarding, and is reachable through channels with proven engagement: Cardano Forum threads, ambassador calls, and dRep communities. Onboarding friction is minimized by a one-click ADA-to-USDM swap built into the first-trade flow (via DEX aggregator APIs). We will run an incentivized testnet in month two -the standard Cardano playbook that Bodega and major DeFi protocols used successfully to convert testers into mainnet users. Creator acquisition is structural: lifetime fee-share plus a public creator leaderboard makes every successful creator a recruiting channel. We are pursuing LOIs with USDM ecosystem communities (whose coalition doubled monthly users and retained them after incentives ended — evidence that this audience sticks).

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/w8ZNU5sZSx4

### Who else solves this today - competitors/alternatives, and why does your approach win?

Off-chain/EVM: Polymarket and Kalshi dominate but curate markets centrally, resolve via UMA's slow, bond-gated oracle ($750 to challenge), and don't share fees with creators. On Cardano: Bodega is a curated platform where market creation requires governance approval — a few big markets, not an open layer.

We win on three axes they structurally can't copy quickly: (1) permissionless creation with lifetime creator fee-share — a supply-side flywheel no incumbent offers; (2) a tiered AI + optimistic resolution engine that auto-settles most markets in seconds with on-chain evidence memos, escalating only disputes; (3) positioning as infrastructure — our Resolution-as-a-Service API is an open outcome oracle any Cardano dApp (including Bodega) can consume, making incumbents potential customers.

### Please provide details about the Technology Readiness Level selected for your existing product

Our team's core technology components are individually validated in live environments, while BETTER as an integrated product is new. Our lead's previous platform ran in production on ApeChain with 100,000+ on-chain transactions and 1,000+ users, validating our transaction infrastructure, wallet flows and fee mechanics at scale. Our Goblin Market demo validated the acquisition and onboarding funnel with 200,000+ registrations. The AI resolution approach is validated externally: peer-reviewed research shows web-enabled LLM resolvers reach \~90% agreement with UMA dispute outcomes and 97.9% accuracy on high-confidence auto-resolutions, and UMA's deployed OOTruthBot operates at \~$0.005 per resolution. What remains is composing these validated pieces on Cardano — the work this Pilot funds.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

BETTER is built natively on Cardano's eUTxO model with Aiken smart contracts.

Markets: each market is a parameterized escrow validator holding USDM collateral, minting paired outcome tokens (YES/NO native assets) against deposits. Trading runs through a bonded AMM pool per market — eUTxO-friendly, avoiding order-book concurrency issues while keeping every trade a fully on-chain, fee-paying transaction (the Pilot's success metric). All wagers settle in USDM, giving Cardano's leading stablecoin daily transactional utility and directly serving the Stablecoins area; a one-click ADA-to-USDM swap via DEX aggregators removes onboarding friction.

Resolution (Oracles area): a three-tier engine. Tier A: deterministic outcomes (governance results, on-chain data) settle trustlessly from chain state. Tier B: our AI resolver gathers evidence off-chain and submits a proposed outcome whose reasoning memo is hash-anchored in transaction metadata — publicly auditable — followed by a 24-hour optimistic challenge window where anyone can dispute by posting a bond. Tier C: disputed cases escalate to human arbitration. Market creators post a bond at creation; our AI transforms free-text questions into machine-resolvable specs before listing, and unresolvable markets slash the bond.

This resolution engine is exposed as an open Resolution-as-a-Service API — a general-purpose outcome oracle any Cardano dApp can consume, which is why our own markets are just its first customer.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Our target market has three segments. \
(1) Crypto-native forecasters and traders: Polymarket settled billions of dollars in volume in 2024 and grew through 2025-26 alongside Kalshi, proving forecasting is a killer app; disputed markets alone represent over $970M in traded volume, showing both scale and the unmet need for better resolution. \
(2) Market creators: [pump.fun](http://pump.fun) demonstrated that permissionless creation plus creator fee-share generates explosive long-tail supply — no prediction market has applied this flywheel yet. \
(3) The Cardano community itself: with Voltaire governance live, dReps and delegators debate hard forks, budgets and elections every month with no price signal to aggregate expectations — our launch catalog of governance markets serves an existing, wallet-holding, highly engaged audience with zero cold-start cost.

Evidence of demand on Cardano specifically: the existing curated prediction market (Bodega) reached mainnet and sustained activity despite gating market creation behind governance votes — demand exists even with high friction. Every market it cannot list is our long-tail opportunity. On the resolution side, research shows web-enabled AI resolvers reach \~90% agreement with UMA's dispute outcomes and 97.9% accuracy on high-confidence auto-resolved questions — the technical basis of our engine is validated, not speculative. We will convert LOIs from Cardano DeFi communities into day-one seeded markets.

### Applicant name

Temulun Khongorzul (Hiisver)

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue flows from usage, not grants. Traders pay a small fee on every trade (in USDM); that fee splits three ways: market creator (their lifetime share), protocol treasury, and resolution costs. Market creators pay a small flat listing fee plus a refundable bond — spam control that also generates revenue. Third-party dApps pay per-call or subscription pricing for the Resolution-as-a-Service oracle API.

Why usage continues after the pilot: the creator fee-share is a permanent income stream, so creators keep launching markets without us paying them — supply is self-incentivized. Governance markets renew themselves every epoch: each new governance action, election and hard fork generates fresh markets organically. AI resolution costs roughly $0.005 per market (validated by UMA's OOTruthBot economics), so the unit economics stay positive at small scale. The protocol treasury funds ongoing infrastructure from trading fees alone once volume exceeds a few thousand trades monthly.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, Cardano's prediction market layer stays curated and closed, and no open outcome oracle gets built — our team would ship this on an EVM chain, where our prior traction lives. The grant makes Cardano the home of this infrastructure.

Spend (200,000 ADA): 100k — engineering (three devs, three months: Aiken validators, AI resolution engine, indexer, dashboard); 30k — frontend and USDM on-ramp integration; 25k — third-party security review of escrow and resolution contracts before mainnet; 30k — seed liquidity for the governance-market launch catalog plus creator incentives during the measurement window; 15k — infrastructure (AI APIs, Blockfrost, hosting). Milestone-gated per the 40/40/20 structure, targeting 12,000+ labeled mainnet transactions in the first period.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Month 1 (Preview testnet): Aiken contracts deployed — market escrow validator, YES/NO outcome token minting policy, per-market USDM AMM pool, creator bond/slash logic, 24h optimistic challenge mechanism — open-sourced (Apache 2.0) with tagged GitHub release. AI resolution pipeline v1: question-to-spec transformation, tier classification, evidence resolver with hash-anchored on-chain memos. End-to-end demo: create → trade → resolve → settle.

Month 2 (Preprod): web app with market creation, trading UI, creator fee-share dashboard and one-click ADA→USDM swap; Resolution-as-a-Service API with public docs; third-party security review completed and remediated; incentivized testnet with 500+ unique wallets.

Month 3 (Mainnet): mainnet deployment with Pilot transaction labeling live on the public dashboard; launch catalog of 20+ seeded Cardano governance markets; first real user transactions — 1,000+ labeled in launch month, on track for 13,000+ in the measurement window.

### Oracles - expected transaction count

3000

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

BETTER is a permissionless prediction market protocol on Cardano with an AI-verified resolution layer.

The problem: prediction markets are proven "killer apps" (Polymarket settled billions), but they have two structural flaws. First, market creation is gated — a small team curates a few big markets, so thousands of long-tail questions (local events, governance outcomes, niche industries) never get a market. Second, resolution is the bottleneck: human/token-voting oracles are slow and expensive, while naive automation fails on ambiguous questions. On Cardano specifically, existing options gate market creation behind governance votes, and there is no general-purpose outcome oracle other dApps can reuse.

Our solution, for three audiences:

1\. Creators: anyone spins up a market in 2 minutes for a small fee and earns a lifetime share of its trading fees — a [pump.fun](http://pump.fun)-style flywheel applied to forecasting. A creator bond + on-chain reputation system filters spam.

2\. Traders: all markets settle in USDM, with a one-click ADA/CEX-to-USDM on-ramp, giving Cardano's stablecoin daily transactional utility.

3\. Cardano dApps: our tiered resolution engine — deterministic on-chain data (Tier A), AI proposer with evidence memos + optimistic challenge window (Tier B), human arbitration (Tier C) — is exposed as an open Resolution-as-a-Service API. We are building the outcome-oracle infrastructure Cardano lacks, with our own markets as its first consumer.

### Supporting links (repo, site, demo)

- https://dune.com/hiisver/hiilink
- https://www.gobmarket.com/
- https://x.com/basenameapp
- https://github.com/Erchim-Labs

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

1200

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

All core components are open source under Apache 2.0: Aiken smart contracts (escrow, AMM, bonds, challenge logic), the AI resolution engine, and the indexer. Public GitHub repo from month one, tagged releases at each milestone. Every AI resolution memo is hash-anchored on-chain, making resolutions publicly auditable — not just the code. The Resolution-as-a-Service API will be openly documented so any Cardano dApp can integrate without permission. Only the BETTER brand/logo remain team property.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

10000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

4000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The Cardano-specific integration is at proof-of-concept stage today. We have designed the full architecture: Aiken validators for market escrow and outcome tokens, USDM as the settlement asset (policy ID integration via Blockfrost is documented and straightforward), and the three-tier resolution flow with on-chain evidence memos in transaction metadata. Our AI resolution pipeline exists as an off-chain prototype (question-to-spec transformation and evidence-gathering agent) built on infrastructure our team has already shipped in production for AI agent systems. No Cardano mainnet deployment exists yet — months one and two of the build plan take this from PoC through Preview and Preprod testnets, with an incentivized testnet in month two, reaching mainnet (TRL 7-8) in month three.
