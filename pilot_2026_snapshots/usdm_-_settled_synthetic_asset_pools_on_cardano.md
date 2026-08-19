# USDM - Settled Synthetic Asset Pools on Cardano

> Gold exposure on Cardano, settled in USDM : no CEX, no bridge, no CDP.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 29
- **Proposer:** `stake1uyjnt8h5kesf7hzxtvg2cmd4ltk27q8v4hzjxa0mf06xrtcjng4ck`
- **Funding requested:** ₳120,000
- **Last finalized:** 2026-08-19T07:46:38.199000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Tran Anh Quan - Aiken Engineer\
4 years on Cardano.\
GitHub: <https://github.com/Mavis2103> \
\
Nguyen Van Viet - Fullstack\
LinkedIn: <https://www.linkedin.com/in/viet-nv/> \
\
Nguyen Thi An - Product\
<https://www.linkedin.com/in/nguyen-thi-an-4a586171/>\
\
Security: contracts will be reviewed by NoWithness Lab before the pilot cap is raised.\
\
Scope discipline: this proposal is deliberately narrowed to one production pool, a reusable pool factory, an oracle path registry, a USDM settlement layer, an SDK, a UI and a public evidence bundle. Additional pools, uncapped limits and governance decentralisation are explicitly outside the pilot scope.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

This proposal gives Cardano native gold exposure, productive USDM utility, real user fees, a routable endpoint for wallets/aggregators, and a reusable synthetic-asset model. It builds on DJED-style reserves with isolated USDM pools, oracle paths and public IDs. Risks are managed through capped launch, audits, freshness checks, timelocks, multisig, partner routing and self paid user fees.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

DECLARED FEE TARGET: 1,000 ADA in counted Cardano network fees under Stablecoins, against a 279 ADA programme floor at a 120,000 ADA award.\
\
Usage comes from users moving USDM from a CEX into gold exposure on Cardano and later redeeming to USDM; treasuries rotating between USDM and a hedged allocation; aggregators routing when our quote wins; and DeFi protocols using sGOLD as a leg. This is a round trip, not one transaction.\
\
The target is built from:

- Around 1,560 external entry/exit transactions across the window.
- Around 0.64 ADA average network fee, because script execution, oracle reference input and multi-asset outputs sit above the 0.33 ADA network average. Even at 0.55 ADA, the same target needs around 1,820 transactions.
- 50 distinct external wallets against a 28 wallet minimum, a 79% margin against clustering risk.
- No single day above 20% of total and no single wallet above 35%, by spreading flow through partner routing.
- 1,000 ADA is ambitious but reasonable: 3.6x the floor, inside the Ambitious band, and about 0.44% of a 30-day network fee total. M1 delivery in month two extends the window beyond six epochs and lowers the pace to about 40 external tx/day.

### How will you reach and onboard real users - and what evidence backs your channels?

Distribution is partly engineering: adoption depends on external wallets transacting inside a fixed window.\
\
Before M1, we publish the onchain architecture, threat model and risk parameters with the simulation, run builder reviews, and start a conversation with the USDM team.\
\
At M1, we launch one capped sGOLD pool: connect wallet, deposit USDM, review quote, fee, reserve ratio, oracle freshness and cap, sign, hold and redeem. Risk limits, identifiers and known limitations are public from day one.\
\
The primary channel is stablecoin holders: users who hold or can acquire USDM. We use issuer co-marketing, USDM liquidity venues, and content around "I hold USDM, now what?"\
\
For wallets and aggregators, we ship a TypeScript SDK, transaction build examples, reference scripts, deterministic errors and test vectors. We also use direct channels.\
Activity is measured against declared script hashes, policy IDs, pool addresses and registered message tag on the programme dashboard from M1.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

There are four relevant alternatives on Cardano, but none offers USDM-settled commodity exposure.\
DJED proves reserve backed issuance works, but is limited to one stablecoin, one reserve coin, and an ADA reserve. We extend that into isolated pools with per pool oracle paths, caps, fees, and stablecoin settlement.\
Indigo proves demand for synthetics, but its CDP flow requires collateral management, liquidation checks and position upkeep. Our flow is quote driven: review quote, fee, pool health and output, then sign.\
USDM, USDCx and USDA are complements: we give holders a productive destination. DEXs and aggregators can only swap existing assets, so they become distribution partners.\
We win by filling the gap: repeatable, USDM settled, oracle-priced issuance with public verification.

### Please provide details about the Technology Readiness Level selected for your existing product

Our existing product, BTCGrow, has been live at <https://btcgrow.io/> since September 2025 and is deployed on Cardano mainnet.\
\
The Cardano synthetic pool integration proposed here is new work, but it is being built by the same team on top of that prior mainnet delivery experience.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The design uses Cardano's eUTxO model, with one isolated pool per synthetic asset and each reserve in USDM.\
\
Each pool has two onchain components. The Pool Validator guards the ReservePool UTxO holding the USDM reserve; its datum tracks supply, reserve ratio, fees, oracle path ID, config version and admin key hashes. The Minting Policy issues or burns the synthetic token only when the matching ReservePool transition is valid.\
\
Pool parameters live in a separate AssetConfig UTxO: asset name, accepted stablecoin policy ID, fee model, supply cap, reserve ratio limits, oracle paths, price freshness window and admin permissions. Changes are timelocked and multisig-gated, with every version traceable.\
\
On entry, the user sends USDM into the ReservePool and receives the synthetic token. On exit, the token is burned and USDM is returned. The validator checks that the stablecoin matches the declared policy ID; the Pyth Pro price comes from an approved path within freshness and deviation bands; reserve ratio stays within limits; fees and caps are respected; and quantities match the state transition.\
\
This fits the Stablecoins area because no position can open or close without moving the declared verified stablecoin policy, so counted-fee evidence is intrinsic. Everything resolves to script hashes, policy IDs, pool addresses, datums, redeemers and the registered message tag.\
Diagram: <https://github.com/Mavis2103/demo-stablecoin/blob/master/onchain_architecture_flow_final.jpg>

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

Our market is Cardano users, wallets, aggregators, DeFi protocols and treasuries that hold, or can acquire, verified stablecoins and want reference asset exposure without leaving Cardano.\
\
The demand pattern is already proven elsewhere, but it is still unserved here:

- Tokenised commodities: [RWA.xyz](http://RWA.xyz) tracks roughly $7.5B in tokenised commodity market cap, overwhelmingly tokenised gold such as XAUT and PAXG. Cardano's share is currently zero; there is no native gold exposure on the chain today.
- Tokenised exposure more broadly: WBTC reports 530K+ users, 116K+ BTC wrapped and $7B+ market cap, showing that users will hold a synthetic representation when it lets them stay inside a DeFi environment instead of exiting to custody.
- Oracle priced synthetics: Synthetix shows sustained demand for exposure to crypto, fiat and commodities without holding the underlying asset.
- The Cardano stablecoin gap: DefiLlama tracks a $300B+ global stablecoin market cap against tens of millions on Cardano. That gap is often described as a supply problem. It is also a demand problem: stablecoins arrive where there is something useful to do with them, and Cardano still gives verified stablecoin holders comparatively few productive destinations.\
  \
  Evidence links: 
- <https://app.rwa.xyz/commodities>
- <https://www.wbtc.network/>
- <https://defillama.com/stablecoins/cardano>
- <https://docs.synthetix.io/>

### Applicant name

Nguyen Thi An

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The business model is transaction based: revenue grows with real usage. \
\
Users pay a transparent entry/exit fee, shown before signing, when converting USDM into synthetic exposure or redeeming back. They pay because the alternative is leaving Cardano for a CEX, buying gold exposure elsewhere, or bridge/counterparty risk. 

After the pilot, revenue comes from user conversion fees; protocol share of pool fees, with part retained for reserves; routing fee share with wallets, dApps and aggregators; and setup fees for future synthetic assets. \
Costs are mostly fixed: oracle subscription, indexing, monitoring, UI/API hosting, contract maintenance, support and security review. Fee revenue grows with volume and each new pool, keeping the product viable after the grant.

\
Usage is recurring: users enter and exit gold exposure, treasuries rotate between USDM and hedged allocation, and aggregators route when our quote is competitive.

\
No user is rewarded or rebated; users pay network fees.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding moves this from a validated simulation to a capped mainnet pool inside the pilot window: audited onchain code, USDM settlement, oracle validation and an aggregator ready surface.\
120,000 ADA breakdown:

- Smart contracts and tests: 34,000
- USDM settlement + Pyth Pro validation: 18,000
- Transaction builder, quote engine, TypeScript SDK: 20,000
- UI, admin tooling, public metrics: 16,000
- External audit and remediation: 22,000
- Documentation, integration package, launch and measurement: 8,000
- Contingency: 2,000\
  The audit cost is essential: a pool holding user stablecoin reserves should not reach mainnet on internal review alone. Without funding, this remains a simulation with no mainnet identifiers, public transaction evidence or reusable primitive for the next asset.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery: month 2 or 3, to earn extra measurement epochs; deadline is fallback.\
M1 deliverables:\
1.Protocol/risk spec: multipool parameters, USDM settlement, sBTC follow on, threat model\
2.Contracts/IDs: pool factory/config, USDM reserve validator, mint/burn policy, fee/admin rules, script hashes, policy IDs, addresses, Dune tag\
3.Offchain builder: pool creation, oracle config, enter/exit, quotes, fees, slippage, error codes\
4.UI/admin: deposit USDM, review quote/health, sign/redeem, create pools, publish IDs, public metrics\
5.Aggregator package: TypeScript SDK, API examples, liquidity guide, test vectors\
6.Capped sGOLD pilot: capped USDM pool live, external enter/exit transactions, release notes\
7.Verification: unit/property tests, integration tests, audit report, issue log, critical/high fixes, Demo Day video, live URL\
\
Out of scope: extra pools beyond sGOLD, uncapped supply, governance, ADA reserves, medium/low audit fixes before cap raise.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano users holding USDM have few options beyond holding it. If they want exposure to gold or another non crypto asset, they must leave Cardano: withdraw to a CEX, buy PAXG/XAUT on another chain, or accept bridge risk. Cardano has stablecoins and CDP based synthetics, but no simple way to convert stablecoins into oracle priced realworld asset exposure and back. \
We are building USDM-settled synthetic asset pools. Each asset has an isolated reserve pool, approved oracle path, reserve ratio rules, supply cap and fee model. A user deposits USDM, reviews the quote and pool health, signs one transaction, receives the synthetic token, and can redeem back to USDM any time. There is no debt position, collateral monitoring, liquidation risk, or bridge. \
The first mainnet pool is sGOLD, tracking XAU/USD through a Pyth Pro feed. Gold fits because Cardano has no native gold exposure today, while tokenised gold has proven demand through PAXG and XAUT. sBTC and further assets can follow on the same architecture. \
USDM settlement gives verified Cardano stablecoins utility, creates a reason to bring USDM onto Cardano, and avoids ADA denominated reserve volatility. \
The deeper output is repeatability: pool factory, oracle path registry, quote and transaction builder, aggregator package, and public pool metrics. Each later asset is a configuration, not a new protocol.

### Supporting links (repo, site, demo)

- https://github.com/Mavis2103/demo-stablecoin
- https://demo-stablecoin.vercel.app/
- https://github.com/Mavis2103/demo-stablecoin/blob/master/onchain_architecture_flow_final.jpg
- https://btcgrow.io/

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

Yes. All onchain validators and minting policies will be published under an open source licence at Milestone 1, with a tagged commit matching the deployed mainnet script hashes.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1526

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The Extended Djed reserve mechanism is implemented and validated as an interactive simulation at <https://demo-stablecoin.vercel.app/>. It supports configurable reserves, oracle rate updates, mint/redeem actions, reserve ratio visualisation and transaction history. The economic model runs and has been inspected, but no Cardano validator, minting policy, USDM settlement path or transaction builder exists yet. This places the integration at TRL 3: proof of concept for the core mechanism. \
\
This grant funds the move to mainnet: Aiken validators and minting policies, USDM settlement and reserve accounting, Pyth Pro oracle validation, offchain builder and SDK, automated/property tests, security review, remediation, aggregator examples, and a capped sGOLD pool live on Cardano mainnet at M1.
