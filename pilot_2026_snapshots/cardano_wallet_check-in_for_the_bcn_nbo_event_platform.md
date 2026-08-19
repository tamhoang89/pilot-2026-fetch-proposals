# Cardano Wallet Check-In for the BCN NBO Event Platform

> Adding CIP-0170 on-chain identity to the live reservations & check-in service used by external Web3 communities at a commercial Nairobi venue.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 20
- **Proposer:** `stake1u9wcuh0vyw9r6aacuwkufx8gaq7numn8dazx4u0fefyqneslmsep4`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-19T10:15:26.070000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Lido Nation Foundation is the team behind Catalyst Explorer (open-sourced by community vote in Fund 12, iterating toward 2.0 with AI tooling and a public API) and [lidonation.com](http://lidonation.com). 

Delivery is led by Darlington Wleh (Lead Developer & Architect), driving the integration's architecture and project delivery

- GitHub: <https://github.com/profd2004> · 

- LinkedIn: <https://www.linkedin.com/in/profd2004/> 

Emmanuel Shikuku Titi (Supporting Developer), who leads the Lido Developer team in Nairobi

- LinkedIn: <https://www.linkedin.com/in/emmanuel-shikuku-titi/>.

Organization references: <https://www.lidonation.com> · <https://www.catalystexplorer.com>

Active funded project disclosure: LidoNation's Fund 14 "Cardano Hub NBO — Grassroot Community Building" (<https://www.catalystexplorer.com/en/proposals/cardano-hub-nbo-grassroot-community-building-by-lidonation-f14/details>) is funded and active ran by Herine Omollo (<https://www.linkedin.com/in/herine-omollo-319a6033b/>) a long time Cardano Community leader in Kenya. It funds community programming (meetups, hackathons, education) at the venue. 

This proposal funds a distinct deliverable, the CIP-0170 identity integration in the venue's check-in platform, with no overlapping budget lines or scope.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Transacting wallets = attendees of the external communities that book Blockchain Centre Nairobi - Cardano, Midnight, Avalanche, and Binance hold recurring meetups; SUI, Base, and SingularityNet have also hosted events. The venue has hosted 97 public events since Apr 24, 2025 (\~6/month); wallet check-in applies to every event at the space, whichever community books it.

Each attendee generates 2-3 mainnet transactions per event: (1) an RSVP/identity anchor, (2) a check-in attendance credential (CIP-0170), (3) for select events, a non-transferable achievement badge mint gated on the verified credential. Fees average \~0.3 ADA per transaction; users sign and pay fees from their own wallets.

Targets: 10-15 distinct external wallets per 5-day epoch (above the \~10-wallet minimum), \~50 transactions/epoch sustained by the booking calendar - no spikes, no synthetic activity.

On-chain identity (CIP-0170) — expected transaction count: 280

On-chain identity (CIP-0170) — fee target (ADA): 84 ADA (the program floor for a 140,000 ADA award; 280 x \~0.3 ADA clears it).

Channels: \~80% from events booked by external communities; \~20% from teams adopting the open-sourced library.

### How will you reach and onboard real users - and what evidence backs your channels?

The venue has hosted 97 public events since Apr 24, 2025 for multiple external communities; every attendee of every booked event checks in through the venue's platform, so user acquisition is the existing booking calendar, not a new channel. The on-site team  runs a wallet-onboarding desk at the door.

**First two weeks after mainnet launch (M1):** 

- **Week 1:** Deploy wallet check-in at the first 2-3 booked events with a staffed desk and guided wallet setup; targets: 25-35 onboarded, 15+ distinct external wallets, 40-60 CIP-0170 transactions. 

- **Week 2:** Extend to the next external community's event, email the [lu.ma](http://lu.ma) RSVP list with the wallet option, run organizer walkthroughs; cumulative: 50+ onboarded, 25+ wallets, 90-120 transactions. Owners: on-site venue team + Nairobi dev team. We'll also publish docs for the open-sourced library and promote via [catalystexplorer.com](http://catalystexplorer.com) and [lidonation.com](http://lidonation.com).

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Paper lists & platforms like [lu.ma](http://lu.ma), Meetup, & Eventbrite are per-event silos. The cost: 

1. Organizers must prove attendance to sponsoring foundations;.

2. The venue sells "measurable traction" reporting as a paid deliverable; verifiable check-ins are that product.

3. Attendees repeat across communities; only a wallet-anchored credential is a record all parties can verify.

No venue or community platform offers CIP-0170 wallet-linked credentials today. We win because: 

1.  We integrate into a live product with recurring real-world usage - no user bootstrap risk.

2. The integration is spec-native to CIP-0170, not a wallet-connect workaround.

3. We maintain production open-source Cardano tooling (Catalyst Explorer) with sustained post-funding maintenance.

### Please provide details about the Technology Readiness Level selected for your existing product

The existing product is the live Blockchain Centre Nairobi reservations and check-in platform: it runs the venue's real event operations today (RSVP and check-in, currently via [lu.ma](http://lu.ma)) across 97 public events since April 24, 2025 (\~6/month) for multiple external communities. It currently has no on-chain component; a native mobile app is on the roadmap (contributed in-kind, not funded here). The proposed CIP-0170 integration itself is at TRL 1-2 (see below).

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The app's identity layer wraps CIP-0170's identity data model so a wallet-holding member can anchor and verify claims on-chain without custom plumbing.

Production flow: RSVP → event check-in scan → the app submits a mainnet transaction anchoring an identity/attendance credential tied to the member's wallet → the app can later verify that credential for identity-gated features (e.g. member roles, bootcamp certification). Credentials are non-transferable attendance badges with no redeemable value during the measurement period. Users sign transactions and pay network fees from their own wallets. This is a repeatable, real-world-triggered flow (not a synthetic tx), giving genuine, recurring on-chain identity usage tied to BC NBO's actual event calendar.

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

Primary users: attendees of the external communities that book the venue: Cardano, Midnight, Avalanche, and Binance communities hold recurring monthly/quarterly meetups at the space, with SUI, Base, and SingularityNet among the communities that have also hosted events there, plus open events (coworking days, mixers, trivia nights). These are not Lido Nation's users: each community is an independent organization whose members check in through the venue's platform because their event happens there.

Evidence of demand: 97 public events hosted since April 24, 2025 (\~6/month), visible on the venue's public calendar ([blockchaincentrenbo.com/events](http://blockchaincentrenbo.com/events); e.g. a Cardano meetup on Aug 27, coworking and community nights weekly). Organizer-side demand is verified attendance reporting to sponsors and foundations; attendee-side demand is a cross-community participation record (bootcamp graduates proving completion, regulars carrying reputation between communities). Secondary audience: other Cardano teams who adopt the open-sourced integration library.

### Applicant name

Lido Nation

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The community app is core operating infrastructure for Blockchain Centre Nairobi; sustainability comes from:

1. BC NBO's own operating revenue (event rental + ecosystem growth program fees) funds the app's continued operation and development.

2. LidoNation's existing sustainable maintenance model (as demonstrated with Catalyst Explorer) extends to the app's identity integration and the open-sourced library.

3. The identity layer increases the app's value to the center's programs (verifiable attendance for bootcamp certification, member reputation), reinforcing the case for ongoing investment.

### On-chain identity (CIP-0170) - expected transaction count

280

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, the app stays a conventional web2 event tool, the on-chain identity layer would not get built. Funding pays for integrating CIP-0170 into the live app and operating it through real events; as a by-product, the integration is open-sourced as a reusable library for the ecosystem.

Spend: CIP-0170 integration engineering, user onboarding and adoption at the center's events, open-source documentation and packaging, project management, and tax/compliance overhead. (Broader app development, including the native mobile app, is contributed in-kind by Lido Nation Foundation, not funded by this grant.)

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

The big ideas for:

- CIP-0170 identity integration live in the Blockchain Centre Nairobi reservations/check-in platform: wallet-linked RSVP, check-in, and attendance credentials in production use at booked events.

- The integration's internal library is open-sourced (npm package `identikit`, MIT/Apache-2.0, documented) as a reusable by-product for other Cardano teams.

- At least one verified, repeatable end-to-end mainnet transaction (multiple independent runs), with explorer links.

- Declared footprint (script hashes, policy IDs, addresses, team wallets) published.

- Release notes, technical walkthrough video, test evidence bundle, repo + tagged commit.

- Live demo at Demo Day.

**Budget:**

- CIP-0170 integration engineering (Darlington + Titi): 70,000

- User onboarding & adoption at BC NBO events: 30,000

- Open-source documentation & packaging of the integration library: 12,000

- Project management: 12,000:  

- Tax & regulatory compliance: 16,000 

- Total: 140,000

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

90

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

We are adding a "check in with a Cardano wallet" option to the Blockchain Centre Nairobi platform, the live reservations and check-in service the venue operates as part of its commercial event-space business. BC NBO is a fully-equipped 100+ capacity venue in Kilimani, Nairobi, booked by independent Web3 communities for their own events: Cardano, Midnight, Avalanche, and Binance communities hold recurring (monthly/quarterly) meetups there, and SUI, Base, and SingularityNet communities have also hosted events at the space. Check-in and reservations are a service the venue provides to every organizer that books it; the venue has hosted 97 public events since April 24, 2025 (\~6/month). Today that check-in flow runs through our backend and [lu.ma](http://lu.ma) and leaves no verifiable record: 

- organizers cannot prove attendance to their sponsors and ecosystem foundations

- attendees cannot carry a participation record across the communities they belong to. 

This funding adds CIP-0170 on-chain identity to the platform: any attendee of any event at the space can check in with a Cardano wallet and receive a non-transferable attendance credential anchored on mainnet. The big idea is to create one portable record that works across every community using the venue. The integration is built as a cleanly separated internal library we open-source (npm: `identikit`), but the funded deliverable is the integration into the venue's live platform.

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

TRL 1-2 (concept/requirements) today; mainnet-verified prototype (TRL 6-7) by M1; repeated real-world usage (TRL 8-9) through the M2 window.

Specs: 

- Credential: a CIP-0170 claim with venue/event/community IDs, timestamp, and type (rsvp | attendance | achievement), signed by the venue's issuing key; the attendee wallet is the subject. 

- Non-transferable: bound to the wallet's staking credential via a mint-to-subject-only policy; a transferred token is invalid. 

- Event-to-transaction mapping:

  -  RSVP: identity-anchor tx (\~0.2 ADA)

  - check-in: attendance-credential tx (\~0.3 ADA)

  - select events: gated badge mint (\~0.4 ADA). 

Users sign and pay their own fees. Footprint (issuing key hash, policy IDs, addresses) published at M1.
