# CIP-0170 Identity Rails for Global Medical Travel

> Aline Health processes CIP-0170 identity for cross-border healthcare: credentials are issued and revoked in TELs, independently verified via a fresh-store verifier

## Proposal Metadata

- **Status:** finalized
- **Revision:** 35
- **Proposer:** `stake1uy3d2ywtn90megrayll7fxlrkf4976x7hv96dgcahuw5ssg34jyqe`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-23T12:47:35.326000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

**Raschel Kaushal, Founder:** CS engineer (IGDTUW), INSEAD AI Venture Lab founder and former partnerships lead at Reslink. Leads product, operations, provider onboarding, LOIs and patient acquisition. [LinkedIn](http://linkedin.com/in/raschelkaushal)

**Dr. Dinesh Kumar Kaushal, Medical Advisor:** MBBS, MAMC; Nuclear Medicine, INMAS (DRDO). Head of Nuclear Medicine & PET at National Heart Institute, Delhi, with 20+ years in imaging and radionuclide therapy. Defines clinical milestones, validates workflows and leads clinician onboarding. [LinkedIn](http://linkedin.com/in/dinesh-kaushal-032a3126)

**Shubham Talwar, Fortis Worldwide Ops:** Leads Insurance, Embassy, Pacific Islands & Rest of World at Fortis Group, with seven years in international sales and business analysis. Runs the international patient desk and is our contact for referrals and consultant introductions. [LinkedIn](http://linkedin.com/in/shubham-talwar-544554ab)

**Nandika Bassi, Marketing:** BA Psychology, University of Melbourne, with experience in marketing, outreach and operations. Leads campaigns and patient onboarding. [LinkedIn](http://au.linkedin.com/in/nandika-bassi-25b3a2296)

**Sakshi Soni, Lead Engineer:** [B.Tech](http://B.Tech) CS, IGDTUW; Google Women Engineers scholar and former Microsoft intern. Leads KERI, ACDC credentials, TEL revocation, passkeys, attestations, verifier infrastructure, mainnet deployment, and the security review. [LinkedIn](http://linkedin.com/in/sakshisoni23)

### Eligible area

Yes

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Patients self-anchor a KERI credential at booking from their passkey wallet; clinicians attest admission and sign-off; aftercare teams attest recovery checks each epoch a case is active; the handover digest anchors at transfer of care; follow-up clinicians and the insurer attest; auditors review. Every transaction is signed and paid by the acting party's own wallet. A funded case generates 8-14 attestations; cadence is built into the care pathway itself, spreading across epochs rather than spiking.

A 17-day Liberia pilot produced 600+ inbound patient leads at $0.2 per lead. A fraction of that flow converts to 100+ funded diagnostics and dental cases, plus 40 professional and auditor wallets across our hospital network (NHI & Fortis): \~1,300-1,500 attestations at the 0.33 ADA network average.\
\
The front of the window is dated rather than assumed: around 120 transactions across 25 external wallets in the entry epoch, around 300 across 60 wallets by day 15. The rest accrues as those cases move through handover, aftercare and follow-up, with new bookings opening each epoch.

### How will you reach and onboard real users - and what evidence backs your channels?

Our funnel is live. In 17 days in Liberia, it generated 600+ inbound patient leads at $0.20/lead from 325K+ impressions at \~2% CTR. It now targets diagnostics and dental, which close within 30 days, so post–Demo Day conversions can transact. Teleconsult partners in Zambia, Nigeria and the Caribbean feed patients in.

Provider onboarding: Fortis Healthcare’s Shubham Talwar routes referrals to treating consultants, while NHI Delhi’s Dr. Dinesh Kumar Kaushal introduces clinicians and validates the workflow.

Onboarding happens inside booking: patients create a passkey wallet, anchor their credential and fund gas; professionals sign and pay for attestations.

From Demo Day sign-off, with 10+ professionals credentialed: Days 1–5 target 15 patients, 25 external wallets and \~120 transactions. Days 6–15 add 35 patients, aftercare and first insurer/auditor attestations, reaching 60 wallets and \~300 cumulative transactions. Network target: 40 professionals vs. a 10-wallet minimum.

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

Our market is cross-border patients, plus the operators and insurers serving them. Demand is already proven: the UK has 7.2M people on NHS waiting lists, Caribbean households spend \~40% of income on healthcare, and India received 507K+ medical travellers in 2025, with treatment 65–90% cheaper than developed markets. The global market is growing from \~$58B toward $120B+.

Our own PMF evidence is live. In 17 days in Liberia, we generated 600+ inbound patient leads at $0.20 each from 325K+ impressions at \~2% CTR. At NHI Delhi, Dr. Dinesh Kumar Kaushal introduces clinicians for credentialing; at Fortis, Shubham Talwar routes international referrals and consultant introductions.

Existing operators sell treatment access, not verifiability. We add trusted treatment evidence and tamper-resistant handover records to cases our funnel already produces, starting with diagnostics and dental, where decisions can close within 30 days.

### Applicant name

Raschel Kaushal

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Our business runs on conventional infrastructure and fiat rails; the chain carries identity and evidence, never money.

Hospitals pay a 30% referral commission per treated patient. In India, a $7,200 procedure yields $2,160 to us, with commission routes through National Heart Institute and Fortis Healthcare. Teleconsult clinic partners across Zambia, Liberia, Nigeria and the Caribbean share a 30% consult fee. Providers pay credential/network fees to be verified, and insurers pay for the verifiable evidence feed.

Grant funding covers only identity integration; referral economics fund operations, with no payment-licensing burden because payments stay off-chain.

Usage compounds with care: each funded case anchors a patient credential and care attestations, each hospital adds a recurring attester stream, and every new corridor reuses the same declared footprint.

### On-chain identity (CIP-0170) - expected transaction count

1500

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding takes the system from Preprod to production over three months,

- User-paid flows, passkey wallets, self-anchoring and professional attestations: 46,000 ADA

- Clinician tooling from admission through follow-up: 34,000 ADA

- Mainnet deployment, 10+ professional credentials, Demo Day and adoption ops: 32,000 ADA

- Platform integration and KEL/TEL evidence explorer: 32,000 ADA

- Independent security review: 16,000 ADA

- Security remediation and QA: 12,000 ADA

- Three KERI witnesses, monitoring and infrastructure: 14,000 ADA

- Legal, privacy and deployment counsel: 8,000 ADA

- Release engineering and production testing: 6,000 ADA

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, live on mainnet and demonstrated at Demo Day:

1. The platform in production at a stable URL: booking journey with passkey wallet onboarding, credential self-anchoring, and a public evidence explorer.
2. Our organizational KERI authority on mainnet, 3 witnesses at 2-of-3, its CIP-0170 lifecycle anchored under the registered labels.
3. A credentialed network before Demo Day: 10+ named clinicians from NHI & Fortis, aftercare, insurer and auditor roles holding anchored, revocable credentials and attesting from their own wallets.
4. User-paid flows live: self-anchor, admission, sign-off, discharge handover digest, aftercare, follow-up.
5. Registered message tag on every transaction; footprint declared (org AIDs, schema SAIDs, addresses, team wallets), all newly deployed.
6. Launch readiness at sign-off: first cases booked, ready to transact from day 1.
7. Demo Day: an external patient self-anchors, an independent clinician attests on mainnet, plus a revocation demo.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

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
- https://linkedin.com/in/raschelkaushal
- https://www.linkedin.com/in/dinesh-kaushal-032a3126 
- https://www.linkedin.com/in/shubham-talwar-544554ab

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

What exists today, live at [preprod-id.alinehealth.world ](http://preprod-id.alinehealth.world): our org KERI AID with three witnesses at 2-of-3, its lifecycle anchored under labels 170, 674 and 9126 with a registered CIP-20 tag; ACDC role credentials chained to that authority; a KEL at post-rotation sequence with witness receipts; a revoked credential failing to authorize later actions; SHA-256 milestone digests against opaque case references. All synthetic data, sponsor relayer paying fees.

The grant covers the ground from here: mainnet with newly deployed identifiers, user-paid flows from passkey wallets, witnesses on stable hosts, clinician tooling, and security review before any real user transacts.
