# VOW: proof of person for money-backed commitments

> VOW is a mobile app where people put their own money on a commitment and check in to prove they kept it. This grant adds CIP-0170: one verified person, one portable identifier, anchored on Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 27
- **Proposer:** `stake1u9xcvu7j3c5gap5mvzjgds6qy2wnhm34zr6vaffzhkvgdvcrjerx0`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-22T03:03:25.035000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

I am a solo founder, and I would rather say that plainly than pad a team page.

Evidence of capability is the product itself. VOW is built end to end by me: the mobile app in React Native, the backend, the database with row level security, and the payment integration, including a separate service on a host with a fixed egress IP, because the payment provider requires an IP allowlist for transfers. That last piece is the kind of problem that only appears once you actually move money.

Evidence for this specific work is already public. Before writing this proposal I ran the KERI feasibility spikes and published them: [github.com/tecnologiavow-creator/vow-identidade](http://github.com/tecnologiavow-creator/vow-identidade). Offline identifierderivation, publication with three witnesses at threshold two, and key rotation that preserves the identifier, with the real console output in the README and the limits stated rather than hidden.

Evidence of reach: I am a Cardano Ambassador, and I moderate a Telegram community of 1,800 Cardano members.

The risk of a one-person team is real. What reduces it here is scope: six to eight weeks of work, on tooling already proven to run.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A for this round. If VOW's on-chain identity trail proves sustained adoption beyond the pilot, I would welcome a conversation about a revenue-share contribution to the ecosystem treasury in future rounds.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: people who already use VOW. They put their own money on a commitment and check in to prove they kept it. Identity is not a separate product they must adopt. It is attached to something they already had a reason to do.

Why: a portable identity replaces the ordinary account login. The person proves they are the same unique human across sessions, and the proof belongs to them, not to us.

How often: 4 authentications each within the window, one anchoring cycle per authentication. That is roughly weekly across 30 days, which matches how often someone opens a 30 day commitment to check in.

Why 50 people is reasonable: VOW already runs on real devices with a closed group of testers. The cohort comes from them, not from cold acquisition.

Why it is still ambitious: every participant needs a Cardano wallet holding ADA, and must sign and pay for each anchor. That is the real barrier, not the app. Fifty funded wallets, from people who came for a fitness commitment, is a demanding ask. We would rather declare a number we can defend than one that flatters the proposal.

### How will you reach and onboard real users - and what evidence backs your channels?

Two channels, both made of people who already hold ADA.

A Telegram community of 1,800 Cardano members, which I moderate. Reaching 20 to 50 signing wallets means converting 1% to 3% of that group.

The Cardano ambassador network, national and international. I am a Cardano Ambassador, which is verifiable.

I also run a YouTube channel with 10,000 subscribers. Its monthly views are currently low and I am not counting on it.

Onboarding, first two weeks after going live: a walkthrough video and a written guide in Portuguese and English, a live session in the Telegram group, and direct one-to-one onboarding of the first 10 wallets, so early problems surface with me rather than with a stranger.

Nobody is paid, rewarded or reimbursed to transact, and no wallet is funded by us. Every fee is paid by the person signing.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/P1KgfydHBgM?is

### Who else solves this today - competitors/alternatives, and why does your approach win?

StickK, Beeminder and Forfeit all put money behind a personal goal, and have done so for years. Habit trackers like Habitica and Streaks do the same job without money, which is why they are easy to abandon.

Two things separate VOW. First, the ladder. Competitors let anyone commit any amount on day one. VOW starts everyone at level 1 and unlocks longer durations, harder goals and larger deposits only through completed commitments.

Second, and this is what the grant funds, identity. In all of these products your record is a row in the company's database, and a user who fails can start over with a new email. None of them gives the user a portable identifier they control. That is not a feature they chose not to build. It is one that needs an identity standard to exist.

### Please provide details about the Technology Readiness Level selected for your existing product

VOW is a finished mobile app, already built and running. The backend is deployed. The app is installed and used on real iPhone and Android devices. A person can create a commitment, receive a PIX charge, pay it, check in with a photo or with Strava, and see the outcome.

It is not launched yet. The app is not in the App Store or Google Play, and payments still run against the payment provider's test environment. The full system has been demonstrated end to end, but with test money and a small closed group of testers.

Reaching the next level needs three things: a production payment account, store approval, and real paying users. None of these are research problems. They are launch steps.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Identity does not live on chain. The key event log (KEL) is held by KERI witnesses off chain. Cardano is the anchor: each relevant event writes a transaction with metadata under label 170, carrying a digest of the event and its sequence number in the log.

Three event types are anchored: AUTH_BEGIN, ATTEST and AUTH_END. Only digests go on chain. No personal data, no biometrics, no credential content. Anyone shown an event can hash it and check that the hash was published in that block.

The user's own wallet signs and pays each anchor, so every anchor is a genuine user transaction, not ours.

Why this fits. The chain gives what KERI cannot give itself: public ordering and a timestamp nobody controls. KERI gives what a chain is bad at: key rotation. A rotated key keeps the same identifier, so a stolen key never forces a new on-chain identity and no past anchor is invalidated. Putting the identity itself on chain would turn every rotation into a migration.

Digest-only anchoring keeps cost low and predictable, which matters because the user pays, not us.

Metadata label 170 is CIP-0170 itself, so the pilot exercises the standard it is meant to test instead of a private format beside it.

The honest limit: the witnesses start under our control, so the log's independence is partial until they are opened to outside parties. The chain anchors are already independent of us, which is exactly why they carry the weight.

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

Target market: people who set themselves a goal and do not follow through. VOW's first market is Brazil, where the app is built, in Portuguese, with PIX as the payment rail. The Cardano identity layer opens a second and narrower market: crypto-native users who already hold a wallet.

Honest position on product-market fit. VOW is built and running, but not launched. It is installed on real devices with a closed group of testers, payments still run against the provider's test environment, and it is not in the app stores. We have no user-level PMF evidence, and we are not going to dress a closed test up as traction.

What we do have is category evidence. Commitment contracts are not a new idea being tested here for the first time. StickK has run since 2008, out of research by Yale economists on commitment devices. 

Beeminder charges users when they go off track and has operated for over a decade. Forfeit runs the same photo-proof mechanic. These businesses persisted for years on paying users, which is the evidence that people will put money behind their own goals.

What VOW adds is the ladder and the feed: consequence that scales with proven history, and public accountability. Whether that combination outperforms the incumbents is what launch will show.

### Applicant name

Bosco Ribeiro

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue comes from commitments that are not kept. Keep the promise and the money returns in full, to withdraw or to commit again. Break it and it stays with VOW. There is no platform fee on top, and the withdrawal fee is the bank's transfer cost passed through without margin.

This is not a wager. There is no chance element and no opponent. The outcome is decided entirely by whether the person did what they said they would do.

The model does not depend on the grant. VOW's costs are hosting and payment processing, covered by the same revenue whether or not the identity layer exists.

The identity layer's own running cost is witnesses, which is small and fixed. Anchoring fees are paid by users, because authentication is part of the ordinary flow rather than an extra step. Usage continues after the grant for the same reason it starts: a person with money committed authenticates in order to check in.

### On-chain identity (CIP-0170) - expected transaction count

670

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without funding, VOW still ships. It works today with ordinary accounts, so self-sovereign identity is not on its critical path. That is the honest answer: this money buys the part that has no business case of its own, and would otherwise be postponed indefinitely.

At a high level, the spend is:

- Engineering, about six to eight weeks, to issue and verify credentials and anchor events on Cardano.
- Proof of personhood, a cost per verified person. This is the largest variable line.
- Witnesses, paying independent operators so the log does not depend only on us.
- Testing and documentation, published openly.

User transaction fees are not funded. Each person signs and pays for their own anchors.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. VOW live at a public URL, with the identity flow inside it: a person connects their own wallet, signs, and anchors when checking in.
2. Anchoring live on mainnet under metadata label 170, evidenced by hashes from independent runs by real users, not by us, covering AUTH_BEGIN, ATTEST and AUTH_END, mapped to flow steps with explorer links.
3. Declared footprint per Standard 4.1: identifier, message tag and team wallets by stake key, all newly deployed for this work.
4. Three KERI witnesses public at threshold two, and a personhood credential (ACDC) issued and verified against a published schema.
5. Public MIT repository with the tagged commit that produced those transactions.
6. Release notes covering architecture, scope and limitations; test evidence bundle with checklist, bug log and security note.
7. Dune tagging live, feeding the Catalyst Impact dashboard.
8. A verifier script and guide, so a third party can check an attestation and find its anchor without asking us.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

200

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

VOW is a mobile app for personal commitments with money at stake. A person promises something concrete, for example running 100 km in 30 days, deposits their own money, and checks in with a photo or a Strava activity to prove they kept it. Keep the promise and the money comes back. Break it and it is lost.

What makes this work is a ladder. Every user starts at level 1, and longer durations, harder goals and larger deposits unlock only by completing what you already committed to. Three failures in a row send you back to level 1.

That whole mechanism rests on one assumption: that an account is one person. Today the only thing enforcing it is our own database. Someone who fails can open a new account and start clean, and we cannot tell the difference. The penalty that gives a commitment its weight is one signup away from being erased.

The second problem is that the record has no life outside us. Someone who kept eight commitments over a year owns nothing they can take anywhere. Their reputation is rows in our database, and it dies if we do.

CIP-0170 addresses both. A verified person holds one portable identifier, controlled by their own keys, with attestations anchored on Cardano. We cannot forge it, and we cannot erase someone's history by deleting a row.

For whom: people who want a commitment to carry real consequence, and any product that needs to know it is dealing with one real human without collecting their documents.

### Supporting links (repo, site, demo)

- https://vowapp.io/
- https://github.com/tecnologiavow-creator      
- https://github.com/tecnologiavow-creator/vow-identidade
- https://www.linkedin.com/in/bosco-ribeiro-4475513a0/
- https://x.com/bosconfts

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

VOW is a working mobile app, not a concept. The backend runs in production. People create a commitment, deposit money by PIX, and check in with a photo or Strava. It is not in the app stores yet.

The Cardano identity part is younger. We have run it, not only designed it. Keys are created on the device. The identifier is published with three witnesses at threshold two. Key rotation changes the key and keeps the same identifier, so a stolen key does not force a person to become a new person.

This ran in a local test environment, not in production. Issuing and checking a credential is the next step. The witnesses are still ours, and opening them to outside parties is real work, not a detail.
