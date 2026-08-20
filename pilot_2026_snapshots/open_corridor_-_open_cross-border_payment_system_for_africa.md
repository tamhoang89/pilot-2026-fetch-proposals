# Open Corridor - Open cross-border payment system for Africa

> African money shouldn't travel via London to get from Lagos to Johannesburg. Open Corridor lets licensed banks pay each other in seconds — promises on Cardano, priced by Pyth, settled per corridor.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 15
- **Proposer:** `stake1u9htywez2l628qvmqacp0py292w0g6m6vevmqy0dhw8n6lglca2et`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T04:41:12.822000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

TESOBE has built bank-grade open-source infrastructure for 15 years — the Open Bank Project, an inspiration for UK Open Banking, used by Tier 1 and smaller banks worldwide. Team has worked together for 10 years:

\- Redfern — project lead; Bank Node engineering (Rust/Cardano). [github.com/simonredfern](http://github.com/simonredfern) · [linkedin.com/in/simondavidredfern](http://linkedin.com/in/simondavidredfern)

\- Zhang — OBP-API platform (Scala), bank integration. [github.com/hongwei1](http://github.com/hongwei1) (3,000+ commits)

\- Milić — OBP-API platform (Scala). [github.com/constantine2nd](http://github.com/constantine2nd) (4,000+ commits)

\- Wölk — Kubernetes, DevOps, smart contracts. [github.com/tawoe](http://github.com/tawoe)

\- Tippmann — DevOps, infrastructure, monitoring. [github.com/karmaking](http://github.com/karmaking)

\- Thiam — research, marketing, business development. [linkedin.com/in/dylan-thiam](http://linkedin.com/in/dylan-thiam)

Collaborators: corridor development partners (entrepreneurs) in Nigeria, SA and Cameroon — the pilot banks are recruited through this network. Names confidential until participation agreements are signed (months 1–2); evidence of engagement available to reviewers on request.

To recruit: an in-country bank integration engineer per pilot jurisdiction, and a senior Cardano specialist (Aiken/Plutus) to independently review all on-chain work.

No team member appears on any other proposal this round, in any role.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

0.1% of corridor transaction-fee revenue to the Cardano treasury for 5 years, capped at 200,000 ADA

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Usage is the product working i.e. each customer payment a pilot bank sends becomes one promise transaction on Cardano; each netting cycle becomes one settlement with a Pyth-verified quote. Who transacts: the two pilot banks, on instruction of their existing customers — remitters and SMEs already paying across the corridor, rerouted because the bank credits in seconds at \~0.5% instead of 3–9%. How often: customer payments daily once live; settlements on a regular cycle in both directions. The targets are a sliver of real flow: ≥500 promises is \~10–15 payments/day on corridors moving billions per year — no user incentives needed — yet ambitious: each one needs licensed banks running their own nodes on mainnet. ≥20 settlements follows from regular netting; 100% Pyth-priced holds by construction. Two caveats: bank onboarding pace is what we control least — banks and regulators set it — so targets are floors for a live corridor, not calendar promises; mainnet USDCx settlement in month 3 is in our hands, real flows ramp at the banks' pace. And fee targets assume the cadence above (daily netting, daily FX attestation, one quote per settlement): volume follows corridor count.

### How will you reach and onboard real users - and what evidence backs your channels?

Our users are banks. TESOBE has sold banking infrastructure for 15 years — to Tier 1 and smaller banks globally, an inspiration for UK Open Banking — with commercial clients in Africa today: a Tanzanian bank and a Botswana innovation centre. Around them sits a working partner network of entrepreneurs and fintechs in Nigeria, South Africa and Cameroon, candidates to open the first corridors with their local banks — seven countries, including the two markets anchoring the top intra-African corridors; Africa–China trade corridors are a later target on the same channel. Onboarding is deliberately self service: a bank runs its own open-source node against existing systems — two touchpoints, no core rebuild. The pilot's largest budget line funds exactly this channel: contracting the pilot banks, integrating their cores, training staff to run the nodes, engaging their regulators — so the second corridor opens cheaper than the first.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/v9T0dolrniw

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today: SWIFT + correspondent banking — the default route, but messaging only, not settlement; flat fees compound per correspondent hop (3–9% on typical African transfers), and they are structural: SWIFT cannot cut them without dismantling correspondent banking itself. PAPSS — central-bank netting, 160+ banks in 19 countries — proves banks want African-owned rails but is sovereign RTGS-style, with no REST API; since Open Corridor is settlement-agnostic, PAPSS is a potential rail under OC, not only a rival. Zone — a licensed blockchain switch, Nigeria-only. OC wins as the commercial, API-native, pan-African layer: banks self-onboard with an open-source node (no core rebuild), \~0.5% fees, customers credited in seconds with netted settlement, every promise and price auditable on Cardano.

### Please provide details about the Technology Readiness Level selected for your existing product

The foundation, OBP-API, has been in commercial use for nearly 15 years by various banks and regulators and deployed in different contexts including Kubernetes and Open Shift. Functional Scala code in the JVM. 

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Three on-chain uses. (1) Promises: every payment anchors a salted SHA-256 commitment in transaction metadata (CIP-20; addresses per CIP-19) — no amounts, names or PII ever touch the chain, satisfying banking confidentiality and data-protection requirements while keeping every commitment independently verifiable. Cardano's deterministic fees make per-payment anchoring predictable at volume — a treasury can budget it. (2) Settlement: the netted difference between two banks moves as a native-asset transfer — ADA today, USDCx next. Because Cardano native assets need no token contract, USDCx enters through the same settlement executor, wallet, signing and audit path as ADA — one integration, two assets, and the same path for future per-corridor stablecoins. The eUTxO model gives exact, replayable settlement history, and the node promotes a settlement to FINAL only at configurable confirmation depth. (3) Verification: the FX rate locked at settlement is verified on-chain against the Pyth Lazer integration, so the price a settlement executed at is auditable on the same chain as the settlement itself — by either bank or a regulator, after the fact, without trusting the platform. The CIP-0170 exploration designs on-chain participant attestation (today: X.509 certificates against a regulator-operated register). Throughout, banks hold their own keys and write through their own cardano-node — no third-party custody.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Oracles
- Stablecoins
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Target market: Africa's licensed commercial banks — 760–850 institutions, only \~10–15 of which can offer meaningful cross-border payments today; the rest buy expensive intermediation. We start with the highest-volume intra-African corridors — Nigeria–South Africa (\~$2.3B/yr), SA–Zimbabwe (\~$4.6B), Nigeria–Ghana (\~$1B) — reached through TESOBE's existing network of banks, fintechs and entrepreneurs across seven countries including Nigeria and South Africa, home to the continent's largest banks by Tier-1 capital. TESOBE already has commercial clients there: a Tanzanian bank and a Botswana innovation centre.

Evidence of demand: banks pay 3–9% per transfer through multi-hop correspondent chains, plus $45k–$950k three-year TCO for SWIFT connectivity; Open Corridor charges 0.5% through a node the bank runs itself. Adjacent adoption proves appetite: 160+ banks across 19 countries joined PAPSS — banks clearly want African-owned rails — but PAPSS is sovereign RTGS-style infrastructure with no REST API and slow onboarding; Open Corridor is the commercial, API-native complement. The region already settles on-chain (\~$205B in the year to mid-2025, 43% of it stablecoins — Chainalysis), and regulators have moved from bans to licensing: cNGN live in Nigeria, CASP licensing in South Africa, Botswana's Virtual Assets Act. And the product exists: a working end-to-end system on Cardano, demoed to pilot-candidate banks, built on the platform TESOBE has run with banks for 15 years.

### Applicant name

TESOBE GmbH

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Open Corridor is transaction infrastructure with a simple model: participating banks pay a one-time onboarding fee, an annual membership, and \~0.5% per transaction (tiered, capped for high values) — against the 3–9% they pay correspondent chains today, so every payment saves them money from day one. Unit economics are software-like: hosting plus sub-cent Cardano fees leave &gt;90% gross margins, and our plan projects profitability from year two on modest corridor volumes. Usage continues after the grant because the pilot's deliverable is not a demo but revenue-generating corridors: banks running their own nodes on real customer flows, under participation agreements, with a regulator evidence pack and playbook that make each new corridor cheaper to open than the last. Every payment anchors a promise on Cardano and every netting cycle settles on-chain — commercial usage that outlives the grant is, by construction, recurring Cardano usage.

### On-chain identity (CIP-0170) - expected transaction count

10

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without funding the new code stays in the lab; with it, licensed banks run it on mainnet in real situations — and we learn what real corridors demand. The grant buys what does not self-serve: recruiting and contracting the pilot banks, integration support while each bank connects its own core system and treasury, training bank staff to run their own nodes, and structured regulator engagement in each jurisdiction (\~47%); the USDCx settlement rail (\~22%); on-chain Pyth quote verification (\~10%); the CIP-0170 identity design and prototype (\~8%); documentation and security review (\~5%); reporting (\~8%). Banks and regulators will tell us what must change or be added — those learnings become the published month-4 report, alongside two banks test settling in USDCx on mainnet by month 3.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

From day one: pilot banks and corridor partners engaged — participation agreements signed, register entries and certificates issued, regulator briefings opened. Month 1: USDCx support in the Bank Node treasury wallet and settlement executor (per-corridor choice alongside ADA); records and UI updated; signed Pyth price update persisted per settlement; on-chain Lazer verification designed. Month 2: a two-bank corridor settling USDCx in both directions on preprod with full reconciliation; failure handling and an operations runbook; bank staff trained, running testnet dry runs. Month 3 — mainnet: USDCx net settlement on Cardano mainnet, priced by a Pyth-verified quote, daily on-chain FX attestation running; release notes, deployment docs and security review on the public repo. Evidence per the standard: live product at [apisandbox.openbankproject.com](http://apisandbox.openbankproject.com), mainnet tx hashes mapped to flow steps, declared footprint, demo video, repo tag — at Demo Day.

### Oracles - expected transaction count

20

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### On-chain identity (CIP-0170) - fee target (ADA)

300

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Open Corridor is a payment network for licensed banks, built on the Open Bank Project and Cardano. Each bank runs an OBP Bank Node — a Rust gateway on its own infrastructure, connected to its existing core banking system — and pays other member banks directly. The sending bank anchors a payment promise on Cardano as a salted SHA-256 commitment (no names, amounts or PII on-chain); the receiving bank verifies the payment details against that commitment and credits its customer in seconds; the banks then settle only the netted difference of opposing flows in one on-chain transfer — ADA today, USDCx with this grant — at an FX rate locked from Pyth feeds and recorded for audit. 

The problem: cross-border payments between African banks route through correspondent chains via Western intermediaries — 2–5 days, and the world’s highest fees (Sub-Saharan Africa averages 8.8% on a $200 transfer, against a 3% SDG target), while correspondent withdrawal makes direct rails scarcer every year. 

For whom: African commercial banks, who get a direct, auditable corridor they run themselves; their customers — remitters and businesses trading under AfCFTA — who get payments in seconds at lower cost; and regulators, who get a tamper-proof, independently verifiable trail (promise, price, settlement) instead of one bank’s private records. 

This is a working system: the full flow runs end-to-end against a real cardano-node today, open source under AGPL v3. 

### Supporting links (repo, site, demo)

- https://youtu.be/K_Ck-3_ne0s
- https://github.com/TESOBE/OBP-Bank-Node
- https://github.com/OpenBankProject/OBP-API
- https://www.tesobe.com/
- https://www.openbankproject.com/

### Identified dependencies

Yes

### Good standing

Yes

### Oracles - fee target (ADA)

301

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

AGPLv3 Copyright TESOBE GmbH

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

20

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

361

### Current funded commitments

Members of our team are contributing to [OGCR.eu](https://OGCR.eu) - which is an EU Horizon program (the project uses OBP-API) but we have plenty of capacity and our commitments are not exclusive.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The OC functionality in OBP-API and the OBP Bank Node (Rust; promise anchoring, evidence, settlement via the bank's own cardano-node, bank-held keys) are new code, running the five-step flow end-to-end on Cardano preprod with a web UI used in bank demos — not yet operated inside a bank; this pilot closes that gap. By component: Pyth feed consumption TRL 6; on-chain Pyth Lazer verification TRL 2–3 (approach defined, not yet prototyped); USDCx settlement TRL 3 (the same executor settles ADA end-to-end today; USDCx substitutes the asset); CIP-0170 identity TRL 2 (deliverable: evaluated design and prototype anchoring). Milestones take USDCx and the Pyth verifier to mainnet operation (TRL 7–8) by month 3. Code: [github.com/TESOBE/OBP-Bank-Node](http://github.com/TESOBE/OBP-Bank-Node)
