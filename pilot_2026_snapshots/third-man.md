# THIRD-MAN

> Trust the deal, not the stranger.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1u9zkjnsdmkway764336rl8gj2kacdnwnz0g6scp3nn847vga6a5kc`
- **Funding requested:** ₳190,000
- **Last finalized:** 2026-08-21T15:34:12.704000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

3rd Man is built and led solo by me, Paul Kaberere I'm the project lead and sole developer across the whole stack. That covers the Rust/Axum backend (auth, KYC, agreements, negotiation, collateral, escrow, disputes, points, ledger), the React/Vite/TypeScript frontend (wallet integration, agreement wizard, milestone delivery, arbiter console, governance panel), and the on-chain Aiken (Plutus V3) validator, including the Pallas-based Rust transaction builder wired to Cardano Preprod testnet.

We've already budgeted for a third-party smart contract security audit ahead of mainnet deployment this is a precondition for the M1 milestone, since the validator will be holding real user funds. I've reached out to Invariant0, the Cardano audit team with a scoping email covering the validator's architecture, its current Preprod-tested status, and our 3-month mainnet timeline. I'm now waiting on their reply about availability and cost before we can lock in a schedule. I'll also bring on a legal/compliance advisor for Kenyan financial regulation on the escrow/custody model, on the same near-term timeline, once I've identified specific candidates.

Links: Paul Kaberere — [github.com/paloxmah0](http://github.com/paloxmah0)

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge 2% of net transaction fee revenue back to the Catalyst treasury, activating once monthly fee revenue exceeds 500 ADA ensuring the give-back reflects genuine, sustained usage, not pilot-phase test activity. This continues for 12 months after the threshold is first met, then reviewed. Kept modest and threshold-gated since our fee-based model is still unvalidated at this stage.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Our first users are Nairobi freelancers and secondhand-goods sellers doing real P2P deals reached first through the Cardano NBO Blockchain Centre's existing Web3 community, then Nairobi's WhatsApp/Facebook Marketplace trading groups, where escrow demand is already proven by competitors like Shikilia and TrustPay. This is a deliberately global product proven locally first: the same non-custodial mechanic applies anywhere P2P trust is a problem, and Kenya is where we validate it before extending to other mobile-money markets. Each user registers on-chain identity (CIP-0170) once per wallet this sets the 150 target, matched to our realistic first-cohort size across these channels. Oracle transactions come from delivery/condition confirmation: not every escrow needs one, since simple pay-on-confirmation deals settle peer-to-peer, but staged/freelance work and delivery-dependent sales the higher-friction deals oracles exist to solve do, at roughly 1.3 oracle calls per active user across the adoption window, giving 200 total. Both targets sit modestly above floor rather than being padded, because they're built from named, already-warm channels, not a generic marketing funnel.

### How will you reach and onboard real users - and what evidence backs your channels?

We launch in Kenya first, then extend to other mobile-money markets once the model is proven. Our first channel is the Cardano NBO Blockchain Centre's existing Nairobi Web3 community a warm, already-assembled group, not a cold audience. Beyond that, we're targeting Nairobi's existing secondhand/freelance WhatsApp and Facebook Marketplace trading groups directly the same channels TrustPay and Shikilia already use to reach this exact user base, which tells us the channel converts. Once usage is proven in Kenya, the same non-custodial model ports directly to other mobile-money economies (e.g. Nigeria, Ghana, the Philippines) with the same trading-group and community-first playbook. We do not yet have signed letters of intent, and we are stating that plainly rather than overclaiming

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

This space has real answers already, locally and globally: Kenya Escrow, TrustPay KE, eConfirm, and Shikilia offer M-Pesa escrow for Jiji/WhatsApp/freelance deals, and globally [Escrow.com](http://Escrow.com) and PayPal's buyer protection serve the same need in card/bank-based markets. They prove demand exists — but every one is custodial: your money sits in a company's account, and you're trusting that business not to misuse, freeze, or lose it. That's the exact "just another middleman" problem we're removing. 3rd Man is non-custodial: funds sit in a Cardano smart contract tied to the user's own wallet, so no team, including ours, can access or override them the same advantage anywhere in the world. Users switch for the same reason people move from trusting a company to trusting code.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 5 – Validated on Cardano Preprod testnet. Backend (Rust/Axum): CIP-8 wallet registration (did:cardano), KYC tiers, agreement drafting, OTP invites, dual signing, collateral, escrow init, milestone proof/review with auto-dispute, arbiter/oracle resolution, governance points, ledger mirror. Frontend (React/Vite/TS): CIP-30 wallet connect, contract viewer, milestone delivery, arbiter console. On-chain (Aiken/Plutus V3): validator (hash b8e74f7bf6e126055bab145507e59c3bf8fb40059c2239d772ecfe92, addr_test1wzuwwnmm7msjvp2m4v292pl9nsal376qqkwzywwhwtk0aysufmxqn) handling Deposit, ClaimUnit, SubmitProof, ReviewProof, RaiseDispute, ArbiterResolve, Refund. Txs via Pallas (no Lucid), submitted via Koios. End-to-end flow tested on Preprod; Typhon wallet signing confirmed.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The system splits into on-chain and off-chain layers: the off-chain layer (Rust/Axum backend) handles everything that doesn't need trustlessness — wallet-native auth, negotiation, notifications, dispute routing — while custody of funds lives in the deployed Aiken Plutus V3 validator, not the backend. Wallet-native auth uses CIP-8 COSE_Sign1 parsing and Ed25519 verification, so users authenticate by signing with their Cardano wallet, with identity as did:cardano:

 derived directly from the wallet — the right fit for on-chain identity (CIP-0170) since the DID is already anchored to a cryptographic signature, not a database record. Transactions are constructed with Pallas (Rust) — real Babbage-era CBOR built and submitted server-side via Koios, with no browser-side or Lucid dependency — keeping the trust-critical transaction logic inside the same audited codebase as the rest of the backend. The validator itself handles Deposit, ClaimUnit, SubmitProof, ReviewProof, RaiseDispute, ArbiterResolve, and Refund natively, so dispute resolution — exactly where oracle condition-verification is needed — is enforced on-chain via Ed25519-verified oracle-signed data, not bolted on after the fact. Config carries the deployed script hash and address as first-class values the backend points at, consistent with non-custodial design and Cardano's eUTXO model.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The P2P trust gap is global anywhere a buyer and seller don't fully know each other, someone has to go first. It's sharpest in mobile-money-driven, informal-commerce economies: Kenya's informal sector alone is roughly 18.1M people (\~84% of employment), and the same pattern  heavy mobile money use, thin formal escrow, large informal/gig commerce repeats across Sub-Saharan Africa, South/Southeast Asia, and Latin America. We launch in Kenya first: Nairobi freelancers and secondhand-goods sellers trading over WhatsApp, where at least four M-Pesa escrow products already operate itself demand evidence. Kenya is our proof market; the model extends to any mobile-money-first market.

### Applicant name

PAUL NGIGI KABERERE

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue is a small % fee taken on release of escrowed funds the same model TrustPay, Shikilia, and [Escrow.com](http://Escrow.com) already validate as accepted globally for this exact service. The difference is where that fee lives: settlement happens on-chain, so network fee volume from 3rd Man transactions is directly, verifiably measurable on Cardano, not something we can inflate in a report, regardless of which market it comes from. Usage should persist post-pilot because the underlying need doesn't expire in any market every new P2P deal recreates the same trust problem and switching to non-custodial escrow is a one-way improvement: once someone stops worrying about a company holding their money, they don't go back. The pilot in Kenya proves the fee-per-transaction economics at real volume before we extend the same model to other mobile-money markets

### On-chain identity (CIP-0170) - expected transaction count

150

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding takes the validator from unit-tested code to a deployed, integrated, testnet/mainnet-verified escrow flow  the one piece not yet proven live. Without it, the completed off-chain system has nothing real to orchestrate against. Funds go to: validator deployment and integration testing, wiring the backend's escrow/collateral/dispute modules to real on-chain transactions, oracle and CIP-0170 integration work, and onboarding real users in Nairobi to generate usage evidence. It does not fund already-completed off-chain wor

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By end of the 3-month window: (1) Aiken escrow validator completed, audited for basic logic errors, and deployed to Cardano mainnet, holding funds in a script address tied to user wallets, not a company account. (2) CIP-0170 on-chain identity integrated into the existing auth flow users register their DID on-chain via wallet signature (CIP-8 verification already built). (3) Oracle integration live for delivery/condition confirmation on staged and delivery-dependent deals. (4) Existing Rust/Axum backend (agreements, collateral, escrow, dispute modules) fully wired to the deployed validator, replacing placeholder config with real script hash/address. (5) At least one real user completes a full escrow deal end-to-end on mainnet create, pay, lock, confirm, release  repeated across independent runs. (6) Public repo, release notes, and technical walkthrough video published.

### Oracles - expected transaction count

200

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

100

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

We're building 3rd Man, an automated escrow system that solves a problem most people doing business with a stranger have faced, anywhere in the world: nobody wants to pay first, and nobody wants to deliver first. If you're buying something secondhand, hiring a freelancer, or paying for work in stages, you're stuck in a standoff. The usual fix is finding someone both sides trust to hold the money until the deal is done a "third man." It works, but only if you know someone trustworthy who's willing to do it, and even then they could be slow, unavailable, or dishonest. 3rd Man replaces that person with a smart contract on Cardano holding payment until both sides confirm the deal is done, except it can't be bribed and can't run off with the money. You create a deal, share a link over any messaging app, and pay through whichever rail is native to your market mobile money like M-Pesa, or card/bank rails elsewhere. Funds lock automatically once payment lands, and release once the condition is met, with a real dispute process if something goes wrong. The trust gap this solves exists globally, but is sharpest in mobile-money, informal-commerce markets. We launch first in Kenya, where the gap is easiest to prove, then extend to other mobile-money markets worldwide.

### Supporting links (repo, site, demo)

- https://github.com/paloxmah0/third-man-protocol

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

300

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

Oracles (TRL 3): the oracle endpoint (POST /disputes/:id/oracle) exists and feeds arbiter decisions as non-fatal evidence; the Aiken validator's ArbiterResolve action already supports oracle-signed data via Ed25519 verification. Remaining: wiring a real decentralized oracle (Charli3 or Orcfax) for delivery confirmation, and moving oracle data on-chain as a required release input, not just off-chain arbiter evidence. On-chain identity CIP-0170 (TRL 4): did:cardano:

 generation from wallet signatures works, with KYC tiering and per-field privacy preferences already enforced. Remaining: full CIP-0170 DID document compliance (resolution endpoint, verification methods, service endpoints) and on-chain attestation anchoring via CIP-10 metadata transactions.
