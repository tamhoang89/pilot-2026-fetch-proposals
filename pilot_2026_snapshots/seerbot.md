# SeerBOT

> A non-custodial, AI-powered trading and analytics platform on Cardano, integrating real-time Oracles and verified Stablecoins.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 6
- **Proposer:** `stake1uy9evuj2y30jrwf5pa0mey50wfmm7u4fmhv3k4lshnfz55gndm0gn`
- **Funding requested:** ₳198,000
- **Last finalized:** 2026-08-20T01:43:05.531000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Proposed Answer:** The SeerBOT team is comprised of seasoned blockchain engineers, AI specialists, and product strategists with extensive hands-on experience in the Cardano ecosystem:

- [Luke Nguyen:](https://www.linkedin.com/in/anhoang12?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) Experienced in AI & Data, , hands-on with infrastructure, logic, and algorithmic design for technical indicators and AI auto trading
- [Heart Phung](https://www.linkedin.com/in/anhoang12?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app): 10+ years in Web3. Also, a smart contract developer with hands-on experience building secure, efficient trading platforms across multiple chains
- [Barov Vi](https://www.linkedin.com/in/vibao3902/): Over 4 years in Web3 across marketing and BD roles in projects, incubators, and outsourcing, driven by a passion for building strong, value-focused communities transparent and fully prepared for review by the community curators during onboarding.
- [Loc La:](https://www.linkedin.com/in/nguyenphuocloc1999/) Casual trader with a strong technical background, hands-on with multiple front-end and back-end frameworks, and experienced in building and scaling Web3 products
- [Armin Nguyen:](https://www.linkedin.com/in/anhoang12?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) Front-end developer with 2 years in Web3. Passionate about clean UI/UX and precision in execution

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Genuine on-chain usage is driven by active Cardano DeFi traders, retail investors, and AI enthusiasts. Retail users execute 2-3 rebalancing swaps per week, while advanced traders utilizing SeerBOT’s automated DCA, Limit Order, and Stop-Loss strategy vaults execute 1-5 transactions daily.

**User Motivation (Why):** Users transact to access low-slippage, non-custodial swaps secured by real-time Pyth Oracles and settled in verified stablecoins (USDM/USDCx) without compromising private keys. SeerBOT’s AI Assistant simplifies complex technical analysis into actionable conversational execution, encouraging higher transactional frequency.

- **Realistic:** Achieving a cumulative 2,000 ADA in L1 fees requires \~120 daily transactions over the 40-day measurement window. This is fully achievable by converting our active community and launching co-marketing integrations with major Cardano wallets (Lace, Eternl, Vespr) during the first two weeks post-launch. No sponsored or internal team wallets will be counted, ensuring 100% genuine, external user activity.

### How will you reach and onboard real users - and what evidence backs your channels?

We focus on "stable and informed traders on Cardano" (specifically the "Steady" and "Pro" segments) who value clarity over hype. Active and new traders currently struggle with complex, unreliable, or fragmented tools. We will onboard them by solving this pain point directly: offering an intuitive interface equipped with real-time signals, precise indicators, and AI-guided trading suggestions.

### **Channels & Evidence**

We will capture this audience through a highly targeted, community-first approach:

- **X (formerly Twitter):** As the undisputed, proven hub for crypto discourse, X will drive our top-of-funnel awareness and establish our brand presence where crypto users naturally congregate.

- **Telegram & Discord:** We will tap into dedicated Cardano trader communities on these platforms. The evidence backing this is the existence of concentrated, high-intent user groups within these channels that are currently underserved and untapped.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/IvYyb7PGAxk

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Competitors/Alternatives:** Centralized Telegram trading bots (prevalent on EVM and Solana) and standard decentralized exchanges (DEXs) on Cardano.

- **Why SeerBOT Wins:**
  1. **Cardano Focus:** ....
  2. **Conversational AI Analysis:** SeerBOT is not just a routing engine; it acts as an active, 24/7 personal on-chain data analyst that explains market dynamics and suggests technical set-ups in natural language.
  3. **Deep Oracle & Stablecoin Alignment:** By natively integrating real-time feed updates and verified stablecoins, we eliminate price delays and slip-page, outperforming basic DEX router interfaces.

### Please provide details about the Technology Readiness Level selected for your existing product

SeerBOT’s selection of **TRL 5** is backed by verifiable on-chain and operational evidence:

1. **Live Platform ([seerbot.io](http://seerbot.io)):** SeerBOT's web-based user dashboard is active and accessible, allowing users to connect their CIP-30 wallets securely.
2. **Operational Analytics Engine:** Our backend successfully indexes and calculates live Cardano on-chain data, displaying real-time technical indicators to active users.
3. **Proven Non-Custodial Security:** Wallet sign-ins and data-read flows are executed on-chain with zero custody over user private keys, demonstrating robust product maturity in a realistic L1 blockchain environment.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**SeerBOT’s on-chain architecture** is a secure, modular Aiken/Plutus v2 system with two core components:

- **Oracle Consumer Contract**: Retrieves and stores tamper-proof price feeds from Pyth Network on-chain.

- **Stablecoin Swap Engine**: A non-custodial contract routing verified stablecoins (USDM/USDCx). It cross-references the Oracle to ensure trades meet user slippage tolerances, instantly aborting invalid swaps.

**Why it fits technical requirements:**

- **Absolute Self-Custody**: Funds stay in user wallets until atomic settlement (zero-custody).

- **Fee Efficiency**: Aiken compiles to compact UPLC scripts, reducing exUnits and L1 costs for cheaper trades.

- **Transparent Audit**: Transactions are natively tagged with Catalyst labels, feeding directly to Dune Analytics to prevent wash trading.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

SeerBOT focuses on stable and informed traders on Cardano who prefer clarity, occasional engagement, and smart automation instead of hype or overly complex strategies.

- **Target Market:** The growing community of active Cardano DeFi traders ranging from retail newcomers looking for simpler workflows to professional traders requiring fast, data-informed strategy execution.
- **Evidence of Demand & Product-Market Fit:** AI-driven trading is experiencing massive growth globally. In other major blockchain networks, conversational trading bots and automated vaults generate tens of millions in daily volume, validating high demand. Cardano users are highly security-conscious and actively seek advanced analytical and automation tools that *do not* require sacrificing self-custody. Our testnet feedback indicates strong interest in having a unified AI analyst that directly hooks into non-custodial execution scripts.

### Applicant name

SeerBOT Team

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The platform operates on a clear fee-based model where the **users (traders)** pay for the services. It relies on three main revenue streams:

- **Trading Fees:** A flat fee of **0.1%** per trade.

- **Vault Management Fees:** Performance-based fees charged on the profits generated within the vaults.

- **Pro Subscriptions (Soon):** Future recurring revenue from premium "SeerBOT Pro" subscription tiers.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This grant of 198,000 ADA serves as a key catalyst for integrating SeerBOT with oracles and stablecoins, helping to address some of the current hurdles the platform faces on the Cardano network. 

**Budget Allocation Breakdown:**

- **45% (89,100 ADA):** Software R&D (Aiken smart contracts, AI engine optimization, frontend/backend integration).
- **25% (49,500 ADA):** Professional external Security Audit for our transactional smart contracts.
- **20% (39,600 ADA):** Infrastructure overhead (Oracle node query fees, data feeds, high-performance hosting).
- **10% (19,800 ADA):** Targeted user onboarding and educational marketing post-launch.

Details: <https://docs.google.com/spreadsheets/d/18K5T24uZnESHcwaL5XdTaqkCmTy-8NN6/edit?usp=sharing&ouid=113364882239312587968&rtpof=true&sd=true>

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month window, we will transition our proposed Oracle and Stablecoin integrations from TRL 2 to TRL 7 on Cardano Mainnet, delivering the following verifiable outputs:

**1. Technical Deliverables:**

- **Aiken/Plutus v2 Smart Contracts:** Completed, open-sourced (Apache 2.0) on GitHub with integration documentation for the Oracle Consumer module and Stablecoin Swap Engine.
- **Professional Security Audit:** A final, independent third-party audit report certifying contract safety on Mainnet.

**2. Verification & Acceptance Evidence:**

- **Live Mainnet Transaction:** At least one transaction of an oracle-verified stablecoin (USDM/USDCx) swap, proving TRL 7 functionality.
- **Tracking Setup:** Registration of script hashes, policy IDs, and Catalyst-designated transaction labels with the Dune Analytics indexer.
- **Demo Video:** A &lt;3-minute technical walkthrough video for the official Demo Day.

### Oracles - expected transaction count

2300

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

The Cardano DeFi landscape is expanding rapidly, yet everyday retail users and professional traders still face three critical barriers:

1. **Fragmented Technical Analysis and On-Chain Data:** Tracking real-time market movements, key indicators (RSI, ADX, MACD), and liquidity across multiple tokens is tedious, requiring fragmented tools and advanced technical knowledge.
2. **Security Risks from Custodial Solutions:** Many automated trading tools and bots require users to hand over their private keys, creating severe security vulnerabilities and counterparty risks.
3. **Information Overload and Data Noise:** Users are bombarded with thousands of news items daily, making it impossible to separate value from FUD. Major price moves often occur when users are asleep or offline. FOMO and panic lead to a lack of discipline and the classic "buy high, sell low" behavior

**The SeerBOT Solution:** We are building **SeerBOT**, a non-custodial, AI-driven trading and market analytics platform designed specifically for Cardano traders. SeerBOT combines conversational AI intelligence with secure automated trading contracts to optimize user capital efficiency and trading workflows.

Slide Deck Details: <https://drive.google.com/file/d/1gpqcjr9uokiUdDmfnJrnE1mUHBqeuOyD/view?usp=sharing>

### Supporting links (repo, site, demo)

- https://seerbot.io
- https://youtu.be/IvYyb7PGAxk
- https://drive.google.com/file/d/1gpqcjr9uokiUdDmfnJrnE1mUHBqeuOyD/view?usp=sharing
- https://docs.google.com/spreadsheets/d/18K5T24uZnESHcwaL5XdTaqkCmTy-8NN6/edit?usp=sharing&ouid=113364882239312587968&rtpof=true&sd=true

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

1000

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

No

### Mature product

Yes

### Licensing / IP details

All newly developed smart contracts for the Oracle integration and Stablecoin Swap Engine will be fully open-sourced under Apache 2.0 license

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

2800

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We have selected **TRL 2** for the proposed integration because it represents completely new, incremental engineering work:

- **Completed Specifications:** We have finalized the system specifications of our Aiken Oracle Consumer module and Stablecoin Swap Engine, including slippage boundaries.
- **Prototyping & Future Work:** Writing the Aiken validators, conducting unit testing on private devnets, deploying to the public testnets (Preview/Preprod) for validation (TRL 5/6), conducting external smart contract audits, and deploying the final code to Cardano Mainnet (TRL 7) are future-only development activities that will be funded entirely by this grant.
