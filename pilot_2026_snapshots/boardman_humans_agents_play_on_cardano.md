# Boardman: Humans & Agents Play on Cardano

> CIP-0170 agent identity and USDM deposits, humans and AI agents play for real stakes, with Cardano as the identity and funding layer, Arc as settlement.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1uyymqdhp54p4xppkvrzsrukzkaaql53wkvgkdv8f707n8pgvwrfls`
- **Funding requested:** ₳60,000
- **Last finalized:** 2026-08-20T05:57:02.870000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

I built Boardman solo and it's live.\
\
WHAT I'VE SHIPPED ALONE:\
• Live gaming platform: agent arena, human matches, spectator betting, LP vaults, all with real USDC stakes and on-chain settlement\
• BoardmanEscrow smart contract V2 on Arc testnet (0xD8984396f12Cd0BD3C3e120858dd7eCdEeEF66Fc) with real dual-lock transactions on Arcscan\
• Full Stack: Python matchmaking engine, Solidity contracts, Next.js frontend, Telegram bot, Circle wallet integration, game registry, agent registry, spectator book, LP book\
• Game-agnostic architecture: chess today, football managers and other games next\
• Multi-chain design: Arc, Avalanche, Base, Stellar funding rails configured\
• Published builder docs, API protocol, sample agents, game submission pipeline\
• 1,400-line economy spec covering skill escrow, spectator pools, LP vaults, fee routing\
\
That's product, contracts, infra, docs, and operations, one person.\
\
WHAT I NEED (FUNDED BY THIS GRANT):\
• GTM strategist / user acquisition: drive agent creators AND human bettors to the platform\
• Marketing & community: tournaments, hackathons, content to onboard builders and players\
• Sales: partnerships with gaming communities, game studios, agent frameworks, and Cardano projects\
\
The platform is built. The grant funds the team to bring Cardano users into it.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

We pledge to return 10% of the grant (6,000 ADA) to the Cardano treasury once Boardman generates 250,000 ADA in cumulative on-chain fees on Cardano mainnet. This threshold is expected within 12 months post-pilot based on projected agent registrations, USDM deposits, and spectator activity. If the threshold is not reached within 18 months, no repayment is due.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

1\. Human players deposit USDM: players top up their Boardman play wallet from Cardano. Each deposit = 1 stablecoin tx. Target: 1,000 deposits from existing beta testers converting to mainnet plus new users from Lagos gaming communities. Average player deposits 3x per month. Friction removed: no PayPal or US accounts needed, just USDM on Cardano.

2\. Spectators and LPs operate programmable tokens: spectators place bets using compliance-gated tokens. LPs deposit and withdraw liquidity. Target: 650 token operations from spectators and LPs during tournaments, hackathons, and weekly Raja vs Nero events.

 3\. Agent creators mint identity attestations: each new agent registered on Boardman gets a CIP-0170 identity on Cardano. Target: 300 new agent registrations from hackathons, builder outreach, and Lagos gaming community. One-time cost per agent, permanent, verifiable.

 

CADENCE: Agent creators register once. Players deposit 3x/month. Spectators bet weekly during events. With 300 agents, 300 active players, and 100 spectators, 1,950 txs over a 1-month window is \~65 txs/day, achievable given our existing beta base and planned community outreach.

### How will you reach and onboard real users - and what evidence backs your channels?

We have testnet beta testers and a working product, not an established community. This grant funds the community build.

Skill-based betting happens informally in gaming chat rooms, WhatsApp groups, and local communities across Lagos. It's unregulated, unverifiable, and most platforms require PayPal or US accounts, excluding international users. Boardman solves this: play with USDM on Cardano, no bank account needed, on-chain settlement. We reach these communities through direct outreach to local gaming hubs, university chess clubs, and esports groups.

We also reach competition hosts, esports communities, and gaming Discord servers who run tournaments but lack trustless escrow. Boardman becomes their settlement layer. 

AGENT ECONOMY: We host hackathons, track one: design games agents can play, track two: design agents that play existing games. This creates a self-sustaining economy where builders create content, players compete, spectators bet, all generating Cardano network fees.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/0a51JtGlVrs

### Who else solves this today - competitors/alternatives, and why does your approach win?

1\. Prediction markets (Polymarket, Azuro): real-world event betting. We do skill contests with deterministic outcomes, PGN + SHA-256 digests, not oracle-dependent.\
\
2. Gaming platforms (Steam, casinos): centralized, no on-chain settlement. We're trustless escrow + public settlement on Arc testnet.\
\
3. AI agent frameworks (LangChain, CrewAI): help agents think. We're the economic layer where agents lock stakes, compete, and earn money.\
\
4. Generic identity (DIDs, ENS): human-focused. CIP-0170 identity for agents is novel: game IDs, wallet binding, PNL digest. Nobody else does this.\
\
Why we win: we already have the live product, on-chain proof (0xD898...), and multi-chain architecture. The grant funds a Cardano integration, not a new product from scratch.

### Please provide details about the Technology Readiness Level selected for your existing product

Boardman is live on Arc testnet (chain ID 5042002). Evidence: 17 matches played, 8 settled, $350+ USDC volume on-chain. Smart contracts deployed: BoardmanEscrow V2 (0xD8984396f12Cd0BD3C3e120858dd7eCdEeEF66Fc), SpectatorPool, ClawEscrow. Live arena at [boardman.playingsidequest.fun](http://boardman.playingsidequest.fun), Telegram bot @myboardmanOfficialBot, AI agents (Raja, Nero) competing 24/7. Multi-chain architecture: Arc primary, Stellar and Avalanche testnets configured. Spectator betting pools and LP positions active. Every match settles via smart contract with verifiable tx hashes on Arcscan.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Boardman uses a multi-chain architecture where Arc is the settlement hub and Cardano is the identity and funding layer. CIP-0170 attestations are signed metadata records (label 674) anchored on Cardano mainnet. Each attestation contains: agent name, game IDs, Arc wallet address, rolling PNL digest, and issuer signature. We use Blockfrost for chain interaction and the Cardano serialization library for transaction building. Attestations are permanent, once minted, they exist forever on Cardano.

 

The USDM deposit rail mirrors our existing Stellar and Avalanche rails. Users fund their Boardman play wallet from USDM on Cardano. We facilitate the bridging: USDM on Cardano is locked, USDC is released on Arc to the user's play balance. This creates Cardano network fees on every top-up.

Both integrations follow proven patterns. The architecture is: Cardano for identity + funding, Arc for settlement, Boardman platform for matchmaking and game logic. This separation means Cardano handles trust and access, while Arc handles speed and cost. Neither chain bears the full load.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins
- On-chain identity (CIP-0170)
- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Our target market is anyone who wants to play, bet on, or fund competitive games, humans and AI agents alike.

TWO USER SEGMENTS:
1\. Human bettors and players: people who want to challenge friends, bet on agent matches, or LP an agent's bankroll. Our Telegram community and arena visitors are already doing this on Arc testnet. Cardano users can now join by topping up with USDM.

2\. Agent creators and operators: developers building autonomous agents that compete for real stakes. They need portable identity (CIP-0170) so third parties can trust their agent's track record. They need USDM as a native currency if their agent runs on Cardano.

EVIDENCE OF DEMAND:
\- Live 24/7 arena: Raja vs Nero chess, auto-playing with real USDC stakes
\- Human matches via Telegram bot: challenge, lock, play, settle
\- Spectator betting on agent outcomes (pari-mutuel pools)
\- LP positions earning profit share from agent wins
\- Public PNL page showing every match, every winner (boardman.playingsidequest.fun/agentic/metrics.html)
\- Real dual-lock transactions on Arcscan (0xD8984396f12Cd0BD3C3e120858dd7eCdEeEF66Fc)
\- Builder documentation and API for third-party agent registration

Market size: The AI agent economy is nascent but growing fast. OpenAI, Anthropic, and Google are deploying agents that need identity and payment rails. Cardano's stablecoin ecosystem (USDM, USDCx) is maturing. Boardman connects both, agents that can be trusted, funded, and watched.

### Applicant name

Olanrewaju Animashaun

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

REVENUE MODEL (sustains after pilot)

1. Platform fee: 7% of every skill pot. Every human vs human match generates revenue.
2. Agent match fee: 7% of every agent skill pot, revenue scales with agent count.
3. Spectator pool fee: 7% of every spectator pot. Every bet on an agent match generates revenue.
4. LP management: Boardman takes a share of LP profit spread. Grows as TVL grows.\
   \
   WHY USAGE CONTINUES AFTER THE GRANT:

- The arena runs 24/7 autonomously. Matches settle without human intervention. Revenue scales with agent count and stake size, not grant funding.
- Identity attestations are permanent: once minted on Cardano, they exist forever. New agents generate new identity txs automatically
- The USDM deposit rail creates ongoing Cardano network fees. Every user top-up is a Cardano tx
- The grant is the enabler, not the business. We have a live product generating testnet volume. Mainnet revenue follows.
- Top performers earn up to 50% bonus. Our targets are conservative.

### Programmable tokens (CIP-0113) - expected transaction count

650

### On-chain identity (CIP-0170) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The grant funds three things that wouldn't happen otherwise:

 1\. Mainnet deployment: we migrate CIP-0170 attestations and USDM rail from testnet to mainnet. This requires contract redeployment, security review, and Dune tagging for Catalyst dashboard visibility.

2\. Team hires: we're currently solo. The grant funds a GTM strategist, and marketing to build the community from beta testers to real users.

3\. Community and hackathons: we run agent hackathons and gaming tournaments to onboard builders and players. Without the grant, we stay on testnet with beta testers. With it, we go live on mainnet with real users generating real Cardano network fees.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

MILESTONE 1A: CIP-0170 Identity (Week 1-4)

• Deploy identity minting on Cardano mainnet

• Mint Raja and Nero identities on mainnet (done)

• Integrate into agent registration flow

• Deliverable: mainnet tx hashes on explorer

 

MILESTONE 1B: USDM Deposit Rail (Week 5-8)

• Implement USDM deposit handler on mainnet

• Bridge: USDM locked on Cardano, USDC released on Arc

• Test end-to-end deposit flow

• Deliverable: first real user deposit with explorer link

 

MILESTONE 1C: CIP-0113 Tokens (Week 9-10)

• Deploy spectator receipts on Cardano mainnet

• Deploy LP position tokens on mainnet

• Integrate into spectator pool and LP vault contracts

• Deliverable: first CIP-0113 token operation on mainnet

 

MILESTONE 1D: Launch (Week 11-12)

• End-to-end testing, Catalyst label tagging

• Demo Day: live mainnet demo with explorer links

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Programmable tokens (CIP-0113) - fee target (ADA)

117

### On-chain identity (CIP-0170) - fee target (ADA)

60

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Boardman is a live gaming platform where humans and AI agents play for real stakes. Spectators bet on outcomes, LPs back agents' bankrolls, and every dollar is settled on-chain.\
\
THE PLATFORM:\\

1. HUMAN vs HUMAN: Challenge a friend, lock USDC, play, winner paid automatically. Live on Telegram + web.\\
2. AGENT vs AGENT: AI agents compete 24/7. Raja vs Nero chess is live now. Anyone can watch the arena.\\
3. SPECTATOR BETTING: Pick who wins. Pari-mutuel pool held by smart contract. Winners split the pot.\\
4. LIQUIDITY PROVISION: Back an agent's bankroll, share in their profits as they win.\
   \
   THE PROBLEM ON CARDANO:\
   Two things are missing for Cardano-native participation:\
   A) PORTABLE AGENT IDENTITY: AI agents need verifiable on-chain identity proving who they are, what they play, and how they've performed. Today that's a JSON file on our server. Third parties cannot trust it.\
   \
   B) STABLECOIN ENTRY POINT: No way to fund play from Cardano stablecoins without bridging elsewhere. Agents on Cardano need USDM as native currency. Humans on Cardano want to top up and play.\
   \
   WHAT WE WILL BUILD:\\
5. CIP-0170 identity for every agent: signed attestation on Cardano mainnet: name, game IDs, wallet, PNL digest. Portable. Verifiable.\
   \\
6. USDM deposit rail: humans top up with USDM, agents use USDM as currency. We bridge: USDM on Cardano → Arc play balance.\
   \\
7. Dune label: all Cardano txs tagged for the Catalyst dashboard.

### Supporting links (repo, site, demo)

- https://boardman.playingsidequest.fun
- https://github.com/0xkenichi/boardman
- https://drive.google.com/drive/folders/16ZSpWB1dRimPSHuxH_yPtudq8YKWMzfN?usp=drive_link

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

200

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

CIP-0170 identity is at TRL 6 on Cardano Preview testnet. We have already minted identity attestations for both agents: Raja (tx: 8137034986b8979c3762c9de50fd64839a43d5e1d794cb0b296b0419af28d975) and Nero (tx: 510a5d59272788cddce3ebdbbb822f2dc49b42bb0542089ca1630e9ac83bd078). Both contain CIP-0170 metadata (label 674) with agent name, type, platform, Arc wallet, performance, and issuer attestation. USDM deposit rail is at TRL 3, architecture designed, same pattern as existing Stellar/Avalanche rails. The grant carries both from testnet to mainnet.
