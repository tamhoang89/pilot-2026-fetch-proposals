# Stablecoin Working Capital and Last-Mile Cash Rails

> Stablecoin Working Capital and Last-Mile Cash Rails for Informal Retailers

## Proposal Metadata

- **Status:** finalized
- **Revision:** 33
- **Proposer:** `stake1u94re22pm03854xdln9awhqpmaurqwdmq2kpme0vzq9qcasly7q6p`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-18T17:05:11.953000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Natalia gomez \
[Natalia Gomes | LinkedIn](https://www.linkedin.com/in/elijah-g-98277873/)\
\
As CEO & Owner of Nomanini, a Cape Town-based fintech platform, she directs a business that connects informal retailers, financial service providers, and distributors across Africa by integrating digital payments, working capital, and data analytics — unlocking financial access for the continent's MSME and informal retail economy. She brings a Chartered Accountant (CA-SA) qualification and business training from GIBS Business School, giving her the financial rigor to navigate margins, cashflow, and capital strategy alongside the commercial judgment to scale a fintech serving thousands of merchants in low-margin, high-friction markets.\
\
\
\
elijah githinji

[Elijah Githinji | LinkedIn](https://www.linkedin.com/in/elijah-g-98277873/)\
<https://github.com/Ej-leone>\
As Technical Lead e architects cloud-native microservices. He has built carrier-grade telco integrations enabling mobile money and payment services across African markets, with systems specifically engineered for low-connectivity environments. Prior to Nomanini, he spent over a year as a Software Engineer at Kotani Pay, a Nairobi-based Web3 fintech that bridges blockchain and stablecoin rails to local mobile money and payment channels across Africa — giving him direct experience in both traditional fintech infrastructure and crypto on-/off-ramp systems.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Nomanini's give-back is directed at the merchants this programme is intended to serve, in the form of reduced borrowing costs for those under demonstrable financial pressure.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Source A (Loans): Merchants borrow morning float earning more than the fee by closing. Each cycle yields two merchant-signed txs (acceptance creating the UTxO, repayment closing it). Steady-state: \~60% of active merchants borrow daily.

Source B (Ramps): Merchants earn commission converting cash to stablecoins (or vice versa) at existing counters, or buying digital goods with stablecoins.

To address the initial ramp to real merchants before reaching the 60% cadence, we start with 30, scaling to a goal of 300:

Pre-Launch (Engineering):

- Finalize Cardano adapter, pool wallets, and wallet logic.
- Execute Preprod testing and mainnet smoke tests.

Post-Launch (14-Day Onboarding):

- Days 1-3: Reps guide the initial 30 high-volume merchants through new loan/CICO features.
- Days 4-7: Expand to 60 merchants. Cohort 1 enabled for stablecoin cash-in/out.
- Days 8-14: Scale to 100+ terminals. Limits auto-widen on clean repayments, clearing Epoch 1 floors before reaching the 300-merchant goal.

### How will you reach and onboard real users - and what evidence backs your channels?

 \
 Nomanini's in-country field representatives visit these merchants in person on established routes as part of existing operations

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

Microfinance\
Weekly to monthly tenors with group liability and branch visits; cannot serve a gap that opens and closes within a trading day.\
\
Telco agent float overdrafts\
Closed-loop: one operator, one country, operator-set pricing. Funds only a fraction of a merchant's multi-operator activity.\
\
Informal lenders\
Available and fast, at rates that consume the margin. The incumbent being displaced.

### Please provide details about the Technology Readiness Level selected for your existing product

Nomanini's payments platform has been in commercial production since 2010, serving informal merchants across Ghana, Kenya, Mozambique, Namibia and South Africa through handheld vending terminals connected to a cloud transaction platform, historically processing on the order of one million end-user transactions per month. Merchants transact commercially on it daily, distributors settle inventory through it at volume

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Cardano is integrated natively into the Nomanini platform: no separate application, no crypto product alongside the merchant's existing account, no parallel onboarding. Every merchant is provisioned a Cardano wallet as part of her Nomanini account, and that wallet is her operating account — funded, receiving credit-scored loan principal, taking cash-service proceeds, and repaying. The loop is **wallet → credit-scored stablecoin float → trade and cash services → repay.**

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

Nomanini serves informal retail merchants across sub-Saharan Africa. The typical merchant sells airtime, data, electricity and insurance, operates as a mobile money agent, and performs cash-in/cash-out for her community. She is the last-mile financial rail for her area, financing both her own retail stock and the agent float her customers draw on from a single pool of working capital.\
\
For the loans the embedded day to day financing model has been winning over the  cash handouts . \
<https://www.m-kopa.com/newsroom/m-kopa-reaches-10-million-customers-across-5-markets>

### Applicant name

Nomanini PTY

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

1. **Loan origination fee** — a flat fee per loan `2%`, **Crucially, the initial pilot loan pool is funded 100% from Nomanini’s own balance sheet.** No external capital providers are load-bearing for this pilot.
2. **Ramp commission** — a spread or flat fee on each cash-in/cash-out, shared with the merchant. This represents new revenue for the merchant on volume already being handled.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This grant funds the two things standing between an operating platform and a working stablecoin rail: **engineering** — native Cardano wallet provisioning with on-device keys across our deployed terminal fleet, pool and treasury operations, the credit limit engine and loan ledger, cash-in/cash-out flows, network-fee management for merchants who cannot buy ADA, and platform-to-chain reconciliation — and **merchant onboarding and support**, delivered in person by the field representatives who already visit these merchants

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. **Cardano Blockchain Adapter :** A production-ready integration implemented behind the existing chain interface in the Nomanini codebase. This handles native asset construction, min-ADA requirements, deterministic fee computation, and transaction submission (utilizing Lucid Evolution with redundant Blockfrost/Koios providers), requiring no bespoke smart contracts or validator audits.
2. **Merchant Wallet Layer on Terminal :** A self-custody wallet layer provisioned directly on the Nomanini terminal. This includes secure, on-device key generation and signing capabilities, designed with a "zero-blockchain-knowledge" UI so merchants interact only with plain-language prompts and a single accept action.
3. **Stablecoin Ramp Flows on Mainnet :** Fully functional, end-to-end cash-in and cash-out (CICO) legs executed on Cardano mainnet. .

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**Who.** Informal retail merchants across sub-Saharan Africa. The typical merchant sells airtime, data, electricity and insurance, operates as a mobile money agent, and performs cash-in/cash-out for her community. Nomanini currently serves this merchant in Ghana, Kenya, Mozambique, Namibia and South Africa.

**The problem.** She finances two books from one pool of working capital: her own retail stock, and the agent float her customers draw on. That pool is exhausted before the trading day is. When agent float runs out, cash-out requests are refused and the customer goes to a competing agent; when product float runs out, the remaining trading hours are lost margin.

The constraint is liquidity, not settlement speed. Float is already loaded over mobile money — instant, via USSD, without internet. That rail works and is not what we propose to replace. What is missing is credit: a loan taken mid-morning and repaid from the day's takings by the next day No conventional lender can originate it. Banks' cost to originate exceeds the total interest on a single-day loan of that size and they require collateral and a credit file she does not have; microfinance operates on weekly-to-monthly tenors and cannot address a gap that opens and closes within one trading day. The gap is currently filled by informal lenders at rates that consume the margin the float was intended to earn

### Supporting links (repo, site, demo)

- https://nomanini.com

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

15000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

6000

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The integration is a native extension of the Nomanini platform. 

**1.** Every merchant set up with a Cardano wallet, provisioned automatically during normal Nomanini onboarding, keys on her terminal. **2.** Her daily trading history *is* the credit score — no application, no collateral — and principal is disbursed in USDM/USDCx from the Nomanini pool wallet into hers. **3.** She uses that balance as float to sell digital goods and provide cash-in/cash-out, then repays from the day's takings.
