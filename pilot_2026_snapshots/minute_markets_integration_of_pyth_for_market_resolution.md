# Minute Markets: Integration of Pyth for Market Resolution

> Integrating decentralized oracle infrastructure into Minute Markets to enable reliable, verifiable price settlement for high-frequency 15-minute on-chain markets.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 31
- **Proposer:** `stake1uykc5y3tecvepardywpvky6tvhqguumzcepptkav3vu7w5gpsz4xl`
- **Funding requested:** ₳130,000
- **Last finalized:** 2026-08-24T03:34:45.528000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

- Daniel Sampson: Co-founder of Metera Protocol and I led the launch of both Metera Protocol and Minute Markets. For this project, I will serve as Project Manager, coordinating the development and delivery of the integration while overseeing product strategy, partnerships, and business viability to ensure the solution is technically feasible and commercially sustainable. Linkedin: <https://www.linkedin.com/in/daniel-sampson-26966a225>


- Lawal Musa Role: QA and End-to End testing. Github: <https://github.com/musalawal04> LinkedIn: <https://linkedin.com/in/musalawal04>
- Mahadi Abuhuraira Role: Backend infrastructure Github: <https://github.com/mamt4real> LinkedIn: <https://linkedin.com/in/mamt4real>
- Idris Samir Role: Validator remodelling, oracle integration, and offchain. Github: <https://github.com/scisamir> LinkedIn: <https://linkedin.com/in/scisamir>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Minute Market’s usage is tied to the incentives attached in every user facing protocol action. Whether it is users placing predictions for a potential prize win or users submitting oracle price updates onchain for a share of the rewards from a just concluded/expired market.   

\
Participants in ADA price predictions can win from fellow participants or from the protocol pool since each live market cycle is matched with 5ADA opposing bet from the protocol funded pool. So participants are always certain of rewards in the event of a winning bet.\
\
Current implementation is timed at 15mins and assuming all markets are engaged and transitions happen as often as the markets expire, then we can expect to have about 90 - 96 active markets within a 24hr period and that happens as often as every 15Mins (+-30secs). Each market transition is a confirmed oracle update by users which is charged at 0.29ADA. The same system can record 0 participation. However, our assessment of the protocol is based on current proven usage which puts us on a mid-case scenario of daily transaction count between 0 - 96 transactions and between 0 - 2880 transactions during the 30 - 35 days  adoption phase.

### How will you reach and onboard real users - and what evidence backs your channels?

We'll lean on Metera and Minute Market's existing Cardano community, its social channels, ecosystem relationships, and partnerships, to bring in new users.

But the bigger point is we already have a working, active user base. Our 50 unique bettors have placed around 3,200 orders between them, which tells us that once someone's onboarded, the short-duration format keeps them coming back.

Going forward, we're splitting focus between acquiring new users and getting more out of the ones we already have as we roll out additional markets and assets.\
\
Social Media:\
<https://x.com/minute_markets>\
<https://x.com/MeteraProtocol>\
\
Live apps: \
<https://www.minutemarkets.io/>\
<https://app.meteraprotocol.io/>

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Polymarket and PancakeSwap are our biggest competitors out there although they are not native to Cardano. 

Minute Markets focuses on fast, simple and short-duration prediction markets specifically on Cardano. Unlike broader platforms such as Polymarket and PancakeSwap, we're not trying to compete with the big event-based prediction markets. We are designed specifically around short-term markets that resolve every five minutes, with outcomes and settlement handled on-chain. This creates a simpler user experience, faster feedback and a product built specifically for users who want to make frequent, short-term predictions. This is our winning strategy.

### Please provide details about the Technology Readiness Level selected for your existing product

Minute Markets is a fully deployed, production-ready polymarket/pancakeswap style prediction market protocol running on Cardano mainnet. It operates live 15-minute markets continuously, with users participating in real markets and the full market lifecycle executing as designed, from prediction and on-chain transaction processing through oracle-based outcome determination and automated settlement.

The protocol has demonstrated sustained operation in a real production environment rather than a testnet or controlled prototype, with live markets resolving consistently and all core smart-contract functionality performing as expected. The product is a complete and operational system proven through successful mainnet deployment and real usage.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Minute Markets uses Cardano smart contracts to manage the full lifecycle of a market, from market creation and user participation through to outcome determination and settlement. A market is opened with defined parameters, users submit their positions on-chain, and once the market expires, the outcome is determined from the relevant asset price provided by the oracle.

The current architecture relies on an oracle price being made available to the settlement logic at the end of each market. The market validator checks the market state, expiry conditions and supplied price data to determine whether the UP or DOWN outcome has been reached, after which the settlement logic allows winning positions to be paid according to the market rules.

The proposed Pyth integration fits this architecture because Pyth would provide the price data used at the critical point of outcome determination, while the existing Minute Markets validators remain responsible for enforcing the market rules and settlement. This keeps the core market and settlement logic on-chain while replacing the price-data component with a more transparent and decentralized oracle source.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Our users are crypto-native retail traders looking for quick, low-friction exposure to price movement.

The product has been live on mainnet since April 14, 2026. In that time we've done about 33,480 ADA in volume across 3,200 orders, with 62 registered users. Average ticket size sits around 10.53 ADA.\
\
Smart contract address: addr1wyyfk4jzkfu2rw3jzpqwfzspdj8q65hgrhwz2fn09c6n0ugsjggvl

### Applicant name

Daniel Sampson

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Our business model is usage-based. We charge a platform fee on every user activity on the platform. Since launching April 14, we have already generated roughly 1,590 ADA in fees. (Smart contract address: addr1wyyfk4jzkfu2rw3jzpqwfzspdj8q65hgrhwz2fn09c6n0ugsjggvl)\
\
As for what keeps the product running after the pilot, the continuous volatility in the crypto market keeps the product running as more volatility/price movements creates tradeable outcomes which is what Minute Markets are built for. So this goes beyond the pilot funding. Consequently, as users participate in predictions, the protocol generates fees which are used to maintain the protocol and for further development.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding enables Minute Markets to move ADA markets to the permissionless, oracle-driven settlement architecture as it was originally designed. The integration changes how market outcomes are determined and how markets can be settled on-chain.

On a high level, the 130,000 ADA requested funding will be used for:

- Aiken validator remodelling and Pyth verification to verify and enforce expiry-time price selection : 40,000ADA
- Off-chain pyth integration and transaction infrastructure (Settlement txs): 25,000ADA
- Permissionless settlement implementation: 25,000ADA
- End-to-end testing, hardening, and mainnet migration( including stale prices, delayed settlement, invalid updates and failure cases.): 18,000 ADA
- Security review and independent audit: 22,000

              Total: 130,0000ADA

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

**Week 1-4 (Onchain):**

1. Architecture and integration flow diagram

2. Integrate pyth SDK/contracts and establish price feed retrieval flow for ADA

3. Validator remodelling (Implement Pyth price verification within the minute market's validators).

4. Validator remodelling (Connect Pyth price updates to market state transitions and outcome determination).

5. Update settlement logic to determine winners and trigger payouts.

6. Testing and debugging

**Week 5 - 8 (Offchain)**

1. Offchain infrastructure setup

2. Update transaction building logics and services to accommodate the new integration

3. End-to-End testing and debugging

**Week 9 - 12 (Testing, Quality Assurance, and mainnet deployment)**

1. Internal testnet

2. Security review and hardening

3. Mainnet deployment and validation

### Oracles - expected transaction count

862

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Minute Markets is a prediction market on Cardano where users predict whether an asset moves UP or DOWN over a definite time window.

Minute Markets solves the problem of prediction markets being slow, complex and difficult to access. It gives users a simple way to make short-term predictions on asset price movements and receive an immediate, transparent outcome through on-chain settlement. 

It is for crypto users, traders and prediction-market participants who want a simple, low-cost way to speculate on short-term market movements without relying on centralized intermediaries.  

### Supporting links (repo, site, demo)

- https://www.minutemarkets.io/
- https://x.com/MeteraProtocol
- https://x.com/minute_markets
- https://app.meteraprotocol.io/

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

250

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

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

At this stage, the Pyth integration for Minute Markets remains at the technical conceptualization and planning phase. \
\
We have discussed how Pyth price updates would fit into the existing market lifecycle, including how verified price data would be received and used for market outcome determination and settlement. The integration approach and required changes to the existing architecture have been identified, but no implementation or on-chain validation has been completed yet. The proposed work will therefore move the integration from a defined technical approach to a tested and operational component of Minute Markets.
