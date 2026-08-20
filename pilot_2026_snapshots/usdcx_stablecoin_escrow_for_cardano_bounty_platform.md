# USDCx Stablecoin Escrow for Cardano Bounty Platform

> The Quest adds USDCx stablecoin escrow to its live Cardano bounty platform so posters fund missions in stable value and hunters receive predictable payment, fully settled on-chain.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1u8x5mm8k4dcvl0ayp4ax4r2h2ymnkg538nrcqdr2xh3yq8cvx9t0v`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-20T03:37:39.512000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

I am Opakunle Micheal, solo full-stack developer building on Cardano. LinkedIn: <https://www.linkedin.com/in/opakunle-omotayo-055358184/>

Earlier this year I built TrustBCH, a peer to peer escrow on Bitcoin Cash with full state machine Pending, Awaiting Funding, Funded, In Progress, Submitted, Verified, Released. TrustBCH won Runner Up in Application Track at BCH-1 Hackcelerator. Proof: <https://trust-bch.vercel.app> <https://x.com/bch_1_official/status/2029927755270529102>

I built The Quest solo in 12 weeks: Next.js frontend, Supabase with row level security, CIP-8 wallet auth, isolated signing microservice on [Fly.io](http://Fly.io), Groq AI difficulty detection, multi claimer up to 100 hunters, deadline auto refunds, public on chain ledger. The Quest won Cardano Pie track at Gimbalabs Piece of Pie Hackathon, rewards paid by Cardano Foundation. Live: <https://thequesters.fun> GitHub: <https://github.com/opa1/the-quest> X: <https://x.com/the_questgg>

Aiken escrow is the next step from both projects. I have escrow design from TrustBCH and live Cardano infra from The Quest.

Prior funding: Gimbalabs Piece of Pie winner reward paid by Cardano Foundation. No overlapping scope, TrustBCH Runner Up BCH-1 Bitcoin Cash not Cardano, Skypie DAO commercial poster no funding, no other Catalyst funding. USDCx escrow is new work not funded elsewhere.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Every mission is 4 base tx: deposit, Accept, Submit, Approve with payout. About half the posters hold ADA and need DexHunter swap, add one tx. Average 4.5 per mission. Network fee for Aiken escrow with USDCx asset and min ADA buffer is about 0.35 ADA on preview testnet. Only network fees. Platform fee 2.5 percent capped at 25 ADA goes to treasury and is excluded.

Note: Previous targets of 700 tx and 250 missions were forecasting errors and have been removed. All numbers below are corrected and aligned.

Target 120 missions in 90 days. 120 x 4.5 = 540 transactions. 540 x 0.35 = 189 ADA, clears program floor 180.

Base 4 missions, 30 users, 13 hunters paid, 3 posters:\
13 existing hunters, 80 percent stay = 10 x 3 = 30\
Skypie DAO 30 active, 20 percent convert = 6 x 3 = 18\
Gimbalabs 150 builders, 5 percent as posters = 8 x 2 = 16\
X drove 30 users in 12 weeks, next 12 weeks expect 60 new, 30 percent as hunters = 18 x 2 = 36\
Discord 40 active, 25 percent activation = 10 x 2 = 20\
Total 30+18+16+36+20 = 120\
No paid promotion, no ADA incentives.

### How will you reach and onboard real users - and what evidence backs your channels?

Current channels with verifiable evidence:

X: @the_questgg (<https://x.com/the_questgg>) and @Opa007i (<https://x.com/Opa007i>), 12 weeks of public build updates that drove the initial 30 mainnet users.

Discord: <https://discord.gg/tXSnBVqFp>, active community of testnet and mainnet users.

Skypie DAO partnership: funded live bounties on the platform. Proof: <https://thequesters.fun/ledger>. Being extended to other Cardano DAOs through direct outreach.

Gimbalabs community: winning the Cardano Pie track put The Quest in front of active Cardano builders and project teams. We are leveraging this directly to onboard new posters and hunters.

Post-grant: community onboarding via AMAs, 1:1 outreach to existing hunters, and mission drops through verified Cardano DAO channels. No Cardano-native asset incentives, no referral rewards, no transact-to-earn schemes.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/oDCLp_CYqm4

### Who else solves this today - competitors/alternatives, and why does your approach win?

Gitcoin (Ethereum): largest Web3 bounty platform, no Cardano support, no on-chain reputation system, USD/ETH only.

Dework: multi-chain task coordination, no smart contract escrow, no stablecoin support on Cardano, reputation is platform-held not portable.

Upwork / Fiverr: centralised, fiat-only, reputation disappears if account is banned or platform shuts down.

Discord/spreadsheet bounties: no escrow, no on-chain proof, manual payment coordination.

The Quest wins on three specifics: Cardano-native with real mainnet transactions, on-chain proof of every completion creating a portable reputation the user owns, and stablecoin settlement removing the ADA volatility tax that competitors on Cardano cannot address.

### Please provide details about the Technology Readiness Level selected for your existing product

The Quest is live on Cardano mainnet at <https://thequesters.fun>. Working systems:

- CIP-8 wallet authentication: live, used by 30 registered mainnet users
- ADA bounty deposit and payout: 4 completed missions, 166.32 ADA settled across 13 hunters, all verifiable at <https://thequesters.fun/ledger>
- Isolated signing microservice on [Fly.io](http://Fly.io): handles all platform wallet operations
- Multi-claimer missions up to 100 hunters per mission: live
- Deadline-based automatic refunds: live
- Public on-chain ledger with Cardanoscan-linked transaction hashes: live

The product is not a prototype. It handles real funds on Cardano mainnet with real users.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Current architecture (live on mainnet): The Quest uses a custodial escrow model. The platform signing service (Express, [Fly.io](http://Fly.io), Lucid Evolution, Blockfrost) holds the platform wallet and sends ADA payouts to hunters on poster approval. CIP-30 wallet connect handles poster deposits. CIP-8 COSE_Sign1 Ed25519 signature verification handles authentication. All transactions are real Cardano mainnet transactions with verifiable hashes.

Integration addition (Aiken smart contract escrow): A single asset-parameterised Aiken validator replaces the custodial payout path for USDCx missions. The datum carries mission ID, poster, hunter, arbiter, platform keys, reward asset (USDCx policy ID), reward, payout, fee, submit deadline, review window, and status. Eight redeemers govern state transitions: Cancel, Accept, Submit, Approve, Reject, ResolveDispute, ClaimTimeout, ReclaimExpired. Two timeout paths are critical: ClaimTimeout lets a hunter auto-collect if the poster ghosts after submission; ReclaimExpired lets the poster reclaim if a hunter claims and disappears. These cannot be enforced off-chain without trusting a single custodian, which is why the contract is necessary. USDCx missions require a min-ADA buffer on token UTXOs handled at tx build time by Lucid Evolution. DexHunter aggregator routes in-app ADA-to-USDCx swaps across 15+ Cardano DEXs.

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

Two user segments with demonstrated demand:

Hunters: independent contributors (developers, designers, writers, researchers) who want to earn crypto for real work without intermediaries. The Quest already has 13 hunters paid on mainnet across completed missions.

Posters: DAOs, community organisations, and projects that need work done and want on-chain accountability. Our first commercial poster, Skypie DAO (<https://x.com/SkypieDAO>), funded and ran live bounties through the platform. Proof: <https://thequesters.fun/ledger> <https://x.com/the_questgg/status/2078027501960384675>

Current mainnet traction (independently verifiable):

- 30 registered users
- 4 completed missions
- 166.32 ADA distributed to 13 hunters
- 3 unique posters including a verified DAO partnership

All numbers are publicly auditable at <https://thequesters.fun/ledger>

The stablecoin integration directly expands the poster market. Organisations that budget in USD terms cannot commit to ADA-denominated bounties with confidence. USDCx removes that barrier entirely, which is the same reason USDC dominates Ethereum-based bounty platforms like Gitcoin.

X presence: <https://x.com/the_questgg> Discord: <https://discord.gg/tXSnBVqFp> Proof of DAO partnership: <https://thequesters.fun/ledger> <https://x.com/the_questgg/status/2078027501960384675> <https://x.com/SkypieDAO>

### Applicant name

Opakunle Michael

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The platform charges a 2.5% fee per mission, capped at 25 ADA or the USDCx equivalent, denominated in the bounty asset. The fee is collected from the escrow at the moment of approval, not charged to users upfront. This positions the fee as a completion signal: no fee unless work is actually delivered and approved.

At 120 completed missions per 90-day window at an average bounty of 20 ADA equivalent each: 120 x 0.5 ADA average fee = 60 ADA equivalent per cycle. At scale this covers infrastructure costs and funds ongoing development. The fee model scales with usage with no flat subscription that discourages low-value missions.

Post-grant sustainability: platform fee revenue is the only revenue source. No external funding dependency. The fee applies identically to ADA and USDCx bounties, so the stablecoin integration expands the fee-generating transaction base rather than requiring a new model.

No referral incentives, airdrops, or transact-to-earn schemes are part of the business model

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant the stablecoin escrow cannot be built on this timeline. The Quest has no external revenue yet.

50,000 ADA breakdown:

- Smart contract dev Aiken 8 transitions plus DexHunter: 30% 15k ADA, M1-M2 W1-8
- Frontend USDCx flow and hunter dashboard: 20% 10k ADA, M2 W4-8
- Security review internal audit plus Anastasia Labs quote obtained for pilot: 15% 7.5k ADA, M3 W7-8
- Infra Supabase and [Fly.io](http://Fly.io) 3 months only: 10% 5k ADA
- Community launch 3 AMAs no paid ads: 15% 7.5k ADA, M1-M3
- PM and contingency 10% buffer: 10% 5k ADA\
  Total 50k ADA

No ADA giveaways, no airdrops, no referral incentives paid in Cardano native assets, no transact to earn.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

W1-2 Preview testnet:

W1 D1-7 USDCx deposit live, form shows USDCx+ADA, DexHunter live. Target 5 users fund.

W2 D8-14 Full flow: claim, submit, approve live. Outreach to 13 hunters. Target 5 cycles.

W3-4 Validator hardening: ClaimTimeout and ReclaimExpired tested, validator final, UI done.

W5-6 Quality: internal tests, property tests, Lucid builder done.

W7-8 Launch prep: security review and fixes, mainnet deploy with 1 real USDCx mission. Anastasia Labs quote obtained for pilot.

W9-10 Mainnet Launch Execution:

W9 D1-7 Post-mainnet: announce on X, Discord, Gimbalabs. Onboard 13 hunters. Post first 3 USDCx missions. Target 5 funded.

W10 D8-14 Post-mainnet: Skypie DAO AMA + 4 bounties, outreach to Gimbalabs. Target 18 missions active or done, 81 tx. Evidence at [thequesters.fun/ledger](http://thequesters.fun/ledger) with tx hashes

W11-12 Scale: 120 missions via 8 target DAOs avg 12 each, pipeline in Appendix A, 540 tx, 189 fees, final report and video.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

The Quest is a live gamified bounty platform on Cardano mainnet. Posters fund tasks with ADA, hunters claim and complete the work, and on poster approval the bounty is released on-chain. Every completed mission produces a verifiable transaction hash recorded permanently on Cardano, giving contributors a portable reputation no platform can delete.

The problem: ADA price volatility creates real friction. A poster who funds a 100 ADA mission today may be paying a very different real-world value by completion. This makes bounty pricing unpredictable and discourages organisations with fixed operational budgets from committing to on-chain bounties.

This proposal builds a USDCx stablecoin escrow contract in Aiken. Posters can fund missions in USDCx. The contract holds funds on-chain and releases payment to the hunter only on approval, with automatic timeout refunds if the work is not completed. ADA-holding posters can swap in-app before funding through DexHunter routing. The settlement value is stable from posting to payout.

The primary beneficiaries are freelancers, DAOs, and community organisations needing predictable, verifiable work agreements on Cardano.

### Supporting links (repo, site, demo)

- https://thequesters.fun
- https://x.com/the_questgg
- https://thequesters.fun/ledger
- https://github.com/opa1/the-quest
- https://github.com/opa1/the-quest/blob/main/docs/Appendix-A-Pipeline.md

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

Yes. MIT License. Repository: <https://github.com/opa1/the-quest>

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

540

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

189

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The USDCx stablecoin escrow integration has a fully specified design: Aiken datum and redeemer types, eight state transitions (Cancel, Accept, Submit, Approve, Reject, ResolveDispute, ClaimTimeout, ReclaimExpired), asset-parameterised validator, min-ADA buffer handling for token UTXOs, and DexHunter routing for in-app ADA-to-USDCx swaps. The architecture is documented and the core contract logic has been validated in pseudocode. The Aiken toolchain and Lucid Evolution off-chain builder are already part of the project infrastructure.

No production Aiken code has been written yet. Existing escrow experience from TrustBCH on Bitcoin Cash and the running Cardano infrastructure from The Quest mean the implementation path is clear and low-risk, not exploratory.
