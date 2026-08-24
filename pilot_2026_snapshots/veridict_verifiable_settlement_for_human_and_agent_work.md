# Veridict: verifiable settlement for human and agent work

> Bounties that pay themselves. Stake a reward, agree the criteria up front, and the escrow releases payment only when a signed, independently replayable verdict says the work meets them.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 10
- **Proposer:** `stake1uxzcgxquevj06f0cgveyttt3zh0q3696kqwcxl384zwjq3g3cr5np`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-24T11:54:38.653000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Ashwin Goyal — sole developer and applicant. No other individual is named on this or any other proposal this round.

I work on agent reasoning and verification full time, and compete in ARC Prize 2026 (ARC-AGI-3), the interactive reasoning benchmark. Veridict exists because the recurring problem there is proving what an agent did, to someone who wasn't there.

Why I'll finish, not just start — the fair question about an unknown solo applicant:

Track record: 96 public repositories at [github.com/let-the-dreamers-rise](http://github.com/let-the-dreamers-rise), mostly TypeScript, across web3, payments and infrastructure. Not a first project and not a one-off proposal.

I built and deployed Veridict before asking for anything. Escrow, signed verdicts, oracle-priced settlement, an independent verifier and a live web app all work on Preprod, unpaid, every commit timestamped before submission.

Apache-2.0 and public:  the ecosystem keeps the validator, the verifier and the tests.

Delivery risk is structurally low — no team to lose, no payroll, minimal infrastructure, and the research this rests on is already my full-time work.

Accountability is public and permanent: proposal, reports and results published beside a real name and KYC'd identity. Milestones mean undelivered work is unpaid work.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary pledge: once cumulative protocol fee revenue exceeds 2x the grant, I will direct 20% of ongoing fee revenue to the Cardano treasury until 100% of the grant is returned, capped at five years from completion.

The threshold is set where repayment comes from real revenue rather than cutting runway, so it's a pledge I can honour.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts and why: posters staking rewards for work they want done, and workers claiming them. Fees come from users' own wallets because that is how the product works, not because activity is manufactured.

What counts is precise: only transactions that consume the declared feed — the resolution, one per submission judged. Creating, committing and revealing are real activity but are not counted, because they do not read the feed.

Declared target: 415 qualifying transactions, ₳200, against the ₳150 floor. Measured, not modelled: a feed-consuming resolution on Preprod cost 0.482295 ADA, so 415 resolutions is ₳200 and the floor needs 311. At three submissions per bounty that is \~140 bounties over a \~10-week window from a six-week M1, across a minimum of 15 external wallets with 18 planned.

First two weeks, concretely: week 1 — ten seeded bounties live, 8 external worker wallets, \~30 qualifying resolutions, ₳14 counted. Week 2 cumulative: 20 bounties, 13 wallets, \~70 resolutions, ₳34. Every reward is payment for a deliverable I would otherwise contract for; no fee is ever reimbursed and no transaction is ever paid for.

### How will you reach and onboard real users - and what evidence backs your channels?

The cold-start is solved by seeding demand myself and letting the market supply the labour. Weeks 1-2 after M1: I post ten real development bounties from declared team wallets — SDK examples, wallet integrations, docs and test coverage for Veridict's own roadmap, $25-75 each, funded by the budget's seeded-bounty line as procured deliverables. My poster-side fees count for nothing; every counted fee comes from an external worker wallet doing real work for a real reward. Fees are never reimbursed, and every seeded bounty is flagged to the fund operator for scrutiny.

Worker channels, named: Catalyst Discord (5,226), CF engineering Discord (2,337), Aiken Discord, r/CardanoDevelopers, Cardano Stack Exchange — plus an agent lane: the machine-readable bounty feed lets AI-agent operators work bounties, which is my own community.

Weeks 3+: convert workers into posters; recruit Catalyst-funded teams who already pay for milestone work.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Upwork and Fiverr: custodial, 10-20%, private arbitration, geographically restricted. Users switch when fees and delay outweigh brand familiarity, strongest for cross-border work these platforms serve badly.

Gitcoin and Algora bounties: remove the custodian, keep a human maintainer approving payouts. Veridict removes that step for criteria a machine can check, which is most of what maintainers pay for.

Cardano escrow contracts: solve custody, not judgment. Someone still decides.

Why mine wins where it wins: criteria agreed and hash-committed before money moves, a verdict signed and independently replayable from public chain data, a payout released by rule rather than anyone's choice, and a dollar amount that stays a dollar amount.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 5, validated on a public testnet. Deployed and working on Cardano Preprod, including the oracle integration .

Live: <https://veridict-five.vercel.app> ,anyone with a preprod wallet can post a bounty, and anyone at all can verify a past verdict without connecting anything.

hash:30da5ba8797fc4e34c53b4bb796ec26b2b2769662d06a353d531a1db.

A $12.00 bounty settled on-chain at exactly 30.000000 tADA, priced at $0.40 per ADA by a feed the resolution read as a reference input: f76999d78f611e511e260e73116f3a8f9d42864b2bfb3b246a99b3d7b1d3b0b1. The poster staked 60 tADA and the surplus above the priced amount returned to them.

A failing verdict on the same validator withheld the payout: 25 tADA remains locked in state Resolved (c1bee46bd021ffbc7459bd9262ba5a0d477629ee842c6ecf86152fdf8185a4ee).

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

One bounty lives on one UTxO thread, advanced by an Aiken (Plutus V3) validator through Open, Committed, Submitted, Resolved, Appealed.

Why eUTxO fits, concretely:

\- Reference inputs. The price feed is read, never spent, so any number of bounties can settle against the same feed in the same block with no contention and no permission from the oracle operator.

\- Determinism. Whether a transaction succeeds is knowable before submission, so a payout either happens or the transaction fails — never a partial release.

Oracle consumption: the resolution transaction carries the feed as a reference input. The validator finds it by its NFT, reads price, timestamp and expiry, refuses an expired statement, and computes lovelace = usd_micro \* price_scale / price. The scale is declared in the bounty datum rather than assumed, so a change in feed precision cannot silently change what a bounty pays. The stake is a ceiling: if ADA fell the worker takes everything staked rather than a promise the escrow cannot honour; if it rose the surplus returns to the poster.

Verdict authorisation: the redeemer carries the verdict and an Ed25519 signature. The validator rebuilds a 180-byte fixed-width preimage on-chain — the bounty's own output reference inside it — hashes with blake2b-256 and verifies against the oracle key in the datum. That binding makes a verdict unreplayable elsewhere.

Source: [github.com/let-the-dreamers-rise/veridict](http://github.com/let-the-dreamers-rise/veridict)

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Three segments, in the order I will reach them.

Open-source maintainers paying for issues. Bounty funding is established behaviour — GitHub Sponsors, Polar, Algora and Gitcoin exist because maintainers already pay for work — and all still put a human in the approval loop. Maintainers are ideal first users because their acceptance criteria are already machine-checkable: the test suite passes or it does not.

Cross-border contract work. Upwork and Fiverr take 10-20% and settle in days to weeks, and both exclude workers in countries their rails do not serve. A worker in one of those countries with a wallet gets paid in minutes, in dollars, at a price the chain agrees on.

Agent operators. x402 processed over 165 million transactions across roughly 69,000 active agents through 2026. Those rails answer how to pay; none answers whether the work was done — the settlement gap an autonomous agent cannot bridge by opening a support ticket.

The honest limit: the first two are proven markets with incumbents taking real fees, which shows willingness to pay but not that these users switch to me. I have zero users and no letters of intent today. What I have is a working system and a seeding plan that needs no third party to say yes before fees exist. Better to state that than dress up a projection.

### Applicant name

Ashwin Goyal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

A protocol fee in basis points on settled bounties, capped in the validator itself at 500 bps and set at 250 today. Implemented and working: the passing Preprod resolution routed the fee to the treasury in the same transaction that paid the worker.

Who pays: the poster, from the staked reward, at settlement. They pay because the alternative is 10-20% to a platform, or paying on trust and absorbing the risk themselves.

Why usage persists after the window: the fee scales with settled work rather than with grants, and running costs are low — a static frontend, one signing service and sandbox runners, a few hundred ADA a month. No token, no emissions, nothing to unwind when grant funding stops. A maintainer running a weekly bounty program has no reason to stop the week measurement ends; they started because it settles their work automatically.

Honest limit: at 250 bps this is a volume business, and volume is what I have not yet proven.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without it this stays a testnet demo by one unpaid developer.

Mainnet with real funds, which I will not do without an independent security review of the validator — the main reason this has not shipped already.

A live production price feed rather than my own: connecting Pyth on mainnet and proving a real settlement.

A product a non-technical poster can actually use.

Budget, inside the four-month frame: security review 15,000; mainnet deployment and Pyth integration 14,000; web app and public verifier 12,000; infrastructure 3,000; documentation, seeded development bounties and onboarding 6,000. Total 50,000.

No user incentives, no re-granting, nothing retroactive. The seeded-bounty line procures real deliverables through the product itself — the adoption engine.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?


1\. Bounty escrow validator deployed to Cardano mainnet, script hash and address declared as the on-chain footprint.

2\. Live production ADA/USD feed (Pyth) integrated, feed identifier declared, so every resolution consumes it.

3\. At least one complete end-to-end USD-denominated bounty on mainnet by a real external user — create, commit, reveal, resolve — with transaction hashes mapped to each flow step, repeated across independent runs.

4\. Public web application allowing a non-technical poster to create a bounty, review and approve the compiled criteria, and resolve it.

5\. Public verifier, hosted page and CLI, recomputing any verdict from chain data alone with no backend dependency.

6\. Independent security review of the validator completed before mainnet holds user funds, report published.

7\. Dune dashboard live against the declared identifiers.

8\. Release notes stating architecture, scope and limitations, plus a technical walkthrough video.

### Oracles - expected transaction count

415

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Paying for work requires trusting someone. Freelance platforms hold the money and arbitrate privately: 10-20% fees, weeks of delay, whole countries excluded. Crypto escrow fixes custody but not judgment — a human still decides if work is acceptable, and they have an incentive.

It breaks entirely for AI agents, which now do useful work but cannot open a support ticket, wait 14 days for arbitration, or receive a bank transfer.

Veridict is a bounty escrow whose payout condition is machine-checkable and whose check is published on-chain

A poster writes a spec and stakes a reward denominated in dollars. The spec compiles into explicit checkable criteria, which the poster approves BEFORE money is locked; the criteria hash goes on-chain, so the standard cannot change once submissions arrive. Workers — human or agent , submit under commit-reveal, so nobody can copy their work from the mempool and claim the bounty first. Deterministic criteria (tests, file checks, schemas, hashes) run in a locked-down sandbox; only the subjective residual goes to bounded judgment against the fixed rubric

Every resolution reads an ADA price feed and pays the dollar amount in ADA at the settlement price, so a poster advertises $50 without carrying ADA volatility, and a worker is paid what was promised rather than what the market did meanwhile

For: open-source maintainers paying for issues, teams paying contributors across borders, and agent operators needing work settled without a human in the loop

### Supporting links (repo, site, demo)

- https://github.com/let-the-dreamers-rise/veridict
- https://preprod.cardanoscan.io/transaction/fe3fda67c72d2d226dc1d3fb93ab1b3742c499c72db7227523b47f5305a00e3b
- https://preprod.cardanoscan.io/transaction/95805b36483f1cd376df0438e5e46c5f4dc4560df3e17e0cc4c50f27deb3fd5b
- https://github.com/let-the-dreamers-rise/veridict/blob/main/docs/TRL5-EVIDENCE.md
- https://veridict-five.vercel.app

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

200

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

TRL 4 — the mechanism is built and validated on Preprod; the live-provider connection and mainnet deployment are what the grant funds.

What works: the validator finds a feed by the NFT it carries, not its address, reads price, timestamp and expiry from a Charli3-standard datum, refuses an expired feed, and converts a USD reward to lovelace at that price. Ten on-chain tests cover the arithmetic, freshness rejection, and stake ceiling.

Diligence: both public Charli3 ADA/USD feeds are long expired (preprod since 2026-03-01, mainnet since 2026-05-26), so the demo uses my own feed in the identical datum shape, declared as such; mainnet targets Pyth, which this program names.

The single signing key is a named limitation; a quorum is deliberately out of scope.
