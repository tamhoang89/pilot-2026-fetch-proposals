# Wargrum: Scaling a Launched Cardano TCG to Mass Adoption

> Wargrum is live on Cardano mainnet with card payments and managed wallets. This proposal funds tournaments, player trading, and the GRUM economy to turn our launch into sustained on-chain activity.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 18
- **Proposer:** `stake1u9cu08wj5rwd9d0vjakf0qv8mc46zzqlkft4s8k20sl0l0qvng7uy`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-16T01:56:38.645000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

Wargrum is built by a team that already shipped the product this proposal extends. Eli Skenandore, applicant, lead designer and product architect (https://www.linkedin.com/in/eli-skenandore/), built large-scale gaming platforms including the architecture for NFL Fantasy Football 2.0, and designed the systems now in production: the real-time multiplayer game, the provably fair pack engine, managed wallet onboarding, the marketplace, and the fiat payment rail. Jason Appleton, Crypto Crow, community and growth (https://www.youtube.com/@CryptoCrowOfficial), has been a Cardano educator since 2017 with a large audience across YouTube and X. JP Steinmetz, technical director (https://www.linkedin.com/in/jeanphilippesteinmetz/), is a veteran game developer with shipped credits on XCOM 2, The Evil Within, Lost Planet 3, and Hawken. Crypto Face, economic design and outreach (https://www.youtube.com/@CryptoFace), supports the GRUM token model. The extended team includes contract artists, blockchain engineers, and testers.

The strongest evidence of capability is the live product: [play.wargrum.io](https://play.wargrum.io) runs today on Cardano mainnet with real payments, real NFTs, and real players, launched without grant funding. No additional hires are needed for the pilot scope; funding expands content, tournaments, and growth within the existing team.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Wargrum meets its declared pilot fee target, we pledge to return 10 percent of the grant to the Cardano treasury within 12 months of the pilot's end, funded from marketplace revenue. If cumulative fees reach five times the target within 24 months, we will return a further 10 percent. Both thresholds are measurable on-chain.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Wargrum generates transactions from ordinary play, not incentivized clicking. Who transacts: players. Why: they buy packs (each purchase mints NFTs), earn GRUM in ranked matches and tournaments, spend GRUM on packs and entries, trade cards in the Bazaar, and withdraw assets to self-custody. How often: buying and trading are weekly habits for TCG players, and set releases plus weekend tournaments create recurring spikes.

Path to target: the pilot goal is tens of thousands of registered players with a paying core in the thousands. Pack purchases mint on-chain; one box mints 54 cards. GRUM settlement writes rewards and spends on-chain. Trades settle per transaction. Two hundred thousand transactions over the pilot is roughly 550 per day, a few hundred active players transacting twice a day, within what one strong tournament weekend produces in a healthy TCG.

The fee target follows from the count at current average network fees. Both targets sit far above the floor because a consumer game either produces real volume or it has failed. All activity is organic play under the Transaction Integrity Standard: no wash trading, no self-dealing, no empty transactions.

### How will you reach and onboard real users - and what evidence backs your channels?

Our channels already produce users. Jason Appleton (Crypto Crow) has been a Cardano educator since 2017 with a large audience across YouTube and X, and every announcement drives signups. Phaser, the engine behind the game, featured Wargrum to its web game developer audience, bringing players from outside crypto. Cardano NFT communities, marketplace listings, and the Catalyst community itself round out the crypto-native reach.

The fiat rail unlocks mainstream channels closed to wallet-first games: TCG creators on YouTube and Twitch, Reddit card game communities, web game portals, and paid social with direct signup-to-purchase attribution, since a new player needs only an email and a debit card. Onboarding is the proof: signup to first pack opening takes under five minutes with no seed phrase. Tournaments with prize pools give creators a story every week, and each set release is a marketing moment with published print runs and verifiable odds.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=yDkd3sgZNUk

### Who else solves this today - competitors/alternatives, and why does your approach win?

Off-chain, the alternatives are Hearthstone, Magic Arena, and Marvel Snap: polished, huge audiences, but players own nothing and cards vanish if the publisher pulls the plug. On-chain, Cardano and other ecosystems have NFT card collections with thin gameplay, and most Web3 card games demand a wallet extension and crypto before the first match, which kills conversion.

Wargrum wins on the combination: real competitive gameplay in the browser, true NFT ownership, and Web2-grade onboarding. Email signup, Apple Pay, first pack in five minutes. No other Cardano game offers that today. Provably fair pack odds, committed and revealed per pull, also beat the black-box odds of traditional TCGs. Collections here carry resale value, so trying Wargrum costs a player nothing.

### Please provide details about the Technology Readiness Level selected for your existing product

Wargrum is live in production at [play.wargrum.io](https://play.wargrum.io) on Cardano mainnet. Real users play real-time multiplayer matches, sign up with email, receive managed Cardano wallets, and buy booster packs with ADA or by card through Stripe with Apple Pay and Google Pay. Our first edition NFT collection is minted on mainnet with published print runs, a provably fair pull engine commits and reveals a server seed for every pack, and the in-game Bazaar marketplace shows live supply per card. The platform includes payment reconciliation, refund backstops for edge cases, automated ownership verification against on-chain state, and multi-chain support with Solana. This is an operating product with paying customers, not a prototype: TRL 9.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Wargrum runs a proven hybrid architecture. Gameplay is off-chain for speed: a browser client built on Phaser talks to a real-time multiplayer backend, so matches feel like a modern card game. Value is on-chain for trust: cards are Cardano native assets, ownership is verified against on-chain state through indexer queries, and a reconciliation loop continuously repairs any drift between game state and chain state. Payments flow through custodial wallets so mainstream players never touch key management: ADA debits settle on mainnet, Stripe card payments trigger the same mint pipeline, and every order uses idempotent exactly-once semantics with automatic refunds for unfulfillable payments.

This is the right fit for CIP-0113 programmable tokens. GRUM needs exactly what the platform already provides: managed wallets to hold balances for non-crypto users, a live economy with natural earn and spend loops, and battle-tested minting and reconciliation infrastructure. The programmable token standard gives us on-chain enforcement of reward rules and transfer logic, while our custody layer makes the token invisible by default for mainstream players and fully self-custodial for players who withdraw to their own wallets. The architecture has already survived production. The same rails will carry GRUM.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Our target market is trading card game players, a mainstream audience that already spends heavily on digital cards. Hearthstone, Marvel Snap, and Magic Arena have shown that tens of millions of players will pay for digital packs, and the physical TCG market exceeds 6 billion USD a year. Wargrum targets the slice of that audience that wants real ownership: players tired of buying cards locked inside a publisher's account.

Evidence of demand: Wargrum is not a concept. The game is live at [play.wargrum.io](https://play.wargrum.io) with real-time multiplayer, a full starter set, mainnet Cardano purchases, and card purchases through Stripe at 8.99 USD per booster. Our first edition collection is minted on Cardano with published print runs shown in the in-game Bazaar. The project has a community built since 2022 through Jason Appleton's Cardano audience, a waitlist and Discord grown across multiple public teasers, and third-party coverage including a feature by Phaser, the engine that powers the game.

The commercially significant fact: a card payment plus a managed wallet means our addressable market is every TCG player with a debit card, not the small subset who already hold ADA.

### Applicant name

Eli Skenandore

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Wargrum earns revenue directly from players: booster packs and boxes at 8.99 USD per pack or 55 ADA, paid in ADA or by card through Stripe, plus marketplace fees on player-to-player trades and tournament entry fees. This is the proven TCG model that has run profitably for decades, with the chain adding resale value and provable scarcity that digital TCGs cannot match.

It keeps running after the pilot because players pay for fun, not subsidies: packs are exciting to open, cards are needed to compete, and collections hold value. Set releases create recurring revenue waves, seasons create recurring engagement, and every trade pays a fee. Operations are already funded by sales and the founders. Pilot funding accelerates the flywheel with content, tournament prize pools, and user acquisition. The goal by pilot end: organic player activity generates network fees and sales that exceed infrastructure costs, making Wargrum a permanently self-sustaining source of Cardano usage.

### Programmable tokens (CIP-0113) - expected transaction count

200000

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, the GRUM economy, tournaments, and player trading wait behind revenue growth, likely a year or more, and the launch window closes quietly. The pilot pulls the work forward and funds the push that fills it with players.

Spend: 50 percent marketing and user acquisition, because a live consumer game converts spend directly into adoption: TCG creators on YouTube and Twitch, paid social with signup-to-purchase attribution, launch campaigns, and tournament prize pools. 30 percent engineering: GRUM as a CIP-0113 token with earn and spend sinks, tournament infrastructure, and marketplace trading. 15 percent content: the next card set and seasonal events. 5 percent security review. Every line converts into on-chain activity: mints, trades, token transactions, network fees.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

M1 delivers the GRUM programmable token live on Cardano mainnet, integrated into the already launched game at play.wargrum.io. Deliverables in the 3-month window:

GRUM implemented per CIP-0113 and deployed to mainnet with published minting policy and transfer logic.

Earn loop live: ranked match rewards and daily missions credit GRUM to player managed wallets with on-chain settlement.

Spend loop live: booster packs and tournament entries purchasable with GRUM in production.

First tournament with GRUM entry and prize payout, producing verifiable mainnet transactions from real players.

Withdrawals: players can move GRUM and card NFTs to self-custody wallets.

Public page listing our on-chain identifiers (policy IDs, script hashes, team wallets) for independent verification.

Demo Day: a real player earns GRUM in a match, spends it on a pack, opens the pack, and the transactions appear on a mainnet explorer.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

34000

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Wargrum is a competitive trading card game that runs in the browser at [play.wargrum.io](http://play.wargrum.io), and it is live on Cardano mainnet today. Players build decks, battle in real time, and own their cards as Cardano NFTs. A new player signs up with an email, gets a managed Cardano wallet automatically, and buys booster packs with ADA or with a regular debit card through fiat, including Apple Pay and Google Pay, at 8.99 USD per pack. Every pack pull is provably fair with a server seed committed before the draw, and every card is minted as a real NFT the player owns.

The problem: Cardano has very few consumer products that a person with no crypto experience can use in their first five minutes. Wallet extensions, seed phrases, and acquiring ADA filter out nearly everyone before they start. Games are the proven wedge for consumer adoption, but Web3 games usually offer speculation without gameplay or gameplay without real ownership.

Wargrum removes the onboarding wall completely. Someone who has never touched crypto can open a pack of on-chain cards within minutes of clicking a link, while Cardano handles ownership, scarcity, and trading underneath. This proposal funds the next phase of the launched product: tournaments and seasons, player-to-player trading, the GRUM reward economy, and growth to bring tens of thousands of players through this pipeline.

### Supporting links (repo, site, demo)

- https://play.wargrum.io
- https://www.wargrum.io
- https://phaser.io/news/2025/11/wargrum
- https://www.youtube.com/watch?v=yDkd3sgZNUk

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

### Funder, status, and what it covers

*Funder: Project Catalyst, Fund15, Cardano Use Cases: Prototype and Launch category. Status: applied, pending vote. Proposal: WARGRUM - Play-to-Earn NFT Trading Card Game on Cardano, 200,000 ADA requested. What it covers: the broader 12-month game roadmap, including a public beta, a full 240-card set with audits, the Land Wars land NFT system, and version 1.0 launch. What this pilot would fund instead: a tightly scoped CIP-0113 integration (the GRUM token live on mainnet with earn and spend loops), tournaments, and player-to-player trading. If both were approved, we would carve the overlapping GRUM scope out of the Fund15 work plan before accepting funds, so no deliverable is funded twice.*

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The GRUM programmable token economy is at the design stage. The token model was developed for our Fund15 proposal: earn through ranked play, daily missions, and tournaments; spend on packs, tournament entries, crafting, and cosmetics. What exists today is everything the token plugs into: the live game loop, the managed wallet layer that will custody GRUM for mainstream players, the marketplace where GRUM becomes a settlement option, and the pack engine that will accept GRUM as payment. No CIP-0113 code has been written yet, which is exactly the work this pilot funds: implementing GRUM as a programmable token, wiring earn and spend sinks into the live game, and shipping it to our existing player base.
