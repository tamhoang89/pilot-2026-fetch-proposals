# Built-In RWA & KYC/AML Rules for CIP-0113 Tokens

> Compliance, not code - programmable rules for real-world asset tokens.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 8
- **Proposer:** `stake1uyauluwnjuvzkmdgudj30nuxvyarg2zqdspdlluw3286d0cxv8y35`
- **Funding requested:** ₳115,000
- **Last finalized:** 2026-08-16T00:14:23.917000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

I have shipped and operate [mintmytoken.today](http://mintmytoken.today) in production today, including its CIP-0113 vesting/streaming feature, direct, verifiable proof I can design and deploy programmable-token logic on Cardano mainnet, not just propose it.

- Full-stack development (Flask/PyCardano stack) and Plutus V3/Aiken smart contract development.

- Already implemented CIP-0113 validator logic in production (mintmytoken's vesting feature) - this compliance module extends existing, working infrastructure rather than starting from zero.

- Hands-on experience with complex on-chain validator logic and security testing, including resolving deep transaction-encoding and hardware-signer edge cases in prior work.

- Administrator of a community group, giving direct access to real early users for the adoption phase rather than a cold-start audience.

- Role: compliance rule-engine design, validator development, mainnet deployment - solo-owned end to end.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

If this feature reaches sustainable commercial revenue, we pledge 10% of net revenue from it to the Cardano treasury, capped at ₳115,000, activating once annual revenue from it exceeds ₳100,000.

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: RWA issuers configuring and minting compliance-enabled tokens on [mintmytoken.today](http://mintmytoken.today), plus verified counterparties (investors, fund participants) receiving/transferring under enforced rules.

Why: Issuers need enforceable on-chain compliance — eligibility, jurisdiction restrictions, transfer freezes — which today requires custom smart-contract development. This turns it into form-based configuration inside a platform they already use.

How often: Each issuer generates a token-creation transaction, periodic eligibility-list updates as rosters change, and a compliant transfer each time tokens move — realistically 4–5 qualifying transactions per issuer/investor group, not a single one-off mint.

Justification: 350 transactions and ₳200 in fees is grounded in \~70–90 real users at 4–5 transactions each, consistent with RWA issuance being lower-volume, higher-value than simple minting. Compliance-checked transfers execute on-chain validator/rule logic, carrying higher script-execution fees than a bare transfer — supporting ₳200 with real margin above the ₳152 floor.

### How will you reach and onboard real users - and what evidence backs your channels?

Existing channels: [mintmytoken.today](http://mintmytoken.today)'s live user base and an existing Cardano community network. Usage tracked through distinct wallets minting and transacting compliance-enabled tokens.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Alternatives: Issuers write bespoke Plutus/Aiken compliance validators themselves, or use off-chain KYC gating that isn't actually enforced by the token contract itself (meaning compliance can be bypassed once tokens leave the issuing platform). Our advantage: On-chain enforcement (not just off-chain gatekeeping at mint time) means compliance rules travel with the token itself - an unauthorized wallet genuinely cannot receive or hold it, not just "isn't supposed to." This is a stronger compliance guarantee than most alternatives, delivered through a form instead of custom code.

### Please provide details about the Technology Readiness Level selected for your existing product

[mintmytoken.today](http://mintmytoken.today) is a live, publicly accessible Cardano token-minting platform with a full CIP-30 wallet-connect flow, real users, and real mainnet minting transactions today.

- [mintmytoken.today](http://mintmytoken.today): <https://mintmytoken.today>
- The platform already includes a shipped, working CIP-0113 vesting/streaming feature - direct evidence of production programmable-token infrastructure, not a prototype.
- The Pilot does not fund [mintmytoken.today](http://mintmytoken.today)'s existing minting or vesting features. It builds a new compliance rule-engine module on top of this already-operational, already CIP-0113-integrated product.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

- **Standard/vesting minting layer** (existing, live): [mintmytoken.today](http://mintmytoken.today)'s shipped minting and CIP-0113 vesting flow, unchanged.
- **Rule configuration layer** (new): form-based interface for issuers to define eligibility lists, jurisdiction restrictions, and freeze/revocation conditions.
- **Compliance validator layer** (new): CIP-0113-compliant Plutus/Aiken logic enforcing configured rules at transfer time, rejecting transactions that violate eligibility conditions.
- **Registry/allowlist layer** (new): on-chain or hybrid on/off-chain eligibility list the validator checks against, updatable by the issuer.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Programmable tokens (CIP-0113)

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

Target market: RWA issuers, regulated fund managers, and businesses on Cardano needing enforceable investor-eligibility rules — a segment explicitly named as a priority growth area across the wider Cardano ecosystem. Evidence: [mintmytoken.today](http://mintmytoken.today) is live with real users and real mainnet transactions, and has already shipped a CIP-0113 vesting/streaming feature - direct proof this platform can ship programmable-token infrastructure quickly and reliably. RWA and compliance tooling is a natural next module on the same infrastructure.

### Applicant name

Daniel Micov

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Revenue: [mintmytoken.today](http://mintmytoken.today)'s existing pure-profit fee model (costs paid from the user's wallet) extends directly to compliance-enabled token minting - issuers pay standard platform fees plus a premium for compliance-rule configuration. Why usage continues: Once live, this is a permanent platform feature generating ongoing transaction/fee revenue independent of grant funding, and RWA issuance is a growing, recurring category rather than a one-off use case.

### Programmable tokens (CIP-0113) - expected transaction count

350

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

₳115,000 funds new Pilot work only:

- ₳34,000: Compliance validator logic (eligibility, jurisdiction, transfer-freeze conditions)
- ₳23,000: Rule-configuration UI
- ₳19,000: Eligibility/allowlist registry system
- ₳17,000: Testnet validation and security testing (rule-bypass resistance)
- ₳12,000: Mainnet deployment and integration into existing minting flow
- ₳6,000: Open-source rule-engine templates and documentation
- ₳4,000: User onboarding, launch activities, adoption measurement

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Compliance rule-configuration UI live on [mintmytoken.today](http://mintmytoken.today).
- CIP-0113-compliant compliance validator logic built and tested on preprod.
- Eligibility/allowlist registry system functional, with issuer-side management tools.
- End-to-end flow live on mainnet: issuer configures rules → compliant token minted → eligible transfer succeeds, ineligible transfer rejected on-chain.
- Mainnet deployment with the Pilot-required message tag and declared identifiers.
- Open-source rule-engine templates and integration documentation published.
- Security testing completed (rule-bypass resistance, eligibility edge cases).
- Live product, tagged repository release, release notes, transaction evidence, and Demo Day presentation.

### How far along is the integration you're proposing, today?

TRL 3 - Experimental proof of concept

### Programmable tokens (CIP-0113) - fee target (ADA)

200

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Problem: Real-world asset (RWA) tokenization on Cardano — tokenized securities, regulated fund shares, real-estate fractions, or any asset requiring investor eligibility checks — currently has no accessible way to enforce compliance rules on-chain. Issuers wanting to restrict who can hold or transfer a token (verified/accredited investors only, jurisdiction restrictions, transfer freezes for sanctioned addresses) must write custom Plutus/Aiken validators from scratch, which puts RWA tokenization on Cardano out of reach for most issuers.

Target users: Businesses and projects wanting to tokenize real-world assets on Cardano (funds, real estate, regulated securities, loyalty programs with eligibility rules) without hiring dedicated smart-contract compliance engineers.

Solution: Extend [mintmytoken.today](http://mintmytoken.today)'s existing CIP-0113 programmable-token infrastructure (already live via a shipped vesting/streaming feature) with a **compliance rule engine** — a form-based configuration layer letting issuers attach enforceable, on-chain KYC/AML and eligibility logic directly to a token at mint time, with zero custom code required.

Outcome: The first accessible, no-code compliance layer for CIP-0113 tokens on Cardano — turning RWA tokenization from a bespoke, multi-week engineering project into a configuration flow inside a platform issuers already use.

### Supporting links (repo, site, demo)

- https://mintmytoken.today

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

- License: MIT for all open-sourced components.
- Open-source outputs: CIP-0113 compliance validator logic, rule-configuration schema, integration documentation, and reference examples
- This covers the new compliance module built under this grant. The broader [mintmytoken.today](http://mintmytoken.today) commercial platform (unrelated core minting infrastructure) remains closed-source.
- Third-party IP: Koios/Ogmios and CIP-30 wallet-connector integrations retain their original licenses.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

TRL 3 - experimental proof of concept. Builds on already-implemented CIP-0113 validator infrastructure (from [mintmytoken.today](http://mintmytoken.today)'s shipped vesting feature), so wallet integration and transaction construction are already proven in production.

Planned flow: issuer configures rules (eligibility, jurisdiction, transfer-freeze) via form → platform compiles CIP-0113-compliant validator logic → transactions checked against rules on-chain.

New for this Pilot: rule-configuration schema, compliance-specific validator logic, and the eligibility/allowlist registry - none exist yet.

Delivery path: rule-engine design → preprod testing → security testing (rule-bypass resistance) → mainnet deployment with real compliance-enabled transactions.
