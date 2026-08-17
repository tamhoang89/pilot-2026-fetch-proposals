# Stablecoin Payments for Cardano RWAs & Launchpad

> BankFi's RWA platform and NFT/Token launchpad will peg prices to USD and accept stablecoin payments for non-volatile investment opportunities.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 28
- **Proposer:** `stake1u94sq8k5rjax9vf5eyyzdnmh0d7nmhgf38f4tchdnspyy5qrlwfym`
- **Funding requested:** ₳145,000
- **Last finalized:** 2026-08-17T13:47:56.604000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Our team collectively has several decades of experience providing financial solutions on Cardano, with diverse backgrounds and skills that produce a well-rounded business strategy and product line.

**Andrew Caldwell - CEO**

<https://www.linkedin.com/in/andrew-caldwell-94557baa/>

Key decision maker and driver of business growth. Oversees budgets & operations and ensures key business partnerships are formed. Has experience managing complex systems at scale as the CEO of Smart Choice.

**Jake Shearman - CTO**

<https://www.linkedin.com/in/jake-shearman/>

Leads software and infrastructure development. Has a comprehensive understanding of Cardano's protocols (\~6 years experience). FinTech background delivering stock market data at scale.

**Stephen Caldwell - Information Security Expert**

<https://www.linkedin.com/in/stephen-caldwell-b882971b/>

Provides critical insights into fund management and associated cybersecurity measures to ensure transparent, efficient, and safe outputs in every project.

**Nicholas Fekete - Product Lead**

<https://www.linkedin.com/in/nicholas-fekete/>

Oversees team to ensure modern, reactive, and high quality product launches.

**Tyler McVety - UX & DevOps**

<https://www.linkedin.com/in/tyler-mcvety/>

User journey mapping & DevOps infrastructure management.

**Dominic Monette - Product Developer**

<https://www.linkedin.com/in/dominic-monette-7273b287/>

Ensures internal processes and product quality are optimized as we scale.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Our RWA platform is built on steady and sustainable portfolio growth, which attracts DCA buyers. With the integration of stablecoins, users will be able to purchase RWAs by moving money from their bank to stablecoins without needing to worry about ADA tax implications; this reduced barrier to entry will encourage more frequent purchases regardless of market activity. With over 1,000 users (400-500 active every month), we anticipate this product to generate several hundred qualifying transactions per month.

For our launchpad, stablecoin integrations will enable risk-averse companies to try their hand at fundraising. Due to the nature of a launchpad, these transactions will be less consistent but high impact for each sale; the RWA platform will serve as the transaction backbone to maintain our "rhythm".

We will align the launchpad integration with a high-potential sale that is already committed (not dependent on this proposal). The 2-week sprint after going live will consist of running/promoting this sale and the integrations, a site-wide banner on the RWA platform for awareness, and an X marketing campaign with graphics to showcase the benefits of our stablecoin integrations.

### How will you reach and onboard real users - and what evidence backs your channels?

We receive a consistent flow of launchpad clients through social media marketing (primarily X) and word of mouth from clients/users that have experienced our product. We frequently scan the ecosystem for companies that may benefit from a fundraise and work with them to plan the best timeline and approach to maximize value for their company and its users.

Our two products work harmoniously, with users of the launchpad having natural exposure to our RWA platform. We find clients that need to raise funds, we introduce their users to our ecosystem through the sale, and we create a win-win situation -- in terms of both awareness and financial opportunities -- for our clients, ourselves, and the users of both.

The evidence lies in our history and reputation, having provided launchpad services for more than 100 Cardano clients (and custom development services for many more).

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Our true competitors at a large scale are outside of the Cardano ecosystem. Other Web3 ecosystems have their own versions of launchpads and RWA opportunities, and our main differentiator is one of Cardano's main differentiators -- native assets -- and the ways in which we leverage them for cheap and transparent payment flow, ownership management, and asset distribution.

Within Cardano, NMKR and Titans are competitors in the launchpad and RWA sectors, respectively, however our focuses have significantly diverged and our offerings now have very little overlap.

Our quality, track record, intuitive user experiences, and deep Cardano knowledge have provided us with a consistent supply of clients and users for 5 years now.

### Please provide details about the Technology Readiness Level selected for your existing product

Our launchpad has been operational on Cardano mainnet for more than 5 years, with 40+ million ADA processed from thousands of users and \~228,000 transactions to date.

Our RWA platform has been operational on Cardano mainnet for more than 1 year, reaching over 1,000 users, a TVL of \~$2.5 million USD, and distributing over 1.5 million ADA in returns to date.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The foundational core of both of our products is transactions processing. We have a comprehensive suite of tools and processes for transaction building, indexing, and processing on both the frontend and backend.

Our transaction infrastructure leverages the UTxO model for on-chain payments and distributions but off-chain processing. We can support stablecoins with flexible implementations and without the need for an on-chain oracle. This will allow us to adapt our solutions over time to match the needs of any corporate and enterprise use cases involving our products.

Specifically, the integration work defined in this proposal will include:

- Backend tracking, utilizing multi-source exchange APIs, of ADA's current and historical price to enable real-time and delayed transaction processing
- Backend tracking, using libraries that integrate with Cardano's main DEXs, to ensure that USDM and USDCx, which are assumed to be $1 for the purposes of purchases, do not slip more than an acceptable amount from that assumed peg.
- Websocket integrations for real-time price updates (note: this is partially supported for the RWA platform already for a different use case).
- Frontend UI/UX and transaction building updates that utilize real-time price updates to facilitate both stablecoin and ADA purchases.
- Frontend UI updates for user education and clarity around stablecoin purchase options.
- Overhaul off-chain transaction processing to validate stablecoin and dynamic ADA payments.

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

Our RWA platform and our NFT/Token launchpad both target end users that are are interested in Web3 investment and ownership opportunities. As a neutral provider of Cardano fundraising services and RWA revenue opportunities, the target market expands as our offerings deepen in certain industries and expand to others.

Our launchpad clients are small-medium businesses that see an opportunity to raise funds through payments on Cardano. We typically see companies targeting $100,000 to $1,000,000 per launch. Anecdotally, the majority of funds raised are from high net worth individuals. These are the same users that want to avoid volatility in their holdings while they wait for investment opportunities, making them prefer to operate in stablecoins.

The proof of demand and our current level of product-market fit is evidenced by both our history and our KPIs. We bootstrapped in 2021 and have been serving our Cardano products without interruption for 5 years now. We scaled slowly and continue to grow the team over time. We have handled more than 100 launches, processed 40+ million ADA in sales, and are responsible for 228,000 Cardano transactions. We currently have a baseline of \~2,000 transactions per month, with a large positive variance on months with more popular sales. Our RWA platform has 1,022 unique users, \~$2.5 million USD in TVL, and has distributed more than 1.5 million ADA from RWAs since launching in 2025.

### Applicant name

BankFi (BankerLabs Sociedad Anonima)

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

As mentioned, we have a track record of 5 years providing NFT and token launches on Cardano in addition to over 1 year of operating an RWA yield platform. This proposal does not fund a new service, but rather integrations of stablecoins into our existing services. This means that purchases on the RWA platform and launchpad will leverage stablecoins directly for reduced volatility.

Our business model is primarily commission based for both products; we receive a percentage of all funds generated by the RWAs on our platform, and we typically receive a percentage of each sale on our launchpad (occasionally payment is upfront).

Our history in the space provides word-of-mouth leads consistently, however we also drive growth by continuing to innovate, support broader use cases, and adapt to trends. This stablecoin integration is a perfect example of a feature with a clear use-case that we'll be able to use to drive increased client and user traffic.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Stablecoins on Cardano, while widely available, are not yet widely adopted. Without funding, we are not able to justify the business decision of investing development hours into stablecoin-related infrastructure. This funding will enable us to optimize for long-term stablecoin adoption without focusing on the short-term bottom line, implementing the volatility-eliminating features that are needed to drive greater corporate and enterprise usage of our launchpad and RWA platform.

130,000 ADA - Software engineering salaries to support dedicated frontend and backend development time for the integrations.

14,000 ADA - Project management, non-technical product design, UI mockups

1,000 ADA - Vendor costs & overhead, e.g. short-term price API costs

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- The BankFi: Pillar launchpad gives clients the option to peg the NFT or token sale price to USD. When selected by the client, the sale will accept USDM and USDCx at the pegged sale price.  USDM and USDCx are valued at exactly $1 USD for the purposes of the purchase. ADA will be accepted at a rate that changes dynamically based on market price changes.
- RWA purchases on the BankFi platform can be made utilizing both USDM and USDCx in addition to the current ADA option. USDM and USDCx are valued at exactly $1 USD for the purposes of the purchase

### How far along is the integration you're proposing, today?

TRL 1 - Basic principles observed

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

We have been operating our NFT & Token launchpad on Cardano since 2021. BankFi: Pillar (formerly Yepple) has processed more than 40 million ADA in sales across 228,000 transactions (as of August 1, 2026).

We launched the BankFi platform, a suite of RWA yield opportunities, in early 2025 to give Cardano users the ability to passively earn from industry verticals of their choice; no hyped sales, no marketing gimmicks, just straightforward passive financial tools and avenues for portfolio growth.

Both of our products have a shared pain point: volatility. Our launchpad clients' operational costs, as well as our RWA acquisition, demand USD. When accepting payments in ADA, the time between receiving payment and deploying capital creates a significant risk. Accepting payment creates an obligation to the buyer; if the value of that payment decreases from volatility before it can be utilized, there is now an imbalance where the buyer is owed something in return but the seller does not have the means to fulfill it. We have seen this lead to poor returns, sacrificed features, and, at times, bankrupt companies.

Our stablecoin integration will not only allow payments using stablecoins in both our RWA platform and our launchpad, but it will also allow our clients to peg the sale price to USD so that the stablecoin payment options remain steady while the other payment options adapt based on volatility. This solves the volatility problem for any company looking to launch on Cardano.

### Supporting links (repo, site, demo)

- https://bankerlabs.io
- https://bankerlabs.io/market/trade/mining
- https://pillar.bankerlabs.io/wargrum

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

4000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

780

### Current funded commitments

Our company was bootstrapped for 5 years (no external funding). In early 2026, we received our only grant to date: a $40,000 payment through the Builder DAO for a combination of marketing and KPI growth. All planned work was completed ahead of schedule, and the majority of KPIs have already been reached. There is one month remaining until the end of that funding cycle, but there is no overlap between the work funded through the Builder DAO and the features detailed in this proposal.

<https://drive.tiny.cloud/1/1k7o5om77fbj49trj4wcd7e92e5fxyf06ggt48984hs8asnh/ffb3c626-36ed-4918-8315-c029f24823dd>

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We have not yet begun any planning or development beyond the extent required to ensure that this proposal is accurate, viable, and beneficial to our business operations and applicable related targets.
