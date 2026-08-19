# CIP-0170 Identity Rails for Global Medical Travel

> Aline Health processes CIP-0170 identity for cross-border healthcare: credentials are issued and revoked in TELs, independently verified via a fresh-store verifier

## Proposal Metadata

- **Status:** finalized
- **Revision:** 19
- **Proposer:** `stake1uy3d2ywtn90megrayll7fxlrkf4976x7hv96dgcahuw5ssg34jyqe`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T17:30:13.048000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Raschel Kaushal**\
Computer science engineer (IGDTUW, Delhi) and AI venture founder at the INSEAD AI Venture Lab. She led partnerships for 16 months at Reslink, an Indian deep-tech hardware startup, taking it through Bharat Mobility and EV India Expo. At Aline Health she owns the product, operations, provider onboarding, the LOIs and patient-acquisition channels.\
\
[linkedin.com/in/raschelkaushal](http://linkedin.com/in/raschelkaushal)

### Eligible area

Yes

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Patients self-anchor a KERI credential at booking from their passkey wallet; clinicians attest admission and sign-off; aftercare teams attest recovery checks each epoch a case is active; the handover digest anchors at transfer of care; follow-up clinicians and the insurer attest; auditors review. Every transaction is signed and paid by the acting party's own wallet. A funded case generates 8-14 attestations; cadence is built into the care pathway itself, spreading across epochs rather than spiking.

A 17-day Liberia pilot produced 600+ inbound patient leads at $0.2 per lead. A fraction of that flow converts to 100+ funded diagnostics and dental cases, plus 40 professional and auditor wallets across our hospital network (Fortis, Marengo Asia, Artemis, Max): \~1,300-1,500 attestations at the 0.33 ADA network average.

### How will you reach and onboard real users - and what evidence backs your channels?

Our own acquisition funnel: 17 days on the ground in Liberia produced 600+ inbound patient leads at an optimized $0.2 per lead, from 325K+ impressions at \~2% CTR. That funnel now points at diagnostics and dental, which convert inside a 30-day window.

Hospital referrals: Fortis, Marengo Asia, Artemis, and Max Healthcare, onboarding as credentialed providers.

(3) Teleconsult clinic partners in Zambia, Liberia, Nigeria, and the Caribbean feed assessed patients in.

(4) 30+ professional attester wallets across those providers, plus independent auditors. Total 200+ external wallets against a 10-wallet minimum.

Onboarding sits inside the booking journey. Each patient creates a passkey self-custody wallet, anchors their own CIP-0170 credential, and funds their own gas; every attestation is signed and paid by the professional's own wallet. Provider credentials anchor pre-window; first cases run from day 1.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

(1) The Medical Travel Company (UK), our closest competitor: a full-journey UK-to-India operator. Trust rests on brand and reviews; nothing is verifiable or revocable.

(2) Marketplaces such as Bookimed (1M+ patient requests): listings at scale, same gap.

(3) Booking via an agent: cheapest, least protected, handovers as email PDFs.

(4) EBSI/EUDI-style credential pilots: jurisdiction-bound, built for static credentials, not care events.

(5) Atala-lineage work, now Hyperledger Identus: a framework, no live deployment.

We win on verifiability plus a tested funnel: 600+ patient leads in 17 days at $0.2 each, with hospital relationships in place. On Preprod, a revoked provider credential already fails to authorize later actions. No competitor can show either.

### Please provide details about the Technology Readiness Level selected for your existing product

We validated end-to-end in a relevant environment: Cardano Preprod. It is live and publicly demonstrable across four layers: a medical-travel marketplace, a patient workspace, a partner console, and a public evidence explorer. The complete patient journey runs against Preprod using synthetic data: role credentials, funded care route, reservations, milestone schedule, handover evidence, settlement, reassignment, and provider revocation \[live URL; walkthrough video\]. No real patients, PHI, or payments in the demo by design; the grant funds the mainnet launch.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

One identity spine, digest-only on-chain state, fees paid by the acting party. Every mainnet identifier is newly deployed.

KERI anchored through CIP-0170. Our organizational authority is a KERI AID with 3 witnesses at a 2-of-3 receipt threshold; its lifecycle (AUTH_BEGIN, attest, AUTH_END, reauthorization) anchors under metadata labels 170, 674, and 9126, with a registered CIP-20 tag on every transaction. Each patient and professional runs their own AID with an ACDC role credential chained to our authority credential. Issuance and revocation state live in TELs; any verifier can replay KEL and TEL from a fresh store and reach the state we assert. Rotation and revocation are proven on Preprod: the KEL sits at a post-rotation sequence with witness receipts, and a revoked credential fails validation on later actions.

Each care milestone (consult, admission, sign-off, handover, aftercare, insurer verification) is a transaction signed and paid by the attesting party's wallet: a SHA-256 document digest anchored against an opaque case reference, with a monotonic per-actor sequence and one-use nonce. On-chain state is strictly AIDs, schema and credential SAIDs, roles, status, nonces, sequences, digests. PHI never reaches the chain.

This is what CIP-0170 specifies: identity evidence separated from authorization, credential state verifiable without trusting the issuer, enforced revocation. Patients self-anchor from passkey wallets; our own wallets are declared, never counted.

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

Our target market is patients who cross a border for treatment, plus the operators and insurers who serve them. The demand doesn't need our projections. The UK has 7.2 million people on the NHS waiting list; Caribbean households spend 40% of income on healthcare; patients face &gt;3x prices locally versus equally effective treatment abroad. India received 507K+ foreign arrivals for medical treatment in 2025, with costs 65-90% below developed-market prices, and the global market is headed from $58B toward $120B+ at 14% CAGR. Live operators already monetize this gap: The Medical Travel Company (UK), Bookimed, and hospital international patient desks.

Our product-market fit evidence is our own. Before asking the market to believe us, we tested it: 17 days on the ground in Liberia produced 600+ inbound patient leads at an optimized $0.2 per lead, from 325K+ impressions at \~2% CTR. On the supply side, we work with India's leading hospital groups: Fortis, Marengo Asia, Artemis, and Max Healthcare.

None of them sell verifiability. Insurers need treatment evidence they can trust; follow-up clinicians need handover records that cannot be quietly edited. That is the layer this grant funds, riding on cases our tested funnel already produces. Acquisition starts with diagnostics and dental, the packages with decision cycles fast enough to convert inside a 30-day window.

### Applicant name

Raschel Kaushal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Our business runs on conventional infrastructure and fiat rails; the chain carries only identity and evidence, never money. Who pays, with tested numbers: 

- Hospitals pay us a 30% referral commission per treated patient. For India, a $7,200 procedure at 30% is $2,160 per patient
- Clinic partners in our teleconsultation stream (Zambia, Liberia, Nigeria, Caribbean) share a 30% consult fee
- Providers pay credential and network fees to appear as verified, and insurers pay for the verifiable evidence feed. The grant funds only the identity integration; referral economics fund operations, and because no payments touch the chain, we carry no payment-licensing drag.

Usage continues because attestations are a byproduct of care happening: every funded case anchors a patient credential and a stream of care attestations, every onboarded hospital brings a recurring attester stream with no grant incentive attached, and each new corridor reuses the same declared footprint.

### On-chain identity (CIP-0170) - expected transaction count

1500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this grant it never reaches mainnet in a live medical operation. What remains unfunded: replacing the demo's sponsor relayer with user-paid flows (patients self-anchoring from passkey wallets, professionals paying their own attestations), moving KERI witnesses to stable hosts, tooling our hospital clinicians will actually use, a security review, and connecting the chain layer to our tested patient funnel. Nothing is retroactive: the prototype predates the grant and is not billed to it.\
\
We spend on user-paid flow rework and wallet onboarding; witness infrastructure; clinician tooling; platform integration and evidence explorer; security review and counsel; mainnet deploy, Demo Day, adoption ops.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, live on Cardano mainnet and demonstrated at Demo Day:

1. The Aline Health platform in production at a stable URL: booking journey with passkey wallet onboarding, patient credential self-anchoring, and a public evidence explorer.
2. Our organizational KERI authority on mainnet (3 witnesses, 2-of-3 threshold), its CIP-0170 lifecycle anchored under the registered labels.
3. A credentialed professional network: at least 10 named professionals (clinicians, aftercare, insurer, auditor) holding anchored, revocable credentials, attesting from their own wallets.
4. User-paid attestation flows live: patient self-anchor, admission, treatment sign-off, discharge handover digest, aftercare, follow-up.
5. Registered message tag on every transaction; full footprint declared (org AIDs, schema SAIDs, addresses, team wallets), all newly deployed.
6. Demo Day: an external patient self-anchors and an independent clinician submits a live attestation on mainnet, plus a revocation demo.

### How far along is the integration you're proposing, today?

TRL 9 - Actual system proven in operational environment

### On-chain identity (CIP-0170) - fee target (ADA)

500

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cross-border healthcare runs on unverifiable trust. A patient sending thousands of pounds abroad cannot check, at the moment it matters, whether the surgeon on their case is currently licensed, or whether a provider struck off last month has actually been shut out. Operators vouch for their networks by hand, and no outside party can audit the claim.

Aline Health puts that trust layer on Cardano using CIP-0170. Every actor in a case (patient, hospital, clinician, coordinator, insurer, aftercare provider, auditor) holds a KERI identifier with an ACDC role credential. Issuance and revocation state live in Transaction Event Logs, so any verifier can replay a TEL from a fresh store and reach the same answer we do. Revocation is enforced, not advisory, a revoked provider's credential fails to authorize any subsequent action.

Care milestones anchor evidence, not records. Admission, treatment sign-off, discharge, and follow-up each commit a SHA-256 digest of the handover document against an opaque case reference. An insurer or home clinician can verify that an event occurred and which credentialed actor attested it, without access to the underlying record. No PHI reaches the chain.

Three groups have this problem: patients trusting a provider network they cannot inspect; medical-travel operators whose only governance tool is a phone call and a spreadsheet; insurers and GPs who need verifiable treatment evidence, not an emailed PDF, before continuing care.

### Supporting links (repo, site, demo)

- https://preprod-id.alinehealth.world/

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

The demo's sponsor relayer goes, replaced by user-paid flows where patients self-anchor from passkey wallets and professionals pay their own attestations, and the KERI witnesses move to stable production hosts.

An independent security review, before any real user touches the system. 

We deploy to mainnet with newly deployed identifiers and our declared footprint, and run a live Demo Day: an external patient self-anchors, a clinician submits a real attestation. 

Live operation: real patients and clinicians from our tested funnel transact through the adoption window, and anyone can verify credential state on our explorer.
