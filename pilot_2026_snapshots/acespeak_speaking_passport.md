# AceSpeak Speaking Passport

> Portable, privacy-preserving communication credentials for learners — shareable as a link, verifiable by a scan, anchored by Cardano and usable across work and education.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 26
- **Proposer:** `stake1uyz8kucpahj960vh3klvgnes60tswdhxl66sfkeqrape84qlvrwwy`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-19T13:49:39.214000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

AceSpeak combines communication expertise, a working consumer product, growth capability and Cardano engineering evidence.

Krystle Cheung, Founder & CEO, owns product vision, assessment pathways and user adoption. She is a two-time public-speaking champion with 14 years' experience, 5,000+ events and work for 200+ brands.

Amanda So, Cofounder & CTO, owns the CIP-0170 build. She has led engineering teams since 2019, holds an MPhil from HKUST and BEng from Warwick, and built and exited MamaHelpers in 2023.

Alfred Chan (CHAN, Kwun Nam), Cofounder & CIO, supports architecture, security and delivery. He has 14+ years across web, mobile, cloud and AI, led 100+ engineers and completed a Cyberport-funded project in 2020.

Yasmine Ananda, AI Engineer, owns the eligibility service and learner claim flow. She is a published AI researcher with EdTech-AI experience.

Wistkey Lab has eight merged PRs to bloxbean/yaci-devkit, proving team-level Cardano-tooling experience. The assessment engine already runs; this grant funds one credential flow and verifier.

Profiles/evidence:

Krystle <https://krystle.hk/en/>

Amanda <https://uk.linkedin.com/in/styamanda>

Alfred <https://nam-ai.uk>

Yasmine <https://www.linkedin.com/in/ananda-yasmine-08a94411a/>

Cardano PRs <https://github.com/bloxbean/yaci-devkit/pulls?q=is%3Apr+author%3Awistkeylab>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Each count is an external user-funded credential event. We forecast 530 CIP-0170 attestations across about 70 wallets. Preprod balancing measured ATTEST at 0.1834 ADA, so the forecast generates 97.2 ADA against our 85 ADA declaration — about 14% headroom.

Bottom-up:

\- 40 adult paid learners × 8 events = 320 transactions / 58.7 ADA.

\- 18 crypto-native founders/professionals new to Cardano × 7 = 126 / 23.1 ADA.

\- 12 Cardano users × 7 = 84 / 15.4 ADA.

About 84% of forecast fees come from the first two new-to-Cardano cohorts. At the measured fee the 50 ADA floor requires 273 transactions; cohorts two and three forecast only 210, so the floor depends on the paid-user cohort. This risk is explicit: 43 of 46 surveyed subscribers said they would connect a wallet and pay, while the forecast uses 40.

Events represent a verified baseline, improvement milestones or completed Interview Ready, Presentation Ready, Oral Communication or Pitch Ready pathways—not every practice session. Team wallets, automation, duplicates, incentives, reimbursements and sponsored fees are excluded. Week 1 opens to 10–15 prepared users; week 2 adds another cohort; later releases remain staged.

### How will you reach and onboard real users - and what evidence backs your channels?

We use three measurable channels.

1\. Existing paid learners: 174 people subscribe; 43 of 46 surveyed on 16 August said they would connect a wallet and pay. We target 40 adult subscribers after allowing for on-ramp friction.

2\. Crypto-native founders and professionals new to Cardano: live demonstrations through startup and Web3 communities target 18 external wallets.

3\. Cardano-native learners and educators: community outreach supplies 12 wallets, feedback and early verifiers. It is deliberately not the majority because we aim to bring new users to Cardano.

We measure eligibility, wallet started/connected, claim reviewed, transaction submitted/confirmed and later verification. Team wallets, incentives, reimbursements, automation, duplicates and sponsored fees are excluded. Thirteen organisations committed to pilot the speaking product receive no forecast usage attribution. Releases are staged across the measurement window.

### Is the underlying project open source?

No

### Short Video Pitch

https://youtu.be/R1b-pbb2yQw

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include voice-first coaches such as Orai, Yoodli and Poised; human coaching; interview simulators; PDFs/Open Badges; and Cardano infrastructure including Andamio and Veridian.

Voice apps miss body language; human coaching is expensive and subjective; PDFs are easy to copy; badge infrastructure does not provide AceSpeak's assessment or learner journey.

AceSpeak combines a live multimodal product, paying users, expert-defined criteria and a path to genuine transactions. We do not claim to invent Cardano credentials: Andamio and Veridian are potential infrastructure routes, while we own the assessment and learner journey. The app remains useful without blockchain; an open profile can support other issuers, while verifiers choose which issuers and thresholds they trust.

### Please provide details about the Technology Readiness Level selected for your existing product

AceSpeak is a complete, deployed consumer application available on iOS and Android. It performs AI speaking assessment and feedback in a real user environment and currently has 495 lifetime users and 174 active paid subscriptions: 90 Max and 84 Pro. The team operates production delivery, subscriptions, support and the assessment workflow that will trigger credential eligibility. Product site: <https://acespeak.uk>.

TRL 8 reflects that the underlying system is complete and operating with paying users while undergoing normal improvement. The Cardano component is assessed separately; we do not use the maturity of the base app to imply that CIP-0170 work is complete.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

AceSpeak uses a privacy-preserving off-chain/on-chain split.

1\. Private assessment: the existing service analyses practice audio/video. Raw media, transcripts, detailed scores, account identifiers and personal data stay off-chain.

2\. Eligibility: when a learner meets published criteria, the credential service creates a versioned payload with credential type, issuer, issue time, assessment profile/version, a non-personal subject reference and cryptographic digest.

3\. Consent and control: the learner connects a CIP-30 wallet, signs a challenge, reviews the claim, public-data implications and measured fee, then chooses whether to proceed.

4\. CIP-0170 anchor: AceSpeak signs the attestation using its managed issuer identity and KERI event chain. The learner submits and funds the Cardano ATTEST transaction; its metadata carries AceSpeak's issuer AID and the anchored credential digest.

5\. Verification and lifecycle: a public verifier resolves the Cardano record, checks the issuer signature, KEL seal, digest and schema/version, and shows current, superseded or invalid status.

Cardano is used only where independent trust is needed: issuer identity, integrity, timestamp and status. AceSpeak remains responsible for assessment. This avoids permanent personal data on a public ledger and supports future compatible issuers while letting each verifier choose which issuers and criteria it recognises.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- On-chain identity (CIP-0170)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

Yes

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

We serve two paying segments: adults improving communication for interviews, presentations and pitches, and parents buying accounts for school-interview preparation. The on-chain pilot is adult-only; no adoption target depends on a minor transacting.

AceSpeak is live on iOS and Android with 495 lifetime users and 174 active paid subscriptions (90 Max, 84 Pro). Pro costs HK$98/month and Max HK$168/month. Of 46 paid subscribers surveyed on 16 August 2026, 43 said they would connect a wallet and pay the fee. We forecast 40 participants, deliberately below stated intent because wallet onboarding—not the measured 0.1834 ADA fee—is the main barrier.

Demand is also proven offline. Krystle Cheung's one-to-one coaching rate rose from HK$480 to HK$1,280/hour in H1 2026; children's interview preparation starts at HK$880/lesson; and she expanded into corporate training in 2026. Her 14-year, 5,000-event audience and existing clients created the warm launch cohort behind the app's early conversion.

Thirteen education, professional and HR organisations are committed to pilot AceSpeak's speaking product. Recognition of Cardano-anchored credentials is the next conversation, not an existing agreement, and no forecast usage is attributed to them. The on-chain pilot remains adult-only.

### Applicant name

Wistkey UK Limited

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Paid Pro (HK$98/month) and Max (HK$168/month) subscriptions fund AI practice, hosting and support. Speaking Passport adds consumer certification and B2B plans for cohort administration, issuer/verifier tools and API access. Thirteen organisations are committed to pilot the speaking product; Cardano recognition and paid B2B contracts remain prospective.

The learner pays the Cardano fee from an external wallet. Sponsored accessibility claims are reported separately and excluded from the target.

Usage persists through the learning cycle: baseline, verified improvement milestones and completed Interview Ready, Presentation Ready, Oral Communication or Pitch Ready pathways. We do not transact for app opens or routine practice. Catalyst funds the one-off integration, security, verifier and launch; subscription revenue supports ongoing operation. Public profile and verifier documentation allow future education-provider compatibility.

### On-chain identity (CIP-0170) - expected transaction count

530

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The 50,000 ADA pilot funds a focused three-month mainnet delivery not covered by existing coaching revenue:

• 22,000 ADA — issuer identity, signing, anchoring, CIP-30 wallet flow, lifecycle handling and mainnet release.

• 9,000 ADA — eligibility logic, consent, fee explanation and mobile/web UX.

• 6,000 ADA — privacy, threat modelling, key-management review, QA and remediation.

• 8,000 ADA — real-user onboarding, support and channel execution; no rewards or reimbursements for counted transactions.

• 5,000 ADA — public verifier, analytics, open credential profile and documentation.

Without the pilot, core AI development would continue, but the Cardano identity layer and adoption programme would not receive dedicated delivery capacity.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

By the end of month three, AceSpeak will deliver:

1\. A production mainnet claim flow with at least two independent transactions by real external users, using the declared CIP-0170 identifiers.

2\. A production CIP-0170 issuer, four versioned communication-credential profiles and a public verifier that checks the issuer signature, KEL seal, digest and lifecycle status.

3\. Privacy and security evidence: a data-flow and threat model, key-management review and tests confirming that raw media, transcripts, detailed scores and personal data remain off-chain. Funnel analytics will exclude team-controlled wallets.

4\. Release evidence comprising the live URL, mapped transaction hashes, declared footprint, technical walkthrough, release notes, test evidence, integration documentation and Demo Day presentation.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

85

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

AceSpeak is a live AI communication coach for interviews, presentations and pitches. It privately analyses expression, gestures, pace, intonation and pauses, turning practice into measurable improvement. We will add AceSpeak Speaking Passport: an optional Cardano layer that converts meaningful achievements into portable, verifiable credentials.

Today, progress is trapped inside the app or training provider that measured it. Screenshots and PDF certificates are easy to copy, depend on the issuer's live database and give employers, schools or clients no independent integrity check.

An eligible adult learner will connect a Cardano wallet, prove control, review the claim and choose to anchor an issuer-signed Interview Ready, Presentation Ready, Oral Communication or Pitch Ready credential. A public verifier will check issuer, type, issue time, integrity and status without an AceSpeak account. Learners can share one verification link on a profile or application, or present a QR code at an AceSpeak workshop.

AceSpeak, not blockchain, assesses speaking. Cardano supplies a neutral, tamper-evident trust rail when learner, issuer and verifier differ, while supporting future education providers. Raw video, audio, transcripts, detailed scores and personal data remain off-chain; only minimum cryptographic and status data is anchored. The normal app stays wallet-free and claiming is optional. Initial users are adult job seekers, professionals and founders.

### Supporting links (repo, site, demo)

- https://acespeak.uk
- https://github.com/bloxbean/yaci-devkit/pulls?q=is%3Apr+author%3Awistkeylab
- https://krystle.hk/en/
- https://uk.linkedin.com/in/styamanda
- https://acespeak.uk/catalyst/acespeak-speaking-passport-pitch-deck.pdf

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

### Funder, status, and what it covers

Cyberport Creative Micro Fund (CCMF) — AceSpeak application under consideration. It covers general product and company development, not the CIP-0170 integration, public Cardano verifier, privacy/security work or user-funded adoption programme requested here. No Catalyst deliverable has been delivered or funded by CCMF.

### Standard read and attested

Yes

### Current funded commitments

HKSTP Ideation — VitaLedger (2026). Alfred Chan and overlapping team members are currently delivering this separate health-record/Cardano project; completion follows the 2026 HKSTP Ideation programme schedule. VitaLedger is not being submitted to this Catalyst Pilot round and has separate scope, budget and deliverables. It does not fund AceSpeak, communication credentials, the CIP-0170 Speaking Passport integration, the public verifier or the adoption programme. The team has no current Catalyst-funded commitments.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The product requirements, privacy boundary, user journey and CIP-0170 architecture are defined. An internal spike created, anchored and resolved a representative signed KERI attestation on preprod, paid by an external wallet, and measured the counted ATTEST fee at 0.1834 ADA. The team also has eight merged contributions to bloxbean/yaci-devkit.

The production issuer, wallet claim flow and public verifier are not yet integrated. The final deck's public-repository and transaction-hash fields are still placeholders, so TRL 2 remains the defensible selection until those links are attached. The grant funds production implementation and validation.
