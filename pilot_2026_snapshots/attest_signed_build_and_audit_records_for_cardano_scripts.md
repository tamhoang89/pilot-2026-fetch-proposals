# Attest: signed build and audit records for Cardano scripts

> Cardano shows you a script hash, not where it came from. Attest publishes KERI-signed records binding that hash to a reproducible build and its audits, so anyone can check a contract before signing.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 53
- **Proposer:** `stake1u90cjqt5yy4wvhtnu0pudpxgdp7kfnn5e56fqs0qf00znsqh6c3g8`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-19T18:46:25.213000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 5 - Technology validated in relevant environment

### Why is your team well-suited to deliver this?

Maheswaran Velmurugan, sole contributor. Engineering, outreach and support. My only proposal this round; no other Catalyst commitments.

Checkable references:

[linkedin.com/in/maheswaran-velmurugan](http://linkedin.com/in/maheswaran-velmurugan)

[audits.sherlock.xyz/watson/soloking](http://audits.sherlock.xyz/watson/soloking), 7 findings, 3 high and 4 medium, one top-25 finish.

Arbitrum Foundation grant delivered, both milestones accepted and paid: [questbook.app/dashboard/?grantId=67d802bd46da2f90cc3267b0&chainId=10&role=builder&proposalId=68f638ebfb7e884efac8d911&isRenderingProposalBody=true](http://questbook.app/dashboard/?grantId=67d802bd46da2f90cc3267b0&chainId=10&role=builder&proposalId=68f638ebfb7e884efac8d911&isRenderingProposalBody=true)

Four merged PRs into paritytech/polkadot-sdk, in pallet-revive's Ethereum JSON-RPC layer: eth_getBlockReceipts, eth_feeHistory percentile validation, eth_getLogs block tags. Open work on XRPLF/xrpl-rust and Blockstream/lwk (BIP-352 silent payments), plus an RFC to polkadot-fellows. Heavily reviewed repositories where being wrong about an encoding detail does not get merged.

Attest is a standards implementation, CESR primitives, KERI identifiers, CBOR script hashing and CIP-170/171 conformance, so that is exactly the skill it needs.

No other contributors today. If I bring anyone in I will name them and their role in the milestone report.

### Eligible area

Yes

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Third parties transact from their own wallets, paying their own fees. I never pay on anyone's behalf.

Audit firms anchor a report at delivery and at re-review. Protocol teams anchor a build per validator shipped, and a release is rarely one contract; eight to fifteen validators is normal. Ten organisations shipping weekly is about 400 transactions a month. Delivering M1 early extends the window.

Arithmetic: 900 bytes of metadata in a 1,200-byte transaction. At 155,381 + 44 per byte that is 0.208 ADA. 770 x 0.208 = 160 ADA, the bottom of the ambitious band.

First two weeks after going live:

Days 1-3. Verifier live at a public URL indexing label 170. OOBI and declared footprint published.

Days 4-7. The three organisations from M1 publish from their own wallets on mainnet. Check the epoch-1 floor of 13.3 ADA.

Days 8-12. Two more onboarded in person: KERI identifier, Action in their pipeline. Fix what the first three hit, which I expect in wallet setup, not the protocol.

Days 13-14. First audit attestation from an audit firm. Publish a per-epoch table.

Integrity: every attestation resolves to a public git commit and a real script hash, signed from a third party stake key.

### How will you reach and onboard real users - and what evidence backs your channels?

Ten organisations, not thousands of users. Direct outreach, not marketing.

Named targets, none committed yet. Anastasia Labs, Cardano audits and Midgard L2, works in Haskell, Aiken and Plutarch. TxPipe, Buenos Aires, Cardano infrastructure behind Tx3 and Demeter. MLabs, UK, production smart contracts across Cardano and EVM. Vacuumlabs, audits Plutus, Plutarch and Aiken.

Method. Each gets a one-page brief and a Preview transaction they can verify themselves, then a 30-minute call to issue their KERI identifier and add the Action to one repository. Publishing costs them 0.208 ADA and no new infrastructure.

Channels. Cardano Developer Portal, the Cardano and Aiken developer Discords, and Cardano Buidler Fest Buenos Aires 2026, run by TxPipe, where both CIPs are already discussed.

Evidence: I have shipped developer tooling into more than ten ecosystems this way, including Stellar, Starknet, Solana, Aptos, Polkadot and XRPL.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Nobody solves this on Cardano today.

Closest alternatives:

CIP-171. A Proposed CIP with no shipped implementation. It records what source a script came from but not who says so, so anyone can publish a record pointing at someone else's repository. Attest implements CIP-171 and emits its records, then adds the signature it is missing.

Etherscan-style verification. Centralised, single operator, EVM only. If they delist you, your verification is gone.

Audit PDFs on a website. Editable, deletable, unsigned, undated.

Trusting a Discord link.

Why this approach wins: it is the only one where the claim is non-repudiable and the check needs no service I run. Both standards already exist and are backed by the Cardano Foundation. I am joining them, not inventing a format nobody will adopt.

### Please provide details about the Technology Readiness Level selected for your existing product

Deployed and working on Cardano Preview at <https://attest-v1.vercel.app>.

Transaction 795b472ff73c0d04cd2eaa1c863fa321a3787ce4b1cbf200b658c964e0ff357e was published from a browser wallet under identifier EJ5aZI_RBtBaPGwTLS1wYcRhadnLFnDSeNn3fjWdvWVt. It carries the CIP-170 record, the attestation document and the CIP-171 record under labels 170, 1701 and 1984.

Verification returns verified from chain data alone: the document hashes to the identifier the record cites, and the issuer's key event log commits to it at the cited sequence.

Six packages, 214 tests, CI green. Script hashing reproduces the exact hashes of contracts on mainnet.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Three metadata labels in one transaction, no validator of my own.

Label 170: the CIP-170 ATTEST record — issuer AID, document SAID, key event sequence. Label 1701: the document, chunked to 64 bytes. Label 1984: the CIP-171 record, so CIP-171 tools see the build without knowing Attest.

Metadata, not a script: an attestation is a claim about a script, not state to guard. Publishing stays permissionless, with no new trusted contract in the path.

Evidence chain: script hash, document, CIP-170 record, key event log. Every link checks offline.

CIP-170 says who signed but not what. CIP-171 says what was built but not who claims it. The pairing is the product.

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

The market is small and named, not a broad consumer base. Two groups transact:

1\. Cardano audit firms and independent auditors: Anastasia Labs, TxPipe, MLabs, Vacuumlabs. Each publishes an audit record per engagement and per re-review.

2\. Protocol and dApp teams shipping Aiken or PlutusTx validators. DeFi, DEXs, NFT infrastructure. Each publishes a build record per release and per contract in a deployment.

Both already hold ADA and already run CI. No wallet onboarding, and no reason for me to sponsor anyone's fees.

Evidence of demand:

Cardano wrote a standard for half of this problem and nobody shipped the product. CIP-171 (On-chain Smart Contract Bytecode Verification) exists as a Proposed CIP precisely because the ecosystem stated that users "regularly interact with Cardano smart contracts without any practical way to verify that an on-chain script was produced from source code they have reviewed or that has been audited." That problem statement was written by the ecosystem, not by me.

CIP-170 covers the other half and is already in production in Reeve at the Cardano Foundation, with real tooling behind it: KERIA, SignifyTS, Veridian.

Ethereum solved the build half years ago with verified contracts on Etherscan; it is table stakes there. Cardano has no equivalent. The audit half is unsolved on both chains.

No external users yet; the Preview deployment is mine. I am not going to claim traction I do not have.

### Applicant name

Maheswaran Velmurugan

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

The tooling stays free and Apache-2.0. Publishing an attestation costs the issuer a transaction fee of roughly 0.208 ADA. That is the whole cost, and it is paid by the party making the claim.

Usage continues because the incentive is not the grant. An audit firm publishes because a signed, dated record is worth more to its clients than a PDF, and because a competitor doing it makes not doing it look bad. A protocol publishes because "verified build" next to its contract in a wallet reduces the questions it has to answer.

Revenue later:

Hosted verifier and API for wallets and explorers that do not want to run their own indexer. The indexer is open source, so this sells convenience, not access.

Paid support and private deployment for audit firms with compliance requirements.

There is no token and no protocol fee. Nothing breaks when the grant ends, because nothing depends on me paying for it.

### On-chain identity (CIP-0170) - expected transaction count

770

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The code in the repository was written before this proposal. It is contributed to the programme at no cost, and none of the requested funds pay for it. That covers the packages, CLI, verifier, indexer, Action and the Preview deployment.

Everything below has not happened yet.

Onboarding and integration support, ₳20,000. Ten organisations, hands-on: a KERI identifier and a pipeline change each. This is the bulk of the job and none of it is written.

Mainnet hardening, CIP-10 label registration, and publishing the Action, ₳12,000.

Hosting and operating the verifier for four months, ₳6,000.

Independent security review of the verification logic, ₳8,000.

Documentation, Demo Day and milestone reporting, ₳2,000.

Transaction fees and contingency, ₳2,000.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

1. Mainnet publication live. One transaction carries the CIP-170 record, the attestation document and the CIP-171 record, anchored in a KERIA key event log. Evidenced by transaction hashes from wallets that are not mine.
2. Metadata label registered under CIP-10 for the document, replacing the provisional 1701.
3. Hosted verifier at a public URL, indexing label 170 and returning build and audit status for any script hash.
4. At least three external organisations onboarded, each with its own KERI identifier, publishing from its own wallet.
5. GitHub Action published, dropping into an existing release workflow in about ten lines.
6. Tagged release with notes covering architecture, scope and limitations, plus a test evidence bundle: checklist, bug log, security note.
7. Declared footprint published: metadata labels, issuer identifiers, verifier URL, team wallets. All created during the programme, nothing pre-existing.

### How far along is the integration you're proposing, today?

TRL 5 - Technology validated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

160

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Anyone can read a script hash off Cardano. Nobody can find out what it came from.

No way to check that a deployed validator was compiled from a particular commit, or that anyone has audited it. Today this is settled by a link in a Discord message or a PDF on a website. Both can be edited or taken down, and neither is signed by the party making the claim.

Attest fixes that. It publishes on-chain records binding a script hash to a reproducible build (repo, commit, compiler version) and to the audits performed against it (report digest, scope, findings, outcome).

It is a web application, not a library. Users connect a wallet at [attest-v1.vercel.app](http://attest-v1.vercel.app), review what is being attested, and sign. The CLI and GitHub Action exist for teams who prefer automation, but they are a second way in, not the product.

Each record is a JSON document that hashes to its own identifier, committed to the issuer's KERI key event log and published in a CIP-170 transaction citing the exact log position. The document travels in the same transaction, so verification needs the chain and that log, nothing else.

Who it is for. Wallets and explorers, which can show whether a contract a user is about to sign was built from public source and audited. Audit firms, which get a signed, dated record instead of a PDF someone can swap out. Protocol teams, which can prove a deployment matches the code that was reviewed.

### Supporting links (repo, site, demo)

- https://attest-v1.vercel.app
- https://github.com/soloking1412/Attest
- https://github.com/soloking1412/computelens
- https://github.com/soloking1412/Stylus-Toolkit
- https://github.com/soloking1412/dpm-disclose

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

Apache-2.0 across the whole repo, including the CLI, GitHub Action and docs. Copyright is mine as an individual, no company or employer claim. Apache over MIT for the patent grant, as others are meant to implement this. All production dependencies are MIT or Apache-2.0, no copyleft. The format and verification rules are specified in docs/format.md, so an independent verifier that never touches my code reaches the same verdict.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

Live at [attest-v1.vercel.app](http://attest-v1.vercel.app) on Cardano Preview as a web application. A user connects a CIP-30 wallet, submits a blueprint and signs.

Transaction 795b472ff73c0d04cd2eaa1c863fa321a3787ce4b1cbf200b658c964e0ff357e was published that way, from a browser wallet which paid its own fee. The server recomputes the script hash from the bytecode and anchors the document in the issuer's key event log; it holds no Cardano key.

Going live found three defects offline tests could not: native metadata values, a silently accepted network mismatch, and an unconfirmed transaction read as missing. All fixed.

Key event logs resolve from a KERIA agent today; production should read them from witnesses, which the resolver allows. Scoped into M1.
