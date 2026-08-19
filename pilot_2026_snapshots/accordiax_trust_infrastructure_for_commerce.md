# Accordiax: Trust Infrastructure for Commerce.

> Scale an existing agreement-and-escrow platform beyond its student MVP with Cardano-powered, non-custodial settlement, verified stablecoins, and verifiable identity.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 2
- **Proposer:** `stake1u9l3zn3f46hs2rfzgzer9khesfsfe0cfgren2nsqy0hys6c5pydtz`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-19T06:59:49.306000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Our core team combines Cardano engineering, product/adoption, project delivery, and existing Accordiax experience.**

**Abdulbasit Abdulrahman Adigun: Project Lead & Lead Software Architect/Developer:** leads system architecture, Cardano integration, engineering, and internal technical contributors. [GitHub](https://github.com/devbasrahtop) · [LinkedIn](https://www.linkedin.com/in/devbasrahtop/) · [Portfolio](https://devbasrahtop.com)

**Aanuoluwapo Ayomide Osemene: Growth & Adoption Lead:** owns the 500-user acquisition strategy, adoption channels, and transaction-growth plan. [LinkedIn](https://linkedin.com/in/ayomishuga) · [X](https://x.com/shugaayomicontruct)

**Kamarudeen Fad: Project Manager:** coordinates sprints, milestones, blockers, documentation, and delivery; he has already managed Accordiax development. [LinkedIn](https://www.linkedin.com/in/fad-kamarudeen) · [X](https://x.com/kamarudeen22205)

**Yuguda Muhammad: Cardano Software Developer/Integration Engineer, contributes** to Aiken/Plutus smart contract development, transaction engineering, testing, and evidence. He has contributed to Nextrium’s Zivana Protocol Validation project. [LinkedIn](https://linkedin.com/in/yuguda) · [GitHub](https://github.com/Yuguda999)

**Nextrium’s wider internal technology and community teams provide additional execution capacity as required.**

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A — Accordiax is an early-stage commercial product entering its first Cardano integration, and our sustainable revenue, operating costs, and post-pilot economics are still being validated. We do not want to make a financial commitment that could be speculative or undermine the resources required to sustain the product and its Cardano adoption after the grant.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

We target 500 distinct external users, acquired through Nextrium's existing community, UNILAG student-association outreach, referrals, targeted word-of-mouth, and later, Nigerian TikTok/Instagram creators. We expect roughly half to become recurring agreement initiators, with repeat use from service providers and customers. Stablecoin usage comes from genuine commerce: users fund protected agreements and settle completed or refunded engagements through verified stablecoins on Cardano. Our target of 3,000 transactions is based on approximately 1,500 protected settlement cycles, with funding and settlement creating multiple genuine on-chain actions per cycle. CIP-0170 usage comes from participants establishing and using verifiable Cardano-linked identity/attestations throughout real agreements, targeting 1,200 genuine attestations. Activity will be distributed across the measurement window rather than concentrated in spikes. We will not pay, rebate, or otherwise incentivize users to transact; sponsored-fee UX may be used for accessibility, but those fees will not count toward adoption.

### How will you reach and onboard real users - and what evidence backs your channels?

We will onboard at least 500 external users through a combination of existing communities and scalable acquisition channels. Initial outreach will leverage Nextrium's existing community and our previous work with the [University of Lagos Sciences Students’ Association on Cardano onboarding](https://x.com/nextriumglobal/status/1882727364968550609?s=20), while we explore additional student associations within UNILAG and other universities. A referral program and targeted word-of-mouth outreach will support early adoption. After initial validation, we will expand through Nigerian TikTok and Instagram creators whose audiences include students, freelancers, professionals, and small businesses. We will track users by acquisition source and target at least 500 distinct external users.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, Nigerians use direct bank transfers, informal agreements, marketplaces with payment protection, and custodial escrow services. Emerging services such as EscrowPay, SafeTrades, Ajé, and LINQ address parts of this problem. Accordiax differs by making the agreement itself the foundation of the transaction: scope, price, timeline, and deliverables are agreed before escrow, and disputes are resolved against those terms. We are extending this proven model beyond academic consulting into general commerce, replacing custodial escrow with non-custodial Cardano settlement and supporting verified stablecoins and other Cardano assets.

### Please provide details about the Technology Readiness Level selected for your existing product

Accordiax is an operational MVP with 4 external users and 10 completed end-to-end agreement workflows during validation, including 2 agreements involving real payments. The platform demonstrates structured requests, offers, agreements, escrow, delivery, disputes, identity verification, and payouts. Evidence: [Accordiax](https://www.accordiax.com/), [TRL 5 Evidence Pack](https://drive.google.com/file/d/1RwB_s3xGYoFk4CHTONOf2viQy9-kcxWP/view?usp=sharing), and [Cardano repository](https://github.com/Nextrium/accordiax-cardano-lab). The proposed Cardano integration is new work, with core escrow feasibility already validated on Preprod.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Accordiax separates the commercial agreement layer from the settlement layer. The application manages requests, offers, signed terms, delivery, and disputes; a Plutus V3 Cardano escrow contract controls the settlement asset and executes release/refund conditions. We considered stablecoins because the product needs non-custodial settlement for commerce; our existing traditional payment flow cannot provide this conditional settlement model. The settlement layer therefore accepts verified stablecoin policies rather than issuing our own asset. [**Architecture** ](https://github.com/Nextrium/accordiax-cardano-lab/blob/main/docs/architecture/accordiax-cardano-integration.md)documents the design.

Wallet abstraction is a core requirement. Informal-commerce users should not need prior knowledge of UTxOs, ADA fees, minimum-ADA requirements, or collateral before transacting. Accordiax will construct and guide transactions while preserving user authorization. Prototype testing demonstrated that native-asset outputs require dynamic ADA calculation and that transaction completion can depend on UTxO selection and collateral. Production, therefore, requires resource sponsorship so the seller is not forced to hold ADA solely to release funds; the sponsorship and cost-recovery model remain a production decision. CIP-0170 will add verifiable participant identity/attestation without replacing Accordiax's application identity model. The core escrow has already been validated on Cardano Preprod.

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

Accordiax initially serves students and academic consultants and has already validated its model with 4 real users. We are now expanding the same agreement-and-escrow infrastructure to buyers, sellers, clients, and service providers across Nigeria's wider commerce economy.

The underlying need is broader than our initial student market. [Nigeria's 2024 Consumer Protection Survey](https://www.findevgateway.org/paper/2025/01/consumer-protection-in-digital-financial-services) found that nearly one in four digital-financial-service users had experienced unexpected fees or been targeted by fraudsters, while only about half of affected users sought formal redress.\
\
Digital commerce is also increasingly occurring through channels where parties may not have established trust. [Visa's 2026 Nigeria study](https://www.visa.com.ng/about-visa/newsroom/press-releases/prl-11062026.html) found that 83% of consumers had purchased directly through social commerce, while 57% of consumers who experienced a scam said it occurred on social media.

Market activity further validates the demand for transaction protection: Nigerian escrow products are now being launched specifically to address buyer-seller trust, while platforms targeting the informal service economy are using structured agreements, identity verification, and escrow to improve trust and payments.

Accordiax's opportunity is to make this trust layer programmable and non-custodial through Cardano.

### Applicant name

Nextrium Global Innovations Limited

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Accordiax earns revenue through a transaction protection fee paid by the party initiating an agreement. Our proposed tiered pricing ranges from 1.5% for smaller transactions to 0.75% for higher-value transactions, with a minimum fee. This aligns revenue with transaction volume while allowing larger users to benefit from volume pricing. Third-party conversion, issuer, and payment costs will be passed through where applicable rather than treated as Accordiax revenue.

Catalyst funding accelerates the Cardano integration and initial adoption; it is not our long-term operating model. Recurring transaction revenue will fund infrastructure, support, compliance, dispute handling, and continued development, while enterprise/API volume can provide additional revenue as adoption grows.

See our [Accordiax Business Model Spreadsheet](https://docs.google.com/spreadsheets/d/1esagKpshb75Shve_Lu0w-2ErJ8olsn3QgtVAOVlToa8/edit?usp=sharing) for detailed assumptions, unit economics, costs, etc.

### On-chain identity (CIP-0170) - expected transaction count

1200

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The funding enables Accordiax to connect Cardano to an already substantial African stablecoin market through real commerce use cases. Nigeria accounts for roughly 60% of Sub-Saharan Africa’s stablecoin inflows, and stablecoins represented over 65% of Nigeria’s crypto inflows in 2024. Cardano’s USDCx infrastructure only became available on mainnet in 2026. The grant will fund engineering, stablecoin integration, wallet and fee abstraction, transaction-resource sponsorship pilots, security auditing, compliance work, partner integration, mainnet deployment, monitoring, and user acquisition. Our goal is to make Cardano settlement accessible to users who need commerce protection without requiring prior blockchain expertise.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

**1. Stablecoin settlement:** Deploy a production Plutus V3 escrow supporting at least one verified Cardano stablecoin policy within the agreement → funding → delivery → approval/release flow.

**2. On-chain identity:** Integrate CIP-0170 to link participating users to declared Cardano identity/attestation identifiers within protected transactions.

**3. Wallet abstraction:** Implement production transaction flows handling UTxOs, minimum ADA, fees, and required resources without requiring users to understand Cardano mechanics.

**4. Security & operations:** Complete production testing, security review, monitoring, error handling, and release documentation.

**5. Mainnet evidence:** Declare scripts, policies, addresses, message tag, and team wallets; provide real-user transaction hashes, explorer links, technical walkthrough, release notes, test/security evidence, and a tagged open-source release.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

400

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Millions of transactions between buyers and service providers depend on trust, yet many parties still rely on informal agreements, direct payments and limited dispute protection. This creates risk for both sides: buyers may pay upfront without confidence that the agreed work or goods will be delivered, while sellers may hesitate to begin because they cannot be certain they will be paid. When disputes occur, evidence of what was actually agreed is often weak or scattered.

Accordiax is a trust infrastructure for commerce that turns an agreement into a structured transaction. Parties define the scope, price, timeline and deliverables in writing, confirm the terms, and place payment in escrow. Funds are released only when the agreed conditions are met or resolved through the defined dispute process.

Accordiax has been validated initially through an academic consulting MVP connecting students and consultants. We are now scaling that proven agreement-and-escrow model beyond students to broader commerce and professional transactions, while replacing the platform's custodial escrow mechanism with non-custodial Cardano-based settlement.

### Supporting links (repo, site, demo)

- https://github.com/Nextrium/accordiax
- https://github.com/Nextrium/accordiax-cardano-lab
- https://www.accordiax.com/
- https://www.nextrium.org/
- https://www.youtube.com/watch?v=CctebLM55ys

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

Accordiax's underlying Cardano integration code is released under the MIT License and maintained publicly by Nextrium Global Innovations Limited. The MIT License permits use, modification, distribution, sublicensing, and commercial use, subject to preservation of the copyright and license notice. Project-specific intellectual property and branding remain with Nextrium, while the open-source code is made available under the stated MIT terms.

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

1000

### Current funded commitments

**Programme:** Intersect MBO, Cardano Product Committee, Product Research Grants (RFP 07)\
**Project:** L2 Adoption and Interoperability Demand in African Emerging Markets: A Builder-Embedded Research Study\
**Project number:** CPC-26-0015\
**Statement of Work:** SOW 2, Product Research, ER-0004b-25\
**Grantee:** Nextrium Global Innovations Ltd\
**Value:** 25,000 ADA across four milestones, paid on delivery\
**Period:** 27 July 2026 to 19 October 2026\
**Status:** Active. Milestone 1 delivered. Milestone 2 is in progress, due 4 September 2026.\
**Named Project Lead:** Abdulbasit Adigun Abdulrahman

**Team members engaged:** Abdulbasit Adigun Abdulrahman (Lead researcher), Yuguda Muhammad (research coordinator), and Samir Idris (independent technical reviewer, engaged for a defined scope).

**Deliverables:** Sixteen across four milestones, all licensed to Intersect and the Cardano ecosystem under CC BY 4.0.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We have implemented and validated the core Accordiax Cardano escrow prototype on Cardano Preprod using Plutus V3, Lucid Evolution, and Blockfrost. Testing includes escrow funding with a native asset, inline datum validation, transaction accounting, minimum-ADA handling, and a confirmed release of 1,000 NXTEST to the beneficiary. The full experiment history is documented in our [integration experiment log](https://github.com/Nextrium/accordiax-cardano-lab/blob/main/docs/INTEGRATION-EXPERIMENTS.md), with the proposed system design documented in our [integration architecture](https://github.com/Nextrium/accordiax-cardano-lab/blob/main/docs/architecture/accordiax-cardano-integration.md). Stablecoin settlement and CIP-0170 identity remain the next integration work toward mainnet.
