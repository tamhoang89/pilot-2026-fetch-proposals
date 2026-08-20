# AgentPay

> The Control Layer for Autonomous Payments.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 3
- **Proposer:** `stake1uxeqt4nfprcz6s9ey6x9d4ehla7lf4chp25ndzalnzn9e3qmltcgs`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-20T04:34:41.445000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

**Ezekiel Marvellous Oghenemaga — Full-Stack Developer & Architect**\
Ezekiel has 5+ years of software development experience, delivering 10+ projects serving over 1,000 users. He specializes in scalable backend architecture, APIs, databases, cloud infrastructure and application security, providing the engineering foundation for AgentPay’s policy and payment infrastructure.

<https://www.linkedin.com/in/ezekiel-marvellous-oghenemaga/>

**Peter June — Blockchain Engineer**\
Peter specializes in blockchain infrastructure, DeFi and agentic commerce across Rust, Solidity, Cairo and TypeScript. He has built Web3 applications spanning payments, identity and marketplaces and is a winner of the Solana Students Africa Hackathon.

<https://www.linkedin.com/in/peterojo/>

### **Obasi Okechukwu— CEO**

I'm the **CEO of AgentPay**, leading product strategy, partnerships, fundraising and ecosystem growth. Also have experience building technology ventures across blockchain & fintech.

[www.linkedin.com/in/obasi-okechukwu-kingsley](http://www.linkedin.com/in/obasi-okechukwu-kingsley)

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

AgentPay pledges to return 5% of net revenue generated from the Cardano integration for 24 months after reaching $100,000 **in cumulative revenue**, capped at the original grant amount. This commitment only activates once AgentPay has achieved the revenue threshold, ensuring that early-stage growth and operating sustainability are not constrained.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

AgentPay will generate genuine usage from **businesses, AI-agent developers and agent platforms** giving autonomous agents controlled budgets for real work. Agents will use Cardano to pay for APIs, data, compute, AI services and other agents, while AgentPay enforces policy before settlement. We will onboard users through Cardano/Masumi and x402 communities, hackathons, our open-source repository and direct outreach to agent builders. Usage is naturally recurring because agents repeatedly consume paid services while completing tasks. Our target of **3000 transactions** is achievable with 5–10 active external users averaging 1–2 controlled payments per active day, while still requiring sustained adoption beyond one-off test transactions.

### How will you reach and onboard real users - and what evidence backs your channels?

We will recruit early users from **Cardano/Masumi developers, x402 builders, AI-agent communities, hackathons and API/service providers**, supported by direct outreach to teams already building payment-enabled agents. AgentPay’s open-source MIT-licensed repository, SDKs, documentation and reference agents reduce adoption friction. Early users receive direct integration support: connect an agent, define its spending policy, attach a Cardano account and execute a controlled payment. These channels target developers already building agent-commerce applications rather than relying on broad marketing.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://vimeo.com/1219754737?share=copy&fl=sv&fe=ci

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include **Nevermined, Skyfire, Payman, x402 facilitators, agent wallets and internal approval systems**. Most focus on enabling agents to hold funds, monetize services or execute payments. AgentPay focuses on the **control layer before money moves**: roles, spending policies, approvals, asset/counterparty restrictions, emergency stop, isolated signing and audit evidence. On Cardano, x402 handles payment requests, Cardano settles, Masumi provides identity/escrow, while **AgentPay determines whether an agent is authorized to spend**.

### Please provide details about the Technology Readiness Level selected for your existing product


AgentPay is a **working MVP demonstrated in a relevant environment**. The platform enables autonomous agents to initiate payments while an independent policy engine enforces organizational roles, spending limits, approval thresholds, approved counterparties/assets and emergency controls before funds move. It includes x402 payment flows, policy-controlled virtual cards, isolated signing, scoped agent credentials, immutable audit evidence and transaction reconciliation. The dashboard, policy engine, payment services, database and automated tests operate as an integrated system. AgentPay is therefore **TRL 6**, with broader real-user deployment, production hardening and independent security validation as the next stage.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

### AgentPay separates organizational authorization from Cardano settlement. An autonomous agent initiates an x402 `exact` payment in ADA, USDCx or an approved native token. Before funds move, AgentPay evaluates the agent’s role, immutable spending policy, transaction/hour/day/month limits, counterparty, permitted asset and approval requirements. Pyth provides conservative USD valuation, while payment-critical checks fail closed.

Once authorized, AgentPay queries Cardano for live UTxOs and protocol parameters and constructs a constrained eUTxO transaction with the exact payer, recipient, amount, asset, fees, TTL and payer-only change.

Agents never control private keys. Approved transactions pass to an isolated signer using a remote Ed25519/HSM-style boundary. The facilitator independently verifies signed CBOR, payer inputs, payee, amount, asset conservation, fees, network, nonce and resource binding before submission.

Masumi provides agent identity and escrow/refund/reputation workflows; optional Veridian/KERI credentials strengthen trust, while Dune remains read-only analytics.

Cardano’s eUTxO model provides deterministic, verifiable settlement, while native assets such as ADA and USDCx can transfer without token approval contracts. This gives agents controlled purchasing power without direct control of organizational funds or signing keys.

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

AgentPay targets **AI-agent developers, agent platforms, API providers, fintechs and businesses deploying autonomous agents with spending authority**. Our initial beachhead is Cardano, Masumi and x402 builders whose agents purchase APIs, data, compute and other digital services.

The market is commercially significant because autonomous agents are moving from generating information to executing economic actions. x402 provides infrastructure for machine-native payments, while ecosystems such as Masumi provide agent identity, discovery and payment infrastructure on Cardano. AgentPay addresses the control layer required as these agents begin handling real organizational funds.

### Applicant name

Okechukwu Obasi

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

AgentPay uses a **B2B SaaS + usage-based model**. Businesses and agent platforms pay subscriptions for spending policies, approvals, reconciliation and audit, with usage fees scaling as their agents make more controlled payments, agents can also receive **policy-controlled virtual cards for work-related purchases at merchants that do not support x402 or crypto payments.**

Enterprise customers pay for dedicated deployments, integrations and support. The grant funds integration and initial adoption, not transaction subsidies. Usage continues because agents repeatedly purchase APIs, data, compute and services. Each purchase requires AgentPay authorization and Cardano settlement, so **revenue and genuine on-chain usage grow together**.

### Programmable tokens (CIP-0113) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

AgentPay requests **₳100,000** to move its Cardano integration from validated prototype to production mainnet deployment. Cardano/x402 and stablecoin engineering receives **₳30,000 (30%)** for mainnet settlement, ADA/USDCx support, transaction verification and reconciliation. Security, isolated signing and production hardening receives **₳25,000 (25%)** for custody, signing review, failure testing and security assessment. Pyth, Masumi and Veridian/KERI integrations receive **₳20,000 (20%)** for USD policy, identity, escrow/refund and trust verification. External-user onboarding and adoption receives **₳15,000 (15%)** for developer pilots, integration support and documentation. Monitoring, testing, Catalyst reporting and Demo Day delivery receives **₳10,000 (10%)**.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months, AgentPay will move its Cardano integration from prototype to a **live, externally usable mainnet product**. We will deploy the dashboard, Cardano x402 facilitator and isolated signer, enabling policy-controlled x402 exact payments with ADA and approved stablecoin/native tokens **(USDM and USDCx)**. The production flow will enforce roles, spending limits, Pyth-valued USD controls, approvals, asset/counterparty restrictions, emergency stop and audit evidence. We will complete Masumi identity/escrow integration, strengthen custody, reconciliation, monitoring and security testing. By M1, external users will execute the full mainnet flow. We will demonstrate at least **two independent end-to-end transactions**, publish on-chain identifiers and evidence, release tagged code and documentation, and demo the live flow at Demo Day.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Programmable tokens (CIP-0113) - fee target (ADA)

150

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

AgentPay solves a growing problem for **businesses, developers and AI-agent platforms**: autonomous AI agents can increasingly initiate payments, but giving software direct access to organizational funds creates serious financial and security risks.

AgentPay provides a **policy-controlled payment layer** between AI agents and payment infrastructure. It lets organizations set spending limits, approved assets and counterparties, approval requirements and emergency controls, while isolating signing keys and recording every decision for audit.

On Cardano, AgentPay enables controlled x402 payments using ADA, USDCx and approved native tokens, allowing AI agents to transact autonomously **without giving them unrestricted control of funds**.

### Supporting links (repo, site, demo)

- https://agentpay-zeta.vercel.app/
- https://github.com/Daniel419797/agentpay-control

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

**MIT License**

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

3000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

300

### Please provide details about the Technology Readiness Level selected for the integration you're proposing


AgentPay’s Cardano integration is at **TRL 4**, with core components implemented and validated at code/test level but not yet proven with external mainnet users. Cardano x402 `exact` payment routing and eUTxO transaction construction are designed for **ADA, USDCx and USDM settlement**. An isolated signer supports remote Ed25519 signing, while the facilitator independently verifies transactions before submission. Pyth USD controls, Masumi identity/escrow workflows, optional Veridian/KERI trust and Dune analytics are integrated. The grant will fund Preprod/Mainnet validation, production custody, security testing and real-user deployment.

The grant will fund Preprod/Mainnet validation, production custody, security testing and real-user deployment.
