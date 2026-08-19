# L-ADA: Deeper Stablecoin DEX Liquidity on Cardano

> Pairing stablecoins with a yield-bearing asset that never stops staking, so liquidity gets deeper and swaps get tighter.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 12
- **Proposer:** `stake1uy7j4j6t0nuzpkz54ur4y22qu56m74kllajv7ce7elsxzlcsrnq0x`
- **Funding requested:** ₳115,000
- **Last finalized:** 2026-08-19T17:21:02.210000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

I (Nick) bring direct experience turning tokens into usable DeFi assets. At AlphaGrowth, I worked with clients to give their tokens real utility across DeFi, essentially the same problem Lava is solving now, just applied to staked ADA instead of a single project's token. Some of these clients include King Protocol, Compound Finance, and Rocketpool.

The rest of the team fills in what Lava needs to actually ship and scale. FluidLabs is the development partner, with Matteo and Raul leading smart contract engineering and protocol infrastructure. Nesso handles marketing, growth, and business development, with Lorenzo directing go-to-market strategy and a dedicated BD lead, Imrahn, focused specifically on partnerships. Security is covered by UTXO Company, an independent auditor, with the core audit already complete.

All of us together maps exactly what the business actually requires: someone like myself who's done token-to-DeFi integration work before leading the vision, experienced smart contract engineers building the product, and a BD-focused team executing the distribution strategy that's already landed real pre-launch integrations.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

L-ADA/stablecoin pair usage comes from three recurring flows. \
\
(1) DEX LPs and arbitrageurs on L-ADA/USDM or L-ADA/USDCx pools rebalance whenever the redemption rate or ADA price drifts - arbitrage runs several times daily to keep pools priced correctly. \
\
(2) FluidTokens or Surf borrowers post L-ADA as collateral to draw USDM/USDCx, generating deposit/borrow/repay cycles roughly weekly per active user. \
\
(3) Lava's own mint/redeem flow adds a steady baseline: every stablecoin-funded entry or exit through the protocol (mint L-ADA, later redeem for ADA) generates a transaction independent of DeFi activity elsewhere.

Our 300 ADA fee target implies \~1,000 transactions across the window - roughly 33 tx/day at Cardano's \~0.33 ADA average fee. This is deliberately conservative relative to our Day-1 integration partners (Surf, Atrium, FluidTokens, Pulse, Atlas). No paid incentives are used (never counted, per Catalyst §12); all activity comes from organic collateral, LP, and mint/redeem flows.

### How will you reach and onboard real users - and what evidence backs your channels?

Lava's onboarding strategy meets ADA holders where they already are: ADA holders sitting on idle capital that want to earn more yield. The ask is simple, convert already staked ADA into L-ADA, keeping the yield the whole time.

The main channel is distribution through alraedy existing Cardano DeFi protocols. We have locked in day-one integrations across lending, yield splitting, and staking (FluidTokens, Surf, Atlas, Atrium) before launch, with more in build or under LOI (Gravity + Palm). Users encounter L-ADA naturally through platforms they already use, rather than needing to discover Lava on its own.

On top of that, a seasons-based points program rewards real L-ADA usage across partner protocols, not just activity on Lava itself, giving users a reason to move early and stay active as new integrations go live.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/I21DR2UeZ_o

### Who else solves this today - competitors/alternatives, and why does your approach win?

The closest alternative is Optim (OADA/SOADA), which takes a similar approach but only partially preserves staking exposure and has basically no core DeFi integrations. Optim is also not very active. Beyond that, the real competitor is the status quo, where holders just have to choose between staking rewards and DeFi.

L-ADA wins by fully preserving staking exposure, launching with real integrations already locked in across lending, DEXs, and yield markets, and not requiring a token to work. It's a more complete solution than the partial alternatives, and it's live on tes with distribution rather than just promising it.

### Please provide details about the Technology Readiness Level selected for your existing product

L-ADA is at TRL 6. The core protocol (staking, minting, and redemption logic) has completed a full audit with UTXO Company, finished private testnet and integration testing with no critical issues, and is essentially mainnet-ready. This isn't a design or prototype, it is a security reviewed system ready for real transactions, which is why we're positioned above the TRL 5 bar and effectively at the mainnet finish line. We are now mostly focused on frontend optimizations for a better user experience.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Lava's architecture is built in Aiken, Cardano's native Plutus v3 smart contract language, using an order batching model rather than direct swaps. When a user stakes, an order UTxO is created holding their deposit, and an authorized batcher processes it alongside other users in a single transaction. This keeps per-user costs low and avoids UTxO contention. Pools are identified by one-shot NFTs to prevent spoofing, admin controls require multisig, and reference inputs let validators read shared config without locking a single UTxO. The exchange rate itself is enforced on-chain to only ever increase, so redemption value is protected by the contract logic, not a promise.

This design is a good fit for the stablecoin integration specifically because L-ADA is essentially just a standard native Cardano tokens once minted, it lives in a wallet, transfers freely, and can be paired in a liquidity pool like any other asset. That means integrating L-ADA as a paired asset for USDM, USDCx, and similar stablecoins doesn't require new contract logic on our end, LPs simply hold a token that already appreciates in the background while their liquidity position earns swap fees. The batching architecture also means this scales cleanly: as more LPs pair stablecoins against L-ADA, order volume increases but per-transaction cost stays low.

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

Lava's target market is Cardano's ADA holders who are staking, from individual delegators to DReps, funds, and whales, anyone whose ADA is currently locked in staking with nowhere else to go. It's also built for Cardano DeFi protocols that need better, more productive collateral.

The clearest evidence for demand is the pattern already playing out on nearly every other proof of stake chain. Liquid staking is one of the biggest primitives in crypto: on Ethereum LST's makes up a huge portion of all onchain TVL, and on Solan, liquid staking tokens have become core DeFi collateral with billions of dollars in TVL. Wherever staking participation is high, a liquid staking primitive shows up and becomes essential infrastructure, because holders want yield and utility, not one or the other. Cardano stands out as the exception: 21.7B ADA staked, but no liquid staking layer, which helps explain why our DeFi TVL has stayed so thin.

Lava also has real traction in the ecosystem. We have locked in day-one integrations across lending, yield splitting, and staking (FluidTokens, Surf, Atlas, Atrium) before even launching, with more protocols in build or under LOI with us. 

### Applicant name

Lava Labs S.A.

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Lava's revenue comes directly from L-ADA usage, not grants or token emissions. The protocol earns a small cut of the ADA staking spread, fees on every mint and redemption, and additional fees plus partner revenue share as L-ADA flows through lending, DEXs, and yield markets. Revenue scales naturally with adoption since there's no reliance on subsidies to keep it running.

This model is proven, not hypothetical. Lido earns around $40M a year in protocol revenue on roughly $18 billion in TVL, almost entirely from staking fees. Jito runs a similar model on Solana, taking a cut of staking rewards and MEV, and has become core DeFi collateral as a result. 

That's what keeps Lava running once Catalyst funding ends: usage generates fees automatically. Cardano has 21.7B ADA staked and almost none of it productive in DeFi, a bigger opportunity than either Ethereum or Solana had when Lido and Jito reached this stage. Lava is built to capture that gap the same way they did.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding directly enables deeper L-ADA and stablecoin liquidity, something that wouldn't happen on its own timeline without dedicated resources behind it. Without it, LP depth grows slowly and organically, meaning early users pairing L-ADA against USDM or USDCx would face real slippage, discouraging the exact behavior we want to encourage.

Funds go directly toward DEX liquidity to bootstrap deeper L-ADA and stablecoin pools on Cardano DEXes, plus the integration work needed to get LPs comfortable pairing against L-ADA. The result is that users can swap between a stablecoin and L-ADA in meaningful size.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month window, Lava will deliver a live, audited L-ADA stablecoin integration on Cardano mainnet, with all evidence required for M1 acceptance:

- **L-ADA minting contract live on mainnet** at a public product URL, with mint/stake/redeem functions operational and the exchange-rate mechanism (1 L-ADA ≥ 1 ADA) verifiable on-chain.


- **Repeated end-to-end mainnet transactions** - the full user flow (deposit → stake → mint → use/redeem) run multiple independent times, with transaction hashes and explorer links provided.
- **Declared footprint published**: script hashes, policy ID, addresses, message tag, and team wallets, per the Transaction Integrity Standard (§4.1) - nothing pre-existing.
- **Audit from UXTO Company published**, with test evidence bundle (checklist, bug log, security note).


- **First L-ADA/USDM DEX pool and FluidTokens lending integration live**, giving real users a reason to transact from day one.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Lava is building L-ADA, a solution to one of Cardano's most basic inefficiencies: right now, you can either stake your ADA and earn staking rewards, or use it in DeFi, but not both. This is a real and tangible problem at scale. There's about 21.7B ADA staked on Cardano, but only \~566M sits in DeFi. Most holders just leave their ADA parked because using it in DeFi means giving up the underlying staking yield.

L-ADA fixes that. You stake your ADA once, and instead of getting a static receipt in your wallet, you get L-ADA, a liquid token that keeps earning staking rewards in the background (its value against ADA quietly increases every epoch) while you're free to actually use it in DeFi: lend it out, provide liquidity on a DEX, post it as collateral, drop it into a yield market. You're not choosing between yield and utility anymore, you get both from the same asset.

This matters for more than just individual holders. Protocols and Institutions get a better class of collateral because L-ADA is productive by default instead of dead weight. And for Cardano as a whole, it's a way to unlock a huge pool of capital that's currently just sitting still, without needing to convince anyone to bring in new money since the ADA is already there, staked and idle. \
\
L-ADA is basically the missing piece that lets Cardano's DeFi ecosystem grow using capital it already has.

### Supporting links (repo, site, demo)

- https://x.com/lava
- https://lava.markets

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

The stablecoin-paired liquidity integration sits at TRL 2 to 3. We've designed the approach (L-ADA paired against USDM, USDCx, and similar stablecoins to give LPs a yield-bearing asset instead of idle ADA), and the core mint/redeem mechanism this depends on is already proven. What's new is the LP-facing layer: incentivizing liquidity providers to pair stablecoins against L-ADA so they earn DEX fees without giving up staking yield, improving depth and transfer experience for stablecoins on Cardano. This grant would carry that integration from design to a live, testnet-validated LP experience and toward mainnet.
