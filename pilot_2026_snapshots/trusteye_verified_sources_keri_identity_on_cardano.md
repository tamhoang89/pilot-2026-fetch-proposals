# TrustEye Verified Sources: KERI Identity on Cardano

> Hardware-signed camera evidence gets an accountable source: organizations publish wallet-paid CIP-0170 attestations on Cardano so anyone can verify who authorized a capture, on which device, and when.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 21
- **Proposer:** `stake1u80xxjl5pktq7fyeh46f2mwnzvjhjafmsdzv0hq3hxzc9kq6vwzsx`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-21T21:25:37.889000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

Marius Georgescu — individual lead applicant; CIP-0170/KERI architecture, Cardano transaction and wallet flows, backend/infrastructure, measurement, and Catalyst reporting. Doctor of Engineering, solution architect with 10+ years across banking, fintech, and telecom; EMURGO Academy Cardano Solution Architect; first Plutus Pioneers cohort. LinkedIn: [linkedin.com/in/georgescumarius](https://linkedin.com/in/georgescumarius)  · GitHub: [github.com/mariusgeorgescu](https://github.com/mariusgeorgescu)  · Catalyst: [projectcatalyst.io/proposers/georgescumarius](https://projectcatalyst.io/proposers/georgescumarius) \
\
Andrei Georgescu — named participant and co-proposer; TrustEye product, mobile integration, device-authorization model, evidence/verifier changes, testing, pilot UX. Machine-learning and computer-vision engineer with 10+ years in distributed systems and image-processing pipelines; MSc in AI; three patent publications. LinkedIn: [linkedin.com/in/andreigeorgescoo](https://linkedin.com/in/andreigeorgescoo)  · GitHub: [github.com/androclassic](https://github.com/androclassic)\
\
Delivery evidence: TrustEye itself — live on iOS and Android with a public verifier, built and self-funded by this team; a working pre-production Cardano prototype (disclosed, excluded from budget); three completed Catalyst projects (Fund 10 dApp documentation, 20k; CardanoTicker, 15k; BJJ Belt System, 40k). No additional hires are needed for this scope.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Voluntary pledge: once cumulative TrustEye revenue directly attributable to the Cardano higher-assurance organizational plan (subscriptions that include the CIP-0170 accountable-source feature) exceeds 50k ADA-equivalent, we will share 10% of further attributable revenue with the Cardano treasury, paid annually for three years from M1, up to a cumulative cap equal to the full 50k ADA grant. 

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: organization administrators, from their own wallets. Cadence: a one-time onboarding footprint per organization (AUTH_BEGIN plus ATTESTed device enrollments - 5-10 tx), then one ATTEST per completed evidence package or inspection batch - roughly 4-6 per active organization per week, following case flow. Scale check (ASF, H1 2025): Romanian RCA insurers paid 2.8bn lei at \~11,172 lei per file - \~250,000 claim files in six months, \~1,000 per working day; 4-6 per week per organization is a sliver of a small adjuster's caseload. Model: 6-10 independent organizations (program minimum 5 wallets) averaging 30-50 qualifying tx each: \~300 transactions producing 99-120 ADA gross at 0.33-0.40 ADA/tx against the declared 100 ADA target (floor 50). Conversion: \~25-35 outreach starts, base case needs one in four to six, \~1 organization onboarded per week across the \~9-week pre-M1 runway. Sensitivity: base 6 organizations × \~50; success 8-10 × 30-40; below 6 we treat the target as at risk rather than manufacture volume. The target sits deliberately in the Credible band; zero organizations are committed today. Team-paid, sponsored, or incentivized transactions never count.

### How will you reach and onboard real users - and what evidence backs your channels?

Named channels, not a generic plan (no commitments claimed): 

1. direct contacts at Romanian insurers and banks from the lead applicant's fintech career — 3-5; 
2. loss-adjusting and inspection vendors serving those insurers, via warm referrals — 5-8; 
3. Flip.ro and eMAG Buy-Back — condition-photo intake workflows; 
4. auto trade-in/remarketing dealers in the Autovit/OLX ecosystem — 10-15; 
5. equipment-leasing and fleet operators from the same network — 3-5.

 Roughly 25-35 outreach starts for 6-10 active organizations (one conversion in four to six), worked across the \~9-week pre-M1 runway; written pilot intents are the current top priority. Onboarding: ten-minute administrator flow, wallet setup and self-payment guidance, lifecycle playbooks, public dashboard. First two weeks after M1: onboarding sessions, first attestations from each active workflow, 24-hour review of failed wallet journeys, published transaction list and counting methodology, one public technical demonstration.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/shorts/rCgtSUh670s

### Who else solves this today - competitors/alternatives, and why does your approach win?

C2PA Content Credentials: the principal open provenance standard; it separates machine identity from organizational identity. We stay interoperable rather than compete — our differentiation is a durable, independently queryable Cardano identity and authorization history joined to hardware-backed capture evidence. Truepic Vision: proves enterprises pay for capture integrity, but verification runs through its platform; we add user-controlled organizational identity and a public Cardano trail verifiable without any vendor. Numbers Protocol Capture: broader Web3 provenance suite; we are narrower — organization-to-device authority chains for operational and legal review. Plain hash/timestamp anchoring: proves a digest existed, not who authorized the device — that gap is our commercial feature.

### Please provide details about the Technology Readiness Level selected for your existing product

TRL 8: a complete system deployed in production and distributed through both major app stores — [iOS](https://apps.apple.com/app/trusteye/id6784402834) and [Android](https://play.google.com/store/apps/details?id=io.trusteye.app) — with a public website and verifier at <https://trusteye.io> . \
The production system combines photo/video capture, SHA-256 content binding, a tamper-evident evidence chain, ECDSA P-256 signatures from a device-held hardware-backed key, Apple App Attest and Android platform attestation, public-chain timestamp anchoring, and an exportable evidence bundle checkable independently of the device. An operational B2B layer provides organization records, API keys, and reporting. This states technical readiness; no active-user or revenue figure is claimed.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The integration implements the merged CIP-0170 specification end to end (metadata label 170). Authority first: per organization, an AUTH_BEGIN transaction — signed and paid from its own wallet — publishes the ACDC credential chain establishing why its KERI identifier holds signing authority. Two declared chain profiles: a vLEI chain (GLEIF root → Qualified Issuer → Legal Entity vLEI → metadata signer) where the organization holds one, and a published bootstrap profile for SMEs — an ACDC chain rooted in a TrustEye-published root AID (OOBI and schemas on trusteye.io), issued after KYB checks: the organization's legal name and registry number are bound into the leaf credential and displayed by the verifier, which also shows which root anchors each attestation. Each Verified Source Attestation is a CIP-0170 ATTEST: the evidence-bundle digest anchored in the organization's Key Event Log, valid while AUTH_BEGIN authority stands and ignored after AUTH_END. Key rotation is an ordinary KEL event (anchored attestations stay verifiable); AUTH_END revokes an organization's signing authority (re-AUTH_BEGIN restores it); operator/device lifecycle lives in ATTESTed enrollment/revocation records, so the verifier can confirm a device was authorized at capture time. Off-chain by design: a new indexer (built on signify-ts) validates the ACDC chain, digest anchoring, and authority period, and marks attestations unverified after revocation. External wallets pay every counted transaction.

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

Initial target: small and medium field-evidence organizations (inspection firms, adjusters, field-audit teams) with several operators or devices whose evidence third parties must verify; the buyer is an administrator or compliance lead.

Demand evidence, stated candidly: TrustEye is live with an operational B2B organization/API layer, and enterprises already pay for capture-integrity workflows (e.g. Truepic Vision, sold to insurers). Not claimed: no committed pilot organization or distribution commitment exists at submission; no existing app user is assumed to become a Cardano user; zero of the target is attributed to named partners. Conversion is the declared principal risk.

Reachable market, worked first: direct contacts at Romanian insurers and banks from the lead applicant's career (3-5); loss-adjusting and inspection vendors serving them, via warm referrals (5-8); Flip.ro and eMAG Buy-Back (condition-photo intake); Autovit/OLX-ecosystem trade-in dealers (10-15); leasing and fleet operators from the same network (3-5) — \~25-35 outreach starts for the 6-10 active organizations required: one conversion in four to six across the \~9-week pre-M1 runway.

Responding to curation: cadence is grounded in public ASF claim volumes (see usage model); the conversion asked is ordinary for warm B2B channels; Demo Day evidence will list every onboarded organization and any signed intents — if fewer than six are active, we will say so there rather than defend the target.


### Applicant name

Marius Georgescu

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

TrustEye already sells consumer sealing capacity and a B2B organization/API service; those remain the sustainability route. The Cardano accountable-source layer becomes part of a paid higher-assurance organizational plan: organizations pay TrustEye for the workflow and pay the Cardano network themselves for their identity and Verified Source Attestation transactions — recurring events driven by their real case flow (new operators and devices, rotations, revocations, evidence publications), not by the grant. We do not claim existing revenue or proven willingness to pay for this feature; that is a stated validation goal of the pilot. Usage persists after the measurement window because attestations track each organization's ongoing field operations — the same reason the post-window kicker pace is credible. The integration stays in production under TrustEye's commercial model after the pilot. 

The Pilot's own structure prices adoption risk: Adoption/Kicker pay only on real external usage.

### On-chain identity (CIP-0170) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without the grant, Cardano stays a background-anchoring roadmap item like Solana and Ethereum — no accountable-source layer, no external-wallet CIP-0170 flow, no public verification artifacts. The grant funds only future work. Build (20,000 ADA): CIP-0170/KERI profile and Verified Source Attestation implementation with the reference-wallet flow (8,000); chain indexing and identity-state resolution (4,500); backend and verifier integration (4,500); tests, the Apache-2.0 artifact set, telemetry/dashboard, and M1 operations (3,000). Adoption (up to 20,000) and Kicker (10,000) are earned only through valid external usage and fund onboarding, support, and continued operation. No user subsidies, no fee refunds, no re-granting.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By end of week 12 (internal target: week 9): 

1. newly deployed Cardano mainnet footprint with declared Pilot identifier and registered message tag; 
2. the complete external-wallet CIP-0170 flow on mainnet: AUTH_BEGIN with a real organization credential chain plus a valid ATTEST over a real evidence bundle, externally paid; 
3. live TrustEye capture-to-verifier demonstration joining organization identity, device authorization, content integrity, and Cardano timestamp; 
4. published schemas, transaction identifiers, deterministic test vectors, and verification steps; 
5. public adoption dashboard separating qualifying identity fees from all other Cardano activity; 
6. open-source artifact set at github.com/en7angled/trusteye-cip170 (Apache-2.0): CIP-0170/KERI profile, event and attestation schemas, test vectors, and a standalone verification adapter; 
7. organization onboarding flow, wallet self-payment guidance, and lifecycle playbooks ready for the pilot cohort.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### On-chain identity (CIP-0170) - fee target (ADA)

100

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

TrustEye is a production mobile camera and verification system, live on iOS and Android, that creates cryptographic evidence about how a photo or video was captured: a device-held hardware key signs the captured bytes, the app preserves a tamper-evident proof chain, and a public web verifier checks the result. It proves provenance and integrity — not that the depicted scene is true.

The gap: a valid device signature answers "did these bytes come from this device, unchanged?" It does not answer "which accountable organization controlled that device at capture time?" Today that relationship lives in TrustEye's database, so a verifier must trust our service.

Who has this problem: field-inspection and evidence-collection organizations whose evidence feeds third-party decisions — insurance claims, RealFi/RWA collateral inspections, financed-project monitoring, proof of delivery, buy-back condition assessment, and compliance review. Their reviewers need a durable chain from organization to operator and device to evidence, verifiable even if TrustEye is unavailable.

The funded solution: a Cardano-native accountable-source layer. Each participating organization controls a CIP-0170/KERI identifier, authorizes operators and devices, and publishes Verified Source Attestations from its own wallet — one externally paid transaction binding its identifier, device-authorization state, evidence-bundle hash, and timestamp. A public verifier joins identity, device, content, and time.

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

TRL 3: a private TrustEye branch contains an experimental Cardano backend, an Aiken validator, relay work, and an iOS Mithril verification path, and produced a real Preprod transaction before this proposal (ac02d2ae0386d6dbc4e06a458e018720338de1b14418e8dc573c550f615696d9 on preprod.cardanoscan.io). Its limitation is exactly what this grant funds: it used sponsored submission and did not implement the CIP-0170/KERI external-wallet flow proposed here — no organization identifiers, no operator/device authorization events, no Verified Source Attestation profile, no mainnet footprint. Baselines are frozen and disclosed (private branch bd6f41ef, production main d14e7d99) so no prior work is funded retroactively; Catalyst funds only the new CIP-0170 integration built after onboarding.
