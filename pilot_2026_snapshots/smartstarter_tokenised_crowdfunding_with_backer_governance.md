# SmartStarter: Tokenised Crowdfunding with Backer Governance

> Every backer holds tokens that govern how funds are released, for the life of the project. Cardano stablecoin settlement, milestone-gated tranches, backer vote and veto, CIP-0170-attested reviewers.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1u9r7ydxxctwmkj2scwtwhdk32anhr4zgz9329ehsjt55t8quv9pvf`
- **Funding requested:** ₳125,000
- **Last finalized:** 2026-08-19T06:19:47.705000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Reshma Mohan: Founder and Ecosystem Lead, [linkedin.com/in/reshmohan](https://linkedin.com/in/reshmohan). She has ten years in software engineering, previously served as technical writer at Genius Yield, was in Plutus Pioneer cohort 1, and is an elected member of Intersect's Open Source Committee.

Sandeep Sooryaprakash: Principal Engineer and Architect, [github.com/sandykwl](https://github.com/sandykwl). He spent ten years on enterprise backend systems and is a community maintainer with Intersect.

Allen Saji: Lead Frontend Engineer, [github.com/Allen-Saji](https://github.com/Allen-Saji). He has built contract-connected frontends on Cardano and Solana, and builds what a backer actually uses here.

As a team they placed 2nd runner-up and won Best UI/UX at Cardano Summit 2025 in India, and won Community Choice at the Charli3 Hackathon 2026. Individually, Sandeep took 2nd place in the Cardano Summit 2025 hackathon Berlin for Masumi track, and Reshma was a winner at the Cardano Foundation Holiday Hackathon 2026.

Management and support come from Vinumole K B, Director, [linkedin.com/in/vinumolekb](http://linkedin.com/in/vinumolekb), and Ebin Shaji, business development, [linkedin.com/in/0xeby](https://www.linkedin.com/in/0xeby/) .

The founders have funded SmartStarter's development to date. Lambdac has delivered two Catalyst grants: a CIP-1694 workshop in Bengaluru (Fund 12, 1200081) and a Plutus off-chain REST wrapper (Fund 9, 900183).

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge to share 10 per cent of net platform fee revenue with the Cardano treasury for as long as the platform operates, beginning in the first financial year in which Reafino's platform fee revenue exceeds USD 10,000. The pledge attaches to the platform rather than to this grant, and holds whether or not further Catalyst funding follows.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Backers and campaigns generate the fees. A backer contributes and later redeems or is refunded: two counted transactions, at 0.45 ADA each measured on preprod. Votes add transactions only when backers object to a release, so we count none of them. Campaigns add the creator's collection and each tranche release. Identity fees come from attestations, one by the creator at launch and one by each appointed reviewer at each tranche gate. Each anchoring transaction also mints a non-transferable identity beacon, taking its fee to about 0.4 ADA.

Our declared stablecoin target of 520 ADA is about 1,150 transactions at the measured fee. At two counted transactions per backer that is roughly 575 backers across the adoption phase, drawn from the two channels in our go-to-market. The identity target of 126 ADA is about 315 attestations. Both sit inside the programme's Credible band, above the displayed floors: targets for an initial adoption phase, for a platform reaching mainnet inside this same window. The longer ambition is activity at the scale of the established platforms, carried by the same fee that sustains us.

### How will you reach and onboard real users - and what evidence backs your channels?

An organic coffee business in Kerala is lined up as one of our first campaigns: a group ready to raise, execute and fulfil rewards. We reach creators through two channels.

RealFi campaigns: grower groups, self-help groups and cooperatives ready to run initiatives, reached through direct grassroots outreach. The evidence for this channel is presence in those networks. This on-the-ground programme starts in South India and expands after the pilot.

Cardano ecosystem raises: content creators, tooling builders, small projects and meetup organisers operating under constrained funding and steadily losing the means to continue. They raise tranche-gated funding, reached online through the Cardano community, its forums and its events.

The product is permissionless and open to anyone anywhere from day one. Both channels are amplified through the app and our social channels. Onboarding runs in cohorts: the first weeks after go-live go to the first campaigns, with our team on the road.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/aXUpp24PhcQ

### Who else solves this today - competitors/alternatives, and why does your approach win?

Kickstarter and its equivalents hold the money in escrow until a campaign succeeds. But fees reach 8 to 10 per cent, creators can only launch from certain countries, and protection stops once the money releases. Smaller groups use a bank account and a spreadsheet: one person controls the money and contributors cannot enforce a refund. In a plain token sale, funders have no say after the close. On-chain, the closest system we surveyed is Juicebox, which pays a project's treasury in recurring capped cycles, with no check that anything was delivered.

Creators switch on capital efficiency and access: more of the raise stays with the project, and they can launch from anywhere. They stay because the refund, the tranche gate and the backer vote are enforced by the smart contract, not by policy.

### Please provide details about the Technology Readiness Level selected for your existing product

SmartStarter is deployed on Cardano public testnet as a fully functional dApp: the whole flow runs end to end in the browser with any CIP-30 wallet, not through scripts. A visitor can discover a campaign, open its page, connect a wallet, contribute, and receive an automatic refund when a campaign does not reach its target; a creator can create a campaign permissionlessly. Campaigns can be denominated and contributed in a stablecoin: DJED is the asset configured today. The on-chain side is Aiken on Plutus V3, the off-chain side is MeshJS, the current script version is 1.0.0-beta.8, and the validators are covered by 34 unit tests. A recorded demonstration of the current testnet flow is linked above. The product therefore is at TRL 6.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

SmartStarter is an Aiken validator set on Plutus V3 with a MeshJS off-chain layer. Contributions pool at the campaign's script address, and a registry validator holds campaign state, read as a reference input. All-or-nothing is a property of the script, not of our backend: we could not release funds early or refuse a refund even if we wanted to.

The validators are parameterised, so creating a campaign instantiates a template, not new code. The creator fixes the target, deadline, tranche schedule and settlement asset at creation, and those settings live in the campaign datum, so a stablecoin campaign is the same code path as an ADA one. Each contribution is its own UTxO, its datum recording the backer and the amount, so refunds and payouts are decided per contribution on chain, not from a ledger we keep, and the dApp can show backers their own position without trusting our backend.

Tranche release works by veto. Funds move on the schedule fixed at funding unless the backers object; objections are counted on chain, and a release must carry that count, so every tranche decision is auditable. Silence is consent, so inaction cannot stall a project.

The creator anchors a CIP-0170 attestation before a campaign opens, and appointed reviewers anchor when a tranche is judged. Attestations bind to the campaign's identifiers, so identity adds no code to the validator holding funds.

The contracts are public under Apache-2.0 from the grant's award, for their lifetime.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

SmartStarter serves two kinds of raise. The first is RealFi fundraising: independent creators and early-stage ventures, entrepreneurs pre-selling to test demand before committing to production, nonprofits and local initiatives running milestone-based campaigns, and producer groups, cooperatives and self-help groups, for whom 8 to 10 per cent in fees is disproportionate. That shape is worldwide; our first pilot pathways are in India. During the build we observed pilot pathways in Kerala and in the GIFT City ecosystem at Ahmedabad, including organic coffee businesses and women's self-help groups.

The second is project token launches and Web3 raises on Cardano. Across the milestone-funding systems we surveyed, none gives the funders themselves the power to block a release; each places that judgement with people holding no capital at risk. On SmartStarter backers can veto a release, halt a tranche, or by a large majority stop the funding and recover what remains; otherwise money moves on schedule. A campaign can also showcase named reviewers, and nothing gates on them. No platform on Cardano offers this today.

The complaint is the same in both cases: funders pay in and then have no further say. SmartStarter supports any raise where the funders should keep a say, for the life of the project.

We have demonstrated the testnet product at community events, which have led to early pilot and collaboration discussions. Live usage begins with the mainnet launch this grant funds.

### Applicant name

Lambdac Computing Private Limited

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

SmartStarter is Lambdac Computing's crowdfunding product in the Reafino suite. We charge a coordination fee on funded campaigns, targeted at about 2 per cent. The minimum qualifying raise and duration bounds are contract parameters fixed at creation, like the target, deadline and settlement asset, so the fee floor is enforced by the contract. Premium features & campaign tooling will be paid add-ons.

Recurring cost is effectively cloud hosting alone: a frontend for campaign creation, discovery and interaction, and a metadata store run under USD 3,000 a year, so about USD 150,000 of funded campaigns a year breaks even, a small share of the market.

Cooperatives, producer groups and self-help groups sit inside Kerala's federations and peer networks, so one funded campaign is visible to similar bodies nearby.

The grant does not subsidise campaigns or pay users to transact; it funds the engineering to reach mainnet, and the platform then stands on its fee.

### On-chain identity (CIP-0170) - expected transaction count

315

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This grant takes SmartStarter from public testnet to mainnet launch, on a timeline we could not otherwise fund. The release sequence is fixed because the contract holds backers' funds for the life of a project: hardening from testnet feedback, our own adversarial test suite, an internal frontier-AI-assisted security review with its findings published, then a staged rollout.

Of the 125,000 ADA, about 60,000 builds the upgrade: tranche release, the backer veto, attestation flows and hardening. About 40,000 covers pre-launch costs: the security review, infrastructure and mainnet deployment. A commercial audit sits out of proportion to this grant; the published findings and open-sourced contracts keep the review checkable. About 25,000 goes to outreach and contingency.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Stage 1, on public testnet: tranche release on a schedule fixed at funding unless backers object; the backer veto, able to object to a release, halt a tranche, or end the project by supermajority with pro-rata return; CIP-0170 attestation by the creator and appointed reviewers, each minting a non-transferable identity beacon; settlement extended to USDM and other stablecoins available on preprod.

Stage 2, hardened: testnet feedback incorporated, the adversarial suite kept as regression tests, and an internal, frontier-AI-assisted security review published.

Stage 3, on mainnet: live for external users, with creation, contribution and collection in a stablecoin, refund, tranche release and attestation shown by transaction hashes from independent runs; contracts repository public under Apache-2.0 at the reviewed tag; the declared footprint published (script hashes, policy IDs, addresses, attestation identifier, token/NFT names, message tag, team wallets); release notes and video.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

126

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Every way a project raises money today ends the backer's say when the money moves. On Kickstarter, some 20,000 Coolest Cooler backers never received the product, and an Oregon settlement three years later offered $20 against roughly $200 paid. In a Web3 token launch, the sale closes, the team alone decides how the funds are spent, and the buyer has no way to hold the team to its promises. Collective fundraising anywhere runs on one bank account, a spreadsheet of pledges, and trust.

SmartStarter is crowdfunding and token launches where the backers keep their say, and a smart contract drives the whole flow. The contract holds every contribution: if a campaign misses its funding target, everyone is refunded automatically, and the project starts only when the target is met. For a successfully funded project, the contract then releases the money in tranches on a schedule fixed at funding. Each backer holds a proportional token, and money moves on schedule unless the backers restrict it: they can deny a tranche, and a supermajority can end the project and recover what is undisbursed. No party, ourselves included, can move funds outside those rules. The funding flow runs on public testnet today; the tranche layer is what we build next.

Our two integrations answer what backers ask first: stablecoin settlement means the amount pledged is the amount that arrives, and CIP-0170 attestation lets backers check who they are funding: the creator, and any reviewers a campaign showcases.

### Supporting links (repo, site, demo)

- https://reafino.app/dashboard
- https://youtu.be/jEvjPS4L2ik
- https://milestones.projectcatalyst.io/projects/1200081/
- https://projectcatalyst.io/funds/9/developer-ecosystem/restful-wrapper-for-plutus-offchain
- https://lambdac.dev

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

The smart contracts will be open sourced under Apache-2.0 from the grant’s award and for their lifetime, in line with the Fund Rules. The contracts are the Cardano core of the product: the validators that hold and release every contribution, the part a backer or a reviewer needs to read. The platform around them stays proprietary — the frontend, its design and interface work — which holds no funds and enforces none of the funding rules.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1150

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

520

### Current funded commitments

Two disclosures. Neither is SmartStarter work, neither is Catalyst-funded, and neither overlaps this grant's deliverables.

Sandeep Sooryaprakash holds a Community Maintainer Retainer Agreement with Intersect MBO. Under Intersect's Maintainer Retainer Program he is currently assigned to Plutonomicon/plutarch-plutus. Responsibilities include issue and pull-request triage, fixes, CI and dependency upkeep, documentation and contributor mentoring, with no final technical or governance authority. It is an independent engagement of 20 to 40 hours a month paid monthly.

Reshma Mohan has been an elected member of Intersect's Open Source Committee since November 2025, a governance seat carrying a monthly honorarium. The Committee's remit is open-source policy for the Cardano ecosystem; the seat is governance service, not funded delivery.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Stablecoin settlement stands at TRL 4, because the integration is live and validated on our public testnet: a campaign can already be priced and funded in DJED, and our own test suite exercises it. Verifiable identity stands at TRL 2: our integration is designed but not yet built. The metadata schemas, verification path and build plan are written against the deployed contract and are reviewable, and CIP-0170 already has named implementations, Veridian and Reeve. The portal takes a single TRL for the integration pair, so we declared TRL 3, the level between the two. The settlement currency is a setting, not something built into the contract, so adding another stablecoin is configuration and testing rather than a rebuild, and on mainnet we intend to support all Cardano stablecoins.
