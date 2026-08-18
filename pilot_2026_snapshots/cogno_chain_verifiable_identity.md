# Cogno Chain: verifiable identity

> Verifiable organizational identity for Cardano

## Proposal Metadata

- **Status:** finalized
- **Revision:** 52
- **Proposer:** `stake1u87n83zjwny9defgu9527fdyy8gvdfewhmf26a89yx2pvxq3efkzp`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-18T15:23:20.720000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

Logical Mechanism LLC is the applicant. Quinn Parkinson is the sole engineer and operator, the only person on this grant: runtime and pallets, the CESR and key event log verifier, the frontend, and node and db-sync operations. No subcontractors.

Cardano Foundation, 06 Jan 2025, bylined Denicio Bute: "we highlight activities of the Logical Mechanism \[LOGIC\] pool operated by Quinn Parkinson". cardanofoundation.org/blog/spotlight-stake-pools-logic

Catalyst Fund 14, project 1400046: 100,000 ADA, four milestones, all approved, funds fully distributed. One substantive resubmission on milestone 1 (PoA 7274 rejected 2026-01-01, PoA 7356 approved 2026-01-04).

Milestone 1 here is Cogno on mainnet against a full non-pruned db-sync and our own cardano-node. The LOGIC pool registered on 2020-12-03 and has remained registered since, with 4,162 blocks minted. That is the qualification for milestone 1.

Live, with runtime, pallets, node, and contracts public at github.com/logical-mechanism/cogno.

Background: building on Cardano in public since January 2021. I built contracts for Tokhun, DripDropz, Cornucopias, NEWM, Fraction Estate, and Iagon, and from our work account github.com/logicalmechanism (43 repos), merged 14 pull requests into core Cardano tooling: 8 into aiken-lang/stdlib, including the BLS12-381 wrappers and Miller loops, 1 into aiken-lang/aiken, 5 into txpipe/pallas. Current work: github.com/logical-mechanism. This is our only Catalyst proposal this round.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

WHO TRANSACTS

Organizational DRep and record-stream publishers. Cogno builds the AUTH_BEGIN and ATTEST in the browser. The organization signs, pays, and submits from its own CIP-30 wallet. We submit nothing for anyone and do not sponsor any fees.

WINDOW

We will deliver M1 two months after selection, which is a month within the limit. Under 7.3, that stretches the floored window from 6 epochs to 12, and fees count from delivery through a floorless entry ramp. Measurement period about 65 days.

RAMP

Organizations onboard across the first 30 days, not on day one, so average exposure is 50 of the 65 days. Day 14 is 5 wallets and 20 records, as our channels answer states.

COHORT

8 top-decile at 24, 10 consistently active at 18, 12 at the pooled median of 10. Blended 16.4 per organization, so 492 x 50/30 = 820 attestations. Two record-stream publishers add 99 each, under every observed label-1447 month but two.

MATH

1,018 ATTEST at 0.197 plus 32 AUTH_BEGIN at 0.233 is 208.00 ADA across 1,050 transactions from 32 wallets, against a 100 ADA floor and a 10-wallet minimum.

We do not use 34 records per organization per 30 days. Only 22 of 4,230 observed DRep windows reach it.

### How will you reach and onboard real users - and what evidence backs your channels?

We reach this cohort from inside it: we run the LOGIC pool and a registered DRep on mainnet. We have approached no one and have no commitment.

FUNNEL, and the basis for each step

Addressable: 478 DReps publish resolvable CIP-119 metadata, 138 an email, and 95 domains carry 2+ producing pools. 233 are directly contactable at an address they published.

Contacted: all 233 in the first 30 days.

Onboarded: 32, a 14% conversion. This is an assumption, marked as one. Its basis: 46 DReps already anchor 34+ rationales per quarter, so the behavior exists within the contacted population.

Active: those 32 publish at the rates in our usage answer.

FIRST TWO WEEKS

Days 1-2: publish the verifier, test vectors, onboarding guide and footprint.

Days 3-7: two recorded onboarding calls. First, organizations create a KERI identifier, bind it by CIP-8, and lock 100 ADA.

Days 8-14: first attestations from their own wallets. Day 14: 5 of 32 wallets, 20 records. The other 27 were onboarded by day 30.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today is self-assertion. Pool metadata gives a ticker, name, and homepage; DRep metadata a backlink. AdaStat shows both unchecked.

Identus is a credential stack, not a place credentials get used. Veridian is a wallet, not where attestations get checked. Reeve shows the gap: 1,278 of its 1,288 mainnet transactions name the Cardano Foundation, whose auditor already attests them under CIP-170. Neither product checks that attestation for a reader.

We hold the other half, live on preprod. Cogno verifies key control by CIP-8 signature, locked stake, and pool, DRep and committee status in consensus. Binding an attestation yields two independent claims: this key runs this pool, and this legal entity attests to it. Nobody else holds both halves.

### Please provide details about the Technology Readiness Level selected for your existing product

Cogno runs the whole loop live on Cardano preprod. A user locks ADA into the talk_vault from their own CIP-30 wallet. The chain observes the lock through a deterministic db-sync read, verified in consensus every block, and the resulting talk-capacity meters are posted. Enforcement is on. Identity is a CIP-8 signature verified on-chain.

Today: 14 accounts bound by CIP-8, 54 posts from 11 distinct authors, and 21 vault locks funded by 16 distinct payment credentials between 2026-06-18 and 2026-08-06, 1,600 ADA still locked. Every lock is signed and paid from the wallet that owns it; cogno cannot submit an L1 tx on anyone's behalf.

Verify with no account on cogno.forum, or by running state_getRuntimeVersion on cogno.forum/rpc.

Not TRL 7 only because it is preprod. Mainnet is milestone 1.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

Six layers, all readable at github.com/logical-mechanism/cogno.

1\. Cardano L1. contracts/, Aiken Plutus V3. talk_vault, script hash 168a9710e991b768426b58011febec0fa3c5ff6beb49065cc52489c7, 100 ADA minimum. Users lock and exit over CIP-30 from their own wallets.

2\. Read. cogno-dbsync/, the only path to Cardano. Deterministic SQL over db-sync, fail-closed: a missing table abstains rather than reporting emptiness. Pinned by a golden fixture.

3\. Consensus. node/. The inherent data provider seals the observation into every block; pallets/cardano-observer re-derives it and rejects a block that disagrees.

4\. State. runtime/ plus nine pallets. talk-stake holds observed weight, cogno-gate holds CIP-8 identity 1:1, profile holds account data.

5\. Read API. runtime/src/apis.rs serves feed and profile reads, so the client needs no indexer.

6\. Client. app/, Next.js with PAPI and CIP-30.

CIP-170 enters at three of the six. The organization publishes AUTH_BEGIN and ATTEST to layer 1 from its own wallet. A new pointer in pallets/profile at layer 4 holds the AID, the ATTEST hash, and an OOBI: one spec bump, no migration, no transaction_version change. The verifier runs at layer 6, walking the key event log from the OOBI.

It cannot run at layer 2 or 3. The payload carries no signature; authority lives in an off-chain KEL, and a KEL is not byte-identical across sources the way settled db-sync history is. In consensus, a witness disagreement forks the chain.

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

Market: Cardano governance participants acting under an organizational name. On mainnet, 2026-08-17: 1,061 registered DReps and 2,898 registered pools (api.koios.rest, epoch 649).

Headcount is the wrong argument. Concentration is the right one. CIP-119, the DRep identity standard, says at line 175, "Therefore DReps are people" and has no field for organizational status. Of the 478 DReps whose anchors resolve, zero carry a legal-entity suffix and one names a registered legal entity with jurisdiction. Yet 21 self-described organizational DReps are 1.98% of registered DReps and hold 1,962,168,525 ADA, 37.18% of registered voting power; six of them hold 34.28%. Nine of the 21, 11.84% of registered voting power, anchor that identity at an unrelated domain, Blockdaemon at gitlab.com/cbolden. 8.4% of fetched anchors no longer hash-match.

SPOs are the second population, for identity demand only, not record volume. The enacted Constitution, Definitions clause 8, defines an SPO as "An individual or entity". 393 of the 932 pools that produced a block in epoch 648 share a homepage domain with another pool. 2,848 of 2,898 pools and 521 DReps already pay to commit a hash-anchored identity document.

Two tiers. Persistent identity for anyone running a KERI identifier: addressable by both populations. Attested legal entity via a vLEI chain rooted at GLEIF: small today; exactly two organizations have declared a KERI AID on mainnet whose LEI resolves to an active GLEIF record.

### Applicant name

Quinn Parkinson

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Users pay from their own wallets. Preprod locks are signed and paid by the user over CIP-30 today, and every attestation will be. We never submit on anyone's behalf. The declared 208 ADA across about 1,050 transactions is paid entirely from those wallets.

Burn is self-funded hosting. Cogno has no token and charges users nothing; posting is metered by locked ADA, not fees, so no fee revenue is lost when the grant ends. Revenue: none yet, on purpose. Governance can add a validator incentive once mainnet shows usage.

The live chain is sudo-free from its genesis block. An earlier development runtime carried pallet_sudo; commit ce6c546 removed it before this chain's genesis was minted. Privileged calls need a 3-of-5 committee.

Usage continues because an attestation is per record, not per identity. An organization anchors each rationale for as long as it governs. 11,700 of 35,100 Conway votes already carry an off-chain anchor, which we never prompted.

### On-chain identity (CIP-0170) - expected transaction count

1050

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Without this, the CIP-170 verifier does not get built. Walking another org's KERI log and vLEI chain is not work we would self-fund. Mainnet is gated on a full non-pruned, tx_in-enabled db-sync and its own cardano-node.

200,000 ADA: 13 weeks at 13,000, 169,000, plus 31,000 infrastructure. Each line names the M1 output it pays for. M1 lands at two months on D1-D4 and a minimal D5; D5 polish and D6 run inside the window.

D4 verifier: CESR, Ed25519, Blake3, key event log walk. 5 weeks, 65,000

D5 in-browser builder, organization tag, KEL cache. 3 weeks, 39,000

D3 runtime upgrade and spec bump. 2 weeks, 26000

D1, D2 mainnet launch and external loop. 2 weeks, 26000

D6 footprint, reporting, onboarding support. 1 week, 13000

D1 mainnet node and db-sync host, hardware plus four months. 31000

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Six outputs, tagged D1-D6 in the budget breakdown. All six land two months after selection, a month inside the limit.

1\. Cogno live on mainnet, observing through its own full non-pruned db-sync; talk_vault deployed. (D1, with the 31000 host line)

2\. The loop proven by a wallet that is not ours: an ADA lock, a CIP8 bind, a post metered by observed weight. (D2; D1 and D2 share 26000)

3\. Runtime upgrade live on mainnet: a bound account publishes and clears a pallet-profile attestation pointer. (D3, 26000)

4\. Apache-2.0 CIP170 verifier, test vectors pinned to real mainnet transactions: the Grant Thornton AG and Cardano Foundation declarations decode and check; a fabricated ATTEST is rejected. (D4, 65000)

5\. In-browser builder: Cogno builds the AUTH_BEGIN and ATTEST; the organization signs and pays in its own CIP-30 wallet. (D5, 39000)

6\. Declared footprint: our KERI identifier, our team wallets, and our own application label beside 170; attestations still carry 170. (D6, 13000)

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### On-chain identity (CIP-0170) - fee target (ADA)

208

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

Cardano can prove you control a key. It cannot prove you are a real organization.

Every governance participant is a key hash plus whatever they say about themselves. CIP-119, the DRep identity metadata standard, states at line 175: "Therefore DReps are people." No CIP-119 field expresses organizational status, so a DRep cannot declare one.

Mainnet, epoch 649, 2026-08-17, api.koios.rest: of 1,061 registered DReps, 540 publish no identity claim. Of the 478 whose metadata resolves, zero carry a legal-entity suffix in givenName, and exactly one names a registered company with a jurisdiction. Yet 21 self-described organizations hold 37.18% of registered voting power, 1,962,168,525 ADA, and 9 of them, holding 11.84%, anchor that identity on a host belonging to someone else.

An ADA holder choosing a delegate, or a business choosing a counterparty, cannot tell a registered company from someone using its name.

Cogno is a live social appchain on preprod for Cardano governance. It already proves key control through CIP-8 signatures, locked stake, stake pool, DRep, and committee roles in consensus. It cannot prove legal identity.

We are adding CIP-170. An organization publishes a KERI attestation from its own wallet naming its cogno account. Cogno verifies the key event log off-chain, checks for a vLEI chain to GLEIF, and attaches an organization tag to the result.

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

Design complete, no code written. D3, D4, and D5 build it.

Storage: a pointer in pallet-profile holding the AID, the AUTH_BEGIN and ATTEST hashes, and an OOBI. One spec bump, no migration, no change to transaction_version.

Verification is a ladder in the client. Only a verified key event log lights a badge.

Preprod label 170 holds 87 transactions as of 2026-08-17: 51 ATTEST, 12 AUTH_BEGIN, 23 wrapping both under one map, 1 not a CIP-170 event. Separately, 12 carry an issuer that is not a 44-character SAID. tx_by_metalabel?\_label=170 on preprod.koios.rest answers content-range 0-0/87. Authority is not in the payload; it resides in the off-chain key event log, so verification cannot be part of consensus. No preprod row carries an LEI, so the issuer root is configurable per network.
