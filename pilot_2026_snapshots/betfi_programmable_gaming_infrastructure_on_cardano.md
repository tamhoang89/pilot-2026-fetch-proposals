# BetFi: Programmable Gaming Infrastructure on Cardano

> Bringing CIP 0113 programmable tokens into BetFi Poker & Sportsbook to create new gaming utility, user activity and measurable adoption on Cardano.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 16
- **Proposer:** `stake1u8wlhvams7vckmfrrff7j7lyc9eaqwezx9cym5ln6pzxm3gta7m74`
- **Funding requested:** ₳50,000
- **Last finalized:** 2026-08-19T21:50:52.032000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 9 - Actual system proven in operational environment

### Why is your team well-suited to deliver this?

**TO CATAYLYST TEAM: WE’VE MADE NUMEROUS REVISIONS TO THIS PROPOSAL BASED ON THE FEEDBACK PROVIDED.**

At this point, would it be possible to schedule a video call so we can walk you through the BetFi platform and the proposal directly? The application has been returned multiple times, even after addressing the requested revisions, and we want to make sure we fully understand exactly what is still missing.

We’re happy to demonstrate the live platform, show our existing usage, and answer any questions in real time. We want to get this right, but the repeated back-and-forth has become frustrating, and a short call may be the most effective way to resolve any remaining concerns.

Johnny Tran, Founder of Risk Gaming Co. and BetFi, is the sole proposer and key contributor responsible for delivering this Catalyst project. I have been active within the Cardano ecosystem since 2018, working across gaming, blockchain products and community development.

**Verifiable references:**

LinkedIn: <https://www.linkedin.com/in/johnny-tran-03b980429/>

BetFi: <https://betfi.poker/>

Risk Gaming: <https://riskgaming.io/>

Abhiwan Technology: <https://www.abhiwan.com/>

### Eligible area

Yes

### Optional: Voluntary give-back pledge: grant repayment terms and/or treasury revenue share, with your own thresholds/terms and/or %. If no such relevant offer exists, please write 'N/A'.

N/A

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

BetFi has an existing base of 390 registered accounts, including 276 unique connected Cardano wallets. Production records show 298 users have played real Poker and 74 have used the Sportsbook. In the last 30 days, 326 users logged into BetFi and 33 placed Sportsbook bets. We also have 479 completed ADA deposit transactions backed by unique on chain transaction hashes.

Our VIP Table network includes Risk Gaming, Melting Moons, Broker Punks, Bear Market Bulls, BankFi, Wojaks, Walkers Fit, Starforged Infinity and Hops on Cardano, providing existing community distribution channels.

We target 150 to 200 external wallets for CIP 0113 adoption. Users will interact with programmable assets for player access, tournament participation, membership, achievements and partner experiences. During the first two weeks, we will launch through existing BetFi users, VIP partner events and community channels. Our 2,000 transaction target represents approximately 10 to 13 qualifying interactions per participating wallet across the measurement period. Users will initiate transactions and pay their own Cardano network fees. Team wallets and sponsored transactions will not count toward the target.

### How will you reach and onboard real users - and what evidence backs your channels?

BetFi has 390 registered accounts, 276 unique connected Cardano wallets, 298 lifetime Poker players and 74 lifetime Sportsbook users, with 326 users logging in during the last 30 days.

Our VIP Table model gives Web3 projects branded poker experiences they promote to their communities. Partners include Melting Moons, BankFi, Starforged Infinity, Broker Punks, Bear Market Bulls, Wojaks, Walkers Fit and Hops on Cardano.

Evidence:\
Melting Moons: [https://x.com/MeltingMoons/status/2085925703162192052](https://x.com/MeltingMoons_/status/2085925703162192052)\
VIP page: <https://betfi.poker/meltingmoons>\
BankFi: <https://x.com/BankFiOfficial/status/2084710935617294584>\
Starforged: <https://x.com/BetFicasino/status/2085406568494010699>

We target 150 to 200 external CIP 0113 wallets. In the first two weeks after mainnet launch, we will activate existing users and partner communities through branded events, platform promotion and partner social channels.

### Is the underlying project open source?

No

### Who else solves this today - competitors/alternatives, and why does your approach win?

BetFi competes with traditional poker and sportsbooks, crypto gaming platforms, and emerging prediction markets. Most are centralized, operate outside Cardano, or focus on a single product. BetFi is different because we are already live and building an integrated Cardano gaming ecosystem across Poker, Sportsbook and upcoming Prediction Markets. We also operate Multi Table Tournament (MTT) poker and a VIP Table Ownership model that lets Cardano projects run branded poker experiences. Our new CIP 0113 integration will add programmable on chain utility directly into this existing ecosystem, while ChangeNOW provides a pathway for users from other blockchain ecosystems to convert supported assets into ADA and enter Cardano.

### Please provide details about the Technology Readiness Level selected for your existing product

BetFi is currently TRL 9. Our Poker and Sportsbook platform is live in production and used by real users within the Cardano ecosystem. BetFi was developed with support from Abhiwan Technology and includes Cardano wallet connectivity, deposits, withdrawals, poker cash games, Multi Table Tournaments, Sportsbook infrastructure, player accounts and administrative systems. Production usage and gaming volume are publicly available at <https://betfi.poker/stats>. The Catalyst Pilot is not funding the creation of BetFi. It will support a new CIP 0113 integration within our existing production platform, giving the new technology an immediate environment for development, testing, deployment and real user adoption.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

BetFi will use CIP 0113’s shared script architecture with non custodial user ownership. Programmable token UTxOs reside at the programmable_logic_base script, while each user’s stake credential represents ownership and transactions are authorized through their connected Cardano wallet. The CIP 0113 on chain registry maps our programmable token policy to the applicable issuance and transfer validators. programmable_logic_global acts as the global validation coordinator and enforces transaction wide programmable token rules. BetFi will use the CIP 0113 issuance_mint policy and an application transfer substandard based on the permissioned transfer reference pattern. Cardano remains the source of truth for ownership, minting, burning, transfers and validation. BetFi handles wallet connectivity, transaction construction, indexing, submission, confirmation and reconciliation off chain. The user's wallet signs the transaction, Cardano executes the applicable CIP 0113 validators, and BetFi verifies the confirmed transaction, policy ID, resulting UTxO and expected ownership state before updating application state.

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

BetFi is an early stage startup already operating in production. Our live database currently records 390 registered accounts, 276 unique connected Cardano wallets, 298 lifetime Poker players, 74 lifetime Sportsbook users and 479 completed ADA deposit transactions backed by unique on chain transaction hashes.

Since launch, more than 100,000 ADA in cumulative Poker and Sportsbook gaming volume has been processed through the platform. This represents settled gaming activity rather than deposits, withdrawals or BetFi revenue.

These production metrics, including gaming volume, Poker and Sportsbook activity, rake data and measurement methodology, are publicly available for verification: 

Platform Live Stats: <https://betfi.poker/stats>

Live platform: [**https://betfi.poker/**](https://betfi.poker/)

### Applicant name

BetFi Poker

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

BetFi is built to be self sustaining, not grant dependent. Poker generates revenue through rake on completed games, while Sportsbook generates revenue through gaming activity. Our VIP Table Ownership model shares rake with participating partners while creating recurring platform revenue and community driven growth.

Future Prediction Markets will add another revenue and engagement channel. Catalyst funding will accelerate the new CIP 0113 Programmable Token integration, not subsidize existing operations, player bankrolls, prizes or liquidity.

After the Pilot, users continue paying through normal platform activity. Revenue supports ongoing development, infrastructure and operations, while Poker, Sportsbook, Prediction Markets and partner owned tables create multiple reasons for users to return.

### Programmable tokens (CIP-0113) - expected transaction count

2000

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

The 50,000 ADA will allow BetFi to prioritize and accelerate a dedicated CIP 0113 integration outside our current development budget. Funding will support CIP 0113 architecture and Cardano development (20,000 ADA), BetFi product and wallet integration (12,000), testing, QA and security review (8,000), mainnet deployment and monitoring (5,000), and documentation, analytics and adoption measurement (5,000). BetFi will continue funding existing Poker and Sportsbook operations independently. Catalyst funding is specifically for moving this new Cardano capability from concept to production and measurable real user adoption.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Within 3 months, BetFi will design, build, test and deploy our CIP 0113 Programmable Token integration to Cardano mainnet within our existing production platform. Deliverables include programmable token architecture and policy, Cardano wallet integration and live user flows for player access, tournaments, membership and partner experiences. We will demonstrate repeatable mainnet transactions from real external users and publish required policy IDs, script hashes, addresses, message tag and team wallets. M1 will include release notes, test and security evidence, production URL, explorer transaction evidence, walkthrough video and Demo Day presentation.

**Budget:** 20,000 ADA CIP 0113 architecture and Cardano development; 12,000 ADA product and wallet integration; 8,000 ADA testing, QA and security; 5,000 ADA mainnet deployment and monitoring; 5,000 ADA documentation, analytics and adoption measurement.

### How far along is the integration you're proposing, today?

TRL 2 - Technology concept formulated

### Programmable tokens (CIP-0113) - fee target (ADA)

350

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

BetFi is a live Cardano powered gaming platform spanning Poker and Sportsbook, with Prediction Markets planned next. We already operate in production on Cardano and, to our knowledge, have built the first operational Multi Table Tournament (MTT) poker system on Cardano.

The challenge is creating deeper on chain utility and engagement within blockchain gaming while making Cardano useful to everyday users beyond basic transfers.

We propose integrating CIP 0113 Programmable Tokens into BetFi’s existing production platform. Programmable assets will connect Cardano wallets with useful BetFi experiences such as player access, tournament participation, membership, achievements and partner experiences. This creates genuine user initiated Cardano activity through programmable token mints, transfers and applicable rule interactions.

BetFi is also expanding Cardano access through our ChangeNOW.io integration/partnership, giving users from other blockchain ecosystems a pathway to convert supported assets into ADA.

Success will be measured through mainnet deployment, qualifying transactions, external wallets, network fees and repeat usage.

### Supporting links (repo, site, demo)

- https://betfi.poker/

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

The proposed CIP 0113 Programmable Token integration is currently TRL 2. The concept and intended use within BetFi have been defined, while development and mainnet deployment have not yet begun. We plan to integrate programmable tokens into our existing BetFi ecosystem to provide real utility for users through features such as player access, tournament participation, VIP membership, achievements and partner experiences. BetFi itself is already a live TRL 9 production platform, giving our development team an established environment to build, test and deploy the new integration. Catalyst funding will move the integration from concept through development, testing, mainnet deployment and measurable real user adoption.
