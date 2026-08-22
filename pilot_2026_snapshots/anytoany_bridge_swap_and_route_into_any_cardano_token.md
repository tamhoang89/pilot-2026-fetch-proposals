# AnyToAny: bridge, swap, and route into any Cardano token

> Swap any EVM token or exchange-held USDC into any Cardano token—and back—in a single transaction. Built ontop of Circle’s CCTP and xReserve coupled with VIA’s cross-chain network.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 28
- **Proposer:** `stake1uyq8ykytm6mhp4aqtk9350nuu6stj0hswrqg90y7prh3mvcqxjk3d`
- **Funding requested:** ₳200,000
- **Last finalized:** 2026-08-22T06:48:48.328000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

VIA has run cross-chain infrastructure for more than four years. It has processed over 20 million messages across 150+ networks and published seven audits. Cardano and Midnight support went live on August 13, 2026.

For this specific proposal, VIA will lead the EVM and product work and contract Anastasia Labs who will support the Cardano development.

**Team**

- **Robert “Cletus” Pilat, CEO** — Program lead, partners, and compliance. [linkedin.com/in/robert-pilat](http://linkedin.com/in/robert-pilat) · [x.com/Cletus_VIA](http://x.com/Cletus_VIA)
- **Andrea “Druuu” Verri, CTO** — EVM router, CCTP v2 and xReserve integration, relayers + executors. [github.com/DruuuCLT](http://github.com/DruuuCLT)
- **Brad “Bert” Simon, Engineer** — Web app, wallet and dApp SDK, integrations. [github.com/brad-za](http://github.com/brad-za)
- **Jake Salthouse, CBO** — Business development and onboarding. [x.com/JakeSalthouse97](http://x.com/JakeSalthouse97)
- **Anastasia Labs (Philip DiSarro)** — Cardano router, validator, and datum-builder support. Philip audited VIA’s Cardano infrastructure and also built the IOG USDCx bridge. He’s a strong fit to work with us again.
  - Signed LOI of project commitment: <https://drive.google.com/file/d/148RhuyMb_wjTZPhwJWeqi3VTjc9on-Gc/view?usp=drive_link>
  - Company links: [anastasialabs.com](http://anastasialabs.com) · [github.com/colll78](http://github.com/colll78)

The external auditor has not been selected yet. Audit costs sit outside this budget.

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

Who transacts: external users moving their own funds. They send USDC from an exchange or EVM wallet into a supported Cardano token, or move a Cardano token out to USDC. Each route creates one or two Cardano transactions.

Qualifying use: count only mainnet transactions initiated by an external user who signs the route and pays the gas fee. VIA, team, contractor, operator, and test transactions do not count. Duplicate retries do not count.

Target: 1,545 qualifying Cardano transactions and 618 ADA in fees. At 0.40 ADA each, 1,545 × 0.40 = 618 ADA. We assume early delivery of M1 to extend the Measurement window to 9 epochs. The first 14 days target 150 txns. The remaining 1,395 require 31 txns per week for for 7 epochs (45 days).

Why plausible: the official USDCx bridge averages about 16 transfers/day. AnyToAny adds supported output tokens and faster exits. The plan ramps from 150 in the first two weeks to 31 txns / day (217 / week) after day 14. Our [scan site](https://scan.vialabs.tech/) will be configured to report qualifying transactions including external wallets, direction, and fees.

### How will you reach and onboard real users - and what evidence backs your channels?

Real users consist of both existing dApps/companies and the general public. We plan to reach them by:

Pre-Launch: VIA pursues B2B integration commitments prior to launching AnyToAny.

**Previous BD & Marketing work evidenced [here.](https://docs.google.com/document/d/1A1zUOz-tLx9zrbfRybFmU7XKC7q8Ljhk1cU8q7-WuFk/edit?usp=sharing)**

Days 1–7: Launch AnyToAny mainnet and provide developer documentation for parties in the integration queue. Target one external dApp/company onboarded, including usage from 20 ***external*** wallets and ≥50 Cardano txns.

Days 8–14: Target one additional dApp/company onboarded, including usage from 50+ ***external*** wallets and ≥150 total Cardano txns. (Estimated: 100 txns from USDCx users and 50 from integrations)

Day 14+: Target 31 transactions/day through demos, outreach, and integration support. Assuming early delivery of M1 - 9 epoch measurement window.

Marketing includes demo days, hackathons, and speaking engagements both online and in person.

### Is the underlying project open source?

No

### Short Video Pitch

https://www.youtube.com/watch?v=pQWgbrt4qHU

### Who else solves this today - competitors/alternatives, and why does your approach win?

Today a user has three main options:

- IOG’s USDCx portal – forwards through Base into plain USDCx. DEX Direct can swap into other tokens, but the tokens often miss the original slippage and the user is forced to go to the DEX. Plus the 25–45 minute inbound and 9-hour outbound wait.
- Buy ADA on an exchange, withdraw, then swap – adds price exposure and two separate hops.
- Wanchain-bridged USDC or USDT – liquidity and custody concerns.

VIA wins by building on USDCx instead of competing with it. AnyToAny aggregates through it: any token in, USDC across, any token out, with fast paths both ways. The modularity of AnyToAny lets us add other messaging providers (Wanchain, or LayerZero when it arrives) as a post-launch feature if there’s a business case.

### Please provide details about the Technology Readiness Level selected for your existing product

VIA’s cross-chain network has been live for more than four years and has carried over 20 million messages across 150+ networks. Cardano mainnet support launched on August 13, 2026.

The explorer at [scan.vialabs.tech](http://scan.vialabs.tech) shows reliable delivery of cross-chain messages consistently between several networks.

Audits: <https://developer.vialabs.tech/docs/general/audits>

Integration docs: <https://developer.vialabs.tech/docs/examples/cardano/overview>

Anyone can build on our existing infrastructure today.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

VIA moves messages between chains with a simple pattern: validators sign each message, relayers deliver it, and the destination verifies the signatures on-chain. On Cardano a message is a UTxO. The sending client creates a send_request UTxO; after the required confirmations, VIA’s network picks it up and processes it exactly once. A receiving client is a validator that holds a state UTxO listing accepted senders. See the Cardano overview at [developer.vialabs.tech/docs/examples/cardano/overview](http://developer.vialabs.tech/docs/examples/cardano/overview).

AnyToAny plugs into Circle’s existing contracts — CCTP v2 on the source chain and xReserve, which mints USDCx on Cardano. On the way in, the router swaps the user’s token to USDC and hands it to CCTP. On Cardano the router receives the USDCx and swaps it into the chosen token. On the way out, the user signs an intent locked in an escrow UTxO. VIA fronts USDC on the destination chain so the user receives funds quickly. Later the normal xReserve / CCTP path settles in the background and the escrow releases to repay VIA.

This design is the right fit because it reuses Circle’s official USDCx rails, keeps every intent as a user-signed UTxO, and uses VIA’s live messaging layer for reliable delivery.

### Fits the timeline

Yes

### Which integration(s) will you leverage?

- Stablecoins

### Is the work in this proposal, or substantially similar work, currently funded, previously funded, or under active consideration by any other program?

No

### Team

Yes

### Submitting as

Incorporated entity

### Who is your target market, and what evidence shows real demand/product-market fit?

AnyToAny serves two main groups:

- People moving funds between exchanges, EVM chains, and Cardano.
- Cardano products looking to build this into their own interfaces.

The organizations below are uncommitted distribution targets, not delivery dependencies. Specific examples include:

- Wallets such as Eternl, Lace, and Gero. They can offer exchange funding and cash-out directly. Eternl already has a USDCx Bridges page, showing an existing integration surface.
- DEXs such as Minswap and SundaeSwap. Users can deposit from an exchange or EVM chain and receive the desired Cardano asset directly in the DEX for trading, liquidity, or other activity.
- Aggregators such as DexHunter, which can quote supported EVM-to-Cardano routes. DexHunter has publicly asked when USDCx liquidity will grow.
- Lending, trading, and perpetual markets such as Liqwid or Indigo, which can receive the selected Cardano asset as collateral or margin.

Demand already shows in USDCx activity. Supply is 44 million after 2,237 mints and 914 burns since the February launch. Our count from public [xReserve logs](https://etherscan.io/address/0x8888888199b2Df864bf678259607d6D5EBb4e3Ce) shows about 800 exchange forwards from roughly 280 wallets, and around 35 DEX Direct transactions. (Counts observed from public logs in August 2026).

Users want a direct way into Cardano. AnyToAny adds asset choice, support for CCTP-connected EVM chains, and exits in minutes.

### Applicant name

VIA Labs LLC

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

AnyToAny runs on VIA’s existing messaging and relayer network. Ongoing costs are relaying, monitoring, maintenance, and the capital needed for fast settlement. VIA supplies that capital and takes the settlement exposure.

Users see an all-in quote before they sign. The quote can include source-swap costs, Circle CCTP and xReserve charges, Cardano execution, third-party route costs, and a VIA service margin. Fast and standard routes can be priced differently. VIA will set the exact margins after mainnet cost testing; this proposal does not lock in any fixed customer fee. Wallets and dApps can integrate with no access fee.

**The grant only pays for development.** It does not fund transfer liquidity or subsidize fees. After launch, route revenue has to cover general upkeep and server costs. Users will keep coming back because the quoted route is simply easier or faster than the alternatives they have today.

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Funding enables AnyToAny on Cardano now; without it, the work waits behind paid client work. Planned allocation of all 200,000 ADA:

- **80,000 ADA (40%):** Cardano router and escrow validators, DEX-order datum builders, VIA message-layer integration, and Cardano mainnet tests. Supports M1 items 1–3.
- **80,000 ADA (40%):** EVM swap router, CCTP v2/xReserve integration, contract tests, and EVM mainnet deployment. Supports M1 items 1–3.
- **40,000 ADA (20%):** web app, SDK, end-to-end testing, documentation, deployment, and launch monitoring. This supports M1 item 4 and acceptance evidence.

The grant funds development only. VIA separately funds fast-route liquidity and the external audit. Users pay their own transaction costs.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

- Develop and deploy the AnyToAny contracts on mainnet: the EVM router (swap on one EVM DEX, then USDC over CCTP v2 and xReserve) and the Cardano router and escrow validators (Aiken), connected to VIA's message layer.
- Inbound live for real users: USDC from an exchange or an EVM wallet arrives on Cardano and swaps into ADA, USDM, or another supported token on one Cardano DEX. Mainnet transaction hashes published.
- Fast routes live with launch caps: one fast entry and one fast exit completed on mainnet, with completion times published.
- Public front-end at [anytoany.xyz](http://anytoany.xyz) and integration documentation with the SDK at [developer.vialabs.tech](http://developer.vialabs.tech).
- [Scan site](https://scan.vialabs.tech/) updated to show usage data. Including all qualified transactions (external wallets, direction, and fees).

### How far along is the integration you're proposing, today?

TRL 4 - Technology validated in lab

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

AnyToAny is the all-in-one bridge, swap, and router connecting EVM chains and CEXs directly to Cardano.

It takes any token from an EVM chain—or USDC sitting on an exchange—and delivers it on Cardano as the exact token you want: USDM, ADA, or any listed asset. The route also works in reverse: any Cardano asset can become any EVM asset on a CCTP-connected chain.

Under the hood, AnyToAny uses existing liquidity routes. Transfers into and out of Cardano route through xReserve’s USDCx. Circle’s CCTP and xReserve move the USDC between chains, while routers on each side swap into the selected asset.

The issue is timing. Standard wait times for USDCx are 25–45 minutes into Cardano and roughly nine hours out of Cardano, based on 1,620 confirmations. The wait, coupled with separate bridge and swap steps, makes onramping and offramping difficult.

AnyToAny solves this with an intent-based framework that locks and releases USDC on supported EVM chains and USDCx on Cardano. Users get a “fast option” that bypasses the traditional xReserve wait and releases funds in minutes. The liquidity pools are rebalanced afterward through xReserve. VIA fronts the capital and settles in the background.

AnyToAny is built for both B2B and B2C applications. Existing dApps and companies can integrate using detailed documentation to streamline liquidity transfers for payments, lending, and other uses. Traditional blockchain users can use the front end to complete their transfer.

### Supporting links (repo, site, demo)

- https://vialabs.tech/
- https://scan.vialabs.tech/
- https://midnight.anytoany.xyz/
- https://developer.vialabs.tech/docs/examples/cardano/overview
- https://drive.google.com/file/d/1SDxHkFBE7oJ6gNBDQJxHMx8ujv-2UxQc/view?usp=sharing

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

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Stablecoins - expected transaction count

1545

### Standard read and attested

Yes

### Stablecoins - fee target (ADA)

618

### Current funded commitments

- Midnight grant (covers Cardano and Midnight mainnets) - went live Aug 13th. Completed. Awaiting payment. 
- Stellar SCF #35. Mainnet code audited and ready to deploy. We delayed deploying until after Cardano and Midnight went live on Mainnet. All we need to do is deploy it. No additional development work is required. 

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

The proposed work covers the Cardano router and escrow validators, one DEX order path, exchange entry, fast settlement, and the product interface.

The design reuses public USDCx mechanics, VIA’s live Cardano client, and VIA’s existing CCTP v2 work (ongoing). The Cardano-specific AnyToAny integration itself remains proposed work.
