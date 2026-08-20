# Veridict: verifiable settlement for human and agent work

> Bounties that pay themselves. Stake a reward, agree the criteria up front, and the escrow releases payment only when a signed, independently replayable verdict says the work meets them.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 2
- **Proposer:** `stake1uxzcgxquevj06f0cgveyttt3zh0q3696kqwcxl384zwjq3g3cr5np`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-20T05:03:34.151000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Ashwin Goyal — sole developer and applicant. No other individual is named on this or any other proposal this round.

I work on agent reasoning and verification full time, and compete in ARC Prize 2026 (ARC-AGI-3), the interactive reasoning benchmark. Veridict exists because the recurring problem there is proving what an agent did, to someone who wasn't there.

Why I'll finish, not just start — the fair question about an unknown solo applicant:

Track record: 96 public repositories at [github.com/let-the-dreamers-rise](http://github.com/let-the-dreamers-rise), mostly TypeScript, spanning web3, payments and infrastructure. Not a first project and not a one-off proposal — a continuous building habit you can scroll through.

I built and deployed Veridict before asking for anything. Escrow, signed verdicts and verifier all work on Preprod, unpaid, every commit timestamped before submission. Someone who ships without funding doesn't need funding to begin.

Delivery risk is structurally low — no team to lose, no payroll, minimal infrastructure, and the research this rests on is already my full-time work.

Accountability is public and permanent: proposal, reports and results published beside a real name, KYC'd identity and that GitHub history. Milestones mean undelivered work is unpaid work.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary pledge: once cumulative protocol fee revenue exceeds 2x the grant, I will direct 20% of ongoing fee revenue to the Cardano treasury until 100% of the grant is returned, capped at five years from completion.

The threshold is set where repayment comes from real revenue rather than cutting runway, so it's a pledge I can honour.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Posters stake rewards for work they want done; workers claim them. Every bounty is four fee-paying transactions — create, commit, reveal, resolve — and each extra submission adds two. Fees come from users' own wallets because that's how the product works, not because activity is manufactured.

Costs are measured on Preprod, not modelled: script-spending transactions averaged 0.424 ADA, creation \~0.2. A bounty is \~1.5 ADA across four transactions.

Target: 620 transactions, ₳230 against the ₳184 floor — \~155 bounties over \~30 counted days, about 5 a day across 20 external wallets. It sits close to the floor deliberately: with zero users today, claiming 11 a day would be aggression without evidence.

Rhythm is the honest difficulty — bounties are episodic while floors require fees every epoch. The fix is structural: standing weekly bounty programs run by partner maintainers on a fixed cadence.

### How will you reach and onboard real users - and what evidence backs your channels?

Named channels with conversion arithmetic, not a marketing plan.

1\. Open-source maintainers running standing weekly bounty programs: \~20 direct approaches to maintainers of Cardano and Aiken tooling repos, targeting 5 recurring programs. Primary channel — recurring posting produces per-epoch rhythm rather than spikes.

2\. Cardano developer community, forum and X: \~30 approaches, targeting 10 posters running at least one bounty.

3\. AI-agent builder communities: \~25 approaches, targeting 8 worker-side wallets. Agent operators are the natural supply side — an agent that can do the work can submit and get paid without a browser.

\~75 named approaches converting to 20 active external wallets against the minimum.

First two weeks live: onboard the 5 partner programs first so epoch-one fees exist from day one, then open posting publicly.

Honest: no signed letters of intent today. The thin margin over the minimum is the top risk in this proposal.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Upwork/Fiverr: custodial, 10-20%, private arbitration, geographically restricted. Users switch when fees and delay outweigh brand familiarity — strongest for cross-border work these platforms serve badly.

Gitcoin/Algora bounties: remove the custodian, keep a human maintainer approving payouts. Veridict removes that step for criteria a machine can check, which is most of what maintainers pay for.

Cardano escrow contracts: solve custody, not judgment. Someone still decides.

Why mine wins: criteria agreed and hash-committed before money moves, a verdict signed and independently replayable from chain data, a payout released by rule rather than anyone's choice. Nobody else offers a payment decision a stranger can recompute.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 5, validated on public testnet. Deployed and working on Cardano Preprod.

Script: addr_test1wq8fj8jmmj56r6sckrp40uex3uy8lkkr82xzut645jqm0nsh6qe3p

Two complete lifecycles ran on-chain. A passing verdict released the reward and routed the protocol fee to the treasury in one transaction: 95805b36483f1cd376df0438e5e46c5f4dc4560df3e17e0cc4c50f27deb3fd5b

A failing verdict refused. 25 tADA remains locked at the script in state Resolved: fe3fda67c72d2d226dc1d3fb93ab1b3742c499c72db7227523b47f5305a00e3b

Anyone can confirm both with their own Blockfrost key via apps/verifier-cli.

Not claimed: mainnet, or any external user. Every address in the demo is mine, and none of that activity would count under the Standard.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

One bounty lives on one UTxO thread, advanced by an Aiken (Plutus V3) validator through Open, Committed, Submitted, Resolved, Appealed.

Why eUTxO fits:

\- Determinism: success is knowable before submission, so a payout either happens or the transaction fails — no partial state mid-release.

\- Reference inputs: a published verdict can be consumed by other contracts without spending it and without coupling them to my service. This is what makes the oracle integration structurally real, and it has no clean EVM equivalent.

\- Local state: each bounty's terms sit in its own datum, so bounties cannot interfere.

Verdict authorisation: the redeemer carries the verdict plus an Ed25519 signature. The validator rebuilds a 180-byte fixed-width preimage on-chain with two builtins — the bounty's own output reference is inside it — hashes it with blake2b-256, and verifies against the oracle key in the datum. Binding that reference is what makes a verdict unreplayable elsewhere.

Defences, each implemented and tested: double satisfaction (exactly one script input per transaction, so one payment output can't settle two bounties); front-running (commit-reveal); datum rewriting (all terms immutable, only state advances); unbounded validity ranges (timestamps must fall inside a finite range); fee siphoning (fee capped in the validator, not just off-chain).

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

Three segments, in the order I'll reach them.

Open-source maintainers paying for issues. Bounty funding is established behaviour — GitHub Sponsors, Polar, Algora, Gitcoin all exist because maintainers already pay for work — and all still put a human in the approval loop. Maintainers are ideal first users because their acceptance criteria are already machine-checkable: the test suite passes or it doesn't.

Cross-border contract work. Upwork and Fiverr take 10-20% and settle in days to weeks, and both exclude workers in countries their rails don't serve. A worker in one of those countries with a wallet gets paid in minutes.

Agent operators. x402 processed over 165 million transactions across \~69,000 active agents through 2026. Those rails answer how to pay; none answers whether the work was done — the settlement gap an autonomous agent can't bridge by opening a support ticket.

The honest limit: the first two are proven markets with incumbents taking real fees, which shows willingness to pay but not that these users switch to me. I have zero users and no letters of intent today. What I have is a working system and a channel plan with named conversion arithmetic. Better to state that than dress up a projection.

### Applicant name

Ashwin Goyal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

A protocol fee in basis points on settled bounties, capped in the validator at 500 bps, set at 250 today. Implemented and working: the passing Preprod lifecycle routed the fee to the treasury in the same transaction that paid the worker.

Who pays: the poster, from the staked reward, at settlement. They pay because the alternative is 10-20% to a platform, or paying on trust and absorbing the risk.

Why usage persists: the fee scales with settled work, not with grants, and running costs are low — static frontend, one signing service, sandbox runners, a few hundred ADA a month. No token, no emissions, nothing to unwind when the grant stops. A maintainer running a weekly bounty program has no reason to stop the week measurement ends; they started because it settles their work automatically.

Honest limit: at 250 bps this is a volume business, and volume is what I haven't proven.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without it this stays a testnet demo by one unpaid developer.

Mainnet with real funds, which I won't do without an independent security review of the validator — \~10,000 ADA, and the main reason this hasn't shipped.

Removal of the honest weakness in what exists: one signing key authorises every payout. M3 replaces it with an M-of-N attester quorum in the validator.

USDM/USDCx settlement, so posters stake a stable amount — the difference between a demo and something a maintainer would fund real work with.

Split: M1 mainnet, registry, verifier 22,000; M2 stablecoin settlement, web app, judgment hardening 20,000; M3 quorum, appeals, SDK 15,000; security review 10,000; infrastructure 12 months 4,000; docs and partner onboarding 4,000. No user incentives.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Bounty escrow validator on Cardano mainnet, script hash and address declared as the on-chain footprint.
2. Verdict registry on mainnet, publishing signed verdicts as inline datums consumable by third-party contracts as reference inputs.
3. At least one complete end-to-end bounty lifecycle on mainnet by a real external user — create, commit, reveal, resolve — with transaction hashes mapped to each flow step, repeated across independent runs.
4. Public web app letting a non-technical poster create a bounty, review and approve compiled criteria, and resolve it.
5. Public verifier as hosted page and CLI, recomputing any verdict from chain data alone with no backend dependency.
6. Independent security review of the validator completed before mainnet holds user funds, report published.
7. Dune dashboard live against declared identifiers.
8. Release notes stating architecture, scope and limitations, plus a technical walkthrough video.

### Oracles - expected transaction count

610

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

Veridict is a bounty escrow whose payout condition is machine-checkable and whose check is published on-chain.

A poster writes a spec and stakes the reward. The spec compiles into explicit checkable criteria, which the poster approves BEFORE money is locked; the criteria hash goes on-chain, so the standard cannot change once submissions arrive. Workers — human or agent — submit under commit-reveal, so nobody can copy their work from the mempool and claim the bounty first. Deterministic criteria (tests, file checks, schemas, hashes) run in a locked-down sandbox. Only the subjective residual goes to bounded judgment against the fixed rubric. A signed verdict carrying a Merkle root over per-criterion evidence authorises the escrow to pay, or to hold funds for appeal.

No human approves the payout. The criteria decide, and anyone can recheck the decision from chain data alone.

For: open-source maintainers paying for issues, teams paying contributors across borders, and agent operators needing work settled without a human in the loop.

### Supporting links (repo, site, demo)

- https://github.com/let-the-dreamers-rise/veridict
- https://preprod.cardanoscan.io/transaction/fe3fda67c72d2d226dc1d3fb93ab1b3742c499c72db7227523b47f5305a00e3b
- https://preprod.cardanoscan.io/transaction/95805b36483f1cd376df0438e5e46c5f4dc4560df3e17e0cc4c50f27deb3fd5b
- https://github.com/let-the-dreamers-rise/veridict/blob/main/docs/TRL5-EVIDENCE.md

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

230

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

TRL 4,component validated in a relevant environment; the production piece is still to build.

Working on Preprod: verdicts are signed Ed25519 over a fixed-width digest bound to the specific bounty UTxO, and the validator verifies that signature before releasing funds. Known-answer tests assert the Aiken validator and the TypeScript signer produce identical digests, so they cannot silently drift.

Not built — what the grant funds: a public verdict registry publishing verdicts as inline datums, consumable by any third-party contract as reference inputs without integrating with my backend. That is what turns a private signature check into an oracle other Cardano contracts can read.

 unbuilt: multi-attester quorum, so the validator requires M-of-N signatures instead of trusting a single key.
