# PolicyKit: Modular Compliance for CIP-113 Tokens

> Composable compliance for Cardano programmable tokens: whitelist, freeze, and expiry as reusable CIP-113 policy bricks — the ERC-3643 of eUTXO.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1uxeqnhszgnckvq8ra47ahr9m5rf9t75xmtd9v8ttq6x23hgjw64qk`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-15T17:08:25.871000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

PolicyKit is led by a solo founder with an unusually strong fit for this exact problem.

Depth: \~10 years as a developer (since 2016), \~8 years in blockchain (since 2018), and a master's degree in blockchain. Over 2 years working exclusively on Cardano, including cross-chain development — fluent in eUTXO, Aiken, and Lucid Evolution. This removes the two things that usually sink CIP-113 work: the eUTXO and Aiken learning curves. The founder starts where most teams would finish month one.

Scarce skill: writing correct CIP-113 programmable-token validators is one of the rarest skills in the ecosystem — and the founder has already studied CIP-113 in depth and implemented a working reference base for it, which becomes the project's public design repo.

Institutional credibility: enterprise experience with Ford Motor Company, Siemens Energy and Banco do Brasil — a global automaker, an energy multinational, and a major bank. First-hand understanding of the institutional compliance buyer PolicyKit serves.

Delivery discipline: the scope is deliberately cut to what one experienced developer can ship in three months — inherit the Foundation's audited base, build only the net-new time-based policies, and prove the modular thesis on mainnet. Realistic, not optimistic.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: real, distinct external wallets — Cardano developers and community members using our public Compliance Sandbox on mainnet. Zero volume from wallets we control (the fund's golden rule); the Sandbox records each transaction's origin and a public Dune query shows the per-wallet distribution, so it's verifiable.

Why/how often: the demonstrator issues fictional, valueless receivable tokens. Each runs a full lifecycle — issue, whitelist, transfer, freeze/seize, expire, burn — \~6–9 on-chain txs per unit. We drive it via (1) a public "break-the-rules challenge" where the community composes policies and tries to bypass them, each attempt a real tx from a distinct wallet; and (2) open-source SDK adoption.

Target: \~250 successful mainnet txs and a 150 ADA fee target — about 35–40 receivable lifecycles from \~15–20 external wallets. Modest per wallet, comfortably above the 100 ADA floor, not inflated. We size it to what community usage can genuinely produce without committed pilots (which we don't claim): ambitious for a brand-new tool with no product today, yet conservative enough that we're confident of clearing it. Overperformance flows to the bonus pool.

### How will you reach and onboard real users - and what evidence backs your channels?

PolicyKit is developer-first, so we go where Cardano builders already are:

1) Open-source repo + SDK — the primary funnel. Developers discover, try, and integrate a free compliance library; adoption compounds organically.

2) A public "break-the-rules" challenge — we invite the Cardano community (Discord, forums, Aiken/Lucid dev circles) to compose policies in the Sandbox and try to bypass them on mainnet. Each attempt is a real on-chain tx from a distinct external wallet.

3) Founder ecosystem presence — 2+ years building on Cardano gives direct reach into these communities.

Evidence: these channels are active and reachable (Cardano's developer and Aiken/Lucid communities), and RWA demand is visibly arriving — this Pilot cohort already includes an RWA platform, and Libertum builds RWA on CIP-113 with the Foundation. Onboarding is a 5-minute quickstart plus weekly office-hours. We don't claim signed users we don't have.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, issuers rewrite a bespoke, monolithic compliance contract in Aiken per asset — costly and hard to audit. The Cardano Foundation's CIP-113 reference is our base, not a competitor: it's unaudited R&D with no policy library, SDK or UX. Libertum is a closed, vertical RWA product; Brale is stablecoin financial infrastructure — a layer we complement. ERC-3643/Tokeny ($32B) is EVM-only; Cardano has no open equivalent.

PolicyKit wins by being modular and reusable (compose whitelist+freeze+expiry on one token, no rewrite), by inheriting CF's audited base and adding the net-new time-based policies (Expiry, Lock-up) it lacks — plus an SDK and Sandbox — and by being open-source: an open standard any issuer can adopt, not a walled garden.

### Please provide details about the Technology Readiness Level selected for your existing product

Our "existing product" is the founder's body of Cardano work that PolicyKit builds directly on: 2+ years of production Cardano and cross-chain development, plus a CIP-113 programmable-token reference/study base already implemented and validated on public testnet. That base — Aiken validators exercising CIP-113's substandard, RegistryNode and withdraw-zero mechanics — is what we publish as PolicyKit's design repo. We rate it TRL 5: the core technology is validated in a relevant testnet environment, not just theorized. PolicyKit's productized library, SDK and Sandbox are the new integration, rated separately. We don't overclaim a live product we don't yet have.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

PolicyKit's on-chain layer is built as CIP-113 substandards on top of the Cardano Foundation's reference core — consumed as a pinned dependency, never forked. Each policy is the CIP-113-native pattern: three withdraw-zero (stake) validators — minting, transfer, and third-party-transfer logic — registered by credential in the core's RegistryNode. The core enforces that our validators fire on every relevant spend; we implement the rules.

All spec-dependent code (RegistryNode layout, withdraw signature, reference-input ordering) is quarantined in one cip113_adapter module, so CIP-113 churn — the standard is still pre-final — hits one place, not the whole codebase.

The pilot composes two heterogeneous policies on one token to prove modularity: a list-based Whitelist and the net-new time-based Expiry. Expiry needs no on-chain clock — it anchors to the transaction's validity-interval bound and fails closed on unbounded intervals, the correct eUTXO-native way to express "valid until".

Why it fits Programmable Tokens: this is the very mechanism the CIP-113 area exists to advance. The substandard model makes compliance modular and composable natively — impossible to express as cleanly on account-based chains — and building on the audited core concentrates our security surface on the small net-new piece.

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

Target market: teams issuing regulated or rule-bound assets on Cardano — RWA tokenization platforms, fintechs, receivables and private-credit issuers, fund administrators and stablecoin projects — plus the Cardano developers who build for them and need compliance primitives they don't have to write and audit from scratch.

Evidence of demand:

1) Proven elsewhere. ERC-3643 / Tokeny — the EVM standard for modular, embedded compliance — has $32B+ tokenized across 180+ jurisdictions. That is hard evidence that institutional issuers want composable on-chain compliance. Cardano has no open equivalent: the demand exists, the supply doesn't.

2) The Cardano Foundation is investing directly — it built and maintains the CIP-113 reference precisely because compliant-asset demand is arriving on Cardano. We fill the gap between that reference and a usable product.

3) Visible in this ecosystem, and in this round. Libertum is building RWA on CIP-113 with the Foundation, and this very Pilot cohort already includes an RWA/stablecoin tokenization platform. Platforms like these are exactly who needs a reusable compliance-policy layer — potential users, not competitors.

We are honest that this is early-stage: no product yet, and no pilots we can't back. Our evidence is market-level — a $32B proven category with an open Cardano gap — not vanity metrics; our own conservative on-chain usage target is stated in the Adoption section.

### Applicant name

Igor da Silva Bonomo

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Model: open-source core + commercial layer. The policy library and SDK are free and open — driving developer adoption and making PolicyKit the default compliance layer on CIP-113. We monetize the production needs around it: managed hosting of the Sandbox and registry indexer, premium audited policy modules (securities, vesting, jurisdiction), per-asset and per-compliant-transfer pricing, and enterprise support/SLAs.

Who pays: issuers — RWA/tokenization platforms, fintechs, funds, stablecoin projects — who need compliance to reach production and will pay to not rebuild and re-audit it.

Why usage continues after the grant: the open-source core compounds developer adoption at zero marginal cost, and every serious issuer eventually needs the audited, hosted, supported tier. It's the proven ERC-3643/Tokeny model — an open standard beneath a paid production layer.

### Programmable tokens (CIP-0113) - expected transaction count

250

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant, the open compliance layer Cardano is missing simply doesn't get built — no one is funded to spend three focused months, solo, productizing CIP-113 into a reusable library, SDK and Sandbox for the whole ecosystem, for free. The grant is the enabler that turns a proven need (a $32B EVM category with no Cardano equivalent) into working, open mainnet infrastructure.

Spend (50,000 ADA): \~84% the founder's 3 months of development (Aiken validators, registry indexer, SDK, Sandbox); \~4% an adversarial security review of the net-new validator; \~8% infrastructure (Blockfrost/Kupo/Ogmios/Postgres); \~4% real mainnet and seeding fees. The full external audit is a post-grant milestone, before any real-asset use.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By month 3, all public and verifiable:

1) Open-source repos: Aiken validators, TypeScript SDK, Sandbox app.

2) Net-new Expiry validator (Aiken) + green adversarial test suite (property + negative tests for bound-selection, unbounded-interval, double-satisfaction, datum-hijack). Proof: passing CI.

3) cip113_adapter pinned to a CF reference commit, Whitelist composed on top. Proof: preprod tx hashes.

4) Registry indexer (Kupo + Ogmios → Postgres): getCoveringNode / getHolderBalances.

5) SDK (Lucid Evolution): definePolicySet, issueAsset, buildTransfer, checkTransfer (via evaluateTx).

6) Compliance Sandbox on MAINNET (issue/transfer/check + per-holder balances).

7) MAINNET LIVE proof: a real receivable lifecycle on mainnet — issue, authorized transfer accepted, unauthorized/expired transfer blocked, freeze — with public tx hashes.

8) Public Dune dashboard: tx counts, distinct wallets, fees.

Plus a verified registry-isolation check before go-live.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Programmable tokens (CIP-0113) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Issuing a regulated or compliance-bound token on Cardano today means rewriting the same rules — whitelist, freeze, clawback, lock-up, expiry — from scratch, in a monolithic Aiken contract, for every single asset. It's expensive, error-prone, hard to audit, and demands rare smart-contract specialists. Even with the Cardano Foundation's new CIP-113 (Programmable Tokens) reference, there's a gap between the raw framework and something an issuer can actually use.

Who has this problem: teams tokenizing real-world assets, stablecoins, receivables, fund quotas, or any regulated asset on Cardano.

PolicyKit closes the gap. CIP-113 is modular by construction — a policy is a small validator registered by credential — so compliance rules can be reusable, composable Lego bricks instead of a bespoke contract per asset. We ship: (1) an open-source library of policy validators (whitelist, freeze/seize, and the net-new time-based Expiry & Lock-up), (2) a TypeScript SDK to compose and issue them, and (3) a self-serve Compliance Sandbox on mainnet. Issuers pick policies with checkboxes; we generate the CIP-113 logic — no Aiken required.

We build on the Cardano Foundation's reference (inherit, not compete). Think ERC-3643 — the $32B+ EVM compliance-token standard — but native to Cardano's eUTXO. That equivalent doesn't exist on Cardano yet.

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The PolicyKit integration is early-stage by design — this grant funds taking it from design to a working mainnet integration. Today we have, in our public design repo: the full architecture, the net-new Expiry/Lock-up validator design and Aiken skeleton, the SDK interface, and a documented spike-test plan for the CIP-113 reference-input mechanics. This is an experimental proof of concept (TRL 3): the concept and critical path are worked out and partially prototyped, but not yet validated end-to-end on a network. CIP-113 itself is not finalized/audited on mainnet, so no CIP-113 integration can be higher today — the grant exists precisely to build these to mainnet.
