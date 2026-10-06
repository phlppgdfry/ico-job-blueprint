# ICO Job Blueprint · ROLE / OS

Onafhankelijk Nederlandstalig **Job Operating System** voor de vacature [IT Development Officer bij ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). Geen intern ICO-handboek, affiliatie of sollicitatiegarantie.

30 volledige hoofdstukken (circa 30.000 woorden), 35 herleidbare vacaturevereisten, 16 technische onderwerpen, 25 praktijkscenario’s, 14 incidentplaybooks, 56 interviewvragen, 30 vragen aan ICO en 3 portfolio-bouwopdrachten. Onderzocht op 7 oktober 2026.

## Begin hier

- [Researchdossier en bronnen](research/DOSSIER.md)
- [Volledig Job Blueprint / Role Playbook](docs/JOB-BLUEPRINT.md)
- [Ontwerpspecificatie](docs/DESIGN.md)
- [Kwaliteitscontrole en beperkingen](docs/AUDIT.md)

De webapp biedt negen modules, zoeken tot op hoofdstuksectie, inklapbare content, architectuurdiagram, interactieve checklists, lokaal opgeslagen notities/voortgang, skills/evidence-tracker per skill en R-ID, roadmap en dark/light mode. Scenario’s en interviewvragen hebben eigen antwoorden, een timer en model/rubric voor zelfbeoordeling. **Geen AI-score.**

## Lokaal draaien

Node.js 20.19+ of 22.12+ aanbevolen; npm en Python 3 voor contentgeneratie.

```sh
npm ci
npm run dev
```

Open `http://127.0.0.1:5187`. Productiebouw: `npm run build`. Preview: `npm run preview`. De app is statisch en gebruikt geen server/API/database voor persoonlijke voortgang.

## Inhoud aanpassen

`scripts/content.py` is de bron van het playbook en de oefendata. `research/DOSSIER.md` beheert de bronnen/claims. Genereer daarna de JSON, standalone Markdown en download:

```sh
python3 scripts/content.py
npm test
npm run build
```

`src/content.json`, `docs/JOB-BLUEPRINT.md` en `public/JOB-BLUEPRINT.md` zijn gegenereerde bestanden. Niet afzonderlijk aanpassen. UI-modules staan in `src/`; `model.mjs` en `state.jsx` beheren zoeken, importvalidatie en opslag.

## Verificatie

```sh
npm test
npx playwright install chromium
npm run dev
# in een tweede terminal:
npx playwright test
```

`QA_BASE_URL` kan dezelfde tests op de live statische site uitvoeren. Tests controleren scope, veilige import, zoekroutes, alle hoofdstukken, modules, checklists, notities, oefeningen/timer, skills/requirements, export/import, thema en mobiel gedrag. Een workflow bouwt en publiceert de statische app via GitHub Pages; geen secrets of eigen server nodig.

## Bronstatus en privacy

**Expliciet uit vacature** staat los van **Waarschijnlijk / afgeleid uit functiecontext**. Publieke bedrijfscontext en algemene sectorpraktijk zijn herkenbaar gemarkeerd. Productnamen zijn geen bewijs van versies/topologie. Apex is waarschijnlijk Oracle APEX, maar nog te bevestigen. LinkedIn-inhoud kon niet opgehaald worden en is niet gebruikt.

Geen CV aangeleverd: persoonlijke geschiktheid en gaps zijn nog niet beoordeeld. Alle voorbeelden/data zijn synthetisch. Drie portfolio-projecten zijn ontwerpen, geen al gebouwde enterprise-applicaties. Productlicenties/bedrijfstoegang niet nodig om dit leerinstrument te gebruiken.

Voortgang en antwoorden worden alleen in browser-localStorage opgeslagen. Export/import biedt backup en apparaatwissel. Geen account, analytics, cloudsync of AI-verwerking. Opslag kan gewist worden door browserinstellingen; maak zelf exports. Systeemlettertypen en alle inhoud worden zonder externe font-/trackingdiensten gebruikt.

## Veilig gebruik

Oefenrunbooks geven geen toestemming om productie te wijzigen. Stem mandaat, gegevensgebruik, herstelplan en securityprocedure af met echte eigenaren. Verkoop lab/conceptbewijs nooit als professionele AIX/Oracle/iWay/TOS-ervaring.
