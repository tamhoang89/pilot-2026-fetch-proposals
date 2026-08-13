# Mishkan Protocol

> Where Communities Deliberate

## Proposal Metadata

- **Status:** finalized
- **Revision:** 7
- **Proposer:** `stake1uxd9qla44kaftahx8r8z4q5lgyn0lcd8n7uytpjntdcph3qlgneay`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-12T20:01:35.937000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

Leslie T. Borerwe 

[Linkedin](https://www.linkedin.com/in/leslie-borerwe/)

This is a solo-founder team, and that's relevant context rather than a gap to hide: the founder is a self-taught developer, having transitioned into software from a non-technical trade background, now building exclusively in civic-tech and fintech for African and emerging markets.

Directly relevant to this proposal: the founder has already shipped Poloos Council, a live, functioning token-gated governance app — the exact docket/submit/vote/archive workflow Mishkan Protocol generalizes and proposes extending to Cardano. This isn't a concept being built from scratch for the grant; it's a working pattern being made chain-agnostic, which lowers delivery risk considerably compared to a net-new build.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Mishkan Protocol generates hosted-instance revenue post-pilot (core voting/governance stays free permanently), we pledge 5% of net hosted-instance revenue back to the Cardano ecosystem — via Catalyst or a similar public-goods fund — for 24 months post-mainnet-launch, capped at 1x the grant amount received.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Redesigned around genuinely external, distinct-wallet-paid fees, not team-paid distribution: pilot members self-claim their CIP-0113 governance token via a "Join Council" flow — each submits their own wallet-signed claim and pays their own fee. The team never pays on a member's behalf.

Transactors: \~150 individuals from Poloos Council's existing community plus Cardano Catalyst's proposer/voter base, both already fluent in token-gated governance. Each self-claim is one distinct wallet, one transaction — well above the 15-distinct-wallet minimum at this award level.

Frequency: claims run on a rolling weekly onboarding schedule across the full pilot window, not a single bulk event — no single day exceeds 20% of total volume, and a minimum onboarding batch is scheduled every epoch to satisfy per-epoch floors. The one-time registry setup transaction is team-paid and excluded from the counted target per §5.2 — only the \~150 external self-claims count toward the ₳150 fee target at ₳1.00 each, clearing the ₳141 floor with genuinely external activity.

### How will you reach and onboard real users - and what evidence backs your channels?

rimary channel is direct outreach into existing token-holder communities already active on Discord/Telegram for supported chains — starting with communities adjacent to Poloos Council's existing user base, who already understand and use the exact workflow (docket, submit, vote, archive) Mishkan Protocol generalizes. That gives a warm first cohort rather than a cold launch.

Beyond that: Cardano Catalyst itself is an onboarding channel — its proposer and voter community is a natural first Cardano user base already fluent in on-chain governance. We'll also list in ecosystem directories (Gitcoin, chain-specific grant directories) once live on each chain, since public-goods-focused users specifically search those for this category of tool.

Evidence backing this: Snapshot and Tally reported user growth between 35–45% between 2023 and 2025, reflecting adoption that came from DAOs choosing them once a credible community used them, not paid acquisition

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

losest alternatives: Snapshot and Tally (off-chain/on-chain polling for token holders) and Aragon (plug-and-play DAO modules). All three are Ethereum/EVM-centric, offer polling only, and have no built-in dispute-resolution or petition workflow — communities bolt those onto Discord or forums manually. None natively support Cardano's eUTXO model or Stellar.

Mishkan Protocol wins on two fronts: (1) it is chain-agnostic by architecture, via a ChainAdapter interface, so a Cardano (or any new chain) integration is a scoped adapter, not a rebuild; (2) it treats disputes and petitions as first-class, tracked workflows alongside polling, matching how real communities actually govern — not just vote.

### Please provide details about the Technology Readiness Level selected for your existing product

Mishkan Protocol's core workflow — docket, submit, vote, archive, petitions — is live today, generalized from Poloos Council, an existing functioning token-gated governance app. Working EVM support (BNB Chain testnet, Ethereum Sepolia) is deployed, with Supabase-backed state and a live public interface.

Real wallets connect, real balance checks gate voting, and the docket/archive cycle runs end-to-end today, on EVM chains. This does not yet qualify as complete and qualified (TRL 8): chain coverage is EVM-only, multi-instance hosting isn't built, and no security audit has been performed. The core pattern is proven; broadening chain coverage and hardening it is the remaining work.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Mishkan Protocol's architecture separates the application from any single chain via a ChainAdapter interface: connectWallet(), getBalance(), signVote(), and isEligible() are implemented once per chain, while the docket, voting UI, archive, and petitions logic stay chain-agnostic. An EVM adapter already covers BNB Chain and Ethereum through this pattern.

For Cardano, a new adapter implements the same interface using CIP-30 for wallet connection and Blockfrost/Koios to read CIP-0113 programmable-token balances at vote time — this verifies a wallet holds the community's governance token and is eligible to vote. Voting stays gasless: a signed message off-chain (mirroring the EVM pattern), not an on-chain transaction, so casting a vote costs nothing.

This fits CIP-0113 specifically because programmable tokens are designed to carry exactly this kind of policy-enforced, verifiable balance — well suited as the eligibility signal for one-holder-one-vote governance. On-chain identity (CIP-0170) is the natural next layer: strengthening "one holder" against a single person controlling multiple wallets, which balance-checking alone can't solve. Application state stays off-chain in Supabase; only eligibility verification touches the chain

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Target market: DAOs, cooperatives, and civic-tech communities across BNB Chain, Ethereum, Stellar, and (via this grant) Cardano — specifically small and mid-sized token communities that need dispute resolution and petitions, not just simple polling, and can't justify building custom governance tooling.

Evidence of demand: off-chain governance tooling adoption has grown sharply industry-wide — Snapshot alone now serves more than 35,000 decentralized communities, and on-chain voting platform adoption tripled in a single year as DAOs moved away from ad hoc Discord/form-based decision-making. That demand is real but underserved on two fronts existing tools don't cover: most platforms are single-ecosystem (Ethereum/EVM-centric) and offer polling only, with no built-in dispute or petition workflow. Mishkan Protocol's own precursor, Poloos Council, is a live, functioning token-gated governance app already validating the core workflow (docket, submit, vote, archive) with a real community before this generalization. That existing usage is our clearest product-market-fit signal: the workflow works for a real token-holder base today, and this grant extends the same validated model, chain-agnostically, to Cardano

### Applicant name

Leslie Borerwe

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Core governance — reading the docket, submitting items, and voting — stays free permanently on every chain, including Cardano. That's a deliberate constraint: a fee on the act of voting undermines the legitimacy of the governance itself, so it isn't part of the model.

Revenue instead comes from optional, adjacent services: (1) managed/hosted Council deployments for communities that don't want to self-host, priced as a flat hosting fee rather than a cut of activity; (2) future optional features layered on top of core governance, such as advisory futarchy markets, which could carry a small fee only on that optional feature, never on baseline voting.

What keeps it running post-grant: the open-source core has low ongoing infrastructure cost (Supabase/hosting); hosted-instance fees from communities that value convenience over self-hosting are the primary path to covering that and funding continued development once grant funding ends.

### Programmable tokens (CIP-0113) - expected transaction count

150

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, Cardano support doesn't happen on any near-term timeline — as a solo founder chain expansion only gets built where there's dedicated time or funding attached to it, and Cardano currently has neither.

This grant would fund: (1) building and testing the Cardano ChainAdapter (CIP-30 wallet connection, CIP-0113 balance reads via Blockfrost/Koios) on preprod testnet; (2) integrating CIP-0170 identity as a second eligibility signal; (3) documentation and a working demo Council so Cardano-native communities can self-deploy without custom support.

At a high level, spend is founder development time plus Blockfrost/Koios API and testnet operating costs .

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Adoption phase runs as declared: one entry-ramp epoch after M1 mainnet delivery, then six floored 5-day epochs (35 days), within the 4-month program frame. All 150 declared self-claim transactions (150 ADA counted fees) come from external wallets paying their own fee, per the corrected usage model — no team-paid distribution counted.

Entry ramp: seed cohort (10-15 wallets from Poloos Council's community) self-claims on mainnet, validating the flow — roughly 15 transactions.

Epochs 1-6 (5 days each): rolling weekly onboarding from Catalyst's proposer/voter base and broader outreach, \~22-23 self-claims per epoch, spread across each epoch's 5 days (\~4-5/day), well under the daily cap. Each epoch independently meets its floor; registry setup stays excluded from counted totals.

Extra epochs, if earned by early delivery, extend the same rolling pattern rather than front-loading volume.

### How far along is the integration you're proposing, today?

TRL 7 - System prototype demonstrated in operational environment

### Programmable tokens (CIP-0113) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Mishkan Protocol is open-source, multichain infrastructure for community governance: token-gated polls, disputes, petitions, and proposals, decided one holder, one vote, regardless of balance size. Any community — a DAO, cooperative, or civic group — brings its own token and deploys its own Council, without adopting a new protocol token or handing custody of funds to an admin.

The problem: governance tools today are largely single-chain and tied to one ecosystem, forcing communities to either build custom tooling in-house or accept a rigid, closed platform. Smaller and emerging communities, who can least afford custom builds, are the most underserved.

For Cardano specifically: Mishkan Protocol's core is chain-agnostic by design, built around a ChainAdapter interface that separates the app from any single chain's wallet and balance-check logic. A Cardano adapter lets any Cardano-native project, DAO, or token-holder community deploy a working governance Council — polls, disputes, petitions — without waiting on a monolithic, single-chain governance platform. This brings real, working governance infrastructure to Cardano communities while keeping the protocol open source (MIT), self-hostable, and free on every core action: no fee to vote, submit, or read the public record.

Built for: DAOs, cooperatives, and civic or community groups that need transparent, self-hostable governance without launching a new token.

### Supporting links (repo, site, demo)

- https://mishkanprotocol2.lovable.app
- https://github.com/polooscouncil/mishkan-protocol

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

[MIT License ](https://github.com/polooscouncil/mishkan-protocol/blob/24429fd59d34c9a99cdbe3e8d1af568f1e02ac2a/LICENSE)Copyright (c) 2026 Leslie T.

[A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.](https://github.com/polooscouncil/mishkan-protocol/blob/24429fd59d34c9a99cdbe3e8d1af568f1e02ac2a/LICENSE)

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Cardano support does not exist yet — this is honest starting ground, not understated. What does exist is the architecture that makes adding it a scoped, well-defined task rather than a rebuild: Mishkan Protocol's ChainAdapter interface already separates wallet connection, balance verification, and vote signing from the rest of the app for every chain.

The Cardano-specific concept is formulated: read CIP-0113 programmable-token balances via Blockfrost or Koios to verify voting eligibility, connect via a Cardano wallet (CIP-30 standard), and sign votes off-chain in the same gasless pattern already used for EVM chains. No Cardano code has been written yet — this funding is what moves it from formulated concept to a working, tested adapter on preprod testnet.
