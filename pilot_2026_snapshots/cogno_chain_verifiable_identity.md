# Cogno Chain: verifiable identity

> Verifiable organizational identity for Cardano

## Proposal Metadata

- **Status:** finalized
- **Revision:** 38
- **Proposer:** `stake1u87n83zjwny9defgu9527fdyy8gvdfewhmf26a89yx2pvxq3efkzp`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-13T20:29:56.366000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Logical Mechanism LLC is the applicant. Quinn Parkinson is the sole engineer and operator, and will deliver every workstream: runtime and pallet changes, the CESR and KERI verifier, the frontend, and node and db-sync operations.

[github.com/logical-mechanism](http://github.com/logical-mechanism) | [logicalmechanism.io](http://logicalmechanism.io)

Relevant prior work, all public:

Decentralized On-Chain Data Encryption, our completed Fund 14 Catalyst project. All four milestones closed, 100,000 ADA fully distributed. Code at [github.com/logical-mechanism/Peace-Protocol](http://github.com/logical-mechanism/Peace-Protocol).

Seedelf-Wallet, a stealth wallet on Cardano using the BLS12-381 curve, in Rust. This is the closest analog to the work proposed. CIP-170 verification is Ed25519, Blake3, and CESR parsing, and Seedelf shows we implement unfamiliar cryptography correctly rather than approximately.

Assist, an Aiken library other Cardano teams use to build contracts.

Collateral-Provider, an altruistic collateral API we run for the ecosystem.

Cogno, the social appchain this proposal extends.

Development is AI-assisted and disclosed in our commit trailers.

No skills gaps to fill. We verify new cryptography by differential testing. The CIP-8 oracle is an independent Python implementation in CI; for CIP-170 we differential-test against the Cardano Foundation's public Reeve vLEI verifier.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: stake pool operators and DReps under an organizational name, from their own wallets. Never ours, never sponsored. Our identifier is new for this work.

Sources, with volumes. Pool homepages and SPO groups on Telegram and Discord: 2,900 pools, 150 approached, 17 expected. DRep metadata anchors, Intersect, GovTool, Cardano Forum: 1,059 DReps, 100 approached, 13 expected. That is 12 per 100; the 10-wallet floor needs 4.

First two weeks after milestone 1. Days 1 to 2: publish the verifier, test vectors, footprint, and onboarding guide. Days 3 to 7: two onboarding calls. An organization sets up its own KERI identifier, binds by CIP-8, and locks 100 ADA of its own. Days 8 to 14: attestations are published; the 36-hour lock-depth gates only the pointer write. By day 14: the first external attestation, 5 locked, 20 records. Counts reported weekly.

Targets: 30 organizations, each one AUTH_BEGIN plus about 34 records, is 1,050 transactions. On preprod, an ATTEST pays 0.197 ADA and an AUTH_BEGIN pays 0.233 ADA, so about 208 ADA against a 100 ADA floor. The 6-epoch worst case, 660 transactions, still pays 131 ADA. The epoch floor binds: 1.6 records per org per working day.

### How will you reach and onboard real users - and what evidence backs your channels?

Channels, population reached, organizations approached, and share of our 30:

Pool homepages and SPO groups on Telegram and Discord: 2,900 pools, 150 approached, 17 expected.

DRep metadata anchors, Intersect groups, GovTool, Cardano Forum: 1,059 DReps, 100 approached, 13 expected.

That is 12 per 100 approached. The 10-wallet floor needs only 4 per 100.

First two weeks after milestone 1:

Days 1 to 2: publish the verifier, its test vectors, the declared footprint, and an onboarding guide.

Days 3 to 7: two open onboarding calls. An organization sets up its own KERI identifier, binds by CIP-8, then locks 100 ADA of its own.

Days 8 to 14: attestations are published from the organization's wallet; the lock clears its 36-hour depth, so the pointer write lands. By day 14: the first external attestation, 5 locked, 20 records. The 10-wallet floor clears across the window, not week 2. Counts reported weekly.

Every transaction is signed in the organization's own wallet, never ours.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today's answer is self-assertion. Pool metadata includes a name and homepage; DRep metadata includes a social backlink; and GovTool and AdaStat display those claims unchecked. ADA Handle gives a readable name, not an identity.

Hyperledger Identus now carries the W3C DID and credential stack, since IOG has dropped Atala PRISM. That is a credential stack, not a place credentials get used. Veridian is the Foundation's KERI wallet, and Reeve is its own publisher and verifier. Issuance is GLEIF and the QVIs.

We win because we hold the other half. Cogno verifies key control, locked stake and pool, DRep and committee status from Cardano in consensus. Binding an attestation to it yields "this key runs this pool, and this entity attests to this account." Nobody else has both.

### Please provide details about the Technology Readiness Level selected for your existing product

Cogno is a full working system on Cardano preprod, running the complete loop with realistic flows.

A user locks ADA into a vault from their own CIP-30 wallet. The chain observes that lock through a deterministic db-sync read, verified in consensus in every block, and the resulting talk-capacity meters their posting. Weight enforcement is on. Identity is a CIP-8 signature verified on-chain, not an operator claim.

It is live now, with 14 accounts that have bound a Cardano identity by CIP-8 signature, all 14 carrying observed locked-ADA weight, and 52 posts from 11 authors metered by it.

Verifiable at www.cogno.forum and at [polkadot.js.org/apps](http://polkadot.js.org/apps) connected to wss://cogno.forum/rpc.

Not TRL 7 only because it is preprod. Mainnet is milestone 1 of this proposal.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Cogno is a Polkadot-SDK appchain with its own Aura and GRANDPA validators. Cardano is observed, never bridged: a consensus-inherent read of Cardano through db-sync every block, and any node running its own db-sync re-derives the same result or rejects the block. A node without one abstains. Reads fail closed, so an under-indexed database abstains rather than reporting false emptiness.

That machinery is already what CIP-170 asks for. The CIP assigns validation to chain indexers, and cogno is a deterministic, fail-closed Cardano metadata indexer today. It reads tx_metadata at label 867 to observe Calidus role registrations, pinned byte-for-byte by a golden vector from a real cardano-signer registration. Label 170 is the same kind of read, judged in the client.

Identity is already key-proven. An account binds to a Cardano stake credential by a CIP-8 signature verified on-chain. So a CIP-170 attestation attaches to an identity that has already proved key control, giving two independent claims: control of the key, verified in consensus, and legal identity, attested by the credential chain. Attaching a credential to a bare address gives only the second.

The attestation pointer lands in pallet-profile, feeless and gated on a bound identity. Verification runs on the client because CIP-170 payloads carry no signatures and authority resides in an off-chain key event log.

Cost is one spec bump: no migration, no change to transaction_version, and the consensus path untouched.

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

Our market is Cardano governance participants who act publicly under an organizational name. On mainnet today, that is 2,900 registered stake pools and 1,059 registered DReps: 3,959 registrations ([api.koios.rest](http://api.koios.rest), August 2026).

Both groups already do the work of asserting identity. Pool metadata carries a ticker, name, and homepage. DRep registration carries a metadata anchor. None of it is verifiable, and the standard for DRep identity asks you to post your DRep ID in a social media bio, which anyone can copy.

That is the demand signal: roughly 4,000 entities already spend effort telling people who they are, using the only mechanism available, and it proves nothing.

We serve them in two tiers, and we size each honestly.

Persistent identity. Any operator running a KERI identifier publishes an attestation binding it to their cogno account. Cogno's client verifies the key event log, so the account maintains a single stable identifier through key rotation, with auditable key history. Addressable today: all 3,959.

Attested legal entity. A vLEI credential chain rooted at GLEIF proves registered legal identity. This tier is small, and we will not pretend otherwise: there are 8 Qualified vLEI Issuers worldwide, and 2 entities have published a CIP-170 attestation on mainnet. The LEI system has issued 3.4M identifiers (gleif.org), so the constraint is vLEI issuance, not demand.

Commercial significance: these registrations carry Cardano's governance votes.

### Applicant name

Quinn Parkinson

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Cardano users pay from their own wallets. Every attestation and stake lock is signed by the user over CIP-30. We do not submit on anyone's behalf, so nothing can be routed through an operator to inflate a number.

Who pays for Cogno: the operator. Burn is one server running cardano-node, db-sync, and the cogno node, and has been self-funded since launch. The live chain has no sudo and never has: a 3-of-5 committee origin, one seat filled today, and a changeable validator set let operators join by vote.

Revenue: none yet, on purpose. The chain can add a validator incentive mechanism through governance once mainnet shows real usage. We would rather set it against real numbers than guess now.

Why usage continues: the fees measured here are paid by users on Cardano and do not depend on cogno's economics. An attestation is per record, not per identity. An organization proves who it is once, then anchors each report or rationale it stands behind, for as long as it governs.

### On-chain identity (CIP-0170) - expected transaction count

1050

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this, the client-side verifier does not get built. Cogno's roadmap covers only Cardano-native facts, so verifying third-party credentials is not work we would self-fund. Mainnet is already our plan but self-funded and slow: a full non-pruned db-sync with its own Cardano node gates it. All future work; no code yet.

200,000 ADA: one engineer at 13,000 a week for 13 weeks, plus infrastructure:

D4 verifier: CESR, Ed25519, Blake3, key event log walk. 5 weeks, 65,000

D5 in-browser builder, organization tag, KEL cache. 3 weeks, 39,000

D3 runtime upgrade and spec bump. 2 weeks, 26,000

D1, D2 mainnet launch and external loop. 2 weeks, 26,000

D6 footprint, reporting, onboarding support. 1 week, 13,000

Node and non-pruned DB-sync host, hardware plus four months. 31,000

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Cogno goes live on Cardano mainnet, observing Cardano mainnet through db-sync, with talk_vault at its existing script hash. Verifiable by RPC and cardanoscan.
2. The loop proven by a wallet not ours: lock ADA on mainnet, bind identity by CIP-8, post.
3. A runtime upgrade live on mainnet letting a bound account publish and clear an organization attestation pointer in pallet-profile.
4. An Apache-2.0 CIP-170 verifier that walks a credential chain to a per-network root and a key event log to the key state at the attested event, with test vectors.
5. An in-browser attestation builder. Cogno builds the AUTH_BEGIN and ATTEST; the organization signs and pays from its own wallet. Proven by at least one mainnet attestation from a wallet not ours, and an organization tag that renders only on a verified key event log.
6. Our declared footprint published: our KERI identifier, our own new metadata label rather than the shared 170, and team wallets. Attestations still carry 170.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

200

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano can prove you control a key. It cannot prove you are a real organization.

Every governance participant, DRep, stake pool operator, or committee member, is known by a key hash plus whatever they choose to say about themselves. CIP-119 settles for a social backlink, putting your DRep ID in a social media bio, having judged PKI too complex for minimum viable tooling. Anyone can copy that claim. So an ADA holder choosing who to delegate to, or a business choosing a counterparty, has no way to tell a registered company from someone using its name.

Cogno is a live social appchain for the Cardano governance community. It already proves Cardano-native facts about an account with no trusted third party: key control through CIP-8 signatures, locked stake, and stake pool, DRep and committee roles read from Cardano and verified in consensus. What it cannot prove today is legal identity.

We are adding CIP-170 to Cogno. An organization publishes a KERI attestation from its own wallet naming its cogno account. Cogno verifies it off-chain against the organization's key event log and, if a vLEI credential chain back to GLEIF exists, then gates an organization tag on the result.

This serves ADA holders who are delegating voting power, organizations that are registered but cannot prove it, and businesses that need to know who they deal with.

"This account is Logical Mechanism LLC" becomes something you verify, not something you believe.

### Supporting links (repo, site, demo)

- https://cogno.forum/
- https://github.com/logical-mechanism/cogno
- https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fcogno.forum%2Frpc
- https://github.com/logical-mechanism/Peace-Protocol
- https://github.com/logical-mechanism/Seedelf-Wallet

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

Apache 2\
\
<https://github.com/logical-mechanism/cogno/blob/main/LICENSE>

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Design complete, no code written.

The storage is specified as a pointer in pallet-profile that holds the AID, the AUTH_BEGIN and ATTEST hashes, and an OOBI. A later AUTH_END clears the tag. One spec bump, no migration, no change to transaction_version. Verification is a 6-stage ladder in the client, where only a verified key event log lights a badge.

We measured the target data on preprod: 37 label-170 rows, 11 AUTH_BEGIN, 25 ATTEST, and one row that is not a CIP-170 event at all; the largest row is 1,312 bytes; 0.5ms to query on an index we add to db-sync. None carries a key event log entry or a signature. That is why verification cannot be part of consensus. Preprod is also rooted at a non-GLEIF issuer, so the issuer root is configurable per network.

The grant covers the entire build.
