# AdaBridge: CEX-to-Cardano Onramp for USDCx, EURCx & USYCx

> Withdraw USDC from Binance, OKX, or Bybit straight into Cardano as real USDCx — no bridge UI, no seed phrase, no new wallet. Just the CEX withdrawal flow you already know.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 2
- **Proposer:** `stake1u8gsyfdqddcrvv2zklp4tydpum08u7ukgn8hpd79t0370aqpzyhdd`
- **Funding requested:** ₳145,000
- **Last finalized:** 2026-08-19T16:30:34.116000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

The project is carried out by the[ TEX Labs](https://www.texlabs.org/) team, a blockchain engineering team and official partner of Midnight Network. The team has built and operated two infrastructure products for Midnight: Midnight Explorer and Midnight API Service, with hands-on experience in blockchain infrastructure, backend systems, and ecosystem development.

[**Bach Trinh**](https://linkedin.com/in/trinh-bach) **- Engineering Lead** responsible for the backend architecture, API, the consistency of the transaction-processing pipeline, and the reliability of the relayer system.

[**Hiep Tran**](https://linkedin.com/in/tranhhiep) **- Senior DevOps Engineer** responsible for mainnet infrastructure, CI/CD, relayer deployment, monitoring, alerting, and key management.

[**Long Tran**](https://www.linkedin.com/in/longdevbf/) **- Blockchain Engineer** responsible for developing the blockchain architecture, integrating smart contracts, cross-chain protocols, building the transaction processing and verification mechanism.

[**Trung Pham**](https://www.linkedin.com/in/trung-ph%E1%BA%A1m-029a5827b/) **- Senior Software Engineer** responsible for developing the relayer components and application, integrating source chains and end-to-end testing.

[**Minh Le Dinh**](https://linkedin.com/in/dinhminhle) **- Business Development** responsible for partnerships, user-acquisition channels from CEXs, wallets, and DeFi applications, as well as tracking the adoption plan.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

The users transacting are those holding assets on Binance, OKX, and Bybit who want to bring them into Cardano to trade, provide liquidity, or use DeFi the demand to withdraw from a CEX already exists; it's simply missing a simple path. USDC → USDCx is the first use case, expanding later to EURC and USYC. Frequency isn't one-off: users return whenever they need to top up a DeFi position, rebalance, or move more assets from a CEX to Cardano producing repeat usage rather than a single test-and-abandon action.

The target of 1,000 mint transactions in 60 days (\~17/day, 50 external wallets) is reasonable because the scale of real demand is already proven: USDCx reached over 15 million tokens minted within the first few weeks after launching via xReserve (Feb 2026) the pilot's target is just a small, measurable slice of that demand, not a speculative figure.

It's still ambitious because it exceeds the Stablecoins category's PoA floor (500 ADA in fees, 50 wallets vs. the floor of 435 ADA, 26 wallets), and every transaction is tied to a real CEX withdrawal with a real fee not something that can be faked or cheaply incentivized to hit a number.

### How will you reach and onboard real users - and what evidence backs your channels?

Our go-to-market strategy meets users where they already hold assets and have existing habits: centralized exchanges. Users simply withdraw from Binance, OKX, or Bybit to an address we provide, no bridge or DEX required.

Initially we combine community-led and partner-led growth via the Cardano community, blockchain developers, and ecosystem partners: **Midnight Explorer** (educational content, product campaigns), **Blockchain Pioneer Student Club** (developer workshops, hands-on onboarding), and **SeerBot/C2VN** (community reach).

We also integrate the transfer flow into wallets, DeFi apps, and ecosystem projects' docs/user flows, turning each integration into a new acquisition channel.

Channels are measured via traffic, started/successful transfers, conversion rate, and repeat usage. Milestone 1 targets \~1000 successful mainnet transactions, guiding resource priority and partnership expansion after mainnet.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/S7On-uIdT_o

### Who else solves this today - competitors/alternatives, and why does your approach win?

Current alternatives are mainly cross-chain bridges, DEXs, or intermediary chains. These require users to understand networks, wallets, gas tokens, and multiple technical steps, creating a significant barrier for mainstream CEX users. Some users simply choose not to move assets to Cardano due to this complexity.

The project differentiates by making the CEX withdrawal the entry point. Users only send assets to an address generated by the system; bridge, conversion, and cross-chain processing happen automatically in the background. The experience therefore remains close to a normal CEX withdrawal rather than requiring users to learn DeFi.

The infrastructure is also designed to support multiple assets, including USDC, EURC, USYC and future assets, reducing dependence on any single token.

### Please provide details about the Technology Readiness Level selected for your existing product

The product currently has a complete implementation of the CEX → source chain → xReserve → Cardano flow on a public testnet, allowing the entire process from receiving assets to issuing the corresponding asset on Cardano to be verified, rather than simulating individual components separately. The system has created and managed deposit addresses following the HD standard, processed asset-transfer transactions, carried out transfers via xReserve, and tracked the asset-issuance process on Cardano using a mechanism that reconciles transaction identifiers with Circle's confirmation data.

Regarding testing, 299 tests for the relayer system and 250 tests for the user interface all passed. The source code was also automatically checked for consistency, structure and common bugs before deployment.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Our architecture follows **a two-leg relay model**, leveraging Circle's xReserve instead of building a proprietary bridge and issuing our own token.

- **Leg 1 - intake:** users perform a familiar CEX withdrawal to a source-chain address generated by the system. Three independent relayers monitor deposits, using 2-of-3 consensus to confirm validity before further processing.
- **Leg 2 - transfer to Cardano:** once confirmed, the system moves assets from the intermediary address into Circle's xReserve. Circle then verifies and issues the corresponding asset on Cardano; users never touch a bridge, manage source-chain gas, or take extra technical steps.

This greatly reduces the security logic we must build ourselves: we don't mint our own tokens, maintain a peg, or control asset supply on Cardano issuance is handled by Circle's infrastructure.

A key requirement is that each deposit is processed exactly once. Since one hot wallet handles many transactions, the system reconciles a unique transaction ID with xReserve confirmation data and the Cardano mint transaction before releasing funds. During development we identified and handled many cases that could cause duplicate processing, each reviewed independently.

This fits the Stablecoins category: it expands access to CEX assets on Cardano while leveraging existing issuance infrastructure instead of building a new bridge layer and security mechanism.

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

The project's target market is the group of users who hold digital assets on centralized exchanges such as Binance, OKX, and Bybit and want to bring those assets into the Cardano ecosystem, but are not yet ready to use bridges or manage multiple wallets and networks themselves. This is a group of users accustomed to using CEXs but who have not yet had access to a direct, simple asset-transfer process suited to a mainstream experience.

Demand for bringing assets from other ecosystems into Cardano has already been clearly shown by the growth of assets such as USDCx. After USDCx was launched via Circle's xReserve mechanism in February 2026, this asset quickly reached more than 15 million tokens minted within the first few weeks, helping expand stablecoin liquidity and DeFi activity on Cardano. This is evidence that demand for using stablecoin assets on Cardano is real, although current figures do not specifically reflect the segment of users coming from CEXs.

The gap the project focuses on addressing is precisely this unmeasured segment of users: those accustomed to withdrawing assets from a CEX but who have never used a bridge or complex DeFi tools. The pilot aims to reach about 26 successful deposit transactions per day, thereby generating real-world data to measure the demand from this user group.

As assets such as USDC, EURC, USYC and other tokenized assets are supported on Cardano, the same infrastructure can be expanded to serve the corresponding asset groups and users.

### Applicant name

Texlabs

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The project's business model is based on transaction fees, creating revenue from the first transaction and reducing long-term dependence on pilot funding. Users pay a 0.20% fee on each asset transfer into Cardano, capped at 50 USDC or the equivalent value for other assets. This revenue supports relayers, RPC services, gas, infrastructure, security, and ongoing maintenance.

After the pilot, the model scales with transaction volume. Adding more CEXs, source chains, and assets such as USDC, EURC, and USYC expands the addressable transaction base without requiring a new business model for each integration.

As adoption grows, the project can also develop revenue-sharing agreements with exchanges, wallets, and DeFi applications that benefit from additional Cardano liquidity. Pilot funding therefore supports initial development and market validation, while transaction fees provide the recurring revenue needed to operate and expand the product.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The funding is expected to be used for:

- **Software development**: Expanding the architecture to integrate multiple CEXs (Binance, OKX, Bybit), multiple blockchain networks, and multiple asset pairs: USDC → USDCx, EURC → EURCx, USYC → USYCx.
- **Operations**: Servers, relayer, RPC, key management, monitoring, alerting, maintaining the system after deployment, and supporting users.
- **Testing & security**: Testing new integrations, security assessments and resolving issues before moving into production.


- **Marketing**: Partnership outreach, ecosystem content and communications, and a bug bounty program to drive adoption, visibility, and community participation.

The funding also builds the technical foundation and resources for the product to continue developing after the pilot phase.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of Milestone 1, the project will complete:

- Mainnet relayer deployment: Operating the relayer team with a 2-of-3 key-management mechanism, split among 3 independent operating parties.
- Launching a bug bounty program, with targeted marketing to gather 30 external wallets and 100 transactions on the preprod/preview network.
- First mainnet transaction: Completing at least 1 real transaction from a CEX to Cardano, in which the asset is successfully transferred and received into the user's Cardano wallet.
- Infrastructure: Announcing the necessary on-chain addresses and identifiers, address, the relayer operating parties, and the policy IDs/assets.
- Monitoring and alerting system: Completing monitoring for key system states, including slow transactions, rejected transactions, and errors during processing.
- Public demo: Publishing a complete demo simulating the real usage flow, from withdrawing assets on a CEX to receiving the corresponding asset on Cardano.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

The project is building a solution that helps users move digital assets from centralized exchanges such as **Binance**, **OKX**, and **Bybit** into the Cardano ecosystem in a way that is simpler, safer, and more accessible. Instead of requiring users to research and carry out many steps involving bridges, DEXs, networks, wallets, and gas tokens, the project aims to simplify the entire asset-transfer process and minimize the technical operations users have to handle themselves.

For example, with the **stablecoin USDC**, users can convert USDC on the source chain into the corresponding asset on Cardano, such as USDCx. This model is not limited to USDC and can be extended to many other assets, such as **EURC → EURCx,** **USYC → USYCx**, and other assets supported in the future.

The problem the project focuses on solving is that the cross-chain experience is still complex and prone to errors for ordinary users. Users must correctly identify the network, wallet address, bridge, and gas token; a single mistake can leave assets stuck or permanently lost. The project focuses on abstracting away this complexity, helping users access and use assets from different ecosystems on Cardano more conveniently and safely.

The main audience served is users who hold assets on centralized exchanges and want to bring those assets into the Cardano ecosystem, while also helping Cardano applications gain access to assets and liquidity from other blockchains.

### Supporting links (repo, site, demo)

- https://adabridge.texlabs.org/
- https://youtu.be/S7On-uIdT_o
- https://www.texlabs.org/

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

1000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

500

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The integration proposed by the project has been deployed and validated on the public Ethereum Sepolia and Cardano Preprod testnets. The entire CEX → source chain → intake system → xReserve → Cardano flow has been operated end-to-end with real transactions on testnet, rather than only verifying individual components separately or simulating with fake data.

The testing process has confirmed the ability of the system's main components to work together, including generating receiving addresses, detecting and confirming deposits, processing asset transfers, tracking transaction status, and confirming that the corresponding asset is issued on Cardano. Transactions and costs incurred during testing were also recorded to serve as a basis for evaluating real-world operational feasibility.
