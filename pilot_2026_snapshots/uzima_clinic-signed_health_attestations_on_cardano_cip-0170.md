# Uzima Clinic-Signed Health Attestations on Cardano: CIP-0170

> A Cardano trust layer for African health data: 2,581 record hashes anchored on preprod, sensitive data off chain. This grant has clinics generate their own CIP-0170 keys, sign and pay on mainnet.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 44
- **Proposer:** `stake1uxy8uagayul3nmm7qmzl4tu9g7z37vdrdwmmrr8cv7fdn5gzyjywq`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T16:20:03.393000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

UzimaNexus combines healthcare domain expertise, software engineering, blockchain experience and an existing deployed healthcare platform. [**Prudence Ibila, CEO**](https://www.linkedin.com/in/ibila-prudence26/), leads product strategy, healthcare partnerships, user validation and business development. [**Alvin Maase, CTO**](https://www.linkedin.com/in/alvin-m-b3b968180/), leads the technical architecture and implementation. Our technical team has already built healthcare and enterprise software and understands the interoperability, security and workflow requirements of real-world health systems.

UzimaNexus is not starting from an idea. We have an existing healthcare platform with **1,530+ patients, 10+ specialists and a 500+ clinic pipeline valued at over $1M**, providing an existing environment in which to validate the proposed integration.

We were also part of the [**Techstars + Cardano Founder Catalyst Program**](https://www.techstars.com/blog/program-news/introducing-the-2025-techstars-cardano-founder-catalyst-cohort), giving the team direct exposure to Cardano ecosystem expertise and founder-focused guidance.

Our technical consulting partner, [**Le-Bumba Technologies**](https://www.lebumbatech.com), on retainer, provides additional software engineering and infrastructure capability. Together, we have the domain knowledge, technical capacity, existing users, and ecosystem exposure required for full intergration.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

WHO: the clinic, not UzimaNexus. At shift close the nurse in-charge signs one attestation over that shift set of record hashes, anchoring its key event log under CIP-0170. UziAttest, a container it runs, generates its own KERI AID and Cardano keys on clinic hardware, never sent to us, and the clinic pays every mainnet fee from its own wallet. We cannot sign or pay for it, so no script over our wallets reproduces this. No reward, rebate, points or subsidy.

WHY: obligations they already carry: SHA claim substantiation, donor audit at faith-based and NGO clinics, Data Protection Act records.

HOW OFTEN: two shift closes a day, with or without Cardano.

TARGET: 500 waitlisted, 100 targeted, 25 converted, one key pair each = 25 separately funded external stake keys, 2.5x the 10-wallet gate, clearing at 10 of 40. 25 x 60 = 1500 attestations over 30 days, at 0.367 = 550 ADA, tracking 0.363 tADA measured across 146 operator-signed PREPROD anchors (readiness, not footprint; mainnet at M1 inside 3 months, early to earn epochs). Ambitious band, 5.5x the 100 floor. 22 ADA per clinic, a lab reagent. No facility tops 4 percent, no day tops 3.

### How will you reach and onboard real users - and what evidence backs your channels?

We will use direct B2B healthcare sales, our existing provider pipeline, partnerships and our deployed patient platform to onboard users. Our strongest evidence is existing traction: **500+ clinics on our waitlist representing a $1M+ pipeline, 1,530+ patients and 10+ specialists**, alongside an already deployed patient prototype.

We will first onboard selected clinics, diagnostic providers and specialists from this existing pipeline. Providers will access the Cardano functionality through APIs and familiar UzimaNexus workflows rather than replacing their existing systems. Patients will be onboarded through our existing mobile experience and consent flows.

We will measure onboarding conversion, active providers, patients using consent, records anchored, verification events and repeat usage. Feedback from early users will guide iteration before broader deployment.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/q5K6wKOwZcQ?si=5OnAdKWk4iwJs_Ag

### Who else solves this today - competitors/alternatives, and why does your approach win?

KenyaEMR (OpenMRS distribution) and DHIS2 (HISP UiO, national in Kenya since 2011) are record systems: they store and report, with no proof checkable without trusting the operator. AfyaRekod markets blockchain-secured patient-owned records on a vendor-run chain: the vendor attests. Credential stacks like Hyperledger Identus solve exchange, not the audit question: which clinic key held authority at signing time, after staff turnover. A plain CIP-10 anchor fails once that key rotates. KERI answers it: key event log, pre-rotation, duplicity detection, and CIP-0170 orders them on a ledger no participant controls (see Reeve, Cardano Foundation). Consent revocation is funded work, not built. Shipped: 2,581 record hashes anchored on PREPROD across 146 transactions; mainnet at Milestone 1.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 7 covers the existing product, on production operation rather than on mainnet: UzimaNexus is deployed and in clinical use in Kenya, serving 1,530+ patients, holding 2,581 medical records, on Django, Celery and Postgres.

The Cardano integration sits lower and is declared separately at TRL 5. All chain activity to date is PREPROD, verifiable via Koios: [2,581 of 2,581 record hashes anchored](https://l1nq.com/e6x5s64) across 146 PREPROD transactions, so chain and database reconcile exactly.

All 146 PREPROD anchors were operator signed, so they are readiness evidence, not adoption, and cannot be declared footprint. The integration reaches TRL 7, live on Cardano mainnet with real transactions, at Milestone 1 within 3 months of selection.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Layers: 1) Clinical data stays in Postgres; metadata carries only hashes and identifiers (storage_location=database), nothing clinical on chain. 2) Each clinic runs UziAttest in its own environment, generating its KERI AID and Cardano payment keys on clinic hardware, never sent to us. Per shift the clinic signs an attestation over the encounter hashes for that shift, paying the mainnet fee from its own wallet. 3) CIP-0170 anchors that clinic key event log (KEL), inception, pre-rotated rotations and witness receipts, under a newly registered CIP-10 message tag.

Fit: an anchor signed by a clinic key stops verifying once that key rotates or leaks: nothing proves it held authority when it signed. The KEL and pre-rotation supply that history, duplicity detection catches conflicting logs, and Cardano orders them in a ledger no participant controls. Funded consent revocation needs the same ordering: proof it followed the grant it revokes. SHA/NHIF claims, donor audit and the Kenya DPA need old attestations to verify after turnover.

Disclosure: 2,581 record hashes across 146 PREPROD transactions sit under squatted CIP-25 label 721; funded work moves them to a newly registered tag on mainnet at Milestone 1. Operator signed, clinics sign and pay.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

Our primary market is **healthcare facilities, diagnostic providers, pharmacies, insurers and patients across Africa**, beginning with Kenya and East Africa. Our strongest initial customers are healthcare providers that need interoperable records, faster referrals, secure data exchange and better patient continuity of care.

We already have evidence of demand rather than relying only on market forecasts. UzimaNexus has **500+ clinics on its waitlist, representing a pipeline valued at over $1M, 1,530+ patients, and 10+ specialists**. We have also processed approximately **$75K in transactions** and deployed a [patient-facing prototype](https://uzimanexus.com/my-doktari).

Our existing product addresses problems providers already experience: fragmented records, lack of transparency, limited access to specialists and inefficient workflows. The platform provides encrypted data sharing, smart referrals, interoperability and blockchain-backed data infrastructure.

This existing user base, pipeline and operational experience provide early evidence of product-market demand. The Cardano project extends this validated healthcare platform with a dedicated, reusable **health-data trust and consent layer**.

### Applicant name

UzimaNexus

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

UzimaNexus operates primarily as a B2B healthcare technology business. Healthcare facilities pay recurring annual subscriptions and a one-time onboarding fee for access to our platform. Future revenue streams include commissions, government contracts, wearable/smart-card sales and on-chain transaction fees.

The Cardano grant funds build and validation, not operations. After the pilot, the capability becomes part of our existing commercial platform and can be offered to providers through our subscription and API services. Usage continues because providers have recurring needs for secure record exchange, verification, referrals and consent management. Our existing traction—including **$4,615+ ARR and a 500+ clinic pipeline valued at $1M+**—provides evidence of commercial demand and a foundation for sustainability beyond the grant.

### On-chain identity (CIP-0170) - expected transaction count

1500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Nothing clinic signed reaches Cardano today: in the repo, did_service submits nothing. Basis: 22 days/pm, senior backend Nairobi USD 116.50/day, ADA at USD 0.179, so 14,300 ADA/pm; 9.0 pm build labour. Of 200,000 ADA: KERI agent, KEL, pre-rotation, 3 witnesses 35,750 (2.5 pm); UziAttest container, keys generated on clinic hardware 35,750 (2.5); signify sidecar, newly registered message tag 21,450 (1.5); delete platform derived keys, replace mocked DID, verifier CLI 21,450 (1.5); mainnet cutover, live M1 demo 14,300 (1.0); security review 22,000 (20 days, USD 197); onboarding 25 clinics that pay own fees 25,000; hosting, docs, contingency 24,300. Target 550 ADA over about 1,500 clinic attestations.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Live on Cardano mainnet, demonstrated live inside 3 months; cutover month 2 to earn epochs.

1 Registered CIP-10 message tag: merged registry PR and first mainnet tx carrying it, replacing squatted labels 721 and 674.

2 Footprint file at a fixed commit: mainnet AID prefixes and anchor addresses created after selection, plus operator stake keys; nothing preprod declared.

3 UziAttest image tag, sha256 digest and keygen runbook: each clinic generates its own KERI AID and payment keys on its own hardware and pays its own fee.

4 KEL, pre-rotation, 3 witnesses: inception and rotation tx hashes, witness endpoints, duplicity vectors.

5 Verifier CLI checking an attestation from a tx hash alone; diffs deleting generate_wallet_from_seed and the mocked DID anchor.

6 25 of 100 clinics signing per shift, 25 external stake keys vs the 10 gate, 1,500 attestations, 550 ADA clinic-paid.

7 Third-party security review with remediation commits.

Demo: inception, rotation, attestation still verifying.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

550

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

UzimaNexus is building a **Cardano-powered health data trust and consent layer** that allows healthcare providers to verify the authenticity and provenance of clinical records while giving patients greater control over who can access and share their information.

Today, health records across Africa are fragmented across hospitals, laboratories, imaging centres and insurers. Patients often carry paper records or send documents through insecure channels, while providers have limited ability to verify whether a record has been altered or is authentic. This contributes to repeated tests, delayed referrals, fraud, administrative costs and poor continuity of care.

Our solution keeps sensitive medical data **off-chain** while anchoring cryptographic proofs of records on Cardano. Providers can verify that a record has not been altered and where it originated. Patients can use a consent layer to authorize, limit or revoke access to their records.

The primary beneficiaries are **patients, healthcare providers, diagnostic centres and insurers**, particularly in African markets where health-information systems remain fragmented.

The prototype will demonstrate a practical bridge between existing healthcare systems and Cardano, turning the blockchain into a verifiable trust layer for real-world healthcare data without exposing sensitive patient information on-chain.

### Supporting links (repo, site, demo)

- https://uzimanexus.com/blog/uzimanexus-joins-techstars-cardano-founder-catalyst-2025
- https://uzimanexus.com/UzimaNexus-Consultvrse-Demo-Video.mp4
- https://preprod.cardanoscan.io/address/addr_test1qrxjggksr6f9x9nm7r42fgdyy538kz62umlvwccje2anyjgt62g59qkncsz5ka54z2ekpj0ux8laz5a8k8nlhkhd0z9qf6g6w4
- https://preprod.cardanoscan.io/transaction/29e2ada7be36b31a314bd255a4516865639bb0243111af90d00c7fa4436d51d5
- https://uzimanexus.com

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

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 5 today, TRL 7 live on Cardano mainnet at Milestone 1, within 3 months of selection.

Working now: the sign, submit, confirm pipeline. 2,581 record hashes, covering all [2,581 production records](https://l1nq.com/e6x5s64), are anchored across 146 PREPROD transactions in 7 epochs, 18 May to 19 Aug 2026, for 53.00 tADA, 0.363 per transaction, which sizes the declared target; all operator signed on PREPROD, so this is readiness for mainnet at Milestone 1, not adoption.

Greenfield: no keripy, signify-ts, KERIA or CESR in the repo, so the KERI stack is new; did-service returns a placeholder; metadata sits under label 721; platform derived keys get deleted. Preprod is staging, never the deliverable, which is clinic signed on mainnet in production.
