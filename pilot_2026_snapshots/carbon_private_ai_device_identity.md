# Carbon Private AI Device Identity

> Private, verifiable identity and repair attestations for AI devices on Cardano, without exposing raw device data.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 14
- **Proposer:** `stake1u87jngdwz3p52h6te3lf9hlehaecr29ljv9csey2wy0l4gquf9y05`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-20T05:55:38.780000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Carbon is currently led by Guanbo Yu, who is responsible for product direction, system architecture, implementation coordination, pilot deployment and user validation.

The project is intentionally small and execution-focused. Development uses an AI-assisted engineering workflow together with local private AI infrastructure for coding, testing, documentation and evaluation. This allows a small team to build and validate the initial system efficiently.

The team already operates private AI hardware and local model environments and has practical experience testing AI automation, device integration and real-world service workflows.

For specialized Cardano components, the project will use open-source Cardano tooling and, where necessary, engage experienced Cardano developers for focused technical review and integration work.

The pilot is deliberately scoped so that delivery does not depend on building a large organization. The core objective is a working open-source implementation, deployed pilot nodes, real attestations and measurable user validation.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

Not applicable.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Carbon will create real Cardano usage through AI device identity and verifiable attestations.

Initial users are private AI operators, repair/inspection providers and small teams running local AI hardware. They need proof of which device or AI agent performed an action without exposing prompts, files, credentials or model data.

Pilot target: 50 active users and 200 on-chain identity/attestation transactions. Each device creates an identity event and later attestations for selected tasks, repairs, inspections or verification events.

Success will be measured by active devices, completed attestations, repeat usage, failed transactions and average verification cost.

After the pilot, the open-source implementation can be reused by other developers and service providers.

### How will you reach and onboard real users - and what evidence backs your channels?

We will begin with direct pilot users rather than broad advertising. Initial channels include private AI operators, repair technicians, equipment owners, refurbishment/ITAD contacts and existing business networks in Vietnam and Southeast Asia.

The pilot will provide a simple workflow: register an identity, issue a repair or inspection attestation, and independently verify it.

Adoption will be tracked through real activated identities, completed attestations, repeat users and integrations. Pilot feedback will be used to simplify onboarding before expanding through open-source communities, Cardano developers and commercial partners.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Existing alternatives include centralized device-management databases, repair-management systems, digital certificates and generic blockchain timestamping.

Carbon differs by combining persistent device/operator identity with verifiable repair and inspection attestations. Raw private data stays off-chain while Cardano provides a durable verification layer.

The goal is not to replace existing repair or asset-management software. Carbon provides an interoperable trust layer that those systems can integrate with, reducing vendor lock-in and allowing records to remain independently verifiable.

### Please provide details about the Technology Readiness Level selected for your existing product

Carbon has a working prototype for private AI operation, local model orchestration, device workflows, structured memory/state and automated task execution. These components have been tested on real privately controlled AI hardware. Local inference, state persistence and device automation are functioning. The Cardano identity layer is the new integration: CIP-0170/KERI has not yet reached production deployment. The current product is therefore TRL 4: core components have been validated in a controlled environment, while Cardano identity and attestation require implementation, testnet validation and mainnet deployment.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Carbon uses a hybrid architecture: private data and AI computation remain on the user's device, while Cardano provides a public verification and trust layer.

Each participating AI device maintains a local identity and signing capability. A CIP-0170/KERI-compatible identity layer represents the device or agent identity and supports key rotation and verification. When an AI device performs an eligible action, Carbon creates a signed attestation containing only the minimum verification data, such as an identity reference, event type, timestamp and cryptographic hash.

Raw prompts, private model data, files, credentials and user content remain local. Only verification proofs or references are anchored to Cardano.

This architecture fits private AI because blockchain is used for what it does well—shared verification, provenance and durable public evidence—without turning private AI data into public blockchain data. It also allows independent software, repair services or AI applications to verify that an attestation came from the expected device identity.

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

Our initial market is operators of private AI systems, repair and inspection providers, ITAD/refurbishment companies, and owners of valuable equipment who need trustworthy device and service records.

The immediate problem is practical: AI devices, repairs, inspections and equipment handovers generate records that are usually stored in local files, PDFs, spreadsheets or vendor databases. These records are difficult for another party to independently verify.

We will validate demand during the pilot with real private AI nodes and repair/inspection workflows. Success will be measured by activated identities, completed attestations, repeat usage and external verification of those attestations.

### Applicant name

YU GUANGBO

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The open-source core will remain free. Revenue will come from optional commercial services around the protocol: managed deployment, enterprise integration, private infrastructure setup, support, customized workflows and higher-volume attestation services.

Individual users and developers can self-host the open-source software. Businesses that require installation, integration, maintenance or operational support can pay for these services.

This model allows the Cardano integration to remain open and reusable while creating a sustainable service business without selling user data.

### On-chain identity (CIP-0170) - expected transaction count

100

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding converts the existing private-AI prototype into a reproducible Cardano-integrated pilot. It enables dedicated implementation of the CIP-0170/KERI identity layer, Cardano testnet and mainnet integration, security and interoperability testing, documentation, open-source packaging and deployment on multiple pilot devices. It also supports real-user validation and measurement of issued and verified attestations. Without funding, Carbon can continue local AI development, but the Cardano integration would remain a low-priority experiment. Funding creates the focused engineering capacity needed to deliver and validate the integration as a reusable open-source component.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within three months before mainnet launch, Carbon will deliver a working end-to-end prototype for private AI device identity and repair/inspection attestation.

The deliverable will include a public test interface, CIP-0170-based identity registration, KERI-linked identity evidence, and a complete Cardano testnet transaction flow.

At least one real user will complete the full workflow successfully.

We will publish transaction hashes, test evidence, technical documentation, architecture notes, and an open-source reference implementation.

The workflow will be repeatable and independently verifiable without exposing the user’s private AI data.

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### On-chain identity (CIP-0170) - fee target (ADA)

101

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Carbon is building a private AI device identity and repair/inspection attestation layer on Cardano.

Today, private AI computers, refurbished devices, repair records and inspection results are usually stored in local files, chats, PDFs or vendor databases. These records are easy to lose, difficult to verify independently, and do not provide a persistent identity showing who or what device was authorized to create them.

Carbon solves this by linking a persistent KERI-based identity to Cardano through CIP-0170. Sensitive operational data remains off-chain, while Cardano stores only the minimum identity and attestation reference required for verification.

The first product supports two workflows:

1\. Private AI Device Identity — a persistent identity for a privately operated AI node or workstation that can survive model upgrades or hardware changes.

2\. Repair & Inspection Attestation — a tamper-evident record showing that an authorized operator performed a repair, inspection, validation or equipment handover.

Initial users are private AI operators, repair and inspection providers, refurbishment/ITAD operators, and equipment owners who need verifiable service history without giving up control of their private data.

### Supporting links (repo, site, demo)

- https://github.com/yuguanbo020-svg 

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

### Licensing / IP details

Carbon will be released as open source under the Apache License 2.0. Source code, documentation and Cardano integration will be published in a public GitHub repository. Users retain ownership of their local AI data, device identity and private model data. No private data, wallet keys or recovery phrases will be published. Third-party components retain their original licenses.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed Cardano integration is at an early prototype stage. Carbon's local AI, device identity and attestation workflow already exists independently of Cardano. The funded work will add a CIP-0170/KERI-compatible identity layer and Cardano anchoring for verifiable attestations. Initial work will define the identity schema, key lifecycle, attestation format and Cardano transaction interface, followed by testnet implementation, interoperability tests and a reproducible public demonstration. The integration itself is not claimed as production-ready today.
