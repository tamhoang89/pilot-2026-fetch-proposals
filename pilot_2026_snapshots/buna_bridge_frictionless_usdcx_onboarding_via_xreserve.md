# Buna Bridge: Frictionless USDCx Onboarding via xReserve

> Empowering emerging markets with frictionless, mobile-first USDCx onboarding directly to Cardano via Circle xReserve

## Proposal Metadata

- **Status:** finalized
- **Revision:** 20
- **Proposer:** `stake1u966rf62ct6pcfgn79wn37gys7xurry962ggr9xcfjntc8sqsy52e`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-21T17:12:02.942000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

**Abubakari Mahamudu – Chief Product Officer & Project Lead** 

Role: Oversees product strategy, technical roadmap alignment, user journey mapping, and backend smart contract integration architecture. Brings extensive experience as CEO of Tumahub and Chief Product Officer of [ZaaNet.xyz](http://ZaaNet.xyz).

- LinkedIn: <https://www.linkedin.com/in/abubakari-mahamudu-a41b94213/>

- GitHub: <https://github.com/abubakarim78>

- X (Twitter): <https://x.com/abusadickm_78>

**Sahabia Yakubu – Lead Developer & CEO** 

Role: Directs core blockchain development, smart contract logic, Circle xReserve integration, and technical architecture. Brings deep Web3 leadership as Founder of HackerBoost, former MakerDAO African Ambassador (2019–2021), Founder of DeFi Africa, and CEO of ZaaNet.

- LinkedIn: <https://www.linkedin.com/in/realsahabia/>

- GitHub: <https://github.com/sahadevgh>

- X (Twitter): <https://x.com/sahadevgh>

**Track Record & Capability:** The team has proven execution capability, having successfully built and shipped Buna Protocol V1.0 end-to-end (evidenced by our live Arbitrum and Tron contracts); links are shared in the supporting links section of this proposal. To ensure Cardano-native execution matches our product vision, we are using the open-source Lucid framework and have explicitly allocated budget for comprehensive third-party smart contract security audits before mainnet deployment.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

**Who & Why:** Underbanked individuals, freelancers, and small merchants across West Africa (anchored through HackerBoost hubs in Ghana) transact to bridge external stablecoins or onboard fiat into Cardano-native stablecoins (USDCx) to hedge against local currency inflation securely.

**Target Justification & Frequency:** We are targeting **1,500 transactions generating 350 ADA in fees** (averaging \~0.23 ADA per standard smart-contract transfer). 350 ADA sits comfortably in the "Ambitious" scoring band above the ₳312 baseline floor for a 150,000 ADA Stablecoin grant.

Achieving 1,500 transactions across our warm pipeline of \~350 initial users equates to a highly realistic **\~4.2 transactions per user** during the measurement window (e.g., initial onboarding deposits, weekly savings top-ups, and P2P transfers). This grounded, defensible frequency reflects organic monthly savings habits. By scoping down to just the Onboarding feature, we completely resolve concerns about inflated volume while remaining fully compliant with the Transaction Integrity Standard.

### How will you reach and onboard real users - and what evidence backs your channels?

- **Buna Pilot Users (\~200):** Active savers using our Telegram bot and web app will be guided to migrate funds to native USDCx through a zero-friction in-app campaign.

- [**HackerBoost Hub**](https://www.hackerboost.org/) **(\~150):** Direct onboarding of university students, alumni, and freelance developers in Tamale.

- **Tamale Offline Hangout Community (\~500):** Direct onboarding through established coworking spaces and tech meetups in Northern Ghana.

**First Two Weeks Post-Launch Plan:**

- **Days 1–3:** Deploy the verified integration to mainnet; update the UI; publish the declared footprint.

- **Days 4–7:** Activate Cohort 1. Onboard the first 50-70 pilot savers for live USDCx onboarding.

- **Days 8–11:** Host workshops at HackerBoost hub, onboarding 40-50+ freelancers for stablecoin bridging.

- **Days 12–14:** Track transaction volume, gather feedback, and publish adoption metrics.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/0uXZDd197hA?si=ofucyuccqFMf3H68

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Existing Alternatives:**

- **CEXs & P2P (Binance P2P, Yellow Card):** Custodial, exposing users to account freeze risks and high KYC friction.

- **Standard Web3 Bridges:** Built for power users; steep UTxO and bridging friction for retail savers.

- **Mobile Money:** Convenient for payments but offers zero protection against fiat inflation.

**Why Users Switch to Buna Bridge:**

- **Conversational UX:** Manage digital dollars via a Telegram Mini App and mobile/web app with zero blockchain jargon.

- **Self-Custody:** Funds settle on-chain via client-side user-signed transactions without exchange custody risk.

- **Direct Onboarding:** Connects external USDC seamlessly to Cardano natively via Circle’s open xReserve.

### Please provide details about the Technology Readiness Level selected for your existing product

Buna Protocol is an active, mature product with an Arbitrum pilot testing live with real-world users (accessible via our Telegram bot `@buna_protocol_bot` and web/mobile app). Through our operational deployment, we have successfully validated core architecture components, including our conversational Telegram bot interface and peer-to-peer (P2P) transaction workflows. The existing system has proven reliable and useful in live market conditions.

Our live L2 transaction volume is publicly verifiable on Arbiscan: (0xd117e0fe7aa5f77c8cc00ae133c78727cd4fb830) and Tronscan:(TUTq79xDPgjxmE8V3umpuR4pZULmY5HqAF)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Buna Protocol adopts a hybrid on-chain/off-chain model custom-built for underbanked West African users:

- **Conversational Interface & True Non-Custodial Key Management:** The user experience is handled via a Telegram Mini App/web/mobile friendly interface. **Crucially, the backend only builds unsigned transactions (using Lucid).** Users sign transactions client-side via in-app encrypted local storage or deep-linking to standard CIP-30 mobile wallets. Private keys never touch our servers.

- **Permissionless Onboarding:** We bridge external stablecoins natively into Cardano using Circle's open xReserve infrastructure. This is an open, permissionless smart contract and SDK requiring no closed bilateral business agreements to integrate.

- **Why It Fits:** By pairing high-performance off-chain chat workflows with client-side transaction signing and Circle’s tier-one stablecoin architecture, our design removes barriers like seed-phrase friction without sacrificing non-custodial security.

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

**Who is your target market, and what evidence shows real demand/product-market fit?**

Our main market includes retail savers, tech freelancers, and remote workers in Ghana and Sub-Saharan Africa (SSA) seeking inflation-proof digital dollars. Mobile money, with [23 million](https://www.bog.gov.gh/wp-content/uploads/2024/11/Summary-of-Economic-and-Financial-Data-November-2024.pdf) active accounts in Ghana, is the region's financial backbone but offers no yield against steep inflation. Chainalysis reports [stablecoins account for 43% of crypto transactions](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2024/) in SSA as residents hedge currency devaluation.

**Evidence of Demand & Product-Market Fit:**

Buna Protocol already serves real users on **the** web/mobile and via our Arbitrum-based Telegram bot (`@buna_protocol_bot`), validating demand for our mobile-first UX. In pilot testing, users identified multi-step exchange bridging as the primary barrier to self-custody. We have a live, proven pilot deployed on Arbitrum and Tron, evidenced by our active on-chain transaction logs (see Supporting Links for our Arbiscan and Tronscan contract addresses). With the recent launch of USDCx, Cardano now possesses the native stablecoin liquidity required to serve this market. Buna provides the missing retail-friendly interface to access it.

**Warm Pipeline:** We will onboard \~200 active Buna savers and \~150 freelancers from HackerBoost for mainnet adoption.

### Applicant name

Abubakari Mahamudu

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

**Revenue Model:** Buna Protocol operates a sustainable, transaction-based model. For peer-to-peer (P2P) escrow settlements and external withdrawals, we apply a progressive fee tier ranging from 1% for small transactions down to 0.25% for high-volume transfers (above 20,000 GHS).

**Who Pays?** External users pay standard Cardano network fees directly from their non-custodial wallets. Buna never takes custody of funds, nor do we subsidize or pay transaction fees on users' behalf.

**Post-Pilot Continuity:** Usage persists beyond the grant window because personal saving and P2P settlement are continuous financial habits. Hedging fiat against inflation using digital dollars becomes a recurring monthly routine rather than a one-time promotional event.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This grant enables the focused building of Cardano stablecoin onboarding for Buna Protocol, expanding into the ecosystem safely and efficiently. **High-Level Fund Allocation (₳150,000):**

- **40% (60,000 ADA)** - Core Integration: Circle xReserve SDK bridging adapters, Lucid transaction builders, and Cardano-native USDCx mapping

- **20% (30,000 ADA)** - Security & Audits: Third-party smart contract security review for safe mainnet deployment

- **20% (30,000 ADA)** - Frontend & UX: Telegram Mini App and web integration for client-side CIP-30 signing and seamless stablecoin flows

- **10% (15,000 ADA)** - Infrastructure & Indexing: Cardano nodes, Kupo/Ogmios/Blockfrost services, and data pipelines

- **10% (15,000 ADA)** - Deployment & Onboarding: Pilot workshops and educational outreach

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- **Month 1 (Weeks 1–4) - Core Architecture & SDK Setup:** Develop and test Lucid transaction builders; integrate open-source Circle xReserve bridging adapters for frictionless Cardano-native USDCx onboarding.
- **Month 2 (Weeks 5–8) - Frontend & UX Wiring:** Update the Telegram Mini App and web interface to support client-side, non-custodial wallet signing and guided fiat-to-stablecoin onboarding flows.
- **Month 3 (Weeks 9–12) - Security Audits, Mainnet Deployment & Demo Day:** Complete third-party security reviews (funded by the 20% budget allocation), deploy final updated application logic to Cardano mainnet, finalize test evidence bundles, release documentation, and deliver the live Demo Day presentation to enter the M2 adoption window.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Buna Bridge is a conversational, mobile-first stablecoin onboarding tool designed to solve the fiat depreciation crisis for everyday savers, freelancers, and remote workers across West Africa.

**The Problem**

Our users face double-digit fiat inflation and currency depreciation. While Cardano offers tier-one stablecoin infrastructure (such as USDCx), it remains inaccessible to non-technical retail users. The barrier to entry navigating complex centralized exchanges (CEXs), managing UTxOs, and safeguarding seed phrases locks everyday underbanked users out of digital dollar preservation.

**The Solution**

We are building a single, highly optimized workflow: **Frictionless Direct Onboarding**.

Buna Bridge acts as a simplified gateway to Cardano by bringing Circle’s xReserve infrastructure directly into a familiar Telegram Mini App and web interface. We abstract the blockchain complexity entirely, allowing users to seamlessly move stablecoins from external networks or CEXs onto Cardano as native USDCx with zero Web3 jargon.

By focusing strictly on creating a frictionless onboarding bridge, we empower underbanked African users to preserve their wealth in stable digital dollars (USDCx) securely, non-custodially, and intuitively.

### Supporting links (repo, site, demo)

- https://bunaprotocol.com
- https://hackerboost.org
- https://t.me/buna_protocol_bot 
- https://github.com/hackerboost 
- https://arbiscan.io/address/0xd117e0fe7aa5f77c8cc00ae133c78727cd4fb830

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

1500

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

350

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

While Buna Protocol is in pilot testing, this specific Cardano USDCx / Circle xReserve integration is still in the conceptual and architectural planning stage (TRL 2). We have mapped out the system design to connect our conversational Telegram Mini App to Cardano primitives using Lucid for native USDCx onboarding via xReserve. 

This grant will fund the hands-on engineering, smart contract wiring, testing, independent auditing, and deployment required to bring this single, focused integration from concept to a fully operational mainnet release.
