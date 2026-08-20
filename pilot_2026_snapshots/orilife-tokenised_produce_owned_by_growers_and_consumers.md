# OriLife-Tokenised Produce, Owned by Growers and Consumers

> OriLife recognises an individual tree or fruit by sight - no tag, no QR code - and gives it an identity of its own. 59,461 are registered today. None of them carries a rule anyone can check on-chain.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 11
- **Proposer:** `stake1u9cxecqjjqzn6y872lemnsjngxrq5mcxun9t0f36kryfp9qx8mt9k`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T05:58:55.530000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

GreenSun-Tech owns OriLife, submits this proposal and does the engineering. TonFarm is the application growers use; DDC Holdings runs the Dak Lak pilot.

Engineering, all in the OriLifeTrace org: Thang Loi , Tien Tuan, Phu Thinh, Minh Thu, Thanh Tung.

Pilot, DDC Holdings: [Nguyen Hung Son](https://www.ddcholdings.co/#leadership), Central Highlands director, on their published leadership page; Tran Huu Cuong, field deployment officer, [fb.com/100064740100482](http://fb.com/100064740100482); Phan Thi Quy Nhi, grower onboarding in Dak Lak.

We already ship the layers underneath. [api.orilife.io](http://api.orilife.io) runs in production. The field application is in operational beta, with keys in the device secure element, no seed phrase. Provenance is anchored to Cardano on Preview with a confirmed transaction. The same engineers have Plutus V3 validators and tokens minted on Preview with Lucid Evolution.

Validator work is not new: our identity validators carry 653 test declarations in source, including twenty named attack tests - a forged policy reusing an asset name, a spend after revocation, two anchor references where the second is the attacker's. We claim no audited green build; that is what Milestone 1 buys.

The gap we are honest about: nobody here has shipped a programmable token on mainnet - nobody has, the standard is not merged yet. A Cardano validator specialist is contracted for the transfer-logic work; the Milestone 1 audit checks it independently.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge to return 120% of the grant to the Catalyst treasury. A smart contract donates about 10% of the platform fees we collect each epoch, counted from real transactions only, until 120% of the grant value has been repaid. It is tied to what the business actually earns, so repayment starts the moment the product works rather than waiting on a revenue threshold that may never be crossed.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who pays, and with whose money. Every operation consumes MAGIC, a prepaid usage credit growers and packers buy with their own cash, like a haulier buying diesel. It is not airdropped and not earned by transacting - fees from our own or sponsored wallets would not count, so our model has none.

Growers pay to register a tree, record a harvest and issue a batch. Packers and exporters pay on transfer and verification. Compliance already costs them money - lab tests, certificates - so this replaces a bill rather than adding one.

Target 660 ADA of counted fees: at the measured 0.389193 ADA per transfer, about 1,700 transactions across 32 external wallets, against a minimum of 20.

- 24 issuers register 15 plots each: 360
- Batch minting: 480
- Batch transfers to packers and exporters: 320
- Certificate and rule updates as documents expire: 240
- Buyer-side acceptance and verification: 300

No wallet exceeds 8% of counted fees, inside the 35% limit, and the largest day stays under the 20% daily cap even at harvest peak. Pacing: 55 ADA in each of the first three epochs, 110 in each of the last three.

Not counted: our own or partner wallets, circular transfers, anything we subsidise.

### How will you reach and onboard real users - and what evidence backs your channels?

One channel first, already staffed. DDC DigiTech runs the pilot deployment in Dak Lak, taking OriLife to durian households through TonFarm - field staff, a five-hectare production site and named cooperative partners on its public gallery. Onboarding happens on visits those staff already make.

Onboarding an issuer: install the app, sign in with no password - keys generate inside the device secure element - and register the plot from the field. We deliberately did not build a seed-phrase flow: a seed phrase is where smallholder onboarding dies. This works on testnet today; it is not a plan.

First two weeks: four cooperatives already registered sign from the day after Demo Day, carrying about 20% of target. Packers onboard in week two, first buyer wallet live by day 14. Issuer and buyer onboarding, not producer count, is the binding constraint - a batch only becomes a transfer once a buyer is live to receive it.

We claim no signed offtake. Counts slip for harvest timing and weather.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=viI7IjKMI2M&t=5s

### Who else solves this today - competitors/alternatives, and why does your approach win?

Paper and PDF certificates are the incumbent - cheap, accepted everywhere, and exactly why a rejected lot cannot be argued: a certificate describes a batch, it is not a property of it.

Closed traceability SaaS moves that record into a vendor database, which works until a buyer wants to verify without trusting the vendor. We bind identity to the individual organism by computer vision, not to a tag that can be peeled off and reapplied.

Plain NFTs solve issuance and lose enforcement: the condition goes back off-chain, and the trust goes with it.

Most CIP-0113 work this round is infrastructure or finance. We arrive from the other side, with registered assets and real holders already in the field, and would rather consume a good SDK than rebuild one.

### Please provide details about the Technology Readiness Level selected for your existing product

The base platform is live and independently checkable.

\- [orilife.io](http://orilife.io) and [api.orilife.io](http://api.orilife.io). The field application is in testing on TestFlight and an internal Android track.

\- Recognition works on individuals. On a 26-tree orchard, top-1 identification is 90% across 166 photographs, and when it commits to a match it is right about 97% of the time.

\- Provenance records are anchored to Cardano today. One anchor transaction is confirmed on [Cardano](https://orilife.io/onchain) - at a fixed 0.3 tADA.

\- Keys generate inside the device secure element, StrongBox or TEE on Android and Secure Enclave on iOS, so there is no seed phrase to lose.

Nothing here has transacted on mainnet. Mainnet is Milestone 1, not a past achievement.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Three layers; only the third is new.

Layer 1 - identity capture (live). We recognise an individual tree or fruit by computer vision, with no tag or QR code, so provenance binds to the organism, not to a movable label.

Layer 2 - anchoring (live). Records are hashed and anchored to Cardano; one anchor transaction is confirmed on Preview at a fixed 0.3 tADA.

Layer 3 - the work. An ordinary token can be sent anywhere, so the rule stays a promise. Cardano's programmable-token standard makes the rule execute instead. Tokens sit under a shared spending script and are tied to their owner by stake credential, so any buyer can derive an issuer's address and check it without asking us. Moving one forces our transfer rule to run in the same transaction: it confirms the seller still controls the issuing identity and the buyer is on the verified list. Both are read on-chain, so eligibility needs no call to our servers - the point, since our servers are what a buyer has no reason to trust.

The verified list is written by the issuer's identity, not ours. We hold no key that can add a buyer.

The freeze flag sits in a shared state UTxO read as a reference input rather than spent, so two issuers selling at once never queue behind each other. Each batch is its own asset, so batches do not contend either.

The standard's third-party path is deployed to allow no forced transfer and no seizure - compliance freezes, never takes - and we publish the script so that is auditable.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

[**OriLife**](https://api.orilife.io/) is for anyone who raises something living and loses the value of its history at the point of sale - growers and cooperatives first, then nurseries, aquaculture and livestock. The identity layer does not change by species.

We are not starting from a slide. TonFarm, an application built on OriLife, publishes a live gallery at [tonfarm.co/gallery](http://tonfarm.co/gallery) counting 383 grower projects, 462 gardens and 59,461 individually registered trees, each card naming the grower - VN01 (DDC Holdings, 741 trees), VN02 (HTX Farmland, 1,550), VN04 (Le Van Vinh, 380) - across 47 pages. Anyone reading this can open it and count.

The limitation in the same breath, because it is why we are applying: none of those 59,461 registrations carries a token, and none of those holders has a Cardano wallet. What it proves is the slow part - roughly 400 households completed a digital registration for their own trees, in the field, and kept using it.

The first deployment goes where commercial pressure is sharpest. Vietnam's durian trade runs to billions of dollars a year, nearly all to China, where one failed residue test can suspend a packing code for every grower behind it. DDC DigiTech runs that pilot deployment in Dak Lak.

We have no measured figure for what a rejected lot costs a producer: the rejection is recorded by the buyer, and nobody in this market measures it. Producing the first measured figure is itself an output of this pilot.

### Applicant name

GreenSun Tech Inc

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue is per registered asset, not per seat. Issuers - cooperatives, packers, nurseries - pay per plot and per batch, because a batch carrying verifiable compliance clears inspection faster and prices higher. Buyers pay for verification access. Both already pay for the paper version of this.

OriLife is the layer, not the shopfront. Applications sit on top: TonFarm is the first, DDC DigiTech runs the field pilot, and the SDK this grant funds lets anyone build another. That is deliberate - our cost of reaching a new crop or a new country is an integration, not a field team.

Why usage continues after the pilot: the token is the asset record. Once a plot is registered and its batches minted under a policy buyers check, next season must be minted too or it loses the premium the last one earned. Usage follows the growing calendar rather than marketing spend, and rule updates recur as certificates expire.

No customer pays us for this feature today, because it does not exist yet.

### Programmable tokens (CIP-0113) - expected transaction count

660

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant the on-chain layer does not get built, and the registry stays centralised - the version buyers have no reason to trust. The grant is an enabler, not end-to-end costs, so we scoped it to on-chain work only. No field operations and no recognition research are billed here; the deployment partner and we carry those.

Budget, eight lines: transfer logic and third-party transfer logic (46,000); issuer identity binding and verified-buyer registry (34,000); minting policy and batch lifecycle (30,000); wallet and signing flow shipped to public app stores (28,000); independent audit before mainnet (22,000); anchoring completion and re-verification (16,000); open SDK and reference integration (14,000); documentation and open-source packaging (10,000). Total 200,000.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Each output is paired with the evidence that proves it, against the pre-filled criteria.

1. Transfer logic and third-party path live on mainnet. Evidence: the full declared footprint - policy IDs, script hashes, addresses, token names, message tag, team wallets - and the deployment tx.
2. Tokens minted on mainnet by an issuer that is not us, then a repeat run. Evidence: hashes mapped to each flow step, explorer links.
3. One transfer the rule approves, one it refuses for an unverified buyer. Evidence: both hashes - enforcement, not capability.
4. Freeze and unfreeze on a live batch; forced transfer and seizure disabled. Evidence: hashes, published script.
5. Independent audit. Evidence: full report with unresolved findings; test bundle - checklist, bug log, security note.
6. SDK and reference integration, Apache 2.0. Evidence: repo URL, tag and commit, release notes stating scope and limits.
7. Live demo and Q&A at Demo Day, same identifiers. Evidence: product URL, walkthrough video.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

1700

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

A living thing has no identity that outlives the person who raised it. A tree, a hive, a herd, a harvest batch - the history exists, but it sits in a buyer's spreadsheet or a vendor's database. When a lot is rejected, repriced or copied, the producer has no portable claim to argue with and nothing to borrow against.

[OriLife](https://orilife.io/en) gives the organism an identity of its own. We recognise an individual tree or fruit by sight, with no tag and no QR code, so identity binds to the thing rather than to a label anyone can move. One schema covers every species: a durian and a coffee tree differ in parameter values, not in code.

The unfinished half is on-chain, and it is all we are asking for. That identity is recorded and anchored to Cardano today, but it carries no rules - whoever holds the token can send it anywhere, so the condition stays a promise the platform makes. We want the rule to travel with the asset: a batch moves only to a buyer its issuer has verified, rules update when a certificate expires, and a batch that fails testing can be frozen by its issuer. Frozen, not taken - we configure the standard's third-party path to allow no seizure at all.

Why on-chain, honestly: we are the platform. We hold the producer's record and sell verification of it to the buyer on the other side of the same trade. No buyer has a good reason to accept the seller's vendor as keeper of the ledger, and no producer should have to.

### Supporting links (repo, site, demo)

- https://orilife.io/proposals/pitchs
- https://api.orilife.io/
- https://tonfarm.co/gallery?page=1
- https://github.com/OriLifeTrace/OriLife-SDK
- https://fb.com/61590438448619

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

TRL 2, stated rather than dressed up. We have no programmable-token validator or policy. Today's asset-token design updates metadata but decides nothing about who may receive the token, and closing that gap is the whole proposal.

What exists is the measurement it rests on: we read transfer costs off four Preview transactions the Foundation's reference implementation produced - 384,092 / 389,845 / 393,013 / 389,823 lovelace, mean 0.389193.

The dependency we do not control: the standard is not merged, and the Foundation's own repository says not to put its reference code on mainnet until the pending audit report lands. So we do not ship their code. We deploy our own implementation and buy an independent audit in Milestone 1 - which is why that audit is a budget line, not decoration.
