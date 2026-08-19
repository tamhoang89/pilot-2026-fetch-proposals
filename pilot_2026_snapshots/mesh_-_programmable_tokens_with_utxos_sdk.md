# Mesh  - Programmable Tokens with UTXOS SDK

> Programmable Tokens by Mesh for UTXOS SDK

## Proposal Metadata

- **Status:** finalized
- **Revision:** 14
- **Proposer:** `stake1u8n6j94kn5ztrel7p343sezeysuf6u3arcd39s96vg8y9rgjklvn9`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-19T10:27:21.018000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

The Mesh team created and maintains UTXOS which has:

- \~2,000,000 downloads on NPM
- Powered major Cardano applications including CF, Minswap, FluidTokens, NMKR, Blinklabs, etc etc. More than 800 public projects depending on Mesh.\
  <https://github.com/MeshJS/mesh/network/dependents>


- Delivered 10+ successful Catalyst proposals  <https://gov.meshjs.dev/catalyst-proposals>)
- Comprehensive documentation and developer education materials
- Active maintenance and continuous improvement for 5+ years

UTXOS applies the same rigorous approach that made Mesh successful.

The Team for this proposal includes:

### **Jingles K.**

**Founder & CEO** - GitHub: @jinglescode - x: @jinglescode

Relevant Experience: - Creator and maintainer of Mesh, Cardano's most popular web3 framework - Full-stack blockchain developer with 8+ years experience - Multiple Cardano ecosystem contributions (open source tools, documentation, education)

### **Emmanuel A.**

**Tech Lead**

- GitHub: @temasar1
- x: @temasar_1

**Relevant Experience:**

- 5+ years of experience in blockchain with software and developer infrastructure.
- Lead developer and contributor across Cardano ecosystem projects and open-source tooling.
- Active contributor to Mesh and Gimbalabs.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

In cardano, we already have some serious projects like Andamio among others who are always ready to integrate our products.

with the social-login infrastructure our programmable native assets substandards would be much useful to game developers, while security programmable assets would be useful for compliance seekers.

- 210 fees in ADA and 700 transactions targets should be considered ambitious because the cip-113 is a new concept to cardano, in as much as we want to serve old and already aware cardano integrators we believe users would also come from other ecosystem, So it takes some level of technical understanding to get familiar to start using product.

Usage intervals depends on multiple factors like platforms demands but speculatively with the right user experience we expect consistent interval that would match the integrity standard.

### How will you reach and onboard real users - and what evidence backs your channels?

As infrastructure builders we will reach and onboard real users through direct developer outreach, targeted email campaigns and partnerships with projects preparing for production-scale adoption.

We are also part of CIP-113 Working Group on Telegram together with our dedicated Discord channel for UTXOS in mesh discord server filled with over 700 technical builders and executives building dapps, wallets and token infrastructures, also other various discord servers and developer channels, where we can directly identify teams interested in programmable-token infrastructure. Onboarding will be through our tokenization dashboard, Smart Wallets and SDK, supported by integration guides, demos and direct technical assistance with evidence from usage and adoption

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

The actual fact is UTXOS is Cardano's first production-ready Wallet-as-a-Service (WaaS) platform, enabling developers to integrate wallets into their applications with a single API call.

Our approach would win cause we already have experience, we are building on this with years of onboarding developers with the meshsdk in onboarding with track records of building what is needed and would be used rather than reinventing the wheel

### Please provide details about the Technology Readiness Level selected for your existing product

Readiness includes:

- Reliable API infrastructure
- Proven Cardano transaction and Wallet infrastructure with SDKs already operating in production
- Active documentation and developer integration resources

UTXOS has progressed beyond the prototype and development stage into real-world use. The platform currently provides infrastructure and developer tooling across three blockchain networks;

- Cardano
- Bitcoin,
- and spark a layer-2 on bitcoin

Our development has been driven by actual developer requirements rather than a purely theoretical roadmap, with new capabilities being developed, tested, deployed, and iterated based on real usage. This proposal therefore does not fund the creation of UTXOS itself. It extends an already operational infrastructure platform with cip-113

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

- CIP-113 Token substandard contracts The core token rules will be implemented through CIP-113 compatible Aiken validators because the CIP's implementation is built around Aiken. This allows us to remain aligned with the existing architecture
- Token parameters & Configuration Layer Each programmable token substandards will have an associated configuration and parameters defining the rules governing its lifecycle. Depending on the use case, these parameters are being exposed in a plug-and-play style through our sdk(APIs) and the platform itself.
- Dashboard management Our platform includes self-managed dashboards that allow developers and issuers to directly configure and interact with deployed programmable-token contracts.
- smart wallet integration: as a wallet as a service provider, this part is where we are mostly interested about cause the idea of smart wallet which holds the programmable token can be seemlessly integrated inside utxos, all tools and library already made and working fine.
- Compliance / Identity Integration: For applicable use cases, the architecture can consume verified KYC/KYB status, we've been meeting with Fairway infrastructure as credentials verifiers, so this translate verification into programmable-token conditions. The verification itself does not need to expose sensitive identity information on-chain; instead, the architecture can use appropriate attestations or verification state as the input to the programmable-token rules.

### 

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

Our target markets are enterprises, companies, and DApps within and outside the Cardano ecosystem that want to experiment with and integrate programmable tokens to their platform. UTXOS will expose the functionality through the @utxos/sdk, enabling developers to easily integrate programmable-asset creation, wallet interactions, and transaction capabilities directly into their platforms.

Since our mainnet launch, we've achieved:

- over 500 MAU
- over 4,000 sdk monthly downloads
- over 1000 monthly transactions on testnet and mainnet
- trusted and used by the ecosystem and developers
- 5 Active Projects in production using UTXOS infrastructure
- Stable v1 live on mainnet with proven reliability
- $200 Monthly Recurring Revenue from 1 paying enterprise customer

### Applicant name

MeshJS

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Our Existing business model is based on subscription in Tiers

Free, Pro ($199 Discounted Price), and Scale of $499 for Wallet as a Service, Transaction Sponsorship, Onramp

Programmable Tokens as a Service tiers:

### **Free**

- Limited Smart Wallet services
- Limited access to Programmable Native Asset features

### **Pro**

- Access capabilities to Free tier
- Increased number of managed smart wallets
- Limited access to Security Programmable Asset features

### **Scale**

- Access Free and Pro with advanced substandards
- Transaction sponsorship
- Dedicated support

On who pays, though the Basic Tier is free to experiment with, Paid tiers are targeted at enterprises, token issuers and DApps that require mainnet deployment and are serious about our infrastructure integration.

Product-market fit drives continued paid usage.

### Programmable tokens (CIP-0113) - expected transaction count

700

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This funding is important for the work that sits between "Yes, it works" and "If so, can developers can safely depend on it?" These contracts control the behavior of assets therefore security, testing, and operational reliability are critical.

Funding will be focused on

- Core engineering and integration: completing the integration of CIP-113 substandard contracts and off-chain infrastructure
- Security and independent review: allocating resources toward professional security review and contract auditing of the programmable token implementation
- Scalability and operational infrastructure: improving on high scalability, monitoring infrastructure capacity.
- Contract correctness and testing: developing comprehensive unit, integration, property-based, and end-to-end tests.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

## **1. Contracts/Substandards**

- **Programmable Native Asset (PNA):** User, Admin, Owner roles, mint/burn controls, max mint, max supply, blacklist and global pause, holding limits.

- **Security Programmable Asset (SPA):** Extends PNA with KYC/KYB registry, compliance, verifier roles, freeze, seize, force-transfer and compliance controls.

- **Event triggered assets:** Milestone-triggered release, Time/event expiry, bounties unlock, token vesting.

## **2. Security & Audit**

- Unit, integration and end-to-end testing.
- Threat modelling and security review.

## **3. Wallet Infrastructure & SDK**

- Social-login auth and smart wallet interactions.
- Programmable asset transaction construction and signing.
- PNA/SPA and Event triggered SDK APIs and on-chain to off-chain state interaction.

## **4. Infrastructure & Documentation**

- Mainnet deployment and contract configuration.
- API documentation, integration guides, release notes and test evidence.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### Programmable tokens (CIP-0113) - fee target (ADA)

210

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

The main problem we address:

Right now, available major non-custodian are yet to implement smart wallet features which hold programmable tokens.

Our Solution:

We implement CIP-113 substandard smart contracts with UTXOS Wallet social-login infrastructure, allowing applications to create smart wallets through social-login (google, discord, twitter) authentication and immediately construct, sign and submit programmable-token transactions. This removes the friction of requiring users to first connect or configure specialized wallet providers and gives DApps a simpler path to integrating programmable assets. 

The initial infrastructure will support what we call the Programmable Native Assets (PNA) with configurable minting, burning, supply limits, transfer controls and administration, alongside Security Programmable Assets (SPA) supporting compliance-oriented capabilities such as KYC and KYB, freeze, seize and force-transfer.

Developers will be able to integrate these capabilities through the Mesh SDK and demonstrate flows such as creating a programmable token with minting according to defined rules, transferring it through a smart wallet and extending the infrastructure.

### Supporting links (repo, site, demo)

- https://meshjs.dev/
- https://github.com/MeshJS/wallet

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

Apache 2.0 Licence

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

We assessed at TRL-6 because our already made infrastructure has already been demonstrated in relevant Cardano environments, while the programmable-asset layer is being integrated and validated on top of this existing infrastructure.

There is also strong evidence from the wider ecosystem these already built infrastructure can be exposed to a higher-level programmable platform. example Privy (<https://privy.io/>) demonstrate how wallet infrastructure, controls and hosts tokenization on ethereum which are can be abstracted for application developers, can also be demonstrated on cardano

we will apply this proven infrastructure model to architect and demonste a cardano's Programmable native assets and Security programmable assets with the cip-113 substandards
