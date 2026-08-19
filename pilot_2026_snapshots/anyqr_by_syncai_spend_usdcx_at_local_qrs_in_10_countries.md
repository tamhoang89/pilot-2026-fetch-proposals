# anyqr (By SyncAI): spend USDCx at local QRs in 10 countries

> Spend stablecoins from your Cardano wallet at any local payment QR across 10 countries, non-custodial. Global liquidity from p2p.foundation: $31.4M vol, 341,200+ orders since inception.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 33
- **Proposer:** `stake1u9mzuqyq7c0arwx9knnfccalzydln4mxcvzl6d83y8jn49q6wz2wf`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-19T02:30:48.982000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Adnan has 4+ years of Web3 experience as a product architect across multiple startups. He previously served as a Research Partner at Levitate Labs, a Web3 venture capital firm and accelerator, and was a core contributor to UX research at Fetcch, a Web3 fintech research venture. He holds a degree in Data Science & Machine Learning and is now Founder and CEO of SyncAI Network 

Adnan is also a two-time hackathon winner:

→ AI Track — Cardano Hackathon, IBW Edition

→ Best Oracle Tooling — Charli3 Oracles Hackathon

These wins demonstrate his ability to rapidly design and deliver working blockchain solutions across AI and oracle tooling.

SyncAI Network — [syncai.network](http://syncai.network)

SyncAI is a blockchain development company with 11+ developers specializing in Web3 and AI. The team has worked with established projects including Biconomy, 0G, Nillion, NMKR, Iagon, IAMX and Nucast, contributing to products and infrastructure across the ecosystem.

SyncAI has also built production-ready Cardano governance tooling designed for integration by wallets and dApps, with an existing integration in Begin Wallet. This experience building embeddable infrastructure is directly relevant to delivering utility that can be adopted across the Cardano ecosystem.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

anyqr pledges 5% of all protocol fee revenue to the Cardano treasury from our first mainnet order, until the full 140,000 ADA is returned. Paid in ADA to a published address and reconciled against our public order indexer, so anyone can verify what we owe and what we paid.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Every anyqr order is three onchain transactions, and users sign all three. The buyer signs twice: once to lock USDCx in escrow, once to confirm the shop was paid, and that second signature is the release itself, paying the merchant in the same transaction. The merchant signs once to accept. Every fee comes from a user's own wallet. No server keys, no sponsored fees (§5.2, §12.3).

Mainnet at month 1.5, not the three-month limit, gives a \~14 epoch window and lowers every epoch floor.

WHO TRANSACTS. Buyers are Cardano holders in ten QR-first countries who want to spend, not sell. Merchants are P2P traders on Cardano, plus [p2p.me](http://p2p.me)'s network via dual routing. Buyers repeat because paying a shop is a habit, not a one-off conversion; merchants recycle capital several times a day for a 2% spread.

ARITHMETIC. Preprod fees average 0.31 ADA per transaction, so an order costs about 0.91 ADA. 700 orders over 14 epochs is 2,100 transactions and \~640 ADA against a 301 floor: 10 orders a day from about 120 buyers and 12 merchants.

WHY IT HOLDS. Twelve merchants keeps each wallet under the 35% cap, 70 days of volume clears the 20% daily cap, and we pay nobody to transact.

### How will you reach and onboard real users - and what evidence backs your channels?

Neither side of this market has to be invented. Both already exist.\
\
SUPPLY. Two channels, both already populated. First, [p2p.me](http://p2p.me): integrating their book gives Cardano orders live liquidity from day one, 1,000+ merchants and $4.7M settled a month, instead of a cold start. Second, direct recruitment of traders already doing this on Binance P2P, visible on public leaderboards and Telegram groups across India, Vietnam, Brazil and Indonesia, where up to 90% of P2P listings are stablecoin (TRM Labs). \
Pitch: same business, non-custodial, no freeze risk, rates they set. We pay nothing; they earn the user-paid spread. [p2p.me](http://p2p.me) proved this path to 341k orders.

DEMAND. USDCx holders get a fully functional app on day one, not a waitlist. We reach them through Cardano regional communities and X content marketing. Then marketing the open SDK: so any Cardano wallet can embed pay-to-QR, this one integration reaches a whole userbase instead of one user at a time.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://www.youtube.com/watch?v=VjpIu8M0ZWc

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today it is a centralised P2P desk. Binance P2P or OTC: account, KYC, custodial deposit, find a counterparty, trade, withdraw, then buy. MoonPay and Transak end at a bank too, never the shop's QR.

The onchain model is proven: [p2p.me](http://p2p.me) on Base ($31.4M, 341,200+ orders, Coinbase-backed) and ZKP2P ($1M+ a month). But that is a few 100k orders against 23bn UPI payments a month in just one country, and none on Cardano. We do not compete with [p2p.me](http://p2p.me), we route to their liquidity alongside a Cardano-native book so orders fill faster.

Users switch because nothing is ever held: scan, sign, & your payment is done facilitated via an Aiken validator.

USDCx is Cardano’s largest stablecoin, funded by a 70M ADA vote. anyqr gives users a way to spend it IRL.

### Please provide details about the Technology Readiness Level selected for your existing product

anyqr runs end to end on Cardano Preprod today. A buyer scans a shop QR, locks tUSDM in escrow, a merchant accepts and pays the shop in fiat, the buyer confirms, and the escrow releases to the merchant. 76 transactions at the escrow address so far.

Underneath: one Aiken Plutus V3 validator carries each order as its own UTxO through Placed, Accepted, Paid and Disputed, with 9 property tests over every redeemer, deadline and failure path. @qrpay/sdk on Lucid Evolution gives every action a prepare that returns an unsigned tx and an execute that submits it. CIP-30 connect ships for Lace, Eternl and Vespr. Release is automatic: no merchant signature, no claim button.

[Escrow Link](https://preprod.cardanoscan.io/address/addr_test1wrultc2jal2y5ql8m5ant6u4xkn79zgpr8d590tav7fyjcqng2vfq)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Three parts: a contract that holds the money, an identity layer that makes merchants trustworthy, and an app tying both.

THE CONTRACT. One Plutus V3 Aiken validator, one UTXO per order, like SundaeSwap and Minswap. State (Placed, Accepted, Paid, Disputed) sits in an inline datum, the redeemer picks the action, and no two buyers touch one UTXO. The datum holds the trade: both amounts, deadlines, and the policy id, so one validator settles USDCx today and USDM later. The QR address moves in two steps: the merchant publishes an ECIES pubkey on Accept, the buyer pushes the address encrypted to it, and only that merchant can decrypt and pay. Never public. USDCx is native, so escrow and payout are plain onchain moves. Release needs no merchant signature: Complete checks status Paid, a validity interval past the dispute deadline, and full payment out, fired by the validity range, not a server. CancelUnaccepted, Refund, RaiseDispute and a Resolve that only pays buyer or merchant cover the rest: worst case is delay, not loss.

IDENTITY. A merchant is only a key hash today. Each will anchor a CIP-0170 DID from their own wallet with Reclaim zkTLS social proofs; completed orders write back to it, and reputation also.

THE APP. The order book is the escrow's open UTXO set: merchants read it and self-select, no matching backend. It ships as an npm SDK any wallet can embed. Route two uses [p2p.me](http://p2p.me)'s SDK, bridging USDCx to their contract where it fills faster.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

anyqr sits between two markets that already exist at scale.

**USERS.** Goldman Sachs estimates 66% of stablecoin supply is in emerging markets. 5/10 launch countries alone hold 194 million crypto owners: India 104M, Philippines 27M, Brazil 27M, Vietnam 22M, Indonesia 14M (Triple-A). Chainalysis 2025 puts seven of the ten in the world's top 20: India 1st, Vietnam 4th, Brazil 5th, Indonesia 7th, Philippines 9th, Thailand 17th, Argentina 20th. They hold dollars but cannot spend them. Off-ramps were built for traders cashing out to a bank, not everyday payments: an exchange account, a bank, KYC, days of settlement. Standard Chartered projects $1 trillion leaving EM deposits for stablecoins in three years.

**RAILS.** QR is how these countries pay. Brazil's PIX moved R$35.4 trillion across 79.8 billion payments in 2025. India's UPI processed $3.56 trillion in FY26. Indonesia's QRIS doubled to 12.5B+ txs in H1 2026. Vietnam, Thailand & Peru run the same model, and every shop already accepts.

**PROVEN.** [p2p.me](http://p2p.me) runs this model on Base, swapping USDC against UPI and PIX QR: $31.4M settled, 341,200+ orders, $4.69M in July 2026, up 31% MoM, backed by Coinbase Ventures. Demand is not the question. We will integrate their merchant network so those merchants fill Cardano orders too, giving liquidity on day one, not a cold start.

TIMING. USDCx launched 27 Feb 2026 & is Cardano's largest stablecoin at $17.5M, 36% share (Messari). No spend rail exists. We are building it.

### Applicant name

Mohammed Adnan Khan

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Bob is visiting Vietnam and wants to buy a $10 item. The shop only takes VietQR. He has no Dongs, but he holds USDCx on Cardano.

He scans the shop's QR in anyqr and signs once. About $10.25 of USDCx locks: $10 for the shop, \~2% to the merchant, a small anyqr fee, all quoted before he signs. A merchant, from our book or [p2p.me](http://p2p.me)'s network, accepts and pays the shop in Dongs from their bank app. Charles confirms the money arrived and the escrow releases the money.

**WHO PAYS.** Bob, once, at settlement. Merchants set their own spread and compete on rate in an open book. anyqr never touches fiat, so we are not a money transmitter, only a fee on settled volume.

**WHY IT RUNS.** Merchants earn real yield on capital they recycle several times a day, and a purchase repeats where a conversion does not. Completed orders build reputation in their DIDs, reputation raises limits, limits pull more Cardano mainnet volume. 

### On-chain identity (CIP-0170) - expected transaction count

550

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without it, anyqr stays a Preprod demo. The contract works; what we cannot do on our own time is carry it to mainnet with everything above.

Build (\~60%): mainnet on USDCx/USDM; updated validator (merchant DID, fee split, QR onchain); dispute flow; merchant order book & onboarding (Reclaim proof, DID mint, reputation); parsers for the 9 QR standards beyond live UPI through VietQR and Yape; dual routing to [p2p.me](http://p2p.me); an npm SDK with wallet plugins; client-side signing, no server keys.

Grow (\~25%): recruiting first merchants in India, Brazil, Indonesia and Vietnam through outreach, education and support, never payment for transacting; concierge onboarding; a public dashboard day one.

Marketing (\~15%): local-language content and dev relations so wallets embed it.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By week 6, anyqr is live on mainnet, real users completing USDCx orders.

ESCROW. Updated Aiken validator on mainnet: release merged into the buyer's confirmation (three txs per order); a merchant timeout claim; merchant DID in the datum; a fee split at release; the QR address on chain, encrypted to the merchant

SIGNING. Non-custodial CIP-30: users sign & pay every tx, no server keys (§5.2)

ORDER BOOK. Merchants post their own rates onchain, orders route by reputation. Dual routing: orders reach our book and [p2p.me](http://p2p.me)'s merchants

IDENTITY. CIP-0170 live: merchant DID mint, Reclaim zkTLS verification, buyer credential anchor at signup, reputation stamped at close. Disputes with a resolution path

CORRIDORS. UPI, QRIS, PIX, VietQR, PromptPay, QR Ph, Yape, Nequi, DeUna, MercadoPago. SDK on npm

MEASUREMENT. A message tag on every tx, a public dashboard, a declared footprint: script hashes, USDCx policy, stake keys

PROOF. 20+ orders from 10+ non-team wallets, 5+ DIDs

### How far along is the integration you're proposing, today?

TRL 9 - Actual system proven in operational environment

### On-chain identity (CIP-0170) - fee target (ADA)

160

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

USDCx launched on Cardano in February 2026, the first Circle-issued dollar native to the chain. You can hold it, trade it and bridge it. You cannot spend it in real world.

To turn it into money a shop accepts, you need a centralised exchange, a bank account and days of waiting. In emerging markets, where stablecoins matter most, that path is often geo-blocked, KYC-gated or simply missing.

Yet those same people pay by QR every single day. UPI in India, PIX in Brazil, QRIS in Indonesia, VietQR in Vietnam. UPI and PIX alone moved over $10 trillion last year. And these are the world's heaviest crypto users: in the Chainalysis 2025 Crypto Adoption Index, seven of our ten launch countries rank in the global top 20, five in the top 10.

The rails exist. The dollars exist. Nothing connects them.

anyqr is that connection. You scan any shop's QR code & sign one Cardano transaction that locks your USDCx in an on-chain escrow. A local merchant takes the order, from our Cardano book or from [p2p.foundation](http://p2p.foundation)'s network ($4M+ vol/month), pays the shop in local currency over the QR rail, and claims the USDCx once you confirm the money arrived in just 90 seconds.

The shopkeeper never touches crypto. No custodian ever holds the funds, only an Aiken validator on Cardano.

Cardano finally has USDCx. We make it spendable at ten million corner shops. Idle balances become daily transactions, and a chain built for the unbanked finally does the thing it was built for.

### Supporting links (repo, site, demo)

- https://anyqr.cash/
- https://github.com/skepx/anyqr
- https://www.youtube.com/watch?v=VjpIu8M0ZWc

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

MIT License

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

2100

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

600

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

LIVE:

An escrow contract and MVP app on Preprod. Settlement is in tUSDM, a real Cardano native stablecoin, and a trade runs end to end: buyer locks, merchant accepts, buyer confirms, escrow releases with no merchant signature.

WHAT THE GRANT BUILDS:

Merchant DID onboarding. Each mints a CIP-0170 DID and uses Reclaim Protocol for zkTLS social proofs. The proofs attach to the DID, completed orders write back which increases reputation score.

\-updated validator: merchant DID in the datum, a fee split on Complete, the QR address on chain, encrypted\
-mainnet deployment with USDCx and USDM\
-the dispute resolution flow\
-dual routing, so an order reaches our book and [p2p.me](http://p2p.me) merchants\
-nine countries beyond live UPI: PIX, QRIS, VietQR\
-a public npm SDK with wallet plugins
