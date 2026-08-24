# OriLife-Tokenised Produce, Owned by Growers and Consumers

> OriLife recognises an individual tree or fruit by itself with tag or QR, and gives it an identity of its own. 59,461 are registered today but no one of them carries a rule anyone can check on-chain.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 24
- **Proposer:** `stake1u9cxecqjjqzn6y872lemnsjngxrq5mcxun9t0f36kryfp9qx8mt9k`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-24T11:57:00.417000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

GreenSun Tech Inc owns OriLife, submits this proposal and does the engineering. TonFarm is the grower application; DDC DigiTech runs the Dak Lak field deployment.

Engineering, OriLifeTrace org - one role and one public profile each:

\- [Thang Loi](https://github.com/loinguyen1905) - lead engineer, backend, API and deployment

\- [Tien Tuan](https://github.com/tuanzoro2k) - Cardano validators, CIP-0113 transfer logic

\- [Phu Thinh](https://github.com/lrybi) - validators and on-chain anchoring

\- [Minh Thu](https://github.com/thupham03) - mobile and computer vision

\- [Thanh Tung ](https://github.com/thanhtungdo2003)- front end, UIUX and integration.

The transfer logic is built in-house by Tuan and Thinh

Field partner [DDC DigiTech](https://www.facebook.com/61590438448619), Director [Nguyen Hung Son ](https://www.ddcholdings.co/#leadership)is the partner signatory.

[api.orilife.io](http://api.orilife.io) runs in production; the field app is in operational beta with outside testers, keys in the device secure element, no seed phrase. The same engineers have Plutus V3 validators and tokens minted on Preview with Lucid Evolution. Our identity validators carry 653 test declarations, including twenty named attack tests. We claim no audited green build; that is what Milestone 1 buys.

Nobody here has shipped a programmable token on mainnet. Nobody has - the standard is not merged.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

10% of the platform fees we collect from the programmable-token compliance layer, paid to the Cardano treasury each epoch and counted from real transactions only. It starts when the product earns, not at a revenue threshold that may never be crossed, and runs until 120% of the grant has been returned. Reported annually alongside the figures the percentage is calculated from.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

One credit runs the platform: every OriLife service is bought with it, the same in every app built on us. Users buy it with their own money. The network fee is separate: each transaction's ADA leaves the user's own wallet, which is why it counts.

Who pays, step by step:

\- A grower spends credit to give a fruit its identity, then to log care, pest checks, quality.

\- At harvest the grower hands those tokens to a trader, who pays the transfer.

\- A packer splits a fruit token into box tokens, binding old identity to new.

\- An exporter moves boxes to a buyer the issuer verified; the rule runs on-chain.

\- Certificates expire, so rules update; a failed batch is frozen, then unfrozen.

The fee follows from the count, not the reverse: 1,700 x 0.389193 = 661.6, declared as 660. 32 external wallets, min 20.

\- grower registration: 360

\- harvest handover to traders: 480

\- packer splits: 320

\- rule updates on expiry: 240

\- export transfers to buyers: 300

No wallet exceeds 8% of counted fees (limit 35%); no day exceeds the 20% cap. We plan above the Standard's per-epoch floors, 55 ADA then 110.

### How will you reach and onboard real users - and what evidence backs your channels?

One channel first, already staffed. DDC DigiTech runs the pilot deployment in Dak Lak, taking OriLife to durian households through TonFarm - field staff, a five-hectare production site and named cooperative partners on its public gallery. Onboarding happens on visits those staff already make.

Onboarding an issuer: install the app, sign in with no password - keys generate inside the device secure element - and register the plot from the field. We deliberately did not build a seed-phrase flow: a seed phrase is where smallholder onboarding dies. This works on testnet today; it is not a plan.

First two weeks: four cooperatives already registered sign from the day after Demo Day, carrying about 20% of target. Packers onboard in week two, first buyer wallet live by day 14. Issuer and buyer onboarding, not producer count, is the binding constraint - a batch only becomes a transfer once a buyer is live to receive it.

We claim no signed offtake. Counts slip for harvest timing and weather.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=Yh7JQQH69v0

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

Yes

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Primary market: **Durian farmers** in Dak Lak, Vietnam.

The route is stepwise. The infrastructure is built to carry [TonFarm](https://tonfarm.co/gallery) across 12,000 hectares of durian in Dak Lak, then 100,000 of Vietnam's 155,000, then any crop or herd in the food chain - some 70 million bearing trees worldwide.

Demand is a running product, not a paper. The TonFarm grower app (owned by DDC Holdings, powered by DDC DigiTech) covers 462 gardens for 383 named growers: 59,461 registered trees and 3,833 photographs. 168 gardens hold a GACC planting-area code, the licence Vietnam requires to export to China; 119 publish the issuing document. They pay for compliance today, so we replace a bill, not add one.

The deadline is legal, not aspirational. Vietnam's Circular 11/2026/TT-BCT requires unit-level traceability by end-2026; GACC returned \~100 containers of Thai durian in early 2025, costing some USD 14.6m; and the [EU deforestation rules](https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en) reach the same farms - 46.7% of Vietnam's coffee ships to the EU, and breach costs up to 4% of EU turnover.

The gap: that app uses printed QR tags, manual registration, a central record, and anchors to TON and Ethereum. Not one of those 59,461 trees carries a programmable token; not one grower holds a Cardano wallet.

What it proves is the slowest part: about 400 households register their own trees and keep using it.

### Applicant name

GreenSun Tech Inc

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue is per registered asset, not per seat. Issuers - cooperatives, packers, nurseries - pay per plot and per batch, because a batch carrying verifiable compliance clears inspection faster and prices higher. Buyers pay for verification access. Both already pay for the paper version of this.

OriLife is the layer, not the shopfront. Applications sit on top: TonFarm is the first, DDC DigiTech runs the field pilot, and the SDK this grant funds lets anyone build another. That is deliberate - our cost of reaching a new crop or a new country is an integration, not a field team.

Why usage continues after the pilot: the token is the asset record. Once a plot is registered and its batches minted under a policy buyers check, next season must be minted too or it loses the premium the last one earned. Usage follows the growing calendar rather than marketing spend, and rule updates recur as certificates expire.

No customer pays us for this feature today, because it does not exist yet.

### Programmable tokens (CIP-0113) - expected transaction count

1700

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

Identification is deterministic and needs no tag, the record is anchored rather than held by us, and cost is measured not promised, the flow runs without us in it.

1. Transfer logic and third-party path live on mainnet. Evidence: declared footprint and deployment tx.
2. Tokens minted on mainnet by an issuer that is not us, then a repeat run. Evidence: hashes per flow step, explorer links.
3. One transfer the rule approves, one it refuses for an unverified buyer. Evidence: both hashes - enforcement, not capability.
4. Freeze and unfreeze on a live batch; forced transfer and seizure disabled. Evidence: hashes, script.
5. A record verified end to end without our servers; the same fruit resolves to the same identifier across repeated captures. Evidence: anchor hash, retrieval path, test results.
6. A published fee table for every on-chain operation, measured from mainnet.
7. Independent audit and an Apache 2.0 SDK release. Evidence: report with unresolved findings; repo, tag, commit.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

660

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

- https://orilife.io/proposals
- https://api.orilife.io/
- https://tonfarm.co/gallery?page=1
- https://github.com/OriLifeTrace/OriLife-SDK
- https://orilife.io/onchain

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

### Funder, status, and what it covers

Cardano treasury, via an on-chain governance action - status: applied, not funded, no funds received.

A governance action is a spending proposal that ADA holders vote on directly, separate from Catalyst. In 2026 we submitted a treasury withdrawal action titled "OriLife x TonFarm" requesting 2,400,000 ADA. It did not pass.

The two are not the same ask: that action covered the whole OriLife and TonFarm programme, twelve times the 200,000 ADA here and far wider in scope. This proposal is one integration - CIP-0113 programmable tokens - taken to mainnet in three months against a declared fee target. The work proposed here would have been one component of it.

Nothing here was paid for by it, so there is nothing to double-fund. We disclose it because it is a permanent public record on-chain and we would rather name it than have it found.

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 2, stated rather than dressed up. We have no programmable-token validator or policy. Today's asset-token design updates metadata but decides nothing about who may receive the token, and closing that gap is the whole proposal.

What exists is the measurement it rests on: we read transfer costs off four Preview transactions the Foundation's reference implementation produced - 384,092 / 389,845 / 393,013 / 389,823 lovelace, mean 0.389193.

The dependency we do not control: the standard is not merged, and the Foundation's own repository says not to put its reference code on mainnet until the pending audit report lands. So we do not ship their code. We deploy our own implementation and buy an independent audit in Milestone 1 - which is why that audit is a budget line, not decoration.
