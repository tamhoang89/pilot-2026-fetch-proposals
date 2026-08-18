# ProcureFlow Verified Quote Rail

> Verifiable supplier quotes on WhatsApp, powered by Cardano for tamper-proof procurement compliance.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 12
- **Proposer:** `stake1u9eelt7nfc4082z6s3pr2vpjaepuqkqkd4zdsghwxy9jh2culxr6l`
- **Funding requested:** ₳75,000
- **Last finalized:** 2026-08-18T11:29:45.827000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Our team is well-suited to deliver this because we are already building Procure Africa to digitise procurement for African markets, and this proposal grows directly out of that work. Through Procure Africa, we have been developing a real procurement workflow for RFQs, supplier engagement, and quote collection, using WhatsApp and AI-assisted sourcing to fit the way procurement actually happens in the market. That gives us practical experience with the buyer and supplier pain points this project solves, rather than a theoretical understanding of them.

We also already have exposure to the target users we need to reach. Our work in Procure Africa has helped us identify manufacturers, importers, distributors, and procurement-heavy organisations that need faster quoting, stronger traceability, and cleaner workflow control. We are also pending a POC with an importer client, which gives us a concrete path to validate the solution with a real user and refine it based on live feedback.

In addition, our background in procurement automation and compliance-oriented workflow design means we understand both the operational and trust layers of the problem. We know how to structure RFQs, onboard suppliers, manage quote flows, and reduce friction for adoption. This project is therefore not a new direction for us, but a focused extension of the infrastructure we are already building to help African businesses source, trade, and operate more efficiently.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

We are building this extension based on two years of experience running the platform, during which we have grown a supplier database of 1,000 and continuously gathered feedback on the pain points suppliers face when responding to procurement demand. Suppliers have told us they need faster RFQ turnaround, better visibility into opportunities, stronger quote tracking, and a way to trade even when buyers are not active on the platform. This product directly addresses those needs by giving suppliers a practical way to receive, manage, and respond to opportunities more efficiently.

In addition, we will notify suppliers on WhatsApp whenever new opportunities are posted on other tender sites, encouraging them to come to the platform to request, manage, and respond to quotes. This gives suppliers immediate visibility into opportunities they might otherwise miss, while also driving them into our workflow where we can structure the RFQ process, improve response speed, and preserve quote integrity.

### How will you reach and onboard real users - and what evidence backs your channels?

We will reach and onboard users through our existing Procure Africa network, which already gives us direct access to manufacturers, importers, and distributors who actively respond to RFQs. Our experience running the online marketplace has shown us which suppliers are responsive, which buyers generate recurring demand, and where quote friction is highest. That gives us a warm-start channel rather than a cold launch. We are also in discussions for a POC with an importer client, which will let us validate the workflow with a real user and create an early reference case. Our onboarding strategy is supplier-first: we will invite source suppliers into a WhatsApp-based pilot, then expand to buyers once there is active quote traffic.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

In South Africa, the main alternatives are general procurement suites, quotation tools, and manual WhatsApp/email workflows. These systems help with sourcing or quote generation, but they usually do not make quotes identity-bound, time-limited, and tamper-evident. Our approach wins because it fits how procurement already happens locally: on WhatsApp, through informal supplier networks, and under real compliance pressure. It gives suppliers faster quoting and buyers better auditability without forcing them into a heavy enterprise system.

### Please provide details about the Technology Readiness Level selected for your existing product

We have selected a Technology Readiness Level consistent with an MVP that is ready for proof of concept and integration. The core workflow is already built and usable, including RFQ intake, supplier engagement, and quote handling through our existing procurement flow. What remains is validating the solution in a live client environment, integrating with the customer’s operating process, and refining based on real-world usage. This places the product beyond concept or prototype stage and into a pre-commercial, pilot-ready phase where the next step is structured POC deployment and production hardening.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Our on-chain architecture is lightweight: the procurement workflow stays off-chain in ProcureFlow, while Cardano anchors identity, quote provenance, approvals, and audit events. Each RFQ and quote gets a unique on-chain reference linked to the off-chain record, making the history tamper-evident without forcing the whole process onto the chain.

This fits the use case because procurement needs low-cost trust events, not heavy on-chain computation. It also keeps the product fast and easy to use through WhatsApp and web, while still giving buyers and auditors verifiable records.

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

Our primary target market is manufacturers, importers, and distributors in South Africa who receive frequent RFQs and need a faster, more reliable way to manage supplier quoting through WhatsApp. Our secondary market is procurement-heavy organizations such as SMEs, NGOs, municipalities, and enterprise buyers that need cleaner quote provenance, stronger audit trails, and better compliance in sourcing workflows. Evidence of demand already exists in the widespread use of WhatsApp and fragmented vendor channels for procurement coordination, as well as in the growing adoption of WhatsApp-based procurement and vendor-management tools that aim to reduce turnaround time and simplify RFQ handling. Our solution improves on these existing behaviors by making quote submissions identity-bound, time-limited, and auditable, so suppliers gain immediate operational value while buyers gain traceability and compliance.

### Applicant name

Tseliso Mosiuoa

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Our business model is a transaction-based SaaS model built around procurement workflow usage. During the pilot, grant funding supports product development and onboarding, but after that the platform is sustained by the organizations that benefit directly from faster quoting, cleaner audit trails, and reduced procurement friction. Buyers and suppliers pay for premium workflow features such as verified quote handling, audit exports, supplier management, analytics, and compliance controls. In some cases, larger buyers or procurement teams may sponsor supplier access to accelerate adoption. Usage continues after the grant because the product sits inside an active business process: suppliers keep receiving RFQs, buyers keep comparing quotes, and both sides keep needing traceability, speed, and compliance. The more the network is used, the more valuable it becomes, which creates natural retention beyond the pilot.

### On-chain identity (CIP-0170) - expected transaction count

40

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding would let us turn a working procurement MVP into a live, Cardano-anchored pilot with real users and verifiable audit trails. Without it, we would keep iterating internally, but we would not be able to complete the integration, onboard suppliers and buyers, and validate the model in market.

It will be spent on:

- Cardano integration for identity, provenance, and audit events.

- Product hardening for the RFQ-to-quote workflow.

- Pilot onboarding and support.

- Testing, deployment, and infrastructure.

- Refinements from live POC feedback.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within the 3-month window, we will deliver a mainnet-ready pilot of ProcureFlow Verified Quote Rail with the following measurable outputs:

- A working RFQ-to-quote workflow on WhatsApp and web.

- Supplier identity binding for quote origin and provenance.

- On-chain quote references for submitted, updated, approved, and rejected quotes.

- A buyer review dashboard and supplier quote history view.

- At least one live client POC integrated into the workflow.

- A minimum pilot set of active suppliers onboarded from our existing database.

- Live mainnet transactions proving quote and identity activity.

- Audit logs and exportable records for compliance review.

- Basic monitoring, support, and deployment hardening for pilot use.

- A short pilot report showing usage, feedback, and next-step recommendations.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

80

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

We are building **ProcureFlow Verified Quote Rail**: a WhatsApp-first supplier quoting workflow that lets manufacturers, importers, and distributors issue identity-bound, time-limited quotes directly to buyers, with tamper-evident audit trails.

It solves the problem of **slow, opaque, and often manipulated RFQ handling** in procurement, where intermediaries frequently source quotes from downstream suppliers without clear provenance, causing delays, compliance risk, price distortion, and poor auditability.

It is built for:

- **Manufacturers, importers, and distributors** who need a faster, safer way to receive and manage RFQs.

- **Procurement teams, SMEs, NGOs, and government-adjacent buyers** who need cleaner quote records and better traceability.

- **Organizations operating in regulated or audit-heavy environments** that need provable quote origin, expiry, and approval history.

### Supporting links (repo, site, demo)

- https://procureafrica.co.za

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

We selected **Technology Concept Formulated** because the integration has been clearly defined, but not yet fully built. The product workflow and Cardano trust layer are designed, and the next step is to validate the integration through a POC and client testing.
