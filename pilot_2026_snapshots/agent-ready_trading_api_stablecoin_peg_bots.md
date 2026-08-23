# Agent-Ready Trading API + Stablecoin Peg Bots

> Surge packages its live non-custodial trading stack into one API and SDK: automated peg maintenance for Cardano stablecoins, plus DEX execution for developers, retail users, and AI agents.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1uxps2qmn404pnne875tjr6zjzf6d7ys4c4md434m3w3mm3gh3adnj`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-23T15:50:58.064000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Surge is built and operated by the team behind the live platform: four-DEX order construction, fill and refund detection with rollback handling, a real-time WebSocket layer, and automated strategies trading continuously on mainnet for 397 registered users. Everything in this proposal packages infrastructure this team already runs in production, which is what makes the 3-month mainnet window credible.

Team:

- Humam Husam Eldeen (CTO) ([LinkedIn](https://www.linkedin.com/in/humam-husam-eldeen/))

- Mehmet Emin Kilinc (CMO) ([LinkedIn](https://www.linkedin.com/in/mehmet-emin-kilinc/))

- Majd Mourad Agha (Software engineer) ([LinkedIn](https://www.linkedin.com/in/majd-mourad-agha/), [GitHub](https://github.com/Majd-Murad))


- Tyson (Frontend Developer)\
  LinkedIn: <https://www.linkedin.com/in/mohammad-tello> \
  GitHub: <https://github.com/TaiseerT>

- Edmund (Frontend developer)\
  GitHub: <https://github.com/Brave-source> \
  LinkedIn: <https://www.linkedin.com/in/edmund-ebiyenrin-305196192?utm_source=share_via&utm_content=profile&utm_medium=member_ios>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge ecosystem value: continued operation of the stablecoin peg bots at our own cost for at least 12 months after pilot completion, and the client SDK published and maintained for public use.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Declared target: 700 ADA in counted network fees over the measurement window, with at least 36 distinct external wallets.

Who transacts: external users on the Surge platform, which migrates onto the funded API at launch; retail users trading through spend-limited agents; developers integrating the API; and RealFi, with whom we are in discussions to stabilize USDr at its mainnet launch. Surge is non-custodial: all customer activity is signed by the customer's own wallet. Team and bot wallets are declared and excluded; targets cover external activity only.

Why ambitious but defensible: the target equals roughly 2,000 external transactions across the window. Surge is in beta: live on mainnet with 601K ADA of 30-day volume and 397 registered users, but a small set of active external traders today. The target is a launch commitment, not an extrapolation: converting the signup base at public launch, recurring strategies that transact daily by design (satisfying per-epoch floors and the daily cap), agent onboarding across 36+ wallets below the concentration threshold, and RealFi's USDr launch.

### How will you reach and onboard real users - and what evidence backs your channels?

1. **Platform migration:** Surge’s retail app becomes the API’s first production consumer at launch, moving 397 registered users and 25 monthly actives onto the funded surface. External wallets sign their own transactions; no acquisition spend is required.
2. **Agent onboarding:** Existing users get a guided flow to link an agent, set spend limits, and trade. Strategy users are the natural first adopters.
3. **Developer outreach:** Launch public docs, SDK, and a worked integration for wallets, bots, vaults, and dashboards, timed with Maestro’s sunset.
4. **Agent distribution:** Publish the SDK, MCP connector, and spend-limited-key tutorial across Cardano’s AI-agent ecosystem.

First two weeks: migrate the app, publish SDK/docs, open trials, release the agent tutorial, and label transactions from day one for on-chain measurement.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

DexHunter is the closest comparable, offering a partner swap API. Surge goes further in three ways: **scope**—full order lifecycle infrastructure, including deterministic builds, fill/refund attribution, stuck-order cancellation, and rollback handling; **custody**—builds return unsigned CBOR for customer signing, so Surge never holds keys or funds; and **agent execution**—spend-limited keys built for AI agents.

Genius Yield routes for its own venue, while Blockfrost, Koios, and Cardano MCP tools are read-only. Maestro exits September 18, 2026. No provider continuously maintains stable-stable pegs on Cardano.

Surge already has four DEX builders, fill detection, recovery logic, and real users in production. It monetizes from day one, making the infrastructure sustainable.

### Please provide details about the Technology Readiness Level selected for your existing product

Surge is live on Cardano mainnet at [beta.surgecardano.com/mainnet](http://beta.surgecardano.com/mainnet). Last 30 days: 693 transactions, 601K ADA volume, 397 registered users, 25 monthly actives, and 85 running strategies. Production includes order construction/cancellation across Minswap, SundaeSwap, WingRiders, and Splash; fill/refund detection with rollback handling; automated strategies; an internal price feed; and WebSocket price/order events. Evidence: [beta.surgecardano.com/mainnet](http://beta.surgecardano.com/mainnet), [surgecardano.com](http://surgecardano.com), and labeled on-chain transactions. Chain access uses Blockfrost, so Maestro’s Sept. 18 sunset poses no delivery risk. All work predates the grant and is not claimed as funded.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Surge introduces no new on-chain code. We compose the existing, audited DEX validators, which removes smart-contract risk from the 3-month window entirely: no validator to write, audit, or deploy. Off-chain, the stack constructs valid order transactions for four DEX protocols, returns unsigned CBOR for the user to sign (non-custodial by construction), detects fills through node events with tiered fallbacks, and handles rollbacks with a durable ledger. This is the correct architecture for the Stablecoins area: peg maintenance is a cross-DEX execution problem, and cross-DEX execution is precisely the production asset Surge holds. All pilot activity carries a registered message tag, making every transaction independently auditable on-chain against our declared identifiers.

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

Three segments, each evidenced.

1. Retail users adopting agent-driven trading. Connecting an AI agent to on-chain trading on Cardano today requires assembling pricing, transaction construction, and signing from several services. Surge reduces this to one spend-limited API key, opening agent trading to non-developers. Demand baseline: 397 registered users and 25 monthly actives running 85 automated strategies, with USDM already among our top traded assets. These users pay execution fees today (527 ADA in the last 30 days), demonstrating willingness to pay rather than asserting it.

2. Developers requiring execution infrastructure. Building DEX execution in-house means order construction, fill and refund attribution, and cancellation across four incompatible protocols, and no Cardano provider sells that lifecycle today. Teams also weigh sustainability now, after TapTools' closure and Maestro's September 2026 sunset. A typed SDK lowers the cost of adopting ours. Our own retail platform is the first production consumer, migrating onto the public API at launch.

3. Stablecoin issuers. Healthy pegs are a precondition for stablecoin commerce, lending, and settlement, and peg maintenance has no incumbent. We are in discussions with RealFi, whose asset-backed stablecoin USDr is approaching mainnet launch, to stabilize USDr across DEXs from launch: a named, time-relevant application of the funded infrastructure.

PMF signal: paying users, live volume, and named issuer demand.

### Applicant name

SURGE DAO

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Two revenue lines; one is live, one launches with the pilot.

1. Platform execution fees, operating today: 527 ADA collected in the last 30 days from real users.

2. API subscriptions: tiered plans with weighted-credit metering, so revenue tracks upstream cost (the model used by Blockfrost and Alchemy). 

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without funding, Surge remains an internal trading platform packaged incrementally around limited capacity; the peg bots, public API, and agent layer would not ship this year, and Cardano's stablecoin pegs would remain unmaintained while its infrastructure providers exit. Funding converts this into dedicated full-time delivery within the 3-month window and covers work only a public product requires: reliability hardening and security review before third parties depend on the API, tenancy, metering and billing infrastructure, stable-pair rollout, SDK and documentation, agent layer, and developer onboarding. Indicative allocation of 200K ADA: approximately 70% engineering across the three deliverables, 15% infrastructure, 10% security review and testing, 5% documentation and onboarding.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?


1. Stablecoin peg bots live on mainnet USDM/USDCx pairs: peg-deviation detection with independent price verification, liquidity-floor sizing, continuous operation.

2. Surge Core live on mainnet: /prices, /quote, /build, /orders/:id, /cancel; keys with tenant scoping, weighted-credit metering, versioned paths, idempotent builds; published SDK, documentation, and a worked integration.

3. Agent access live: spend-limited API keys enabling agents to quote and build within user-set caps, every transaction signed by the user's own wallet; retail linking flow shipped in-app.

4. Surge platform migrated onto the public API as its first production consumer, with real external users executing end-to-end mainnet transactions through the funded surface.

5. Declared footprint registered: message-tag labeling on all pilot transactions, declared addresses, and team/bot wallets excluded from adoption counts. Demonstrated live at Demo Day using the same identifiers.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano faces two concurrent infrastructure problems. Stablecoins (USDM, USDCx) drift from peg across DEXs, and no mechanism corrects them continuously. And DEX execution remains a build-it-yourself burden, months of work across four incompatible protocols before a first trade, while the hosted providers teams rely on exit the market: Maestro's developer API sunsets September 18, 2026, following TapTools' closure.

Surge addresses both from a system live on mainnet today: order construction, fill tracking, and cancellation across Minswap, SundaeSwap, WingRiders, and Splash, with automated strategies trading continuously. Last 30 days: 693 transactions, 601K ADA volume, 397 registered users.

The grant funds three deliverables.

1. Stablecoin peg bots. Our arbitrage engine, extended to USDM/USDCx pairs, closing peg deviations continuously. Ecosystem infrastructure benefiting every stablecoin holder and protocol.

2. Surge Core: API and SDK. The pricing and execution stack behind one key: prices, quote, build, order status, cancel, plus a published TypeScript SDK. Builds return unsigned CBOR and the caller signs; Surge never takes custody.

3. Agent access. Spend-limited API keys connecting AI agents to Cardano trading. Retail users link an agent and trade non-custodially without code; developers integrate the same interface.

For whom: stablecoin protocols and holders, developers needing execution rails, and retail users adopting agents.

### Supporting links (repo, site, demo)

- https://beta.surgecardano.com/mainnet
- https://surgecardano.com/
- https://docs.surgecardano.com/

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

2000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

700

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Design complete; build not started, so the grant funds genuinely new work. The stablecoin integration extends our production arbitrage engine to stable-stable pairs (USDM/USDCx): new pair configuration, peg-deviation thresholds, and liquidity-floor sizing calibrated to thin stable pools, with independent price verification so we never act on deviations that cannot be executed. The public surface is specified and unbuilt: pricing and execution as an independently deployable service, tenancy and key management, weighted-credit metering, versioned endpoints, idempotent builds, a published SDK, and documentation. The agent layer (spend-limited keys, retail linking flow) is designed and unbuilt. Each lands within the window because the underlying engine already runs in production.
