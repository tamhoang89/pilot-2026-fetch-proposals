# On-Chain Identity for the Blockchain Centre Nairobi Communit

> Adding Cardano on-chain identity RSVPs, check-ins, and attendance credentials to Blockchain Centre Nairobi's live community app.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 12
- **Proposer:** `stake1u9wcuh0vyw9r6aacuwkufx8gaq7numn8dazx4u0fefyqneslmsep4`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-18T09:20:06.137000+00:00

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

Transacting wallets = Blockchain Centre Nairobi attendees using the community app to RSVP, check into events, and receive/verify attendance credentials. The center runs 200-300 attendees/month across all event types (meetups, hackathons, bootcamps, community nights), \~60/month Cardano-specific; the check-in flow applies to every event type.

\
Each attendee generates 2-3 mainnet transactions per event: (1) an RSVP/identity anchor, (2) a check-in attendance credential (CIP-0170), (3) for select events, a non-transferable achievement badge mint gated on the verified credential. Fees average \~0.3 ADA per transaction; users sign and pay fees from their own wallets.

\
Targets: 10-15 distinct external wallets per 5-day epoch (above the \~10-wallet program minimum), \~50 transactions/epoch sustained by the weekly event calendar - no spikes, no synthetic activity.

\
Channels: \~80% from BC NBO's existing recurring events via the app; \~20% from teams adopting the open-sourced library.

### How will you reach and onboard real users - and what evidence backs your channels?

BC NBO already runs recurring developer bootcamps, hackathons, and monthly Cardano meetups in Nairobi with an established local audience (\~60 Cardano-specific attendees/month, 200-300 center-wide). Every attendee at these events is onboarded to the app's wallet-linked check-in at the door — user acquisition is the center's existing event calendar, not a new channel we must build. We'll also publish docs/examples for the open-sourced library and promote through LidoNation's existing Catalyst/governance-tooling audience ([catalystexplorer.com](http://catalystexplorer.com), [lidonation.com](http://lidonation.com)).

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Community platforms today ([lu.ma](http://lu.ma), Meetup, Eventbrite) manage RSVPs and check-ins but leave no verifiable, portable record — attendance and roles are locked in a silo with no on-chain identity semantics. No Cardano community app offers CIP-0170 wallet-linked credentials. Our approach wins because: 

1. We integrate into a product that is already live with recurring real-world usage — no user bootstrap risk.
2. The integration is spec-native to CIP-0170, not a generic wallet-connect workaround.
3. Our team already maintains production open-source Cardano tooling (Catalyst Explorer) with a track record of sustained post-funding maintenance.

### Please provide details about the Technology Readiness Level selected for your existing product

The existing product is the live Blockchain Centre Nairobi community web app: it runs the center's real event operations today (RSVP and check-in, currently via [lu.ma](http://lu.ma) and the web app backend), with 200-300 attendees/month across all event types. It currently has no on-chain component; a native mobile app is on the roadmap (contributed in-kind, not funded here). The proposed CIP-0170 integration itself is at TRL 1-2 ( see below).

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

Primary users: the existing Blockchain Centre Nairobi community — attendees of its recurring meetups, hackathons, bootcamps, and community nights. BC NBO is an active Kilimani, Nairobi event space and ecosystem-growth partner (venue capacity 150+), part of the Two Lovelaces / LidoNation / WADA / Cardano Foundation / Midnight network.

BC NBO's Cardano-specific programming averages \~60 attendees/month, with the wider center seeing 200-300/month across all event types. This is a real, recurring user base already using the app's event flow today — the demand is proven attendance, not projected adoption. Secondary audience: other Cardano teams who adopt the open-sourced integration library.

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

Without this funding, the app stays a conventional web2 event tool — the on-chain identity layer would not get built. Funding pays for integrating CIP-0170 into the live app and operating it through real events; as a by-product, the integration is open-sourced as a reusable library for the ecosystem.

Spend: CIP-0170 integration engineering, user onboarding and adoption at the center's events, open-source documentation and packaging, project management, and tax/compliance overhead. (Broader app development, including the native mobile app, is contributed in-kind by Lido Nation Foundation, not funded by this grant.)

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Deliverables:

- CIP-0170 identity integration live in the Blockchain Centre Nairobi community app: wallet-linked RSVP, check-in, and attendance credentials in production use.
- The integration's internal library open-sourced (npm package `identikit`, MIT/Apache-2.0, documented) as a reusable by-product for other Cardano teams.
- At least one verified, repeatable end-to-end mainnet transaction (multiple independent runs), with explorer links.
- Declared footprint (script hashes, policy IDs, addresses, team wallets) published.
- Release notes, technical walkthrough video, test evidence bundle, repo + tagged commit.
- Live demo at Demo Day.

**Budget (140,000 ADA total)**

- CIP-0170 integration engineering (Darlington + Titi): 70,000
- User onboarding & adoption at BC NBO events: 30,000
- Open-source documentation & packaging of the integration library: 12,000
- Project management: 12,000
- Tax withholding & regulatory compliance on project labor: 16,000
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

We are adding CIP-0170 on-chain identity to the Blockchain Centre Nairobi community app — a live consumer application serving a real, recurring community in Kilimani, Nairobi. Today the app's event flow (RSVP and check-in, currently run through [lu.ma](http://lu.ma)) has no on-chain component: attendance leaves no verifiable record, and community roles and achievements can't follow a member across events. This funding adds wallet-linked identity to that existing product: members RSVP with a Cardano wallet, check in at the door, and receive a non-transferable attendance credential anchored on mainnet — a portable, verifiable record of participation. The integration will be built as a cleanly separated internal library that we open-source (npm: `identikit`) so other Cardano teams can reuse it, but the funded deliverable is the integration into our live app for our existing users.

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
