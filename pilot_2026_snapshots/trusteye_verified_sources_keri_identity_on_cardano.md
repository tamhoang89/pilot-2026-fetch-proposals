# TrustEye Verified Sources: KERI Identity on Cardano

> Hardware-signed camera evidence gets an accountable source: organizations publish wallet-paid CIP-0170 attestations on Cardano so anyone can verify who authorized a capture, on which device, and when.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 30
- **Proposer:** `stake1u80xxjl5pktq7fyeh46f2mwnzvjhjafmsdzv0hq3hxzc9kq6vwzsx`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-23T19:46:54.399000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

Marius Georgescu — individual lead applicant; CIP-0170/KERI architecture, Cardano transaction and wallet flows, backend/infrastructure, measurement, and Catalyst reporting. Doctor of Engineering, solution architect with 10+ years across banking, fintech, and telecom; EMURGO Academy Cardano Solution Architect; first Plutus Pioneers cohort. LinkedIn: [linkedin.com/in/georgescumarius](https://linkedin.com/in/georgescumarius)   · GitHub: [github.com/mariusgeorgescu](https://github.com/mariusgeorgescu)  · Catalyst: [projectcatalyst.io/proposers/georgescumarius](https://projectcatalyst.io/proposers/georgescumarius) \
\
Andrei Georgescu — named participant and co-proposer; TrustEye product, mobile integration, device-authorization model, evidence/verifier changes, testing, pilot UX. Machine-learning and computer-vision engineer with 10+ years in distributed systems and image-processing pipelines; MSc in AI; three patent publications. LinkedIn: [linkedin.com/in/andreigeorgescoo](https://linkedin.com/in/andreigeorgescoo)  · GitHub: [github.com/androclassic](https://github.com/androclassic)\
\
Delivery evidence: TrustEye itself — live on iOS and Android with a public verifier, built and self-funded by this team; one adjacent sponsored Preprod transaction that implements no CIP-0170 lifecycle (disclosed, excluded from budget); three completed Catalyst projects (Fund 10 dApp documentation, 20k; CardanoTicker, 15k; BJJ Belt System, 40k). No additional hires are needed for this scope.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary pledge: once cumulative TrustEye revenue directly attributable to the Cardano higher-assurance organizational plan (subscriptions that include the CIP-0170 accountable-source feature) exceeds 50k ADA-equivalent, we will share 10% of further attributable revenue with the Cardano treasury, paid annually for three years from M1, up to a cumulative cap equal to the full 50k ADA grant. 

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Only valid CIP-0170 ATTESTs for completed evidence packages enter the forecast. Each VSA binds the evidence digest, organization credential, valid device interval and signed capture-time claim; label-170 d digests the canonical label-70170 value and must match its KEL seal. An earlier valid AUTH_BEGIN is required. AUTH_BEGIN, AUTH_END, setup, tests, team-paid and sponsored transactions are excluded.

Declared target: 100 ADA. Hypothesis: 360 qualifying ATTESTs yield 118.8-144 ADA gross at the Standard's 0.33-0.40 sanity range; operational buffer aims for ≥110 counted ADA after exclusions. Planning case: 8 independent organizations ×45 completed packages, about 10-11 per week in the minimum window. Eight wallets exceed the 5-wallet minimum; no day may exceed 20%, and no source may breach concentration.

Evidence today: 0 organizations, 0 ATTEST and 0 ADA—no commitments, conversion, repeat-use or measured fee baseline. Acquisition goals are 80 contacts→24 discovery calls→12 wallet sessions→8 activations; these are future hypotheses, not traction. External wallets self-pay. We publish funnel and shortfall; no subsidies, rebates or transaction incentives.

### How will you reach and onboard real users - and what evidence backs your channels?

Evidence today: zero committed organizations, conversion baseline or measured VSA fee. Acquisition objectives—not traction—are 80 qualified contacts, 24 discovery calls and 12 wallet-readiness sessions before M1, seeking 8 activations. An organization activates only after onboarding, control of its AIDs, an independent wallet, valid AUTH_BEGIN and first self-paid VSA.

Cumulative post-M1 KPIs: Week 1—3 organizations, 3 wallets, 3 AUTH_BEGIN, 30 completed packages→30 ATTEST/transactions and ≥9 ADA gross eligible; Week 2—6 organizations, 6 wallets, 6 AUTH_BEGIN, 90 packages→90 ATTEST/transactions and ≥27 ADA. Week-1 fees remain provisional until the ≥5-wallet rule. AUTH_END is zero unless genuine; a test identity covers revocation without counting. Failed journeys are reviewed within 24 hours; funnel and shortfalls are public. Nobody is paid or reimbursed for transacting.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/shorts/rCgtSUh670s

### Who else solves this today - competitors/alternatives, and why does your approach win?

C2PA Content Credentials is the main open provenance standard; we complement it with a Cardano record of organizational signing authority. Truepic Vision shows enterprise demand for capture integrity, but verification depends on its platform. TrustEye's chain, KEL and credential proofs will be independently checkable; under our SME profile, organization assurance remains rooted in TrustEye's onboarding policy and the verifier will display that trust anchor. Numbers Protocol offers broader Web3 provenance; we focus on organization-to-device authority for operational review. A plain hash/timestamp proves that data existed, not which credentialed organization authorized its source.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 8 for the existing product, not the proposed integration: TrustEye is deployed on iOS ( <https://apps.apple.com/app/trusteye/id6784402834>  ) and Android ( <https://play.google.com/store/apps/details?id=io.trusteye.app> ), with a public site and photo verifier at trusteye.io; web video verification, team billing and API access are roadmap items. The applicant reports SHA-256 binding, tamper-evident chains, hardware-backed ECDSA P-256 device signatures, platform-attestation signals, public-chain timestamps and exportable bundles. Store and verifier links evidence deployment; reviewer-accessible artifacts must support deeper implementation claims. No active-user, organization, customer or revenue figure is claimed.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The funded work will implement Proposed CIP-0170 v1.0 as a disclosed non-vLEI TrustEye Organization profile. Verifiers pin its Root AID. Chain: Root issues issuer-authority ACDC to TrustEye's issuer AID; issuer issues Organization ACDC to a participant AID; organization issues custom Metadata Signer ACDC to its signing AID. The leaf binds issuee, organization edge and labels:\[70170\], a CIP-10 private-use label; relevant registries are published. TrustEye controls root/issuer; participant controls organization/signer through Signify/KERIA. TrustEye's onboarding/issuance/revocation policy—not Cardano or vLEI—defines assurance.

Persistent OOBIs plus watchers/mirrors discover every KEL; OOBIs are untrusted locators, so events/ACDCs verify cryptographically. AUTH_BEGIN carries i/s/c/v: i=leaf issuee, s=leaf schema SAID, c=complete credential/registry/attachment stream, v=CIP1.0/KERI10/ACDC10; label 70170 must be authorized. Each VSA ATTEST uses BLAKE3-256/CESR-E over RFC8949 deterministic CBOR for the exact label-70170 value, sealed in the signer KEL at sequence s; verifier matches both. A separate external wallet signs/submits/pays. AUTH_END carries matching i/s/c/v; c contains valid revocation-registry events, ending future authority. Prior ATTESTs and ordinary rotation remain valid. Tests freeze bytes, qb2 chunking, size and fee. Only valid external-paid ATTEST fees count.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Initial target: small and medium inspection, adjusting and field-audit teams whose evidence is reviewed by third parties; the buyer is an administrator or compliance lead.\
\
Evidence ledger. Committed: zero pilot organizations or external wallets. Historical: TrustEye is live on iOS, Android and a photo web verifier, but has no measured organization-to-Cardano conversion, repeat-use or VSA-fee baseline; team billing and API access are roadmap. Truepic shows category demand, not demand for this integration. CIP-0170 remains Proposed; Reeve and Veridian show a technical reference path, not adoption of TrustEye's profile.\
\
Acquisition is therefore a hypothesis, not traction. Before M1 we will use TrustEye's app/site and direct inspector, adjuster, insurer, auto and fleet outreach to contact 80 qualified organizations, target 24 discovery calls and 12 wallet-readiness sessions, and seek 8 activations. Qualification requires a recurring evidence workflow, accountable administrator, independent Cardano wallet and self-payment. These are future process goals with no historical conversion basis; no company is claimed as a partner. We will publish denominators, activation, retention and shortfalls and never manufacture usage. 

### Applicant name

Marius Georgescu

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

TrustEye sells consumer seal packs; team billing and API access are roadmap items, and no revenue figure is claimed. If validated, Cardano will become a paid higher-assurance organizational add-on: customers pay TrustEye for workflow access and use their own external wallets to pay genuine VSA ATTEST fees. The grant never pays those fees. Counted recurring demand can come only from completed evidence packages, not setup, key rotation, authority/device lifecycle events or revocation. We will test willingness to pay through activated organizations, retention and self-paid transaction records; none exists today for this feature. The integration and verifier will remain available after the Pilot. Cryptographic checks will be reproducible while organization assurance will depend on TrustEye's disclosed policy and continued KEL availability.

### On-chain identity (CIP-0170) - expected transaction count

360

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

50,000 ADA funds future fixed-output WPs; team absorbs overruns and routine infra in-kind. WP1 W1-2, Marius, 7k: published root/profile, AIDs, schemas/SAIDs, registries/OOBIs and vectors. WP2 W3-5, Marius, 10k: Preprod lifecycle/rotation traces and external-wallet round-trip. WP3 W5-8, both, 11k: indexer/backend/verifier integration tests. WP4 W8-12, both, 7k: threat report, mainnet organization flow, tx IDs/demo and Apache repo. WP5 M1→close, both, 10k: onboarding/runbooks, support/telemetry, W1/W2 actuals and completion report. WP6 M1→close, both, 5k: measurement-window operations, reproducibility and handover. Total 50k. Fixed amounts are accepted by public artifacts, tests, tx IDs and logs, not timesheets; separate from 40/40/20 payments. No prior work, fees, subsidies or re-granting.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By W12 (target W9): 

1. publish root/issuer AIDs, custody/onboarding/issuance/revocation policy, schema SAIDs, registries, label 70170, OOBIs/KEL mirrors and version profile; 
2. publish VSA bytes/digest vectors, AUTH_BEGIN qb2 framing/chunking, size, fee and wallet/indexer round-trip; 
3. ship a KERI10/ACDC10 authority verifier; 
4. publish Preprod trace: pre-AUTH ATTEST rejected; AUTH_BEGIN→ATTEST accepted; rotation valid; AUTH_END revocation→later ATTEST rejected; fresh chain/AUTH_BEGIN restores authority; 
5. on mainnet, onboard a consenting organization and publish AUTH_BEGIN plus ≥2 repeatable VSA ATTEST runs paid by its independent wallet; 
6. demo organization/device authority interval, content/digest, signed capture-time and Cardano publication time; 
7. publish tx IDs, release notes, runbooks and dashboard separating lifecycle overhead from countable ATTEST fees; 
8. release schemas, vectors and verifier adapter at github.com/en7angled/trusteye-cip170 under Apache-2.0.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

100

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

TrustEye is a production camera and verification app, live on iOS and Android. A hardware-backed device key signs capture bytes and the app preserves a tamper-evident proof chain; the public web verifier checks sealed photos. It proves provenance and integrity, not scene truth.\
\
A device signature does not establish which accountable organization controlled that device at capture. Today that relationship is not independently verifiable, so field-inspection and evidence-collection reviewers must rely on our service. They need an auditable organization→operator/device→evidence chain.\
\
The funded work will create that layer under a disclosed TrustEye Organization profile. Before any VSA, a valid CIP-0170 AUTH_BEGIN will publish the complete ACDC/registry stream and grant a KERI signing AID authority over label 70170. That AID will anchor the deterministic VSA-payload digest in its KEL; a separate external Cardano wallet will sign, submit and pay for each ATTEST. The payload will bind organization credential, the device-authorization interval valid at capture, evidence digest and signed capture-time claim. Cardano proves publication time, not capture time by itself. The verifier will check the pinned root policy, chain, authority interval, authorized label, KEL seal, device signature and content. A valid AUTH_END revocation ends future authority; earlier valid attestations remain valid. Organization assurance will depend on TrustEye's published onboarding and issuance policy.

### Supporting links (repo, site, demo)

- https://trusteye.io
- https://apps.apple.com/app/trusteye/id6784402834
- https://play.google.com/store/apps/details?id=io.trusteye.app
- https://e7d.tech/
- https://projectcatalyst.io/proposers/georgescumarius

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

TRL 2: the selected CIP-0170 integration is a formulated architecture, not an experimental proof of concept. No existing build demonstrates its defining path: ACDC credential chain, AUTH_BEGIN, KEL-anchored ATTEST, AUTH_END, verification, and external-wallet payment. A private branch did produce a sponsored Preprod Cardano transaction (ac02d2ae0386d6dbc4e06a458e018720338de1b14418e8dc573c550f615696d9), plus validator/relay/Mithril experiments; these are adjacent Cardano feasibility evidence only and do not raise the integration TRL. Baselines bd6f41ef and d14e7d99 exclude prior work from funding.
