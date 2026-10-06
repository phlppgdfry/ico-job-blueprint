# Kwaliteitscontrole — ICO Job Operating System

Datum: 7 oktober 2026. Gecontroleerd tegen de volledige publieke vacature, researchdossier en gevraagde 30 delen. Onafhankelijke auteurscontrole; geen review of goedkeuring door ICO.

## Inhoudelijke kwaliteit

35 vacatureclausules als R01–R35: functiecontext/opleiding/uren/wachtdienst, waarden/voordelen, projectplanning, outsourcing/budget/capaciteit, modelling/releases, volledige stack, EDI/rapportering/portalen/development, portefeuille, afwijkingen, tweede lijn, rapportage, teams/training, talen/Office/methode, gedrag/rapporteerlijn/contacten, beide sites en kwaliteit/veiligheid/milieu. Alles opgenomen in hoofdstuk 2 en bewijsmatrix. De 30 hoofdstukken zijn aanwezig, circa 30.500 woorden.

Technologiehandboek: 16 onderwerpen met alle 15 gevraagde uitleg-/praktijkvelden en 44 jargondefinities. Conceptanalogieën onderscheiden van productexpertise. Geen toegewezen cloud, CI/CD-product, SSO, EDI-standaard of teamgrootte verzonnen. APEX/ORDS onderscheiden van JBoss; productversies onbekend. Een in de Context7-resultaten meegekomen destructief APEX-removal-commando is bewust niet overgenomen.

## Praktische bruikbaarheid

25 gestructureerde, toenemend moeilijke cases met scope, onbekenden, vragen, oorzaken, bewijs/logs, DB/netwerk/app/integratie, aanpak, hypothese, herstel, communicatie, preventie en rubric. 14 zijn ook als incidentrunbook aangeboden; hergebruik is uit dezelfde dataset zodat de twee views niet uiteenlopen. 56 vragen in acht categorieën met intentie, sterke/zwakke antwoorden en vervolgvragen; vijf hebben aparte 2-minutenuitwerking. 30 vragen aan ICO, tien prioritaire. Drie portfolio-ontwerpen volledig met requirements, architectuur, security, tests, release en bewijs. Deze projecten zijn bouwopdrachten, niet al gebouwde productsystemen.

Leerplan met 7 afzonderlijke dagen, 30/60/90-voorbereiding, deliverables en stopcriteria. Afzonderlijk 30/60/90-onboardingplan en eerste werkweek. Niveaus, gaptypes en credential/experience-beperkingen expliciet. Geen persoonlijke ervaring verzonnen of kandidaatgeschiktheid beoordeeld zonder CV.

## Betrouwbaarheid

Firecrawl: vacature, bedrijfscontext, officiële productpagina’s en twee inhoudelijk gelezen vergelijkingsvacatures. Context7: Oracle APEX officieel geraadpleegd. LinkedIn werd door providerinstelling geblokkeerd; geen inhoud gebruikt. Eerste TIBCO-routes gaven generieke inhoud; vervangen door juiste ibi-pagina’s. Percentageverdeling, scores, leertijd, systeemverbindingen en cases zijn expliciet inschattingen/afleiding. Algemeen sectorwerk is geen intern bedrijfsfeit.

## Functionele controle

Browser/IAB-acquisitie via CUA gaf **“No browser is available”**. Daarom Playwright Chromium gebruikt. macOS blokkeerde de browserlaunch binnen de sandbox; de tests zijn daarna met toestemming buiten de sandbox uitgevoerd. Dit was een uitvoeringsbeperking, geen appfout.

| Controle | Resultaat / bewijs |
|---|---|
| Build | Vite-productiebouw geslaagd; app/vendor/content apart, geen chunkwaarschuwing |
| Inhoud/scope | Node-test: 30 chapters, 35 requirements, 25 cases, 56 vragen, 3 projecten, complete techvelden |
| Import/opslag | Validatie van schema/waardetypes; corrupt/geblokkeerd storage valt veilig terug; UI meldt schrijffout |
| Zoekfunctie | Full-content zoekresultaten; directe sectieroute en lege resultaten gecontroleerd |
| Navigatie | Alle negen modules, bronnen en 30 hoofdstukken gerenderd |
| Checklists/notities | 30 proceschecks in hoofdstuk 11; wijziging/reload behoudt keuze en notities |
| Voortgang | Afgevinkt hoofdstuk overleeft reload en verandert werkelijk percentage |
| Scenario’s | Filter, eigen antwoord, timer, modelaanpak en bewaarde rubric gecontroleerd |
| Interviews | 56 vragen, categoriefilter, eigen antwoord, model en vervolgvragen gecontroleerd |
| Skills/bewijs | Niveau, bewijs, R01-notitie en reload getest |
| Roadmap | Periodecheck blijft na reload bewaard |
| Export/import | Werkelijke JSON-download, afwijzing fout schema en succesvolle roundtrip |
| Dark/light | Reload bewaart theme; contrast visueel opnieuw gecontroleerd |
| Mobiel | 390×844: menu/Escape/navigatie, cases, chapter table en skills zonder documentoverflow |
| Console | Geen page-/consolefouten bij definitieve capture van dashboard/reader/scenario/mobile |
| Downloads/bronnen | Playbook aanwezig in dist; bronhrefs in dossier, geen verzonnen bronnen |

Vier Node-tests en zes end-to-endtests slagen. Scripts: `npm test`, `npx playwright test`, `npm run build`. Unitchecks toetsen inhoudelijke afspraken en importgrenzen; UI-tests toetsen echt gebruikersgedrag.

## Publicatie en live controle

Openbare repository: [phlppgdfry/ico-job-blueprint](https://github.com/phlppgdfry/ico-job-blueprint). Live: [ROLE / OS](https://phlppgdfry.github.io/ico-job-blueprint/). [GitHub build/test/deployment](https://github.com/phlppgdfry/ico-job-blueprint/actions/runs/37547745720) afgerond met success voor build en deploy. De actuele release-tags van de vijf officiële GitHub Actions zijn via GitHub API gecontroleerd voordat de workflow werd geschreven.

Na publicatie gaf de site HTTP 200. Alle zes end-to-endtests zijn ook op de live app geslaagd, inclusief alle 30 hoofdstukken, search, persistence, import/export en mobiele weergave. De tests gebruiken relatieve routes zodat de projectsubdirectory op GitHub Pages correct blijft. Code en inhoud van de live app zijn dezelfde als de gecontroleerde lokale versie.

## Gevonden en daadwerkelijk hersteld

1. Dubbele H1 op bronpagina: Markdown-brontitel naar H2 gerenderd.
2. Mobiele skills-overflow door absoluut geplaatste verborgen labels: scrollcontainer krijgt eigen positioneringscontext; documentbreedte 390px bij viewport 390px.
3. Onleesbare ruwe Markdown in hoofdstukpreview: taakgerichte samenvatting per hoofdstuk toegevoegd.
4. Technologielinks openden alleen handboekbegin: direct naar betreffende sectie navigeren.
5. Zoekresultaten stuurden naar lang hoofdstukbegin: directe sectieroutes/open/scroll toegevoegd.
6. Import accepteerde ongeldige waardetypes: types, hoofdstuknummers en skillniveaus gecontroleerd.
7. Dark-modecapture toonde overgangskleur met tijdelijk laag contrast: kleurtransitie op buttons verwijderd; definitieve capture helder.
8. Grote single chunk: app, vendor en inhoud apart gebundeld.
9. Extern fontrequest: verwijderd; app gebruikt systeemlettertype zonder externe fontservice.
10. Ontbrekende jargonverklaringen: 44 concrete definities en legacy-analogieën toegevoegd.

## UI/UX en ontwerpvergelijking

Concept en laatste render allebei met `view_image` bekeken in dezelfde QA-pass. Native conceptmaat 1505×1045 gecontroleerd; extra mobiel 390×844. [Referentie](assets/design-reference.png), [desktop](assets/dashboard.png), [dark](assets/dark-mode.png), [mobiel](assets/mobile.png).

| Vergelijkingspunt | Waarneming / verwerking |
|---|---|
| Informatiehiërarchie | Sidebar, heading/subtitle, CTA, preparationpanel, architecture en chapter rows volgen concept |
| Palette | White canvas, navy rail/panel, orange CTA en grijze hairlines behouden |
| Containers/spacing | Tweepanel-layout en open rijen; rail 246px/topbar 54px; rowpadding verfijnd |
| Typografie | System sans fallback, expliciete heading/control/body sizes; geen externe fontdependency |
| Iconen | Consistente dunne lijniconen; decoratieve crane weggehaald om RoRo-context niet te vertekenen |
| Copy | Hoofdtitel/subtitle/CTA en negen modules behouden; extra bronstatus/voortgangsbetekenis bewust toegevoegd |
| Architectuur | Gecontroleerde inhoudcorrectie: Oracle is database, EDI/BI zijn aanvullende stromen; hypotheses gelabeld |
| Responsive | Sidebar drawer, verticale flow, interne table scroll en éénkolomsoefening op mobiel |

De uitvoering is tegen de gekozen ontwerpspecificatie visueel geverifieerd. Intentionele afwijkingen staan ook in DESIGN.md: juiste architectuur, geen containerkraan, bronnenmodule, echte voortgangsbetekenis, systeemfont en extra volledige hoofdstukken. Geen fixbare clipping/overflow/contrast-/interactiefouten bij de gecontroleerde schermen. Geen claim van pixel-identieke replica: functionele en inhoudelijke correctheid bepaalt de expliciete afwijkingen.

## Restbeperkingen

- Geen persoonlijke CV/GitHub-analyse, geen professionele kandidaatreadinessscore.
- Geen AI-feedback, login, serveropslag of cloudsync; rubric is zelfbeoordeling, exports zijn backup.
- Niet getest in Safari/Firefox, op echte telefoons of met screenreader; Chromium desktop/mobile en keyboarddrawer gecontroleerd.
- Geen productie-ICO-omgeving, productsandbox, licenties, echte incidentdata of interne procedures; geen enterprise-producttests.
- Publieke pagina’s kunnen veranderen; verifieer open vragen tijdens gesprek/onboarding.
- Leertijden en werkmix zijn niet empirisch gemeten bij ICO.
