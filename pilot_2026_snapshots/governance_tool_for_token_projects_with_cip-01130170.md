# Governance Tool for Token Projects with CIP-0113/0170

> Complete and publish Open Vote for native token projects to create their own governance space using CIP-0113 for KYC/payment rules and CIP-0170 for on-chain proposals, votes, and fund distributions.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 115
- **Proposer:** `stake1uxgs7ejclumtfax0c5fsun6l5ghngegq5gc6k8wuw9naynsn3w9j5`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-18T18:15:55.024000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

We are a small Cardano development team active in Project Catalyst since Fund 8, with all our funded projects completed. Open Vote builds on our Fund 11 [PAAS project](https://projectcatalyst.io/funds/11/cardano-use-cases-solution/classified-smart-contracts-for-distinct-use-case-dapps), reusing and extending its Aiken smart contracts and existing work for on-chain governance.

A three-person team supported by AI coding agents will accelerate development, testing, and maintenance:

**Thang Tran** full-stack engineer, product manager

[https://github.com/saigonbitmaster, https://t.me/ThangTranNam](https://t.me/ThangTranNam)

**Thang Vu** full-stack engineer, business manager

[https://github.com/vmthang, ](https://github.com/vmthang)<https://t.me/vmthang>

**Chuong Pham** full-stack engineer

<https://github.com/jackchuong>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

No grant repayment or revenue-share pledge. Open Vote will remain free for native-token communities and allow others to use, modify, and build upon it.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Holders and teams transact when registering tokens, proposing, voting, and recording decisions — repeatedly as projects evolve.**

**We target adoption by 3–5 native token projects within 6 months, with 500 CIP-0113 and 2,000 CIP-0170 transactions generated through recurring KYC, proposals, voting, and governance decisions.**

### How will you reach and onboard real users - and what evidence backs your channels?

We'll reach native token projects through Discord, Telegram, and Twitter/X, where token communities already gather.

We'll also attend Cardano events to talk directly with project teams and holders.

Our team has worked on Catalyst-funded projects since F8, giving us real relationships to onboard early adopters faster.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://www.youtube.com/watch?v=oE0l1bDIUZQ

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Competitors:**

- Cardano GovTool — official, ADA-only.
- Snapshot — off-chain voting, not verifiable on-chain.
- Clarity / WingRiders — on-chain, but need self-hosting or lack compliance.

**Open Vote:** Free, light, and ready to use for native tokens — on-chain verifiability (CIP-0170) plus built-in compliance (CIP-0113), no dev setup and no wallet snapshot needed.

### Please provide details about the Technology Readiness Level selected for your existing product

**We assess Open Vote at TRL 7 based on its current development status.**

- Open Vote is deployed and running on Cardano mainnet: users can connect a wallet holding a native token and start governing their project.
- CIP-0170 attestations execute as real on-chain transactions, covering the governance cycle from proposal and voting to fund distribution.
- CIP-0113 integration is designed but has not been tested live because no CIP-0113-compliant token is currently available for testing.
- Usage so far has been limited to internal testing, and the system has not yet undergone a security review.

Evidence:

- [Live demo](https://open-vote-app.vercel.app)
- [GitHub](https://github.com/bWorksApp/open-vote)
- [Demo video](https://www.youtube.com/watch?v=oE0l1bDIUZQ)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Open Vote uses on-chain and off-chain components, with each handling what it does best:**

- **Aiken smart contracts** enforce CIP-0113 KYC with Off-Chain Proofs and On-Chain Validator, and payment rules on Cardano.
- **CIP-0170** records governance actions and results on-chain through metadata without asset transfers, keeping transactions simple and low-cost. Raw proposal content is stored on IPFS, with its hash recorded on-chain.
- **Off-chain service** snapshots wallet voting power and calculates Token-Weighted or Quadratic Voting results, then records snapshots and final results on-chain.
- **Cardano wallets** let users register tokens, submit proposals, vote, and participate in governance.

**This fits native-token governance by keeping rules and decisions verifiable on-chain while moving large data and calculations off-chain, providing low-cost, transparent, verifiable, and immutable results.**

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)
- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

**Target market:** Small and mid-size Cardano native token projects — memecoins, utility tokens, and emerging DAOs — that want on-chain governance without building it themselves.

**Evidence:** No usage data yet as a new project, but the signal is clear:

- Thousands of native tokens trade on Cardano with no governance option.
- Cardano's GovTool supports only ADA.
- Many rely on unverifiable tools like Discord polls.

This shows real, unmet demand of on-chain governance for Cardano token projects.

### Applicant name

Thang Tran

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

**Business model:** Open Vote is free for core use — any native token can register, propose, and vote at no cost.

We plan to add optional premium features later, like analytics, custom branding, or higher usage limits for larger communities.

Core governance stays free for everyone. Premium revenue will cover hosting and development after the grant ends.

### Programmable tokens (CIP-0113) - expected transaction count

500

### On-chain identity (CIP-0170) - expected transaction count

2000

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, Open Vote stays a demo, not a usable tool. The grant covers developer time to reach mainnet, hosting for the off-chain tallying service, and outreach to onboard the first native token projects — turning a prototype into a free governance tool any Cardano project can use.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- **CIP-0113:** Complete/test the Aiken smart contract for KYC/payment rules and mint an Open Vote CIP-0113 token for optional KYC verification and payment compliance.
- **CIP-0170 & IPFS:** Store raw proposal content on IPFS and submit its hash on-chain through CIP-0170.
- **Voting Power:** Implement wallet voting-power snapshots off-chain and record them on-chain through CIP-0170 for Token-Weighted and Quadratic Voting.
- **CIP-0170 & Governance Flow:** Complete wallet connection, governance-space registration, proposal, voting, and funding flows and record data on-chain.
- **Security & QA:** Complete test checklist, bug log, and security review; resolve critical issues.
- **Public Release:** Deploy Open Vote with documentation, release notes, declared footprint, and walkthrough video.
- **Mainnet Adoption:** Demonstrate the complete governance flow with real users and provide transaction hashes as evidence.
- **Demo Day:** Present the completed flow through live demo and Q&A.

### How far along is the integration you're proposing, today?

TRL 8 - System complete and qualified

### Programmable tokens (CIP-0113) - fee target (ADA)

200

### On-chain identity (CIP-0170) - fee target (ADA)

400

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**Solution:**

Open Vote is our product that creates a free, dedicated governance space for each Cardano native token project, where its holders connect their wallets to create or vote on proposals for that project:

- Open Vote uses CIP-0113 for on-chain KYC of token issuers and selected proposers, and CIP-0170 to record proposals, votes, voting-power snapshots, and fund distributions on-chain.
- Off-chain code aggregates CIP-0170 on-chain data and computes voting power using token-weighted or quadratic mechanisms for governance decisions.
- Token projects and token holders can use Open Vote without any developer setup or wallet snapshot.

Open Vote keeps token holders and projects connected, allowing holders to take part in project decisions through trusted, transparent, and immutable on-chain governance.

To try demo and find useful links please see [our document](https://docs.google.com/document/d/1uXRenwhQTxx1aMC3tAJ-nydTs-pO0sbY_rWwox2T9rw/edit?tab=t.0).

**Problem it solves - for whom:**

Cardano’s official GovTool supports ADA governance, while native token projects lack a standard way to govern on-chain. As a result, their holders often have no simple way to propose ideas, vote, or participate in decisions about the projects they support.

### Supporting links (repo, site, demo)

- https://open-vote-app.vercel.app
- https://github.com/bWorksApp/open-vote
- https://github.com/bWorksApp/paas-aiken-contracts

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

Open-sourced under the Apache License 2.0, allowing anyone to inspect, fork, contribute to, and use the project freely through its GitHub repositories.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

**We aim to move Open Vote from TRL 7 to TRL 8 through this integration.**

- M1 will complete and deploy CIP-0113 KYC and payment rules, complete the security review, and prepare Open Vote for general public use.
- The complete governance flow—from token registration to proposal, voting, and fund distribution—will run on Cardano mainnet using CIP-0170, with each step verifiable through on-chain transactions.
- By the end of M1, Open Vote will be a complete, security-reviewed, mainnet-deployed system ready for general use. Evidence will include mainnet transactions, security review results, and public deployment.
