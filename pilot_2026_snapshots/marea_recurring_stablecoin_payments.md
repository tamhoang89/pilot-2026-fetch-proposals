# Marea: Recurring Stablecoin Payments

> Marea gives Cardano merchants predictable recurring USDM collection while subscribers set period and lifetime caps, retain control, and can cancel and recover remaining funds at any time.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 3
- **Proposer:** `stake1u8kr6zpxqc3h3rljg54ltdvex3vemk4mjk94ruclj9p7wqcleq8fv`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-23T20:05:19.011000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Tolga Yaycı - Software Engineer**

\
Tolga is a software engineer with a Computer Engineering degree and experience building and shipping blockchain products, developer tools and production applications.

\
He designed and built Marea’s tested Cardano Preprod MVP: an Aiken/Plutus V3 validator, eUTxO mandate architecture, Mesh transaction construction, Vite/React CIP-30 interfaces, automated tests, fee benchmarks and recorded create, repeat-collect, rollover and cancel flows.

\
For Marea, Tolga owns product architecture, smart-contract and application delivery, deployment, documentation, merchant onboarding and Catalyst reporting. Independent smart-contract security review and specialist compliance advice are budgeted separately so critical assurance is not self-certified.

\
**GitHub:** <https://github.com/tolgayayci>\
**LinkedIn:** <https://www.linkedin.com/in/tolgayayci/>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Starting:** Marea has no signed merchant or subscriber commitments; none are presented as traction. Before mainnet, I will publish a tracker for 40 qualified Cardano SaaS/digital-service prospects needing recurring or usage-based billing, sourced from Catalyst, Intersect, Cardano Forum and GitHub. It records contact, reply, demo, pilot and invited-user counts. Target: 40 contacted → 12 demos → 6 pilots; each targets 20–22 customers.

\
**First 14 days:** Days 1–7: 2 merchants, 20 funded mandates, 25 external subscriber wallets, 45 repeat collects and 120 qualifying transactions. Days 8–14 cumulative: 4 merchants, 50 funded mandates, 60 external subscriber wallets, 220 repeat collects and 400 transactions. The tracker and dashboard show actuals.

\
**Window model:** 125 create/fund + 2,500 collects (4–5 per wallet/week) + 125 top-up/cancel = 2,750 transactions. Preprod fees model \~1,240 ADA; the target is 1,100 ADA.

\
**Fee path:** The subscriber funds the ADA reserve at create/top-up; the external merchant signs Collect; the reserve pays the fee. This is the only production path. No team wallet funds fees. Team, mock-token, failed, rewarded or reimbursed activity is excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

Marea uses merchant-to-subscriber distribution rather than broad paid social.

- **Direct onboarding:** founder-led outreach to Cardano SaaS, infrastructure, creator, membership and professional-service merchants with recurring billing needs.

- **Merchant distribution:** merchants receive mandate templates, an integration session and dashboard, then invite customers through existing billing communications.

- **Developer channel:** public docs, SDK examples, workshops and the repository support technical evaluation and integration.

- **Retention loop:** reusable invitations and repeat collection workflows keep the product embedded in merchant billing.

\
Marea tracks merchants, wallets, funded mandates, repeat collections, retention and fees. Evidence comes from the tested MVP, public transactions, onboarding records and dashboard. No user is paid, reimbursed or rewarded to transact; team and sponsored fees are excluded.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include Stripe Billing and stablecoin subscriptions, GoCardless bank mandates, Request Finance and manual stablecoin invoices, Sablier/Superfluid streams, custodial billing, pre-signed transactions and Cardano subscription prototypes. Marea does not claim an empty market. It differentiates through one non-custodial Cardano mandate UTxO: the subscriber fixes asset, timing and caps; the merchant collects variable invoices only within those terms; exact nonce progression and an opaque invoice reference support reconciliation; and the subscriber can top up, rotate the merchant key, cancel and recover funds. This is discrete bounded billing, not unlimited authority or a continuous stream.

### Please provide details about the Technology Readiness Level selected for your existing product

Marea is a tested MVP validated on Cardano Preprod. \
\
Evidence includes:

- Aiken validator and tests;

- TypeScript/Vite/React applications and Mesh transaction construction;

- deployed script hash, fee benchmarks and explorer transactions; and

- create/fund, three successful collects, cap refusal, period rollover, and cancel with full recovery.

\
The evidence uses scripted throwaway keys; browser apps provide CIP-30 interfaces. `TopUp` and `UpdateMerchantKey` exist in the contract but are not claimed as demonstrated Preprod flows. Mock `tUSDM` tests six-decimal behavior and is not official USDM. M1 adds independent review, official-USDM configuration, mainnet deployment and real external-user operation.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Each mandate is one independent eUTxO at an Aiken spending validator. Its inline datum records subscriber and merchant credentials; exact stablecoin policy ID and asset name; period anchor, length and expiry; period and lifetime caps/counters; last nonce; \`max_fee_per_collect\`; and \`min_ada_reserve\`.

\
`Collect` requires the merchant signature and a narrow finite validity interval. The validator enforces active timing, positive amount, both caps, nonce exactly +1, exact stablecoin payment, one continuing state, deterministic counters and token conservation. The invoice reference is deliberately opaque and is not validated on-chain; it supports off-chain reconciliation.

\
The merchant contributes no spendable inputs. On a successful collect, the network fee and merchant payout’s min-ADA carry come from the mandate’s subscriber-funded ADA reserve, bounded by the two reserve fields; collateral remains unspent. `TopUp` and `Cancel` require the subscriber. `Cancel` works at any time, including after expiry, and returns the remaining assets. `UpdateMerchantKey` lets only the subscriber rotate the merchant credential; asset, timing and caps remain fixed. Independent mandate UTxOs allow parallel use across customers.

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

**Initial market:** Cardano-native digital-service merchants that bill customers weekly, monthly or by usage: SaaS, analytics and infrastructure subscriptions, memberships, creator tools and professional services. These businesses already manage repeat invoices and can distribute mandate links through their existing customer channels.

\
**Demand evidence:** Stripe has launched stablecoin subscription payments; Request Finance offers recurring stablecoin-payment workflows; Sablier supports recurring token streams; and multiple Catalyst proposals and Cardano repositories address subscriptions. Card disputes, broad payment authority and repeated manual crypto invoices create a clear merchant and subscriber problem.

\
**Marea evidence:** The tested Preprod MVP, public validator, transaction-level tests and repeat wallet flows validate the core mechanism. The product is designed specifically for variable recurring collection with subscriber-defined period and lifetime caps, cancellation and recovery. The pilot validates commercial adoption through direct merchant onboarding and measures funded-mandate activation, successful repeat collection, cancellation, support demand, merchant retention and willingness to pay.

### Applicant name

Tolga Yaycı

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Subscribers pay no Marea platform fee; their mandate’s bounded ADA reserve covers network fees and the min-ADA carried with merchant payouts. Merchants pay for the hosted layer: mandate APIs, webhooks, invoice reconciliation, analytics, notifications, accounting exports, monitoring and priority support. Pilot tiers will test a monthly SaaS fee with included mandate and collection volumes. Enterprise revenue can come from implementation and service-level support.

\
Published validators and documentation make enforcement inspectable and self-hostable, while merchants buy workflow reliability. Revenue funds RPC/indexer and hosting, monitoring, support, compliance, incident response and security maintenance. Usage continues when merchants retain subscribers and issue repeat invoices; it does not depend on a Marea token, transaction rewards or further grants. The pilot measures willingness to pay and cost per active mandate.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The grant advances Marea’s tested Preprod MVP into an independently reviewed, observable mainnet product and funds adoption work beyond engineering alone. It supports Aiken hardening; frontend/CIP-30 and backend/indexer delivery; independent security review and remediation; expanded test and QA evidence; exact official-USDM configuration; reproducible deployment; monitoring, Dune tagging and incident procedures; public documentation; and merchant onboarding. Without it, Tolga can continue delivery, but mainnet rollout, external review and ecosystem adoption would proceed more slowly and at narrower scope. The 200,000 ADA funds future work only; no transaction rewards, fee rebates, liquidity or retroactive costs are included.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, Marea will:

1. Publish a hardened Aiken validator and reproducible build.

2. Deploy new mainnet scripts for official USDM; publish script hashes and addresses.

3. Launch live Vite/React CIP-30 apps for create/fund, collect, top-up, cancel and merchant-key rotation.

4. Obtain written Catalyst fee-attribution classification and implement the approved vault-reserve or subscriber fee-UTxO route.

5. Complete an independent smart-contract security review; publish findings and remediation.

6. Publish unit, property, transaction and E2E tests, plus checklist, bug log, security note, architecture, limitations and tagged release.

7. Add the Catalyst message tag, monitoring and public Dune dashboard.

8. Complete repeat mainnet flows with external users; publish transaction hashes, explorer links, identifiers and team-wallet list.

9. Publish a technical walkthrough and deliver the live Demo Day demonstration and Q&A.

All mainnet identifiers will be newly deployed.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**Problem:** Subscription billing often asks customers to grant broad payment authority or approve every invoice manually. Merchants need predictable collection; subscribers need enforceable limits and a clear exit.

\
**Solution:** Marea is a non-custodial recurring stablecoin mandate on Cardano for SaaS, infrastructure, memberships, creator tools and professional services.

\
A subscriber connects a CIP-30 wallet, chooses the authorized merchant and official stablecoin, funds one mandate, and fixes:

- period anchor and expiry;

- billing-period length;

- per-period cap; and

- lifetime cap.

\
The merchant can collect variable invoice amounts within those limits without a fresh subscriber signature each time. Every collection requires the merchant signature, increments the nonce by exactly one, carries an opaque invoice reference for reconciliation, and pays the exact stablecoin amount.

\
The merchant cannot change economic terms or exceed either cap. The subscriber can top up, rotate the merchant key, or cancel at any time—including after expiry—and recover the remaining assets. A bounded ADA reserve inside the mandate covers collection fees and the merchant output’s min-ADA carry. Cardano’s eUTxO model makes the state and enforcement publicly auditable. Catalyst funding takes the tested Preprod MVP through independent review, official-USDM configuration, mainnet deployment, monitoring and real adoption.

### Supporting links (repo, site, demo)

- https://mareapay.com
- https://docs.mareapay.com
- https://github.com/tolgayayci/mareapay

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

Yes. Marea's Aiken validators, TypeScript/Vite/React applications, transaction-building code, tests and technical documentation will be published under the Apache License 2.0. The repository will include the LICENSE file, reproducible build/test instructions, Preprod evidence and versioned releases.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

2750

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1100

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Marea’s Preprod MVP proves the mandate logic with mock `tUSDM`, including asset conservation, capped collection, exact nonce progression, bounded fee reserves and subscriber recovery. The invoice reference is intentionally opaque and used off-chain. Mock `tUSDM` is not official USDM and cannot count toward Catalyst adoption. Production will pin Moneta’s verified mainnet policy ID and asset name, complete independent review, deploy new mainnet identifiers, add the Catalyst tag and monitoring, obtain the required fee-attribution ruling, and prove repeat flows with genuine external users. The grant moves a tested mock-asset proof of concept to a verified USDM mainnet integration.
