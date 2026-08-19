# anyqr (By SyncAI): spend USDCx at local QRs in 10 countries

> Spend stablecoins from your Cardano wallet at any local payment QR across 10 countries, non-custodial. Global liquidity from p2p.foundation: $31.4M vol, 341,200+ orders since inception.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 39
- **Proposer:** `stake1u9mzuqyq7c0arwx9knnfccalzydln4mxcvzl6d83y8jn49q6wz2wf`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-19T17:33:30.592000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Delivery team:

Mohammed Adnan Khan: Lead Dev & Founder, SyncAI Network\
[Linkedin](https://linkedin.com/in/adnan-khan-x/) | [Github](http://github.com/skepx) | [X](http://x.com/skepticus_x)\
Work: Aiken validators, SDK, identity layer, multi-country deployment, milestone reporting.\
4+ yrs Web3 product architect. Technical Lead at Gravity X Capital and Levitate Labs (Web3 VC/accelerator). Core contributor, UX research, Fetcch.

Jefferson Rohith Fernando — Marketing & BD Strategist\
[Linkedin](http://linkedin.com/in/jeffersonrohithfernando/) | [He runs the social account of SyncAI ](http://x.com/SyncAI_Network)\
Work: wallet/dApp integration outreach, marketing, user onboarding, multi-country partners. He led the BD that put SyncGovHub's DRep tooling live inside Begin Wallet.

Track record:\
Adnan built [SyncGovHub](https://syncgovhub.com), A production Cardano governance tooling: | [Docs](https://docs.syncgovhub.com), live in Begin Wallet (governance tab, DRep explorer).\
[Code for this proposal](https://github.com/SkepX/anyqr)\
AI Track win, Cardano Hackathon IBW: [Code](https://github.com/SkepX/syncai-candi-server) | [Proof](http://x.com/emurgo_io/status/1996847152275116073)\
Best Oracle Tooling, Charli3: [Code](http://github.com/SkepX/charli3-js) | [Proof](http://x.com/Oraclecharli3/status/2048119131447382294)

Recruitment: none required

One Proposal: Adnan's other Catalyst records are prior-fund submissions. In this round Adnan has submitted only this proposal

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

anyqr pledges 5% of all protocol fee revenue to the Cardano treasury from our first mainnet order, until the full 140,000 ADA is returned. Paid in ADA to a published address and reconciled against our public order indexer, so anyone can verify what we owe and what we paid.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Every anyqr order is three onchain transactions, all signed and paid from users' own wallets: the buyer locks USDCx, the merchant accepts, the buyer confirms and that signature releases the funds. No server keys, no sponsored fees (§5.2, §12.3). Mainnet at week 10, ahead of the limit, gives a \~10 epoch window.

STABLECOINS. The 76 Preprod transactions calibrate unit cost, not demand: 0.31 ADA per transaction, 0.91 per order. 700 orders is 2,100 transactions and \~640 ADA on a 301 floor: 14 orders a day across 15 merchants, under one each per day.

IDENTITY, DERIVED. 15 merchants x (1 DID mint + 1 zkTLS proof) = 30. 120 buyers x 1 credential anchor at first order = 120. 700 orders x 1 reputation attestation at close = 700. Total 850. We declared 550, since orders opened late in the window close after it.

REACHING IT. Conversion is our own GTM, merchants recruited off Binance P2P leaderboards, pay-to-QR embedded in Cardano wallets via our SDK, concierge onboarding, regional launches. The target assumes zero [p2p.me](http://p2p.me) fills which is a open smart contract, no LOI needed.

CAPS. Fifteen merchants keeps each wallet near 2% of fees, 50 days clears the daily cap,.

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

Without it, anyqr stays a Preprod demo. The contract works; what we cannot fund on our own time is mainnet with everything above. Nothing here is retroactive.

BUILD 84,000ADA

19,600 validator update: merged release, merchant DID in datum, fee split, QR onchain\
19,600 CIP-0170 service: DID mint, Reclaim zkTLS, reputation attestation\
14,000 merchant order book, onboarding, dispute path\
14,000 nine QR parsers beyond live UPI\
7,000 dual routing to [p2p.me](http://p2p.me)\
9,800 npm SDK, wallet plugins, client-side signing

GROW 35,000ADA

21,000 merchant recruitment in India, Brazil, Indonesia, Vietnam; never payment for transacting\
14,000 concierge onboarding, public indexer and dashboard day one

MARKET 21,000

local-language content and dev relations so wallets embed the flow

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By week 10, anyqr will be live on mainnet, real users completing USDCx orders

ESCROW. Updated Aiken validator on mainnet: release merged into the buyer's confirmation (three txs per order); a merchant timeout claim; merchant DID in the datum; a fee split at release; the QR address on chain, encrypted to the merchant

SIGNING. Non-custodial CIP-30: users sign & pay every tx, no server keys (§5.2)

ORDER BOOK. Merchants post their own rates onchain, orders route by reputation. Dual routing: orders reach our book and [p2p.me](http://p2p.me)'s merchants

IDENTITY. CIP-0170 live: merchant DID mint, Reclaim zkTLS verification, buyer credential anchor at signup, reputation stamped at close. Disputes with a resolution path

CORRIDORS. UPI, QRIS, PIX, VietQR, PromptPay, QR Ph, Yape, Nequi, DeUna, MercadoPago. SDK on npm

MEASUREMENT. A message tag on every tx, a public dashboard, a declared footprint: script hashes, USDCx policy, stake keys

PROOF. 20+ orders from 10+ non-team wallets, 5+ DIDs

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

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

WHAT THE GRANT BUILDS FOR A TRL 9:

Merchant DID onboard. Each mints a CIP0170 DID & uses ReclaimProtocol for zkTLS social proofs. The proofs attach to DID, completed orders write back which increases reputation score.

\-updated validator: merchant DID in the datum, a fee split on Complete, the QR address on chain, encrypted\
-mainnet deployment with USDCx & USDM\
-the dispute resolution flow\
-dual routing, so an order reaches our book and [p2p.me](http://p2p.me) merchants\
-nine countries beyond live UPI: PIX, QRIS, VietQR\
-a public npm SDK with wallet plugins
