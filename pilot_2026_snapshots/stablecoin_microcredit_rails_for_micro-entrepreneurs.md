# Stablecoin Microcredit Rails for Micro-Entrepreneurs

> Connecting global stablecoin capital to verified micro-entrepreneurs through local trust and Cardano rails.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1uxehpytm8p8a328egw6u65e3t9lxq7juwx3dxt6w2k290zgk5ta30`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T19:36:40.291000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Founder Profile & Technical Delivery**

PettyCash is founded and led by **Yacouba Mouanfon**, sole core member and accountable delivery owner. I combine 20+ years across institutional banking, trading, financial modeling, and risk management with formal training in **software architecture, coding, and technical product management**. I architected and built PettyCash from concept to its deployed, multi-tenant baseline.

**De-Risked Baseline & Institutional Alignment**

Catalyst is not funding a theoretical idea; a functional platform with CIP-30 wallet integration, lending pools, and Koios watchers already exists. Grant funding is strictly for external mainnet validation, security hardening, and pilot rollout. Additionally, advanced exploratory discussions are underway with an established impact-investment institution (confidential; not counted as a delivery dependency).

**Resilient Execution Model**

To ensure delivery resilience and avoid single-person bottlenecks:

- **Security:** Engaging independent third-party Cardano auditors.

- **Cameroon Engineering Stream:** Contracting two local software engineers to deliver production tasks (reconciliation watchers, regression tests, runbooks) against strict acceptance criteria.

I remain fully accountable for product strategy, architecture, milestones, and Catalyst reporting.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

PettyCash has not yet established production unit economics to make a treasury revenue-share or grant repayment promise responsible. Immediate priorities are compliant operations, borrower protection, local maintainability, and genuine Cardano adoption. Future treasury contributions will be assessed using audited operating data rather than projections.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Transaction Integrity & Scope**

Counted usage derives strictly from independent external users making genuine Cardano stablecoin funding and capital-management decisions through PettyCash. Team wallets, circular volume, bot churning, and subsidized fees are excluded.

**Adoption Target & Math Justification**

The target model projects **\~350–400 distinct external funding wallets** completing an average of **5–6 qualifying lifecycle actions** during the measured adoption window, generating **\~2,000 verifiable transactions** and **\~450 ADA** in network fees (avg \~0.225 ADA/tx). Repeat volume reflects organic lending cycles: initial loan funding, pool pledges, returned capital withdrawals, and re-lending. No artificial transaction splitting is used.

**Channel Pipeline & Compliance**

- **Borrowers:** Onboarding begins with &gt;10 consented and re-verified offline requests, expanding to **25–40 verified positions/pools** in Cameroon.

- **Lenders:** Sourced via Cardano communities, diaspora channels, and impact investors.

**Public Proof:** An evidence layer will report transaction hashes, distinct wallets, and fees without exposing borrower PII.

### How will you reach and onboard real users - and what evidence backs your channels?

**Borrower Onboarding**

Initial intake leverages genuine offline requests collected in Cameroon, imported only after consent and re-verification. Further demand will scale through accredited local ambassadors, cooperatives, entrepreneur hubs, and direct field outreach.

**Lender Acquisition & On-Chain Participation**

Capital providers are onboarded via diaspora networks, impact-finance communities, and Cardano stablecoin holders. The platform’s lending-pool and pledge architecture allows multiple independent CIP-30 wallets to co-fund verified positions, driving genuine, non-speculative on-chain activity backed by real capital.

**Staged Growth Targets**

Acquisition follows a phased rollout:

1. Validate initial end-to-end loan lifecycles.

2. Scale to 25–40 verified borrower positions/pools.

3. Engage \~180 distinct external funding wallets across Cardano and diaspora channels during the adoption measurement window.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=Lref96FShSc

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Alternatives vs. PettyCash**

- **Kiva:** Centralized, slow fiat settlement, opaque fee drag, and no real-time loan traceability.

- **Symbiotics / BlueOrchard / responsAbility:** Wholesale, high-barrier debt funds with aggregated institutional reporting, not grassroots micro-loans.

- **DeFi / Off-ramps:** Require borrower crypto literacy, gas fees, and collateral, lacking field verification and loan servicing.

**Why PettyCash Wins**

1. **Zero-Crypto Borrower UX:** Borrowers apply, receive, and repay in local fiat/mobile money with zero crypto knowledge or gas fees.

2. **Deterministic Attribution:** Lenders fund verified loans directly via CIP-30 Cardano wallets with 1:1 on-chain auditability.

3. **Multi-Tenant:** Reusable rails for local operators without building Web3 custody.

### Please provide details about the Technology Readiness Level selected for your existing product

PettyCash is live at `[https://pettycash.world](https://pettycash.world)`, integrating borrower intake, ambassador verification, loan publication, lending pools, lender pledges, multi-tenant controls, Cardano address registration, and reconciliation. It supports importing offline-collected demand with explicit provenance.

**Validation Completed**

The baseline has passed production builds, database functional tests, role-based access checks, multi-chain regressions, Cardano unit tests, and live health checks.

**TRL 5 Rationale**

TRL 5 is claimed because the system is validated in a relevant deployed environment, but has not yet run sustained real-world operations with independent external lenders. Security audits and local pilot servicing are the next milestones.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

**Hybrid On-Chain Architecture**

PettyCash utilizes a hybrid architecture: **Cardano** provides non-custodial, immutable settlement rails, while the **off-chain platform** manages sensitive borrower identity (PII), verification records, repayment tracking, and multi-tenant access controls.

**Lender Flow & Non-Custodial Security**

Lenders connect via standard CIP-30 wallets. Before authorizing funding, they review the allowlisted stablecoin, exact amount, destination address, and network fee. PettyCash never requests private keys or seed phrases—a wallet connection cannot move funds without explicit user authorization.

**Cardano Listener & Event Reconciliation**

The Koios-backed listener confirms funding only when:

- The destination matches an authorized, registered address.

- The asset policy and token name match allowlisted stablecoin registries.

- Exact integer amounts are verified and block-confirmation thresholds are met.

- Deduplication checks prevent double-crediting before binding to the loan record.

**Privacy & Custody Controls**

Borrowers remain entirely off-chain in familiar local fiat/mobile money to ensure financial privacy and zero crypto friction. Server-side Dfns infrastructure enables programmatic operations for organizational accounts (disabled by default until production approval policies are active). Catalyst transactions will carry pilot-specific metadata tags for public auditability without exposing borrower PII.

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

**Target Market**

The borrower market comprises micro-entrepreneurs and grassroots economic operators across emerging markets—including **Africa, Asia, and South America**—seeking productive working capital for inventory, tools, and equipment. The capital-provider market includes diaspora funders, impact-oriented individuals, foundations, family offices, CSR initiatives, and institutions seeking transparent, traceable microenterprise-finance rails.

**Demand Evidence & Field Validation**

Current demand evidence is early and precisely documented. More than thousands genuine borrower requests were collected locally offline during field assessments. Because these were not processed directly via the platform, they represent field-demand signals rather than historical platform usage. Accredited ambassadors can import these requests with original collection dates and offline-source classifications, subject to consent, re-verification, and privacy controls.

**Rollout Strategy & Validation**

Cameroon serves as the first controlled pilot market to validate legal and operational workflows before expanding to broader regional corridors in Africa, Asia, and Latin America. PettyCash makes no unverified claims of historical funded volume or product-market fit at scale; the pilot converts a deployed technical baseline and genuine field demand into measurable on-chain settlement, adoption, and operating evidence.

### Applicant name

Yacouba Mouanfon

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

**Revenue & Business Model**

PettyCash earns disclosed platform and servicing fees solely on successfully funded loans, complying with local regulations. Revenue never relies on borrower application fees or speculative platform tokens.

**Self-Sustaining On-Chain Activity**

Organic loan cycles drive Cardano utility: stablecoin funding, multi-lender co-funding, capital returns, and user-directed re-lending. Catalyst funding is strictly for infrastructure, security hardening, and pilot execution—not loan capital. Loan liquidity is provided by independent lenders.

**Post-Pilot Sustainability**

Long-term growth relies on transparent performance, compliance, and low overhead. A Cameroon engineering workstream trains local maintainers on Cardano via production tasks, securing long-term technical autonomy.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

**Delivery Leadership & Budget Allocation**

Led by **Yacouba Mouanfon** (20+ yrs finance/risk, formal software architecture & product management background). Execution converts deployed infrastructure into verifiable mainnet usage via 200,000 ADA of defined work packages:

- **Stablecoin & Wallet Hardening (42k ADA):** Registry verification, UX, failure handling, settlement.

- **Cameroon Engineering (50k ADA):** 2 local devs for tests, tooling, and runbooks.

- **Security Review & QA (25k ADA):** External audit of wallet flows & listeners.

- **Attribution & Evidence (20k ADA):** Public dashboard, fee tracking, 1:1 attribution.

- **Pilot, Compliance & Ops (63k ADA):** Legal, field intake, hosting, and Demo Day.

100% future execution; zero funds used for loan principal or incentives.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- **Pre-Baseline:** Timestamped scope prevents retroactive claims.
- **Stablecoin Policy:** Verified asset policy ID, asset name, and decimals allowlisted.
- **CIP-30 Funding:** Lenders sign via CIP-30 with 1:1 on-chain loan attribution.
- **Privacy:** Automated reconciliation keeping borrower PII off-chain.
- **Adoption Standards:** Dedicated pilot label, public dashboard of hashes, fees, wallets, and cadence.
- **Mainnet Proof:** $\\ge$3 independent users complete end-to-end mainnet stablecoin flows.
- **Cameroon Pack:** Operating procedures for offline-request import and servicing controls.
- **Engineering Workstream:** Local devs deliver tests, watchers, and runbooks against acceptance criteria.
- **Security Audit:** Third-party review of wallet and reconciliation flows with fixes verified.
- **Evidence Package:** Public evidence bundle, video walkthrough, and Cardano playbook.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

PettyCash connects global stablecoin capital with micro-entrepreneurs who need small productive loans for inventory, tools, agricultural inputs or equipment but are often underserved by conventional lenders.

It connects three participants: borrowers; approved local ambassadors, cooperatives or partners that verify and service requests; and external lenders or impact-capital providers.

The flow is:

**Request → human verification → publication → Cardano stablecoin funding → reconciliation → local-currency disbursement → repayment → return or re-lending.**

Borrowers need no crypto wallet and pay no blockchain fee to apply. Cardano remains in the infrastructure layer, providing lenders with attributable settlement and auditable funding while borrowers retain a simple mobile-first experience.

PettyCash is already deployed with borrower intake, verification, lending pools, lender pledges, multi-tenant controls, wallet registration and reconciliation. Cardano capabilities include CIP-30 wallets, Cardano address registration and Koios-backed monitoring.

Catalyst funding is not retroactive. It will move this validated baseline into real external-user mainnet stablecoin funding, security-reviewed operations and measurable adoption, starting with a controlled Cameroon pilot designed for global replication.

### Supporting links (repo, site, demo)

- https://pettycash.world
- https://pettycash.world/catalyst

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

1999

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

450

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The integration is fully implemented and tested, featuring:

- CIP-30 wallet connection & Bech32 address validation.

- Mainnet/Preprod awareness & Koios-backed deposit watchers.

- Exact integer math, confirmation controls, and queue-based reconciliation.

- Dfns programmatic wallet generation & idempotent transfers (disabled by default until production approval policies are set).

**TRL 5 Rationale**

Cardano tooling is operational in a deployed staging environment, but independent users have not yet run live mainnet stablecoin loan lifecycles. Catalyst funding bridges this baseline to live external validation.
