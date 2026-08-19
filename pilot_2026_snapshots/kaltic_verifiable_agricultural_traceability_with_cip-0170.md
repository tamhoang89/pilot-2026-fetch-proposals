# Kaltic: Verifiable Agricultural Traceability with CIP-0170

> Turn agricultural traceability records into verifiable claims: farms, packers and exporters attest who created each record through CIP-0170 on Cardano

## Proposal Metadata

- **Status:** finalized
- **Revision:** 5
- **Proposer:** `stake1uy46yvqwywwvsr5ak3wmszg5ps4zl3cyxcyjde5kq05qg9cpcmepk`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-19T14:10:52.855000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Cristian Rojas — Founder & Technical Lead\
LinkedIn: <https://www.linkedin.com/in/cristian-rojas-cardano-community/>\
GitHub: <https://github.com/Crisro0787>\
X: @CrisRo0787 | Cardano Forum: @Cristian_Jair_Rojas | [Kaltic.app](http://Kaltic.app)

Cristian designed and developed Kaltic’s current TRL 6 MVP, including product architecture, agricultural traceability workflows, Cardano testnet integration, Digital Product Passports and backend components. Public technical documentation and evidence are available through GitHub. He will lead the CIP-0170 architecture, implementation, testing and mainnet deployment.

Cristian has been active in Cardano since 2021 and is a Cardano Ambassador. He is an Industrial Engineer specialized in supply-chain processes, with experience in compliance and management standards such as ISO 9001, combining technical, supply-chain and compliance expertise under one project lead.

Kaltic plans to recruit a junior web developer for frontend, UI, APIs, testing and other non-blockchain work. Candidates include university programming students previously onboarded to Cardano by Cristian, including CBCA-certified students.

Pilot/user operations support may also be contracted for onboarding, training, coordination and feedback with farms and packers. These roles add execution capacity; core delivery remains founder-led.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If Kaltic reaches **USD 50,000 in cumulative commercial revenue**, we pledge to return **2% of subsequent revenue** to the Cardano Treasury until a maximum of **USD 2,000 equivalent** has been contributed. Payments will be made in ADA at market value when each payment is due.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Kaltic targets 450 real transactions and 160 ADA in counted fees during the adoption period.

Usage comes from farms, packers and other agricultural operators using Kaltic in normal traceability workflows. Each organization uses its own external wallet and CIP-0170 identity. Events such as harvest, receipt and transfer can generate signed attestations linking each record to the responsible organization.

Initial users will come from the Zacatlán and Aquixtla pilot channels, where anchor organizations can introduce multiple independent users.

For the minimum six-epoch window, the 160 ADA target requires 13.33 ADA in each of the first three floored epochs and 26.67 ADA in each of the final three. We will use the floorless entry epoch to ramp users, plan above every epoch floor, and target roughly 15 transactions/day toward 450 total. We will maintain more than the required 5 external wallets and monitor activity daily so no day is relied upon for more than the Standard’s 20% cap. We do not plan to rely on the one-miss allowance.

Usage comes from recurring operations, not rewards or transaction incentives; participants pay their own network fees.

### How will you reach and onboard real users - and what evidence backs your channels?

Our go-to-market starts with agricultural organizations that aggregate producers rather than acquiring farms one by one.

Our first channel is Finca La Concordia / Berries Club in Zacatlán. Our second is the greenhouse and packing cluster in Aquixtla, where packers/exporters can introduce Kaltic across supplier networks.

The confirmations cover Kaltic’s current testnet pilots, not pre-committed CIP-0170 mainnet users. They evidence existing relationships and an onboarding channel. They are being signed on 19 August 2026 and will be uploaded before the deadline.

If funded, these networks will be first invited to onboard independent KERI identities and external wallets.

Days 1–3: onboarding and first attestations; Days 4–7: partner-introduced users and repeat use; Days 8–10: resolve issues and verify independent use; Days 11–14: expand active users and establish recurring activity.

Confirmations: <https://drive.google.com/drive/folders/17mUh6nB6Xs9cWbKb6fjWMVVOhgSz2jD2?usp=sharing>

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The main alternatives are spreadsheets/manual records and traceability platforms such as FoodLogiQ and iFoodDS, which help companies capture CTE/KDE data and support FSMA 204 compliance.

Kaltic focuses specifically on Mexican agricultural producers and first-mile operators, with simple workflows designed around how farms already record harvest and shipment data.

Its differentiation is verifiability: Kaltic creates Digital Product Passports and, through the proposed CIP-0170 integration, will let organizations cryptographically attest to the records they create. This adds a portable, tamper-evident link between a supply-chain claim and the organization responsible for it, without requiring users to replace their entire operational workflow.

### Please provide details about the Technology Readiness Level selected for your existing product

A functional MVP is deployed on the Cardano Pre-production testnet. It implements realistic agricultural traceability workflows: farm and field registration, harvest records, and the creation of verifiable on-chain records linked to operational data.

The MVP already connects its application layer with Cardano transactions and has been used to test the complete workflow from capturing agricultural data to generating a user-facing traceability record with corresponding blockchain evidence.

**Evidence:**\
Kaltic app: <https://kaltic.app/jw/web/login>\
User: Pilot_2026\
Password: catalyst2026\
Cardano testnet tx example:\
[Harvesting Record](https://preprod.cardanoscan.io/transaction/2a42fb79867b948d5990dd564abee307b404de54cdcdd6d78dea84a4039b472b)

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Kaltic uses a hybrid architecture: operational and potentially sensitive supply-chain data remains in the application layer, while Cardano provides the immutable verification and identity-attestation layer.

For the CIP-0170 integration, each participating organization will be associated with a KERI Autonomic Identifier (AID) and its Key Event Log (KEL). Signing authority will be established on Cardano using the CIP-0170 `AUTH_BEGIN` flow and an appropriate credential chain.

When a user records a supply-chain event in Kaltic, such as a harvest, receipt or transfer.\
Kaltic generates a canonical record and digest. The organization responsible for that event anchors the digest in its KERI event log and creates a CIP-0170 `ATTEST` transaction containing its AID, digest, KERI sequence number and application metadata under Cardano metadata label 170.

The Cardano transaction is submitted from the participating organization’s wallet rather than a Kaltic-controlled wallet. Kaltic then indexes the transaction and verifies the attestation against the organization’s KEL before displaying it as verified within the Digital Product Passport.

This architecture fits CIP-0170 because Cardano stores the persistent identity-to-record binding while KERI provides key continuity, signing authority and independent cryptographic verification. It also avoids placing sensitive operational data directly on-chain.

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

Kaltic’s initial target market is Mexican agricultural producers, farms, packers, and other supply-chain operators serving regulated and export-oriented markets, especially the United States.

The market is significant: U.S. agricultural imports from Mexico averaged about **$43.8B annually in 2021–2025** (USDA ERS: <https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/agricultural-trade>). In horticulture, Mexico supplied **63% of U.S. vegetable imports and 47% of fruit and nut imports in 2023** (USDA ERS: <https://www.ers.usda.gov/amber-waves/2024/october/growth-in-mexico-s-horticultural-exports-to-the-united-states-continued-even-as-new-u-s-food-safety-laws-took-effect>).

Demand is reinforced by regulation. FDA’s Food Traceability Rule (FSMA 204) requires additional traceability records for covered foods, including foreign firms supplying the U.S. market (FDA: <https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods>).

Kaltic is at the pilot-validation stage. A working agricultural traceability MVP has been built, and upcoming pilots with agricultural operators will test real workflows, usability, and traceability data exchange before broader commercialization.

### Applicant name

Cristian Jair Rojas Velez

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Kaltic uses a B2B, usage-based model. Exporters, packers, cooperatives and other supply-chain operators pay based on the volume of traceability records processed, either per record or through monthly plans with included record volumes.

This aligns revenue with actual operational use: every new harvest, receipt, transfer or transformation creates a traceability record and, through the proposed CIP-0170 integration, can generate a verifiable organizational attestation on Cardano.

Usage therefore continues after the pilot because customers need to create new records as part of their normal supply-chain and compliance operations. As customer volume grows, both Kaltic revenue and genuine Cardano activity grow with it, without subsidizing transactions.

### On-chain identity (CIP-0170) - expected transaction count

450

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Kaltic’s current TRL 6 MVP was funded by a previous Catalyst proposal, no previously funded work is included here. This 50,000 ADA grant funds the next stage: 20,000 ADA for the new CIP-0170 integration through mainnet delivery, and 30,000 ADA for adoption operations after M1.

The build budget covers architecture, identity onboarding, attestations, DPP verification, mainnet deployment and testing. The adoption budget supports onboarding real agricultural users, field operations, travel/logistics, outreach, user support and retention.

Without this funding, the founder would need to prioritize external paid work and this expansion would slow significantly.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, Kaltic will deliver its CIP-0170 integration on Cardano mainnet:

1. Architecture/specification — 2,000 ADA: KERI AIDs, signing flow, metadata 170, verification and privacy.
2. Identity onboarding — 3,000 ADA: organizational AIDs and external-wallet linking.
3. CIP-0170 attestation engine — 6,000 ADA: reusable attestations across at least 3 traceability event types.
4. Verification/DPP integration — 3,000 ADA: automatic verification and visible on-chain evidence.
5. Mainnet deployment/testing — 3,000 ADA: production release and independent real-user attestations.
6. Evidence/release package — 1,000 ADA: footprint, release notes, testing, security note and demo.
7. Initial user onboarding & field preparation — 2,000 ADA: prepare pilot organizations for mainnet use and the adoption phase.

**Initial Build/M1 budget: 20,000 ADA.**

### How far along is the integration you're proposing, today?

TRL 1 - Basic principles observed

### On-chain identity (CIP-0170) - fee target (ADA)

160

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

**Kaltic is a digital traceability platform for agricultural supply chains, starting with farms and other operators that need to maintain and share reliable records for regulatory compliance and commercial traceability.**

Today, critical supply-chain events such as harvesting, receiving, packing, and transformation are often recorded across disconnected systems, spreadsheets, documents, or messages. This makes it difficult for buyers, auditors, and other participants to verify not only that a record has not been altered, but also **which organization was responsible for making that claim**.

Kaltic turns these events into structured digital traceability records and product passports. Through this project, Kaltic will integrate **CIP-0170 on-chain identity attestations** so participating organizations can cryptographically attest to the records they create, linking supply-chain data to a persistent, verifiable organizational identity on Cardano.

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

All research and software architecture documentation, as well as the prototype, will be made public. operated under a open source [**GNU General Public License**](https://www.gnu.org/licenses/gpl-3.0.en.html)

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Current funded commitments

**Project Catalyst —** Project ID1100136 **— Project Lead.**\
This funded project covers development of Kaltic through its current agricultural traceability MVP (TRL 6), including pilot testing and final reporting.\
\
M1 and M2 have been delivered and approved, the remaining M3 and M4 outputs are in their final delivery stage and are expected to be submitted no later than **7 September 2026**.

The scope of this new application does not duplicate previously funded work. The existing Catalyst project delivers Kaltic’s current MVP, this proposal begins from that point and funds the new **CIP-0170 integration, mainnet deployment and adoption phase**.\
\
The project is currently beyond the program’s 90-day/12-month good-standing thresholds; I have contacted Catalyst/Fund Operator to disclose the circumstances and request acceptance of the valid reason while the remaining milestones are being completed.

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed CIP-0170 integration is currently at **TRL 1: Basic principles observed**.

Kaltic is already a functioning agricultural traceability product, but CIP-0170 has not yet been implemented or formally architected within the platform. We have identified a clear use case for the primitive: linking agricultural traceability records to verifiable organizational identities so the actor responsible for a supply-chain claim can cryptographically attest to it.
