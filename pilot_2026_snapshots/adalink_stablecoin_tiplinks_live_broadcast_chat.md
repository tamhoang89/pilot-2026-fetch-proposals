# AdaLink: Stablecoin TipLinks & Live Broadcast Chat

> Powering direct creator support and live audience interaction with Cardano stablecoins.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 13
- **Proposer:** `stake1u8qm4n5yeuqzac5rdnafd359y5g7sh4w9hzhlvamsd9kheq9h2n9j`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-23T19:05:19.337000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

The [AdaLink team](https://drive.google.com/file/d/1cd7OL4CqthYIA18y-N14EpSiSbBeqbuH/view?usp=sharing) brings together three strengths directly relevant to this project: an existing Cardano mainnet product, deep creator and media industry experience, and Cardano-native engineering.

[**Natalia Rosa**](https://www.linkedin.com/in/natalia-rosa-film/), **CEO & Co-Founder**\
Natalia leads product strategy, business development, creator programs, campaign development, and growth. She brings more than 15 years of experience across advertising, film, broadcast, and multimedia production, with firsthand knowledge of production workflows, commercial relationships, and creator-focused industries.

[**Gisela Rosa**](https://x.com/GR_JSAT), **COO & Co-Founder**\
Gisela is a professional cellist with years of experience in the music and entertainment industry, performing alongside Luis Miguel, Luis Enrique, Willie Colón, RaiNao, and others. Her career gives her firsthand insight into artist relationships, live production, and sustainable creative careers.

[**Mahmoud Nimer**](https://github.com/Fourzin), **CTO & Lead Developer**\
Mahmoud is a Mechanical Engineer with an M.S. in Control Systems and Robotics. A Plutus Pioneer, he has built in the Cardano ecosystem for more than four years. Mahmoud led development of [AdaLink’s early MVPs](https://milestones.projectcatalyst.io/projects/1100015/milestones/4), funded by Catalyst.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Transactions are generated when creators share TipLinks and audiences voluntarily send stablecoin tips. TipLinks also give users a simple way to send and receive supported stablecoins.

Recurring uses include direct support for creators, communities or causes, and live interaction through messages attached to tips and displayed during broadcasts. TipLinks remain reusable across profiles, livestreams, videos, websites and Discord.

Our target is 2,500 qualifying transactions / 500 ADA in qualifying fees during the measurement window. This is external-user activity, not a quota tied to a fixed creator cohort. Users will not be paid or reimbursed to transact.

During the 3-month pre-launch period, we will help users integrate the existing TipLink experience into their workflows. Reachable channels include 3,740 X followers, 530 Discord members and 300 registered AdaLink creators. Post-launch targets are:

- Week 1: 300
- Week 2: 400
- Week 3: 500
- Week 4: 600
- Week 5: 700

The target is ambitious, but combines a live mainnet product with three months of funded GTM activation, creator education and workflow preparation.

### How will you reach and onboard real users - and what evidence backs your channels?

AdaLink will use the 3-month build and launch period to prepare and onboard users through our [channels](https://linktr.ee/adalink_io). Creators are core users; any creator can participate.

Funded activation includes X Spaces, creator meetings, onboarding content and outreach across X and Discord.

Our first confirmed collaborator is [Viviana Oppenheimer](https://www.instagram.com/vivioppenheimerlugo/), founder of [Dejando Huellas](https://www.instagram.com/dejando_huellas_pr/), with 15K+ Instagram followers. Her organization regularly raises funds for animal rescue, including $20K+ at a [July 2026 event](https://www.instagram.com/dejando_huellas_pr/reel/DbEM8GKI0Eg/). We will produce ongoing fundraising content, demos and interviews showing TipLinks and Live Broadcast Chat, while helping creators integrate TipLinks into livestreams and podcasts.

Creator compensation is for content/production only, never tied to tips, transaction volume or on-chain activity.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives fall into three categories: platform-native tools like YouTube Super Chat and Twitch Bits, creator-support platforms like Ko-fi, and direct wallet transfers. Platform tools offer strong interaction but lock creators into their ecosystems. Ko-fi is portable but remains an intermediary. Wallet transfers are direct but lack the creator experience.

AdaLink combines these strengths in a Web3-native model. Creators keep their audiences, use one TipLink across the platforms they already use, and access promotional campaign opportunities.

We are not replacing content platforms. **AdaLink is building a Web3-native economic layer creators can use across them.**

### Please provide details about the Technology Readiness Level selected for your existing product

AdaLink is a live Cardano mainnet product, launched on February 4, 2026. It currently includes Token Campaigns, Creator Profiles and ADA TipLinks, supported by CIP-30 wallet connection and signing, Cardano transaction construction, metadata, transaction confirmation, attribution and performance tracking.

As of August 2026, AdaLink has:

- **338 registered users**
- **278 on-chain transactions**
- **21,824 ADA distributed**
- **7 campaigns**

Most relevant to this proposal, **TipLinks already support non-custodial, wallet-to-wallet tipping in ADA**.

These existing components are not being rebuilt with this grant. The funded work extends this live infrastructure with stablecoin tipping and Live Broadcast Chat functionality.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The integration uses a **non-custodial, wallet-to-wallet architecture** built on AdaLink's existing Cardano transaction infrastructure.

A supporter opens a creator's TipLink, connects through a CIP-30 wallet, selects an accepted asset such as USDCx, enters an amount and optional message, reviews the transaction and signs it directly from their wallet. The stablecoins settle directly to the creator's wallet. **AdaLink never takes custody of user funds.**

After confirmation, AdaLink verifies and indexes the transaction and mirrors the application data needed for tip history, notifications, moderation and Live Broadcast Chat. The blockchain remains the source of truth for the payment, while AdaLink controls how associated messages are moderated and displayed.

This architecture is appropriate for the Stablecoins integration because it:

- produces directly verifiable on-chain stablecoin transfers
- identifies the relevant asset through its policy ID and transaction data
- avoids custody, pooled funds and unnecessary smart-contract risk
- preserves user-controlled wallet signing
- extends transaction infrastructure already operating on Cardano mainnet

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

***Our core users are creators and their audiences.*** Creators need a simple way to receive support, and audiences need an easy way to send it. The market extends far beyond Cardano: [LunarCrush](https://lunarcrush.com/en/creators?category=cryptocurrencies) tracks 262,000+ unique creators posting about crypto daily. In its current top 100 crypto creator ranking, non-exchange/non-blockchain accounts collectively show 200M+ followers, with a median above 2M.\
\
Web3 businesses also benefit. A larger creator network gives them more creators for future campaigns.\
\
AdaLink launched on Cardano mainnet on February 4, 2026, during a low-activity period when Cardano averaged roughly 280,000 transactions per month, with nearly half concentrated in one platform. Despite these conditions, by August 2026 AdaLink had:

- 338 [registered users](https://www.adalink.io/creators)
- 278 on-chain transactions
- 21,824 ADA distributed
- 7 campaigns

 This proposal changes an important variable: for the first time, AdaLink will have a dedicated GTM operationalization and market activation budget to prepare users before release. Our current traction was achieved without a dedicated acquisition budget or the built-in distribution and incentive mechanisms available to token-based products.

Direct creator support and paid livestream interaction are established through YouTube Super Chat, Twitch Bits and other platforms. We aim to bring that behavior into a Web3-native, wallet-to-wallet experience.

### Applicant name

Blockverse Media, Inc.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

AdaLink primarily operates on a **B2B2C model**, connecting businesses with creators and affiliates who help them reach and convert users. Creators and affiliates participate for free, while businesses pay through campaign fees, sponsored placements, and Affiliate Program Listings. We also charge transaction processing fees and may introduce fees for premium stickers or longer Live Broadcast Chat messages.

Stablecoin-enabled TipLinks strengthen the creator side without charging creators directly. Campaigns let creators earn from businesses for measurable results, while TipLinks let them earn directly from their audiences. Creator Profiles and performance data help them build a Web3 identity.

This creates a reinforcing model: better creator tools attract and retain creators, stronger participation improves campaign distribution, and better outcomes create more value for businesses and more opportunities for creators.

The grant funds the build and initial activation of this product.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding enables AdaLink to prioritize this creator-economy expansion now and bring it to mainnet as an actively used stablecoin product.

Funding will support:

- Product Development, 40K ADA: Stablecoin TipLinks, USDCx, asset controls, messages, moderation, history, Live Broadcast Chat, testing and deployment.
- Project Management & Operations, 20K ADA: Coordination, QA, reporting and operations.
- GTM & Pre-Launch Activation, 20K ADA: Creator outreach, meetings, tutorials, X Spaces and onboarding.
- Post-Launch Activation & Optimization, 120K ADA: Creator onboarding, content, education, support and product improvements based on feedback to strengthen usability, retention and product-market fit.

Without funding, this expansion would progress more gradually.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, AdaLink will deploy **Stablecoin-enabled TipLinks and Live Broadcast Chat Tipping to Cardano mainnet**, with the onboarding and launch assets needed for activation.

**Month 1:** USDCx/accepted-asset architecture, creator settings, GTM preparation, onboarding materials and creator-content pre-production.

**Month 2:** Stablecoin tipping flow, supporter messages, history, moderation, Live Broadcast Chat integration, testing and creator demo production.

**Month 3:** Catalyst transaction identification, end-to-end QA, mainnet deployment, documentation, creator activation, tutorials and case-study content.

M1 deliverables include creator-controlled stablecoin TipLinks, wallet-to-wallet USDCx tipping, supporter messages, moderation/history, Live Broadcast Chat, Catalyst tagging, testing and release, plus an onboarding toolkit and confirmed activation with Viviana Oppenheimer / Dejando Huellas producing fundraising demos, interviews and reusable launch content.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

AdaLink is building **Stablecoin TipLinks and Live Broadcast Chat Tipping**, an expansion of our existing Creator Profiles and TipLinks product.

AdaLink is a live Cardano-native performance marketing platform connecting businesses, creators, and users through measurable campaigns.  Today, we support Token Campaigns, with SPO, user activation and content campaign models in development.

Our strategy intentionally prioritizes creators because we believe healthy creator economies produce more durable growth. Web3 incentives can generate short-term activation, but participation often declines when rewards disappear. Creators add something incentives alone cannot: education, context, trust, distribution, and ongoing relationships with users.

This extension gives creators an additional revenue path between campaigns. ***Today, our TipLinks support tipping in ADA. With this expansion, users will be able to configure their profiles to accept USDCx and other supported stablecoins,*** choose which assets they accept, receive funds directly to their Cardano wallets, attach messages to tips, and display approved messages during livestreams through a Live Broadcast Chat overlay.

**Creators** gain another way to earn. **Audiences** gain a direct way to support and interact with them. **AdaLink** gains a stronger creator ecosystem that can support more durable Web3 growth.

### Supporting links (repo, site, demo)

- https://www.adalink.io/

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

### Stablecoins - expected transaction count

2500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

500

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The complete **Stablecoin TipLinks + Live Broadcast Chat** experience has not yet been integrated and tested end-to-end.

It will reuse AdaLink's existing wallet connection, signing, transaction construction, metadata and confirmation infrastructure.

The newly funded work includes:

- USDCx and supported stablecoin tipping
- creator accepted-asset controls
- optional supporter messages, history and moderation
- Live Broadcast Chat for displaying approved messages
- integration-specific transaction identification
- end-to-end testing, QA and mainnet deployment

By Milestone 1, the target is **TRL 7**, with external users able to send real USDCx tips directly to creator wallets and approved messages appearing through the Live Broadcast Chat experience on mainnet.
