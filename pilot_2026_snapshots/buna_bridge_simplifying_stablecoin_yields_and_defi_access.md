# Buna Bridge: Simplifying Stablecoin Yields and DeFi Access

> Empowering underbanked users to protect savings against inflation via intuitive, non-custodial USDCx vaults and seamless stablecoin swaps on the Cardano network

## Proposal Metadata

- **Status:** finalized
- **Revision:** 9
- **Proposer:** `stake1u966rf62ct6pcfgn79wn37gys7xurry962ggr9xcfjntc8sqsy52e`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-19T02:41:25.771000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

**Project Team & Roles:**

- **Abubakari Mahamudu – Chief Product Officer & Project Lead**

  - *Role:* Oversees product strategy, technical roadmap alignment, user journey mapping, and backend smart contract integration architecture. Brings extensive experience as CEO of[ Tumahub](https://tumahub.netlify.app/) and Chief Product Officer of[ ](http://zaanet.xyz)[ZaaNet.xyz](http://ZaaNet.xyz).

  - *Profile / References:*[ LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/abubakari-mahamudu-a41b94213/) |[ GitHub](https://github.com/abubakarim78) |[ X (Twitter)](https://x.com/abusadickm_78)

- **Sahabia Yakubu – Lead Developer & CEO**

  - *Role:* Directs core blockchain development, smart contract logic, DeFi protocol integration (Liqwid pools and Circle xReserve), and technical architecture. Brings deep Web3 leadership as Founder of[ HackerBoost](https://www.youtube.com/watch?v=B0d79Z3UI7M), former MakerDAO African Ambassador (2019–2021), Founder of[ DeFi Africa](https://x.com/defiafrica), and CEO of ZaaNet.

  - *Profile / References:*[ LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/sahabia-yakubu) |[ GitHub](https://github.com/sahadevgh) |[ X (Twitter)](https://x.com/sahadevgh)

**Track Record & Previous Deliverables:** The team has proven execution capability, having successfully built and shipped[ Buna Protocol V1.0 (Arbitrum)](https://www.bunaprotocol.com/) end-to-end, as well as developing decentralized infrastructure projects.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

- **Who Transacts:** Underbanked individuals, freelancers, and small merchants across West Africa (anchored through[ HackerBoost hubs in Ghana](https://www.hackerboost.org/)) seeking protection against local currency inflation.

- **Why & What Transactions:** Users transact to bridge external stablecoins or onboard fiat into Cardano-native stablecoins (USDCx/USDM) and allocate capital into Liqwid Earn yield vaults, or execute in-app swaps.

- **Cadence & Reach:** Users make weekly savings deposits, compound monthly yield, and manage liquidity routinely. We will reach these targets by embedding these workflows inside our familiar conversational Telegram bot interface, eliminating Web3 friction, and driving adoption via community onboarding workshops across HackerBoost hubs.

- **Target Justification:** Our declared target of **450 ADA in fees** (spanning approximately **5,000 transactions**) comfortably clears the program floor of **₳312** for our 150,000 ADA grant. It is ambitious yet realistic, grounded in our active regional developer community and designed to reflect organic, recurring transaction loops without artificial volume.

### How will you reach and onboard real users - and what evidence backs your channels?

**Buna Pilot Users:** Active savers using our Telegram bot and web app will be guided to migrate funds to native USDCx vaults through a zero-friction in-app campaign.

[**HackerBoost Hub**](https://www.hackerboost.org/) **(\~150):** Direct onboarding of university students, alumni, and freelance developers in Tamale.

Tamale Offline Hangout Community **(\~500):** Direct onboarding through established coworking spaces and tech meetups in Northern Ghana

**First Two Weeks Post-Launch Plan:**

**Days 1–3:** Deploy verified contracts to mainnet; update UI; publish declared footprint and explorer links

**Days 4–7:** Activate Cohort 1. Onboard the first 50 pilot savers for live USDCx deposits and Earn allocations

**Days 8–11:** Host workshops at HackerBoost hub, onboarding 40+ freelancers for P2P escrow and CEX-to-Cardano bridging

**Days 12–14:** Track transaction volume, gather feedback, deploy UX hotfixes, and publish adoption metrics

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/0uXZDd197hA?si=ofucyuccqFMf3H68

### Who else solves this today - competitors/alternatives, and why does your approach win?

**Existing Alternatives:**

- **CEXs & P2P (Binance P2P, Yellow Card):** Custodial, exposing users to account freeze risks and high KYC friction.

- **Cardano DeFi UIs (Liqwid, Minswap):** Built for power users; steep UTxO and slippage friction for retail savers.

- **Mobile Money:** Convenient for payments but offers zero yield against steep fiat inflation.

**Why Users Switch to Buna Bridge:**

- **Conversational UX:** Manage savings via a Telegram bot or web app with zero blockchain jargon.

- **Self-Custody:** Funds settle on-chain via user-signed transactions without exchange custody risk.

- **Stable Yield:** Earn sustainable USDCx yield via Liqwid pools without liquidation risks.

- **Direct Onboarding:** Connects CEX-held USDC to Cardano natively via Circle’s xReserve.

### Please provide details about the Technology Readiness Level selected for your existing product

Buna Protocol is an active, mature product currently undergoing live pilot testing with real-world users in production. Through our operational deployment, we have successfully validated core architecture components, including our conversational Telegram bot interface, peer-to-peer (P2P) transaction workflows, and a transparent, share-based savings accounting model.

The existing system has proven its reliability and user-facing utility under live market conditions, confirming that our platform mechanics effectively bridge the gap between underbanked users and digital asset savings. This established foundation provides a robust, tested framework upon which we are ready to expand.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Buna Protocol's proposed architecture adopts a hybrid on-chain/off-chain model designed to bring frictionless Web3 access to emerging markets:

- **Conversational Interface & Backend:** User interactions are handled via a Telegram bot and web interface powered by a secure backend, abstracting complex UTxO management and key handling away from retail users.

- **Onboarding via Circle xReserve:** The integration design utilizes Circle's xReserve infrastructure to bridge centralized exchange-held stablecoins directly into Cardano-native USDCx.

- **Yield Generation via Liqwid Finance:** Savings deposits will be programmatically routed into Liqwid Finance lending pools, utilizing our share-based accounting model to distribute decentralized yield.

- **DEX Liquidity & Swaps:** Planned in-app asset swaps between USDCx, USDM, and ADA are architected around Cardano DEX liquidity routers (such as Minswap).

**Why It Is the Right Fit:** This architecture is custom-built for underbanked West African users. By pairing high-performance off-chain chat workflows with Cardano DeFi primitives, our design removes barriers like seed-phrase friction while ensuring complete non-custodial security

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

**Our main** market includes retail savers, tech freelancers, and remote workers in Ghana and Sub-Saharan Africa (SSA) seeking inflation-proof, digital-dollar yields. Mobile money, with [23 million](https://www.bog.gov.gh/wp-content/uploads/2024/11/Summary-of-Economic-and-Financial-Data-November-2024.pdf) active accounts in Ghana as of August 2024, is the region's financial backbone. These accounts offer no yield against double-digit fiat inflation, prompting SSA to promote retail crypto adoption. Chainalysis reports [stablecoins account for 43%](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2024/) of crypto transactions in SSA as residents hedge currency devaluation. The demand for stable, yield-bearing digital dollars is substantial.

**Evidence of Demand & Product-Market Fit:**

- **Buna Protocol already serves real users on web and Telegram, validating demand for our** mobile-first savings UX.

- In pilot testing, users identified price volatility and multi-step DEX bridging as major barriers. Adding native Cardano stablecoins (USDCx/USDM) directly addresses this validated issue.

- USDCx quickly became Cardano's top stablecoin, with Liqwid Finance absorbing \~3M USDCx in its first week. On-chain liquidity exists; Buna offers the user interface to direct it to African retail savers.

- **Warm Pipeline:** We won't start from zero; we'll onboard \~200 Buna savers and \~150 freelancers from HackerBoost for mainnet adoption.

### Applicant name

Abubakari Mahamudu

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

**Revenue Model:** Buna Protocol operates a sustainable, transaction-based model. For peer-to-peer (P2P) escrow settlements and withdrawals to external exchanges, we apply a progressive fee tier ranging from 1% for small transactions down to 0.25% for high-volume transfers (above 20,000 GHS). For our Earn vaults, we charge a flat 1% fee on withdrawals.

**Who Pays?** External users (savers, freelancers, and remote workers) pay standard Cardano network fees directly from their non-custodial wallets. Buna never takes custody of funds, nor do we subsidize, reimburse, or pay transaction fees on users' behalf.

**Post-Pilot Continuity:** Usage persists beyond the grant window because personal saving, yield compounding, and P2P settlement are continuous financial habits. Once users hedge fiat against inflation using digital dollars, their deposits and withdrawals become recurring monthly routines rather than one-time promotional events.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This grant enables the building of Cardano integration for Buna Protocol, expanding into the ecosystem. Without it, users would be limited to Arbitrum and miss Cardano's liquidity, stablecoins, and yield.

**High-Level Fund Allocation:**

- **40% (60,000 ADA) - Core Integration & Smart Contracts:** Aiken vault contracts, share accounting logic, and Liqwid/Minswap SDK adapters

- **20% (30,000 ADA) - Security & Audits:** Third-party smart contract security review for safe mainnet deployment

- **20% (30,000 ADA) - Frontend & UX:** Telegram Mini App and web integration for CIP-30 signing and xReserve flows

- **10% (15,000 ADA) - Infrastructure & Indexing:** Cardano nodes, Kupo/Ogmios/Blockfrost services, and data pipelines

- **10% (15,000 ADA) - Deployment & Onboarding:** Pilot workshops

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- **Month 1 (Weeks 1–4): Core Smart Contract Architecture & SDK Setup**

  - *Deliverable:* Develop and test Aiken vault contracts for share-based savings accounting; integrate Liqwid Finance lending SDK and Circle xReserve bridging adapters for Cardano-native USDCx onboarding.

- **Month 2 (Weeks 5–8): Frontend, UX Wiring & DEX Swap Integration**

  - *Deliverable:* Update the Telegram Mini App and web interface to support CIP-30 wallet connectors, guided xReserve fiat-to-stablecoin flows, and Minswap DEX liquidity routers for in-app swaps.

- **Month 3 (Weeks 9–12): Security Audits, Mainnet Deployment & Demo Day**

  - *Deliverable:* Complete third-party smart contract security reviews, deploy final contracts and updated application logic to Cardano mainnet, finalize test evidence bundles, release documentation, and deliver the live Demo Day presentation to enter the M2 adoption window.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Buna Bridge is a conversational, mobile-first stablecoin integration that solves the critical financial challenges faced by everyday savers, freelancers, and remote workers across West Africa.

**The Problem**

These individuals face high inflation, fiat currency depreciation, and limited access to interest-bearing financial tools. While decentralized finance (DeFi) on Cardano offers robust infrastructure, it remains inaccessible to non-technical users who struggle with complex exchange interfaces, UTxO management, and seed-phrase maintenance. Traditional savings methods offer zero yield, leaving users vulnerable to economic instability.

**The Solution**

Buna Bridge acts as a simplified, intuitive gateway to the Cardano ecosystem. We are building three unified flows directly into our platform:

- **CEX-to-Cardano Onboarding:** Streamlined conversion of stablecoins from centralized exchanges onto Cardano as native USDCx

- **USDCx Earn Vaults:** Automated personal savings vaults that route deposits into Liqwid Finance lending pools, allowing users to generate stablecoin yield through a simple, share-based model

- **USDCx Swaps:** In-app, seamless stablecoin swaps across USDCx, USDM, and ADA, powered by Minswap liquidity

Buna Bridge simplifies blockchain access for underbanked African users, providing a seamless way to preserve digital dollars and earn decentralized yield. This enables them to protect savings and engage in global finance without needing technical expertise.

### Supporting links (repo, site, demo)

- https://bunaprotocol.com
- https://hackerboost.org
- https://t.me/buna_protocol_bot 
- https://github.com/hackerboost 

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

5000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

450

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

While Buna Protocol is in pilot testing, this specific Cardano integration is still in the conceptual and architectural planning stage (TRL 2). We have mapped out the system design to connect our conversational Telegram bot and interface to Cardano primitives (native USDCx onboarding via xReserve, Liqwid Earn vaults, and DEX swap (minswap) routing).

This grant will fund the hands-on engineering, smart contract wiring, testing, and deployment required to bring this integration from concept to a fully operational mainnet release.
