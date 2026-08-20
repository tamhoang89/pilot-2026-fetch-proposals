# Permissionless Auto-Rebalancing CLMM Vaults

> Liquidity that never sits idle - rebalanced by anyone, governed by code.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1uy52mnl5eqqqg6h8jpk34xzvwf2afq3uwzzehmcdzhuv95qt77z5w`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-20T04:40:06.643000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

1. Ho Duy Long - Project Manager
   - Responsibilities: Roadmap, milestone reporting, stakeholder comms, budget tracking
   - LinkedIn: [https://www.linkedin.com/in/long-h%E1%BB%93-42b988247](https://www.linkedin.com/in/long-h%E1%BB%93-42b988247/)
   - Github: [https://github.com/tempovote](https://github.com/tempovote/)
2. Truong Quang Hung
   - Responsibilities: APIs, indexer/chain sync, database, integrations, DevOps
   - LinkedIn: [https://www.linkedin.com/in/quang-hùng-trương-1377a2235](https://www.linkedin.com/in/quang-h%C3%B9ng-tr%C6%B0%C6%A1ng-1377a2235)
   - Github: <https://github.com/TruongQuangHung>
3. Nguyen Thi Hoang
   - Responsibilities: On-chain logic, Aiken/Plutus validators, tests, audit prep
   - LinkedIn: <https://www.linkedin.com/in/hoangnt219/>\
     Github: <https://github.com/HoangNguyen219>
4. Tran Ngoc Minh Chau
   - Responsibilities: dApp UI, wallet connection, UX, accessibility
   - LinkedIn: [https://www.linkedin.com/in/chau-tran-ngoc-minh-468b21328](https://www.linkedin.com/in/chau-tran-ngoc-minh-468b21328/)
   - Github: <https://github.com/minhchau1112>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

DECLARED FEE TARGET: 800 ADA in counted network fees (Stablecoins), against a 255 ADA floor at a 100,000 ADA award.\
\
Target: 800 ADA in counted fees across \~1,081 transactions, against a 255 ADA floor at a 100,000 ADA request. This is performance-gated, not existing volume. The baseline today is zero: no vault deployed, no depositors, no committed LPs.\
\
First 14 days after going live. Days 1-3: vaults live, eligible-vault feed public, footprint declared. Days 4-7: pilot LPs deposit from their own wallets and the first rebalances execute - check the epoch-1 floor of 66.7 ADA. Days 8-12: onboard the next cohort, fix what the first LPs hit, which I expect in wallet setup, not the validator. Days 13-14: publish a per-epoch table.\
\
Excluded: our own seed capital, team wallets, tests, circular transfers, any rebalance by a wallet we fund, any fee we reimburse. 55 external wallets against a floor of 26.

### How will you reach and onboard real users - and what evidence backs your channels?

Our users are liquidity providers, and on Cardano they are individually identifiable from public data, which makes acquisition unusually targeted.\
\
Position-level outreach. Every CLMM position, its range and its time out of range is readable on chain. We publish a free tool that lets any LP look up their own position history and see what being out of range cost them, then offer the vault as the fix. The pitch is the LP's own data.\
\
Executor recruitment. A permissionless bounty needs people watching for it, so we publish a reference keeper, a public feed of vaults eligible for rebalance, and expected bounty economics. The barrier becomes running a script, not writing one.\
\
Strategy choice as acquisition surface. We launch vaults with narrow, medium and wide strategies so an LP picks a risk profile rather than being offered one product.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Nothing on Cardano manages CLMM positions. LPs monitor manually or accept being out of range.

Manual management fails predictably: it needs attention at unpredictable times. A position exiting range overnight stays out until noticed.

Wide ranges are the workaround. They reduce the problem and discard the efficiency that justified concentrated liquidity.

Managed vaults elsewhere delegate to a trusted keeper. That works until the operator is offline or extracts value, so depositors carry operator risk as well as market risk.

Our difference is the absence of an operator. Anyone may rebalance, nobody may rebalance badly. That is a stronger guarantee than any managed vault offers, and practical because validation and execution share a transaction.

### Please provide details about the Technology Readiness Level selected for your existing product

Our existing product is Tempo (<https://tempo.vote>), a Cardano governance platform: DRep profiles and delegation, governance action tracking, dApp rankings and community polls.\
\
Usage is publicly verifiable on the site. Individual polls have recorded 1,000+ participating wallets and hundreds of millions of ADA in registered voting power, against governance actions carrying DRep weights in the billions.\
\
That places it at TRL 7: a complete system operating in its real environment, on mainnet, with real users and real on-chain state - not a testnet deployment.\
\
Tempo required wallet integration, on-chain certificate transactions for DRep registration and delegation, and chain-state indexing. The vault needs the same competences: the domain differs, the discipline does not.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Each vault is a UTxO guarded by the Vault validator, holding a CLMM position and a share-token supply representing depositor claims. Its datum records the strategy: pool identifier, range width, trigger band, range placement formula, bounty rate, strategy version, and current position bounds.\
\
Deposits mint share tokens proportional to vault value; withdrawals burn them and return proportional assets. Both are user-signed, and the validator enforces that share price cannot be moved by the depositing or withdrawing party.\
\
Rebalance is the mechanism that matters. Any wallet may build a transaction that spends the vault UTxO and the CLMM position, withdraws liquidity, and redeploys it into a new range. The Rebalance validator accepts it only if: the current pool price, read from the pool UTxO being spent, genuinely lies outside the trigger band in the datum; the new range bounds equal exactly what the strategy formula produces for that price; total vault value after the rebalance is at least the value before, minus the permitted bounty and pool fees; the bounty taken matches the datum rate; and the strategy version is unchanged. Any deviation aborts.\
\
The executor therefore chooses only timing, never destination. There is no operator key and no off-chain component the vault depends on. Strategy parameters are timelocked and multisig-gated.

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

The market is liquidity providers on Cardano concentrated liquidity pools. We start with Dano Finance's CLMM because its contracts are open source, its SDK is public, and pool and position state is readable on chain - so the problem can be measured, and our claims verified, without privileged access.\
\
From public on-chain data over the last 2 months:

- 66 active liquidity positions across Dano CLMM pools
- 18 of provided liquidity sat outside its range at any given time
- 14 positions were never rebalanced after going out of range\
  \
  Every out-of-range position is capital its owner intended to earn fees and did not. That is the demand case, and anyone can reproduce it from the chain.\
  \
  The pattern is proven elsewhere: Gamma, Arrakis and similar CLMM vaults on Ethereum attracted substantial deposits because passive LPs cannot monitor ranges themselves. Cardano has concentrated liquidity but no vault layer above it.

### Applicant name

Long Hồ

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue is a performance fee on fees the vault positions actually earn, plus a protocol share of the rebalance bounty and configuration fees for new pairs and strategies. We are paid on returns generated, not on capital parked.\
\
The case for the LP is arithmetic. Capital out of range earns nothing, and public data shows how often that happens. A performance fee levied on fees actually earned is strictly preferable to no fees at all.\
\
Cost structure is fixed and unusually light: contract maintenance, monitoring, support, periodic review. Notably absent is keeper infrastructure - the permissionless design removes it entirely, which is the main reason operating cost stays low once grant funding ends.\
\
Operation is autonomous. Rebalances occur when price moves, executed by whoever is watching, funded by the bounty. No step requires our presence, which is what makes the model durable.\
\
Bounties are paid from vault fee accrual. Executors fund their own transactions.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Concentrated liquidity without a management layer under-delivers for everyone not watching it full-time. Building that layer trustlessly - strategy enforced in the validator rather than by an operator - is more work than building it with a keeper, and it needs an audit before it can hold LP capital.\
\
Allocation of the 100,000 ADA request:

- Vault validator, share accounting and deposit/withdraw: 25,000
- Permissionless rebalance validator and bounty mechanics: 22,000
- Strategy research, backtesting and calibration: 10,000
- Transaction builder, strategy engine and library: 13,000
- Eligible-vault feed, reference keeper and dashboard: 10,000
- External security audit and remediation: 18,000
- Documentation, launch and measurement: 4,000

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery: month two of the three-month window, to earn additional measurement epochs.\
\
On-chain: Vault validator with share accounting; permissionless rebalance validator with bounty mechanics; strategy registry with timelocked, multisig-gated updates; declared mainnet script hashes, addresses and the registered Dune metadata message tag.\
\
Off-chain: transaction builder for deposit, withdraw and rebalance; strategy engine computing eligible rebalances and bounty; vault view showing range, value, fees earned and share price; public feed of eligible vaults; reference keeper.\
\
Live mainnet: 6 vaults holding real LP capital, with at least one rebalance executed by an external unaffiliated wallet and transaction hashes published.\
\
Verification: property tests for strategy enforcement and share accounting; backtests; external audit and remediation of critical and high findings; release notes; repo tag.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Concentrated liquidity is better than constant-product liquidity in theory and often worse in practice, because nobody is watching.\
\
An LP picks a price range. Inside it, capital earns far more fees per unit. Outside it, the position earns nothing - capital is fully converted into the weaker asset and sits idle, taking impermanent loss with no fee income to offset it. ADA moving a few percent is enough to push a tight range out of play.\
\
Staying in range means monitoring price and rebalancing manually. That is a full-time job, and LPs who do it well capture most of the returns while everyone else provides liquidity that is out of range more often than in it.\
\
We are building vaults that keep positions in range automatically. An LP deposits once. The vault holds a CLMM position with a defined strategy: range width, rebalance trigger, and the formula for where the new range goes.\
\
The decision that makes this different from every managed-vault product is that rebalancing is permissionless. There is no keeper we operate and no privileged address. Any wallet may submit a rebalance, and the contract accepts it only if the price genuinely sits outside the trigger band, the new range matches the formula exactly, no value leaves the vault, and the executor takes only the permitted bounty.\
\
That inverts the usual trust model. In a managed vault, depositors trust the manager. Here the strategy is enforced by the validator, and an executor influences only timing.

### Supporting links (repo, site, demo)

- https://github.com/tempovote/clmm-vault
- https://github.com/tempovote/tempo-vote-v2

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

1081

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

800

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The strategy model is specified against Dano Finance's open-source CLMM: trigger band, range placement formula, share accounting, and the validity rules that let any wallet execute a rebalance without being able to execute a harmful one. Dano's contracts are open source and its SDK public, so no privileged access is needed to build or verify this.\
\
No vault validator exists on any network yet, placing the integration at TRL 2.\
\
This grant funds the climb to mainnet: the vault validator and share accounting, the permissionless rebalance validator, the transaction builder, the eligible-vault feed and reference keeper, strategy backtesting and calibration, property and integration tests, an external audit and remediation, and live vaults holding real LP capital on mainnet at Milestone 1.
