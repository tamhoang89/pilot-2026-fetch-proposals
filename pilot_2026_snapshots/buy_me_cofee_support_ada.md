# Buy me Cofee | Support Ada

> Support Ada is a non-custodial creator funding platform on Cardano. A supporter sends value straight to a creator's wallet in one transaction, and that same transaction mints an on-chain receipt.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 17
- **Proposer:** `stake1u9rgdnznvl7grnrpg4zd0f20mgds0pfg205ej206esw03vq8g8msa`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-21T18:23:10.347000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Jethro Adebisi: UX Designer, Project Lead.\
<https://github.com/adebisijethro>\
Responsible for project Management and flow and overall Frontend implementation, and User experience. \
\
Asaolu Emmanuel: Co-Lead and Blockchain Developer.\
<https://github.com/Temasar1>\
Responsible for Aiken protocol work, transaction building and implementation.\
\
The rest of the team at \
<https://blockprint.team/contributors> 

We have worked with Gimbalabs on several occasion, Asaolu has also worked with Meshjs and Uxtos. 

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge to return 10% of net platform fee revenue to the Cardano treasury, beginning in the first full quarter in which cumulative platform fee revenue exceeds the grant amount of 60,000 ADA, and continuing for eight consecutive quarters. Reported quarterly against the same on-chain identifiers declared for adoption measurement, so the figure is independently checkable.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

one transaction, settling straight to the creator's wallet and minting a receipt. Creators transact too, because a membership is a prepaid balance they draw down one period at a time, so each period produces a claim transaction the creator signs.

Cadence is what holds the target across six epochs instead of spiking at launch. A tip happens once; a membership keeps producing claims while it runs. Period length is a datum field in the existing validator, so weekly and monthly tiers are configuration, not new work, and weekly pays the creator sooner.

Build-up to 1,400 stablecoin transactions from \~90 live creators:

- 1,000 one-off supports, about 11 per creator
- 175 memberships started
- 225 claims, allowing for start dates spread across the window

Roughly 47 a day, from about 590 distinct external wallets.

CIP-0170: 300 attestations. Creators bind more than one handle (repo, social, site): \~90 creators at 3 bindings, plus re-attestation when one changes.

Both targets sit above the floors, 2.5x and 1.6x, without assuming viral growth. Nothing is funded by us; fees from our own wallets are excluded under the Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

Channels, in the order we will use them:

1. Direct creator recruitment in the Cardano developer and SPO community, where the first cohort already holds wallets.

2. Popular cardano creators on X like: ayomishuga

3. Partnership with the DEX used for stablecoin routing, which is a distribution channel as well as a technical dependency. 

4. Demo Day and Catalyst channels themselves.

First two weeks after going live: onboard the named creator cohort, publish each page, and have each creator announce to their own audience. The audience already exists; we are not building one.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/XdRFdhZ8sLU

### Who else solves this today - competitors/alternatives, and why does your approach win?

Web2 incumbents: Patreon, Ko-fi, Buy Me a Coffee. They own the category and work for creators with bank access. Their weaknesses are structural, not fixable by a better interface: a cut the creator cannot audit, custody of funds in transit, deplatforming risk, and payouts that are unreliable or unavailable across much of the world.

The default alternative on Cardano is sending ADA to an address. Free and non-custodial, but it leaves no receipt, no membership and no proof of the split.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 5, validated in a relevant environment.

Evidence:

- Live product: <https://supportada.vercel.app>
- Repository: <https://github.com/BlockPrintio/Buy-Me-a-Coffee>
- Two Plutus V3 validators compiled with Aiken v1.1.23, blueprint checked in.
- 47 passing contract tests, mostly adversarial.
- End-to-end support transaction built, signed and submitted on public testnet via CIP-30.

The payment layer is complete and exercised: wallet connection, balance and network reads, fee computation matching the validator's own rule, receipt minting, and CIP-20 message metadata. It is not TRL 6+ because it has not run on mainnet with real users, which is exactly what this grant delivers.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Two Aiken validators, Plutus V3, compiled and tested.

1. Receipt minting policy. Parameterised at compile time by platform payment credential, fee rate in basis points, and the minimum fee worth paying as its own output. It mints exactly one receipt and refuses unless the creator receives at least the declared amount and the platform receives exactly the fee due. Because parameters apply at build time, the policy ID is itself a commitment to one set of terms.

2. Membership script. A prepaid balance drawn down one period at a time. The creator cannot claim early (validity-range lower bound), take two periods at once, keep the remainder out of the script, or alter the terms in the continuing output. The supporter cannot cancel out from under an earned period: reclaiming the balance needs an upper bound proving the transaction runs before the next claim date.

Funds never sit at a script address in the support flow; ADA moves supporter to creator directly, which is what makes it non-custodial.

Fit for stablecoins: the split is already enforced by a value check inside the policy, so extending from lovelace to a native asset changes a predicate, not the architecture. The fee-waiver rule lives in one function shared by validator and client.

Fit for CIP-0170: the receipt is already an attestation-shaped artefact bound to a creator credential.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Primary market: creators who already hold a Cardano wallet and publish to a global audience. Open-source developers and tool maintainers, technical educators, digital artists, and stake pool operators who publish transparency reports and want delegators to fund that work directly. Cardano has roughly 3,000 active stake pools and over 70% of circulating supply staked, so this cohort is large enough to launch into and reachable without paid acquisition.

Category size, as evidence the demand exists rather than needs creating: Patreon alone has paid creators over $10bn since 2013, more than $2bn a year, across roughly 300,000 creators and 25m paid memberships (Axios, 5 Aug 2025).

Why those creators would move: Patreon's standard plan charges a 10% platform fee plus roughly 2.9% + $0.30 processing, an effective 12-15%, with about 2.5% more on foreign-currency pledges (Patreon Creator fees FAQ). We charge 2.5%, waived entirely below \~40 ADA, and never take custody.

Payout access is also more fragile than it looks: PayPal restored inbound payments to Nigeria only in January 2026, through a local partner, after 22 years closed. Chain settlement removes that dependency entirely.

### Applicant name

Jethro Adebisi

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue: 2.5% of support, waived entirely below roughly 40 ADA because a percentage cut of a small tip falls under Cardano's min-UTxO deposit and cannot exist as an output at all. So the model earns nothing on coffee-sized tips by design and earns on larger support and on memberships.

Why usage persists after the measurement window: memberships, not tips. A one-off tip is a single transaction. A membership is a prepaid balance the creator draws down one period at a time, so it produces a claim transaction every period for as long as it runs. Usage therefore compounds with the number of active memberships rather than depending on repeated marketing pushes.

Honest limitation: at low volume 2.5% with a sub-40 ADA waiver is not yet a business. The pilot funds reaching the volume where it becomes one.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The payment layer exists because it could be built without external dependencies. The two integrations cannot. Stablecoin settlement means reworking the validator's value predicate and re-deriving min-UTxO behaviour for token-carrying outputs, then an independent security review before it touches real money. CIP-0170 means implementing against a standard new to this ecosystem. Shipping either to mainnet unreviewed would be irresponsible.

Where the money goes:

- Protocol and product engineering, 55%: stablecoin settlement, CIP-0170, client work
- Independent security review, 15%: both validators, before mainnet
- Infrastructure, 5%: chain provider, hosting, monitoring
- Creator onboarding and launch, 20%
- Contingency, 5%

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of the three-month window, deployed on mainnet and usable by real users:

1. Stablecoin settlement live. The receipt policy enforces the creator/platform split on a native stablecoin amount, not lovelace alone, with the fee-waiver threshold re-derived for token-carrying outputs. Creators select payout denomination in the product.

2. CIP-0170 creator attestation live. A creator binds their wallet to the handles their audience knows; the supporter-facing verification state derives from that attestation, not a database flag.

3. Both validators independently security reviewed, report published.

4. Public dashboard live on the declared metadata footprint, showing transactions and counted fees per integration.

5. Release notes stating architecture, scope and limitations; repository tagged at the reviewed commit.

6. At least one end-to-end mainnet transaction per declared integration by a real external user, hashes mapped to flow steps.

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

The problem is that neither side can verify the split. Patreon, Ko-fi and Buy Me a Coffee take a cut the creator cannot audit, hold the funds, settle on their own schedule, and can remove a creator along with the audience relationship they built. Sending ADA directly avoids all of that, but it is a bare payment: no record of what it was for, no memberships, and no proof for either party afterwards.

Our minting policy refuses to issue a receipt unless the creator was paid the full declared amount and the platform took exactly its stated fee, not one lovelace more. Holding a receipt is therefore proof the split was honoured, because the ledger would have rejected the transaction otherwise. The rate is a compile-time parameter capped at 10% inside the validator, so a deployed policy ID commits to one set of terms permanently; changing the rate changes the policy ID and leaves old receipts verifiable under the terms they were minted with.

Who has this problem: independent creators publishing to a global audience who are underserved by card-based platforms. Open-source developers, educators, artists, and stake pool operators publishing transparency reports, particularly those in regions where card payouts are unreliable, delayed, or unavailable entirely.

### Supporting links (repo, site, demo)

- https://github.com/BlockPrintio/Buy-Me-a-Coffee
- https://supportada.vercel.app/
- https://blockprint.team/

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

The Repo is Public

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

400

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

400

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

What exists is the design and the extension point. The receipt policy enforces the split in lovelace only, through a paid_to(creator) &gt;= amount check. The stablecoin version replaces that with a check on a specific asset policy ID and quantity, and re-derives the fee-waiver threshold, because min-UTxO behaves differently once an output carries a token. That boundary is already isolated, so the change is localised rather than a rewrite.

For CIP-0170, the product carries a creator "verified" flag that is a boolean guaranteeing nothing. The integration replaces it with an attestation a supporter checks independently. The data model and UI surface exist; the attestation does not.
