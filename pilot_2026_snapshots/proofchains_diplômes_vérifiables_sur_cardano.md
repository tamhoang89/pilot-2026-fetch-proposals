# PROOFCHAINS : Diplômes vérifiables sur Cardano

> Le diplôme est sur papier, mais la preuve du mérite doit durer. PROOFCHAINS la rend vérifiable en ligne, même lorsque le document ou les archives disparaissent.

## Proposal Metadata

- **Status:** finalized
- **Revision:** 1
- **Proposer:** `stake1uxddfwete6jxt5ug0derhpj58zfm38dvhvwepqurfxxrdjs3977v2`
- **Funding requested:** ₳150,000
- **Last finalized:** 2026-08-20T04:03:59.722000+00:00

### What is the current status and Technology Readiness Level of your existing product?

TRL 6 - Technology demonstrated in relevant environment

### Why is your team well-suited to deliver this?

L’équipe PROOFCHAINS réunit les compétences nécessaires pour transformer un prototype existant en solution pilote. Jonas Makeke assure la coordination, le développement Web3/Cardano, l’adoption, les partenariats et le suivi des livrables. Alain Paluku prend en charge le développement technique et produit, notamment la plateforme d’émission, le système de vérification et l’intégration blockchain.

Cette complémentarité couvre le développement logiciel, l’intégration Cardano, la gestion de projet et les relations avec les établissements. Le dépôt public et le prototype fonctionnel de PROOFCHAINS prouvent que l’équipe a déjà commencé à construire et tester le produit.

Pour les besoins spécialisés, notamment l’audit de sécurité et l’UX/UI, nous ferons appel à des collaborateurs identifiés avant leur intervention. Le financement permettra à l’équipe de finaliser, sécuriser et déployer PROOFCHAINS auprès des établissements pilotes.

### Eligible area

Yes

### How will your product generate genuine usage - who transacts, why, and how often? Justify your previously declared targets as reasonable but ambitious enough to be considered valid.

PROOFCHAINS sera utilisé par les établissements pilotes qui délivrent les diplômes et qui seront responsables de créer les attestations CIP-0170/KERI. Chaque établissement utilisera son propre portefeuille pour signer et ancrer les informations vérifiables liées aux diplômes ; les frais seront donc payés par des participants externes et non par l’équipe seule.

Nous prévoyons trois établissements pilotes pendant 10 semaines. Chacun créera environ 100 attestations, soit 300 transactions Cardano au total. Cela représente en moyenne 10 attestations par établissement et par semaine, un objectif cohérent avec l’émission progressive de diplômes et la validation des dossiers. Les étudiants et diplômés utiliseront ensuite les preuves, tandis que les employeurs et institutions partenaires pourront les vérifier.

Les transactions seront suivies sur Mainnet et comparées aux credentials émis, aux établissements actifs et aux vérifications réalisées. Le pilote permettra ainsi de mesurer une utilisation réelle de CIP-0170 et d’ajuster le modèle avant son extension à d’autres établissements.

### How will you reach and onboard real users - and what evidence backs your channels?

PROOFCHAINS adoptera une approche B2B en ciblant les universités, instituts supérieurs, écoles et organismes de formation en RDC. Notre réseau local permettra d’identifier les décideurs, de présenter la plateforme et d’obtenir des établissements pilotes. Les démonstrations du site et du portail montreront une solution fonctionnelle.

L’intégration commencera par la configuration d’un établissement, la formation du personnel, l’émission de credentials et l’accompagnement aux vérifications. Après validation, nous intégrerons d’autres établissements. Notre réseau Cardano et Web3 apportera des retours techniques et des partenaires.

La preuve actuelle repose sur un prototype public, un dépôt open source et de premiers tests utilisateurs. Pendant les 10 semaines financées, nous mesurerons les établissements actifs, les credentials émis, les vérifications, les utilisateurs formés et les transactions Cardano. Les résultats des pilotes serviront à convaincre de nouveaux établissements.

### Is the underlying project open source?

Yes

### Short Video Pitch

https://youtu.be/WZUOnXIhghY?si=ERTcbX4yhW3khqme

### Who else solves this today - competitors/alternatives, and why does your approach win?

Les alternatives à PROOFCHAINS sont les diplômes papier, les archives internes, les vérifications par e-mail et des plateformes comme [Diplome.cd](http://Diplome.cd), principalement orientée vers les diplômes d’État en RDC. Des solutions internationales utilisent aussi la blockchain.

PROOFCHAINS cible les universités, instituts supérieurs, écoles et organismes de formation. L’établissement conserve le diplôme papier, mais lui associe une preuve vérifiable sur Cardano, accessible par identifiant ou QR code. Les diplômés peuvent préserver et partager cette preuve, tandis que les employeurs vérifient plus rapidement les documents. Notre différenciation sera mesurée par les établissements pilotes, les credentials émis, les vérifications effectuées et l’utilisation réelle de Cardano.

### Please provide details about the Technology Readiness Level selected for your existing product

PROOFCHAINS dispose actuellement d’un prototype fonctionnel accessible publiquement, avec un portail d’émission, une interface de vérification et une intégration Cardano testée sur le réseau Preprod. Le site public, la démonstration et le dépôt open source permettent de vérifier l’existence du produit et de ses principales fonctionnalités.

Le prototype a dépassé le stade de la preuve de concept : le parcours d’émission et de vérification a été développé et présenté dans un environnement pertinent. Toutefois, le déploiement Mainnet, le renforcement de la sécurité, la formation des établissements et l’utilisation régulière par des institutions pilotes restent à réaliser. Le financement demandé permettra de franchir cette étape vers une utilisation opérationnelle.

### What is your on-chain architecture, and why is it the right fit for selected integration(s) and this area of interest's technical requirements?

L’architecture on-chain de PROOFCHAINS repose sur Cardano, avec un actif numérique unique associé à chaque diplôme papier. L’établissement émet le credential depuis son portefeuille ; un identifiant ou un QR code placé sur le document permet ensuite d’accéder à la preuve et de la vérifier.

Les métadonnées nécessaires à la vérification sont ancrées sur Cardano, tandis que les fichiers ou informations complémentaires sont conservés via IPFS. Lucid est utilisé pour construire et soumettre les transactions Cardano, et Blockfrost pour consulter les données de la blockchain. L’interface de vérification contrôle l’identifiant, l’émetteur et l’intégrité des informations associées au credential.

Cette architecture sépare les données volumineuses de la preuve on-chain, tout en conservant une référence publique, durable et vérifiable. Elle convient au projet parce qu’elle permet aux établissements de continuer à délivrer des diplômes papier, aux diplômés de préserver une preuve partageable et aux employeurs de vérifier les documents sans dépendre uniquement d’échanges manuels avec l’établissement.

Le prototype a été testé sur Cardano Preprod. Le financement permettra de renforcer la sécurité, finaliser le déploiement Mainnet et valider l’architecture avec des établissements pilotes. Si CIP-0170 est conservé comme intégration sélectionnée, les éléments KERI requis devront être implémentés et démontrés séparément.

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

Le marché cible principal de PROOFCHAINS est constitué des universités, instituts supérieurs, écoles et organismes de formation en RDC, puis dans d’autres pays africains. Ce sont eux qui délivrent les diplômes et peuvent financer le service. PROOFCHAINS les aide à conserver une preuve vérifiable des qualifications délivrées et à répondre plus rapidement aux demandes d’authentification.

Un second segment regroupe les employeurs, recruteurs et établissements qui doivent vérifier les diplômes de candidats. Au lieu de dépendre uniquement de documents papier, d’archives difficiles d’accès ou de procédures manuelles, ils peuvent vérifier une preuve associée au diplôme sur Cardano.

Les étudiants et diplômés sont les principaux bénéficiaires, mais pas les premiers payeurs. Leur établissement peut leur offrir une preuve durable, retrouvable et partageable si le diplôme papier est perdu ou si les archives disparaissent.

La demande initiale repose sur un problème réel, un prototype fonctionnel, une plateforme publique, un dépôt open source et de premiers tests utilisateurs. Le financement permettra de valider l’adoption auprès d’au moins trois établissements pilotes en mesurant les établissements actifs, les credentials émis, les vérifications effectuées et les transactions Cardano.

### Applicant name

Yedidya kahire Gandura

### What is your business model, and what keeps this running after the pilot? Who pays, and why does usage continue once grant funding ends?

PROOFCHAINS adoptera un modèle B2B. Les universités, instituts supérieurs, écoles et organismes de formation seront les clients et les principaux financeurs, car ils doivent émettre, conserver et faire vérifier leurs diplômes. Les employeurs et autres institutions utiliseront la plateforme pour authentifier les documents des candidats. Les étudiants et diplômés bénéficieront gratuitement d’une preuve durable et partageable de leur réussite.

Pendant le pilote de 10 semaines, Catalyst financera le renforcement du produit, la sécurité, le déploiement Mainnet, la formation et l’accompagnement des établissements. Après le pilote, les établissements paieront un abonnement ou des frais liés à l’émission et à la gestion des credentials. Ces revenus financeront l’hébergement, les transactions Cardano, la maintenance, le support et l’acquisition de nouveaux établissements. PROOFCHAINS pourra ainsi fonctionner sans dépendre en permanence des subventions.

### On-chain identity (CIP-0170) - expected transaction count

300

### Named, verifiable team

Yes

### Real users

Yes

### What does this funding enable that wouldn't happen otherwise - and, at a high level, what will it be spent on?

Le prototype PROOFCHAINS existe déjà, mais l’équipe ne dispose pas des ressources nécessaires pour le transformer seule en service Mainnet sécurisé et utilisé par des établissements. Le financement Catalyst permettra de finaliser l’intégration Cardano, renforcer la sécurité, déployer l’infrastructure, former les établissements pilotes, financer leur onboarding et mener une campagne d’adoption mesurée.

Les 150 000 ADA couvriront le travail de l’équipe, la documentation, le support, le suivi des résultats et une réserve pour les imprévus. Sans ce financement, PROOFCHAINS resterait limité à un prototype Preprod. Avec lui, nous réaliserons un pilote de 10 semaines et mesurerons les établissements actifs, les credentials émis, les vérifications effectuées et les transactions Mainnet générées.

### I confirm that I have read, understood and shall adhere to the Terms & Conditions, Fund Rules, Proof of Adoption & Standard, and Privacy Policy. I understand that providing accurate and truthful information is essential for my proposal to remain eligible to participate in the current Fund.

Yes

### Real target

Yes

### M1 outputs: what measurable, tangible deliverables will you complete within the 3-month window to reach mainnet?

Au terme des trois mois, nous livrerons PROOFCHAINS sur Cardano Mainnet avec l’intégration CIP-0170/KERI fonctionnelle. Un établissement pilote réalisera une transaction complète avec son propre portefeuille, puis le flux sera répété sans erreur avec les autres établissements.

Nous fournirons l’URL du produit, les hachages des transactions avec leurs liens vers l’explorateur, les identifiants déclarés de l’intégration, une vidéo de démonstration, les notes de version, le dépôt open source avec son commit de livraison et un dossier de tests comprenant la checklist, le journal des bugs et une note de sécurité.

Nous formerons les établissements pilotes, documenterons l’émission et la vérification, puis présenterons les résultats lors du Demo Day. Ces preuves confirmeront le fonctionnement réel de l’intégration et prépareront la mesure de l’adoption.

### How far along is the integration you're proposing, today?

TRL 6 - Technology demonstrated in relevant environment

### On-chain identity (CIP-0170) - fee target (ADA)

88

### Clear budget

Yes

### Genuine new work

Yes

### One proposal

Yes

### What solution are you building, and what specific problem does it solve - for whom?

En République démocratique du Congo, particulièrement dans l’Est du pays, les conflits et les déplacements forcés peuvent faire disparaître les documents scolaires et académiques. Lorsqu’une famille fuit des zones comme Goma ou Rutshuru, les diplômes, certificats et relevés peuvent être perdus, détruits ou rester dans des écoles devenues inaccessibles. Pour un étudiant, cela peut signifier perdre la preuve de plusieurs années d’efforts et rendre son parcours difficile à vérifier.

C’est pour répondre à cette réalité que nous avons créé PROOFCHAINS. Les établissements continuent de délivrer leurs diplômes papier, mais chaque document est associé à une preuve numérique unique et vérifiable sur Cardano. Un identifiant ou un QR code permet de retrouver cette preuve en ligne, même si le papier est perdu ou si les archives disparaissent. Les diplômés peuvent préserver et partager leur réussite, tandis que les employeurs et les établissements partenaires peuvent vérifier plus rapidement l’authenticité des documents.

PROOFCHAINS s’adresse aux établissements d’enseignement, aux étudiants, aux diplômés, aux employeurs et aux institutions partenaires. Le financement permettra de renforcer le prototype, d’améliorer sa sécurité, de préparer le déploiement Mainnet et de le tester auprès d’établissements pilotes en RDC.

### Supporting links (repo, site, demo)

- https://proofchains.org/
- https://docs.google.com/document/d/1vIOXKV1nL2IuUDyHFRGcvmU6jI5fuCdQCgjRB3lsWYc/edit?tab=t.0
- https://github.com/alainpaluku/PROOFCHAINS
- https://youtu.be/6DV1eMeAnC4?si=U6jFGLpfkteByyKq

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

Le code source de PROOFCHAINS est public sous licence MIT : <https://github.com/alainpaluku/PROOFCHAINS>. Catalyst financera l’amélioration du code, de la sécurité et de l’intégration Cardano. Les établissements paieront l’hébergement, l’onboarding, la formation, le support, la maintenance et la personnalisation. La marque et l’infrastructure déployée restent gérées par l’équipe.

### Technical

Yes

### Public proposal

Yes

### Confirmation: our plan complies with the [Transaction Integrity Standard](https://docs.projectcatalyst.io/open-funding/funding-basics/proof-of-adoption-and-standard#transaction-integrity-standard)

Yes

### Standard read and attested

Yes

### Please provide details about the Technology Readiness Level selected for the integration you're proposing

L’intégration Cardano de PROOFCHAINS a été développée et testée sur le réseau public Cardano Preprod. Le prototype permet d’associer à chaque diplôme papier une preuve numérique vérifiable, accessible par identifiant ou QR code. Le site public, la démonstration et le dépôt open source montrent que l’intégration a dépassé le stade de la conception théorique. Elle n’est toutefois pas encore déployée durablement sur Cardano Mainnet ni utilisée par des établissements pilotes en production. Le financement permettra de renforcer la sécurité, finaliser le déploiement Mainnet, former les établissements et mesurer les credentials émis, les vérifications effectuées et les transactions générées.
