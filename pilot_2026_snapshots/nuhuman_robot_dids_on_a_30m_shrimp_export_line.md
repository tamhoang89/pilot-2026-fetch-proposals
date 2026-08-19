# nuhuman: Robot DIDs on a $30M Shrimp Export Line

> Every nuhuman robot at Coastal Corporation (NSE: COASTCORP) carries a DID. Every batch of shrimp is stamped on Cardano, QR verifiable by the buyer. Pilot signed for 120+ robotic cells.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1u86sa7qzppfh24sugfdxasm0ye2cqp2f35n82yec06h7xsscfgpd9`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-19T15:03:16.425000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Sricharan Ganta, Founder and CEO, sole named member: <https://www.linkedin.com/in/sricharangm>. Role: architecture, integration delivery, the Coastal relationship, program compliance. 7+ years in business roles, 4+ in web3, MS Computer Science (University of Central Missouri, USA).

Coastal Corporation (NSE: COASTCORP), one of India's largest shrimp processors, is his family's business, where he held business development roles. That is why a robotics startup got a live export line: January pitch, March floor access, June first arm, August a 120+ cell contract. Coastal is named with its written consent (MoU); its sign-offs are its own duties.

Cardano: 13 funded Catalyst projects, F10-F14, 11 delivered, 2 at final milestone \[proposer page URL\]; 1st place, Midnight Hackathon at Rare Evo 2024; live at [app.nucast.io](http://app.nucast.io); code: <https://github.com/Nucastio>.

Physical AI: building since 2025, a year before the first contract: bimanual arm hardware, teleop training, simulation, the DECAP-0 policy, a cell live at Coastal.

Delivery: the Nucast Labs team (<https://www.linkedin.com/company/nucast/people/>) builds under Charan: on-chain contracts, platform, attester flows; engineers named at KYC/KYB.

To recruit: a compliance lawyer for the fractionalization legal pathway, the one gap.

Disclosure: our only submission this round; Charan is on no other proposal in any delivery role. 

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Coastal is our existing customer, \~90% of fees. Auditors and importers give the rest. Signers are new to Cardano.

Why 30 days: six epochs is the shortest window, what we get if M1 lands on the deadline. Entry epoch fees are extra.

Why 20 cells: the MoU names 60 cell pairs. We instrument 20 in the window, starting at 3, so 12 on average.

Why 3 batches a cell a day: the line runs 20 hours, QC releases one per 7.

Why 0.42 ADA a tx: an attestation runs a script and carries metadata. Network average is 0.33, scripts cost more.

CIP-0170: 3 x 12 x 30 = 1,080 QC releases, plus 220 from hygiene, maintenance, dispatch, auditors and importers. 1,300 txs, 546 raw. Coastal pays all its signers, so 6.2 makes it one wallet and halves its share over 35%. Counted 387, target 380.

CIP-0113: 650 mints at 0.50, 520 transfers at 0.45, 200 burns at 0.40. 1,370 txs, 639 raw, 471 counted. Both raw numbers are Ambitious. The 6.2 discount, not caution, makes this Credible.

Why 17 importers: Coastal ships to 13 countries already. With Coastal and two audit firms that is 20, over minimums of 18 and 9. All live before M1.

Nobody is paid to transact. Each company pays its own signers. 

### How will you reach and onboard real users - and what evidence backs your channels?

Our users already work at the plant. The robots replaced the hands that dehead shrimp, not the people who approve the work. Those people are salaried staff: QC officers who release each batch, hygiene and maintenance checkers, dispatch staff who confirm shipments. The signed MoU makes them the signers. Outside the plant: auditors who already visit for BAP and BRCGS, and importers who receive Coastal's shipments. Devi Sea Foods becomes the second site once signed.

Reaching them is simple: our engineers are already inside the plant installing the robots. Setting up a signer is part of installing a cell: a wallet on their phone, keys made on site, one training session, and they sign inside the workflow they follow today. We plan 12 to 20 signer wallets against a minimum of 10, across separate companies, each covering its own signers' costs. First signers go live at Demo Day; auditors and importers join over the window. Most activity will come from our existing customer.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Everyone solving this today digitizes paperwork. Audit firms (SGS, Bureau Veritas) sample paper a few visits a year. Seafood SaaS is established, Trace Register since 2005, ReposiTrak's 30,000-company FSMA 204 network, Wholechain on GDST, but all are databases of what people type, editable by the audited party. IBM Food Trust used a private chain the industry runs. Machine makers (Laitram, Marel) lock machine data in plant systems.

Why we win: the labour which was producing records is disappearing & a robot doesn't fill forms, it emit records. We run robotic cells on a shrimp line where key events signed at source, hashed to Cardano, countersigned by QC.  A cell with a CIP-0170 identity with provable work is an asset, which is what our tokenization test-run builds on. 

### Please provide details about the Technology Readiness Level selected for your existing product

Robot cells dehead shrimp on Coastal's line every shift. On Cardano we are live on Preprod: <https://preprod.nuhuman.ai/#identity>.

Identity is furthest along. The three roles the design rests on exist there as KERI AIDs: Issuer, QC Coastal, Auditor 01. That is the counter-signature triangle: who claims, who releases, and an auditor outside both. CIP-170 authority is complete, records carry their identity state on chain,.

Fractions sit on the same ledger: a CIP-113 directory binds the policy to our issuance and transfer logic, a registry checks signer, uniqueness, entitlement and claim amount, the ledger takes the AND. Issue, transfer, claim, confirmed.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Two layers, one record.

Identity, CIP-0170. Each cell gets a KERI AID at commissioning and posts what it measured that shift: quantity in and out, grade, line, lot. Cell wallets are ours, declared and never counted. The people who approve the work hold their own keys and anchor their own credentials: QC officers, hygiene and maintenance, dispatch, auditors, importers. A batch closes only when an independent signer countersigns the cell's claim. Those counter-signatures are the counted fees, each company paying its own. The triangle already runs on Preprod as AIDs: Issuer, QC Coastal, Auditor 01.

Tokens, CIP-0113. Batch custody moves as a programmable token. A BatchPass mints when QC releases the batch, carries the batch hash, transfers only to a credentialed importer, burns on receipt. Those rules belong on the ledger, not in our server, or the audited party edits them. CIP-113 puts transfer rules at the policy and binds them to identity. That is the reason to use it.

The gates are already confirmed on Preprod: the directory selects the policy, the registry checks signer, uniqueness, entitlement and claim amount, the script checks owner, claimant and scope, the ledger takes the AND. Custody reuses them.

Fit: FSMA 204 wants Key Data Elements for a transformation event, retrievable in 24 hours. Plant data stays in the plant, hashes, DIDs and custody go on chain, and every batch carries a QR to a free public verifier. Checking costs nothing and nobody is paid to transact.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)
- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

The market is shrimp processing. India has 646 registered seafood units, \~420 handling shrimp \[MPEDA registry\]: a $220M serviceable market inside $1.0B of Asian shrimp processing. Of the ten largest Indian shrimp companies, one has signed: Coastal Corporation (NSE: COASTCORP, Rs 639 Cr FY26, 3 Andhra Pradesh plants, 71 MT a day), a 120+ cell contract. Next: Devi Sea Foods (Rs 3,310 Cr FY24, 5x Coastal), in talks.

Why they buy this layer: the robots are already on the line. Coastal bought them to fix labor shortage. Under FSMA 204, deheading is a Critical Tracking Event, transformation, and the machines measure its Key Data Elements every shift: quantity in and out, grade, line, date, lot. Coastal needs it provable to an auditor or importer without opening its books, and buys it as it bought the robots: no capex, per kilo.

On-chain demand has signatures and dates. Coastal signed the traceability pilot: three cells now, sixty cell pairs in the MoU. Regulatory pull: the Food Traceability List covers shrimp as crustaceans, plus finfish, smoked finfish and bivalves \[FDA FTL\]; the rule wants lot codes, KDEs, a 24-hour sortable spreadsheet, enforcement July 2028. Walmart requires KDEs per shipment \[Walmart\]. \
\
The third opportunity is capital: a $2.6M yearly wage line is being replaced by arms costing \~$200 to build. Machines this cheap, earning per kilo, are built for tokenization: the grant test-runs it on mainnet.

### Applicant name

Nucast Pte Ltd

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Who pays: Coastal pays nuhuman a subscription for the traceability layer, per instrumented cell per month, billed on the same invoice as deheading. The robots earn per kilo; the record earns per cell. Network fees are an operating cost of the service: each entity covers the negligible gas its own signers use, Coastal for its QC officers, auditors and importers for theirs. 

Why usage persists: batches close every day the line runs, 20 hours a day. Attestations happen because shrimp gets processed. Every new cell in the 120+ contract adds a DID and a stream; the MoU names sixty cell pairs. After the window nothing changes: the subscription keeps billing, QC keeps signing, and FSMA enforcement in July 2028 is still ahead. The activity does not stop when the measurement does.

Tokenization adds the future line: issuance and transfer fees on cell fractions once we have a legal pathway.

### Programmable tokens (CIP-0113) - expected transaction count

1370

### On-chain identity (CIP-0170) - expected transaction count

1300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Coastal pays us for records it can show an auditor. A database satisfies that bill, and is cheaper. Nobody pays for what makes a record worth trusting: a QC officer holding their own key rather than a login we issue, rules the audited party cannot edit, a verifier an importer opens without asking us. Preprod proves it works. The grant puts it on mainnet, held by people who do not work for us.

Spend, 150,000 ADA\
CIP-0170 cell AIDs, credentials, counter-signature flows: 45,000\
CIP-0113 BatchPass policy, transfer and burn rules: 35,000\
Signer onboarding, wallets, key ceremonies: 25,000\
Public verifier, QR resolution, MIT SDK: 20,000\
Mainnet deployment, security review, Demo Day: 15,000\
Counsel on the fractionalization pathway: 10,000

The Preprod build was unfunded. 

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Live on Cardano mainnet by M1, demonstrated at Demo Day.

1. CIP-0170: KERI AIDs anchored for the issuer, each cell at commissioning, and each signer role. A batch closes only when a signer outside nuhuman countersigns the claim.
2. CIP-0113: BatchPass policy deployed. Mint at QC release carrying the batch hash, transfer only to credentialed parties, burn on receipt.
3. Live product: cell registry, batch console, signer onboarding with key ceremony and credentials. Each batch carries a QR to a free verifier.
4. Declared footprint published: policy IDs, script hashes, addresses, token names, message tag and our own wallets, all newly deployed.
5. At least three independent runs of the flow on mainnet: QC release, counter-signature, mint, transfer, and one cycle closed by burn on receipt. Hashes mapped to steps.
6. At least three signers live outside nuhuman, holding their own keys and paying their own fees.
7. Release notes, walkthrough video, MIT repo tag, test bundle.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### Programmable tokens (CIP-0113) - fee target (ADA)

470

### On-chain identity (CIP-0170) - fee target (ADA)

380

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

A kilo of shrimp leaves Andhra Pradesh for a shelf in Texas or Rotterdam. It is deheaded, frozen, packed and shipped, and every step must be recorded: that record is what HACCP, BRCGS and import rules are. Today it is paper, easy to fake, costly to audit, slow in a recall. The bar is rising: FSMA 204 puts shrimp on the FDA's Food Traceability List, demanding a lot code on every lot, Key Data Elements at every Critical Tracking Event, and a sortable spreadsheet in 24 hours, foreign firms included.

nuhuman has been building physical AI since 2025. We built a bimanual arm that deheads shrimp and won our first contract: 120+ cells with Coastal Corporation (NSE: COASTCORP), one of India's largest shrimp processors, live today. Under the rule, deheading is a Critical Tracking Event, transformation, and the robot writes its Key Data Elements by working: quantity in and out, which is yield, grade, line and lot, stamped to the second, plus the cleaning log HACCP demands. No form filled by hand.

This grant makes the record impossible to rewrite. Every cell gets a CIP-0170 identity on Cardano, each lot fingerprinted against it, on a chain nobody can edit, us included. The data stays private; only the proof is public. QC signs every batch from their own wallet; each pack carries a QR: scan it, verify nothing changed. Paper asks for trust. This can be checked by anyone. Identity is step one: the grant also test-runs fractional ownership of the robots on mainnet, mapping the legal path.

### Supporting links (repo, site, demo)

- https://www.nuhuman.ai/
- https://preprod.nuhuman.ai/
- https://youtu.be/9z0eHF5j4ek
- https://drive.google.com/file/d/1WRGmgp0oYAi1FlbSB5uSq7lpi_bCX1C5/view?usp=sharing

### Identified dependencies

Yes

### Good standing

Yes

### Business

Yes

### Is your team (or any members of) currently delivering any funded commitment, in any ecosystem or program?

Yes

### Mature product

Yes

### Licensing / IP details

Yes for the on-chain layer (attestation tooling, batch registry contracts if any, verifier, SDK) under MIT. The DECAP-0 robot control stack stays proprietary. 

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Current funded commitments

Yes. Two Catalyst projects are at their final milestone, both under this same proposer account:

1\. IndiaCodeX '26 (project 1400070), India's largest Cardano hackathon: event delivered, final milestone reporting in progress, expected to close \[month\].\
2. Nucast: Music Video Festival 2026 (project 1400087): final milestone in progress, expected to close \[month\].

Eleven earlier Catalyst projects funded to this team are fully delivered \[proposer page\]. No other grant, treasury, accelerator or program commitment is being delivered by the team in any ecosystem.

Neither open project overlaps this proposal in scope, budget or deliverables. Both are event and creative programs whose remaining work is reporting, not engineering, so they take no build capacity from this integration. nuhuman's private equity fundraise is separate commercial funding and does not pay for any deliverable in this proposal.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Preprod only today. The counter-signature triangle exists there as AIDs, Issuer, QC Coastal and Auditor 01, CIP-170 authority complete. Nothing declared is on mainnet.

What the grant adds:\
Mainnet policy IDs and AIDs, newly deployed and declared at M1.\
Cell AIDs anchored at commissioning, each cell wallet posting its shift record, declared & uncounted.\
Real signers in place of test AIDs, holding their own keys & paying their own fees: QC, hygiene, maintenance, dispatch, auditors and importers.\
The gate: a batch closes only when an independent signer countersigns the cell's claim.\
BatchPass, a custody token minting on QC release, moving only to a credentialed importer, burning on receipt.\
A free public verifier behind a QR on every batch.\
Fractions stay gated tests, pending counsel.
