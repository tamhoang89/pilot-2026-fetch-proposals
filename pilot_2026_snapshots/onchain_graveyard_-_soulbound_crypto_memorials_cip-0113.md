# Onchain Graveyard - soulbound crypto memorials (CIP-0113)

> Bury what the bear market took. Engrave a permanent, non-transferable memorial on Cardano L1 using CIP-0113 programmable tokens, then light candles and leave flowers for free inside a Hydra Head.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 20
- **Proposer:** `stake1uyhp5yphtclaane5rvgfgml0yp8luy49f6mld848a32ff5qvs3l0x`
- **Funding requested:** ₳118,000
- **Last finalized:** 2026-08-19T16:55:11.193000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Vtechcom has completed and fully closed three Fund14 projects. Onchain Graveyard already runs on preprod, so this is a focused three-month integration and productization effort, not a greenfield build.\
\
Pham Hai — Technical Lead, Cardano/Aiken/CIP-0113: <https://www.linkedin.com/in/phamhai99/>\
Trinh Manh Cuong — Backend/L1 Indexing: [https://www.linkedin.com/in/cường-trịnh-mạnh-241446385/](https://www.linkedin.com/in/c%C6%B0%E1%BB%9Dng-tr%E1%BB%8Bnh-m%E1%BA%A1nh-241446385/)\
Vu Quoc Huy — Frontend/Wallet UX: <https://www.linkedin.com/in/huyvu-dev/>\
Cong Nghia Khiem — DevOps/Hydra: <https://www.linkedin.com/in/congnghiakhiem/>\
Hong Quyen — QA: <https://www.linkedin.com/in/hong-quyen-383653118/>\
Nguyen Viet Thanh — Product/Project/Growth Lead: <https://www.linkedin.com/in/nguyenvietthanh/>\
Public engineering evidence: <https://github.com/Vtechcom>.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Individuals memorialise real crypto losses. Not everyone who loses money will pay. Our hypothesis is that a subset will pay for closure, humour and a lasting story-not to recover the loss-much as people pay for a rage room. Unlike a rage room, the deed remains as a shareable, permanent, non-transferable memorial. Entry starts at 1 ADA; users sign and pay from their own wallets and may return for another memorial or one-step tier rise.

First 14 days: Days (1–3) five LOI partners launch posts/banners; Vtechcom provides bilingual wallet help. Days (4–7) follow-ups, Q&A, stories and funnel fixes; target 130–170 external wallets/240–320 transactions. Days (8–14)second partner wave, creator stories, “Depegs” collection and public dashboard; target 280–340 wallets/600–720 transactions. Afterward: one theme plus two community/creator activations weekly. Details: <https://drive.google.com/file/d/1FwSm-pIjydlot3h4MoUhSiV7BXf7DYvl/view>

Total: 1,000–1,150 mints from \~800 distinct external wallets plus \~700–750 tier rises = \~1,800 transactions and 510 ADA fees \~0.283 each. No airdrops, rebates, sponsored transactions; every counted user independently chooses, signs and pays.

### How will you reach and onboard real users - and what evidence backs your channels?

Five signed LOIs anchor launch: FIMI; VCC/Cardano ADA Viet Nam; SKY3; DCOne; and Midnight Explorer. LOIs schedule launch posts on Days 1–3, follow-ups on Days 4–7, and reminders/onboarding on Days 8–14. Minimum stated reach is 14,900 views/impressions. [Click to view details of the planned operational commitments from signed partners.](https://drive.google.com/drive/folders/1KlNQdc-9Scqkn0biAojtcJMIjrjeUgQR)

Full-window sources: 300 external wallets from LOI partners; 160 from Vtechcom's Cardano/Hydra network; 130 from global Cardano channels; 120 from creators and weekly “Depegs/Lost Exchanges/Bear Market 2026” collections; 90 from share pages/cross-chain reach = 800. We provide bilingual wallet guides, two live Q&As and daily signing support, tracking source -&gt; visit -&gt; wallet connect -&gt; confirmed L1 transaction. [Click to view our plan.](https://drive.google.com/file/d/1FwSm-pIjydlot3h4MoUhSiV7BXf7DYvl/view)

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/EJYxE5LKI6k

### Who else solves this today - competitors/alternatives, and why does your approach win?

Crypto Graveyard ([cryptograveyard.io](http://cryptograveyard.io)) is the closest competitor: token cemetery, memorials, leaderboards and SBT-style profiles. But its public version is still pre-MVP, uses sample data and has no live wallet connection. Free alternatives such as X loss threads, Discord screenshots and “rekt” leaderboards are temporary.

Why users switch: others cost nothing but leave nothing. We offer permanence—an artifact no platform can delete.

Our key proof: memorials are genuinely non-transferable, enforced by a shared-custody spend validator and validated through 13/13 adversarial gates against real ledger rules. Many “soulbound” designs only block burning at minting, leaving tokens transferable later. Ours does not.

### Please provide details about the Technology Readiness Level selected for your existing product

Existing product: TRL 6—an integrated prototype demonstrated in a relevant environment. The public Cardano preprod deployment includes CIP-30 wallet connection, a 2.5D cemetery with about 1,160 plots, engraving and upgrade flows, public grave/share pages, backend and event processing, plus Hydra candle/flower interactions. Reviewers can test it at <https://preprod.hydra-graveyard.vtechcomlabs.com/>. It is not yet a mainnet production system: L1 authority migration, CIP-0113, security hardening, independent review and production operations remain in the Pilot scope.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

One direct wallet transaction contains the Cardano network fee, deed-UTxO min-ADA, transparent service payment, one-shot plot claim and deed issuance. The Programmable Memorial Deed uses CIP-0113 shared programmable-token custody, with ownership resolved by stake credential. The NonTransferableMemorial rule rejects outputs owned by a different stake credential, permits same-owner restructuring/upgrades, and exposes no burn flow during the Pilot. Registry/lifecycle configuration is pinned and published so the transfer promise cannot be silently relaxed.\
\
Cardano L1 is authoritative for deed existence, owner, plot consumption, content hash and the declared measurement footprint. A rollback-aware indexer creates only a PostgreSQL projection; a grave becomes Active only after L1 confirmation. Moderated display text stays off-chain and is anchored by a deterministic hash.\
\
Hydra handles candles, flowers and visit activity; no deed or user-owned asset must enter a Hydra Head. A Hydra outage cannot block L1 issuance and degrades the social layer to read-only. CIP-0113 is therefore essential, not decorative: it enforces non-transferability while L1 supplies verifiable, attributable usage under the Transaction Integrity Standard.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Our primary market is retail crypto users who suffered losses in a bear market. This audience spans every major blockchain and renews with each cycle. Thousands of listed tokens are now effectively worthless, each leaving a community of holders with untold stories. CoinGecko Research reports that 53.2% of cryptocurrencies in its GeckoTerminal dataset had failed, including 11.6 million token failures in 2025 alone.

Demand already exists but is underserved. Loss threads, “rekt” leaderboards and portfolio screenshots show that grief-and-humour rituals around crypto losses are a durable social format. People perform them publicly and for free, but existing platforms preserve no permanent record. We believe a durable, ownable artifact for the same ritual will find an audience.

The complete product already runs on Cardano preprod with real Eternl and Lace wallets. The full journey-from wallet connection and epitaph engraving to social interactions in the 2.5D cemetery-works end to end across the backend and user interface.

Our beachhead is Cardano/Hydra communities, Vietnamese crypto users and market-cycle content creators. The pilot is deliberately limited to \~1,500 plots, targeting 1,000–1,150 memorials from \~800 external wallets-a small, realistic and defensible share of the market.

### Applicant name

VTECHCOM

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Users pay per action from their own wallet, in the transaction that mints the deed, no prepaid balance, and we never custody user funds. Checkout shows three components: network fee (to Cardano), min-ADA (locked in the deed's UTxO, disclosed as non-recoverable), and our service price (routed to the Onchain Graveyard treasury by the validator itself).

Service pricing runs across eight tiers, 1 ADA (Earth) to 200 ADA (Diamond), multiplied by a district land factor of 0.6–2.0 and doubled on premium plots. Tier upgrades are a second revenue event: one step, pay the difference, enforced on L1.

Why usage persists after the grant: revenue is not grant-dependent — this is a digital-goods sale with positive unit economics from the first memorial, and the cemetery gains value as it fills. Post-pilot lines already scoped: sponsored and curated collections, physical QR plaques, premium visual upgrades, and archive/API access.

Out of scope: resale marketplace, rewards pool, holder revenue share.

### Programmable tokens (CIP-0113) - expected transaction count

1800

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The grant converts a self-funded preprod product into a secure, measurable mainnet vertical slice. Budget: CIP-0113 rule, plot claim and tx builder-23k ADA; L1 indexer/backend authority-14k; wallet/frontend/proof UX-10k; independent security review and remediation reserve-24k; Hydra social operations-3k; QA, DevOps, release engineering and documentation-8k; user acquisition and partner onboarding-18k; creator, launch and retention campaigns-8k; project management, adoption measurement and reporting-5k; infrastructure, storage and monitoring-5k. Total: 118k ADA. The increase funds security, production hardening and post-launch stabilization-not sunk work, generic price speculation or user incentives.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. CIP-0113 memorial certificate on mainnet: a shared-custody spend validator enforcing non-transferability, one-step same-owner tier rises and no burn path, registry authority irreversibly frozen. Published script hash and policy ID.
2. Plot Ticket beacon policy seeded across \~1,500 plots, making duplicate mints impossible at ledger level.
3. Independent audit completed, no unresolved Critical or High findings,remediation published.
4. L1 mint-indexer live, rollback- and replay-safe: no deed is marked active without a valid observed L1 transaction.
5. Non-custodial checkout live: users pay from their own wallet in the minting transaction, with network fee, min-ADA and service price shown before signing. Prepaid Grave Credit removed.
6. Public product live on mainnet: real external users engraving deeds, with Hydra-settled candles and flowers.
7. Catalyst message tag on 100% of core transactions, public usage dashboard and declared footprint registered.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Programmable tokens (CIP-0113) - fee target (ADA)

510

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Crypto losses are universal but rarely preserved. Every cycle wipes out retail portfolios, while the stories behind those losses disappear in group chats, deleted posts and abandoned communities. Failed projects vanish too, taking part of each cycle’s history with them.

Onchain Graveyard turns those failures into public, verifiable memory. A user writes an epitaph for a personal loss or documented failed project, signs one Cardano mainnet transaction, and receives a permanent, non-transferable Memorial Deed. The grave appears in a shared isometric cemetery of \~1,500 plots. Visitors can light candles, leave flowers and pay respects instantly at zero fee inside a persistent Hydra Head. See: <https://onchain-graveyard.vtechcomlabs.com/?lang=en#built>

The memorial uses a CIP-0113 programmable token that cannot be sold, preventing loss stories from becoming speculative assets. Its epitaph is stored in the on-chain datum, so the record survives even if our servers disappear.

The product is for retail crypto users across any chain who want to mark a loss and preserve its story, while also creating a simple first interaction with Cardano. It offers no refunds, yield, resale market or fraud claims. Its value is closure, memory and ritual.

### Supporting links (repo, site, demo)

- https://preprod.hydra-graveyard.vtechcomlabs.com/
- https://github.com/Vtechcom
- https://youtu.be/EJYxE5LKI6k
- https://onchain-graveyard.vtechcomlabs.com/?lang=en#built
- https://onchain-graveyard.vtechcomlabs.com/phase0.html

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

Apache-2.0

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Proposed CIP-0113 integration is at TRL 4, validated in a controlled lab environment. The in-house NonTransferableMemorial and PlotTicket validators run together in an offline Hydra Head using L1 Conway rules and the Plutus V3 cost model. All 13 ledger gates and 54 on-chain tests pass, including issuance, owner rejection, same-owner tier upgrades, underpayment, content mutation and duplicate plots. Estimated fees are \~0.398 ADA for issuance and \~0.320 ADA for upgrades; deed min-ADA is 1.534–2.384 ADA. Report: <https://onchain-graveyard.vtechcomlabs.com/phase0.html>. Public Preview/Preprod validation is still pending, along with owner-credential choice, land pricing, PlotTicket hardening, reference scripts, CIP-30 signing, rollback-safe indexing, independent review and mainnet release.
