# Unified Autonomous Finance interface

> Jumpa is an AI financial assistant that moves and manages money across boder in chat.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 26
- **Proposer:** `stake1u8wxzfycrxvfwc9mgkkrgds96z42jmd0pvv5swtaetyx5pgcqns4h`
- **Funding requested:** ₳175,000
- **Last finalized:** 2026-08-19T19:16:54.318000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Ndukwe Anita — CEO

Previously served as COO at Susu, a savings platform that enabled users to save in stablecoins, earn rewards, and withdraw in local currency. The platform was backed by PoolTogether and won both Privy and Circle hackathons.

Anita has also contributed to projects across Axelar, PoolTogether, and Superteam Nigeria.

<https://x.com/a_nitapounds>

Damian Olebuezie — CTO

Damian is part of  at  Gida community , where he helps train and mentor new developers in the blockchain space. He has worked across multiple Web3 products, with a strong focus on building payment infrastructure.

<https://github.com/czdamian>

Ismail Mohammed — COO

Ismail previously served as the Africa Lead at Exsty, where he oversaw regional operations and drove over $200,000 in presale revenue, contributing to a total volume of $4 billion. He also worked at CoinW as a Regional Business Development lead.

<https://x.com/CryptoMDee>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who Transacts**\
African & international freelancers receiving USDM/USDCx income, cross-border traders & SMEs settling invoices to avoid banking delays and 4–6% FX losses, diaspora remittance senders, and existing Jumpa beta users moving to Cardano.

**Why They Transact**\
\~0.20 ADA fees vs bank wires or 4.8% card charges, conversational simplicity (“Send 30 USDM to @Amina”), and true self-custody with no exchange counterparty risk.

**Target & Compliance**\
2,500 transactions over 30 days (\~83/day across 150–250 wallets). Each epoch targets \~416 transactions. Volume stays under the 20% daily cap and no wallet exceeds 35%.

Plan fully complies with the Transaction Integrity Standard: only genuine external-user transactions, CIP-20 metadata tags on every tx, no self-dealing or fee manipulation.

### How will you reach and onboard real users - and what evidence backs your channels?

We will acquire users through **direct community outreach, referrals, partnerships, and targeted pilots** rather than relying primarily on paid advertising. Our initial users are travelers, immigrants, freelancers, diaspora families, and internationally active business people. We have already conducted user interviews across these segments to validate pain points around transfer costs, delays, FX and access to local payment methods. Our existing early-user base and previous Jumpa beta provide an initial audience for reactivation and testing. We will partner with travel communities, diaspora groups, freelancer communities, business associations, and local financial/payment partners to access concentrated groups with recurring cross-border needs. We will also use referrals, where users invite family members, recipients, or business partners, creating natural network effects. Our objective is to convert these channels into verified, transacting users with repeat usage.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://www.youtube.com/watch?v=e1U-ya6XGR0

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today, users rely on FX agents, banks, providers such as Western Union, Wise and Flutterwave.  Flutterwave lists 4.8% for international card transactions in several African markets, while some international settlements can take up to five business days depending on the market and payment type. <https://flutterwave.com/us/support/pricing/pricing-for-receiving-payment>

**Jumpa** brings these experiences together. A traveler spends locally, a freelancer receives income, a diaspora member sends money home, and a business pays internationally all through one conversational interface using chat, voice or images takes 3-5 minutes.

Its long-term advantage is learning from how users move money, turning that activity into personalized intelligence, automation and eventual access to credit.

### Please provide details about the Technology Readiness Level selected for your existing product

Jumpa is an operational, production-tested web application with real-world multi-chain transaction volume:

1. Live Conversational AI Engine: Parses natural language and multi-turn chat into structured transactions (transfers, swaps, deposits, withdrawals).
2. Non-Custodial Security: Seed phrases encrypted with PBKDF2 (600,000 iterations) and user PIN. Signing occurs entirely in-browser—private keys never leave the device or touch our servers.
3. Multi-Chain Settlement: Live pipelines on Solana, Stellar and Base (EVM).
4. Fiat On/Off-Ramp & Pilot: Integrated banking rails; closed beta with 87 users processed 450+ mainnet transactions and ₦3.4M+ volume.

Core AI engine, non-custodial wallet, fiat rails and settlement pipelines are already live in production (TRL 6).

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

1. Conversational Intent to eUTxO Assembly\
   Jumpa links conversational AI with Cardano’s eUTxO model. The AI parses plain-language prompts (e.g. “Send 50 USDM to addr1…”) to extract address, asset and amount. It then queries indexers for UTxOs, balances and parameters, builds an unsigned transaction that includes the stablecoin plus required min-UTxO ADA, and optimizes coin selection for low fees. CIP-20 metadata tags are added for Catalyst tracking.
2. Client-Side Non-Custodial Signing\
   A chat confirmation card shows amount, recipient, fee and collateral. After PIN entry the private key is decrypted only in-browser memory, the transaction is signed locally and broadcast to mainnet. Keys never leave the device.
3. Why Cardano Fits\
   USDM and USDCx are first-class native assets—no smart-contract execution or approvals needed. Fees are fully deterministic. Users receive a non-custodial Cardano wallet they can operate through everyday conversation.

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

Our primary customers are **people who live, work, travel, or have financial relationships across borders**: travelers, international business people, immigrants, diaspora families, and freelancers receiving or sending international payments. **West and East Africa represent a significant cross-border financial market:** Nigeria, Ghana, Kenya, Uganda, Tanzania and Rwanda alone have populations of over **450 million people**, with remittances representing a major financial flow. In 2024, Nigeria received remittances equivalent to **7.8% of GDP**, Kenya **4.2%**, Ghana **2.1%**, Uganda **2.7%**, Tanzania **1.4%**, and Rwanda **3.6%**. Users still face high costs: sending $200 to Sub-Saharan Africa averaged **7.9%**, well above the UN target of 3%.

We have validated these pain points through direct interviews and early product testing. Our initial Jumpa product onboarded **87 users and processed over ₦3.4M in transaction volume**, while our ongoing user research continues to show demand for simpler cross-border payments. We are now expanding Jumpa into an AI-powered financial assistant that combines international payments, local spending, accounts, cards, and financial management in one platform.

### Applicant name

Jumpa trading bot technology LTD

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Jumpa is a transaction-based financial platform that earns from **cross-border payments, FX conversion, and financial products**. Users pay transparent fees when they send, receive, or convert money internationally. We also earn a share of the **yield generated through our savings partnerships** and a percentage of returns from **commercial paper investment products** offered through appropriate partners. As our credit product matures, we will generate interest income from **on-chain credit**, using transaction and financial behavior to assess users rather than relying solely on traditional collateral. This enables us to serve users who are underserved by conventional banks while offering competitive rates. We have already conducted user interviews around savings, yield, commercial paper, and credit, with strong interest. Longer term, businesses can also integrate Jumpa's payment infrastructure through our API, creating recurring usage beyond grant funding.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Jumpa targets production-scale native Cardano stablecoin integrations for USDM and USDCx plus conversational tools with ₳175,000. Core blockchain engineering and eUTxO integration receives ₳50,000 (28.6%) for key derivation, transaction building, multi-asset UTxO, minUTxO and node indexer. Security auditing, cryptographic verification and testnet QA receives ₳45,000 (25.7%) for signing review, validation, Preprod/Preview testing and mitigation. AI intent engine and stablecoin flow receives ₳35,000 (20%) for AI updates, Bech32 and chat confirmations. User onboarding, diaspora pilots and adoption receives ₳30,000 (17.1%) targeting freelancers, traders and diaspora. Project management, Catalyst reporting and Demo Day receives ₳15,000 (8.6%) for milestones, compliance and documentation.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

During the 3-month window, we will build out full Cardano support across Jumpa. We will implement our non-custodial wallet infrastructure with PIN secured signing, enabling users to generate and manage native Cardano addresses directly within the application. We will integrate Cardano native stablecoins (USDM and USDCx) with our conversational AI engine, allowing users to send, receive, and manage funds via chat. The interface will include interactive confirmation cards with real-time fee calculation, balance tracking, and registered Catalyst metadata tagging for adoption measurement. Finally, we will deploy the integration to Cardano Mainnet, publish technical release notes and opensource test evidence, and deliver a live demonstration at Demo Day.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**The Problem**\
$685 billion was sent home last year at an average 6% cost tens of billions lost just moving money across borders. Over 200 million people travel across Africa and Asia each year and lose significant amounts to poor rates and fees. An African business owner may move money daily yet still struggle to access credit because that activity never appears in a traditional bank history.

**What’s missing is a simple financial layer that connects everything together.**

Imagine a migrant worker receiving money and accessing it in local currency without heavy fees. Imagine holding stablecoins, earning yield, and using local services. Imagine on-chain activity building a financial history that unlocks credit. And imagine investing in commercial papers and treasury bills without being a sophisticated investor.

**Jumpa** is a non-custodial, chat-first AI financial assistant and multi-chain payments platform. Users send, swap, save, bridge, invest and spend stablecoins using plain language almost as naturally as messaging a friend.

On Cardano we integrate USDM and USDCx so users can move from a centralized exchange into Cardano, receive the stablecoins, then send, spend, save or invest without giving up custody.

We also make commercial paper and treasury bills available through the same interface. A user should be able to say: “Put $300 of my $500 into a treasury bill and keep the rest for spending.” Jumpa handles the complexity.

### Supporting links (repo, site, demo)

- https://github.com/official-jumpa/jumpa-website
- https://www.jumpa.xyz/

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

2500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

500

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We have not yet implemented Cardano in production. Current status is TRL 4 (lab-validated architecture):

1. Architectural Design: Completed research and blueprints using CIP-1852 hierarchical key derivation for Shelley addresses, integrated with our multi-chain security model.
2. eUTxO & Native Asset Modeling: Mapped the lifecycle for USDM and USDCx, including coin selection, min-UTxO ADA (\~1.14–1.4 ADA), and indexing via Blockfrost/Maestro.
3. Conversational Intent Mapping: Designed AI prompts to detect Bech32 addresses (addr1...) and extract USDM/USDCx payment intents.
4. Adoption Tracking: Structured the transaction builder to embed CIP-20 metadata tags for Project Catalyst tracking.

This grant will fund building, testing and deploying Cardano stablecoin  to full mainnet (TRL 7/8).
