# Signed Delivery Attestations for Restaurant Supply Chains

> Restaurants sign delivery notes before they can check them, so missing goods get invoiced anyway. We turn each delivery step into a signed on-chain attestation neither side can rewrite.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 18
- **Proposer:** `stake1u9h0faq043ged3ffnwjfy86hy0awvyxdly5mry4lmtqejvgyglfg2`
- **Funding requested:** ₳128,000
- **Last finalized:** 2026-08-18T18:14:45.233000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Samuel Schneider — CEO/CFO. Serial entrepreneur in medical devices and Industry 4.0, building combined software and hardware systems including UWB-based real-time location for risk prevention in regulated environments. That is precisely the problem this project faces at the dock: binding a physical event to a verifiable digital record. Law degree in international and European law, master's in entrepreneurship (IAE Bordeaux), MIT Professional Education certificate in machine learning, one-year fellowship at École Polytechnique (2022). The legal training is not decoration — GDPR exposure of on-chain commitments and the French e-invoicing mandate are live design constraints.

Armand Collier — CTO. 10 years in software: JavaScript, C++, backend, frontend, algorithms. Owns the off-chain layer — TypeScript transaction construction, salted commitment handling, chain indexing — and the reception app that must work in 30 seconds at 6am.

Dani Schneider — Operations and distribution. 22 years in food service, more than 20 establishments run. He is why our launch establishments signed and why our distributor conversations are warm. He also defines what "usable at 6am" means.

Cardano experience, plainly: none of us had shipped a Cardano contract before this project. Our Aiken validator is written and working — full state machine, 66 passing tests, Plutus V3 \[REPO+COMMIT\]. Mainnet deployment and review are what the build payment funds.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

5% of net attestation-layer revenue — supplier subscriptions and receivables-financing fees — paid annually in ADA to a Cardano treasury address. Starts the first full year that revenue exceeds €250,000; runs five years or until cumulative payments reach 130% of the grant, whichever comes first.

No grant repayment: a pledge tied to revenue the integration generates is one we can honour.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Split per §3.2 — existing users 45% (\~540 attestations), new users 55% (\~660).

Existing users cannot carry the target, and the earlier phrasing was misleading. Our two establishments place \~10 orders a day, but an order only becomes an attestation when its supplier is onboarded too. They buy from 4–12 suppliers each; with two suppliers live at launch, about a third of that flow qualifies. Supplier onboarding, not buyer volume, is the binding constraint.

Growth is structural, not aspirational: the milestone requires 8 distinct external wallets and no wallet above 35% of counted fees. Two buyers satisfy neither, whatever the fee total.

Channels and volumes. Two distributors in active discussion, one national, each serving hundreds of restaurants. Our co-founder has 22 years in the trade, 20+ establishments run, and knows their executives personally. Target: 4 new establishments and 3 further suppliers by week 3, \~4 orders a day each.

First two weeks. Both establishments and both suppliers attest from the day after Demo Day sign-off, no ramp — weeks 1–2 carry \~20% of target. New onboarding starts week 2, first new establishment live by day 14.

### How will you reach and onboard real users - and what evidence backs your channels?

Supplier-led distribution is our primary channel and the one that compounds. A regional distributor serves hundreds of establishments; onboarding it puts the flow in front of its whole customer base, and it has its own reason to push — a sealed manifest protects it in disputes it currently absorbs. We are in active discussion with two distributors already serving our launch establishments, one a national player.

This is warm access, not cold outreach. Our co-founder has 22 years as a restaurateur and has run more than 20 establishments; he knows these distributors' executives personally, and that network is our distribution.

Timing helps: France's e-invoicing reform took effect on 1 September 2026, so the whole trade is restructuring procurement flows this year.

Onboarding friction is real. Each party holds a self-custodied wallet and small ADA float, because sponsored fees would not count as adoption. We provision wallets inside existing onboarding, custody stays with the user.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Ordering apps (Choco, Rekki and local rivals) digitise the order and stop at the door: reconciliation is still a supplier-issued note, signed unverified. Management software (Easilys, Marketman) catches discrepancies at inventory, long after the claim window closed. EDI and supplier portals serve chains able to impose a format; independents are not.

None of them can be neutral. Each stores the record in a database owned by one commercial party. A supplier will not accept the buying side owning the ledger of its shortfalls, and a factor will not finance a receivable proven only by a vendor's database.

We win on sequence — the supplier seals its manifest before the buyer declares — and on custody: nobody owns the record, including us. That is what makes suppliers willing to be measured.

### Please provide details about the Technology Readiness Level selected for your existing product

Our procurement application is live and in commercial use. Two establishments place their orders through it across their identified suppliers, representing €400–500k of annual purchasing volume between them. This is production use by paying-side users solving a real operational problem, not a pilot deployment or a demo environment.

The product is not on a blockchain today — it is a conventional SaaS, live in its own market. Ordering, supplier catalogues, order history and delivery notes all run through it every week.

That is precisely what makes this grant an integration rather than a launch: the users, the suppliers and the order flow already exist. What does not exist is the trust layer, and that is what we are asking to build.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Each order is one UTxO at our validator, carrying a unique state token and inline datum, running through four states: Created, Accepted, Shipped, Disputed. Each transition is submitted by the party entitled to it and signed by its key.

One order, one UTxO, one token. Orders never contend for the same UTxO, so the eUTxO concurrency problem that forces batching in most Cardano designs never arises

The critical property is ordering. The supplier's manifest hash is sealed when the truck departs, before the buyer declares. The buyer then attests independently, unable to alter the opposing commitment, and neither can rewrite it. The validator enforces that sequence, and enforces 0 &lt;= attested_received &lt;= sealed_manifest: the buyer cannot attest owing more than the supplier claimed, and has no incentive to attest less, the attestation being signed and admissible in arbitration. Every state also has an exit needing no cooperation, so an absent counterparty cannot strand a record

No value moves on-chain. Settlement is fiat, via a French approved e-invoicing platform. The chain carries proof, not money — a restaurant needs only fee-level ada

How CIP-0170 is used: it is a metadata standard, and Plutus scripts cannot read metadata. Each transition emits a label-170 ATTEST record whose digest commits to the on-chain UTxO, verified off-chain per the CIP. What is enforced on-chain is the signature — the validator requires the key the KERI credential chain binds to the legal entity

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

Target market: independent and small-group commercial food service in France — restaurants, hotels, caterers — buying produce, meat, drinks and dry goods from 4 to 12 regional suppliers, with no ERP, no EDI and no reconciliation beyond a signature at the dock. INSEE counts \~179,000 restaurant businesses; commercial food service turns over €75.4bn, of which €46.9bn is table service, our segment (Gira, 2026).

Evidence of demand:

2 establishments onboarded, placing €400–500k of orders a year between them — roughly €225k each.

They estimate 1–3% of what they are invoiced is never delivered. On their own volume that is €4,000–15,000 a year written off silently, or €2,000–7,500 per establishment.

2 suppliers in active commercial discussion

We are explicit that 1–3% is our users' estimate, not a measurement. Nobody in this market measures it, because the delivery note is the only record and it is signed before it can be checked. Producing the first measured discrepancy rate is itself a deliverable of this pilot.

That gap is the demand signal. Both establishments committed on the ordering product alone, before any on-chain layer existed, and both named short deliveries unprompted as the reason they wanted a single interface in the first place.

### Applicant name

Samuel Schneider

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Suppliers pay €249/month plus €0.40 per processed order. A distributor serving 100 establishments pays around €8,600 a year — €86 per establishment served, against disputes it currently absorbs with no way to disprove them.

Restaurants use it free. They are the side we need most, and each one added is another independent participant.

We take no fee on dispute outcomes and hold no arbitration key: arbitration is 2-of-3 between buyer, seller and an independent third party. An intermediary paid a percentage of a verdict it could influence is one no supplier would accept.

Who pays for the chain: users do. Each party holds its own wallet and pays its own fees — about €0.20 on a €400 delivery, against losses ten to thirty times higher. We rejected sponsoring those fees: if we paid them, usage would not be usage.

After the grant the incentive is the loss, not the funding. And verifiable delivery proof makes receivables financeable: factors pay for proof quality, never for an outcome.

### On-chain identity (CIP-0170) - expected transaction count

1200

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant the attestation layer does not get built. Our procurement product funds itself commercially, but no single customer pays to build a record whose value is that it belongs to nobody — that is exactly the coordination gap a grant closes.

What it accelerates: mainnet in three months rather than as a side project competing with revenue work.

Spend, roughly:

- 40% off-chain layer and self-custody wallet provisioning: transaction construction, salted commitments, indexing
- 30% external security review before mainnet — a locked validator is unrecoverable, and we will not deploy unreviewed
- 20% reception app with GS1-128 crate scanning, the last-metre capture the chain cannot provide
- 10% deployment, monitoring, dashboards

All future work. Nothing retroactive.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Aiken validator live on Cardano mainnet, newly deployed for this grant, nothing pre-existing. It enforces sequence, not value: the manifest is sealed before the buyer declares, the buyer cannot attest more than was sealed, and no absent party can strand a record. Footprint published: script hash, policy ID, addresses, message tag, team stake keys.

CIP-0170 attestation layer. Each transition emits a label-170 ATTEST record whose digest commits to the on-chain UTxO, verified off-chain per the CIP. On-chain, identity is bound by signature: the validator requires the key the KERI chain binds to the entity. Self-certifying AIDs via KERIA/signify-ts; vLEI out of scope.

Off-chain TypeScript layer: transaction construction, salted blake2b-256 commitments, chain indexing. Open source, tagged commit.

Reception app with GS1-128 scanning, live at both establishments, attestation under 30s.

Three independent end-to-end mainnet runs by real users, one on the discrepancy path

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### On-chain identity (CIP-0170) - fee target (ADA)

360

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

n food service the delivery note is signed before it can be checked. Deliveries land at 6am during prep; the chef signs for fourteen crates without counting them. From then the note is proof of conformity, and disproving it falls on the restaurant — impossible, the goods are in the cold room. Short-delivered items get invoiced and paid. Not fraud: no counter-record exists.

We build a procurement app where a restaurant orders across all its suppliers from one interface, and every delivery step becomes a signed on-chain attestation neither side can rewrite.

Restaurants stop paying for goods they never received; attesting takes seconds, so a chef will actually do it at 6am. Suppliers get a sealed manifest proving what left the warehouse, and our invoicing runs on the undisputed portion at once — a €2 gap no longer freezes an €800 invoice.

Why on-chain, honestly: we are an aggregation platform. We sit between buyer and seller, take a margin, and propose to hold the record of every supplier's shortfalls. No supplier would accept that in our private database. The chain solves our own neutrality problem: it makes the record adoptable by suppliers with no reason to trust us, and usable by a factor.

We do not claim the chain knows what was in the crate, or that it moves money: physical checks stay human, settlement stays fiat. It guarantees declarations are irreversible and symmetric: the supplier seals its manifest at departure, the buyer attests independently after.

### Supporting links (repo, site, demo)

- https://lagragnaguette.com
- https://www.linkedin.com/in/armand-collier/
- https://www.linkedin.com/in/13121996/
- https://github.com/armandParser
- https://www.pappers.fr/dirigeant/dani_schneider_1983-04

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

he Aiken validator compiles, and both the order-opening and acceptance flows execute end to end against the compiled validator in a local chain emulator. Not yet on a public testnet.

Four states — Created, Accepted, Shipped, Disputed — and eight transitions, with a one-shot state-token policy for order uniqueness, M-of-N arbitration bounded both ways, and permissionless exits so no order is stranded by an absent party. Attestation only: no value moves, totals in euro cents. Aiken v1.1.19, Plutus V3.

66 passing tests, including simulations of every transition and the negative cases that matter: a supplier attesting reception for the buyer, a buyer inflating the amount, the deposit diverted at closing, a panel exceeding the manifest.
