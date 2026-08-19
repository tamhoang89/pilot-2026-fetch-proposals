# Selkie: Stablecoin Payments to Any Social Handle

> Send USDM or USDCx to an X or Telegram handle. The recipient needs no wallet, no seed phrase and no ADA — they sign in with the account they already have, and the money is there.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 16
- **Proposer:** `stake1u9n50ajq5u4sfwec6l8uhx8hswd3rd6anj3lvnzuz3c656sxlzkg4`
- **Funding requested:** ₳90,000
- **Last finalized:** 2026-08-19T17:45:23.478000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Selkie is a two-person team that has already built and shipped the product on Stellar and is now bringing it to Cardano.

**Emmanuel Akalo — Engineering Lead**\
GitHub: [https://github.com/nuelose](https://github.com/NueloSE)\
Built most of the existing codebase, including the escrow contract, chain adapter, API and web app.Will lead the Aiken validator and Cardano adapter.

**Oshioke Salaki — Engineer and promoter**\
GitHub: <https://github.com/Oshioke-Salaki>\
Built persistent storage, multi-platform handle support and request idempotency. He will own the claim flow and CIP-0170 attestation integration, onramp and offramp. Owns product direction, market research, creator/community outreach, adoption and partnerships. He will lead the initial Cardano rollout.

Our work is public at <https://github.com/selkiepaylabs/selkiepay>. The product is running end to end on Stellar testnet with a tested escrow contract, chain-agnostic core, web app, API, database and X bot.

**Skills gap:** Aiken/Plutus and Cardano eUTXO expertise. We plan to engage a Cardano/Aiken specialist to review the validator and provide security guidance during implementation.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge to return ₳45,000 (50% of the grant) to the Cardano treasury from revenue. Once Selkie's cumulative net revenue from Cardano-settled payments exceeds ₳90,000, we will direct 10% of subsequent net Cardano revenue to the treasury until ₳45,000 has been returned. If we never reach that threshold, no repayment is due.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: the people being paid. A creator or community funds a payout, and each recipient claims it from their own wallet - that claim is both the stablecoin movement and the CIP-0170 attestation. Recipients then hold a verified stablecoin and transact onward.

Cadence: campaigns run several times weekly across the window, deliberately spread. No single day carries more than 20% of our total, and we hold every

epoch floor rather than finishing in a burst.

The numbers: 850 claims at roughly 0.45 ADA for a script spend carrying a native asset and attestation metadata gives our ₳380 identity target. Stablecoins adds onward user-paid transfers to those claims - 1,250

transactions at about 0.43 ADA, giving ₳540.

Why it is genuine: every claim requires a distinct, verified social account, so volume cannot be reproduced across wallets we control. We compensate no one for transacting and run no transact-to-earn scheme - the money is always the sender's, and we only carry it. Our operator wallet is declared under §4.1 and its fees are excluded; recipients pay their own claim fees, which is what makes the resulting usage countable.

### How will you reach and onboard real users - and what evidence backs your channels?

Our channel is the surface the product already lives on. Selkie's X bot is

built and tested: payment happens by replying in a public thread, so

distribution and product are the same action. The payment can happen directly in the public thread where the recipient was already engaged, turning the payment itself into a distribution event.

Onboarding has no install step: the recipient signs in with the account that

was mentioned and their wallet is created in that moment. Because nothing can

be claimed without a new user signing in, every transfer onboards exactly one

person. Acquisition cost is the sender's motivation, not our marketing budget.

We reach creators directly: they already do this by hand and know what it costs.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/vszgUFJ251U

### Who else solves this today - competitors/alternatives, and why does your approach win?

Paying someone who has no wallet is mostly solved today by not solving it.

Creators run a form, collect addresses in a spreadsheet and send manually,

which is slow and silently drops everyone without a wallet. Tip bots work but

are closed custodial loops. Airdrop tools need addresses you do not have.

Cross-border, remittance to Sub-Saharan Africa averages 8.46% and 14.99% via

banks, while Wise or Lemfi require the recipient to install, register and pass

KYC first. On Cardano, verified stablecoins are live but nothing can pay a

handle.

All of them need the recipient to already hold something: an address, an

account, an app, a wallet. Selkie needs only the social account they already

use. That is the step where every alternative loses people.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 6. Selkie is a working MVP on a public testnet, running realistic flows with test wallets. Working today on Stellar testnet: a handle-escrow smart contract in Rust, with its own test suite; a chain-agnostic core exposing a four-method adapter interface; a Next.js application; an API with Postgres persistence and account keys sealed before storage; and an X bot.

The complete flow runs end to end: sign in with Google or X, fund a wallet, pay a handle that has no account, and the funds release the moment that person signs in. Sender refund after expiry is implemented and tested.

We do not claim TRL 7 yet: Cardano mainnet deployment and real-user transactions are part of the proposed work.

Evidence: [github.com/selkiepaylabs/selkiepay](http://github.com/selkiepaylabs/selkiepay)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Funds are locked at an Aiken validator script address. The datum carries the sha256 of the recipient's handle, the sender's key hash, an expiry slot and the asset held; the redeemer selects Claim or Refund.

Claim requires a signature from Selkie's oracle key attesting a verified login, and that the output pays the recipient's address. The oracle can only release to a proven owner - it can never redirect funds to itself, alter an amount, or block a refund. Refund: after the expiry slot the sender's signature alone unlocks, so money is never stuck. The held value is a verified stablecoin (USDM or USDCx) as a native asset in

the locked UTXO. Every Cardano UTXO carries a min-ADA requirement, so the sender's transaction includes that minimum, which Selkie sponsors - the recipient still needs nothing.

On claim, the same transaction writes a CIP-0170 attestation binding the handle to the recipient's new wallet, making "this wallet proved control of this

handle" publicly verifiable rather than a row in our database. The claim is signed and submitted by the recipient's own wallet, not ours.

This fits eUTXO directly: an escrow is a held-value problem, and eUTXO expresses it natively - money sits in a UTXO governed by a validator, not as a mutable balance in a contract we administer.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Selkie serves anyone who needs to pay a person who has no wallet. One primitive, two markets.

The immediate market is creators and communities paying out at scale on X. An influencer rewarding followers, a live Space distributing to attendees, a project paying bounties, a community running a payout. All hit the same wall: they can reach 50,000 people by handle, but can only pay the few who already hold a wallet. The current workaround is a form, a spreadsheet and a week of manual sends, and it silently excludes everyone without a wallet to give.

Selkie makes it one reply. We serve this market on day one with the surface we have already built, and the sender already has the money and the recipient relationship; Selkie removes the wallet requirement in between.

The market it opens into is cross-border payments. Nigeria received $21.8bn in diaspora remittances in 2025, at an average cost to Sub-Saharan Africa of 8.46% against a 3% SDG target, and 14.99% through banks: at the regional average cost, that would imply roughly $1.8bn against Nigeria's annual remittance volume. Sub-Saharan Africa took in over $205bn in on-chain value in the year to June 2025, up 52%, with stablecoins now around 43% of regional volume and over 8% of transfers under $10,000. Demand for stablecoin payments here is established. The first mile is what remains unsolved.

Same contract, same claim flow. Our existing test usage validates the payment primitive, cross-border payment is where it scales.

### Applicant name

Emmanuel Akalo

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The sender pays, with two types of sender.

Creators or communities funding payouts pay a fee on the total distributed. It is a commercial transaction for a distribution they currently handle manually. Individuals sending across borders pay a percentage below the 8.46% regional average and 14.99% bank average. Direct stablecoin settlement gives us room to price below traditional remittance costs while retaining margin. Cash-out adds an FX spread once a payout partner is integrated.

Usage is recurring: creators run campaigns and Spaces regularly; family support is often monthly. The grant funds infrastructure and initial adoption, while the underlying payment behaviour repeats without us manufacturing demand.

The model also compounds. Every first-time claim can create a Cardano wallet for someone who had none, turning a recipient into a potential future sender. Revenue grows with real payment activity and continues after the pilot.

### On-chain identity (CIP-0170) - expected transaction count

850

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant Selkie stays on Stellar. We are a small team, a second chain is a deliberate investment we cannot make speculatively, and eUTXO plus CIP-0170 is the largest single piece of new engineering in front of us.

What the funding builds, none of which exists today:

- The Aiken escrow validator and its test suite
- The Cardano adapter implementing our existing ChainAdapter interface
- CIP-0170 attestation on claim, via signify-ts
- Verified stablecoin settlement in USDM and USDCx
- Mainnet deployment, transaction labelling, and specialist Aiken review

Roughly 60% engineering across the three of us, 20% specialist Aiken review, 20% launch and creator onboarding. None of it covers completed work: the Stellar build was funded by us.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of the window Selkie is live on Cardano mainnet, and a person can be

paid at their X handle without holding a wallet.

Deliverables:

1. Aiken handle-escrow validator on mainnet, with tests covering the claim, refund-after-expiry and oracle-authorisation paths.
2. A chain-cardano adapter implementing our existing ChainAdapter interface, registered and serving the live product.
3. Claim flow signed and paid by the recipient's own wallet, writing a CIP-0170 attestation binding handle to wallet in the same transaction.
4. Settlement in verified stablecoins: USDM and USDCx.
5. Declared footprint published: script hash, registered message tag, and operator wallets by stake key.
6. Live product URL, with the X bot running against mainnet.
7. Release notes, a technical walkthrough video, and a test evidence bundle: checklist, bug log, security note.
8. Live demo and Q&A at Demo Day.

We intend to deliver ahead of the deadline to earn additional adoption epochs.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

380

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

To receive money on Cardano today you need three things first: a wallet, a recovery phrase you must never lose, and ADA to pay the fee. Three obstacles stand between a person and money that is already meant for them.

That cost falls on the receiver, not the sender. A parent being sent money from abroad. A freelancer paid across a border. A community member owed a payout. Each is asked to become a crypto user before they can be paid at all, and most simply don't — the money stops there.

Selkie removes all three. You send stablecoins to a social handle — an X or Telegram username — and the funds are locked in an on-chain escrow against a hash of that handle. They are held by the contract, not by us. When the recipient signs in with the account they already own, that ownership is attested on-chain and the funds are released to a wallet created for them in

that moment. They never chose a wallet, never wrote down a recovery phrase, and never had to acquire ADA to be paid.

On Cardano this settles in verified stablecoins — USDM and USDCx — and the handle-to-wallet binding is written as a CIP-0170 attestation, so "this wallet

proved control of this handle" becomes publicly verifiable rather than something users take on our word.

The product is real and running. Selkie works end to end on Stellar testnet today, built on a chain-agnostic core that isolates all chain-specific code in a single adapter. This proposal brings it to Cardano mainnet.

### Supporting links (repo, site, demo)

- https://selkiepay.com
- https://github.com/selkiepaylabs/selkiepay
- https://youtu.be/vszgUFJ251U

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

### Stablecoins - expected transaction count

1250

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

540

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 2. The architecture is specified; no Cardano code exists yet.

What exists is the seam it plugs into. Our ChainAdapter interface(ensureAccount, getBalance, send, claim) is already implemented and working in our Stellar adapter, so the contract this integration must satisfy is

established rather than theoretical. The product, API, front end and bot all talk to that interface and need no changes to gain a second chain.

What does not exist: the Aiken validator, the Cardano adapter, and the CIP-0170 attestation path. We treat the escrow as new work rather than a port - eUTXO

differs enough from the account model our current contract targets that translating it would be the wrong instinct.

This grant funds exactly that gap.
