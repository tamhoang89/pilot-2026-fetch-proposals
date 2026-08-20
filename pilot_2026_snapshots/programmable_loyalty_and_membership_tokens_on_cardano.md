# Programmable Loyalty and Membership Tokens on Cardano

> Loyalty points customers can verify, not just trust

## Proposal Metadata

- **Status:** finalized
- **Revision:** 6
- **Proposer:** `stake1uyjj7t7wxvvh2vxlvuqn2eujq9kml6j6j3kw64e05edchfgq9lsxq`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-20T05:30:06.921000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

We are suited for this because we have worked on the exact problem already: loyalty flows, customer balances, merchant rules, and Cardano transaction design.

Our previous loyalty work with Cardano/Hydra taught us an important lesson: putting points on-chain is not enough if the real rules still live in a backend. This proposal is a focused improvement on that experience. Instead of making a token and then managing loyalty logic off-chain, we use CIP-0113 so that expiry, transfer limits, redemption scope, and membership rules can be enforced during token movement.

Our team:

Project Leader: LE DINH TRI

<https://www.linkedin.com/in/tri-le-dinh-018a90b/>

Smart Contract Engineer: HO TRUNG DUNG

<https://github.com/hotrdung>

Front-end Developer: VO YEN NHI

<https://github.com/Yenhi501>

Backend Developer: CHAU TRINH

<https://github.com/Chautrinh97>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts, and who pays. Merchants sign and fund batched issuance from their own wallets. Customers sign and fund redemptions, transfers and tier claims from theirs. Both are external to us and we sponsor neither.

That split shapes the target. Batching means fewer, heavier transactions rather than one per purchase: roughly 700 external transactions at \~0.85 ADA average, since a batch mint carries many outputs and the standard's validation runs on every movement. 700 x 0.85 = 595.

Composition: \~120 merchant issuance batches across 2 programmes, \~380 redemptions, \~120 tier claims and transfers, plus migration of our Hydra programme.

First 14 days. Days 1-3: contracts live, footprint declared, first programme configured. Days 4-7: first issuance batches and redemptions - check the epoch-1 floor of 50 ADA. Days 8-12: second merchant onboarded. Days 13-14: publish a per-epoch table.

Per-epoch floors: 50 ADA epochs 1-3, 100 for 4-6. Daily cap planned at 120 ADA.

Wallet diversity is structural: 60 external wallets against a 16 minimum.

### How will you reach and onboard real users - and what evidence backs your channels?

We will onboard merchants first, because one merchant can bring many customers. This is more realistic than trying to acquire individual crypto users one by one.\
\
Our first channel is migration from our existing loyalty work and consumer app experience into a mainnet programmable-token pilot. Our second channel is direct outreach to merchants that already run points, vouchers, or membership tiers and want better auditability.\
\
For merchants, we will provide a hosted console and a simple API/SDK for checkout integration. For customers, the flow should feel familiar: receive points, view balance and expiry, redeem points, and hold or renew a membership tier.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

On Cardano, loyalty has been tried, but mostly as NFTs, plain native assets, or Hydra/Web2 migration. Examples include ADALoyal, Rare Rewards, hotel loyalty APIs, SPO/NFT reward programs, and AIRA/RealFi-style Hydra loyalty proposals. These show demand, but we have not found a Cardano loyalty product using CIP-0113 programmable tokens to enforce rules during token movement.\
That gap is our opening. Plain tokens can show a point exists, but cannot enforce expiry, non-transferable membership tiers, merchant-scoped redemption, or refund reversals after minting. Databases can enforce rules, but users must trust the operator.\
Our approach wins because the loyalty promise becomes on-chain logic: the merchant defines rules, and Cardano checks them whenever the asset moves, redeems, or burns.

### Please provide details about the Technology Readiness Level selected for your existing product

We place the existing product at TRL 5 because we have already delivered an off-chain loyalty/customer app for a real partner/customer, evidenced by the Takashimaya Online app link, and we have also built a Cardano loyalty experiment on Hydra.\
\
The off-chain app proves the real product workflows: customer enrollment, rewards, merchant-side operations, and user-facing experience. The Hydra experiment proves that the team has tested loyalty logic in a relevant Cardano environment, including wallet/transaction flows and the limits of plain token-based loyalty.\
\
This proposal is not starting from an idea. It upgrades proven loyalty workflows into a mainnet programmable-token architecture using CIP-0113.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The design uses Cardano's eUTxO model and the CIP-0113 programmable-token pattern.\
\
Each merchant program has a Program Registry UTxO. It stores the program ID, merchant keys, redemption addresses, earn/refund policy, expiry buckets, membership tiers, transferability settings, and version. Program updates are timelocked and multisig-gated, so a merchant cannot quietly change rules for customers overnight.\
\
Program tokens are held through programmable-token script custody, with ownership tracked by the customer's stake credential. Holder UTxOs include datum for program ID, owner, token type, amount, expiry bucket, and tier state. When points move, redeem, burn, or update, the transaction must pass the validator.\
\
The validator checks that non-transferable tiers stay with the same owner or are burned/renewed; points redeem only at approved merchant addresses; expired buckets cannot be spent after their validity interval; refund/reversal actions require merchant authorization; and pilot transactions include the declared measurement label.\
\
This fits loyalty because the important rules happen after minting. Plain native tokens are cheaper, but they cannot enforce these rules in circulation. CIP-0113 gives us the validation path loyalty needs while keeping Cardano-native assets, wallet control by stake credential, and explorer/indexer visibility.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Our first customers are merchants that already use loyalty, vouchers, memberships, or customer tiers: retail shops, ecommerce apps, restaurants, venues, subscription products, and online communities. They already know why loyalty matters. The problem is that their current systems are private, hard to audit, and usually locked inside one app.\
\
We have practical experience from earlier loyalty work on Cardano/Hydra and from a real consumer app context through Takashimaya Online. That gives us actual workflows to build from: wallet connection, earning points, redeeming points, expiry, refunds, and merchant reporting.\
\
The demand is simple: merchants want repeat customers and cleaner reporting; customers want points they can see and rules they can trust. This pilot does not ask users to become DeFi users first. It brings Cardano into a behavior people already understand: earn, save, redeem, return.

### Applicant name

Le Dinh Tri

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Merchants pay us, and merchants pay the chain. Customers pay neither.

Three revenue lines: a setup fee when a merchant deploys a programme, a monthly platform fee by programme size, and per-issuance fees beyond an allowance.

The gas question deserves a direct answer, because loyalty dies on friction. Nobody will pay a network fee to earn points on a coffee. So issuance is batched and merchant-signed: a merchant mints for many customers in one transaction, from its own wallet, as part of settlement it already runs. Per-customer cost falls to a fraction of a cent, inside the cost of running a programme - which the platform fee prices.

Redemption stays customer-signed. Redeeming is deliberate and infrequent, so a fee against a chosen reward is proportionate.

Why a merchant pays: loyalty in-house means building issuance, redemption, expiry accounting and reconciliation, then carrying a liability nobody can audit. On chain it is countable at any block. We reward nobody for transacting.

### Programmable tokens (CIP-0113) - expected transaction count

1060

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The grant lets us turn our loyalty experience into a mainnet CIP-0113 product instead of keeping the important rules in backend code. The hard part is not the idea of points; it is making expiry, redemption scope, tier transfer limits, refunds, and measurement work safely on mainnet.\
\
Budget:

- Validators and registry: ADA 30,000
- Off-chain transaction builder, indexer, APIs: ADA 22,000
- Merchant console and wallet-facing views: ADA 18,000
- Existing program migration and merchant onboarding: ADA 14,000
- Tests, security review, remediation: ADA 24,000
- Documentation, Demo Day, adoption reporting: ADA 12,000

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months we will launch a working mainnet pilot.\
\
On-chain: CIP-0113-compatible validators for point buckets, memberships, expiry, merchant-scoped redemption, refund/reversal, and burn; Program Registry validator; declared script hashes, policy IDs, addresses, token names, and metadata label.\
\
Off-chain: merchant console, checkout API/SDK, transaction builder, indexer, wallet-facing balance/expiry view, and merchant dashboard for outstanding liability and redemption history.\
\
Launch: at least one real merchant or migrated loyalty program live on Cardano mainnet, with customers completing earn and redeem flows. We will also demo a failed non-transferable tier transfer and a failed expired/restricted redemption.\
\
Evidence: product URL, tx hashes mapped to user steps, repo tag/commit, release notes, security note, test checklist, bug log, short walkthrough video, and Demo Day presentation.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

600

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Most loyalty points are just numbers inside a company database. Customers cannot check if the rules changed, whether points really expire on the stated date, or whether a balance can be adjusted later. Merchants also carry a messy liability: points are issued, redeemed, refunded, and expired across many systems, but auditing that history is hard.\
\
Putting points on-chain helps, but a normal token is not enough. Loyalty points need rules. Some points expire. Some vouchers can only be used at one merchant. A membership tier should often stay with the customer and not be sold. A refund may need to reverse points. Plain tokens prove that something was minted, but they do not enforce these behaviors after minting.\
\
We are building a Cardano loyalty and membership platform using CIP-0113 programmable tokens. A merchant can set a program's rules: earning rate, expiry period, redemption scope, refund logic, transferable reward points, and non-transferable membership tiers. Those rules are registered on-chain and checked whenever the tokens move, redeem, or burn.\
\
For customers, this means loyalty points become something they can verify. For merchants, it means better auditability and less manual reconciliation. For Cardano, it creates real consumer transactions from normal actions: purchases, rewards, redemptions, renewals, and membership activity.

### Supporting links (repo, site, demo)

- https://apps.apple.com/us/app/takashimaya-online/id1591899513

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

We will open-source the core Cardano parts: programmable-token validators, registry validator, redemption validator, deployment scripts, technical documentation, and test evidence. 

The hosted merchant console and some business operation code may remain proprietary because they handle merchant onboarding, customer support, and private operational workflows.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The CIP-0113 integration is at design stage. We have mapped the core pieces: program registry, point buckets, membership tiers, expiry checks, merchant-scoped redemption, refund/reversal policy, wallet-facing balance views, and mainnet measurement identifiers.\
\
We do not yet have our own production CIP-0113 implementation live, so TRL 2 is the honest status. The grant funds the climb to mainnet: validators, registry, off-chain transaction builder, indexer, merchant console, tests, security review, launch program migration, and repeatable transactions by real users within three months.
