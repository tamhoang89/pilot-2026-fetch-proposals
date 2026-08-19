# TAGBASE NFC-Verified Ownership Transfers on Cardano

> Securely transfer digital ownership on Cardano only after the linked physical object has been verified through its cryptographic NFC tag.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 45
- **Proposer:** `stake1uydsltz2939nz2f7nmyeqdmjrkkqd32c37vz7ag2ets3mtsqwpypa`
- **Funding requested:** ₳115,000
- **Last finalized:** 2026-08-19T18:34:28.080000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 8 - System complete and qualified

### Why is your team well-suited to deliver this?

Manuel Mertl – CEO & Co-Founder\
<https://www.linkedin.com/in/manuelmertl>\
Manuel will lead product definition, pilot coordination, partner onboarding, commercial rollout and Catalyst reporting. He has built TAGBASE’s customer and partner network and represented TAGBASE in Cardano programs, including the Techstars Web3 Cardano Founder Catalyst and the Top 10 Battle of the Builders at the Cardano Summit in Dubai.

Mario Uher – CTO & Co-Founder\
<https://www.linkedin.com/in/ream88>\
Mario will lead the technical architecture, Cardano integration, backend development, NFC verification workflow, testing and mainnet deployment. He previously co-founded [Yodel.io](http://Yodel.io), which was acquired by Sendinblue, now Brevo.

Together, we have already built TAGBASE’s operational NFC platform, dynamic cryptographic verification, APIs, cloud infrastructure, analytics, tag-configuration tools, and iOS and Android applications: <https://www.tagbase.io>

The existing platform substantially reduces delivery risk because the project extends working NFC infrastructure rather than starting from zero. No additional core team members are required. We do not provide services to any other proposal submitted in this funding round.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Our only integration is Programmable Tokens (CIP-0113). We target 200 ADA in fees from 300 transactions: 140 artwork registrations, 140 initial ownership assignments and 20 NFC-verified secondary transfers.

Artists register tagged artworks and assign them to buyers. Owners transact again when an artwork is sold, gifted or reassigned. Each transfer requires a fresh cryptographic NFC scan. The fee target assumes about 0.67 ADA per script-based transaction.

Existing customer Joshua Maurer is open to using Cardano ownership transfers and has 27 artworks with TAGBASE. Registering and assigning them would generate 54 transactions, or 18% of our target.

At Joshua’s SOCIA&SOCIUS exhibition on 11 September 2026, we will present TAGBASE to artists and collectors. We aim to onboard up to seven additional artists. At around 20 works each, this could add 140 artworks. Including Joshua’s works, the potential is 167, making our target of 140 conservative.

In the first two weeks after launch, Week 1 covers artist setup, wallets and registrations; Week 2 covers assignments, first transfers and support. External users pay their own fees. Team, sponsored, test and artificial activity is excluded.

### How will you reach and onboard real users - and what evidence backs your channels?

We will begin with existing TAGBASE artist customers and invite them to activate Cardano ownership transfers for NFC-tagged artworks when pieces are sold or gifted. We cannot yet state an exact number of artists who will participate, so we will not claim unconfirmed commitments.

A concrete acquisition channel is Joshua Maurer’s SOCIA & SOCIUS exhibition in Vienna on 11 September 2026. His original artworks use TAGBASE NFC verification, and TAGBASE is publicly named in the event listing: <https://luma.com/7uv79lq1>. We will speak at the exhibition, demonstrate the technology directly to artists, collectors and art-sector attendees, and invite interested artists to follow-up onboarding sessions.

Other artists will be reached through direct demonstrations, existing customer referrals and follow-ups after the event. TAGBASE will provide NFC tags, artist setup, wallet onboarding and guided support for artwork registration, initial ownership assignment and NFC-verified transfers.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=9IXRe19v-8M

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives include Arianee, Verisart and collectID, as well as paper certificates, centralized databases and standard NFTs. Some record authenticity or ownership, but the digital record can still be transferred without verifying possession of the physical object.

TAGBASE requires a fresh cryptographic scan of the object’s NFC tag before a short-lived authorization permits the token transfer. Copied links, QR codes and previous scans cannot be reused, while Cardano provides transparent, enforceable ownership rules.

Cardano will be our first and primary chain for this functionality. We plan to add Ethereum later as a secondary option, as outlined at <https://www.tagbase.io/en/platform/blockchain>. This project specifically develops and drives adoption of the Cardano CIP-0113 integration.

### Please provide details about the Technology Readiness Level selected for your existing product

TAGBASE is a live product used by paying customers to give physical objects secure digital identities through cryptographic NFC tags. The system includes dynamic verification, APIs, analytics, customer portals, and mobile tag-configuration apps. This project extends our mature platform with Cardano programmable tokens and NFC-gated ownership transfers.\
\
Evidence:\
\
Platform: [platform.tagbase.io](http://platform.tagbase.io)\
Docs: [platform.tagbase.io/docs](http://platform.tagbase.io/docs)\
\
Verify: [verify.tagbase.io](http://verify.tagbase.io)\
Docs: [verify.tagbase.io/docs](http://verify.tagbase.io/docs)\
\
Extension: [chromewebstore.google.com/detail/tagbase/lkbmhimafhmlokikhbchafmjkhombagc](http://chromewebstore.google.com/detail/tagbase/lkbmhimafhmlokikhbchafmjkhombagc)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

The proposed architecture combines TAGBASE’s off-chain NFC verification with CIP-0113 programmable-token rules on Cardano.

Each physical object is linked to a unique Cardano token and TAGBASE NFC identity. The current ownership state is represented by a Cardano UTxO. To transfer ownership, the seller initiates a transfer to the buyer’s wallet and scans the physical NFC tag. The tag generates dynamic cryptographic data, which TAGBASE validates off-chain.

After successful verification, TAGBASE issues a signed, short-lived authorization containing the token ID, current ownership UTxO, seller and buyer addresses, expiry time and unique nonce. The transfer transaction submits this authorization to the programmable-token validator. The validator checks the TAGBASE signature, correct token and participants, validity period and required ownership state before permitting the transfer. Consuming the current UTxO and binding the authorization to a single transfer prevents replay.

Sensitive NFC keys, personal data and detailed product information remain off-chain. Only the ownership token, transfer state and minimum verification evidence are recorded on Cardano.

This architecture fits programmable tokens because physical verification becomes an enforceable transfer condition rather than an optional off-chain check, while Cardano provides transparent ownership history and genuine transactions for every issuance and transfer.

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

Our initial target market is artists, galleries, art platforms and collectors who need ownership records to remain connected to physical artworks when they are sold, gifted or resold. We will then expand to luxury brands, collectible producers, certificate issuers and secondary marketplaces handling watches, limited editions and other valuable physical objects.\
This is a commercially significant market where ownership records must remain trustworthy across high-value sales and transfers. The Art Basel and UBS Global Art Market Report 2026 estimates global art sales at $59.6 billion across 41.5 million transactions in 2025. Online-only art sales represented $9.2 billion, showing the importance of trusted digital processes for physical assets: <https://theartmarket.artbasel.com/global-sales>\
TAGBASE already has artists as paying customers who use our secure NFC tags to connect physical artworks with digital records. This gives us direct access to issuers, objects and buyers for testing NFC-verified transfers when artworks are sold. We also have projects and business relationships involving certificates, authentication, luxury goods and physical product identities. These customer relationships show demand for solutions that go beyond initial authentication and maintain trustworthy records throughout an object’s lifecycle.

### Applicant name

TAGBASE GmbH

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

TAGBASE generates revenue by selling secure NFC tags and charging setup, subscription and usage-based platform fees. Artists, brands, certificate providers and marketplaces pay to give physical objects secure digital identities, authentication and ownership services.

The Cardano integration becomes an additional paid feature. Token creation and network fees can be included in the issuer’s plan, while transfer fees may be paid by the seller, buyer or marketplace.

Usage continues beyond the pilot because every newly tagged object can create a Cardano asset, and every later sale, gift or ownership change generates a genuine on-chain transfer. As TAGBASE sells more tags and onboards more issuers, the number of transferable assets and recurring Cardano transactions grows. Ongoing tag sales, subscriptions and transfer fees sustain the service after grant funding ends.

### Programmable tokens (CIP-0113) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this funding, the Cardano integration would be deprioritized in TAGBASE’s roadmap, with no defined delivery date. The 115,000 ADA grant enables two core team members to deliver it within the program timeline.

Budget breakdown:

- CIP-0113 architecture and validator development: 32,000 ADA
- Backend and NFC authorization integration: 27,000 ADA
- Wallet integration and user interface: 17,000 ADA
- Testing, security validation and mainnet deployment: 17,000 ADA
- Pilot onboarding, support and reporting: 12,000 ADA
- Infrastructure, network fees and NFC tags: 10,000 ADA

Funding covers the two team members’ development and implementation work. The remainder supports deployment, testing, infrastructure and real-user onboarding.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the M1 development window, TAGBASE will deliver:

1. A CIP-0113 programmable-token solution deployed on Cardano mainnet, with published policy IDs, script hashes, addresses and message tag.
2. A backend that validates dynamic NFC scans and issues signed, single-use, time-limited transfer authorizations.
3. A live interface for wallet connection, token creation, initial ownership assignment and NFC-gated transfer.
4. Transfer logic that rejects invalid, expired or reused authorizations.
5. At least three NFC-linked physical objects and three external users completing repeatable mainnet issuance and ownership-transfer transactions.
6. A live product URL and explorer-linked transaction evidence.
7. Release notes, architecture documentation, demonstration video, test checklist, bug log and security note.
8. A live Demo Day presentation using the deployed product and declared on-chain identifiers.

### How far along is the integration you're proposing, today?

TRL 1 - Basic principles observed

### Programmable tokens (CIP-0113) - fee target (ADA)

200

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

TAGBASE is building a Cardano-based solution that securely links a digital ownership token to a physical object through a cryptographic NFC tag.

Today, digital tokens representing real-world assets can be transferred without the corresponding physical object being present. This can separate the digital ownership record from the item it represents, weakening trust in tokenized physical assets. The problem affects artists, brands, manufacturers, marketplaces, collectors and buyers of artwork, luxury goods, watches, collectibles, certificates and other valuable objects.

With our solution, a digital ownership transfer can only be completed after the NFC tag attached to the physical object has been scanned and cryptographically verified. After successful verification, TAGBASE creates a short-lived authorization that enables the programmable token to transfer from the current owner’s Cardano wallet to the new owner’s wallet. A copied link, QR code or previous scan cannot authorize the transfer.

This keeps the physical object and its digital ownership record connected when the item is sold, gifted or otherwise transferred.

### Supporting links (repo, site, demo)

- https://www.tagbase.io
- https://www.linkedin.com/company/tagbase-io/
- https://www.tagbase.io/en/tagbase-completes-the-techstars-cardano-founder-catalyst-program
- https://www.tagbase.io/en/cardano-summit-2024-in-dubai-a-momentous-occasion-for-tagbase-and-the-future-of-product-authenticity
- https://www.tagbase.io/en/tagbase-selected-as-top-10-finalist-in-cardano-summit-2024-battle-of-the-builders

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

We have identified the core principle: digital ownership should only be transferable after the linked physical NFC tag has been cryptographically verified. A conceptual architecture and end-to-end transfer flow have been defined, but no CIP-0113 prototype, validator or testnet implementation exists yet.

The underlying TAGBASE components are already operational, including NFC identity creation, dynamic cryptographic verification, APIs, cloud infrastructure and mobile applications. The grant will cover the complete integration journey: technical design, programmable-token implementation, Cardano transaction service, wallet integration, testnet validation, security testing and mainnet deployment.
