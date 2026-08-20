# VOW: On-Chain Identity for a Live Commitment Social Network

> VOW is a live commitment social network bringing privacy-preserving on-chain identity to Cardano, one person, one profile, verified without exposing personal data.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 15
- **Proposer:** `stake1u9xcvu7j3c5gap5mvzjgds6qy2wnhm34zr6vaffzhkvgdvcrjerx0`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T03:34:36.718000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

VOW is led by Bosco Ribeiro, founder and developer, operating through VOW TECNOLOGIA LTDA 68.303.661/0001-20, a registered, active Brazilian company. The team is well-suited to deliver this specific integration for three concrete reasons.

First, deep Cardano roots. Bosco is a Cardano Ambassador and has been in the ecosystem since the ITN (Incentivized Testnet), before the Shelley mainnet. He operates the Cardanistas stake pool (SPO) and holds the PORTO DRep governance identity, running infrastructure and participating in governance, not just building on top. This is years of hands-on ecosystem experience, plus a direct channel to the exact users the pilot needs.

Second, a track record of shipping. VOW is not a concept, it is a complete, built product on iOS and Android, with a full progression system (levels, event-sourced reputation, leagues, achievements), an anti-escalation engine, cryptographic row-level privacy, and a live payment rail. The applicant has already demonstrated they design, build, and ship a non-trivial consumer app end-to-end.

Third, the right foundation for on-chain identity. The existing product already takes privacy seriously off-chain, anonymous vows, cryptographic access control, EXIF stripping, so the team understands selective disclosure in practice, not just theory. Bringing identity on-chain extends architecture the team already built and tested.

Cardano Ambassador, SPO and DRep since the earliest days;

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A for this round. If VOW's on-chain identity trail proves sustained adoption beyond the pilot, we would welcome a conversation about a revenue-share contribution to the ecosystem treasury in future rounds.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

VOW's crypto trail generates transactions through normal product use, not artificial incentives. Who transacts: real users completing commitments, plus organic growth via the app's public feed. Why: identity attestation is required to participate in the on-chain trail, proving one-person-one-profile is the mechanism that keeps rankings and leagues fair. How often: recurring, not one-time. Each vow creation, check-in, and closure generates a fresh signed attestation, so an active user produces 10-15 on-chain events across the measurement window, not a single sign-up transaction.

Target justification: at 200k ADA, the required floor is 100 ADA and 10 external wallets; we declare 340 ADA (Ambitious band). With \~200 active users, and 10-15 attestations each, expected volume is 2,000-3,000 transactions (\~660-990 ADA gross), comfortable margin above 340 ADA even if conversion underperforms by half. The target is ambitious relative to the floor, but grounded in a real, measurable, owned distribution channel rather than speculative reach.

### How will you reach and onboard real users - and what evidence backs your channels?

Primary channel: the Cardanistas YouTube channel, operated by the applicant, 10,000 subscribers, a weekly live stream with 100+ recurring viewers. This is a direct, owned line into the exact audience the integration needs: Cardano users who already hold wallets and understand on-chain transactions. Onboarding is walked through live, a dedicated stream demonstrating the crypto trail step by step, including wallet setup for viewers who need it.

Evidence: the channel's consistent weekly engagement is measurable and public. Beyond it, the applicant is an active Cardano Ambassador, SPO (Cardanistas stake pool) and DRep, with standing in the Brazilian Cardano community, a network that amplifies reach beyond direct subscribers.

The onboarding plan concentrates on the first two weeks after going live, then sustains a weekly cadence driving recurring usage rather than a one-time spike, matching the pilot's requirement for steady adoption across the measurement window.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?


StickK and Beeminder pioneered commitment devices, but both are centralized, expose user data, and offer no cryptographic privacy or Sybil resistance. Generic habit apps (Habitica, Streaks) have no financial stake and no accountability weight. On-chain identity tools (DIDs, proof-of-personhood projects) solve identity but ship no consumer product using it.

VOW wins by combining three things none of them do together: real financial commitment, public social accountability, and privacy-preserving on-chain identity that guarantees one person per profile. It is a shipped consumer product that makes on-chain identity useful in practice, not a primitive waiting for adoption, and not an app without verifiable fairness.

### Please provide details about the Technology Readiness Level selected for your existing product

VOW is a complete, functional commitment social network for iOS and Android, currently in final security audit before app-store launch. The core product is fully built: enrollment state machine, a derived progression system (levels, event-sourced reputation, leagues, achievements), an anti-escalation engine, and cryptographic row-level privacy for anonymous vows. Its payment rail is live, real Pix (BRL) transactions process through Stark Bank, a licensed payment institution. The company (VOW TECNOLOGIA LTDA 68.303.661/0001-20) is registered and active. This is TRL 6: a complete MVP with realistic flows and a live payment integration, demonstrated end-to-end, at the threshold of public launch, well above the TRL 5 eligibility bar, with linkable evidence in the app and repository.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

VOW's on-chain layer centers on identity. Each user binds to a single on-chain identity, one person, one profile, regardless of how many wallets they hold, using CIP-0170 primitives. The key design choice is recurring attestation: normal app actions (creating a vow, checking in, closing a vow) each produce a signed on-chain attestation carrying VOW's declared identifier. This is what turns real product usage into sustained, countable on-chain activity, rather than a single sign-up transaction.

Selective disclosure lets a user prove eligibility, a unique human, meeting criteria, without exposing personal data. The proof goes on-chain; the identity stays with the user. This fits VOW's existing off-chain privacy architecture (anonymous vows, cryptographic row-level security, EXIF stripping), making on-chain identity a natural extension rather than a new paradigm.

Why this fits CIP-0170's requirements: the area rewards real identity usage measured by on-chain fees, and identity attestations are inherently lightweight and frequent, a precise match for a social product where users act repeatedly. The stablecoin trail (USDC staking on the commitment itself) rides the same identity rail, so both integrations share one architecture.

The identity primitive is built as reusable open-source infrastructure: any Cardano project facing the multi-wallet Sybil problem can adopt it. Implementation path (Cardano-base credentials) is validated by a proof-of-concept in the first milestone.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Two concentric markets. The immediate market is the Cardano community, wallet-holding users who already understand on-chain value and want fair, verified competition. VOW reaches them directly through the Cardanistas channel (10k subscribers, weekly live streams, 100+ recurring viewers). The broader market is people seeking accountability to build habits, fitness, reading, discipline, a category proven for over a decade by StickK and Beeminder, which have run millions of commitment contracts.

Evidence of demand: VOW is already built and launching on iOS and Android, not a concept. The product includes a full progression system (levels, reputation, leagues, achievements), anti-escalation logic, and tested privacy architecture. A manual validation was run with real users who paid real value and completed real challenges. The applicant operates a registered company (VOW TECNOLOGIA LTDA 68.303.661/0001-20) and active Cardano infrastructure (Ambassador, SPO, DRep).

The commitment-device category has established product-market fit; VOW's contribution is bringing it on-chain with privacy-preserving identity that existing players lack. The demand signal we are testing in this pilot is specifically whether Cardano users adopt the on-chain trail, which the Cardanistas channel gives us a direct, measurable way to drive and verify.

### Applicant name

Bosco Ribeiro

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

VOW's revenue is built into the product, independent of grant funding. Everyone who uses the platform pays,  servers, AI, and tracking have real cost. On every commitment, VOW retains a service fee when a user succeeds and their staked value returns; when a user does not meet the goal, the staked value funds the service. This revenue exists on day one and scales with usage, not with grants.

The grant funds a one-time build, bringing the identity layer on-chain, not ongoing operations. After the pilot, the on-chain identity layer keeps running because it is core product infrastructure: it makes every ranking, league, and future sponsored challenge trustworthy. Users keep transacting because identity attestations are generated by normal app actions they already do, creating vows, checking in, not by an artificial incentive that disappears when funding ends. The business runs on its own revenue; the grant simply moves it on-chain.

### On-chain identity (CIP-0170) - expected transaction count

2500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant, VOW launches as an off-chain app and its on-chain identity layer does not get built, the team would default to a centralized profile system, leaving the multi-wallet Sybil problem unsolved and the product off Cardano. The grant is what brings identity on-chain.

Spend, at a high level: smart-contract and identity-layer development (Aiken/Plutus and CIP-0170 primitives), a Cardano-base credentials to validate the privacy path, mobile integration of the crypto trail, a second legal opinion covering the virtual-asset regime, and launch activity to drive real adoption through the Cardanistas channel. The grant funds a one-time build to mainnet; VOW's own service revenue sustains it after.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By Month 3, VOW's on-chain identity integration is live on mainnet, with these measurable deliverables:

1. Identity primitive live on Cardano mainnet: CIP-0170-based one-person-one-profile identity, deployed and verifiable on-chain (Cardanoscan link).
2. Recurring attestation working end-to-end: a real vow creation, check-in, and closure in the live app each produce a signed on-chain attestation carrying our declared identifier.
3. Public footprint declared: our wallets, identifiers, and message tag registered, plus a Dune Analytics tag live and feeding the Catalyst dashboard.
4. Open-source repository published and documented, with a demo video of the full attestation cycle on mainnet.

Acceptance: a single live demo transaction on mainnet, an identity attestation from the app, visible on Cardanoscan.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

340

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

VOW is a live commitment social network (iOS + Android) where a user makes a public promise, workout 3x a week, read daily, build a habit, stakes a value on it, and proves follow-through with check-ins. Meet the goal, the value returns; miss it, it funds the service.

We are bringing privacy-preserving on-chain identity (CIP-0170) to this live product on Cardano.

The problem: VOW's fairness depends on one person equating to one profile. Its reputation system, leagues, and future sponsored challenges are only trustworthy if a single person can't run ten wallets to create ten profiles and distort every ranking and reward. This is the multi-wallet Sybil problem, and it is exactly what on-chain identity solves.

For whom: first, for VOW's own users, mostly from the Cardano community via the Cardanistas channel (10k subscribers), who get verified, fair competition without exposing personal data. The proof goes on-chain; the identity stays with the user.

More broadly, for any Cardano project facing the same Sybil problem: our identity primitive, one person, one profile, with selective disclosure, is reusable open-source infrastructure. Each user action generates a recurring on-chain attestation, so real usage produces sustained on-chain activity, not a single sign-up transaction.

We are not building an idea. VOW is already shipped; this grant brings its identity layer on-chain.

### Supporting links (repo, site, demo)

- https://vowapp.io/
- https://github.com/tecnologiavow-creator/vow
- https://github.com/tecnologiavow-creator/vow-app

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

The integration is at TRL 2: the approach is designed but not yet coded on-chain. We have defined the architecture, one-person-one-profile identity via CIP-0170, with recurring signed attestations generated by user actions, and selective disclosure so eligibility is proven without exposing personal data. The transaction flow, the declared on-chain footprint, and the counting model are specified. What does not yet exist is working on-chain code, which is exactly what this grant funds. Per the pilot's own framing, the integration is expected to start at design stage and be carried by the grant to mainnet (TRL 7) at Milestone 1, then toward sustained real usage across the measurement window. Feasibility rests on the architecture and milestone plan below, not on a current readiness number.
