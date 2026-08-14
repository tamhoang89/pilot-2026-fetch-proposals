# [LAB3] Godot × Cardano: Web3 Game Builder

> A hands-on builder pathway helping Godot developers learn Cardano, integrate on-chain features, and turn practical skills into working Web3 game prototypes.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 10
- **Proposer:** `stake1uy02n73u26njqm4lw7xfzavnu2jfpldf7z2e2rwsvtxsa4cvxcfh6`
- **Funding requested:** ₳57,000
- **Last finalized:** 2026-08-14T06:31:05.321000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

**LAB3 combines the blockchain, game development, and delivery capabilities required for this Pilot.**

**Dao Manh Tung — Founder, Project Lead & Blockchain Developer**

- Full-stack, Cardano/Aiken, Godot 4/GDScript & API development

- Funded Proposer — Catalyst Fund 14

- 2nd Place — ST Cardano Hackathon 2025

- 3rd Place — Decentralized LMS with Cardano certificates

- Role: architecture, Godot development, Cardano integration, management & mainnet launch

- GitHub: <https://github.com/dmt041104111003>

**Bui Dinh Giang — Full-stack & Blockchain Developer**

- Cardano/Aiken, backend, DApp & API development

- 2nd Place — ST Cardano Hackathon 2025

- 3rd Place — Decentralized LMS with Cardano certificates

- Role: blockchain/backend development, transaction flows, testing & mainnet deployment

- GitHub: <https://github.com/GiangBui47>

**Nguyen Thu Huong — Technical Documentation & Content**

- Technical writing and developer documentation

- Role: documentation, onboarding guides, testing materials & developer content

- GitHub: <https://github.com/ngthuhuong>

**Track record**

- Catalyst-funded delivery

- Godot × Cardano prototypes

- Cardano DApps & Aiken

- C2VN LMS and developer onboarding infrastructure

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**Conditional give-back pledge:** If the project reaches sustainable commercial revenue, LAB3 pledges 5% of net revenue generated directly from paid Godot × Cardano integration services to the Cardano treasury, capped at the original ₳57,000 grant amount. The pledge activates only after annual project revenue exceeds ₳100,000 equivalent.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Target**

- 500 genuine mainnet transactions generating at least ₳180 in network fees, above the ₳53 program floor.

**Who transacts**

- Godot game players.

- C2VN/Cardano2VN community members.

- Developers joining LAB3 workshops and challenges.

**Why**

- Create/update CIP-0170 identity attestations.

- Record verifiable achievements and meaningful progression.

**Usage**

- Transactions occur only at meaningful identity or gameplay milestones.

- We target approximately 120 real users, averaging 4–5 qualifying interactions per user during the adoption period.

- Repeat transactions come from identity updates, achievements, and progression milestones, supporting the 500-transaction target.

**Adoption**

- Initial users come from C2VN and Cardano2VN.

- Additional users are reached through workshops, playable challenges, Godot content, and open-source distribution.

- The 500 target combines new-user interactions with repeat progression/attestation transactions.

**Integrity**

- Only genuine external-user activity is counted.

- No users are paid or rewarded for measured transactions.

- All activity follows the Transaction Integrity Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

- Existing channels: C2VN LMS, Cardano2VN community, GitHub, YouTube, and our developer/student network.

- Initial target: onboard approximately 120 real users during the Pilot.

- With \~120 users averaging 4–5 meaningful identity/progression interactions per user, the product can support the 500-transaction target.

- Users enter through playable demos, workshops, guided challenges, and Godot-focused technical content.


- Initial acquisition focuses on our existing Vietnam-based communities, reducing cold-start risk.

- GitHub, English technical content, and open-source distribution will extend reach to the wider Godot/Cardano ecosystem.

- Usage will be tracked through distinct external wallets and qualifying mainnet transactions.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Current alternatives:** Developers can combine Godot with general Cardano APIs, SDKs, documentation, and custom backend code, or use blockchain tooling built for other game-development ecosystems.

**Gap:** These approaches require developers to assemble multiple components themselves and provide few complete Godot-focused gameplay references.

**Our advantage:** We combine a playable Cardano-integrated Godot product, reusable open-source components, and practical reference implementations in one ecosystem. Users can experience the integration first, then inspect, modify, and reuse the same code in their own games.

### Please provide details about the Technology Readiness Level selected for your existing product

- C2VN LMS and Cardano2VN are live, publicly accessible products used for Cardano learning, developer onboarding, and community distribution.

- C2VN LMS: <https://lms.cardano2vn.io/>

- Cardano2VN: <https://cardano2vn.io/>

- LAB3 has also developed Godot × Cardano prototypes and open-source examples, providing an existing technical foundation for the Pilot.

- The Pilot does not fund these existing platforms. It builds a new Godot product and CIP-0170 integration on top of this operational ecosystem.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Godot layer**

- Handles gameplay, quests, UI, and high-frequency game state.
- Keeps normal gameplay off-chain for speed and low cost.

**Cardano integration layer**

- Connects Godot with Cardano services.
- Handles wallet interaction, transaction construction/submission, and retrieval of required on-chain data.

**CIP-0170 identity layer**

- Links participating wallets with verifiable player identity/attestations.
- Selected achievements and progression events trigger meaningful on-chain interactions rather than recording every game action.

**Existing infrastructure**

- C2VN LMS supports onboarding and guided user journeys.
- Cardano2VN provides an existing distribution/community channel.
- LAB3's Godot × Cardano work provides the development foundation.

**Measurement**

- Qualifying mainnet transactions will use the Pilot-required transaction label, enabling transparent measurement of real users, activity, and network fees.

- High-frequency gameplay remains off-chain for speed and low cost.

- Cardano is used only for selected events requiring persistent, verifiable identity or attestations.

- CIP-0170 handles the identity/attestation layer rather than ordinary game state.

- This minimizes unnecessary transactions while keeping meaningful achievements independently verifiable.

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

**Target market:** Godot developers, indie game builders, university students, and Web3 newcomers interested in blockchain-enabled games.

**Need:** Moving from a normal Godot game to real Cardano interactions requires developers to combine fragmented blockchain APIs, wallet/on-chain concepts, and game logic.

**Evidence:** LAB3 has already developed Godot × Cardano prototypes and open-source examples, while our existing C2VN learning ecosystem gives us direct access to developers and students interested in Cardano development.

**Initial focus:** Vietnam and our existing Cardano/developer communities, followed by broader open-source Godot communities.

**Product-market validation:** The Pilot will measure real demand through unique users, on-chain interactions, developer usage, and prototype adoption rather than views alone.

### Applicant name

Dao Manh Tung

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

**Open-source core:** The game reference, Godot integration components, and developer resources remain free to maximize adoption.

**Revenue model:** LAB3 can provide paid custom game integrations, technical implementation, developer support, workshops, and advanced solutions for teams that need production deployment beyond the open-source reference.

**Who pays:** Game teams, organizations, and partners requiring customized Cardano integration or implementation support.

**Why usage continues:** The live game remains available after the Pilot, while open-source components allow new developers to build additional Cardano-enabled experiences. Each new application can create recurring user transactions independent of grant funding.

**Long-term goal:** Grow from one reference product into a reusable Godot × Cardano development ecosystem.

### On-chain identity (CIP-0170) - expected transaction count

500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

₳57,000 funds new Pilot work only:

- ₳18,000 — Godot game development: gameplay, quests, UI, and production build.

- ₳14,000 — CIP-0170 & Cardano integration: identity/attestations, wallet and transaction flows.

- ₳8,000 — Backend/API development connecting Godot with Cardano.

- ₳6,000 — Testnet validation, QA, security testing, and mainnet deployment.

- ₳6,000 — Open-source components, reference implementation, examples, and documentation.

- ₳5,000 — User onboarding, launch activities, adoption measurement, and improvements.

Total: ₳57,000.

No funding is allocated to already-completed C2VN/Cardano2VN platforms.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

**Within 3 months, LAB3 will deliver:**

- A playable Godot 4 product available to real users.
- Cardano wallet and transaction flows integrated into Godot.
- CIP-0170 integration for verifiable player identity/attestations.
- End-to-end flow: wallet → gameplay milestone → signed CIP-0170 attestation → confirmed Cardano mainnet transaction.
- Backend/API services for Cardano integration.
- Mainnet deployment with Pilot-required message tag and declared identifiers.
- Open-source Godot × Cardano components, reference implementation, examples and documentation.
- User onboarding through C2VN/LAB3 channels.
- Functional, integration, security and mainnet-readiness testing.
- Live product, tagged repository release, release notes, transaction evidence and Demo Day demonstration.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

180

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**Problem:** Godot developers lack a practical, working example for integrating Cardano into real gameplay. Existing learning resources are fragmented and rarely take users from learning to actual on-chain interaction.

**Target users:** Godot developers, indie game builders, students, and Web3 newcomers.

**Solution:** An open-source Godot game where users complete quests, interact with Cardano, and receive verifiable on-chain achievements and progression. Developers can also use the game as a reference implementation for building their own Cardano-enabled games.

**Outcome:** A working product launched on Cardano mainnet that turns learning into real usage, generates measurable on-chain activity, and provides a reusable foundation for future Godot × Cardano games.

### Supporting links (repo, site, demo)

- https://lab3.io.vn/
- https://www.facebook.com/profile.php?id=61581377131422
- https://projectcatalyst.io/funds/14/cardano-open-ecosystem/c2vn-hydra-on-cardano-complete-step-by-step-dapp-guide
- https://www.cardano2vn.io/
- https://lms.cardano2vn.io/

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

**License:** MIT License.

**Open-source outputs:** Core source code, Godot integration components, reference game, examples, and technical documentation.

**Availability:** Publicly maintained on GitHub beyond the Pilot, allowing anyone to use, modify, fork, and extend the work.

**Third-party IP:** External libraries and Cardano integrations retain their original licenses.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Funder, status, and what it covers

Yes. A previous Catalyst-funded project involved related Godot × Cardano educational and reference work, with members of our team participating. This Pilot proposal does not request funding for previously funded deliverables. It funds new work: a production Godot-based product, CIP-0170 integration, newly deployed mainnet flows, and real-user adoption. There is no duplicate funding of deliverables.

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

- CIP-0170 integration is currently at TRL 2: architecture and use-case design.

- Planned flow: player wallet → CIP-0170 identity/attestation → gameplay milestone → Cardano transaction.

- LAB3 already has experience with Godot, Cardano/Aiken, APIs, and transaction flows.

- New Pilot work focuses on implementing CIP-0170 and integrating it into the Godot product.

- Delivery path: implementation → testnet validation → end-to-end testing → mainnet deployment with real users.
