# Exura: self-custodied yield beyond Cardano

> Deposit USDCx from your own Cardano wallet, earn yield on curated stablecoin vaults without the EVM hassle, receive USDCx back in minutes.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 13
- **Proposer:** `stake1uxqs8hmgwkqza9gp7zqh8sqx5entwhudla5rwc39ufw9anq5set5u`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T16:19:26.014000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

One person builds this, and built what it stands on. Javier Acosta, solo applicant, full-time on the integration through the program window.

The claim to check is the work, not the title. The verification contracts are mine: Solidity, deployed and exercised on Sepolia under a 78-test suite, MIT: [cip8-verifier](http://github.com/ExuraLabs/cip8-verifier). Also Exura itself: a composable indexer that reconstructs and tracks DeFi positions across full Cardano mainnet history, nine protocol integrations, a chain-derived price oracle, and the API and dashboard above them. Its data relay, [Hecate](https://github.com/ExuraLabs/hecate), is public too. I contribute upstream to core projects this work depends on, most recently to [Pallas](http://github.com/txpipe/pallas/pull/792) and [Kupo](http://github.com/CardanoSolutions/kupo/issues/194).

Background and history: [Linkedin](https://linkedin.com/in/javieracost).

With one participant the scope is undivided: the Cardano-side transaction construction and CIP-8 binding, the EVM contracts and account provisioning, the vault integration, the deposit and exit flows in the dashboard, and running the measurement window.

Outside that, one engagement is already in place. Veridise quoted a security audit and holds a pencilled slot for late October; they previously audited [SCL](https://github.com/get-smooth/crypto-lib), the elliptic-curve toolkit the verification layer builds on, so the budget buys review depth rather than ramp-up.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

No repayment terms or revenue share. We give back the primitive: the verifier [contracts](http://github.com/ExuraLabs/cip8-verifier) are public and MIT licensed, delivered before submission and reusable by any Cardano project without us. Any audit report we commission publishes there too, whatever our numbers say. Infrastructure anyone can build on is worth more here than a revenue-share promise.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: the depositor, from their own wallet. The binding attestation moves no USDCx, so we do not count it. What counts is the deposit, a USDCx burn we construct and the user signs, one per deposit. Exits and later instructions are signed messages, not transactions, and an EVM-side arrival produces no Cardano activity.

How often: this is a savings position, and people add to savings. We assume three to five deposits per user across the window, and each vault we list adds another occasion to deposit rather than another way to split one.

The declared ₳375 is 1,113 burns at the measured 0.337 ADA. At four deposits per user that is about 280 depositors, at five about 225, from a launch cohort we expect in the low hundreds through our own announcement and word of mouth. For scale, 134 distinct wallets ran this corridor unprompted in the last 60 days with no product asking them to.

No user will be paid, reimbursed or fee-subsidised to generate counted activity, our own wallets are declared and excluded, and we onboard in waves so the count comes from steady use rather than a launch-day spike the daily cap would discard.

### How will you reach and onboard real users - and what evidence backs your channels?

Onboarding is three steps: connect the wallet they have, sign to bind, sign the deposit.

The first fourteen days after go-live:

Days 1-2. Announce the dashboard on our channels and in the Cardano venues its audience reads, with the walkthrough video.

Days 3-5. Deposit flow open to a first wave, office hours, mainnet activity published as it lands.

Days 6-10. Second wave, with whatever the first stumbled on fixed.

Days 11-14. Third wave, first numbers published, same material into Catalyst's calls.

Waves are deliberate: the daily cap discards a launch-day spike while per-epoch floors reward steady cadence, so onboarding is paced to the measurement structure.

Reach we can show: our own account peaks at 600-800 impressions on a single day and about 2K in a month, on rare and mostly technical posts. The audience is checkable on-chain: 134 distinct wallets burned USDCx through xReserve in the last 60 days, unprompted by any product.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

A custodial exchange pays a rate and holds the keys. It is where ADA holders seeking a return on dollars go.

Cardano's own venues keep the keys but have little room: Liqwid's USDCx market pays about 5% on roughly $161k, and free stablecoin liquidity chain-wide is about $2.6M. The rate holds until you supply into it and your deposit becomes most of the pool.

Doing it yourself keeps the keys, at the cost of a second wallet, a seed phrase, gas and a bridge choice. Most people never start, and the EVM managers serving those who did (Toros, dHEDGE) reach nobody here.

**We remove the second wallet without taking the keys**: a contract that verifies Cardano signatures on-chain lets a Cardano key own and drive the account, so the user reaches a deep venue and can revoke us alone.

### Please provide details about the Technology Readiness Level selected for your existing product

Exura runs in production on full Cardano mainnet history: an indexer that reconstructs and tracks DeFi positions, nine protocol integrations, a chain-derived price oracle, and the API and dashboard above it. None of it is simulated.

  What it is not yet is announced. The dashboard is live but tracks a limited set of accounts while we finish the surface, so a strict reader could call it 6, and we would not argue. The engine has been running on real chain data for a long time; the public front is what remains.

  Nothing here depends on that being finished first. The integration lands on the same indexer, pricing and dashboard, which is why one person can deliver it in three months: the hard part that usually eats a pilot, tracking and valuing positions across a whole chain, already runs.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Two chains, and the user's Cardano key is the root of authority on both.

On Cardano: the user signs a CIP-8 message with their CIP-30 wallet, and that binding is anchored on Cardano mainnet as a metadata attestation their own wallet pays for, verifiable by anyone. Deposits from Cardano are ordinary Cardano transactions, USDCx burns through Circle's xReserve that we construct and the user signs. Later instructions, the exit included, are signed messages, not transactions, and returning USDCx is minted to the Cardano address fixed at setup.

On the EVM side: a smart account the user alone owns, driven by a contract that verifies Ed25519 CIP-8 signatures natively, so the Cardano key is the owner in fact, not by proxy. Our execution permission is narrow, capped, readable on-chain before anyone deposits, and revocable by the user without our cooperation. The contracts are not upgradeable, which is the point: a custody promise that can be edited later is not a custody promise.

Why this fits the area of interest: the steps that touch Cardano are genuine transactions paid by the user's own wallet, the binding and the deposit burn, and those are the only ones we count. Someone entering from the EVM side produces no Cardano activity, and we claim none. The asset moves on the issuer's own rail rather than a bridge of ours, adding no trust assumption the stablecoin does not already carry, and the binding holds because a Cardano payment credential cannot be rotated away.

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

The market we can measure is the smaller one. About $44M of USDCx circulates on Cardano with little to do here: Liqwid's USDCx market is roughly $161k, free stablecoin liquidity chain-wide about $2.6M, so a serious deposit becomes most of the pool.

The larger market is the dollars that are not here yet. Billions of ADA are held, on exchanges and in wallets, by people who keep money in dollars somewhere too, and none of it has a reason to arrive here. Someone who trusts this chain enough to hold serious value in its asset would keep dollars here too, if that did anything. Dollars that come arrive as **newly minted USDCx**, not as ADA sold into stablecoins. We cannot size that group and would rather name it than pad it: demand with nowhere to go leaves no trace. It goes where it is met, which so far means a custodial exchange or another chain.

The circumstantial case is the ratio: Cardano DeFi holds around $62M against an asset worth about $6B, **roughly one dollar in a hundred**. Either ADA holders do not want their money working, or what is on offer does not fit what they hold. Dollar savings products elsewhere hold billions, which makes the second likelier.

**We do not claim product-market fit yet.** The pilot is the test; deposits settle it. What exists is the machinery and the audience: contracts deployed and exercised on testnet, and a portfolio dashboard live across Cardano mainnet history, where these users already arrive.

### Applicant name

Javier Acosta

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Users pay 0.5% per year on what sits in their account. **No entry fee, no exit fee, no performance fee.** We collect it through one narrow permission, capped and pointed at a fixed address, readable on-chain before anyone deposits.

At pilot scale that revenue is small, and we would rather say so. This is the simplest product on the menu, with the simplest fee: one stablecoin position, one flat rate. More involved strategies follow with their own schedules, and the rail carries vaults other than ours. The pilot's job is demand and capability; the model earns on the menu that follows.

**Nothing here depends on grant money.** The account and vault sit on public infrastructure and keep paying whether we are funded or not, the user can exit or fire us without our cooperation, and our side runs on infrastructure we already operate for Cardano DeFi, so one more account costs almost nothing.

Usage continues for the ordinary reason: the position pays, and leaving costs one signature.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without funding it still gets built, slower and between other work, and reaches users with no external review of the contracts holding their permissions. That is the version we would rather not ship.

An independent review is the largest line in this budget and the reason the ask is the size it is. We will commission as much of it as the funding supports, and we will not promise a scope that an exchange rate can take away.

Three months to mainnet is full-time work, and the infrastructure is not cheap either: chain followers, indexes and archives on Cardano, provisioning and gas on the EVM side, through the measurement window.

The build tranche is sized to deliver M1. Everything beyond that, review included, follows the receipts.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Verification contracts deployed to ethereum mainnet, source verified against a tagged commit in the public repository.
2. The binding live on Cardano mainnet: registered message tag, published attestation format, declared footprint.
3. Deposit and exit shipped in the product: bind, burn, the vault position, and the return to the Cardano address fixed at setup.
4. Mainnet transaction hashes from real users' own wallets rather than ours: one complete run of that flow, plus independent repeats by other users.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Over $40M of USDCx circulates on Cardano, with little for it to do. Cardano DeFi is real, but ADA-denominated at heart, so dollar savings is thin here. Mature stablecoin products (sUSDS, sGHO, sUSDe) live on other chains, behind an EVM wallet, a seed phrase, gas, and a bridge decision most Cardano users will never make alone. Stablecoin capital here either sits idle or leaves through a custodial exchange.

Exura builds the leg in between: a Cardano-native route from wallet to stablecoin yield and back, where the user keeps their own keys and never creates an EVM wallet.

1\. One CIP-30 signature binds their wallet to a smart account **only they own**. A contract verifies that Cardano signature on-chain, natively. Our permission over the account is narrow, and the user can revoke it alone.

2\. One ordinary Cardano transaction, a USDCx burn through Circle's xReserve that we build and they sign, moves the USDCx in. We run no bridge and never hold the funds.

3\. The USDCx earns yield in curated stablecoin vaults, tracked in Exura's live dashboard next to their Cardano positions.

4\. Exit takes one more signature. The USDCx returns to their own Cardano address, fixed at setup and unchangeable by us, in 15 to 25 minutes.

It is for Cardano holders who own USDCx and want it earning without handing it to anyone, and for ADA holders who want a dollar-denominated position instead of more ADA exposure. A stablecoin vault is the first listing on this rail, not the whole of it.

### Supporting links (repo, site, demo)

- https://exura.org
- https://github.com/ExuraLabs

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

1113

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

375

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The verification layer is built and exercised in a relevant environment, not yet carrying value on mainnet.

The contracts that verify a Cardano signature on an EVM chain are deployed on Sepolia, driven end to end by real wallets: registrations signed in Eternl and in Lace verify on-chain against the deployed instance, so the path from a CIP-30 signature to an EVM account action is demonstrated, not described. 78 tests, public MIT repository.

What is missing is what the pilot funds. Nothing is on Cardano mainnet yet, and the deposit and exit legs are components, not one flow a stranger can complete. No external user has moved money through it, and no auditor has reviewed it.

We would rather declare 5 and show the Sepolia transactions than claim 6 and be asked which mainnet.
