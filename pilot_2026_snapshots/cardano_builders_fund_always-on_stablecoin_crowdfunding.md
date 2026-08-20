# Cardano Builders Fund: Always-On Stablecoin Crowdfunding

> An always-on Cardano crowdfunding platform where anyone can fund builders, creators, and communities with ADA or stablecoins, without waiting for the next grant round.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 25
- **Proposer:** `stake1u84rzt9g539r3jd0m7tgd5ankpsldks4qmj23pykcglsp5ce7uar4`
- **Funding requested:** ₳130,000
- **Last finalized:** 2026-08-20T01:15:38.959000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

> I am already building Cardano Builders Fund, so this Pilot does not start from a blank page. I have worked across Cardano applications, wallets, infrastructure and chain-level engineering. I also built TSUNAGI, an independent Cardano follower focused on ChainSync, BlockFetch, rollbacks and reliable chain observation. That experience is directly relevant to confirming and reconciling crowdfunding transactions. I work in both Japanese and English, which matters for our first market. I have also deliberately kept the financial side of Cardano Builders Fund disabled until it could be tested properly. The Preprod contribution completed before submission is a good example of how I intend to build this: isolate it, test it, verify it independently, then move forward.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**N/A**

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Cardano Builders Fund generates usage when real supporters fund real campaigns. Contributors choose a stablecoin amount, review the transaction and sign it in their own Cardano wallet. They pay the normal network fee because they want to support the campaign, not because we reward them for creating transactions.

We are targeting 3,000 stablecoin contributions across the Pilot measurement period. That is ambitious for a first launch, so we will not depend on one campaign to carry it. We will start with 3 to 5 reviewed campaigns, bring more campaigns on as the flow proves itself, and work through each campaign's own supporter network. Our Preprod contribution paid 0.172189 ADA in network fees, so the 320 ADA target leaves room for normal mainnet fee variation rather than assuming every transaction will cost exactly the same.

Team wallets, recycled funds, giveaways, fee sponsorship and artificial activity will not count. Usage continues as new campaigns launch, supporters return, and successful builders come back to fund later work.

### How will you reach and onboard real users - and what evidence backs your channels?

We already have a live builder application channel, with applications stored privately and reviewed manually. We will recruit the first campaigns through that pipeline, direct outreach to Cardano builders and Cardano Radio. For the first two weeks after mainnet launch, we will focus on the first 3 campaigns, personally onboard each owner, verify wallet control and support their launches, targeting the first 100 external wallets and 300 genuine stablecoin contributions. We will then add campaigns and expand through each campaign's own community toward our 3,000-transaction Pilot target. No team wallets, sponsored fees or artificial activity will count.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, people can use Catalyst or another grant program, a platform such as CAMPFIRE or Kickstarter, a crypto platform such as Giveth, or simply share a wallet address.

Each option has value, but none is built for our exact use case. Grant programs run in rounds and require selection. Traditional platforms do not connect campaign progress to Cardano transactions. A wallet address is easy to share, but it offers little help with attribution, milestones or reporting.

Cardano Builders Fund combines Cardano wallets, ADA and stablecoin funding, Japanese and English onboarding, verified campaign owners, public transaction evidence and milestone updates. We will begin with reviewed campaigns so supporters know who is raising funds and what the money is for.

### Please provide details about the Technology Readiness Level selected for your existing product

Cardano Builders Fund is already deployed with live builder intake, database-backed campaign and operator workflows, and CIP-30 wallet support. Before submission we completed the full contribution flow on Cardano Preprod. A VESPR wallet built, reviewed, signed and submitted a real 2 tADA contribution. The product then observed it independently, checked the network, destination, amount and on-chain campaign reference, waited for confirmation and attributed it to the test campaign. Transaction: af89cde4c0ab8da3f540d72ed11512bd6cdbcde2de49a49fe6cf8afaa2380cad, block 5076032. Production funding remains disabled.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The architecture is non-custodial from the contributor side. A campaign defines the supported asset, target and verified destination. Cardano Builders Fund creates a bounded contribution intent containing the campaign, network, verified asset identity, amount, destination and unique reference. The contributor reviews and signs the transaction in their own CIP-30 wallet, so the platform never handles seed phrases or private keys.

After submission, the platform independently observes Cardano and verifies the network, exact asset, destination, amount, reference and confirmation state before crediting the campaign. Rollbacks or invalid transactions return to a non-final state rather than remaining credited.

We have already validated this model with a real Preprod tADA contribution. The stablecoin integration extends the same flow to a verified Cardano stablecoin rather than creating a wrapped or synthetic asset.

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

Our first users are Cardano builders, creators, community organizers, events and public good teams that need to raise smaller amounts without waiting for another grant round. We will start in Japan, where we can support users directly in Japanese, then expand to the wider English-speaking Cardano community.

There is clear demand for this type of funding. Project Catalyst reports 11,233 proposals, 2,221 funded proposals and more than 84,900 members. In Japan, CAMPFIRE reports about ¥116 billion raised across around 120,000 projects and 14 million cumulative supporters by March 2026. Crypto-native giving is also established: Giveth lists about 8,300 projects, 29,280 givers and more than $7 million donated.

Those figures prove the market, not our product-market fit. We will not pretend otherwise. What we have today is a public Cardano Builders Fund prototype, working builder application intake, campaign and wallet previews, and a documented stablecoin direction. The Pilot will prove our own fit with 3 to 5 curated campaigns and real external contributors.

### Applicant name

Mallen Chiyari

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The Pilot helps us complete the integration and launch. After that, the platform will earn a success fee paid by the campaign owner only when a campaign reaches its goal. Our current standard fee model is 8 percent. Five percent supports operations, 2 percent goes to the Builder Reserve, and 1 percent covers infrastructure and settlement. Final terms will be confirmed before real funding opens. Campaign owners pay for review, a clear campaign page, wallet based contributions, public transaction records, milestone updates, and launch support. Projects can raise funds throughout the year, so usage does not depend on another grant round. We will not rely on a new token, advertising, selling user data, or artificial transactions.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The product foundation already exists. This funding takes Cardano Builders Fund from a testnet-validated contribution flow to a stablecoin-enabled mainnet launch within three months. It covers stablecoin and wallet integration, chain observation and reconciliation, security, testing, production hardening, legal and operational readiness, onboarding, monitoring and launch support.

Budget: 45,000 ADA for stablecoin and wallet integration, 25,000 for chain observation, reconciliation and security, 20,000 for testing and production hardening, 15,000 for legal and operational readiness, 15,000 for Japanese and English onboarding and launch support, and 10,000 for monitoring, documentation and contingency.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months we will launch Cardano Builders Fund on mainnet with direct support for one verified Cardano stablecoin. The release will include contributor-controlled CIP-30 wallet signing, stablecoin campaign targets, bounded contribution intents, exact asset verification, transaction submission, chain observation, confirmation tracking, campaign attribution, rollback handling and public transaction evidence.

We will launch with 3 to 5 reviewed campaigns, a limited wallet matrix, Japanese and English onboarding, server-side safety gates, monitoring, transaction labeling, release notes and test evidence covering wrong network, wrong asset, duplicate transactions, expired intents, provider failure and rollback.

M1 is complete when a real external user funds a live campaign with the selected stablecoin on Cardano mainnet, the product verifies and attributes it, and the flow repeats successfully.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano Builders Fund is an always-on crowdfunding platform for builders, creators, teams, events, and community projects on Cardano.

Grant programs are valuable, but funding is episodic. Projects may need to wait for a grant round, compete in governance, or rely on informal wallet transfers and centralized platforms. Smaller or early-stage projects can be left without continuous funding. Informal crypto fundraising also creates practical problems: contributions are hard to attribute, totals may not match on-chain records, supporters can send the wrong asset or amount, and ADA volatility makes budgeting unpredictable.

We are building a Japanese-first, global product where approved campaigns can raise ADA and stablecoins directly from supporters. Contributors review and sign transactions in their own Cardano wallets without giving the platform seed phrases or private keys. The platform verifies the network, asset, destination, quantity, campaign reference, confirmation status, and duplicate risk before updating the campaign total.

Campaigns do not need to win a governance vote or wait for the next funding cycle. After identity, wallet-control, and safety checks, supporters decide what succeeds through direct contributions.

The Pilot will take today's working product to a controlled mainnet launch with one verified stablecoin. Supporters will contribute from their own wallets, and payments will only count after they are confirmed and matched to the right campaign.

### Supporting links (repo, site, demo)

- https://cardano.builders/
- https://cardano.builders/infrastructure-readiness
- https://cardano.builders/contribution-preview
- https://preprod.cardanoscan.io/transaction/af89cde4c0ab8da3f540d72ed11512bd6cdbcde2de49a49fe6cf8afaa2380cad
- https://github.com/cryptoleo79

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

3000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

320

### Current funded commitments

Project Catalyst Fund14 · “Empowering Real-World ADA Adoption with Ashiya Pool” · Mallen Chiyari, project lead · currently in progress, with 2 of 5 milestones completed and Milestone 3 in progress. The project covers community outreach, events, media and ADA onboarding in Japan. It is separate from Cardano Builders Fund and does not fund the crowdfunding product or stablecoin integration.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration is at TRL 2. The product flow, asset boundaries, wallet model and safety requirements are defined, and the existing product already includes stablecoin settlement and swap-readiness architecture. No live stablecoin transfer, swap or settlement is enabled today. The Pilot will fund the work from this design stage through testnet implementation and a controlled Cardano mainnet launch.
