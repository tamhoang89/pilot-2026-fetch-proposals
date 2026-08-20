# KOLO Hub: Cardano Stablecoin Credit Layer for AI Tools/Agent

> Enable KOLO  Hub users and AI agents to pay for mini-apps and APIs using verified Cardano stablecoins.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 11
- **Proposer:** `stake1u8r837mdv93allvtghm2wvg9skrhhth3rcvk3mfs2af3v7qw4qrh6`
- **Funding requested:** ₳100,000
- **Last finalized:** 2026-08-20T04:39:44.286000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

The BBO team combines Cardano ecosystem experience, infrastructure operations, full-stack development, system administration, community building, and multimedia communications.\
**\
Do Duc Chau** is a Project Manager and Head of Cardano Integration Team. He has experience in blockchain, programming, data analysis, and application development. He has many years of experience with Cardano infrastructure. He is also the founder of Cardano ECO Talk / Tre Viet - a community of over 800 people dedicated to learning about the Cardano ecosystem.\
[Linkedin](https://www.linkedin.com/in/chau-do-duc-68523099/)\
\
**Chu Cao Bang** is System Administrator. He has experience in data analytics, IT infrastructure, VPS/Linux operations, blockchain and AI node operations, Midnight node, Cardano SPO, db-sync, N8N automation, and finance-industry data management.\
[Linkedin](https://www.linkedin.com/in/cao-b%E1%BA%B1ng-3472722b6/)\
\
**Nguyen Hoang Khai** is a full-stack developer with many years of experience in backend/frontend development, including APIs, system architecture, databases, performance, security, web applications, project management, and AI/automation-related work.\
[Linkedin](https://www.linkedin.com/in/khai-hoang-nguyen-ba5a9b224/)\
\
**Nguyen Duy Hoang** is a multimedia communications specialist, proficient in content creation, production, and social media management.\
[Linkedin](https://www.linkedin.com/in/duy-hoang-nguyen-089324350/)

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

KOLO does not rely on speculation or random transactions, but on existing user demand for digital services. During the 3-month build phase before launch, KOLO will run a “Build in Public” strategy by sharing product progress, feature demos, development stories, community feedback, and real use cases. This helps us avoid launching from zero by building an early audience that understands the product and is ready to test it.\
\
The hypothesis is that Build in Public can attract around 5,000 interested people in 3 months across X, TikTok, and Threads. If 10% convert into real users, KOLO will have its first 500 users. Assuming each user makes an average of 2 USDCx top-up transactions per month, this group can generate 1,000 transactions/month. In addition, KOLO  expects 50 AI Agents/DEVs to use the credit/API layer. If each Agent/DEV makes 4 USDCx top-up transactions per month, this adds 200 transactions/month.\
\
In a downside case, if Build in Public grows slowly, KOLO can still leverage the Cardano ECO Talk community of 800+ people and reach several thousand university students through our advisory role in the digital economy board.

### How will you reach and onboard real users - and what evidence backs your channels?

User Acquisition Strategy

1. Our Cardano ECO Talk community (800+):

- Early adopters matching our profile — already have wallets, familiar with stablecoins.
- Invited to an alpha trial: free credits, feature feedback.
- Expected 5–10% conversion in month one, with high response as the community already trusts the team.

2. University students: the project lead sits on a university's digital economy advisory board, enabling direct access to students via hands-on tool workshops. Students use tools daily and spread the word fast on campus. Target: 200–500 sign-ups in the first semester.
3. Build-in-public on X, TikTok, Threads: sharing the dev journey (design, metrics, pivots) to build trust and attract curious users.

- X: crypto/developer community — where AI Agent operators and crypto users gather.
- TikTok: short demo videos, easy to go viral among younger users.
- Threads: daily updates and conversations with followers. Each post is an acquisition channel.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/R9ADLwoYYNw

### Who else solves this today - competitors/alternatives, and why does your approach win?

Four models today, each addressing only half of the problem:

- Subscription suites (Canva, Adobe, Notion, Setapp): expensive, card-based, no crypto.
- Single freemium tools (TinyPNG, iLovePDF,Remove) fragmented, separate accounts.
- Agent payment infrastructure (Skyfire, Payman, x402): payment only, no tools for humans.
- API marketplaces (RapidAPI, Replicate): card signup, few everyday tools.\
  \
  KOLO  is superior because:
- Both sides: tool app for humans + credit/API layer for agents.
- Pay-per-use USDCx: low fees, wallet-based — vs pricey subscriptions.
- Agent-ready: tools can be called programmatically; agents are free to use them within a limited budget and pay per call.
- Early mover in serving AI Agents — right as giants like Cloudflare and Amazon prepare to enter.

### Please provide details about the Technology Readiness Level selected for your existing product

KOLO now has a working prototype in a sandbox environment, going beyond just a conceptual description. The test includes a user dashboard and several digital applications accessible directly via a demo URL - <https://bboapp.xyz/>\
\
Users can log in/connect their wallet, open the dashboard, select digital applications, and test basic workflows. These steps demonstrate that the core components of the product are operational in the relevant environment, even though it's not yet a complete mainnet version.\
\
KOLO meets TRL 5: the technology has been validated at the prototype level in a suitable testing environment, has an observable product, and has a sufficiently clear technical foundation to move on to the real-world deployment phase.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

KOLO 's on-chain architecture utilizes USDCx on the Cardano mainnet via smart contracts/escrow scripts, combined with an off-chain indexer and internal credit ledger. Users or AI agents/developers create credit deposit requests, then send USDCx to the KOLO escrow address along with metadata/message tags to identify the transaction.\
\
The off-chain indexer monitors the escrow address, verifies the USDCx policy ID/token name, the number of tokens, the sending/receiving address, the transaction hash, the metadata/message tag, and the confirmation status. Once a valid transaction is confirmed, the system writes the transaction hash to the credit ledger, adds credit to the user or balances the AI ​​agent/developer, while also preventing duplicate entries.\
\
Smart contracts/escrow scripts are suitable because they separate the user's stablecoin from the operating wallet, increasing transparency, supporting invoice reconciliation, and allowing refunds if the transaction has an incorrect invoice, incorrect amount, or mismatched metadata. After topping up, users use the credit for subscriptions, digital applications, or APIs; AI Agents/Developers call APIs using the prepaid balance, without needing to create on-chain transactions for each call.\
\
All proof will be verified via escrow address, policy ID, transaction hash, and link explorer on the Cardano mainnet.

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

**KOLO serves two primary target markets on a crypto payment infrastructure:**

1. Users of digital services — office workers, freelancers, content creators.

- Globally, 741 million people owned cryptocurrency in 2025, \~9% of the world's population.
- Stablecoins have become a real payment infrastructure: transaction volume surpassed USD 4 trillion in 2025.
- PMF: KOLO builds a real, practical application that gives cryptocurrency users an additional payment option — bringing small tools together in one place, payable with stablecoins via a Cardano wallet (USDCx), replacing cards, fragmented subscriptions, manual payments, and high fees.

2. AI Agents — agents that search for data, gather information, and call APIs.

- 53% of web traffic in 2025 came from bots/AI Agent; humans dropped to 47%.
- AI agent traffic grew \~8,000% in a single year.
- Agents are the dominant API callers: 70% of API commands come from agents (Stripe).
- According to Gartner, 40% of enterprise applications will integrate AI agents by 2026.
- PMF: the web is still designed for humans — logins, cards, manual API keys — making it hard for agents to discover and pay on their own. KOLO opens a credit/API layer: your AI agent runs a command on your machine — tops up USDCx to a Cardano wallet address — and the AI agent automatically experiments with and discovers language models, applications, and API requests, paying per use from a prepaid stablecoin balance.

### Applicant name

Duc Chau Do

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Who pays — 2 customer groups:

- End users: purchase points, subscribe to membership packages, activate each mini-app; only pay for actual needs.
- AI Agent operators: pay per API request from pre-loaded stablecoin balance; programmable call utility, agents freely explore and use according to tasks.\
  Revenue sources:
- Fees from users/API calls.
- Customized packages for businesses.
- Commissions from third-party tool developers.
- Selective advertising for service providers suitable for users.
- Referral commissions for hosting services to individuals and businesses.\
  \
  Maintaining after funding:
- Break-even on a small scale: just 200-1000 active users per month is enough to cover maintenance and operating costs.
- Upfront payment: Customers deposit before use → positive cash flow early, not dependent on funding.
- Repeated demand: Tools used daily, agents make API calls continuously → recurring revenue.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The three largest cost components are:

- Developing over 20 digital applications and APIs, requiring approximately 50,000 ADA for design, backend, APIs, dashboards, and QA.
- Initial infrastructure and AI model fees, around 25,000 ADA for servers, databases, nodes/indexers, monitoring, logging, and AI model call costs.
- Public build-in media over 3 + 1 + 2 (6 months), approximately 25,000 ADA to produce over 240 posts per platform, demos, tutorial videos, documentation, and onboarding.\
  \
  Without funding, KOLO will struggle to publish over 20 applications on schedule, limit user onboarding, and fail to reach its goal of 1,000 stablecoin transactions, corresponding to 300 ADA in fees, within the program's timeframe.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Published over 20 digital applications: each application has a URL/endpoint, a functional description, and can be used with credits/API.\
USDCx payment gateway on Cardano mainnet: users can connect wallets, deposit USDCx, the system confirms transactions, and credits are added. Proof includes transaction hash, link explorer, and repeatable end-to-end flow.\
Tool for AI Agent/DEV: AI Agents run a command to integrate with the tool, deposit USDCx into prepaid balances, call the API, and have credits deducted based on usage. Proof includes the tool set, API logs and deposit transaction hash.\
On-chain reconciliation system: a service that monitors Cardano mainnet, verifies policy ID/token name, sender/receiver address, token quantity, confirmation, and prevents duplicate transaction hash recording.\
Build in public: Deploy content regularly on X/TikTok/Threads, demonstrate progress, gather feedback, and build a list of interested users before launching.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

KOLO Hub is a digital toolbox for modern users—a collection of compact, easy-to-use tools that can be quickly accessed directly in your browser, helping users efficiently handle daily needs in learning, office work, communication, content creation, and digital life. It also integrates AI-powered tools for automation, suggestion, analysis, and smarter content creation, along with an open API system that allows AI agents and external applications to easily call, connect, and utilize KOLO tools as flexible digital capabilities across various workflows.\
\
Currently, users needing everyday small digital services—for learning, office work, communication, and digital living—are faced with fragmented tools, separate subscription packages, manual payment processes, and limited cryptocurrency payment options. With AI agents, the problem lies in payments: they are almost exclusively payable via Visa/Mastercard — with high fees and slow authentication (3D Secure, OTP) — and lack a true cryptocurrency channel. As a result, agent-per-use payments are expensive, slow, and subject to interruptions whenever human verification is required.\
\
This proposal adds USDCx on Cardano as a way to purchase usage credits in the KOLO system. Users connect their own self-custodied Cardano wallet to buy credits or a subscription; KOLO holds no crypto-asset balance for users. AI agents use the credit/API layer with pre-purchased allowance — no international credit card, no waiting on manual verification.

### Supporting links (repo, site, demo)

- https://bboapp.xyz/
- https://t.me/Cardano_ECO_VN
- https://pay.bboapp.xyz/

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

1000

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

300

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

KOLO's Cardano stablecoin integration is at TRL 2: we have tested proof-of-concept components, but not yet a full mainnet flow.\
\
Completed work includes Cardano wallet connection, a stablecoin credit top-up UI. Tests were done in an internal sandbox and partly on Cardano testnet/preprod. Current evidence is a UI/prototype demo of the basic top-up flow.\
\
The grant will fund the USDCx mainnet payment gateway, script escrow, duplicate-safe credit ledger, and refund flow. The goal is mainnet readiness: real users can top up USDCx, receive credit, and verify payments via transaction hash, policy ID, escrow address, and explorer links.\
link check payment :
