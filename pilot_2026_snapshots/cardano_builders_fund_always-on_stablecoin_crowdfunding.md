# Cardano Builders Fund: Always-On Stablecoin Crowdfunding

> An always-on Cardano crowdfunding platform where anyone can fund builders, creators, and communities with ADA or stablecoins, without waiting for the next grant round.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 46
- **Proposer:** `stake1u84rzt9g539r3jd0m7tgd5ankpsldks4qmj23pykcglsp5ce7uar4`
- **Funding requested:** ₳130,000
- **Last finalized:** 2026-08-23T06:16:55.795000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Mallen Chiyari is my Catalyst and legal applicant name. I work internationally as Chris Ciari, and 9rissc is my long-standing public handle. I am the founder and lead developer of Cardano Builders Fund, responsible for product architecture, wallet and transaction integration, backend development, chain observation, testing and mainnet delivery.

I also built TSUNAGI, a from-scratch Cardano node project with public Preview evidence, and I maintain public Cardano data tooling on GitHub. Cardano Builders Fund itself has completed a real end-to-end Preprod contribution flow.

Public references include TSUNAGI: <https://www.tsunagi.tech/> , Cardano data tooling: <https://github.com/cryptoleo79/cardano-data-layer> , LinkedIn / 9rissc: <https://jp.linkedin.com/in/9rissc> , and my previous Catalyst record under Mallen Chiyari / 9rissc: <https://projectcatalyst.io/funds/14/cardano-open-ecosystem/empowering-real-world-ada-adoption-with-ashiya-pool>

I work in both Japanese and English. No unnamed developer or technical subcontractor is being relied on for M1.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

**N/A**

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Every counted transaction comes from a real supporter funding a campaign from their own Cardano wallet. We do not sponsor fees, reward transactions or count team wallets.

Our 520 ADA target comes from the flow we already measured. The real Preprod contribution used for our TRL 5 proof paid 0.172189 ADA in network fees. At the same fee level, 3,000 contributions would generate about 516.6 ADA, so 520 ADA is based on our own evidence rather than the program floor.

We will start with 3 campaigns, 100 external wallets and 300 contributions in the first two weeks. The working ramp is 5 to 7 campaigns and 800 cumulative contributions, then 8 to 10 campaigns and 1,400, then 10 to 15 campaigns and 2,100. Additional campaigns and repeat supporters take the total toward 3,000.

### How will you reach and onboard real users - and what evidence backs your channels?

We already have a live builder application channel with two real applications received. For launch we also have YAMORI Wallet and TSUNAGI Node as campaign candidates, plus an external candidate from the team behind the Fund14 proposal “Creating Cardano Business cases through Real Coffee World,” who plans to bring a revised coffee-related campaign to Cardano Builders Fund.

We will combine this pipeline with direct outreach to Cardano builders and Cardano Radio.

Our first two-week target is 3 campaigns, 100 external wallets and 300 contributions. We then plan to grow to 5 to 7 campaigns and 800 cumulative contributions, 8 to 10 campaigns and 1,400, then 10 to 15 campaigns and 2,100. Additional campaigns and repeat supporters take the total toward 3,000.

The first 100 external wallets will come from supporters around these campaigns, Cardano Radio and direct Cardano outreach. Team wallets, fee sponsorship and artificial activity will not count.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, people can use Catalyst or another grant program, a platform such as CAMPFIRE or Kickstarter, a crypto platform such as Giveth, or simply share a wallet address.

Grant programs are valuable but run in rounds. Traditional crowdfunding platforms are familiar, but they are not built around Cardano wallets or public on-chain campaign records. A wallet address is simple, but offers little help with attribution, milestones or reporting.

Cardano Builders Fund is built specifically for Cardano, combining ADA and stablecoin funding, Japanese and English onboarding, verified campaign owners, public transaction evidence and milestone updates. We start with reviewed campaigns so supporters know who is raising funds and why.

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

Our first users are Cardano builders, creators, community organizers, events and public-good teams that need to raise smaller amounts without waiting for another grant round. We will start in Japan, where we can support users directly in Japanese, then expand to the wider English-speaking Cardano community.

The wider market is already proven. Project Catalyst reports more than 11,000 proposals and 84,000 members. In Japan, CAMPFIRE reports about ¥116 billion raised across roughly 120,000 projects and 14 million cumulative supporters. Crypto-native crowdfunding and giving platforms such as Giveth also show that people will fund projects directly with digital assets.

Those figures prove the market, not our own product-market fit. Cardano Builders Fund already has a live builder application channel with two real applications received, a working public product, wallet and campaign flows, and a real Cardano Preprod contribution proof. The Pilot will test our own demand through reviewed campaigns, external wallets and measurable stablecoin contributions.

### Applicant name

Mallen Chiyari

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The Pilot helps us complete the stablecoin integration and mainnet launch. After launch, Cardano Builders Fund earns a success fee from the campaign owner only when a campaign reaches its goal.

Our current standard fee model is 8 percent: 5 percent for platform operations, 2 percent for the Builder Reserve and 1 percent for infrastructure and settlement. Final legal, tax and accounting terms will be confirmed before real funding opens.

Campaign owners pay for campaign review, wallet-based contributions, public transaction records, milestone tracking and launch support. The platform runs all year, so projects can raise before Catalyst, between rounds, after a grant or without entering governance at all. We do not rely on a new token, ads, selling user data or artificial transaction activity.

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
- https://preprod.cardanoscan.io/transaction/af89cde4c0ab8da3f540d72ed11512bd6cdbcde2de49a49fe6cf8afaa2380cad
- https://www.tsunagi.tech/
- https://github.com/cryptoleo79/cardano-data-layer
- https://jp.linkedin.com/in/9rissc

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

520

### Current funded commitments

Project Catalyst Fund14 · “Empowering Real-World ADA Adoption with Ashiya Pool” · Mallen Chiyari, project lead · currently in progress, with 2 of 5 milestones completed and Milestone 3 in progress. The project covers community outreach, events, media and ADA onboarding in Japan. It is separate from Cardano Builders Fund and does not fund the crowdfunding product or stablecoin integration.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The stablecoin integration is at TRL 2. The product flow, asset boundaries, wallet model and safety requirements are defined, and the existing product already includes stablecoin settlement and swap-readiness architecture. No live stablecoin transfer, swap or settlement is enabled today. The Pilot will fund the work from this design stage through testnet implementation and a controlled Cardano mainnet launch.
