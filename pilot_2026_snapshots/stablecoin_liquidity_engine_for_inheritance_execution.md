# Stablecoin Liquidity Engine for Inheritance Execution

> Engine that allows an easy Conversion of Cardano Native Assets into stablecoins to simplify Inheritance execution. Users Provide Stablecoin liquidity, and in return get yield from deal arbitrage.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 46
- **Proposer:** `stake1u9grxwsp2vx7585fmuycs9x8d3r8cj4w5u9g9frvfryg8hcyhd03h`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-19T23:04:49.926000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

GenWealth combines proven Cardano product delivery, smart-contract engineering, inheritance-industry knowledge, and real partner access.

[Rafael Cardoso,](https://www.linkedin.com/in/rafael-cardoso-2b03ba146/) CEO, has eight years of experience leading tech-startup projects internationally. He previously built inheritance technology in London, securing clients and partnerships with law firms and inheritance professionals. At GenWealth, he leads product, partnerships, and go-to-market.

[Leandros Holleman](https://www.linkedin.com/in/holleman-leandros-90260a74/), CTO, is a blockchain engineer experienced in smart contracts, self-custody wallets, multisig, and wrapped-Bitcoin infrastructure on Cardano. He leads GenWealth’s V2 architecture and will lead the auction contracts, security model, and stablecoin integration. Leo Heads [LnL labs.](https://lnllabs.io/)

The team has already launched and tested a Cardano inheritance MVP, developed V2 which is currently live on Cardano Testnet, and to be launched on Mainnet very soon, received and completed two Catalyst grants, and validated the product with 80+ users and 26 inheritance firms. We have 15 inheritance firms available for pilots, that will use the solution and provide pratical feedback, and a wailist of 600 users, as well as being part of Techstars and CV labs acceleration programs.

This combination enables us to build a secure auction engine while ensuring it solves a real inheritance and stablecoin-settlement problem.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

5% of revenue generated from this Liquidity Engine will go to the treasury until 180,000 ADA is repaid. We will fully repay the grant cost, and provide additional yield to the treasury. \
\
Afterwards, in our plan to decentralize the solution, all fees will be set up by governance and voting from protocol users, who will decide if any portion of protocol generated fees should go to the treasury.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

GenWealth creates genuine stablecoin usage through real inheritance and recovery auctions, that create incentives for users to aquire and provide stablecoin liquidity

Asset owners or authorized executors list eligible Cardano-native assets. Independent liquidity providers bid with verified stablecoins to acquire them. Winning bidders receive assets, while beneficiaries claim stablecoin proceeds. Each auction creates necessary onchain actions: listing, stablecoin bid deposits, bid updates, settlement, refunds, and beneficiary claims

We target **550 transactions and 400 ADA in fees** from at least **60 independent external wallets**. This is ambitious but credible given our 600+ waitlist, 80+ prior testers, 26 inheritance firms, 15 pilot-ready firms, and Cardano liquidity community

At launch, we will declare contract hashes, addresses, message tags, and team wallets. Only transactions that execute our contracts and move verified stablecoins will count. We will track all trasactions with the protocol as well transactions needed to interact such as acquiring stablecoins

This solution can be used by anyone, looking for a direct system to liquidate CNAs into stablecoins

### How will you reach and onboard real users - and what evidence backs your channels?

We will onboard real users through three validated channels:

**Existing users:** GenWealth has a 600+ waitlist and tested its Cardano inheritance MVP with 80+ crypto users. We will use direct outreach, demos, and guided onboarding.

**Professional partners:** We engaged 26 inheritance firms, with 15 available for pilots, plus law-firm and private-bank partners. They can introduce suitable users and validate compliant workflows.

**Cardano liquidity community:** We will recruit users through our Catalyst audience, Cardano community, social channels, and direct liquidity-provider outreach.

We will target our waitlist users and commit to at least 50 different wallets interacting with the solution. Qualifying activity includes stablecoin deposits, auction bids, settlement, and beneficiary claims. We will report labeled mainnet transactions, wallet counts, stablecoin volume, and network fees.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://www.youtube.com/watch?v=ahUd4qeCXR8

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, inheritance platforms focus mainly on securing and transferring assets, while DEXs and exchanges provide liquidation but are not designed for inheritance.

GenWealth combines both. Our **Liquidation Auction Engine** integrates directly with the inheritance process, allowing authorized executors to liquidate inherited assets transparently on-chain, with non-custodial settlement directly in stablecoins. Additionally, it allows for liquiditation of asset bundles, and creates a need to provide stablecoin liquidity.

This technology, could be easily adapted by other Cardano Dapps who need auctions for asset bundles. Above all,  this creates a new, unexistent, practical use case for Cardano stablecoins: **settling inheritance value securely across generations.**

### Please provide details about the Technology Readiness Level selected for your existing product

GenWealth is **TRL 6**: a working inheritance and recovery MVP demonstrated on [Cardano public testnet ](https://demo.genwealth.app/)with realistic user flows and external validation.

Our V1 supports wallet connection, self-custodial asset division, beneficiary and condition configuration. 

We also built ,tested and launched V2 (live now), a with inheritance plan creation, recovery, professional workflows and permissions, and self-custodial user control. 

We tested both with 80+ crypto users and engaged 26 inheritance firms, incorporating feedback into development. GenWealth received two Catalyst grants for V1 and has a 600+ user waitlist.

TRL 6 fits because this is a functional testnet MVP, not a concept. The proposed stablecoin auction engine is new work for mainnet.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

GenWealth will use **Plutus V2 EUTXO smart contracts** to run self-custodial, time-bound liquidation auctions for eligible Cardano-native assets, settled in verified Cardano stablecoins.

Each auction uses a script-controlled UTXO holding the asset for sale. Liquidity providers place stablecoin bids; the contract enforces the deadline, reserve price, minimum bid increment, and bid validity. At settlement, the highest valid bidder receives the asset, stablecoin proceeds move to the inheritance distribution flow, and unsuccessful bidders receive refunds. Settlement is atomic, transparent, and auditable onchain.

A separate inheritance authorization contract controls who can open an auction and how proceeds are distributed. Roles include the asset owner, executor, beneficiary, and authorized professional. GenWealth never takes custody. Legal documents and personal data remain encrypted offchain; only hashes, permissions, and execution states are referenced onchain.

Verified stablecoin policies will be managed through an allowlist, initially supporting liquid assets such as USDM and USDCx. This meets the Stablecoins category requirement by creating genuine mainnet stablecoin transactions, and creating an incentive for users to acquire, mint and provide stablecoins to the protocol. The EUTXO model fits the use case because it enables deterministic validation, atomic asset-for-stablecoin settlement, reliable refunds, and parallel auctions without a central intermediary.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Consortium

### Who is your target market, and what evidence shows real demand/product-market fit?

Our initial target market is **users holding Cardano assets and Inheritance professionals** piloting our technology, as well as Cardano users providing stablecoin liquidity and participating in the auctions, this are users looking for an opportunity for an extra yeild.. A secondary market includes custodians, tokenization firms and other Cardano applications that need a reliable way to convert assets into stable value.

We already have strong evidence of demand for our underlying inheritance solution. We have conducted **80+ individual testing sessions with crypto users and 26 inheritance firms**, with 15 available for pilot participation, and 600 users on our waitlist.

This validation revealed an important additional problem: successfully transferring assets to beneficiaries is only part of the inheritance process. Beneficiaries may inherit ADA, tokens or NFTs that they do not want or know how to manage, leaving executors to handle sales manually.

Our Liquidation Auction Engine addresses this gap by allowing authorized executors to liquidate eligible inherited assets transparently on-chain, with proceeds settled directly in stablecoins. This provides beneficiaries with a predictable and usable form of their inheritance while reducing manual handling, custodial risk and complexity

Our existing user base and professional network provide the initial distribution channel, while stablecoins provide the settlement layer to make inherited assets practically usable

### Applicant name

GenWealth

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

GenWealth will operate as a **B2B2C infrastructure platform**. Inheritance professionals, custodians, and financial institutions will pay for access to GenWealth's infrastructure and execution services.

For the Liquidation Auction Engine, revenue will come from **small fees on completed liquidations**, complemented by subscription or integration fees from professional and institutional users. *These* customers benefit from reducing the manual work, operational costs and risks of inheritance execution, giving them a clear incentive to continue using the platform.

Catalyst funding will enable us to build and validate the stablecoin settlement functionality and generate initial usage. After the pilot, every inheritance requiring liquidation can generate recurring transaction revenue, while partnerships provide scalable distribution

As usage grows, transaction volume increases without proportional operating costs, creating a sustainable model based on **usage and institutional revenue**

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Catalyst funding enables GenWealth to turn a defined, TRL-2 integration into a safe, working mainnet product within the Pilot timeline. Without it, we would prioritize our core inheritance infrastructure and delay the specialist work required for stablecoin auctions, as we would not have the financial resources to pursue it, at this stage.

Funds will cover Plutus auction and settlement contracts, verified-stablecoin allowlists, inheritance authorization and beneficiary distribution integration, wallet/frontend flows, backend indexing, testing, security review, mainnet deployment, and onboarding of users, professional partners, and liquidity providers.

This funding accelerates both delivery and genuine external-user stablecoin deamnd and activity on Cardano.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month Building window, GenWealth will deliver a mainnet stablecoin integration and core auction infrastructure:

\- Deploy updated GenWealth Plutus contracts with executor-authorized liquidation and verified-stablecoin settlement.

\- Execute a genuine mainnet transaction where an authorized executor initiates liquidation and routes a verified stablecoin payment to the inheritance settlement flow.

\- Publish script hashes, contract addresses, stablecoin policy IDs, message tags, and team-wallet declarations.

\- Test auction contracts for stablecoin escrow, bid validation, refunds, time-bound settlement, and asset delivery.

\- Build transaction logic and a vault UI for executor-initiated, stablecoin-denominated auction creation.

\- Publish technical documentation covering architecture, roles, supported assets, stablecoin allowlists, and security assumptions.

The public bidder miniapp and full auction flow will follow during the adoption phase.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

GenWealth is building a **non-custodial Stablecoin Liquidity Engine** that allows assets inherited through a GenWealth vault to be transparently converted into stablecoins on Cardano.

Today, transferring crypto to an heir is only part of the problem. An inheritance may contain ADA, tokens, NFTs that beneficiaries may not want or know how to manage. Executors are then forced to sell assets manually, often through off-chain or custodial services, creating additional cost, complexity, price uncertainty and security risks.

Our solution allows an authorized executor to initiate an on-chain auction for eligible inherited assets. Bidders compete transparently, the winning bidder receives the asset directly, and the proceeds are settled in Cardano stablecoins such as USDM or USDCx. Authorization, bidding and settlement are recorded on-chain, without GenWealth taking custody of the assets. 

The primary users are **executors and beneficiaries**, supported by inheritance professionals. As well as Cardano users, providing stablecoin liquidity and bids to the auctions. This creates a need to mint stablecoins. The infrastructure can also benefit custodians, tokenization platforms and other Cardano applications that need a reliable mechanism to convert on-chain assets into stable value.

This makes stablecoins a practical **settlement layer for inheritance**, bridging the gap between successfully transferring an asset to an heir and delivering a predictable, usable form of its value.

### Supporting links (repo, site, demo)

- https://genwealth.app/
- https://demo.genwealth.app/

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

The Smart contracts developed under this proposal will be open source under GPL (GNU General Public License), which ensures any improvements to the code should be distributed in the same license, meaning they should be open source, and are prevented from being turned into proprietary software.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

550

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

400

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Our Stablecoin Liquidation Auction Engine is at **TRL 2**. Its technical concept, user flows, and initial architecture are defined, but it has not yet been built, tested, or deployed

The planned integration includes Plutus smart contracts for time-bound auctions, verified stablecoin bidding and settlement, liquidity provision, refunds for unsuccessful bidders, Cardano-native token delivery to winners, and inheritance-specific authorization and beneficiary distribution

It will build on GenWealth’s existing V2 inheritance infrastructure, but could be adapted and used by other Dapps, who can benefit from auctions wether of unique assets or asset bundles

With this proposal we will progress from TRL 2 to a mainnet product, where users need to aquire and provide stablecoins to participate
