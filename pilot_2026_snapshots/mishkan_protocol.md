# Mishkan Protocol

> Where Communities Deliberate

## Proposal Metadata

- **Status:** finalized
- **Revision:** 15
- **Proposer:** `stake1uxd9qla44kaftahx8r8z4q5lgyn0lcd8n7uytpjntdcph3qlgneay`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-17T20:52:36.122000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

LLeslie T. Borerwe\
[LinkedIn](https://www.linkedin.com/in/leslie-borerwe/)

This is a solo-founder team, and that's relevant context rather than a gap to hide: the founder is a self-taught developer, having transitioned into software from a non-technical trade background, now building exclusively in civic-tech and fintech for African and emerging markets.

Directly relevant to this proposal: the founder has already shipped Poloos Council, a live, functioning token-gated governance app — the exact docket/submit/vote/archive workflow Mishkan Protocol generalizes and proposes extending to Cardano. This isn't a concept being built from scratch for the grant; it's a working pattern being made chain-agnostic, which lowers delivery risk considerably compared to a net-new build.

The one area outside the founder's current track record is Cardano-native smart-contract work (CIP-0113's transfer-logic and issuer-logic scripts). Rather than overstating in-house capability the record doesn't yet support, the budget includes a dedicated line to hire a Cardano/Aiken smart-contract specialist for exactly this piece — their name and verifiable credentials (GitHub, prior audited Cardano work) will be added to this application once engaged, ahead of Month 1 delivery.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Mishkan Protocol generates hosted-instance revenue post-pilot (core voting/governance stays free permanently), we pledge 5% of net hosted-instance revenue back to the Cardano ecosystem — via Catalyst or a similar public-goods fund — for 24 months post-mainnet-launch, capped at 1x the grant amount received.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Redesigned around genuinely external, distinct-wallet-paid fees, not team-paid distribution: pilot members self-claim their CIP-0113 governance token via a "Join Council" flow — each submits their own wallet-signed claim and pays their own fee. The team never pays on a member's behalf.

Transactors: \~150 individuals from Poloos Council's existing community plus Cardano Catalyst's proposer/voter base, both already fluent in token-gated governance. Each self-claim is one distinct wallet, one transaction — well above the 15-distinct-wallet minimum at this award level.

Frequency: claims run on a rolling weekly onboarding schedule across the full pilot window, not a single bulk event — no single day exceeds 20% of total volume, and a minimum onboarding batch is scheduled every epoch to satisfy per-epoch floors. The one-time registry setup transaction is team-paid and excluded from the counted target per §5.2 — only the \~150 external self-claims count toward the ₳150 fee target at ₳1.00 each, clearing the ₳141 floor with genuinely external activity.

### How will you reach and onboard real users - and what evidence backs your channels?

Current base: Poloos Council has approximately 50 wallets today. Reaching 150 can't come from Poloos alone — the target splits across two channels with different, realistic conversion assumptions.

Poloos crossover: \~30% of the existing 50-wallet base (about 15 members) are expected to self-claim on Cardano — conservative, since a new wallet is real friction and not everyone will bother.

Primary channel: the remaining \~135 come from Cardano Catalyst's own proposer/voter community and broader outreach — users already holding Cardano wallets and already fluent in on-chain governance, removing wallet-setup friction entirely. This channel does most of the work, not Poloos crossover, which is why the target isn't capped near 50.

Evidence: Snapshot and Tally's growth came from users already active in a given ecosystem adopting a new tool, not cross-ecosystem migration — the same pattern applies here.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

losest alternatives: Snapshot and Tally (off-chain/on-chain polling for token holders) and Aragon (plug-and-play DAO modules). All three are Ethereum/EVM-centric, offer polling only, and have no built-in dispute-resolution or petition workflow — communities bolt those onto Discord or forums manually. None natively support Cardano's eUTXO model or Stellar.

Mishkan Protocol wins on two fronts: (1) it is chain-agnostic by architecture, via a ChainAdapter interface, so a Cardano (or any new chain) integration is a scoped adapter, not a rebuild; (2) it treats disputes and petitions as first-class, tracked workflows alongside polling, matching how real communities actually govern — not just vote.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL6— deployed and working on a public testnet, or live in another ecosystem, under realistic conditions. Mishkan Protocol's core workflow — docket, submit, vote, archive, petitions — is live and working today in another ecosystem: EVM, with working deployments on BNB Chain testnet and Ethereum Sepolia, real wallets connecting, real balance checks gating votes, and the docket/archive cycle running end-to-end under realistic conditions.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Mishkan Protocol separates the app from any chain via a ChainAdapter interface (connectWallet, getBalance, signVote, isEligible), one implementation per chain. An EVM adapter covers BNB Chain and Ethereum today; Cardano gets its own adapter using CIP-30 for wallets and Blockfrost/Koios to read balances.

How CIP-0113 governs the token: its core framework provides a shared programmable-logic-base custody address, an on-chain registry, and a global validation coordinator, deployed once and shared by all programmable tokens — our token registers here, not custom infrastructure. Actual behavior comes from a substandard: a pluggable transfer-logic script and issuer-logic script, invoked via the withdraw-zero pattern (stake validators triggered by 0-ADA withdrawals).

The transfer-logic script is invoked in every user transaction that spends the token — enforcing our rule (a wallet holds at most the configured balance, checked against the registry before authorization). The issuer-logic script governs permissioned actions only (initial minting; no seizure/clawback used) — not invoked on self-claims.

Join Council" is therefore a transfer under our declared substandard: the member's transaction spends from the programmable-logic-base address, the transfer-logic script validates it, and the registry confirms applicable scripts — exactly the transfer-fee category the Standard counts, run by the member's wallet.

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


- CIP-0113 registry-linked programmable token integration — adapting an existing audited reference substandard, registry registration, wiring the self-claim flow to actually invoke the transfer-logic script via the withdraw-zero pattern: 25,000 ADA (25%)
- Cardano smart-contract technical review — a named specialist auditing the CIP-0113 script integration specifically: 15,000 ADA (15%)
- Testing & QA — preprod validation of registry-linked transfer logic, test evidence bundle: 15,000 ADA (15%)
- Mainnet deployment — registry entry, initial mint under issuer-logic script: 5,000 ADA (5%)
- Infrastructure — Blockfrost/Koios, hosting across the adoption phase: 10,000 ADA (10% Community onboarding & outreach: 15,000 ADA (15%)
- Reporting & project management: 10,000 ADA (10%)

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Month 1 (evidence: GitHub commits, contractor engagement confirmed): select and integrate an existing audited CIP-113 reference substandard for the governance token; register the token in the CIP-113 on-chain registry; wire the existing self-claim flow to actually invoke the transfer-logic script via the withdraw-zero pattern — this replaces today's placeholder balance check with real programmable-token enforcement.

Month 2 (evidence: live preprod demo, testnet tx hashes, technical review sign-off): verify on preprod that the transfer-logic script correctly enforces the balance rule, registry lookups resolve correctly, and Blockfrost/Koios reads reflect real programmable-token state; named technical reviewer signs off on the script integration.

Month 3 (evidence: mainnet tx hashes, live URL, demo video): mint initial supply under the issuer-logic script; deploy the registry entry to mainnet; begin rolling self-claim onboarding (detailed in M2/adoption-phase outputs).

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

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
- https://www.linkedin.com/in/leslie-borerwe/

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

Technology concept formulated.  What exists is the architecture that makes it a scoped task: Mishkan Protocol's ChainAdapter interface already separates wallet connection, balance verification, and vote signing per chain, and the CIP-0113 mechanics this integration depends on (programmable-logic base custody, registry-linked transfer/issuer scripts, withdraw-zero invocation) are understood and specified in the architecture answ
