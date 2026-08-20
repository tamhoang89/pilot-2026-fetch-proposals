# In-Place Collateral Swaps for Cardano Lending

> De-risk a loan without repaying it — one atomic transaction.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 3
- **Proposer:** `stake1uy6kdahcjvxgfx6p03xzaf2p83286dvz4ufeyjymdd5h5lgg9cwgk`
- **Funding requested:** ₳140,000
- **Last finalized:** 2026-08-20T03:59:43.077000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 7 - System prototype demonstrated in operational environment

### Why is your team well-suited to deliver this?

This work extends a product we already operate. Dano Finance V2 runs lending, borrowing and a direct-spend concentrated liquidity AMM on Cardano mainnet, so the two systems this proposal composes are both ours, both live, and understood by the people writing the composition.

Mai Thanh Binh - Project Manager: <https://www.linkedin.com/in/binh-mai-6b572493/>

Pham Tung Giang - Smart Contract Lead.  Built the Dano Finance Lending Validators.

Nguyen Thac Dan Thanh - Protocol Engineer.

Nguyen Minh Hoang - Backend / Indexer.

Nguyen Thi Minh Thu - Frontend.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

The wallets paying those fees belong to borrowers opening and servicing USDM debt, borrowers defending positions during drawdowns, the same borrowers reversing swaps afterwards, and independent liquidators. None are ours, and we sponsor nothing.

The rhythm holds because a defended position keeps transacting: a swap on the way down, a swap back on the way up, and continued borrowing afterwards - whereas a liquidated position produces one event and goes quiet. Turning terminal events into recurring ones is the point, and it happens to be what a floored six-epoch window rewards.

Arithmetic: roughly 1,550 external transactions across withdraw, supply, borrows, repayments, swaps, reversals and liquidations, all on newly deployed contracts. Composing a lending validator, pool validators and the swap validator in one transaction puts the average fee near 0.71 ADA, above the 0.33 ADA network average. We commit 65 external wallets against a 31-wallet minimum.

1,100 ADA is in the Ambitious band, 3.7x the floor.

### How will you reach and onboard real users - and what evidence backs your channels?

We do not have to find these users. They already borrow on Dano Finance, and the feature appears inside positions they hold - no new wallet, no new deposit, no onboarding.\
\
What we do have to do is reach them at the right moment, because nobody thinks about de-risking until the health factor moves. So the option surfaces contextually: when a position crosses a warning threshold, the interface offers a collateral swap beside the top-up and repay buttons already there, with the resulting health factor shown before signing. \
\
Permissionless liquidation needs a different audience. We publish a liquidator guide, a reference bot and a feed of liquidatable positions, and point at the 226 liquidations our market produced recently - the revenue we open to whoever runs one.

### Is the underlying project open source?

Yes

### Who else solves this today - competitors/alternatives, and why does your approach win?

On Cardano, nobody. Liqwid, Fluid and other venues offer deposit, borrow, repay and withdraw. None offers collateral substitution while a debt is open, because it requires atomic composition of a lending position with a swap venue, and that needs a validator neither side provides.\
\
The real alternative is the manual sequence: repay, withdraw, swap, redeposit, borrow. Five transactions, five fees, and the borrower is unhedged in the middle - in a falling market, exactly when price moves.\
\
Topping up requires idle capital at the worst moment and increases exposure to the falling asset. Accepting liquidation costs a penalty.\
\
We win by being the only option that reduces exposure without closing the position, and the only one that is atomic.

### Please provide details about the Technology Readiness Level selected for your existing product

Dano Finance V2 is live on Cardano mainnet at <https://dano.finance>, running swap, lending, borrowing and a direct-spend concentrated liquidity AMM. \
\
That places it at TRL 7: a complete system operating in its real environment with real users and real capital at risk, not a testnet deployment.\
\
The in-place collateral swap proposed here is new work: a new validator composing our existing lending positions with our existing CLMM pools, plus a redesigned permissionless liquidation path. Neither exists on any network today.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

A collateral swap is one transaction touching three things: the borrower's lending position, one or more direct-spend CLMM pool UTxOs, and a new CollateralSwap validator that enforces the property none of the others can see.\
\
The transaction spends the position UTxO and the pool UTxOs, and executes the CollateralSwap validator through a zero-withdrawal from its stake script, with the borrower's intent in the redeemer: position reference, collateral out, collateral in, minimum received, minimum resulting health factor, deadline.\
\
The lending validator checks its own invariant: debt unchanged, position still owned by the same credential, collateral accounting consistent. Each pool validator checks its own swap invariant. Neither has visibility into the other.\
\
The CollateralSwap validator enforces what spans them, reading the price feed via reference input: that the debt is unchanged; that the collateral removed belongs to this position; that the net collateral value returned is at least the declared minimum; that the resulting health factor is at least the declared minimum and no worse than before; that pools used are in the approved registry; and that the transaction is inside its deadline. Any failure aborts.\
\
Liquidation uses the same pattern with different rules: any wallet may execute if the validator agrees the position is below threshold, repayment is sufficient, seized collateral is within the close factor, and the bounty matches the formula.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Individual

### Who is your target market, and what evidence shows real demand/product-market fit?

The market is borrowers on Cardano lending markets, and we already serve it: Dano Finance runs lending, borrowing in production at <https://dano.finance>.\
\
Evidence from our own production data:

- 220 borrowers and 2.360 positions
- 226 liquidation events over the last 12 months
- 693 collateral top-ups during drawdowns\
  \
  That last figure is the demand signal. Every top-up is a borrower who wanted to de-risk and had to spend capital to do it. Every liquidation is a borrower who could not.\
  \
  The structural evidence: no Cardano lending venue offers collateral substitution while a debt is open. Aave shipped the equivalent on Ethereum precisely because borrowers kept doing it manually and losing money in the gap, and it became a standard expectation there. Cardano borrowers face the same problem with none of the tooling.

### Applicant name

Pham Tung Giang

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

Transaction-based, aligned with the activity the programme measures.\
\
Four revenue lines: a swap fee on each collateral swap, shown in the quote before signing; the existing lending spread, which continues on positions that survive drawdowns instead of being liquidated; CLMM pool fees on routed volume; and a protocol share of liquidation bounties.\
\
Borrowers pay because the alternative costs more: five transactions instead of one, market exposure in the gap, or a liquidation penalty larger than any swap fee we would charge.\
\
There is a second-order effect that matters more than the fee. A borrower who survives a drawdown keeps paying interest. One who is liquidated stops. Every position this saves is recurring revenue preserved, so the feature pays for itself before its own fee is counted.\
\
Costs are fixed: contract maintenance, monitoring, support, review. Revenue scales with borrowing volume and volatility. We reward nobody for transacting.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

This composes two systems we already run into a primitive neither provides alone so the whole position lifecycle sits inside newly deployed contracts.\
\
Allocation of the 140,000 ADA request:

- Collateral swap validator and health-factor invariant, tests: 36,000
- Permissionless liquidation validator and bounty mechanics: 20,000
- Transaction builder, quote engine and integration library: 20,000
- Position monitoring, liquidatable-position feed, dashboard: 12,000
- External security audit and remediation: 34,000\\
- Documentation, liquidator tooling, launch: 10,000\
  \
  The audit is not optional: this validator moves collateral inside live debt positions.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Target delivery: month two of the three-month window, to earn extra measurement epochs.\
\
On-chain: USDM-denominated lending market contracts, newly deployed so the whole position lifecycle is inside the declared footprint; CollateralSwap validator executed via zero-withdrawal; permissionless liquidation validator; approved pool registry with timelocked, multisig-gated updates; declared mainnet script hashes, addresses and the Dune metadata message tag.\
\
Off-chain: transaction builder for borrow, repay, swap, reverse swap and liquidation; quote engine returning expected collateral, health factor and fees; position view showing projected health factor before signing; liquidatable-position feed; reference liquidator bot.\
\
Live mainnet: borrows and collateral swaps by external borrowers, and at least one liquidation, with hashes published.\
\
Verification: property and integration tests; external audit and remediation of critical and high findings; release notes.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

A borrower watching ADA fall has three options today, all bad. Post more collateral, which needs idle capital at the worst moment. Repay part of the debt, which means selling the asset they borrowed against. Or get liquidated and pay a penalty.\
\
What they want is currently impossible: keep the loan, change what backs it. Move collateral out of the falling asset into a stablecoin, ride out the volatility, move back later, without touching the debt.\
\
Doing it manually means repay, withdraw, swap, redeposit, borrow again. Five transactions, five fees, and a window where the user has no position and full market exposure. If price moves in that window, the manoeuvre taken to reduce risk has increased it.\
\
We are building in-place collateral swaps: one atomic transaction that withdraws collateral from a lending position, swaps it through a direct-spend CLMM pool, and returns the proceeds as collateral to the same position, with the debt untouched. The position is never open, never unbacked, never briefly liquidatable. Either the sequence executes with a verifiably healthier position, or nothing happens.\
\
The same mechanism runs in reverse to restore the original exposure, and works with assets the user already holds.\
\
Alongside it we open liquidations to anyone. Today liquidation depends on keepers the protocol runs itself - a centralisation point and a single point of failure. Under our design any wallet can execute a liquidation the contract deems valid.

### Supporting links (repo, site, demo)

- https://dano.finance

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

We opensource our smart contract

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1550

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

1100

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The mechanism is specified against systems we already run: the health-factor invariant that must hold across an atomic collateral substitution, the routing constraint through direct-spend CLMM pools, and the liquidation validity rules that let any wallet execute.\
\
No validator exists on any network yet, placing the integration at TRL 2.\
\
The collateral swap validator, the permissionless liquidation validator, the transaction builder and quote engine, position monitoring and the liquidatable-position feed, property and integration tests, an external security audit and remediation, and live use by borrowers on Cardano mainnet at Milestone 1.
