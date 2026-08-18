# IdentiKit - CIP-0170 Identity SDK for React Native

> IdentiKit  a reusable, open-source CIP-0170 identity toolkit for React Native.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1u9wcuh0vyw9r6aacuwkufx8gaq7numn8dazx4u0fefyqneslmsep4`
- **Funding requested:** ₳180,000
- **Last finalized:** 2026-08-18T07:53:42.434000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Lido Nation Foundation is the team behind Catalyst Explorer (open-sourced by community vote in Fund 12, iterating toward 2.0 with AI tooling and a public API) and [lidonation.com](http://lidonation.com). 

Delivery is led by Darlington Wleh (Lead Developer & Architect), driving IdentiKit's architecture and project delivery, and Titi (Supporting Developer), who leads the Lido Developer team in Nairobi.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Transacting wallets = real Blockchain Centre Nairobi event attendees using the reference app to RSVP, check into events, and receive/verify prize and attendance credentials. The centre runs 200-300 attendees/month across all event types (meetups, hackathons, bootcamps, community nights), of which \~60/month are Cardano-specific programming. The check-in flow applies to every event type, not only Cardano meetups.

Each attendee generates 2-3 mainnet transactions per event through the  flow: 

1. an RSVP/identity anchor
2. a check-in attendance credential (CIP-0170 credential with metadata), 
3. 3 for prize-eligible events, a badge/reward mint gated on the verified credential. 

These are richer-than-minimal transactions (credential metadata + token actions), averaging \~0.3 ADA in network fees each.

Wallet target: 

\~10-15 distinct external wallets per 5-day epoch, conservative against the \~60/month Cardano-specific baseline but comfortably above the program's distinct-wallet minimum (one wallet per 10 ADA of floor ≈ 10 wallets). 

Transaction rhythm: 

\~50 transactions per epoch sustained across the window, driven by the center's weekly event calendar.

### How will you reach and onboard real users - and what evidence backs your channels?

BC NBO already runs recurring developer bootcamps, hackathons, and monthly Cardano meetups in Nairobi with an established local audience (\~60 Cardano-specific attendees/month, 200-300 center-wide). We'll run IdentiKit onboarding workshops directly through these existing programs, publish docs/examples, and promote through LidoNation's existing Catalyst/governance-tooling audience ([catalystexplorer.com](http://catalystexplorer.com), [lidonation.com](http://lidonation.com)).

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/aQJ_I7kYb1g 

### Who else solves this today - competitors/alternatives, and why does your approach win?

No existing open-source React Native library implements CIP-0170 specifically. Teams currently hand-roll identity/credential logic per-app or use generic wallet-connect libraries with no identity semantics. Our approach wins because: 

1. It's spec-native to CIP-0170, (2)

2. It ships with a real, live reference app and recurring event data 

3. Our team already maintains production open-source Cardano tooling (Catalyst Explorer) with a track record of sustained post-funding maintenance.

### Please provide details about the Technology Readiness Level selected for your existing product

The business has been operational for over a year but current does check-in on [lu.ma](https://lu.ma) and offline, with no on-chain identity component. We are targeting a working, mainnet-verified prototype (TRL 6-7) by M1, and repeated real-world usage (TRL 8-9 operational validation) through the M2 adoption window.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

IdentiKit wraps CIP-0170's identity data model so a wallet-holding user can anchor and verify claims on-chain without custom per-app plumbing. 

Reference flow: RSVP → event check-in scan → IdentiKit submits a mainnet transaction anchoring an identity/attendance credential tied to the user's wallet → conditional prize/reward step reads that credential before releasing a token/NFT. This is a repeatable, real-world-triggered flow, giving genuine, recurring on-chain identity usage tied to BC NBO's actual event calendar.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Primary target: Cardano/React Native developers building identity-dependent community and event products. Immediate first users: Blockchain Centre Nairobi: an active Kilimani, Nairobi event space and ecosystem-growth partner running recurring meetups, hackathons, and dev bootcamps (venue capacity 150+), part of the Two Lovelaces / LidoNation / WADA / Cardano Foundation / Midnight network.

BC NBO's Cardano-specific programming averages \~60 attendees/month, with the wider center seeing 200-300/month across all event types. This is a real, recurring user base to validate IdentiKit from day one, plus a built-in channel (BC NBO's own dev training programs) to reach other Nairobi/African Web3 builders.

### Applicant name

Lido Nation

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

IdentiKit is a free/open-source (npm package: `identikit`); sustainability comes from: 

1. Blockchain Centre Nairobi's own operating revenue (event rental + ecosystem growth program fees) will fund continued development real-world usage. 

2. LidoNation's existing sustainable maintenance model (as demonstrated with Catalyst Explorer) will be extended to IdentiKit.

3. optional paid integration support for other adopting teams.

### On-chain identity (CIP-0170) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding turns a one-off internal integration into a maintained, documented, open-source library other Cardano teams can adopt. 

Spend: IdentiKit engineering, documentation/examples, developer marketing and onboarding workshops, integration support for early adopter teams, and tax/compliance overhead. (Reference mobile app development is contributed in-kind by Lido Nation Foundation, not funded by this grant.)

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

The big idea for the 3-month window to reach mainnet

- Published open-source CIP-0170 React Native SDK:
  - IdentiKit (npm package `identikit`, MIT/Apache-2.0, documented) covering identity registration, credential issuance, verification.
- Reference example app implementing RSVP → check-in → credential-anchoring → conditional reward flow.
- At least one verified, repeatable end-to-end mainnet transaction (multiple independent runs), with explorer links.
- Declared footprint (script hashes, policy IDs, addresses, team wallets) published.
- Release notes, technical walkthrough video, test evidence bundle, repo + tagged commit.
- Live demo at Demo Day!

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

96

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

We're building IdentiKit, an open-source React Native SDK implementing CIP-0170 on-chain identity, letting any Cardano community app issue, anchor, and verify wallet-linked identity credentials (e.g. "this wallet attended this event," "this wallet holds this role") with a few lines of code. Today, every team wanting on-chain identity in a mobile app builds this integration from scratch. There is no reusable, CIP-0170-compliant React Native library. We solve this for Cardano dApp developers building community, event, loyalty, or membership products. We will be the first proof and consumer of the library through Blockchain Centre Nairobi's community app (RSVP, event check-in, prize distribution). Blockchain Centre community app will be IdentiKit's reference implementation in production. We will not be budgeting any line item in this proposal to build the blockchain centre app.

### Supporting links (repo, site, demo)

- https://www.lidonation.com
- https://www.catalystexplorer.com
- https://www.blockchaincentrenbo.com
- https://www.catalystexplorer.com/en/proposals/catalystexplorer-20-ai-powered-exploration-proposal-tinder-funding-transparency-at-your-fingertips-by-lido-nation-f13/details
- https://gitlab.2lovelaces.io/blockchaincentrenbo/identikit

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

Yes, MIT/Apache-2.0 licensed, published to npm.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Current funded commitments

Darlington is a community maintainer for dbsync. \
Emmanuel is on the developer experience working group at intersect. Hey was also a developer advocate but his tenure is over. 

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Starting at TRL 1-2 (concept/requirements), targeting a working, mainnet-verified prototype (TRL 6-7) by M1, and repeated real-world usage (TRL 8-9 operational validation) through the M2 adoption window.
