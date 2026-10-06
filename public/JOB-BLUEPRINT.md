# ICO IT Development Officer — Job Blueprint / Role Playbook

Onderzocht 7 oktober 2026. Onafhankelijk leerinstrument; geen intern ICO-handboek. Geen persoonlijke CV-analyse zonder profiel.

1. [Executive summary](#01)
2. [Vacature regel voor regel](#02)
3. [De functie in de praktijk](#03)
4. [Verantwoordelijkheden](#04)
5. [Technische architectuur](#05)
6. [Technologiehandboek](#06)
7. [Businesskennis](#07)
8. [Skills matrix en prioriteiten](#08)
9. [Mentale modellen](#09)
10. [Troubleshooting playbook](#10)
11. [Incident, problem, change en release](#11)
12. [Requirements naar technische oplossing](#12)
13. [Stakeholder management](#13)
14. [25 praktijkscenario’s](#14)
15. [Interview question bank](#15)
16. [Vragen aan ICO](#16)
17. [Portfolio strategie](#17)
18. [Bewijsmatrix](#18)
19. [Gap analysis](#19)
20. [Gericht leerplan](#20)
21. [Wat moet ik niet leren?](#21)
22. [Sollicitatiestrategie](#22)
23. [30 / 60 / 90 dagen na start](#23)
24. [First week survival guide](#24)
25. [Performance playbook: 6–12 maanden](#25)
26. [Career path](#26)
27. [Moeilijkheidsgraad](#27)
28. [Red flags / green flags](#28)
29. [Cheat sheet voor het gesprek](#29)
30. [Final assessment en acties](#30)

<a id="01"></a>

# DEEL 01 — Executive summary

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

## Wat doe je werkelijk?

Je bent de technische schakel tussen terminaloperaties, applicaties, het ontwikkelingsteam en externe leveranciers. Je helpt businessvragen scherp maken, zet ze om in uitvoerbare technische plannen, begeleidt implementaties en zorgt dat bestaande systemen blijven functioneren. Je combineert projectcoördinatie met applicatiebeheer en hands-on verbetering. Een werkend scherm is onvoldoende: de achterliggende data, integratie, opleiding en overdracht moeten ook kloppen.

## Waarom bestaat de rol?

**Expliciet uit vacature:** ICO wil zijn core-systemen beheren en een nieuw Terminal Systeem en applicatieve vernieuwingen realiseren. Dat vraagt iemand die zowel de technische samenhang als planning, leveranciers en gebruikers bewaakt. Je lost versnipperd eigenaarschap, onduidelijke technische scope, falende koppelingen en gebrekkige releaseafstemming op.

## Persoonlijke verantwoordelijkheid en output

Je bent verantwoordelijk voor efficiënt ontwikkelen, implementeren en beheren van applicatieomgevingen in Kallo en Zeebrugge. Verwachte output: technische plannen, specificaties, CRQ’s, werkpakketten, componentmodellen, gecontroleerde releases, nieuwe functionaliteit/koppelingstools, opgeloste en afgeronde tweedelijnstickets, opleiding en wekelijkse voortgangsrapportage. Budgetgoedkeuring en personeelsmanagement zijn niet expliciet aan jou toegewezen. Je stuurt taken en externe uitvoering, en stemt beslissingen af met Supervisor/Director IT.

## Techniek, business en werkmix

Technisch hoog: je moet over meerdere lagen kunnen redeneren. Businessgericht hoog: een correcte verwerking van terminaldata bepaalt of een oplossing bruikbaar is. Programmering is expliciet onderdeel van de rol, maar de vacature geeft geen taal of percentage. Als werkhypothese: ongeveer 10–25% bouwen/scripten en de rest analyse, beheer, support, tests en coördinatie, sterk afhankelijk van TOS-projectfase. Zie hoofdstuk 3 voor een totaalverdeling die 100% vormt.

| Karakter | Betekenis in deze rol |
|---|---|
| Application management | Kern: continuïteit, componentkennis, lifecycle en configuratie |
| Projectmanagement | Kern: technische werkpakketten, leveranciers, capaciteit en budget |
| Business analysis | Belangrijk: behoeftenanalyse ondersteunen en gebruikers trainen |
| Integratie | Kern: EDI, koppelingen en ketenconsistentie |
| Development | Aanwezig: functies, portalen en tools; omvang onbekend |
| Operations/support | Kern: tweede lijn en expliciete wachtdienst |
| Infrastructure | Begrip nodig; volledige platformverantwoordelijkheid niet bewezen |
| Consulting | Adviserende vaardigheden intern/naar partners; geen consultancyfunctie vermeld |
| Product/architectuur | Afgeleid: prioriteren en afhankelijkheden ontwerpen, geen productowner-titel |

## Met wie werk je?

**Expliciet uit vacature:** Supervisor, Director IT, projectcoördinator, alle business units, intern/extern ontwikkelingsteam, leveranciers, klanten en Service Desk. **Waarschijnlijk / afgeleid:** operationele planners, infrastructuur- en securityverantwoordelijken; aparte teams zijn niet bevestigd.

## Vijf succesfactoren

1. Traceer een businesshandeling van gebruiker tot database en partnerbericht.
2. Herstel incidenten met controle op dataverlies en gevolgen voor operaties.
3. Lever concrete requirements, testbewijs en releaseafspraken aan partners.
4. Communiceer vroeg over impact, risico’s en besluiten, met eigenaar en datum.
5. Maak kleine betrouwbare verbeteringen en documenteer wat de volgende collega nodig heeft.

## De job in één minuut

“Ik zorg dat de applicaties voor terminaloperaties betrouwbaar werken en gecontroleerd verbeteren. Ik vertaal gebruikersvragen naar technische specificaties, stuur interne en externe uitvoering aan, beheer releases en onderzoek complexere incidenten. Daarbij begrijp ik hoe TOS, Oracle, JBoss, AIX en EDI samenhangen. Mijn resultaat is een bruikbare verandering die getest is, waarvan gebruikers weten hoe ze werkt en die we na livegang kunnen ondersteunen.”

<a id="02"></a>

# DEEL 02 — Vacature regel voor regel

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

De bronvereisten zijn volledig geparafraseerd en geordend; navigatie en algemene websitefooter zijn geen functievereisten. IDs vormen de koppeling met skills, portfolio en bewijs.

| ID / vacaturevereiste (parafrase) | Werkelijke betekenis | Praktijk | Moeilijkheid | Belang |
|---|---|---|---|---|
| R01 — Permanente functie, Zeebrugge, 38 uur | Een vaste rol met planning over meerdere projecten. | Plan capaciteit op 38 uur; reserveer interruptieruimte. | Basiskennis | Hoog |
| R02 — IT-master of bachelor gelijkgesteld door ervaring | Toon theoretische basis én toepasbare ervaring; precieze diploma-equivalentie navragen. | Koppel opleiding en projecten aan analyse, systemen en delivery. | Intermediate | Hoog |
| R03 — Dagshift, beperkte verplaatsingen en wachtdienst | Regulier dagwerk met beschikbaarheidsverplichtingen; rooster onbekend. | Vraag oproepfrequentie, compensatie, toegang en escalatiedekking. | Intermediate | Kritiek |
| R04 — Integriteit, intensiteit, innovatie | Eerlijk rapporteren, zorgvuldig afwerken en nuttig verbeteren. | Meld risico’s vroeg; beloof geen onbewezen oplossing. | Intermediate | Hoog |
| R05 — Arbeidsvoorwaarden en opleidingsmogelijkheden | Maaltijd/ecocheques, verzekeringen, GSM/laptop, wagen, vergoeding en cafetariaplan worden genoemd. | Vraag voorwaarden, budget en praktische opleidingstijd. | Beginner | Middel |
| R06 — Technische projectplannen beheren en rapporteren | Jij organiseert technische uitvoering en afhankelijkheden. | Maak mijlpalen, eigenaar, risico’s, planning en wekelijkse status. | Gevorderd | Kritiek |
| R07 — Externe bedrijven aansturen | Uitbesteden verwijdert je verantwoordelijkheid voor resultaat niet. | Specificeer deliverables, acceptatie, deadlines en escalaties. | Gevorderd | Kritiek |
| R08 — Core-systemen en nieuw Terminal Systeem | Continuïteit van huidige applicaties naast verandering. | Leg datastromen vast; plan migratie, test en herstel. | Gevorderd | Kritiek |
| R09 — Kwaliteit, veiligheid en milieu ondersteunen | IT-keuzes hebben operationele gevolgen. | Bespreek foutieve data, toegang, traceerbaarheid en veilige workarounds. | Intermediate | Hoog |
| R10 — Specificaties toetsen aan strategie/procedures/standaarden | Een technisch haalbare wijziging moet ook passen in afspraken. | Controleer ontwerp, security, lifecycle en changevoorwaarden. | Gevorderd | Hoog |
| R11 — Bijstaan in behoeftenanalyse | Vraag door naar probleem en gebruikersdoel. | Observeer huidige werkwijze; maak acceptatiecriteria. | Intermediate | Kritiek |
| R12 — Lastenboek, werkpakketten en CRQ | CRQ is het change request: waarom, wat, risico en goedkeuring. | Beschrijf scope, interfaces, tests, uren, rollout en rollback. | Gevorderd | Kritiek |
| R13 — Implementatie begeleiden | Delivery controleren tot het werkend in gebruik is. | Volg issues en afhankelijkheden; organiseer acceptatie en nazorg. | Gevorderd | Hoog |
| R14 — Gebruikers opleiden | Adoptie is deel van technisch succes. | Maak taakgerichte demo, oefencases en korte werkinstructie. | Intermediate | Hoog |
| R15 — Outsourcing coördineren | Organiseer de grens tussen interne en externe uitvoering. | Leg eigenaarschap, toegang, overdracht en exitdocumentatie vast. | Gevorderd | Hoog |
| R16 — Capaciteit en budget bewaken | Bewaken of inspanning en resultaat nog kloppen. | Vergelijk forecast/actual, scope en resterend werk; escaleer afwijkingen. | Gevorderd | Hoog |
| R17 — Applicatiecomponenten in kaart brengen/analyseren/evalueren | Ken componenten, afhankelijkheden en kwetsbare punten. | Maak componentcatalogus met eigenaar, versie en interface. | Intermediate | Kritiek |
| R18 — Releases op servers/systemen met partners coördineren | Versies moeten samen compatibel live gaan. | Gebruik releasekalender, compatibiliteitsmatrix en go/no-go. | Gevorderd | Kritiek |
| R19 — TOS met IBM P-series, AIX, Oracle en JBoss | Bedrijfskritische applicaties op enterpriseplatformen. | Traceer gebruiker → applicatie → query; stem platformproblemen af. | Gevorderd | Kritiek |
| R20 — EDI-processing en rapportering met WebFOCUS/iWay | EDI is gestructureerde gegevensuitwisseling tussen organisaties. | Volg bericht van ontvangst tot businessresultaat; controleer rapportdefinities. | Gevorderd | Kritiek |
| R21 — Webportalen opzetten en beheren | Gebruikersinterfaces met lifecycle en toegangsbeheer. | Beheer configuratie, permissies, tests, certificaten en releasebewijs. | Intermediate | Hoog |
| R22 — Nieuwe functionaliteit en koppelingstools ontwikkelen | Hands-on bouwen maakt deel uit van de functie. | Implementeer kleine wijziging met contract, validatie en logging. | Intermediate | Hoog |
| R23 — Projectportefeuille beheren | Meerdere projecten concurreren om dezelfde capaciteit. | Orden op impact, afhankelijkheden, risico en beschikbare mensen. | Gevorderd | Hoog |
| R24 — Afwijkingen proactief vinden en bijsturen | Niet wachten op mislukte oplevering. | Vergelijk voortgang met baseline en stel opties met gevolgen voor. | Intermediate | Hoog |
| R25 — Tweede lijn incident/problem/change tot afronding | Service Desk draagt complexere applicatieproblemen over. | Prioriteer, onderzoek, communiceer, herstel en documenteer oorzaak. | Gevorderd | Kritiek |
| R26 — Wekelijks IT en business rapporteren | Vertaal techniek naar voortgang en impact. | Meld resultaat, risico, budget/capaciteit, besluit en volgende stap. | Intermediate | Hoog |
| R27 — Intern/extern ontwikkelingsteam en training nieuwe collega’s | Technische samenwerking en taakgerichte sturing. | Doe review, overdracht en begeleid een collega met echte oefencase. | Intermediate | Hoog |
| R28 — IT-evoluties volgen; technische kennis en analyse | Maak passende verbeterkeuzes, geen technologie om zichzelf. | Vergelijk lifecycle, kosten en operationele haalbaarheid. | Intermediate | Hoog |
| R29 — PRINCE2 of andere projectmethode | Methodisch plannen, beslissen en risico’s beheersen. | Gebruik businesscase, fasering en tolerantie; certificaat niet expliciet vereist. | Intermediate | Hoog |
| R30 — MS Office en gerelateerde producten | Praktische analyse, rapportage en communicatie. | Gebruik Excel voor reconciliatie, Word voor CRQ, presentatie voor opleiding. | Basiskennis | Middel |
| R31 — Apex | Waarschijnlijk Oracle APEX gezien Oracle-stack; verifiëren. | Oefen formulieren, SQL-rapporten, validatie en rechten. | Intermediate | Hoog |
| R32 — Talen N/E/F | Waarschijnlijk Nederlands/Engels/Frans; niveau onbekend. | Leg incident uit, lees documentatie en voer leveranciersoverleg. | Intermediate | Hoog |
| R33 — Communiceren, organiseren, stress en taakgericht leidinggeven | Techniek en mensen onder druk op één resultaat richten. | Prioriteer transparant; benoem eigenaar en updatefrequentie. | Gevorderd | Kritiek |
| R34 — Supervisor/Director IT; projectcoördinator/business/klanten/leveranciers | Beslissen gebeurt in een netwerk van stakeholders. | Maak beslisrechten, escalatie en communicatie per doelgroep duidelijk. | Intermediate | Hoog |
| R35 — Applicatieomgevingen Kallo én Zeebrugge | Wijzigingen kunnen meerdere locaties raken. | Test locatieconfiguratie en operationele afhankelijkheden per site. | Gevorderd | Kritiek |

<a id="03"></a>

# DEEL 03 — De functie in de praktijk

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

## Een typische werkdag — illustratief, geen ICO-rooster

08:30–17:00 is een voorbeeld met pauze; de vacature bevestigt 38 uur, geen dagelijkse begin/eindtijd. Wachtdienst kan de werkbelasting wijzigen.

| Tijd | Wat en waarom | Tools/systemen | Met wie / kennis |
|---|---|---|---|
| 08:30–09:00 | Overdracht, open tickets en EDI-afwijkingen; bepaal of verwerking achterloopt | Ticketing onbekend, monitoring/logs, e-mail | Service Desk; impact/urgentie en ketenbegrip |
| 09:00–10:00 | Onderzoek ontbrekende status voor een groep voertuigen; afbakenen op tijd/locatie/partner | Read-only SQL, berichtmetadata, applicatielogs | Operations en integratiepartner; correlatie en reconciliatie |
| 10:00–10:30 | Leveranciersoverleg: ontbrekende testgevallen en releaseafhankelijkheid bespreken | CRQ, issue-/actielijst | Ontwikkelaar/partner; specificeren en acceptance |
| 10:30–11:30 | Behoeftenanalyse voor correctieformulier; huidige stappen observeren | Procesdiagram, notities, Office | Businessunit/projectcoördinator; doorvragen naar doel |
| 11:30–12:00 | Werkpakket bijwerken: rollen, validatie, audit, uitzonderingen | Technisch lastenboek, componentcatalogus | Supervisor waar besluit nodig is; scope/risico |
| 12:00–12:45 | Pauze; bereikbaarheid volgens echte teamafspraken | Geen veronderstelde verplichting | Rooster verifiëren |
| 12:45–14:15 | Kleine portal/toolwijziging bouwen of partnercode reviewen | APEX indien bevestigd, versiebeheer indien aanwezig, SQL/testdata | Team; validatie, rechten, foutpaden |
| 14:15–15:00 | Integratietest: duplicaat, verkeerde volgorde, timeout; bewijs vastleggen | Testomgeving, berichtenfixtures, resultaatlog | Partner/business tester; expected versus actual |
| 15:00–15:45 | Releaseplan en rollback-check met server-/DB-eigenaren | Versiematrix, checklist, recoverybewijs | Service Desk/infra/DBA indien aanwezig; afhankelijkheden |
| 15:45–16:15 | Gebruikersdemo met concrete taak en uitzondering | Werkinstructie, oefencase | Key user; begrijpelijke taal en adoptie |
| 16:15–17:00 | Tickets afronden, risico’s melden, volgende dag plannen | Rapportage, runbook, e-mail | Supervisor/business; resultaat, besluit en volgende update |

## Een typische week

Maandag: backlog triage, impactanalyse en weekplanning. Dinsdag: analyse/bouwblok en leveranciersafstemming. Woensdag: tests en businessacceptatie, eventueel sitebezoek. Donderdag: gecontroleerde release als operationeel venster dat toelaat. Vrijdag: nazorg, KPI’s, budget/capaciteit en weekrapport. Werkelijke releasevensters zijn onbekend; een incident kan de planning verschuiven.

| Activiteit — exclusieve categorieën | Schatting |
|---|---:|
| Analyse en technische specificaties | 15% |
| Development en koppelingstools | 15% |
| Incidenten/troubleshooting | 15% |
| Reguliere support en applicatiebeheer | 10% |
| Testen en acceptatie | 10% |
| Releases/deployment/nazorg | 8% |
| Projectplanning en portefeuille | 8% |
| Businesscontact en opleiding | 6% |
| Leveranciers en teammeetings | 6% |
| Documentatie en rapportage | 5% |
| Gericht leren | 2% |
| Totaal | 100% |

Meetings zijn al verdeeld over business, leveranciers en projectwerk. Tel ze niet opnieuw op. Een TOS-cutoverweek kan veel meer testen en deployment bevatten; een incidentweek veel meer support. Houd tijd bij en gebruik echte cijfers voor capaciteitsgesprekken.

<a id="04"></a>

# DEEL 04 — Verantwoordelijkheden

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

## Technische projectplanning — R06/R10/R12

**Betekenis en belang:** Jij organiseert technische uitvoering en afhankelijkheden. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Maak probleem, scope en acceptatie concreet voordat je uren plant. Splits in werkpakketten met eigenaar, afhankelijkheid, reviewmoment en opleverbewijs.

**Juniorfout:** Alleen deadlines plannen, zonder afhankelijkheden of businessacceptatie.

**Sterke medewerker:** Gebruikt risicotoleranties en alternatieven; toont gevolgen van scopewijziging.

**Tools:** CRQ, lastenboek, planning, risicolog; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Laat een eigen werkpakket met requirements, testplan en forecast zien.

## Behoeftenanalyse — R11

**Betekenis en belang:** Vraag door naar probleem en gebruikersdoel. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Observeer de echte taak; vraag om drie voorbeelden, een uitzondering en het gevolg van niets doen. Scheid gewenste UI van onderliggende behoefte.

**Juniorfout:** Een voorgesteld scherm verwarren met het probleem.

**Sterke medewerker:** Valideert proces én uitkomsten bij de gebruiker voordat een leverancier bouwt.

**Tools:** Proceskaart, stakeholderlijst, acceptatiecriteria; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Vertel hoe een vraag veranderde na doorvragen en welk resultaat dat gaf.

## Leveranciers en outsourcing — R07/R15

**Betekenis en belang:** Uitbesteden verwijdert je verantwoordelijkheid voor resultaat niet. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Spreek deliverables, toegang, acceptatie, support en documentatie af. Volg acties met eigenaar/datum en bewijs; bespreek afwijking vroeg.

**Juniorfout:** Een technische toezegging accepteren zonder demonstratie of test.

**Sterke medewerker:** Houdt eigen ketenkennis; laat overdracht en beheerbaarheid meeleveren.

**Tools:** Actielog, contractafspraken, opleverchecklist; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Toon een escalatiemail en een acceptatiematrix zonder vertrouwelijke details.

## Capaciteit en budget — R16/R23/R24

**Betekenis en belang:** Bewaken of inspanning en resultaat nog kloppen. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Vergelijk begroting, werkelijk verbruik, resterend werk en beschikbare mensen. Rapporteer forecast, afhankelijkheden en opties; vraag besluit bij overschrijding.

**Juniorfout:** Urenverbruik rapporteren zonder resterende scope.

**Sterke medewerker:** Meldt trend voordat budget op is; herprioriteert met businesswaarde.

**Tools:** Excel, projectportefeuille, forecast; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Gebruik een voorbeeld waarin je scope, tijd of kwaliteit expliciet afwoog.

## Applicatiemodellering en core-beheer — R08/R17/R19/R35

**Betekenis en belang:** Continuïteit van huidige applicaties naast verandering. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Leg component, omgeving, eigenaar, versie, input/output en herstelafhankelijkheden vast. Loop één transactie door en onderhoud die kaart bij changes.

**Juniorfout:** Een schema met blokjes maken zonder eigenaar of foutpad.

**Sterke medewerker:** Kan tijdens incidenten exact aanwijzen welke ketengrens nog gezond is.

**Tools:** Componentcatalogus, logs, read-only SQL; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Leg een eigen architectuurdiagram uit inclusief onbekende aannames.

## EDI en rapportering — R20

**Betekenis en belang:** EDI is gestructureerde gegevensuitwisseling tussen organisaties. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Bewaar bericht-ID, partner, ontvangsttijd, mappingversie en businessresultaat. Reconcile aantallen en unieke sleutels; onderscheid technisch ACK van businessverwerking.

**Juniorfout:** Een ontvangen bestand als succesvolle verwerking tellen.

**Sterke medewerker:** Test duplicaten, order en retries; controleert betekenis van rapportcijfers.

**Tools:** iWay/WebFOCUS indien juiste productvariant, berichtarchief; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Demonstreer replay zonder dubbel effect en verklaar een cijferafwijking.

## Portalen en nieuwe tools — R21/R22/R31

**Betekenis en belang:** Gebruikersinterfaces met lifecycle en toegangsbeheer. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Ontwikkel klein en afgebakend; valideer input server-side, controleer rechten en log wie wat wijzigde. Test happy path en uitzonderingen.

**Juniorfout:** Een knop verbergen als enige toegangscontrole.

**Sterke medewerker:** Bouwt taakgericht met audit, onderhoudsplan en testdata.

**Tools:** APEX indien bevestigd, SQL, ontwikkelomgeving; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Toon formulier, negatieve autorisatietest en duidelijke README.

## Releasecoördinatie — R18/R13

**Betekenis en belang:** Delivery controleren tot het werkend in gebruik is. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Koppel versies, databasechanges en partnerconfiguratie. Leg window, go/no-go, rollout, recovery en nazorg vast. Verifieer een echte businesshandeling na livegang.

**Juniorfout:** Rollback gelijkstellen aan enkel een oude applicatie terugzetten.

**Sterke medewerker:** Onderzoekt data-/schema-compatibiliteit en herstelvenster vóór go-live.

**Tools:** Releaseplan, artefactenregister, checklist; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Laat een gerepeteerde deployment met testbewijs en recoverybeperking zien.

## Tweede lijn en wachtdienst — R03/R25

**Betekenis en belang:** Regulier dagwerk met beschikbaarheidsverplichtingen; rooster onbekend. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Neem ticket met impact, tijd en repro over. Vorm hypotheses, verzamel bewijs, voer alleen toegestane changes uit en sluit met gebruikersvalidatie.

**Juniorfout:** Blind restarten; parallel meerdere changes maken; stil blijven.

**Sterke medewerker:** Beperkt risico, verdeelt taken en communiceert vaste updates.

**Tools:** Ticketing, logs, runbooks, SQL, escalatielijst; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Werk hardop een incident uit en onderscheid herstel van root cause.

## Rapportage en communicatie — R26/R32/R33/R34

**Betekenis en belang:** Vertaal techniek naar voortgang en impact. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Schrijf wat opgeleverd is, wat risico loopt, welke keuze nodig is, wie eigenaar is en wanneer de volgende update komt. Pas detail aan doelgroep aan.

**Juniorfout:** Een logdump sturen of een onzekere ETA als belofte presenteren.

**Sterke medewerker:** Zegt wat bekend/onbekend is en vertaalt risico naar operationele gevolgen.

**Tools:** Office, statusformat, overleg; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Geef hetzelfde incidentbericht voor business en leverancier.

## Opleiden en samenwerken — R14/R27

**Betekenis en belang:** Adoptie is deel van technisch succes. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Laat gebruiker/nieuwe collega zelf een taak uitvoeren, met uitzondering en recovery. Documenteer de stappen en controleer begrip.

**Juniorfout:** Een demo geven zonder de deelnemer zelf te laten oefenen.

**Sterke medewerker:** Maakt overdracht zelfstandig bruikbaar en laat feedback verbeteren.

**Tools:** Quick guide, sandbox, buddyplan; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Toon een werkinstructie en vertel hoe je begrip controleerde.

## Kwaliteit, veiligheid, milieu en integriteit — R04/R09

**Betekenis en belang:** Eerlijk rapporteren, zorgvuldig afwerken en nuttig verbeteren. Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.

**Goed uitvoeren:** Bespreek of foutieve data onveilige fysieke acties of verkeerde rapportage kan veroorzaken. Gebruik traceerbare goedkeuringen en meld onzekerheid eerlijk.

**Juniorfout:** Een workaround laten leiden tot verlies van fysieke traceerbaarheid.

**Sterke medewerker:** Betrekt operationele verantwoordelijke en borgt latere reconciliatie.

**Tools:** Risicomatrix, auditlog, changeprocedure; concrete interne tooling verifiëren.

**Sollicitatiebewijs:** Vertel hoe je onder druk een risicovolle shortcut begrensde.

<a id="05"></a>

# DEEL 05 — Technische architectuur

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

## Bevestigde componenten, onzekere verbindingen

**Expliciet uit vacature:** TOS-gerelateerde applicaties, IBM P-series, AIX, Oracle, JBoss, WebFOCUS, iWay, webportalen en Apex. **Waarschijnlijk / afgeleid:** onderstaande topology, relaties, protocolkeuzes, hosting en aparte omgevingen. De componentlijst bewijst niet dat alles op dezelfde server draait.

```text
Terminalgebruikers / business / klanten
       | (interfaces en auth onbekend)
       v
Webportalen of andere clients
       | (HTTP(S) als oefenmodel)
       v
TOS-gerelateerde applicatie / JBoss-runtime
       | databaseverbinding (configuratie onbekend)
       v
Oracle: operationele data, transacties, mogelijk businesslogica
       ^                         ^
       |                         |
iWay: validatie/mapping       WebFOCUS: rapportering
       ^                         |
       | EDI, transport onbekend v
Externe partners             Gebruikersrapporten

Platform: IBM P-series / AIX voor genoemde TOS-componenten.
Verdeling Oracle, JBoss, middleware over hosts is onbekend.

Alternatieve / aanvullende portalroute, ALLEEN indien Apex = Oracle APEX:
Browser → weblaag / ORDS → Oracle APEX-engine en PL/SQL → Oracle-data
APEX is geen gewone JBoss-frontend. ORDS is niet vermeld bij ICO.
```

## Componenten en diagnostische grenzen

Frontend toont informatie en verzamelt acties; gedrag bij clientfout verschilt van serverfout. Backend voert validatie en businessregels uit. JBoss is een application server: een runtime die applicaties, verbindingen en gedeelde services beheert. Oracle bewaart relationele data en kan PL/SQL-logica uitvoeren. AIX is het OS; IBM P-series de genoemde hardwarefamilie. iWay is de integratiecategorie; precieze variant navragen. WebFOCUS rapporteert; exacte datatoegang en planning onbekend.

| Laag | Wat je moet begrijpen | Niet bevestigd bij ICO |
|---|---|---|
| API/integraties | Contract, mapping, validatie, correlatie, ACK, retries | REST/SOAP, EDIFACT, XML, SFTP of AS2 |
| Messaging | Backlog, volgorde, duplicaten, veilige replay | Queueproduct, broker, dead-letter queue |
| Authenticatie | Wie ben je? Autorisatie: wat mag je? | SSO, AD, LDAP, OAuth/OIDC en identityprovider |
| Networking | DNS, TCP, TLS, routes, timeouts | Firewalls, subnetten, proxy en poorten |
| OS/platform | Processen, disk, geheugen, capaciteit en rechten | AIX-versie, LPARs, HMC, HA-opzet |
| Cloud | Alleen relevant als de echte omgeving dit gebruikt | Azure/AWS/GCP; geen cloud genoemd |
| Deployment | Artefact, configuratie, schema, compatible versions | CI/CD-platform, Git-tool, containergebruik |
| Monitoring/logging | Symptoom, timestamp, correlatie, backlog en transacties | Product, retentie, alertregels en dashboards |
| Security | Least privilege, geheimenbeheer, audit en patchbeheer | Concrete normen of certificering |
| Leveranciers | Interfaces, toegang, versiebeheer en supportafspraken | Namen, contracten en interne RACI |

## Volg een oefentransactie

Een partner meldt fictief VIN DEMO0000000000001 als aangekomen. Transport kan slagen terwijl parsing faalt. Parsing kan slagen terwijl mapping de verkeerde locatie kiest. De databasecommit kan slagen terwijl een ACK faalt en de partner opnieuw zendt. Het rapport kan de commit pas later tonen door refresh of filtering. Vraag dus per grens: input, tijd, eigenaar, versie, output, fout en businessresultaat. Die methode is belangrijker dan een perfect getekend schema.

## Architectuurvragen voor onboarding

- Welke systemen zijn bron van waarheid voor voertuig, locatie, status en partnerreferentie?
- Welke veranderingen zijn lokaal en welke raken beide vestigingen?
- Waar bevinden monitoring, berichtarchief, configuratie, back-ups en testdata zich?
- Welke componenten blijven bestaan na de nieuwe TOS-implementatie?
- Wie mag applicatie, database en platform aanpassen en wie autoriseert herstel?

<a id="06"></a>

# DEEL 06 — Technologiehandboek

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

## Gebruik dit handboek met 80/20-focus

Begin bij TOS/data/SQL, ketendiagnose en delivery. Productversies ontbreken: leer concepten en oefen alleen in een sandbox. Leertijden zijn bandbreedten bij IT-basiskennis, geen garantie van professionele beheersing. Oracle APEX-docs zijn geverifieerd via Context7; een toevallig opgehaald verwijderingscommando is bewust niet opgenomen omdat het irrelevant en destructief is.


## Terminal Operating System (TOS)

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; links in researchdossier.

1. **Wat is het?** Software die terminalprocessen en operationele gegevens ondersteunt. Exact ICO-product en modules onbekend.
2. **Gebruik:** Registratie, status, planning en uitvoering van terminalhandelingen; concrete processen door key users laten tonen.
3. **Waarom:** Een gedeeld operationeel beeld vermindert inconsistentie tussen fysieke goederen en informatie.
4. **Architectuurplek:** Centraal applicatiedomein; de vacature koppelt TOS-componenten aan AIX/IBM P-series/Oracle/JBoss.
5. **Conceptueel:** Businesshandelingen volgen regels en veranderen toestand. Integraties en rapporten lezen/verwerken die toestand. Modelleer state transitions en bron van waarheid.
6. **Wat moet je kunnen:** Eén transactie end-to-end volgen, gebruikersfout versus systeemfout onderscheiden, wijzigingsimpact op beide vestigingen beoordelen en migratietests voorbereiden. Doelniveau: **Begrijpen → zelfstandig ketenanalyse**.
7. **Niet vooraf nodig:** Het onbekende product vooraf volledig kennen of ieder logistiek proces zelf beheren.
8. **Typische problemen:** Onjuiste status, ontbrekende opdracht, inconsistentie na timeout, vastgelopen integratie en foutieve locatie.
9. **Troubleshooting:** Vergelijk fysieke verwachting, bronrecord, audit, businessregels en partnerstatus op dezelfde sleutel/tijd. Laat operatie bepalen wat echt gebeurd is.
10. **Termen:** state, transition, source of truth, cutover, reconciliation, exception, master data
11. **Interviewvraag:** Hoe onderzoek je een voertuig dat fysiek aanwezig is maar niet zichtbaar in het TOS?
12. **Voorbeeldantwoord:** Ik begrens op voertuig, locatie en tijd. Ik controleer ontvangst en het eerste foutieve ketenpunt, vergelijk registratie met bron van waarheid en laat operations de fysieke toestand bevestigen. Herstel gebeurt traceerbaar en met downstreamcontrole. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Modelleer vijf fictieve voertuigen en geldige statusovergangen. Test vertrek zonder aankomst, dubbele aankomst en locatiecorrectie. Lever state diagram en foutmatrix op.
14. **Werksituatie:** Een partner meldt aankomst opnieuw omdat het ACK ontbreekt: controleer eerst of de businesscommit al bestaat voordat je replay toestaat.
15. **Leertijd:** 12–20 uur concept/proceslab; enkele weken lokale proceskennis met buddy. Productexpertise maanden, geen startvereiste.


## IBM P-series / IBM Power

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1/T1; links in researchdossier.

1. **Wat is het?** Genoemde IBM-serverfamilie voor enterprise workloads; huidige Power-benaming en precieze hardware bij ICO verifiëren.
2. **Gebruik:** Platform waarop AIX-gerelateerde TOS-componenten volgens vacature draaien.
3. **Waarom:** Enterpriseplatformen bieden beheermogelijkheden en capaciteit voor langdurige workloads; ICO-keuzehistorie onbekend.
4. **Architectuurplek:** Onder OS/applicatielaag. Virtualisatie/LPAR en beheertools kunnen relevant zijn, maar zijn niet genoemd.
5. **Conceptueel:** Hardware levert CPU, geheugen en I/O. Partities, indien aanwezig, verdelen resources; applicatieproblemen kunnen door capaciteit of opslag worden versterkt.
6. **Wat moet je kunnen:** Platform versus OS versus applicatie onderscheiden en een gericht resourceprobleem aan platformbeheer melden. Doelniveau: **Begrijpen; beheer met hulp**.
7. **Niet vooraf nodig:** Zelf firmware, SAN, HMC of fysieke hardware wijzigen zonder toegewezen rol en opleiding.
8. **Typische problemen:** Resource contention, I/O-latentie, capaciteitsgrens of hardwarealarm; geen vastgestelde ICO-problemen.
9. **Troubleshooting:** Correlatie tussen tijd van applicatievertraging en platformmetrics; vraag eigenaar om partitie-/storagegegevens. Controleer of andere workloads meevertragen.
10. **Termen:** Power, partition/LPAR, CPU entitlement, I/O, capacity, HMC (alleen bij relevante setup)
11. **Interviewvraag:** Moet je de hardware kunnen beheren om applicaties te ondersteunen?
12. **Voorbeeldantwoord:** Ik moet de afhankelijkheid en resource-indicatoren begrijpen. Diep platformbeheer vraagt expliciet eigenaarschap. Ik lever tijd, impact en metingen zodat de beheerder gericht kan onderzoeken. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak een laagdiagram hardware → OS → runtime → database/app. Benoem voor drie symptomen de mogelijke eigenaar en ontbrekende meting.
14. **Werksituatie:** TOS reageert traag bij een batch: sluit query- of poolproblemen niet uit omdat de server-CPU hoog is.
15. **Leertijd:** 3–6 uur voor rolbegrip; productbeheer afzonderlijke opleiding.


## AIX

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1/T1; links in researchdossier.

1. **Wat is het?** IBM Unix-besturingssysteem. Het is geen Linux-distributie; shellconcepten overlappen, specifieke beheertools verschillen.
2. **Gebruik:** Processen, filesystems, gebruikers, netwerk en resources voor de genoemde TOS-componenten.
3. **Waarom:** Stabiele enterprise-OS-functies voor de genoemde omgeving; de reden voor de oorspronkelijke keuze is onbekend.
4. **Architectuurplek:** Tussen IBM-platform en applicatie/runtime/database; verdeling hosts onbekend.
5. **Conceptueel:** Processen draaien met rechten en verbruiken geheugen/CPU/I/O. Filesystems kunnen vollopen. Services hebben eigen start- en beheerprocedures.
6. **Wat moet je kunnen:** Logpaden vinden, process/resourcebegrip toepassen en disk/rechten als oorzaak herkennen; gebruik toegestane read-only controles en lokale runbooks. Doelniveau: **Begrijpen → gebruiken met hulp**.
7. **Niet vooraf nodig:** Kernel tuning, filesystems resizing, systeempatching en rootbeheer vóór indiensttreding.
8. **Typische problemen:** Vol filesystem, verkeerde bestandsrechten, proces niet actief, te weinig resources, klokverschil.
9. **Troubleshooting:** Scopeer fout/tijd; controleer via bevoegde beheerder filesystem en processtatus; vergelijk service- en OS-log. Linuxcommando-output is geen AIX-bewijs.
10. **Termen:** filesystem, process, permission, UID, mount, service, paging, environment
11. **Interviewvraag:** Een verwerking faalt met een schrijffout: wat controleer je?
12. **Voorbeeldantwoord:** Ik controleer doelpad, rechten, beschikbare ruimte en of de applicatie de verwachte gebruiker gebruikt. Ik laat de eigenaar retentie en veilig ruimteherstel bepalen; ik verwijder geen logs of bestanden blind. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak in een Linux-testdirectory een permission denied en herstel alleen de labrechten. Leg op papier uit welke AIX-check nog door officiële versie/runbook bevestigd moet worden.
14. **Werksituatie:** EDI-output kan niet geschreven worden; procesrestart lost volle opslag niet op en kan bewijs verloren doen gaan.
15. **Leertijd:** 8–16 uur Unixbasis/laagdiagnose, daarna 2–4 weken AIX-begeleiding voor lokale taken.


## Oracle Database / SQL / PL/SQL

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; algemene databaseconcepten; links in researchdossier.

1. **Wat is het?** Relationele database met SQL voor data en PL/SQL voor procedurele logica. Versie/licenties en DBA-eigenaarschap onbekend.
2. **Gebruik:** Operationele records, constraints, transacties, mogelijk businesslogica en rapportdata.
3. **Waarom:** Consistente gedeelde opslag met transactie- en integriteitsregels.
4. **Architectuurplek:** Onder applicatielogica en mogelijk rechtstreeks onder APEX; integraties/rapporten kunnen via andere lagen benaderen.
5. **Conceptueel:** Queries lezen tabellen; keys/constraints bewaken relaties. Een transactie bundelt wijzigingen met commit/rollback. Locks voorkomen conflicten maar kunnen wachten veroorzaken.
6. **Wat moet je kunnen:** SELECT/join/filter/group begrijpen, null en datumcorrectheid bewaken, duplicaten detecteren en veilige read-only reconciliatie uitvoeren. Een klein PL/SQL-blok begrijpen indien de codebase dat gebruikt. Doelniveau: **Zelfstandig read-only; wijzigingen met review**.
7. **Niet vooraf nodig:** Production DBA, RAC/Data Guard/backupbeheer of optimizerexpert zijn tenzij expliciet toegewezen.
8. **Typische problemen:** Lockwait, traag plan, connectionpool-uitputting, constraint violation, verkeerde join, stale rapport of timezonefout.
9. **Troubleshooting:** Vraag query/schema/parameters en timing; beperk scope, vergelijk actual/expected rows, laat DBA locks/plan beoordelen. Meet voor/na; voeg niet blind indexes toe.
10. **Termen:** primary/foreign key, constraint, index, transaction, commit, rollback, lock, execution plan, bind variable
11. **Interviewvraag:** Waarom kan een succesvolle update toch een foutmelding opleveren?
12. **Voorbeeldantwoord:** De databasecommit kan geslaagd zijn terwijl het antwoord of ACK faalt. Daarom zoek ik eerst op businesssleutel en request-ID. Een onbeschermde retry kan dubbel verwerken. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak synthetische vehicles/locations/edi_messages. Schrijf een query voor voertuigen zonder locatie en één voor dubbele businessreferenties. Test met nulls en duplicaten. Gebruik parameters.
14. **Werksituatie:** Een rapport telt 120 voertuigen waar brondata 100 heeft: een one-to-many join kan rijen vermenigvuldigen; verklaar de relatie voor je DISTINCT toevoegt.
15. **Leertijd:** 20–35 uur SQLbasis plus 8–15 uur transacties/reconciliatie; DBA-expertise is apart.


## JBoss / Java application server

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1/T2; links in researchdossier.

1. **Wat is het?** Application server in de Java-ecosysteemfamilie. JBoss EAP en WildFly zijn verwante producten; ICO-variant/versie niet vastgesteld.
2. **Gebruik:** Host applicaties en configureert gedeelde services zoals datasources, transacties en logging.
3. **Waarom:** Enterpriseapplicaties hebben een runtime en centrale resourceconfig nodig.
4. **Architectuurplek:** Tussen clients/portalen en database/businesscomponenten. Niet gelijkstellen aan de TOS zelf.
5. **Conceptueel:** Requests gebruiken threads en databaseverbindingen uit pools. Exceptions laten zien waar uitvoering faalt; configuratie/dependency-versies bepalen werking.
6. **Wat moet je kunnen:** Deploymentstatus en relevante logs lezen, datasource/pool/JVM/exceptionbegrip toepassen en configvergelijking met eigenaar uitvoeren. Doelniveau: **Begrijpen → diagnostisch gebruiken**.
7. **Niet vooraf nodig:** De hele Java/Jakarta EE-specificatie of clusterarchitectuur beheersen; geen onbewezen EAP-consolecommando’s kopiëren.
8. **Typische problemen:** Deployment failure, databaseconnectiefout, pool leeg, geheugen-/threadprobleem, incompatibele library of verkeerd configprofiel.
9. **Troubleshooting:** Correlatie-ID en exceptionketen; onderscheid eerste fout van vervolgschade. Controleer recente artefact/configchange, databasebereikbaarheid en resource-indicatoren. Restart alleen volgens plan.
10. **Termen:** JVM, datasource, connection pool, thread, WAR/EAR, exception, subsystem, standalone/domain (variantafhankelijk)
11. **Interviewvraag:** De health endpoint werkt maar transacties timen uit. Hoe kan dat?
12. **Voorbeeldantwoord:** Een simpele healthcheck hoeft geen databaseactie te testen. Ik vergelijk echte transacties, poolwachttijd en DB-latentie. Een healthy proces bewijst geen healthy businessdienst. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Lees een voorbeeldlog met connection timeout, identificeer de eerste fout en maak een evidence pack met vijf vragen aan runtime/DB-eigenaar.
14. **Werksituatie:** Na apprelease gebruikt de datasource de verkeerde testconfig; het artefact start maar de business-smoke test faalt.
15. **Leertijd:** 10–20 uur runtime/diagnoseconcepten; 1–3 dagen begeleide productlab indien beschikbaar.


## EDI

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; protocolvariant onbekend; links in researchdossier.

1. **Wat is het?** Electronic Data Interchange: gestructureerde businessdata tussen organisaties. Een bepaalde standaard of transportvorm is niet bevestigd.
2. **Gebruik:** Partnerberichten ontvangen, valideren, mappen, verwerken en bevestigen.
3. **Waarom:** Vermindert handmatige herinvoer en ondersteunt voorspelbare keteninformatie.
4. **Architectuurplek:** Externe partnergrens via middleware naar applicatie/data, met retourstatus of ACK.
5. **Conceptueel:** Transport → syntax → semantiek/mapping → businessregels → commit → ACK. Iedere stap kan slagen/falen onafhankelijk van de rest.
6. **Wat moet je kunnen:** Contracten en samples lezen, bericht-ID/businesssleutel volgen, duplicaten/order/ACK/replay verklaren en reconciliëren. Doelniveau: **Zelfstandig flowanalyse; productbeheer leren**.
7. **Niet vooraf nodig:** Alle EDIFACT-segmenten of AS2-beheer leren voordat de werkelijke standaard bekend is.
8. **Typische problemen:** Fout datumformaat, onbekende locatie, duplicaat, ontbrekend ACK, verkeerde volgorde, encoding of partnercontractwijziging.
9. **Troubleshooting:** Volg één ID van transport tot commit; vergelijk mappingversie en sample met afgesproken contract. Test replay in sandbox; bepaal partial commits voordat bulk-replay mag.
10. **Termen:** schema, mapping, ACK/NACK, correlation ID, idempotency, replay, retry, ordering, dead letter (concept)
11. **Interviewvraag:** Wat is het verschil tussen een technisch ACK en een businessbevestiging?
12. **Voorbeeldantwoord:** Technisch ACK kan alleen ontvangst/syntax bevestigen. Businessbevestiging zegt of de bedoelde verwerking geaccepteerd is. Ik lees het contract; ik neem niet aan dat een ontvangen bestand gelijk is aan een verwerkt voertuig. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Verwerk tien JSON-oefenberichten met twee duplicaten en één onbekende locatie. Lever per ID ontvangst, validatie, verwerking en resultaat op. JSON is een demoformaat, niet bewezen ICO-EDI.
14. **Werksituatie:** Partner stuurt dezelfde aankomst opnieuw na timeout; unieke businesssleutel plus gecontroleerde transactiestatus voorkomt dubbel effect.
15. **Leertijd:** 12–24 uur concepten/lab, daarna daadwerkelijke partnerformaten tijdens onboarding.


## iWay / middleware

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; productvariant verifiëren; links in researchdossier.

1. **Wat is het?** iWay verwijst naar integratiesoftware voor verbinding, transformatie en orchestration. Variant en version zijn onbekend.
2. **Gebruik:** Koppeling van componenten en EDI-verwerking, zoals genoemd in vacature.
3. **Waarom:** Centrale adapter/mappinglogica vermindert koppellogica in losse applicaties.
4. **Architectuurplek:** Tussen partnertransport en businessapplicatie/database; werkelijke topology onbekend.
5. **Conceptueel:** Een flow heeft input, parse/transform, route, uitvoer en foutafhandeling. Configuratie en mappingversie zijn deel van de release.
6. **Wat moet je kunnen:** Een bestaande flow lezen, foutgrens bepalen, configuratie/retries volgen en wijziging met partner testen. Doelniveau: **Gebruiken met hulp → zelfstandig bestaande flows**.
7. **Niet vooraf nodig:** Productplugin ontwikkelen of alle adapters/administratie leren vóór de eerste werkweek.
8. **Typische problemen:** Adapterverbinding, mapping exception, backlog, verkeerd endpoint, onveilige retry en credential/certificaatverval.
9. **Troubleshooting:** Input/output en flowlog op ID, configversie en endpoint vergelijken; check backlogleeftijd naast aantallen; afstemmen met externe partner.
10. **Termen:** adapter, listener, channel, process flow, transform, route, error handling (benamingen versieafhankelijk)
11. **Interviewvraag:** Hoe vind je een fout in een integratieflow?
12. **Voorbeeldantwoord:** Ik markeer de laatste bewezen goede output en eerste verkeerde input. Ik vergelijk één sample en versie en controleer downstreamcommit vóór retry. Daarna reproduceer ik de mappingfout met synthetische data. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Teken een integratieflow en definieer per stap minimaal logveld, foutpad en eigenaar. Implementeer de concepten in portfolio als productlicentie ontbreekt.
14. **Werksituatie:** Nieuwe locatiecode veroorzaakt mappingfouten voor één partner; de andere stromen blijven werken, dus scopeer de mappingvariant.
15. **Leertijd:** 8–16 uur concepten; 2–5 begeleide productlabdagen voor lokale flows.


## WebFOCUS / BI en rapportering

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; exacte productdocs nog verifiëren; links in researchdossier.

1. **Wat is het?** Business-intelligence-/rapportageproductfamilie; precieze deployment en versie niet vastgesteld.
2. **Gebruik:** Rapportering genoemd bij EDI/TOS-portefeuille; exacte rapporten en databronnen onbekend.
3. **Waarom:** Businessgebruikers hebben betrouwbare cijfers en gecontroleerde definities nodig.
4. **Architectuurplek:** Rapportlaag boven databronnen/adapters; directe Oracleverbinding of tussenlaag niet bewezen.
5. **Conceptueel:** Bronselectie, filters, joins, aggregaties, toegangsregels en refresh bepalen wat het rapport toont.
6. **Wat moet je kunnen:** Rapportcijfers terugleiden tot bronrecords en definitie, parameters/refresh/rechten controleren en wijzigingen valideren. Doelniveau: **Begrijpen → gebruiken; beheer met begeleiding**.
7. **Niet vooraf nodig:** Alle rapportsyntax/dashboardfeatures vooraf beheersen of zelf datawarehousearchitect zijn.
8. **Typische problemen:** Verkeerde telling, refreshachterstand, datumfilter, one-to-many join, verborgen rolfilter en exportverschil.
9. **Troubleshooting:** Vergelijk gelijke sleutelset, tijdzone en snapshot. Controleer datasource, filter, rechten en laatste refresh. Gebruik één afwijkend record als bewijs.
10. **Termen:** measure, dimension, filter, aggregation, report parameter, refresh, drill-down, row-level security (concept)
11. **Interviewvraag:** Twee rapporten tonen verschillende aantallen. Welke vraag stel je eerst?
12. **Voorbeeldantwoord:** Tellen ze hetzelfde businessobject onder dezelfde definitie, tijd en scope? Pas daarna onderzoek ik join, filter en refresh. Ik maak een verschilset met sleutels in plaats van cijfers passend te maken. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak twee synthetische rapportqueries met verschillende inclusie van inactieve locaties. Documenteer definitie, refresh en reconciliatie.
14. **Werksituatie:** Weekrapport telt status op verwerkingstijd waar operations op eventtijd telt; beide queries kunnen technisch correct zijn maar andere vragen beantwoorden.
15. **Leertijd:** 8–16 uur rapportanalyse; echte syntax/catalogus on the job.


## Apex — waarschijnlijk Oracle APEX

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1/T3; interpretatie verifiëren; links in researchdossier.

1. **Wat is het?** Oracle Application Express is databasegerichte low-code webontwikkeling. “Apex” kan theoretisch iets anders zijn; in Oracle-context waarschijnlijk APEX.
2. **Gebruik:** Formulieren, rapporten en taakgerichte webportalen op relationele data.
3. **Waarom:** Snel gecontroleerde applicaties maken met bestaande database en businessregels.
4. **Architectuurplek:** Browser → weblaag/ORDS → APEX-engine in Oracle. ORDS is een productarchitectuurreferentie, niet als ICO-component genoemd.
5. **Conceptueel:** Pagina’s bevatten regions, items, validations en processes; engine bewaakt sessie, page flow, auth en authorisatie. Een browsersessie is niet permanent dezelfde databasesessie.
6. **Wat moet je kunnen:** Rapport en formulier maken, servervalidatie/rechten begrijpen, foutpaden testen en export/versieoverdracht documenteren. Doelniveau: **Gebruiken → kleine functie zelfstandig met review**.
7. **Niet vooraf nodig:** Iedere plugin of JavaScript-API kennen, platforminstallatie of SYSDBA-beheer doen.
8. **Typische problemen:** Verkeerde session state, autorisatielek, onjuiste processvolgorde, constraintfout en niet-geparameteriseerde query.
9. **Troubleshooting:** In test page/process en debuglog volgen; itemwaarden/session state/rollen en DB-resultaat vergelijken. Verberg geheimen en toon niet onnodig interne foutdetails.
10. **Termen:** workspace, application, page, region, item, process, validation, session state, authentication, authorization, ORDS
11. **Interviewvraag:** Waarom is een verborgen knop geen voldoende security?
12. **Voorbeeldantwoord:** Een gebruiker kan een request buiten de UI sturen. Autorisatie hoort op de server en op het relevante object/scope. Ik test een onbevoegde request expliciet en controleer dat data niet wijzigt. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Bouw indien sandbox beschikbaar een voertuiglocatieformulier met reden, autorisatie en validatie. Zonder licentie/sandbox maak een equivalent en label het als conceptbewijs.
14. **Werksituatie:** Een correctieformulier overschrijft stale data; gebruik een gecontroleerde versiecheck en laat gebruiker de actuele toestand herladen.
15. **Leertijd:** 15–30 uur gerichte APEX-praktijk bij SQLbasis; installatiebeheer niet inbegrepen.


## Webportalen / HTTP / API

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1 voor portalen; overige concepten afgeleid; links in researchdossier.

1. **Wat is het?** Een webportaal geeft gebruikers toegang tot applicatiefuncties. HTTP is request/response; API is een afgesproken software-interface.
2. **Gebruik:** Gebruikersacties, rapportinzage en systeemkoppelingen; geen specifieke frontendtaal genoemd.
3. **Waarom:** Maakt businessfuncties toegankelijk met gecontroleerde toegang en feedback.
4. **Architectuurplek:** Client → web/app-laag → businesslogica/data; identity en TLS zijn dwarsdoorsnijdend.
5. **Conceptueel:** Request bevat actie/data/auth; server controleert regels en antwoord. Clienttimeout kan na servercommit vallen; statuscode alleen is onvoldoende businessbewijs.
6. **Wat moet je kunnen:** Repro en browser/netwerkfout onderscheiden, contract/errorcodes begrijpen, rollen/validatie en taakflow testen. Doelniveau: **Begrijpen → gebruiken**.
7. **Niet vooraf nodig:** Een modern framework of microservices invoeren zonder behoefte; vacature vraagt geen React.
8. **Typische problemen:** 401/403, verlopen sessie, 500, TLS-fout, verkeerde scope, timeout en stale cache.
9. **Troubleshooting:** Vergelijk één/gehele gebruikersgroep, requesttijd/ID en serverlog. Test toegang en businessresultaat; onderscheid auth, netwerk en applicatie.
10. **Termen:** request/response, HTTP status, timeout, payload, TLS, session, endpoint, contract
11. **Interviewvraag:** Wat is het verschil tussen 401 en 403?
12. **Voorbeeldantwoord:** Doorgaans ontbreekt of faalt bij 401 authenticatie; bij 403 ontbreekt toestemming. Productgedrag kan verschillen, dus ik controleer serverlog en rolconfig zonder rechten blind te verruimen. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Schrijf contract voor een synthetische locatiecorrectie: input, allowed roles, validatie, conflict, error en audit. Test direct request buiten de UI.
14. **Werksituatie:** Eén klant ziet niets: scopefilter kan correct blokkeren of verkeerde klantmapping bevatten; bewijs nodig vóór aanpassen.
15. **Leertijd:** 8–16 uur web/API-diagnose, aanvullende bouwpraktijk 1–3 dagen.


## Authenticatie / autorisatie / security

**Bronstatus:** Waarschijnlijk / afgeleid uit functiecontext; geen bevestigde ICO-tool. Bronreferentie: Waarschijnlijk / afgeleid; links in researchdossier.

1. **Wat is het?** Authenticatie bewijst identiteit; autorisatie beperkt acties en datascope. Least privilege geeft alleen benodigde toegang.
2. **Gebruik:** Portalen, beheeraccounts, database en partnertransport beschermen.
3. **Waarom:** Voorkomt onbedoelde wijziging, gegevenslek en onbevoegde operationele beslissingen.
4. **Architectuurplek:** Alle lagen; concrete SSO/AD/LDAP/OIDC-keuze onbekend.
5. **Conceptueel:** Identitycontrole, rol/scopebeleid, secretbeheer, transportbeveiliging en audit versterken elkaar. UI-controls vervangen servercontrole niet.
6. **Wat moet je kunnen:** Minimale rechten vragen, secrets uit code/logs houden, role/scope negatieve tests uitvoeren en securityincident gericht escaleren. Doelniveau: **Zelfstandig toepassen; specialist escaleren**.
7. **Niet vooraf nodig:** Cryptografie ontwerpen, pentestexpert zijn of eigen identityprovider bouwen.
8. **Typische problemen:** Te brede rol, hardcoded credential, log met gevoelige data, verlopen certificaat en verkeerde klantfilter.
9. **Troubleshooting:** Bepaal blootstelling/scope zonder data onnodig te kopiëren. Bewaar bewijs volgens procedure; betrek securityowner voor containment en credentialrotatie.
10. **Termen:** least privilege, RBAC, scope, secret, TLS, audit, containment, exposure
11. **Interviewvraag:** Je ontdekt mogelijk klantdata in de verkeerde portal. Wat doe je?
12. **Voorbeeldantwoord:** Ik behandel het als mogelijk securityincident, beperk verdere blootstelling via bevoegde eigenaar, bewaar minimaal bewijs en meld feitelijke scope/ onzekerheid. Ik verwijder geen auditsporen en communiceer extern alleen volgens afspraken. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak een rolmatrix voor reader/operator/admin met twee klant-scopes en test alle verboden combinaties.
14. **Werksituatie:** Een leverancier vraagt permanent adminaccount; bespreek taakgebonden tijdelijke rechten en audit met IT-eigenaar.
15. **Leertijd:** 6–12 uur relevante basis; interne securityprocedure tijdens onboarding.


## Netwerk / DNS / TCP / TLS

**Bronstatus:** Waarschijnlijk / afgeleid uit functiecontext; geen bevestigde ICO-tool. Bronreferentie: Waarschijnlijk / afgeleid; links in researchdossier.

1. **Wat is het?** DNS vertaalt namen, TCP draagt verbindingen en TLS beveiligt transport; poorten/routes bepalen bereikbaarheid.
2. **Gebruik:** Client-server, database en partnerconnectiviteit onderzoeken.
3. **Waarom:** Applicaties hebben betrouwbare en beveiligde netwerkgrenzen nodig.
4. **Architectuurplek:** Onder iedere remote call; topologie/proxy/firewall bij ICO onbekend.
5. **Conceptueel:** Naamresolutie → connectie → TLS-handshake → protocol → applicatieantwoord. Een geslaagde ping bewijst geen applicatieprotocol.
6. **Wat moet je kunnen:** Foutlaag herkennen, timestamp/endpoint geven en gerichte reachability/TLS-check afstemmen. Doelniveau: **Begrijpen → diagnostisch gebruiken**.
7. **Niet vooraf nodig:** Routingprotocollen/SAN/netwerkarchitectuur diep leren of firewall breed openzetten.
8. **Typische problemen:** DNS-verwijzing fout, connect-timeout, certificaat verlopen, trustchain of proxyconfig verkeerd.
9. **Troubleshooting:** Verschil tussen hosts/locaties; check naam, route/poort en certificaat met bevoegde beheerder. Test werkelijk protocol; geen credentials in gedeelde commands.
10. **Termen:** DNS, port, route, firewall, handshake, certificate chain, expiry, proxy, latency
11. **Interviewvraag:** Een endpoint is bereikbaar maar de integratie faalt. Waarom?
12. **Voorbeeldantwoord:** Bereikbaar is een laagbewijs. TLS, credentials, protocolcontract of businessvalidatie kunnen nog falen. Ik volg de eerste foutgrens en vergelijk beide kanten op hetzelfde tijdstip. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Teken vier storingen: DNS, connectie, TLS, applicatie. Geef per fout één onderscheidende veilige controle.
14. **Werksituatie:** Alleen Zeebrugge faalt na routewijziging: vergelijk locatiepad en configuratie, niet direct code aanpassen.
15. **Leertijd:** 6–12 uur appgericht netwerkbegrip.


## Logging / monitoring / messaging

**Bronstatus:** Waarschijnlijk / afgeleid uit functiecontext; geen bevestigde ICO-tool. Bronreferentie: Waarschijnlijk / afgeleid; links in researchdossier.

1. **Wat is het?** Logs tonen gebeurtenissen; metrics tonen trends; alerts vragen actie. Messaging ontkoppelt verzending van verwerking.
2. **Gebruik:** Ketenproblemen vinden en tijdig zien dat backlog of fouten groeien.
3. **Waarom:** Een systeem kan draaien terwijl businessverwerking achterblijft.
4. **Architectuurplek:** Bij app, OS, DB, integratie en rapport; concrete tooling onbekend.
5. **Conceptueel:** Correlatie-ID verbindt stappen, timestamps ordenen gebeurtenissen. Queue age is naast queue length nodig. At-least-once delivery vereist duplicate-safe verwerking.
6. **Wat moet je kunnen:** Geschikte logvelden ontwerpen, backlog/foutpercentage/interactietijd lezen en op businessuitkomst monitoren. Doelniveau: **Zelfstandig ontwerpen op kleine schaal**.
7. **Niet vooraf nodig:** Een observabilityplatform bouwen, exacte brokeradministratie of distributed tracingexpert worden.
8. **Typische problemen:** Geen correlatie, verkeerde tijdzone, alert zonder owner, sensitive logs, consumer stuck en retry-storm.
9. **Troubleshooting:** Vergelijk last successful businessevent, oldest pending en foutgroep. Bewaar IDs, mask persoonsgegevens en stem retentie/alertactie af.
10. **Termen:** correlation ID, metric, alert, backlog, oldest age, consumer, retry, dead letter, retention
11. **Interviewvraag:** Waarom is “aantal fouten nul” geen voldoende monitoring?
12. **Voorbeeldantwoord:** Het proces kan niets verwerken. Ik monitor volume, laatste succesvolle verwerking en achterstand naast foutpercentage. Een stilgevallen consumer geeft mogelijk geen nieuwe error. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak een dashboard met volume/minuut, errors, oldest pending en unieke successful businesskeys. Injecteer stilstand en controleer alert.
14. **Werksituatie:** Een batch start niet: output is leeg en logs tonen geen error. Verwacht volume en schedulerbewijs onthullen het probleem.
15. **Leertijd:** 8–16 uur appgerichte observability-praktijk.


## Deployment / CI/CD / versiebeheer / cloud

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1 releases; CI/CD/cloud afgeleid; links in researchdossier.

1. **Wat is het?** Deployment plaatst een versie; versiebeheer bewaart changes; CI/CD automatiseert checks/uitrol. Cloud is een hostingmodel, niet bevestigd.
2. **Gebruik:** Herhaalbare tests en releases met compatibele config/schema/artefacten.
3. **Waarom:** Reduceert handmatige fouten en geeft herleidbaar releasebewijs.
4. **Architectuurplek:** Deliverylaag over omgevingen; concrete Git/CI/CD en cloudprovider onbekend.
5. **Conceptueel:** Change → review → tests → artefact → acceptatie → goedgekeurde uitrol → businessvalidatie. Secrets/config zijn omgevingsgebonden.
6. **Wat moet je kunnen:** Release manifest, compatibiliteit, pipeline-uitkomst en recoveryplan begrijpen; demo reproductief bouwen. Doelniveau: **Zelfstandig demo; productieworkflow met begeleiding**.
7. **Niet vooraf nodig:** Kubernetes, multi-cloud, enterprise pipelineplatform of containerstrategie vóór bevestiging.
8. **Typische problemen:** Juiste code verkeerde config, schema niet compatibel, test ontbreekt, half deployment en onomkeerbare migratie.
9. **Troubleshooting:** Vergelijk artefactversie, config en schema; laat smoke test echte businessactie doen. Bij datamigratie expliciet beoordelen of restore/forward fix nodig is.
10. **Termen:** artifact, build, pipeline, environment, migration, rollback, forward fix, smoke test, manifest
11. **Interviewvraag:** Is een app-rollback altijd voldoende?
12. **Voorbeeldantwoord:** Nee. Data en schema kunnen gewijzigd zijn. Ik definieer vooraf compatibiliteit en herstelmogelijkheden, inclusief partnerberichten en data die sinds livegang ontstaan zijn. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Bouw een demo met één compatibele schemawijziging en één incompatibele. Documenteer wat veilig terug kan en wat niet.
14. **Werksituatie:** Partneradapter verwacht veld uit nieuwe schema maar app wordt teruggezet; recovery moet alle afhankelijke versies behandelen.
15. **Leertijd:** 10–20 uur release/versiepraktijk; cloud alleen gericht leren indien werkelijk nodig.


## PRINCE2 / projectmanagement / CRQ

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; links in researchdossier.

1. **Wat is het?** PRINCE2 is een projectmanagementmethode; vacature laat alternatieven toe. CRQ is change request; lastenboek beschrijft technische opdracht en werkpakketten.
2. **Gebruik:** Resultaat, fasen, beslissingen, risico’s, budget en leveranciersafspraken organiseren.
3. **Waarom:** Voorkomt onduidelijke scope en onzichtbare afwijkingen.
4. **Architectuurplek:** Besturingslaag rond businessanalyse, techniek en delivery.
5. **Conceptueel:** Businesscase rechtvaardigt werk; fasen maken review mogelijk; tolerantie bepaalt wanneer escalatie nodig is. Werkpakket maakt output en acceptatie concreet.
6. **Wat moet je kunnen:** Kleine businesscase, risico-/actielog, werkpakket, forecast en wijzigingsimpact maken en gebruiken. Doelniveau: **Zelfstandig toepassen, mandaat navragen**.
7. **Niet vooraf nodig:** Certificaat of alle methodeterminologie memoriseren; certificaat niet expliciet vereist.
8. **Typische problemen:** Scope creep, ontbrekende owner, late budgetmelding, leverancier levert zonder acceptatie en onduidelijke beslisrechten.
9. **Troubleshooting:** Vergelijk baseline en resterende scope/capaciteit. Benoem beslissing, alternatieven en consequenties; laat change autoriseren.
10. **Termen:** businesscase, stage, tolerance, work package, risk, issue, CRQ, acceptance, forecast
11. **Interviewvraag:** Een leverancier vraagt 30% extra tijd. Wat rapporteer je?
12. **Voorbeeldantwoord:** Ik vraag bewijs van resterend werk/oorzaak, beoordeel impact en presenteer opties: scope beperken, planning aanpassen of capaciteit wijzigen. Ik maak duidelijk wie beslist en welke tolerantie overschreden is. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Maak CRQ van locatiecorrectie met 6 werkpakketten, risicolog, acceptance en budgetvoorbeeld met expliciete fictieve bedragen.
14. **Werksituatie:** Nieuwe TOS-integratie blijkt afhankelijk van partnerdata die niet geleverd is; escalatie vóór het releasewindow voorkomt verrassingen.
15. **Leertijd:** 8–16 uur toegepaste methode/CRQ; formele certificatie apart.


## MS Office / N-E-F / training

**Bronstatus:** Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid. Bronreferentie: V1; links in researchdossier.

1. **Wat is het?** Office is een productiviteitspakket; N/E/F vermoedelijk Nederlands/Engels/Frans. Vereist taalniveau en gerelateerde producten onbekend.
2. **Gebruik:** Analyse, rapportage, specificaties, leverancierscontact en gebruikersopleiding.
3. **Waarom:** Technische uitvoering vraagt begrijpelijke afspraken en bewijs voor meerdere doelgroepen.
4. **Architectuurplek:** Communicatie-/administratielaag; documenten moeten aansluiten op brondata en changes.
5. **Conceptueel:** Excel helpt reconciliëren/forecasten; documenten leggen scope vast; presentaties begeleiden taken. Schrijf acties met eigenaar en datum; houd dezelfde betekenis over talen heen.
6. **Wat moet je kunnen:** Een betrouwbare verschillenlijst, wekelijkse status en taakgerichte instructie maken; technisch incident praktisch kunnen uitleggen. Doelniveau: **Zelfstandig praktisch gebruiken**.
7. **Niet vooraf nodig:** VBA/complexe dashboards, professionele vertaler of perfecte business-Frans zijn zonder niveau-eis.
8. **Typische problemen:** Foutieve sheetformule, versieverwarring, jargon, vertaalde term met ander betekenis en training zonder oefening.
9. **Troubleshooting:** Controleer formules met kleine handmatige steekproef, versie/eigenaar en definities. Laat ontvanger samenvatten welke actie verwacht wordt.
10. **Termen:** reconciliation, forecast, action log, version, teach-back, key user
11. **Interviewvraag:** Hoe leg je een databaseprobleem uit aan operations?
12. **Voorbeeldantwoord:** Ik beschrijf welke handeling vertraagt, wat wel werkt, welke tijdelijke werkwijze veilig is en wanneer een update volgt. De technische fout geef ik apart aan de uitvoerders. Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** Schrijf hetzelfde incident in 5 zinnen NL/EN/FR. Laat taalhulp fouten verbeteren zonder je competentieniveau te overdrijven.
14. **Werksituatie:** Business leest “test klaar” als “live”; scheid gebouwd, getest, geaccepteerd en productie-gevalideerd.
15. **Leertijd:** 4–8 uur templates/praktijk; taalontwikkeling afhankelijk van uitgangsniveau.


## Jargon en moderne vergelijkingen

| Term | Praktische betekenis |
|---|---|
| Datasource | Gedeconfigureerde databaseverbinding voor een applicatie. |
| Connection pool | Herbruikbare databaseverbindingen; verzoeken wachten als alle verbindingen bezet zijn. |
| Thread | Uitvoeringseenheid binnen een proces; teveel werk of wachten kan capaciteit uitputten. |
| JVM | Java Virtual Machine: runtime waarin Java-code draait. |
| WAR/EAR | Verpakkingen voor Java-web-/enterpriseapplicaties; exacte deploymentvorm versieafhankelijk. |
| LPAR | Logical Partition: afgezonderde platformomgeving met toegewezen resources; niet bevestigd bij ICO. |
| HMC | Hardware Management Console voor relevant IBM-platformbeheer; aanwezigheid onbekend. |
| Paging | Geheugenpagina’s naar opslag verplaatsen; hoge activiteit kan symptoom van druk zijn. |
| UID/permission | Gebruikersidentiteit en bestandsrechten die bepalen welk proces mag lezen/schrijven. |
| Bind variable | Queryparameter apart van SQL-tekst; geen onveilige stringconcatenatie. |
| Constraint | Databaseregel die toegestane waarden/relaties afdwingt. |
| Execution plan | De stappen waarmee database een query uitvoert; DBA interpreteert met volume/parameters. |
| Mapping | Bronvelden/codes vertalen naar doelvelden met expliciete regels. |
| ACK/NACK | Positieve/negatieve bevestiging; contract bepaalt of ontvangst of businessuitkomst bedoeld wordt. |
| Idempotentie | Herhaalde verwerking geeft hetzelfde bedoelde businessresultaat zonder dubbel effect. |
| Atomiciteit | Samenhangende wijzigingen slagen samen of worden samen ongedaan gemaakt. |
| Correlation ID | Referentie die dezelfde handeling door meerdere componenten koppelt. |
| Retry/replay | Retry is opnieuw proberen; replay is bestaande input herverwerken. Eerst commit/duplicaatrisico bepalen. |
| Ordering | Volgorde waarin events verwerkt worden; aankomsttijd is niet altijd businessvolgorde. |
| Backlog/oldest age | Onverwerkt werk en leeftijd van het oudste item; beide bepalen of de keten achterloopt. |
| Dead letter | Afzondering van niet verwerkbare berichten voor gecontroleerd onderzoek; product niet bevestigd. |
| Outbox | Ontwerp waarin businesscommit en verzendopdracht samen duurzaam vastgelegd worden; demo-optie. |
| Backoff/jitter | Toenemende wachttijd en spreiding bij retries om een herstelbare fout niet te verergeren. |
| Circuit breaker | Ontwerp dat tijdelijk calls stopt na herhaald falen; geen genoemd ICO-component. |
| Row-level security | Toegang beperken per record/datascope; exacte mechaniek afhankelijk van product. |
| Authentication/authorization | Identiteit controleren versus toestemming voor actie/object bepalen. |
| Session state | Waarden/context van een gebruikerssessie; niet gelijk aan permanente databasesessie. |
| ORDS | Oracle REST Data Services: webintermediair naar Oracle/APEX; niet genoemd in vacature. |
| Workspace/region/item/process | APEX-werkgebied, paginagebied, invoerwaarde en verwerkingsstap; details in officiële docs. |
| DNS/TCP/TLS | Naamresolutie, netwerkverbinding en versleutelde/beveiligde transportlaag. |
| Certificate chain/truststore | Vertrouwensketen van certificaten en verzameling vertrouwde issuers/config; versiebeheer nodig. |
| RBAC/scope | Rechten via rollen en begrenzing tot relevante objecten/klant/site. |
| Retention | Hoe lang logs/data bewaard blijven; verwijderen alleen volgens beleid/eigenaar. |
| Artefact/manifest | Uit te rollen pakket en overzicht van compatibele app/config/schema/mappingversies. |
| CI/CD | Automatische build-/test-/deliverystappen; platform bij ICO onbekend. |
| Smoke test | Kleine controle op kritieke werking na deployment; ook echte businesshandeling testen. |
| Forward fix | Nieuwe herstelwijziging in plaats van terugzetten; nodig als rollback niet veilig is. |
| UAT | User Acceptance Testing: gebruikers controleren afgesproken taakresultaat en uitzonderingen. |
| CRQ/lastenboek | Change request en technische opdracht met scope, werkpakketten, risico en acceptance. |
| Tolerance/forecast | Afgesproken afwijkingsgrens en verwachting van eindresultaat/kosten op actuele informatie. |
| Optimistic concurrency | Wijziging toestaan alleen als record nog dezelfde versie heeft als bij lezen. |
| Reconciliatie | Bron/target vergelijken op sleutel, velden en businessbetekenis, niet alleen totaal. |
| Cutover/in-flight | Overgang naar nieuw systeem en events die rond dat moment nog onderweg/onverwerkt zijn. |
| RACI | Wie uitvoert, eindverantwoordelijk beslist, geraadpleegd en geïnformeerd wordt; lokale matrix verifiëren. |

**Legacy in moderne concepten:** AIX is dezelfde architectuurlaag als andere Unix/Linux-OS’en, niet dezelfde commandoset. JBoss hoort bij de runtime/application-serverlaag, niet bij databases of frontendframeworks. iWay combineert integratie-/adapter-/mappingconcepten die je ook in moderne middleware aantreft, maar een simulator bewijst geen iWay-administratie. WebFOCUS is BI/rapportering; overdraagbaar zijn joins, filters, definities en lineage, niet automatisch productsyntax. APEX is databasegerichte webontwikkeling; een moderne webdemo kan validatie/rechten/audit tonen maar geen APEX-productexpertise. Vergelijk concepten, benoem productverschillen en respecteer bestaande systeemwaarde.

<a id="07"></a>

# DEEL 07 — Businesskennis

**Bevestigde publieke bedrijfscontext:** [ICO](https://www.icoterminals.com/nl/over-ico/de-toegangspoort-tot-europa) beschrijft RoRo en automotive met terminals in Zeebrugge/Antwerpen en Europese distributie. **Waarschijnlijk / afgeleid uit functiecontext:** onderstaande processen en datamodellen zijn sectormodellen, geen ICO-procedure.

## Begrijp de fysieke operatie

RoRo betekent roll-on/roll-off: rollend materieel rijdt het schip op en af. Een terminal verbindt fysieke overdracht met registratie, planning en informatie aan partners. Een logisch voertuigproces is pre-advice → ontvangst → identificatie → locatie → behandeling/controle → vrijgave/planning → vertrek. Niet ieder bedrijf gebruikt deze statusnamen. Vehicle processing, ship handling en terminal handling zijn op de ICO-site als activiteiten genoemd; concrete IT-workflows verifiëren.

| Begrip | Betekenis | IT-consequentie |
|---|---|---|
| VIN | Identificatienummer voertuig; echte validatieregels afhankelijk van type | Eenduidige sleutel, gevoelige koppeling en duplicaatcontrole |
| Pre-advice | Vooraf aangekondigde aankomst | Aankondiging is geen fysieke ontvangst |
| Gate-in/gate-out | Registratie van binnenkomst/vertrek | Tijd, actor en locatie moeten traceerbaar zijn |
| Yard/positie | Opslaggebied en plaats | Foutieve positie leidt tot zoekwerk of verkeerde planning |
| Vessel/voyage | Schip en reis | Planning/reisreferentie goed koppelen; model onbekend |
| Dwell time | Verblijfsduur op terminal | Exacte begin/eindtijd en uitsluitingen afspreken |
| Release/hold | Vrijgave of blokkering | Softwarevrijgave niet blind gelijkstellen aan fysieke toestemming |
| Reconciliatie | Bronnen vergelijken en verschillen verklaren | Aantallen én unieke sleutels én betekenis controleren |
| Cutover | Overgang naar nieuw systeem | Open processen, historie en berichten meenemen |
| Source of truth | Gezaghebbende bron per gegeven | Conflictregels nodig als bronnen elkaar tegenspreken |

## Gegevens die waarschijnlijk bewegen

Voertuig-ID, partnerreferentie, status, locatie, aankomst/vertrektijd, reis/opdracht, uitzondering en afhandeling. Finance/ERP-koppelingen kunnen bestaan, maar de vacature bevestigt geen ERP of financieel systeem. Leer daarom eerst operationele datastromen, daarna werkelijke downstreamrapportage.

Gebruikersproblemen: voertuig niet vindbaar, status loopt achter, dubbele verwerking, ontbrekende vrijgave, rapportcijfers verschillen en portaal toont data van verkeerde scope. IT-kwaliteit betekent correcte fysieke traceerbaarheid, voorspelbare informatie en gecontroleerde verandering. Vraag altijd wat een verkeerde systeemstatus op de vloer veroorzaakt.

## Oefening

Teken voor tien synthetische voertuigen aankomst, locatie en vertrek. Laat één bericht ontbreken, één dubbel komen en één verkeerd geordend aankomen. Maak een lijst van verschillen en onderscheid fysieke werkelijkheid, systeemregistratie en partnerinformatie. Goed genoeg: je kunt ieder verschil verklaren en weet welke bron beslissend moet zijn; je verzint geen status om aantallen te laten passen.

<a id="08"></a>

# DEEL 08 — Skills matrix en prioriteiten

**Bronstatus:** expliciete verantwoordelijkheden volgen uit [Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer). De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.

Niveaus: **theorie kennen → begrijpen → uitvoeren met hulp → zelfstandig uitvoeren → expert**. Expert zijn betekent specialistische oorzaken/ontwerpkeuzes overzien, geen noodzakelijke startvoorwaarde voor iedere stacknaam.

| Skill | Nodig niveau | Prioriteit | Waarom / vacature | Hoe aantonen? |
|---|---|---|---|---|
| SQL / relationele data | Zelfstandig read-only analyseren | MUST HAVE | R19/R20/R25: Join, null, unieke sleutel, transactie en reconciliatie | Query + uitleg + testdata |
| Incidentanalyse / ketendiagnose | Zelfstandig, productieacties met mandaat | MUST HAVE | R25/R03: Impact, scope, bewijs, veilige herstelstap | Incidentrapport + hardop casus |
| Requirements en acceptatiecriteria | Zelfstandig | MUST HAVE | R11/R12: Businessvraag testbaar maken | CRQ + positieve/negatieve tests |
| Communicatie en prioritering | Zelfstandig | MUST HAVE | R26/R33: Mensen op impact/besluit richten | Businessupdate + STAR-case |
| Applicatiecomponenten en datastromen | Zelfstandig modelleren | MUST HAVE | R17/R19: Fouten lokaliseren en changes beoordelen | Diagram + transactie walkthrough |
| Project-/leverancierssturing | Zelfstandig binnen mandaat | MUST HAVE | R06/R07/R16: Scope, capaciteit en acceptatie bewaken | Planning + risicolog + forecast |
| Release, change en herstel | Uitvoeren met hulp → zelfstandig | SHOULD HAVE | R18/R25: Wijziging veilig en traceerbaar | Gerepeteerd releaseplan |
| EDI / iWay-concepten | Gebruiken en flow diagnosticeren | SHOULD HAVE | R20: Mapping, ACK, idempotentie en replay | Berichtpipeline met negatieve tests |
| Oracle praktijk | Gebruiken; DBA-werk met hulp | SHOULD HAVE | R19: SQL-tooling en foutbeelden kennen | Oracle-demo of expliciete simulatorbeperking |
| JBoss / Java runtime | Begrijpen en logs gebruiken | SHOULD HAVE | R19: Runtime, pool, exceptions en config | Diagnoserapport van testapp |
| WebFOCUS / rapportdefinities | Gebruiken → beheer leren | SHOULD HAVE | R20: Cijfers en filters verklaren | Rapportreconciliatie |
| Webportal / Apex | Gebruiken, kleine functie bouwen | SHOULD HAVE | R21/R22/R31: Input, validatie, rollen en audit | Formulier + rechten/validatietests |
| Nederlands/Engels/Frans | Praktisch communiceren; eisen navragen | SHOULD HAVE | R32: Intern en extern overleg | Zelfde incident uitleggen in drie talen |
| AIX / IBM P-series | Begrijpen; beheer onder begeleiding | ON THE JOB | R19: Laaggrenzen, resources en rechten | Linux-lab met expliciete AIX-verschillen |
| ICO-processen / TOS-product | Lokaal leren | ON THE JOB | R08/R35: Siteconfig en migratie-specifieke regels | Buddy-walkthrough, proceskaart |
| MS Office | Zelfstandig gebruiken | SHOULD HAVE | R30: Rapportage, analyse en opleiding | Budget/reconciliatiesheet + instructie |
| PRINCE2 / alternatief | Begrijpen en toepassen | SHOULD HAVE | R29: Businesscase, stages, tolerantie | Faseplan; certificaat niet verplicht genoemd |
| IT-evoluties en lifecycle | Afwegen | SHOULD HAVE | R28: Beheerbaarheid en migratiekeuzes | Technische beslisnotitie |
| Veiligheid/kwaliteit/milieu | Toepassen, lokale regels leren | MUST HAVE | R09/R04: Fysieke operatie niet schaden | Risicoafweging + traceerbare workaround |
| Training / taakgericht leidinggeven | Zelfstandig kleine groep | SHOULD HAVE | R14/R27/R33: Adoptie en overdracht | Quick guide + teach-back |
| Cloud/Kubernetes | Alleen indien bevestigd | NICE TO HAVE | Afgeleid: Niet genoemd; geen leerblocker | Geen prioritair bewijs nodig |
| Diepe AIX/Oracle tuning | Expert niet aangenomen | NICE TO HAVE | Afgeleid: Specialistische samenwerking; eigenaarschap navragen | Duidelijke escalatiegrens |

## MUST HAVE

Analytisch SQL-denken, incidentafbakening, requirements, communicatie, componentmodel, project-/leverancierssturing en verantwoordelijk omgaan met veiligheid/data. Professionele diepte kan verschillen, maar ontbreken van zowel begrip als bewijs maakt de rol moeilijk.

## SHOULD HAVE

Releasepraktijk, EDI, Oracle/JBoss, rapportering, portalontwikkeling, taalvaardigheid, Office en methodisch plannen. Leer de relevante subset; bespreek niveau eerlijk. Programmeerervaring in een andere stack helpt, maar bewijst geen Oracle/AIX-beheerervaring.

## NICE TO HAVE

Cloud, containers, specialistische performance tuning en formele projectcertificatie. Deze zijn niet allemaal letterlijk vereist. Geen prioritaire roadmap zonder bevestiging van gebruik of selectiecriteria.

## On the job leren

ICO-statuscodes, specifieke TOS, productversies, leveranciersafspraken, toegang, monitoringtool, rapportcatalogus en lokale veiligheidsregels. Wacht niet op kennis die alleen intern beschikbaar is.

## Top 10 op leer-ROI

1. SQL joins, transacties en read-only reconciliatie.
2. Impactgestuurde troubleshooting met bewijs.
3. Datastromen en bron van waarheid.
4. Requirements met acceptatiecriteria.
5. Incidentcommunicatie en escalatie.
6. EDI-validatie, ACK en duplicaatveiligheid.
7. Change/release/recovery-plan.
8. Leverancierswerkpakket en acceptatiebewijs.
9. JBoss/Oracle/AIX-laagbegrip.
10. Taakgericht portaal/APEX-prototype en gebruikersopleiding.

<a id="09"></a>

# DEEL 09 — Mentale modellen

**Waarschijnlijk / afgeleid uit functiecontext — algemene werkwijze.**

## 1. Impact vóór techniek

Vraag: welke taak faalt, hoeveel gebruikers/voertuigen/partners, welke vestiging, is er een veilig alternatief en wat is de deadline? Een bug in een rapport kan kritieker zijn dan een loginprobleem voor één testaccount. Prioriteit is impact × urgentie, niet luidste afzender. Laat operationele verantwoordelijke veiligheid beoordelen.

## 2. De keten van bewijs

Input → validatie → mapping → businessregel → commit → ACK → rapport. Schrijf bij elke grens wat al bewezen werkt. Zoek de eerste aantoonbaar verkeerde overgang. “Bestand ontvangen” bewijst transport, geen businesscommit. “HTTP 200” bewijst niet dat een voertuigstatus is aangepast.

## 3. Hypothesematrix

| Hypothese | Voorspelling | Veilige test | Bewijs dat haar weerlegt |
|---|---|---|---|
| Partner levert ongeldige datum | Alleen nieuwe formaatvariant faalt | Vergelijk één geredigeerd bericht met contract | Zelfde variant slaagt bij dezelfde mapping |
| Databaseverbinding tekort | Meerdere transactietypes wachten tegelijk | Poolmetingen en DBA-sessies correleren | Pool gezond, alleen één payload faalt |
| Rapportfilter fout | Brondata klopt, één rapport wijkt af | Zelfde sleutelset en tijdvenster vergelijken | Bronsleutels ontbreken ook |

Voer één onderscheidende test per keer uit. Zoek actief een tegenvoorbeeld. Controleer tijdzones, versies en scope voordat je “de database” beschuldigt.

## 4. Systeemdenken

Teken afhankelijkheden vóór verandering. Een retry verhoogt load, die een pool uitput, die meer timeouts veroorzaakt. Een lokale fix kan een feedbacklus versterken. Vraag wat downstream moet gebeuren en welke toestand na een halve verwerking overblijft.

## 5. Onzekerheid communiceren

“Bevestigd: partner A-berichten sinds 09:12 wachten. Nog onbekend: oorzaak in mapping of verwerking. Onderzoek: team X vergelijkt bericht-ID’s. Actie: nieuwe retries tijdelijk gecontroleerd, geen bulk-replay. Volgende update: 09:40.” Gebruik geen ongefundeerde ETA.

## 6. Escalatie en mandaat

Escaleren bij veiligheidsrisico, mogelijke datacorruptie, brede uitval, ontbrekend productierecht, benodigde specialist, overschreden afgesproken termijn of besluit buiten je mandaat. Geef impact, tijdlijn, laatste werkende grens, hypothesen, uitgevoerde tests en het benodigde besluit mee.

## 7. Workaround versus oplossing

Workaround: gecontroleerde tijdelijke werkwijze met eigenaar, beperkingen, einddatum en reconciliatie. Structurele oplossing: oorzaak verwijderd, regressietest, monitoring en documentatie aangepast. Een restart kan incidentherstel zijn; herhaalde resource-uitputting blijft een problem-record.

## 8. Businessregels vóór schermen

Voor een correctieformulier vraag je wie mag corrigeren, welke statusovergang geldig is, welke partner opnieuw geïnformeerd moet worden en hoe audit werkt. Ontwerp pas daarna de knop.

<a id="10"></a>

# DEEL 10 — Troubleshooting playbook

**Waarschijnlijk / afgeleid uit functiecontext.** Dit framework is een oefenrunbook, geen toestemming om productie te wijzigen.

## Algemeen framework

1. Definieer de mislukte businesshandeling en verwacht/werkelijk resultaat.
2. Bepaal impact, veiligheid, urgentie en incidentowner.
3. Scope op locatie, gebruiker, partner, berichttype, versie en tijd.
4. Verzamel ticket, tijdzone, reproduceerstappen en geredigeerde voorbeelden.
5. Reproduceer veilig in test; geen echte productie-effecten herhalen.
6. Bekijk logs met tijd/correlatie; bewaar origineel bewijs volgens retentiebeleid.
7. Controleer recente changes, config, certificaten, data en partnerwijzigingen.
8. Vergelijk input en output op iedere ketengrens.
9. Onderzoek database read-only: records, constraints, locks via bevoegd beheerder.
10. Onderzoek netwerk en integratie: bereikbaarheid, TLS, ACK, mapping en backlog.
11. Maak meerdere hypotheses en selecteer een test die ze onderscheidt.
12. Voer herstel uit binnen change/incidentmandaat, met herstelplan.
13. Valideer businesshandeling en vergelijk unieke sleutels/aantallen.
14. Monitor backlog, foutpercentage en dataconsistentie in afgesproken venster.
15. Sluit met gebruikersbevestiging, oorzaak of problem-link, acties en eigenaar.

## Read-only voorbeeld in synthetisch portfolio

```sql
SELECT message_id, partner_id, status, received_at
FROM edi_messages
WHERE received_at >= :from_time
  AND partner_id = :partner
ORDER BY received_at;
```

Dit schema is fictief. Bind parameters, beperk scope en pas query aan het goedgekeurde schema aan. Vraag DBA om dure query/lockdiagnose; voer geen directe UPDATE uit om een incident snel te laten verdwijnen.

## Communicatiemomenten

Bij ontvangst: impact en volgende update. Bij afbakening: bekende scope en maatregelen. Voor herstel: risico en benodigd besluit. Na herstel: functionele verificatie en restimpact. Bij afsluiting: oorzaak/bekende onzekerheid, reconciliatie en structurele acties. Voorbeelden met logdetails staan in de incidenten hieronder.


## 01. Eén gebruiker kan niet inloggen — Basis

Vacaturekoppeling: R21/R25/R32. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Om 08:40 meldt een operator dat het portaal toegang weigert; een collega lijkt wel te kunnen werken.

**Wat weet ik?:** Eén melding en een loginfout, niet bewezen sitebrede uitval.

**Wat weet ik niet?:** Foutcode, rol, accountstatus, omgeving en of andere accounts hetzelfde probleem hebben.

**Eerste vragen / controles:** Sinds wanneer, welk scherm/bericht, account of device, recent wachtwoord/rol gewijzigd?

**Mogelijke oorzaken:** Verlopen account/sessie, verkeerde loginroute, rolprobleem, lokale browsercache of identitydienst.

**Logs / bewijs:** Tijd, geredigeerde account-ID, auth-fout en servercorrelatie. Geen wachtwoord loggen.

**Database:** Applicatierol/scope vergelijken met goedgekeurde matrix; geen eigen productie-accounttabel aanpassen.

**Netwerk:** Alleen relevant als endpoint/authdienst niet bereikt wordt; vergelijk dezelfde URL vanaf twee devices.

**Applicatie:** Onderscheid 401/authenticatie van 403/toestemming; niet blind admin geven.

**Integratie:** SSO is onbekend; als gebruikt, laat identityowner hetzelfde request volgen.

**Mijn aanpak:** Impact bevestigen → vergelijken met werkend account → auth versus rechten isoleren → gericht herstellen.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: account is juist geauthenticeerd maar ontbreekt in operatorrol; bevestigen in serverlog/rolmatrix.

**Oplossing:** Bevoegde eigenaar corrigeert de goedgekeurde rol; nieuwe sessie en echte taak testen.

**Communicatie:** Zeg welke taak geblokkeerd is, wat nog werkt en volgende update; accountdetails alleen aan bevoegde groep.

**Preventie:** Onboarding/rolwijziging met acceptatietest en duidelijke identity-escalatie.

**Goed genoeg / rubric:** Impact en scope; Authenticatie versus autorisatie; Least privilege; Functionele hercontrole.

## 03. Rapportexport bevat verkeerde telling — Basis

Vacaturekoppeling: R20/R30. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een WebFOCUS-rapport en Excel-export tonen een ander voertuigaantal.

**Wat weet ik?:** Twee verschillende uitkomsten, nog geen bewijs van dataverlies.

**Wat weet ik niet?:** Definities, filters, tijdzone, refresh en unieke sleutel.

**Eerste vragen / controles:** Tellen we voertuigen of events? Dezelfde locaties, datumgrenzen en autorisatie?

**Mogelijke oorzaken:** One-to-many join, verkeerde filter, exportlimiet, stale refresh of spreadsheetformule.

**Logs / bewijs:** Rapportparameters, queryversie, refreshmoment en exportmetadata.

**Database:** Verschilset op businesssleutel; join-cardinaliteit en nulls controleren.

**Netwerk:** Pas controleren bij afgebroken export/timeout; geen eerste hypothese.

**Applicatie:** Dezelfde report-versie/parameters en scope testen.

**Integratie:** Controleer bronrefresh indien rapport op downstreamdataset draait.

**Mijn aanpak:** Definitie aligneren → dezelfde snapshot → verschillen per sleutel → query/export isoleren.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: rapport telt eventregels in plaats van unieke voertuigen; bevestigen via kardinaliteit.

**Oplossing:** Definitie/query corrigeren via change; verwacht resultaat door business laten bevestigen.

**Communicatie:** Meld cijferimpact zonder direct “database fout” te zeggen; corrigeer eerder verspreid rapport indien nodig.

**Preventie:** Rapportdatacontract, referentieset en formulecontrole.

**Goed genoeg / rubric:** Definitie en scope; Sleutelreconciliatie; Join-cardinaliteit; Businessacceptatie.

## 06. API geeft serverfout — Intermediate

Vacaturekoppeling: R22/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een portalactie geeft HTTP 500 voor één type aanvraag; andere acties slagen.

**Wat weet ik?:** Serverantwoord is fout, niet dat het hele platform uitligt.

**Wat weet ik niet?:** Payloadvariant, eerste fout, commitstatus en recente changes.

**Eerste vragen / controles:** Welke actie, welke input, sinds wanneer, request-ID, gebeurt hetzelfde bij alle records?

**Mogelijke oorzaken:** Null/validatiefout, constraint, code-exception of downstreamfout.

**Logs / bewijs:** Request-ID, exceptionketen en laatste change, met secrets gemaskeerd.

**Database:** Zoek businessresultaat en constraintfout read-only; commitstatus vóór retry.

**Netwerk:** 500 bewijst bereikbaar applicatiepad; downstreamconnectiviteit kan wel falen.

**Applicatie:** Reproduceer input in test, vergelijk runtime/config en foutafhandeling.

**Integratie:** Contractversie/downstreamresponse controleren als fout door externe service komt.

**Mijn aanpak:** Scope → first exception → input vergelijken → commitstatus → veilige repro → fix/test.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: onbekende status wordt onjuist als null verwerkt; bevestig reproduceerbare exception.

**Oplossing:** Validatie/foutpad verbeteren en alleen veilige requests herhalen; geen bulk retry.

**Communicatie:** Meld getroffen actie en veilige workaround, niet een onbewezen gehele uitval.

**Preventie:** Negatieve contracttests en logging van eerste foutgrens.

**Goed genoeg / rubric:** Scope en correlatie; Eerste exception; Commit vóór retry; Negatieve regressietest.

## 07. EDI-bericht geweigerd — Intermediate

Vacaturekoppeling: R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Eén partnerbericht bereikt middleware maar wordt afgewezen; 18 vergelijkbare berichten wachten.

**Wat weet ik?:** Transportreceipt bestaat; businessacceptatie niet.

**Wat weet ik niet?:** Foutveld, mappingversie, partnercontract en partial processing.

**Eerste vragen / controles:** Welke ID’s, nieuwe formaatvariant, laatste goede sample, contractwijziging aangekondigd?

**Mogelijke oorzaken:** Datum/encoding, onbekende code, verplichte waarde ontbreekt of mappingversie verkeerd.

**Logs / bewijs:** Transport-ID, parser/validationlog, mappingversie, foutveld; geredigeerde payload.

**Database:** Check unieke businesssleutel en eventuele gedeeltelijke commit.

**Netwerk:** Transport werkt voor sample; pas verder testen als receipt onvolledig is.

**Applicatie:** Controleer semantische businessvalidatie na syntax.

**Integratie:** Vergelijk input/output per stap en technisch versus functioneel ACK.

**Mijn aanpak:** Contract vergelijken → foutveld isoleren → representatieve test → correctie → controlled replay.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: partner levert nieuwe datumvariant; onderscheid fout contract versus mapping.

**Oplossing:** Partner corrigeren of geautoriseerde mappingchange; replay pas na duplicate-check en reconciliatie.

**Communicatie:** Geef partner dezelfde ID/tijd en concreet contractverschil; business krijgt impact/volume.

**Preventie:** Contractversiebeheer, sampletests en schema-validatie.

**Goed genoeg / rubric:** Transport versus verwerking; Contractbewijs; Partial commit/duplicaten; Veilige replay.

## 08. Databasequery is traag — Intermediate

Vacaturekoppeling: R19/R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een specifieke zoekactie duurt 20 seconden in de demo; de vorige testbaseline was 2 seconden.

**Wat weet ik?:** Taak is trager onder bepaalde input; cijfers zijn fictief.

**Wat weet ik niet?:** Queryplan, locks, volume, parameters, concurrency en configchange.

**Eerste vragen / controles:** Alle zoekacties of één filter, piekmoment, laatste wijziging, hoeveel records?

**Mogelijke oorzaken:** Verkeerd queryplan, meer volume, missing/poor index, lock, poolwait of onbegrensde export.

**Logs / bewijs:** Requesttiming splitsen in poolwait/query/render; query-ID en parameters volgens privacybeleid.

**Database:** DBA plan/locks laten bekijken; row count en selectiviteit vergelijken met baseline.

**Netwerk:** Meet alleen als server/DB-roundtrip afwijkend is; onderscheid querytijd van netwerktijd.

**Applicatie:** Parameter/ORM-query en pagina-limit vergelijken; geen onbewezen tuning.

**Integratie:** Batchbelasting of partnerburst kan load toevoegen; correleer tijd.

**Mijn aanpak:** Baseline → concrete repro → laag-timings → DBA evidence → meet één wijziging.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: filter ontbreekt in nieuwe query; bewijs via rows/plan, niet alleen CPU.

**Oplossing:** Gerichte queryfix en review/test; index of capacity alleen met eigenaar/impactanalyse.

**Communicatie:** Meld taak/volume/temporary limit en geen prestatiebelofte zonder meting.

**Preventie:** Representatieve performancetest, querylimits en trendmonitor.

**Goed genoeg / rubric:** Baseline en parameters; Pool versus querytijd; DBA/plan evidence; Voor/nameting.

## 09. JBoss kan niet verbinden met database — Intermediate

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Na configuratiewijziging starten applicaties maar transacties geven datasource-fouten.

**Wat weet ik?:** Runtime start; businesshandeling faalt.

**Wat weet ik niet?:** Credentials, endpoint, pool, DB-status en juiste targetomgeving.

**Eerste vragen / controles:** Alle apps/hosts, sinds welke change, eerste foutcode, welk datasourceprofiel?

**Mogelijke oorzaken:** Verkeerd endpoint/secret, DB niet bereikbaar, auth geweigerd of poolconfig.

**Logs / bewijs:** Datasource/JDBC-fout, configrelease, server/starttijd; credentialwaarden nooit tonen.

**Database:** DB-eigenaar controleert listener/auth/service en geschikte sessies.

**Netwerk:** Resolutie/poort en werkelijke DB-service testen door bevoegd team.

**Applicatie:** Vergelijk config met goedgekeurde omgeving; health endpoint is onvoldoende.

**Integratie:** Andere DB-afhankelijke flows als impactgrens vergelijken.

**Mijn aanpak:** Recent change → configdiff zonder secrets → netwerk/auth/pool onderscheiden → herstel.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: testendpoint in productieconfig; bewijs via manifest/configkey.

**Oplossing:** Goedgekeurde config terugzetten of corrigeren; business-smoke en integratiecontrole.

**Communicatie:** Informeer over transacties die wel/niet werken en veilige retryvoorwaarden.

**Preventie:** Omgevingsvalidatie, secretreferenties en dependency healthcheck.

**Goed genoeg / rubric:** Business-smoke; Secretveilig configbewijs; Netwerk/auth onderscheiden; Gecontroleerde restore.

## 10. AIX-filesystem vol — Intermediate

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Verwerking stopt met write-fouten; een beheerder meldt 100% bezetting van een filesystem.

**Wat weet ik?:** Schrijfprobleem en capaciteitssignaal; locatie/data-inhoud nog onbekend.

**Wat weet ik niet?:** Welke files, retentie, andere services en veilige opruimoptie.

**Eerste vragen / controles:** Welk mount/path, groeisnelheid, sinds wanneer, vereist audit/berichtarchief, wie beheert opslag?

**Mogelijke oorzaken:** Loggroei, grote batch, retentiejob faalt of tijdelijke bestanden blijven staan.

**Logs / bewijs:** Write exception, disktrend, retentiescheduler en recente volumenverandering.

**Database:** Controleer of commit al gedaan is en alleen export/ACK faalt; DB-files nooit blind verwijderen.

**Netwerk:** Niet eerste oorzaak; downstreamretries kunnen extra volume opleveren.

**Applicatie:** Welke uitvoer faalt, wat is opnieuw uitvoerbaar en wat moet bewaard?

**Integratie:** Blokkeer ongecontroleerde replay; check output versus gecommitteerde data.

**Mijn aanpak:** Owner → impact → evidence bewaren → retentie/capaciteitplan → controlled herstel.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: logging is gegroeid na debugchange; bevestig zonder auditverlies.

**Oplossing:** Bevoegd beheerder archiveert/roteert volgens beleid of breidt capaciteit uit; app/businessflow testen.

**Communicatie:** Zeg dat herstelplan databehoud omvat; geen “we verwijderen alles” shortcut.

**Preventie:** Diskthreshold, groeitrend, retentietest en debug-einddatum.

**Goed genoeg / rubric:** Geen blind verwijderen; Eigenaarschap opslag; Commit/replay check; Groei en retentie.

## 11. Dubbel verwerkt partnerbericht — Intermediate

Vacaturekoppeling: R20/R22/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een partner verstuurt dezelfde aankomst twee keer; er verschijnen dubbele events.

**Wat weet ik?:** Dubbele input; dubbele business-effecten vermoed.

**Wat weet ik niet?:** Message-ID versus businesssleutel, commit/ACK, impact op rapport en operatie.

**Eerste vragen / controles:** Zijn IDs gelijk, is hetzelfde business-event opnieuw verpakt, welke verwerking is correct?

**Mogelijke oorzaken:** Retry na ontbrekend ACK, deduplicatie op verkeerde sleutel, niet-atomische check/insert.

**Logs / bewijs:** Ontvangst, dedupbesluit, commit en ACK per ID met timestamps.

**Database:** Unieke keys en audit vergelijken; race/transactionboundary bekijken met developer/DBA.

**Netwerk:** Timeout kan trigger zijn; transportprobleem is niet hele oorzaak.

**Applicatie:** Idempotentie moet ook bij concurrente verzending werken.

**Integratie:** Bespreek retrycontract en betekenis van IDs met partner.

**Mijn aanpak:** Effect inventariseren → bron-event bepalen → oorzaak retry/dedup → veilige correctie.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ieder retry krijgt nieuw transport-ID maar dezelfde eventkey.

**Oplossing:** Unique business-eventkey en atomische verwerking via change; correctie met audit en downstreamreconciliatie.

**Communicatie:** Meld dat ontvangst dubbels normaal kan zijn, dubbel effect niet; correctie-impact afstemmen.

**Preventie:** Concurrency/duplicate/timeout-regressietests en dedupmonitor.

**Goed genoeg / rubric:** Businesssleutel versus transport-ID; Atomiciteit; Auditcorrectie; Concurrency test.

## 12. Ontbrekend ACK na succesvolle commit — Intermediate

Vacaturekoppeling: R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Partner zegt “niet ontvangen”; intern lijkt event wel verwerkt.

**Wat weet ik?:** Intern record bestaat; partnerstatus onduidelijk.

**Wat weet ik niet?:** Welke ACK-semantiek, verzendstatus, correlation en retryrisico.

**Eerste vragen / controles:** Welk event, welk expected ACK, sinds wanneer, partner ontvangt andere confirmations?

**Mogelijke oorzaken:** ACK-export mislukt, transporttimeout, partnerfilter of mismatch referentie.

**Logs / bewijs:** Commit en outbound ACKlog op dezelfde correlation/businesskey.

**Database:** Bewijs unieke commit; geen event opnieuw aanmaken om ACK te forceren.

**Netwerk:** Retourpad/TLS/credential en beide tijdlijnen vergelijken.

**Applicatie:** Controleren of ACK los van businessverwerking veilig opnieuw te sturen is.

**Integratie:** Partner vraagt bestaande bevestiging/replaycontract, geen volledige re-import.

**Mijn aanpak:** Commitstatus bewijzen → outbound-grens isoleren → bevestiging gecontroleerd herverzenden.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ACKsend timeout na commit; check outboundqueue en partnerreceipt.

**Oplossing:** Alleen bevestiging opnieuw sturen volgens contract; event niet opnieuw verwerken.

**Communicatie:** Bevestig intern resultaat met minimale gegevens en test ontvangst samen.

**Preventie:** Duurzame outboundstatus, ACK-retries en end-to-end reconciliatie.

**Goed genoeg / rubric:** Commitbewijs; ACK-semantiek; Geen dubbel event; Partnerreceipt controleren.

## 14. TLS-certificaat verlopen — Intermediate

Vacaturekoppeling: R21/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een partnerendpoint faalt sinds middernacht met handshake error.

**Wat weet ik?:** TLS-fout vóór businessresponse.

**Wat weet ik niet?:** Certificaatkant, trustchain, expiry, gewijzigde hostname en andere consumers.

**Eerste vragen / controles:** Welk endpoint, welke chain, laatste goede verbinding, is renewal geweest?

**Mogelijke oorzaken:** Expiry, incomplete chain, truststore verouderd, hostname mismatch of klokprobleem.

**Logs / bewijs:** TLS-fout/expiry/hostname zonder secrets, requesttijd en deploymentconfig.

**Database:** Geen DB-mutatie nodig; check eventueel reeds gecommitteerde queuevoorraad.

**Netwerk:** Bevoegde eigenaar controleert cert/chain/time en relevante endpointroute.

**Applicatie:** Truststoreconfig kan runtimecomponent zijn; tijdelijke trust-all is onveilig.

**Integratie:** Partner bevestigt certwisseling en test hetzelfde endpoint.

**Mijn aanpak:** Certkant identificeren → owner → juiste chain/renewal → test → backlog veilig verwerken.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: partner renewal zonder volledige chain; bewijs via chainvergelijking.

**Oplossing:** Correct certificaat/chain of trustconfig geautoriseerd plaatsen; verificatie nooit uitschakelen.

**Communicatie:** Meld welke stroom blokkeert en plan/volgende update; geen ongefundeerde cyberclaim.

**Preventie:** Expiry-alert, contactlijst en renewalrepetitie.

**Goed genoeg / rubric:** TLS laag; Chain/hostname/time; Geen trust-all; Renewalmonitor.

## 15. Release faalt halverwege — Gevorderd

Vacaturekoppeling: R18/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** App is vernieuwd maar schema-migratie stopt; portaal geeft inconsistent gedrag.

**Wat weet ik?:** Versiemix en gedeeltelijke uitvoering.

**Wat weet ik niet?:** Migratiestappen, irreversible data, oude versiecompatibiliteit, impact.

**Eerste vragen / controles:** Welke stappen geslaagd, transactioneel of niet, huidige schema, herstelbewijs?

**Mogelijke oorzaken:** Migratiefout, ontbrekende permissie, onverwachte data of uitvoervolgorde.

**Logs / bewijs:** Deploymentmanifest, migrationlog, timestamp en first failure.

**Database:** DBA schema/data-status vergelijken met plan; geen blind restore over nieuwe data.

**Netwerk:** Alleen relevant als deployverbinding faalde; eerst state inventory.

**Applicatie:** App/schemaversies en compatibiliteit vaststellen.

**Integratie:** Partners in-/outbound veilig pauzeren als procedure vereist om mixed states te beperken.

**Mijn aanpak:** Stop verdere changes → state inventariseren → go/no-go owner → rollback/forward fix beoordelen.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: migration faalt op onverwachte null-data na eerdere schemawijziging.

**Oplossing:** Gerepeteerd recoverypad of goedgekeurde forward fix; daarna business/data/partnerchecks.

**Communicatie:** Meld precies welke versiestappen klaar zijn en wat onzeker is; updates door één incidentowner.

**Preventie:** Production-like dataset, prereq-check en recoveryrepetitie.

**Goed genoeg / rubric:** Stop en state inventory; Schema/data recovery; Go/no-go owner; End-to-end validatie.

## 19. Productie ligt gedeeltelijk plat — Gevorderd

Vacaturekoppeling: R19/R25/R35. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Zeebrugge meldt dat een kritieke taak faalt; Kallo lijkt nog te werken.

**Wat weet ik?:** Locatiegebonden impact, maar omvang nog te bevestigen.

**Wat weet ik niet?:** Veiligheidsimpact, gedeelde componenten, beschikbaar workaround en prioriteit.

**Eerste vragen / controles:** Welke taak/gebruikers, fysieke gevolgen, starttijd, laatste change, andere locaties echt getest?

**Mogelijke oorzaken:** Siteconfig, netwerkroute, lokaal endpoint, gedeelde app met site-specifieke data of load.

**Logs / bewijs:** Site/time/request correlation, first failure en laatste succesvolle taak.

**Database:** Siteparameters en businesskeys vergelijken; geen systeemwijde datawijziging.

**Netwerk:** Route/DNS/endpointverschil als hypothese; eigenaar laten meten.

**Applicatie:** Zelfde transactie op werkende/ falende site met veilige data vergelijken.

**Integratie:** Partnerstromen per site checken en veilige backlogbewaring regelen.

**Mijn aanpak:** Incidentowner → operationsveiligheid → impactmatrix → laatste goede grens → gerichte hersteltest.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: lokale routeconfigwijziging; bewijzen met locatiepad en app-health/data.

**Oplossing:** Geautoriseerde gerichte herstelactie; test beide sites en reconciliatie, voorkom shared component te verstoren.

**Communicatie:** Vaste updates per getroffen businessunit; benoem wat gecontroleerd blijft werken.

**Preventie:** Sitegerichte synthetic/business checks en configreview.

**Goed genoeg / rubric:** Veiligheid en impact; Werkende site als vergelijking; Gerichte actie; Beide-sites validatie.

## 20. Database lock blokkeert verwerking — Gevorderd

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Meerdere transacties wachten; een DBA ziet één langlopende blocking session.

**Wat weet ik?:** Lock-relatie, nog geen mandaat om sessie te stoppen.

**Wat weet ik niet?:** Owner, transactie-intentie, rollbackduur en commitstatus.

**Eerste vragen / controles:** Sinds wanneer, welke tabellen/taak, recent batch, kan gecontroleerd beëindigd worden?

**Mogelijke oorzaken:** Langlopende transactie, vergeten commit, batchoverlap of gewijzigde lockvolgorde.

**Logs / bewijs:** Requesttiming, DB-session/lock evidence van DBA, job-owner en batchlog.

**Database:** DBA identificeert blocking/waiting sessies en gevolgen; kill kan lang rollbacken.

**Netwerk:** Niet primaire oorzaak als DB-lock bewezen is; geen firewallwijziging.

**Applicatie:** Transactiegrenzen en timeout/retrygedrag bekijken.

**Integratie:** Retryburst vermijden; downstreamstatus pas na commit beoordelen.

**Mijn aanpak:** Owner/impact → lockbewijs → beheerbesluit → veilig beëindigen/herstellen → data check.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: onderhoudsjob houdt lock; controleer eigenaar en status vóór ingreep.

**Oplossing:** DBA voert goedgekeurde actie uit; code/batchfix via problem/change, met transactie/retrytests.

**Communicatie:** Leg uit dat herstel niet onmiddellijk is als rollback nog loopt.

**Preventie:** Batchvensters, transactieduurmonitor, korte transacties en concurrencytests.

**Goed genoeg / rubric:** DBA bewijs; Geen blind kill; Rollbackimpact; Structurele transactiecontrole.

## 22. Mogelijk datalek in portaal — Gevorderd

Vacaturekoppeling: R21/R25/R09. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Klant A meldt mogelijk een voertuig van klant B in de portal.

**Wat weet ik?:** Mogelijke scopefout; omvang niet vastgesteld.

**Wat weet ik niet?:** Reproduceerbaarheid, data/exposure, betrokken users en ownerprocedure.

**Eerste vragen / controles:** Welke minimaal nodige sleutel, tijd, view, accountscope, sinds welke release?

**Mogelijke oorzaken:** Row-scopefilter fout, cache gedeeld, verkeerde klantmapping of data-eigenaarschap.

**Logs / bewijs:** Audit/access/request-ID veilig bewaren; geen gevoelige screenshots breed verspreiden.

**Database:** Goedgekeurde owner controleert klantrelaties en effectieve scope.

**Netwerk:** Geen evidence dat firewallprobleem; eerst server/data-access.

**Applicatie:** Object-level autorisatie en caching toetsen met veilige testaccounts.

**Integratie:** Partner/masterdata kan verkeerd ownership aanleveren, maar server moet scope afdwingen.

**Mijn aanpak:** Securityowner → minimale evidence → containment door bevoegd team → exposure scope → fix/test.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ontbrekende serverfilter; alleen na scopebewijs concluderen.

**Oplossing:** Bevoegd team beperkt toegang en corrigeert autorisatie; credential/notificationkeuzes via echte procedure.

**Communicatie:** Intern feitelijk en vertrouwelijk; externe melding door aangewezen verantwoordelijke.

**Preventie:** Negatieve multi-tenant autorisatietests, cacheisolation en audit.

**Goed genoeg / rubric:** Security-escalatie; Minimale bewijsdeling; Objectscope; Containment en regressietest.

<a id="11"></a>

# DEEL 11 — Incident, problem, change en release

**Expliciet uit vacature:** tweede lijn incident/problem/change en releases coördineren. **Waarschijnlijk / afgeleid uit functiecontext:** onderstaande procesinvulling; ICO-procedure, rollen en tooling eerst verifiëren.

| Proces | Vraag | Voorbeeld | Resultaat |
|---|---|---|---|
| Incident | Hoe herstellen we de dienst? | Partnerberichten verwerken niet | Veilige verwerking hervat en backlog gevalideerd |
| Problem | Waarom gebeurt dit, hoe voorkomen we herhaling? | Iedere maand mappingcrash | Oorzaak, workaround en permanente fix |
| Change | Mag deze wijziging met dit risico uitgevoerd worden? | Mappingversie aanpassen | Beoordeeld/geautoriseerd plan en audit |
| Release | Welke samenhangende versies leveren we op? | App, mapping en DB-schema samen | Versiepakket, communicatie en acceptatiebewijs |
| Deployment | Hoe plaatsen/activeren we die versies? | Artefact uitrollen in test/productie | Technische uitvoering, smoke tests en herstelstatus |

## Incident Management

Neem van Service Desk over met voldoende context. Bepaal prioriteit op operationele impact en urgentie; een P1/P2-schema is niet bekend. Herstel gecontroleerd, houd één owner en voorkom parallelle tegenstrijdige wijzigingen. Sluiten betekent dat de businessdienst werkt en data-effecten zijn gecontroleerd, niet alleen dat een proces draait.

- [ ] Businessimpact, scope en eigenaar vastgelegd.
- [ ] Tijdlijn, laatste goede verwerking en bewijs verzameld.
- [ ] Hypothesen en uitgevoerde acties met tijd genoteerd.
- [ ] Escalatie, mandaat en communicatie afgesproken.
- [ ] Herstel functioneel gevalideerd; backlog/data gecontroleerd.
- [ ] Gebruiker bevestigt resultaat; problem-link bij onzekere/herhaalde oorzaak.

## Problem Management

Een herhaald incident vraagt een oorzaakanalyse. Gebruik causale keten: mapping exception → malformed payload → geen afgesproken versievalidatie → contractwijziging niet gemeld. “Menselijke fout” is geen voldoende root cause. Zoek ontbrekende controles en bewijs. Een post-mortem moet leerbaar zijn, met preventie-eigenaar en deadline.

- [ ] Gerelateerde incidenten, frequentie en impact verzameld.
- [ ] Oorzaak onderscheiden van trigger en symptoom.
- [ ] Hypothese met reproductie/tegenbewijs onderbouwd.
- [ ] Workaround met grenzen gedocumenteerd.
- [ ] Fix via change, regressietest en monitoring gepland.
- [ ] Effect gecontroleerd over passende periode; acties afgesloten.

## Change Management

Het CRQ beschrijft waarom de verandering nodig is, scope, afhankelijkheden, risico, security/data-impact, uitvoerders, test/acceptatie, window en recovery. Goedkeuring door bevoegd persoon; geen aangenomen CAB bij ICO. Emergency change kan sneller maar vereist echte procedure en latere registratie. Een incident geeft geen onbeperkt wijzigingsmandaat.

- [ ] Businessdoel, in/out scope en acceptatiecriteria duidelijk.
- [ ] Componenten/locaties/partners en afhankelijkheden beoordeeld.
- [ ] Capaciteit, budget, eigenaar en goedkeuring bekend.
- [ ] Testbewijs, opleiding en communicatie beschikbaar.
- [ ] Uitrol- en herstelplan haalbaar, inclusief database/data.
- [ ] Go/no-go en stopcriteria afgesproken; nazorg ingepland.

## Release Management

Een release bundelt compatibele wijzigingen. Versieboekhouding voorkomt dat partnerconfiguratie en databaseapplicatie elkaar niet begrijpen. Kies het window met business; niet automatisch elke vrijdag. Neem opleiding, supportoverdracht en bekende beperkingen op.

- [ ] Manifest: app-, mapping-, schema- en configversies.
- [ ] Testresultaten en gebruikersacceptatie gekoppeld.
- [ ] Afhankelijkheden, leveranciers en bereikbaarheid bevestigd.
- [ ] Release notes, supportinstructie en bekende issues klaar.
- [ ] Recovery gerepeteerd of expliciet beperkt met besluit.
- [ ] Productievalidatie en monitorperiode met owner.

## Deployment Management

Deployment is de technische uitvoering. Een technisch succesvolle plaatsing kan functioneel falen door verkeerde config. Test een end-to-end taak. Bij onomkeerbare datamigratie is rollback misschien geen simpele optie; een forward fix of restore/replay vergt een afzonderlijk plan met verlies/duplicaarrisico.

- [ ] Juiste artefact en targetomgeving gecontroleerd.
- [ ] Config/geheimen buiten code, rechten beperkt.
- [ ] Backup/herstelbeschikbaarheid door owner bevestigd.
- [ ] Uitvoering per stap met tijd, verantwoordelijke en uitkomst.
- [ ] Healthcheck én business-smoke test geslaagd.
- [ ] Data/integraties gemonitord; handover afgerond.

<a id="12"></a>

# DEEL 12 — Requirements naar technische oplossing

**Waarschijnlijk / afgeleid uit functiecontext — volledig oefenvoorbeeld.**

## Businessvraag

“Wij willen de voertuiglocatie sneller corrigeren.” Niet meteen een knop bouwen. Probleem begrijpen → stakeholders → huidige situatie → gewenste situatie → requirements → functionele analyse → technische analyse → impactanalyse → implementatie → test → release → nazorg.

1. **Probleem begrijpen:** vraag drie voorbeelden met tijdverlies. Is de fysieke locatie verkeerd geregistreerd, een bericht te laat, of het rapport oud? Stel geen UI-oplossing voor voordat de oorzaak van gebruikerswerk duidelijk is.
2. **Stakeholders:** operationele eigenaar beslist over regels; key user demonstreert; IT behandelt keten/security; partner bevestigt downstreamstatus. Rolbenamingen fictief.
3. **Huidige situatie:** correctieverzoek via e-mail, dubbele invoer, onduidelijke audit. Dit is een scenario, geen ICO-feit.
4. **Gewenste situatie:** bevoegde gebruiker kan geverifieerde locatie met reden corrigeren zonder historie te wissen. Meet doel pas nadat baseline bekend is.
5. **Requirements:** rolbeperking, geldige locatie, huidige versie vergelijken, reden verplicht, oude/nieuwe waarde/actor/tijd auditen, partnercommunicatie indien proces dat vraagt, veilige retry.

## Functionele analyse

| ID | Requirement | Acceptatiecriterium |
|---|---|---|
| F1 | Alleen bevoegde rol corrigeert | Een onbevoegde serverrequest wordt geweigerd, ook buiten de UI |
| F2 | Geldige actieve locatie | Ongeldige/inactieve code faalt zonder datamutatie |
| F3 | Concurrente wijziging detecteren | Update op oude recordversie vraagt herladen, geen silent overwrite |
| F4 | Reden en audit | Succes toont oude/nieuwe locatie en append-only auditrecord in demo |
| F5 | Ketenconsistentie | Eén correctie geeft maximaal één business-effect bij dubbele verzending |
| F6 | Functionele gebruikersfeedback | Mislukking toont geen vals succes en laat hernieuwde controle toe |

## Technische analyse

Hypothetisch: portal/APEX-formulier → server-side validatie → Oracle-transactie → audit en outbox-record → integratieverwerking. Outbox is een ontwerpoptie voor atomiciteit, niet een genoemde ICO-component. Alternatief is bestaande TOS-API; kies die als direct databasebeheer eigenaarschap schendt. Leg beslissing vast. APEX-JBoss-ORDS-topology eerst bevestigen.

## Impact en werkpakketten

W1 procesregels/rolmatrix; W2 schema/contract; W3 UI/serverlogica; W4 integratie/audit; W5 tests/opleiding; W6 deployment/nazorg. Elke taak krijgt owner, afhankelijkheid, raming en opleverbewijs. Risico’s: operationele bevoegdheid, concurrente correctie, partnerduplicaten en gegevensmigratie. Bij overschrijding presenteer je minder scope, later window of extra capaciteit met gevolgen.

## Test, release en nazorg

Test bevoegd/onbevoegd, geldige/ongeldige locatie, gelijktijdige update, timeout vóór/na commit, duplicate message en rollbackbeperking. Laat key user echte taak met synthetische data uitvoeren. Release met pilot en supportinstructie als de interne procedure dat toelaat. Nazorg vergelijkt audit, integratie en gebruikersfeedback. Succes = juiste handeling, juiste data, juiste rechten, begrijpelijke instructie en aantoonbare ketenuitkomst.

## Interviewuitleg

“Ik begin bij het werkprobleem. Ik maak businessregels expliciet en vertaal ze naar positieve en negatieve acceptatiecriteria. Ik kies een oplossing die de bestaande systeemgrenzen respecteert. Ik plan implementatie, gebruikersacceptatie en herstel samen; live zetten is niet het einde van de opdracht.”

<a id="13"></a>

# DEEL 13 — Stakeholder management

**Expliciet uit vacature:** contacten met business units, projectcoördinator, developmentteam, Service Desk, IT-leiding, leveranciers en klanten. **Waarschijnlijk / afgeleid:** aparte security/infra/BA/PM-rollen; ze kunnen door dezelfde mensen ingevuld worden.

| Stakeholder | Communiceer zo | Vraag / oplevering |
|---|---|---|
| Eindgebruiker/key user | Taak, stappen, verwacht/werkelijk, workaround in gewone taal | Toon één echt voorbeeld en valideer de taak na herstel |
| Operations | Impact op fysieke proces, planning en veiligheid | Wat mag doorgaan? Wie beslist over tijdelijke werkwijze? |
| Management/IT-leiding | Resultaat, risico, capaciteit/budget en besluit | Geef 2 opties met gevolgen; geen logdump |
| Developer | Repro, contract, input/output en acceptance | Testbare specificatie; techniekreview met bewijs |
| Infrastructuur/DBA | Tijdlijn, resource-indicatoren, foutcodes, scope | Vraag gerichte meting of actie, geen “server stuk” |
| Security | Data, blootstelling, rechten en logging | Leg minimale toegang en incidentcontainment voor |
| Leverancier | Versie, geredigeerde payload, contract en grensbewijs | Owner, analyse, fix/testbewijs en volgende update |
| Klant | Bevestigde externe impact en betrouwbare status | Intern afstemmen wie klantcommunicatie voert |
| BA/projectcoördinator/PM | Scope, afhankelijkheden, acceptatie en planning | Besluit-/actielog met eigenaar en datum |

## Moeilijke situaties

**Business wil “nu gewoon de data aanpassen”.** “Ik begrijp dat de planning blokkeert. Eerst controleren we welke bron en downstreamsystemen geraakt worden. Een goedgekeurde correctie met audit en reconciliatie kan; ik wil voorkomen dat we later tegenstrijdige statussen hebben.”

**Leverancier zegt “bij jullie”.** “Onze ontvangstlog bevat bericht-ID 42 om 10:04 UTC; de validatie meldt veld X onjuist onder contractversie 3. Kunnen jullie hetzelfde ID aan jullie kant volgen? We testen samen de grens, dan kiezen we de eigenaar op bewijs.” Geen schuldspel.

**Management verwacht een exacte ETA zonder diagnose.** “Herstelduur is nog onzeker. In de komende 20 minuten testen we twee hypotheses. De huidige impact is één partnerstroom; de andere zijn gecontroleerd. Om 11:00 volgt een update met beslissing en resterend risico.”

**Developer en gebruiker spreken elkaar tegen.** Speel de handeling terug met dezelfde testdata. Leg verwacht resultaat vast; vraag operationele proceseigenaar om het businessbesluit en technicus om haalbaarheid. Een technische voorkeur is geen businessregel.

**Taalbarrière.** Vat kort samen, gebruik vaste termen en schriftelijke actiepunten. N/E/F vermoedelijk Nederlands/Engels/Frans; test je niveau met een incidentupdate en vraag welke vaardigheid vereist is.

## Compact statusformat

Resultaat deze week; open risico/impact; budget/capaciteit versus forecast; besluit nodig met opties; volgende stap/eigenaar/datum. Scheid “klaar met bouwen” van “geaccepteerd” en “productie gevalideerd”.

<a id="14"></a>

# DEEL 14 — 25 praktijkscenario’s

**Waarschijnlijk / afgeleid uit functiecontext.** Oefencases in toenemende complexiteit. De app laat je eerst zelf antwoorden, daarna een rubric en modelaanpak bekijken. Er is geen AI-beoordeling: je vergelijkt eerlijk je eigen aanpak met vier criteria. Productie-ingrepen vereisen intern mandaat. De genoemde diagnoses zijn hypotheses, geen vastgestelde root causes.

Gebruik: beschrijf eerste vijf minuten, nodige bewijs, herstelrisico en communicatie. Beoordeel vervolgens ieder rubricpunt en noteer één verbeteractie. Alleen lezen is geen praktische beheersing.


## 01. Eén gebruiker kan niet inloggen — Basis

Vacaturekoppeling: R21/R25/R32. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Om 08:40 meldt een operator dat het portaal toegang weigert; een collega lijkt wel te kunnen werken.

**Wat weet ik?:** Eén melding en een loginfout, niet bewezen sitebrede uitval.

**Wat weet ik niet?:** Foutcode, rol, accountstatus, omgeving en of andere accounts hetzelfde probleem hebben.

**Eerste vragen / controles:** Sinds wanneer, welk scherm/bericht, account of device, recent wachtwoord/rol gewijzigd?

**Mogelijke oorzaken:** Verlopen account/sessie, verkeerde loginroute, rolprobleem, lokale browsercache of identitydienst.

**Logs / bewijs:** Tijd, geredigeerde account-ID, auth-fout en servercorrelatie. Geen wachtwoord loggen.

**Database:** Applicatierol/scope vergelijken met goedgekeurde matrix; geen eigen productie-accounttabel aanpassen.

**Netwerk:** Alleen relevant als endpoint/authdienst niet bereikt wordt; vergelijk dezelfde URL vanaf twee devices.

**Applicatie:** Onderscheid 401/authenticatie van 403/toestemming; niet blind admin geven.

**Integratie:** SSO is onbekend; als gebruikt, laat identityowner hetzelfde request volgen.

**Mijn aanpak:** Impact bevestigen → vergelijken met werkend account → auth versus rechten isoleren → gericht herstellen.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: account is juist geauthenticeerd maar ontbreekt in operatorrol; bevestigen in serverlog/rolmatrix.

**Oplossing:** Bevoegde eigenaar corrigeert de goedgekeurde rol; nieuwe sessie en echte taak testen.

**Communicatie:** Zeg welke taak geblokkeerd is, wat nog werkt en volgende update; accountdetails alleen aan bevoegde groep.

**Preventie:** Onboarding/rolwijziging met acceptatietest en duidelijke identity-escalatie.

**Goed genoeg / rubric:** Impact en scope; Authenticatie versus autorisatie; Least privilege; Functionele hercontrole.

## 02. Portaal toont oude informatie — Basis

Vacaturekoppeling: R21/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een status lijkt oud in het portaal, maar operations zegt dat de handeling net verwerkt is.

**Wat weet ik?:** Eén weergaveverschil.

**Wat weet ik niet?:** Of bronrecord actueel is, refresh/caching en tijdzone.

**Eerste vragen / controles:** Welke sleutel, verwacht event, eventtijd of verwerkingstijd, andere gebruiker/weergave?

**Mogelijke oorzaken:** Cache, vertraagde verwerking, rapportrefresh of verkeerde scope.

**Logs / bewijs:** Request-ID/tijd en laatste succesvolle verwerking van dezelfde sleutel.

**Database:** Read-only bronstatus en update/eventtijd vergelijken met portaalquery.

**Netwerk:** Geen brede netwerkdiagnose zonder timeout; controleer request/response indien stale cache vermoed.

**Applicatie:** Parameters, cachepolicy en rolfilter vergelijken. Refresh bewijst geen oorzaak.

**Integratie:** Check of bericht alleen ontvangen of werkelijk gecommit is.

**Mijn aanpak:** Zelfde sleutel en tijd → bron vergelijken → keten of weergave isoleren.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: bron klopt maar endpoint gebruikt een oude snapshot; test cacheversie en refresh.

**Oplossing:** Cache/refresh via eigenaar corrigeren of verwerking herstellen; gebruiker laat taak opnieuw uitvoeren.

**Communicatie:** Maak duidelijk of fysieke registratie goed is en welk scherm achterloopt.

**Preventie:** Timestamp/refresh zichtbaar maken en freshnessmonitor toevoegen.

**Goed genoeg / rubric:** Bron van waarheid; Tijd en refresh; Geen onnodige mutatie; Gebruikersvalidatie.

## 03. Rapportexport bevat verkeerde telling — Basis

Vacaturekoppeling: R20/R30. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een WebFOCUS-rapport en Excel-export tonen een ander voertuigaantal.

**Wat weet ik?:** Twee verschillende uitkomsten, nog geen bewijs van dataverlies.

**Wat weet ik niet?:** Definities, filters, tijdzone, refresh en unieke sleutel.

**Eerste vragen / controles:** Tellen we voertuigen of events? Dezelfde locaties, datumgrenzen en autorisatie?

**Mogelijke oorzaken:** One-to-many join, verkeerde filter, exportlimiet, stale refresh of spreadsheetformule.

**Logs / bewijs:** Rapportparameters, queryversie, refreshmoment en exportmetadata.

**Database:** Verschilset op businesssleutel; join-cardinaliteit en nulls controleren.

**Netwerk:** Pas controleren bij afgebroken export/timeout; geen eerste hypothese.

**Applicatie:** Dezelfde report-versie/parameters en scope testen.

**Integratie:** Controleer bronrefresh indien rapport op downstreamdataset draait.

**Mijn aanpak:** Definitie aligneren → dezelfde snapshot → verschillen per sleutel → query/export isoleren.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: rapport telt eventregels in plaats van unieke voertuigen; bevestigen via kardinaliteit.

**Oplossing:** Definitie/query corrigeren via change; verwacht resultaat door business laten bevestigen.

**Communicatie:** Meld cijferimpact zonder direct “database fout” te zeggen; corrigeer eerder verspreid rapport indien nodig.

**Preventie:** Rapportdatacontract, referentieset en formulecontrole.

**Goed genoeg / rubric:** Definitie en scope; Sleutelreconciliatie; Join-cardinaliteit; Businessacceptatie.

## 04. Onduidelijke businessvraag — Basis

Vacaturekoppeling: R11/R12. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Business vraagt “maak het scherm sneller” en wil een raming morgen.

**Wat weet ik?:** Er is een klacht, geen meetbaar probleem.

**Wat weet ik niet?:** Welke taak, baseline, volume, uitzonderingen en deadline.

**Eerste vragen / controles:** Welke stap kost tijd, wanneer, voor wie, welke vertraging en wat gebeurt bij niets doen?

**Mogelijke oorzaken:** Trage query, onhandige workflow, dubbele invoer of onrealistische verwachting.

**Logs / bewijs:** Taakduur en requesttimings pas verzamelen na concrete repro.

**Database:** Onderzoeken als een query de taak bottleneck blijkt; niet direct index voorstellen.

**Netwerk:** Latentie tussen locatie en server meten indien scope daarnaar wijst.

**Applicatie:** Observeer gebruiker; scheid klikaantal, responstijd en wachttijd.

**Integratie:** Check of UI op partnerstatus wacht, waardoor snelle frontend niets oplost.

**Mijn aanpak:** Observeer drie taken → probleemzin → doel/constraints → opties → kleine gevalideerde raming.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: dubbele invoer kost meer tijd dan technische latentie; meet beide.

**Oplossing:** Werkpakket voor taakverbetering met acceptatiecriteria en expliciete aannames.

**Communicatie:** Geef bandbreedte met onbekenden en datum waarop raming verfijnd wordt.

**Preventie:** Intakeformat en key-useracceptatie voor iedere CRQ.

**Goed genoeg / rubric:** Probleem vóór oplossing; Taakobservatie; Meetbare acceptance; Raming met onzekerheid.

## 05. Nieuwkomer moet portaal leren — Basis

Vacaturekoppeling: R14/R27. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een nieuwe medewerker kent de taak niet en gebruikt een oude handleiding.

**Wat weet ik?:** Documentatie bestaat maar versie en begrip zijn onzeker.

**Wat weet ik niet?:** Rechten, huidige flow, uitzonderingen en aanspreekpunt.

**Eerste vragen / controles:** Welke echte taak moet zelfstandig lukken, welke fouten komen voor, wie bevestigt de procedure?

**Mogelijke oorzaken:** Oude instructie, te veel jargon, geen oefening of ontbrekende toegang.

**Logs / bewijs:** Geen productielogs nodig voor training; leg labstappen/resultaten vast.

**Database:** Synthetische testdata; geen echte klantgegevens kopiëren.

**Netwerk:** Toegang en juiste omgeving testen vóór sessie.

**Applicatie:** Actuele schermflow en rol aansluiten op instructie.

**Integratie:** Leg externe afhankelijkheid uit zonder live partneractie uit te voeren.

**Mijn aanpak:** Doel afbakenen → toegang → demo → deelnemer oefent → teach-back → feedback.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: instructie hoort bij vorige release; verifieer manifest/screens.

**Oplossing:** Quick guide updaten met eigenaar/versie; deelnemer doorloopt happy en foutpad.

**Communicatie:** Noem helpkanaal en wat gebruiker bij fout wel/niet moet herhalen.

**Preventie:** Training koppelen aan release en terugkerende feedbackreview.

**Goed genoeg / rubric:** Taakgericht doel; Veilige testomgeving; Teach-back; Versiebeheer instructie.

## 06. API geeft serverfout — Intermediate

Vacaturekoppeling: R22/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een portalactie geeft HTTP 500 voor één type aanvraag; andere acties slagen.

**Wat weet ik?:** Serverantwoord is fout, niet dat het hele platform uitligt.

**Wat weet ik niet?:** Payloadvariant, eerste fout, commitstatus en recente changes.

**Eerste vragen / controles:** Welke actie, welke input, sinds wanneer, request-ID, gebeurt hetzelfde bij alle records?

**Mogelijke oorzaken:** Null/validatiefout, constraint, code-exception of downstreamfout.

**Logs / bewijs:** Request-ID, exceptionketen en laatste change, met secrets gemaskeerd.

**Database:** Zoek businessresultaat en constraintfout read-only; commitstatus vóór retry.

**Netwerk:** 500 bewijst bereikbaar applicatiepad; downstreamconnectiviteit kan wel falen.

**Applicatie:** Reproduceer input in test, vergelijk runtime/config en foutafhandeling.

**Integratie:** Contractversie/downstreamresponse controleren als fout door externe service komt.

**Mijn aanpak:** Scope → first exception → input vergelijken → commitstatus → veilige repro → fix/test.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: onbekende status wordt onjuist als null verwerkt; bevestig reproduceerbare exception.

**Oplossing:** Validatie/foutpad verbeteren en alleen veilige requests herhalen; geen bulk retry.

**Communicatie:** Meld getroffen actie en veilige workaround, niet een onbewezen gehele uitval.

**Preventie:** Negatieve contracttests en logging van eerste foutgrens.

**Goed genoeg / rubric:** Scope en correlatie; Eerste exception; Commit vóór retry; Negatieve regressietest.

## 07. EDI-bericht geweigerd — Intermediate

Vacaturekoppeling: R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Eén partnerbericht bereikt middleware maar wordt afgewezen; 18 vergelijkbare berichten wachten.

**Wat weet ik?:** Transportreceipt bestaat; businessacceptatie niet.

**Wat weet ik niet?:** Foutveld, mappingversie, partnercontract en partial processing.

**Eerste vragen / controles:** Welke ID’s, nieuwe formaatvariant, laatste goede sample, contractwijziging aangekondigd?

**Mogelijke oorzaken:** Datum/encoding, onbekende code, verplichte waarde ontbreekt of mappingversie verkeerd.

**Logs / bewijs:** Transport-ID, parser/validationlog, mappingversie, foutveld; geredigeerde payload.

**Database:** Check unieke businesssleutel en eventuele gedeeltelijke commit.

**Netwerk:** Transport werkt voor sample; pas verder testen als receipt onvolledig is.

**Applicatie:** Controleer semantische businessvalidatie na syntax.

**Integratie:** Vergelijk input/output per stap en technisch versus functioneel ACK.

**Mijn aanpak:** Contract vergelijken → foutveld isoleren → representatieve test → correctie → controlled replay.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: partner levert nieuwe datumvariant; onderscheid fout contract versus mapping.

**Oplossing:** Partner corrigeren of geautoriseerde mappingchange; replay pas na duplicate-check en reconciliatie.

**Communicatie:** Geef partner dezelfde ID/tijd en concreet contractverschil; business krijgt impact/volume.

**Preventie:** Contractversiebeheer, sampletests en schema-validatie.

**Goed genoeg / rubric:** Transport versus verwerking; Contractbewijs; Partial commit/duplicaten; Veilige replay.

## 08. Databasequery is traag — Intermediate

Vacaturekoppeling: R19/R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een specifieke zoekactie duurt 20 seconden in de demo; de vorige testbaseline was 2 seconden.

**Wat weet ik?:** Taak is trager onder bepaalde input; cijfers zijn fictief.

**Wat weet ik niet?:** Queryplan, locks, volume, parameters, concurrency en configchange.

**Eerste vragen / controles:** Alle zoekacties of één filter, piekmoment, laatste wijziging, hoeveel records?

**Mogelijke oorzaken:** Verkeerd queryplan, meer volume, missing/poor index, lock, poolwait of onbegrensde export.

**Logs / bewijs:** Requesttiming splitsen in poolwait/query/render; query-ID en parameters volgens privacybeleid.

**Database:** DBA plan/locks laten bekijken; row count en selectiviteit vergelijken met baseline.

**Netwerk:** Meet alleen als server/DB-roundtrip afwijkend is; onderscheid querytijd van netwerktijd.

**Applicatie:** Parameter/ORM-query en pagina-limit vergelijken; geen onbewezen tuning.

**Integratie:** Batchbelasting of partnerburst kan load toevoegen; correleer tijd.

**Mijn aanpak:** Baseline → concrete repro → laag-timings → DBA evidence → meet één wijziging.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: filter ontbreekt in nieuwe query; bewijs via rows/plan, niet alleen CPU.

**Oplossing:** Gerichte queryfix en review/test; index of capacity alleen met eigenaar/impactanalyse.

**Communicatie:** Meld taak/volume/temporary limit en geen prestatiebelofte zonder meting.

**Preventie:** Representatieve performancetest, querylimits en trendmonitor.

**Goed genoeg / rubric:** Baseline en parameters; Pool versus querytijd; DBA/plan evidence; Voor/nameting.

## 09. JBoss kan niet verbinden met database — Intermediate

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Na configuratiewijziging starten applicaties maar transacties geven datasource-fouten.

**Wat weet ik?:** Runtime start; businesshandeling faalt.

**Wat weet ik niet?:** Credentials, endpoint, pool, DB-status en juiste targetomgeving.

**Eerste vragen / controles:** Alle apps/hosts, sinds welke change, eerste foutcode, welk datasourceprofiel?

**Mogelijke oorzaken:** Verkeerd endpoint/secret, DB niet bereikbaar, auth geweigerd of poolconfig.

**Logs / bewijs:** Datasource/JDBC-fout, configrelease, server/starttijd; credentialwaarden nooit tonen.

**Database:** DB-eigenaar controleert listener/auth/service en geschikte sessies.

**Netwerk:** Resolutie/poort en werkelijke DB-service testen door bevoegd team.

**Applicatie:** Vergelijk config met goedgekeurde omgeving; health endpoint is onvoldoende.

**Integratie:** Andere DB-afhankelijke flows als impactgrens vergelijken.

**Mijn aanpak:** Recent change → configdiff zonder secrets → netwerk/auth/pool onderscheiden → herstel.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: testendpoint in productieconfig; bewijs via manifest/configkey.

**Oplossing:** Goedgekeurde config terugzetten of corrigeren; business-smoke en integratiecontrole.

**Communicatie:** Informeer over transacties die wel/niet werken en veilige retryvoorwaarden.

**Preventie:** Omgevingsvalidatie, secretreferenties en dependency healthcheck.

**Goed genoeg / rubric:** Business-smoke; Secretveilig configbewijs; Netwerk/auth onderscheiden; Gecontroleerde restore.

## 10. AIX-filesystem vol — Intermediate

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Verwerking stopt met write-fouten; een beheerder meldt 100% bezetting van een filesystem.

**Wat weet ik?:** Schrijfprobleem en capaciteitssignaal; locatie/data-inhoud nog onbekend.

**Wat weet ik niet?:** Welke files, retentie, andere services en veilige opruimoptie.

**Eerste vragen / controles:** Welk mount/path, groeisnelheid, sinds wanneer, vereist audit/berichtarchief, wie beheert opslag?

**Mogelijke oorzaken:** Loggroei, grote batch, retentiejob faalt of tijdelijke bestanden blijven staan.

**Logs / bewijs:** Write exception, disktrend, retentiescheduler en recente volumenverandering.

**Database:** Controleer of commit al gedaan is en alleen export/ACK faalt; DB-files nooit blind verwijderen.

**Netwerk:** Niet eerste oorzaak; downstreamretries kunnen extra volume opleveren.

**Applicatie:** Welke uitvoer faalt, wat is opnieuw uitvoerbaar en wat moet bewaard?

**Integratie:** Blokkeer ongecontroleerde replay; check output versus gecommitteerde data.

**Mijn aanpak:** Owner → impact → evidence bewaren → retentie/capaciteitplan → controlled herstel.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: logging is gegroeid na debugchange; bevestig zonder auditverlies.

**Oplossing:** Bevoegd beheerder archiveert/roteert volgens beleid of breidt capaciteit uit; app/businessflow testen.

**Communicatie:** Zeg dat herstelplan databehoud omvat; geen “we verwijderen alles” shortcut.

**Preventie:** Diskthreshold, groeitrend, retentietest en debug-einddatum.

**Goed genoeg / rubric:** Geen blind verwijderen; Eigenaarschap opslag; Commit/replay check; Groei en retentie.

## 11. Dubbel verwerkt partnerbericht — Intermediate

Vacaturekoppeling: R20/R22/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een partner verstuurt dezelfde aankomst twee keer; er verschijnen dubbele events.

**Wat weet ik?:** Dubbele input; dubbele business-effecten vermoed.

**Wat weet ik niet?:** Message-ID versus businesssleutel, commit/ACK, impact op rapport en operatie.

**Eerste vragen / controles:** Zijn IDs gelijk, is hetzelfde business-event opnieuw verpakt, welke verwerking is correct?

**Mogelijke oorzaken:** Retry na ontbrekend ACK, deduplicatie op verkeerde sleutel, niet-atomische check/insert.

**Logs / bewijs:** Ontvangst, dedupbesluit, commit en ACK per ID met timestamps.

**Database:** Unieke keys en audit vergelijken; race/transactionboundary bekijken met developer/DBA.

**Netwerk:** Timeout kan trigger zijn; transportprobleem is niet hele oorzaak.

**Applicatie:** Idempotentie moet ook bij concurrente verzending werken.

**Integratie:** Bespreek retrycontract en betekenis van IDs met partner.

**Mijn aanpak:** Effect inventariseren → bron-event bepalen → oorzaak retry/dedup → veilige correctie.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ieder retry krijgt nieuw transport-ID maar dezelfde eventkey.

**Oplossing:** Unique business-eventkey en atomische verwerking via change; correctie met audit en downstreamreconciliatie.

**Communicatie:** Meld dat ontvangst dubbels normaal kan zijn, dubbel effect niet; correctie-impact afstemmen.

**Preventie:** Concurrency/duplicate/timeout-regressietests en dedupmonitor.

**Goed genoeg / rubric:** Businesssleutel versus transport-ID; Atomiciteit; Auditcorrectie; Concurrency test.

## 12. Ontbrekend ACK na succesvolle commit — Intermediate

Vacaturekoppeling: R20/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Partner zegt “niet ontvangen”; intern lijkt event wel verwerkt.

**Wat weet ik?:** Intern record bestaat; partnerstatus onduidelijk.

**Wat weet ik niet?:** Welke ACK-semantiek, verzendstatus, correlation en retryrisico.

**Eerste vragen / controles:** Welk event, welk expected ACK, sinds wanneer, partner ontvangt andere confirmations?

**Mogelijke oorzaken:** ACK-export mislukt, transporttimeout, partnerfilter of mismatch referentie.

**Logs / bewijs:** Commit en outbound ACKlog op dezelfde correlation/businesskey.

**Database:** Bewijs unieke commit; geen event opnieuw aanmaken om ACK te forceren.

**Netwerk:** Retourpad/TLS/credential en beide tijdlijnen vergelijken.

**Applicatie:** Controleren of ACK los van businessverwerking veilig opnieuw te sturen is.

**Integratie:** Partner vraagt bestaande bevestiging/replaycontract, geen volledige re-import.

**Mijn aanpak:** Commitstatus bewijzen → outbound-grens isoleren → bevestiging gecontroleerd herverzenden.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ACKsend timeout na commit; check outboundqueue en partnerreceipt.

**Oplossing:** Alleen bevestiging opnieuw sturen volgens contract; event niet opnieuw verwerken.

**Communicatie:** Bevestig intern resultaat met minimale gegevens en test ontvangst samen.

**Preventie:** Duurzame outboundstatus, ACK-retries en end-to-end reconciliatie.

**Goed genoeg / rubric:** Commitbewijs; ACK-semantiek; Geen dubbel event; Partnerreceipt controleren.

## 13. Locatiecode onbekend in mapping — Intermediate

Vacaturekoppeling: R20/R35. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Berichten uit Kallo slagen, dezelfde nieuwe code uit Zeebrugge faalt.

**Wat weet ik?:** Locatie-/codegebonden scope.

**Wat weet ik niet?:** Siteconfig, masterdataowner en officiële code.

**Eerste vragen / controles:** Welke code, bij wie geldig, mapping per vestiging, wijziging aangekondigd?

**Mogelijke oorzaken:** Masterdata niet gesynchroniseerd, hardcoded mapping, verkeerde siteconfig.

**Logs / bewijs:** Site, code, mappingversie en rejected reason.

**Database:** Locatiemasterdata en geldigheid read-only vergelijken, niet ter plaatse fictieve code maken.

**Netwerk:** Netwerk is minder waarschijnlijk als andere siteberichten langs zelfde pad slagen.

**Applicatie:** Sitevarianten en businessregels beoordelen.

**Integratie:** Contract/codecatalogus en partnerwijziging afstemmen.

**Mijn aanpak:** Codebron bepalen → siteconfig vergelijken → impact → geautoriseerde mapping/masterdatachange.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: code geldig, één mappingcatalogus loopt achter; bewijs van owner nodig.

**Oplossing:** Catalogusupdate met beide-site tests en controlled replay.

**Communicatie:** Geef partner/operations concrete affected codes en backlog, zonder verkeerde fysieke locatie toe te kennen.

**Preventie:** Masterdatagovernance, synchronisatiecheck en site-tests.

**Goed genoeg / rubric:** Site scope; Masterdata-eigenaar; Geen fictieve code; Beide locaties testen.

## 14. TLS-certificaat verlopen — Intermediate

Vacaturekoppeling: R21/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een partnerendpoint faalt sinds middernacht met handshake error.

**Wat weet ik?:** TLS-fout vóór businessresponse.

**Wat weet ik niet?:** Certificaatkant, trustchain, expiry, gewijzigde hostname en andere consumers.

**Eerste vragen / controles:** Welk endpoint, welke chain, laatste goede verbinding, is renewal geweest?

**Mogelijke oorzaken:** Expiry, incomplete chain, truststore verouderd, hostname mismatch of klokprobleem.

**Logs / bewijs:** TLS-fout/expiry/hostname zonder secrets, requesttijd en deploymentconfig.

**Database:** Geen DB-mutatie nodig; check eventueel reeds gecommitteerde queuevoorraad.

**Netwerk:** Bevoegde eigenaar controleert cert/chain/time en relevante endpointroute.

**Applicatie:** Truststoreconfig kan runtimecomponent zijn; tijdelijke trust-all is onveilig.

**Integratie:** Partner bevestigt certwisseling en test hetzelfde endpoint.

**Mijn aanpak:** Certkant identificeren → owner → juiste chain/renewal → test → backlog veilig verwerken.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: partner renewal zonder volledige chain; bewijs via chainvergelijking.

**Oplossing:** Correct certificaat/chain of trustconfig geautoriseerd plaatsen; verificatie nooit uitschakelen.

**Communicatie:** Meld welke stroom blokkeert en plan/volgende update; geen ongefundeerde cyberclaim.

**Preventie:** Expiry-alert, contactlijst en renewalrepetitie.

**Goed genoeg / rubric:** TLS laag; Chain/hostname/time; Geen trust-all; Renewalmonitor.

## 15. Release faalt halverwege — Gevorderd

Vacaturekoppeling: R18/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** App is vernieuwd maar schema-migratie stopt; portaal geeft inconsistent gedrag.

**Wat weet ik?:** Versiemix en gedeeltelijke uitvoering.

**Wat weet ik niet?:** Migratiestappen, irreversible data, oude versiecompatibiliteit, impact.

**Eerste vragen / controles:** Welke stappen geslaagd, transactioneel of niet, huidige schema, herstelbewijs?

**Mogelijke oorzaken:** Migratiefout, ontbrekende permissie, onverwachte data of uitvoervolgorde.

**Logs / bewijs:** Deploymentmanifest, migrationlog, timestamp en first failure.

**Database:** DBA schema/data-status vergelijken met plan; geen blind restore over nieuwe data.

**Netwerk:** Alleen relevant als deployverbinding faalde; eerst state inventory.

**Applicatie:** App/schemaversies en compatibiliteit vaststellen.

**Integratie:** Partners in-/outbound veilig pauzeren als procedure vereist om mixed states te beperken.

**Mijn aanpak:** Stop verdere changes → state inventariseren → go/no-go owner → rollback/forward fix beoordelen.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: migration faalt op onverwachte null-data na eerdere schemawijziging.

**Oplossing:** Gerepeteerd recoverypad of goedgekeurde forward fix; daarna business/data/partnerchecks.

**Communicatie:** Meld precies welke versiestappen klaar zijn en wat onzeker is; updates door één incidentowner.

**Preventie:** Production-like dataset, prereq-check en recoveryrepetitie.

**Goed genoeg / rubric:** Stop en state inventory; Schema/data recovery; Go/no-go owner; End-to-end validatie.

## 16. Leverancier wijst naar ons — Gevorderd

Vacaturekoppeling: R07/R25/R33. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Integratiepartner zegt dat netwerk bij ICO fout is, intern zegt men dat payload fout is.

**Wat weet ik?:** Twee meningen, geen gezamenlijk bewijs.

**Wat weet ik niet?:** Exacte foutgrens en gedeelde correlatie/tijdzone.

**Eerste vragen / controles:** Welk ID, wat verzonden/ontvangen, welke timestamps, contractversie en fout?

**Mogelijke oorzaken:** Echte netwerkfout, payloadreject, timezoneverwarring of ontbreken van grenslogging.

**Logs / bewijs:** Evidence pack met ID, geredigeerd input/output, tijd/zone en eerste error.

**Database:** Businesscommit controleren om retries niet te verdubbelen.

**Netwerk:** Verzend-/ontvangstbewijs naast elkaar; bereikbaarheid test is niet payloadacceptatie.

**Applicatie:** Verwerkingsfout en release/configversie demonstreren.

**Integratie:** Samen één sample langs beide grenzen volgen.

**Mijn aanpak:** Gezamenlijke grens-test plannen, rollen verdelen, feiten/taken noteren, escaleren op ontbrekend ownership.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ontvangst slaagt en validation reject is aantoonbaar; netwerkclaim daarmee voor dit sample weerlegd.

**Oplossing:** Owner op bewijs aanwijzen en testbare fix opleveren; eigen monitoringgat eveneens verbeteren.

**Communicatie:** Neutraal: “bewijs A/B, onbekend C, actie X door Y vóór Z”.

**Preventie:** Contract, shared correlation en escalatieafspraken.

**Goed genoeg / rubric:** Feiten vóór schuld; Gezamenlijke sample; Ketenbewijs; Owner en deadline.

## 17. Twee urgente projecten concurreren — Gevorderd

Vacaturekoppeling: R16/R23/R24. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Business A wil release deze week, business B heeft verplichte partnerwijziging; dezelfde leverancier doet beide.

**Wat weet ik?:** Capaciteitsconflict.

**Wat weet ik niet?:** Deadlinehardheid, risico, minimale scope, afhankelijkheden en beslisrecht.

**Eerste vragen / controles:** Wat als elk project later komt, welke deadline extern vaststaat, wat is MVP?

**Mogelijke oorzaken:** Overplanning, onzichtbare afhankelijkheid, scopegroei of onvoldoende forecast.

**Logs / bewijs:** Projectactuals/actielog, geen technische logs tenzij incident oorzaak van conflict is.

**Database:** Data-/migratieafhankelijkheden van beide changes onderzoeken.

**Netwerk:** Omgevingsvensters/sitebelasting kunnen releasevolgorde beperken.

**Applicatie:** Compatibiliteit en gezamenlijke componenten bepalen.

**Integratie:** Partnerdeadlines en testresources bevestigen.

**Mijn aanpak:** Impact/urgentie/scope vergelijken → capacity forecast → opties → bevoegd besluit → nieuwe baseline.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: extern contractwindow is hard, wensdatum A onderhandelbaar; verifiëren bij owners.

**Oplossing:** Prioriteit en scope geautoriseerd aanpassen met consequenties, geen stille overurenbelofte.

**Communicatie:** Beide businessunits krijgen hetzelfde besluit en onderbouwde timing.

**Preventie:** Portefeuilleoverzicht, capacitybuffer en vroeg risico-overleg.

**Goed genoeg / rubric:** Impact en hardheid; Capaciteit forecast; Opties met gevolgen; Beslisrecht.

## 18. Budget dreigt te overschrijden — Gevorderd

Vacaturekoppeling: R16/R24/R26. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** 70% budget is gebruikt maar leverancier meldt 50% scope afgerond.

**Wat weet ik?:** Verbruik en scopepercentage passen niet vanzelf samen.

**Wat weet ik niet?:** Definition of done, resterende raming en oorzaak.

**Eerste vragen / controles:** Gebouwd of geaccepteerd, fixed/variable kosten, scopewijzigingen, wat resteert?

**Mogelijke oorzaken:** Onderschatting, scope creep, rework, overhead of onbetrouwbare voortgangsmeting.

**Logs / bewijs:** Uren/facturen, werkpakketstatus en changebesluiten.

**Database:** Niet van toepassing op financiële diagnose; datawerk kan extra kostenbron zijn.

**Netwerk:** Niet van toepassing tenzij infrastructuurkosten deel van project zijn.

**Applicatie:** Opleveringen demonstreren aan acceptancecriteria.

**Integratie:** Partnerafhankelijkheden en extra adapterwerk beoordelen.

**Mijn aanpak:** Actuals verifiëren → remaining effort → estimate at completion → opties en escalatie.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: 50% is gebouwd maar test/nazorg niet geraamd; forecast opnieuw onderbouwen.

**Oplossing:** Scope/tijd/budgetbesluit door bevoegde owner; werkpakketbaseline wijzigen.

**Communicatie:** Geen foutloze eindprijs suggereren: bandbreedte, aannames en besluitdatum.

**Preventie:** Voortgang op accepted deliverables, frequente forecast en scopecontrol.

**Goed genoeg / rubric:** Actual versus accepted; Remaining forecast; Vroeg escaleren; Scopebesluit vastleggen.

## 19. Productie ligt gedeeltelijk plat — Gevorderd

Vacaturekoppeling: R19/R25/R35. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Zeebrugge meldt dat een kritieke taak faalt; Kallo lijkt nog te werken.

**Wat weet ik?:** Locatiegebonden impact, maar omvang nog te bevestigen.

**Wat weet ik niet?:** Veiligheidsimpact, gedeelde componenten, beschikbaar workaround en prioriteit.

**Eerste vragen / controles:** Welke taak/gebruikers, fysieke gevolgen, starttijd, laatste change, andere locaties echt getest?

**Mogelijke oorzaken:** Siteconfig, netwerkroute, lokaal endpoint, gedeelde app met site-specifieke data of load.

**Logs / bewijs:** Site/time/request correlation, first failure en laatste succesvolle taak.

**Database:** Siteparameters en businesskeys vergelijken; geen systeemwijde datawijziging.

**Netwerk:** Route/DNS/endpointverschil als hypothese; eigenaar laten meten.

**Applicatie:** Zelfde transactie op werkende/ falende site met veilige data vergelijken.

**Integratie:** Partnerstromen per site checken en veilige backlogbewaring regelen.

**Mijn aanpak:** Incidentowner → operationsveiligheid → impactmatrix → laatste goede grens → gerichte hersteltest.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: lokale routeconfigwijziging; bewijzen met locatiepad en app-health/data.

**Oplossing:** Geautoriseerde gerichte herstelactie; test beide sites en reconciliatie, voorkom shared component te verstoren.

**Communicatie:** Vaste updates per getroffen businessunit; benoem wat gecontroleerd blijft werken.

**Preventie:** Sitegerichte synthetic/business checks en configreview.

**Goed genoeg / rubric:** Veiligheid en impact; Werkende site als vergelijking; Gerichte actie; Beide-sites validatie.

## 20. Database lock blokkeert verwerking — Gevorderd

Vacaturekoppeling: R19/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Meerdere transacties wachten; een DBA ziet één langlopende blocking session.

**Wat weet ik?:** Lock-relatie, nog geen mandaat om sessie te stoppen.

**Wat weet ik niet?:** Owner, transactie-intentie, rollbackduur en commitstatus.

**Eerste vragen / controles:** Sinds wanneer, welke tabellen/taak, recent batch, kan gecontroleerd beëindigd worden?

**Mogelijke oorzaken:** Langlopende transactie, vergeten commit, batchoverlap of gewijzigde lockvolgorde.

**Logs / bewijs:** Requesttiming, DB-session/lock evidence van DBA, job-owner en batchlog.

**Database:** DBA identificeert blocking/waiting sessies en gevolgen; kill kan lang rollbacken.

**Netwerk:** Niet primaire oorzaak als DB-lock bewezen is; geen firewallwijziging.

**Applicatie:** Transactiegrenzen en timeout/retrygedrag bekijken.

**Integratie:** Retryburst vermijden; downstreamstatus pas na commit beoordelen.

**Mijn aanpak:** Owner/impact → lockbewijs → beheerbesluit → veilig beëindigen/herstellen → data check.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: onderhoudsjob houdt lock; controleer eigenaar en status vóór ingreep.

**Oplossing:** DBA voert goedgekeurde actie uit; code/batchfix via problem/change, met transactie/retrytests.

**Communicatie:** Leg uit dat herstel niet onmiddellijk is als rollback nog loopt.

**Preventie:** Batchvensters, transactieduurmonitor, korte transacties en concurrencytests.

**Goed genoeg / rubric:** DBA bewijs; Geen blind kill; Rollbackimpact; Structurele transactiecontrole.

## 21. Veiligheidsgevoelige statuscorrectie — Gevorderd

Vacaturekoppeling: R09/R21/R25. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Een gebruiker wil een hold verwijderen om vertrek te versnellen, maar reden is onduidelijk.

**Wat weet ik?:** Voorgestelde datawijziging kan fysieke actie beïnvloeden.

**Wat weet ik niet?:** Wie vrijgave mag beslissen en waarom hold bestaat.

**Eerste vragen / controles:** Welke holdsoort, bron, bevoegdheid, fysieke verificatie en downstreamgebruik?

**Mogelijke oorzaken:** Legitieme achterhaalde status, ontbrekende update of verkeerde interpretatie van hold.

**Logs / bewijs:** Audit/history en bron van beslissing, minimale persoonsgegevens.

**Database:** Read-only status/herkomst; geen UPDATE op verzoek alleen.

**Netwerk:** Niet relevant zonder aanwijzing voor ontbrekend bronbericht.

**Applicatie:** Serverautorisatie en geldige transitions beoordelen.

**Integratie:** Partner/businesstoestemming en statusbron vergelijken.

**Mijn aanpak:** Operationele eigenaar inschakelen → feitelijke toestand/verantwoordelijkheid → traceerbare change.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: hold heeft nog geldige grond; IT kan dit niet autonoom opheffen.

**Oplossing:** Alleen bevoegde businessbeslissing uitvoeren via goedgekeurde flow met audit en downstreamcontrole.

**Communicatie:** Erken tijdsdruk maar benoem dat vrijgave een business-/veiligheidsbesluit is.

**Preventie:** Rolmatrix, redenplicht, audit en training statusbetekenis.

**Goed genoeg / rubric:** Fysieke gevolgen; Bevoegde beslissing; Geen ongeautoriseerde update; Audit/ketencontrole.

## 22. Mogelijk datalek in portaal — Gevorderd

Vacaturekoppeling: R21/R25/R09. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Klant A meldt mogelijk een voertuig van klant B in de portal.

**Wat weet ik?:** Mogelijke scopefout; omvang niet vastgesteld.

**Wat weet ik niet?:** Reproduceerbaarheid, data/exposure, betrokken users en ownerprocedure.

**Eerste vragen / controles:** Welke minimaal nodige sleutel, tijd, view, accountscope, sinds welke release?

**Mogelijke oorzaken:** Row-scopefilter fout, cache gedeeld, verkeerde klantmapping of data-eigenaarschap.

**Logs / bewijs:** Audit/access/request-ID veilig bewaren; geen gevoelige screenshots breed verspreiden.

**Database:** Goedgekeurde owner controleert klantrelaties en effectieve scope.

**Netwerk:** Geen evidence dat firewallprobleem; eerst server/data-access.

**Applicatie:** Object-level autorisatie en caching toetsen met veilige testaccounts.

**Integratie:** Partner/masterdata kan verkeerd ownership aanleveren, maar server moet scope afdwingen.

**Mijn aanpak:** Securityowner → minimale evidence → containment door bevoegd team → exposure scope → fix/test.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: ontbrekende serverfilter; alleen na scopebewijs concluderen.

**Oplossing:** Bevoegd team beperkt toegang en corrigeert autorisatie; credential/notificationkeuzes via echte procedure.

**Communicatie:** Intern feitelijk en vertrouwelijk; externe melding door aangewezen verantwoordelijke.

**Preventie:** Negatieve multi-tenant autorisatietests, cacheisolation en audit.

**Goed genoeg / rubric:** Security-escalatie; Minimale bewijsdeling; Objectscope; Containment en regressietest.

## 23. TOS-migratie met verschil in aantallen — Specialistisch

Vacaturekoppeling: R08/R18/R35. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Tijdens oefencutover telt nieuwe omgeving minder open voertuigen dan oude bron.

**Wat weet ik?:** Telling verschilt; criterium “open” kan verschillend zijn.

**Wat weet ik niet?:** Snapshot, filters, rejected records, cutoverwindow en terugkeermogelijkheid.

**Eerste vragen / controles:** Zelfde snapshot en statusdefinitie, welke sleutelset ontbreekt, berichten tijdens freeze?

**Mogelijke oorzaken:** Mappingfout, ontbrekende historie, uitsluitingsregel, batchreject of events na snapshot.

**Logs / bewijs:** Migratiebatch, mappingversie, rejected IDs en change/cutovertijd.

**Database:** Sleutel-/veld-/statusreconciliatie, niet alleen counts; bron/target audit.

**Netwerk:** Transport-integriteit indien file onvolledig; checksum/recordcount in demo.

**Applicatie:** Businessacceptatie per status en kritieke taak, niet alleen technische import.

**Integratie:** In-flight messages, dedupkeys en partnerroutewissel mee analyseren.

**Mijn aanpak:** Go-live stoppen volgens criteria → differences by key → classificeer → herstel/afstelbesluit.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: “hold” status verkeerd uitgesloten; bewijs met mapping en keyset.

**Oplossing:** Mapping corrigeren/rehearsal herhalen of cutover afstellen via owner; herstelpad op data beoordelen.

**Communicatie:** Go/no-go op concrete verschillen en risico, geen cosmetisch aanpassen van rapportcounts.

**Preventie:** Meerdere rehearsalruns, reconciliation gates en delta/in-flight plan.

**Goed genoeg / rubric:** Key/field reconciliation; Snapshot/in-flight; Go/no-go gate; Herstelbaarheid.

## 24. Retry-storm veroorzaakt nieuwe uitval — Specialistisch

Vacaturekoppeling: R20/R25/R18. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Na partnertimeout stijgen retries en raken runtimepools vol; errors nemen toe.

**Wat weet ik?:** Retries en resourceuitputting correleren, causaliteit nog testen.

**Wat weet ik niet?:** Commitstatus, retrybeleid, capaciteit, veilige pauze en backlog.

**Eerste vragen / controles:** Welke retryfrequentie, hoeveel unieke events, first failure vóór storm, wie mag throttlen?

**Mogelijke oorzaken:** Onbegrensde retries, geen backoff, concurrency te hoog of oorspronkelijk downstreamprobleem.

**Logs / bewijs:** Retrycount, request-ID, poolwait, errortrend, oldest pending en first failure.

**Database:** Commit/dedup en lock/poolimpact door DBA beoordelen.

**Netwerk:** Timeout oorspronkelijke bron mogelijk; connect versus readtimeout onderscheiden.

**Applicatie:** Threads/pool versus business throughput vergelijken; restart kan load terug laten stormen.

**Integratie:** Veilige rate limit/backoff en duplicate-safe controlled replay met partner.

**Mijn aanpak:** Contain load met bevoegdheid → eerst oorzaak → bewezen healthy baseline → geleidelijk backlog verwerken.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: retries zonder jitter/backoff versterken tijdelijk DB-probleem; meet in lab.

**Oplossing:** Geautoriseerd pauzeren/throttlen, dependency herstellen, idempotente replay begrenzen en monitoren.

**Communicatie:** Meld herstelvolgorde en dataconsistentie; niet beloven dat alle backlog direct weg is.

**Preventie:** Bounded retries/backoff, capacitytest, circuit-breaker als ontwerpoptie en businessmonitor.

**Goed genoeg / rubric:** Feedbacklus herkennen; Containment met mandaat; Duplicate-safe backlog; Geleidelijke hervatting.

## 25. Nieuwe TOS go-live onder tijdsdruk — Specialistisch

Vacaturekoppeling: R06/R08/R07/R18/R33. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**

**Situatie / symptomen:** Leverancier wil live; operationele acceptance, rollbackbewijs en gebruikersopleiding zijn onvolledig.

**Wat weet ik?:** Technische build is klaar, readiness niet.

**Wat weet ik niet?:** Welke kritieke criteria ontbreken, mandate, contractdeadline en restimpact.

**Eerste vragen / controles:** Welke task tests geslaagd, data verschillen, supportcoverage, training, restore en partnerchecks?

**Mogelijke oorzaken:** Planningdruk, definition-of-done te smal, afhankelijkheden of onderschatte adoptie.

**Logs / bewijs:** Test/release manifest, open defects, cutoverrehearsal en goedkeuringslog.

**Database:** Migratiereconciliatie en recoverywindow aantonen.

**Netwerk:** Bereikbaarheid per locatie/partner in go-livebewijs.

**Applicatie:** Kritieke businessjourneys en autorisatiechecks laten accepteren.

**Integratie:** Inbound/outbound route, ACK en in-flight data met partners testen.

**Mijn aanpak:** Readiness matrix → blockers/rest-risico → opties/pilot/uitstel → bevoegd go/no-go.

**Diagnose — te bewijzen oefenhypothese:** Oefenhypothese: geen gevalideerd recoverypad voor migratie is een blocker totdat bevoegd risico-besluit bestaat.

**Oplossing:** Niet zelfstandig politiek beslissen: evidence/advies en expliciet mandaat; missing gates afronden of window wijzigen.

**Communicatie:** Zakelijk: welke gate ontbreekt, welke gevolgen, wat is nodig en wie beslist vóór welk tijdstip.

**Preventie:** Readinesscriteria vanaf projectstart, training/supportworkstream en rehearsalplanning.

**Goed genoeg / rubric:** Build versus readiness; Evidence gates; Recovery en adoptie; Expliciet go/no-go.

<a id="15"></a>

# DEEL 15 — Interview question bank

**Waarschijnlijk / afgeleid uit functiecontext — oefenvragen, geen gelekte ICO-interviewvragen.** 56 vragen, acht categorieën. Gebruik de modelantwoorden als structuur. Geen ervan mag fictieve persoonlijke ervaring worden. Een sterk antwoord noemt feitelijke eigen bijdrage, grenzen, bewijs en relatie met de job.

Een 30-secondenantwoord is het korte antwoord hieronder. Een 2-minutenantwoord gebruikt een echte case: context → jouw taak → acties/bewijs → resultaat → reflectie/rolkoppeling. Bij vijf complexe vragen is een langere invulling toegevoegd. De simulator werkt lokaal met timer, notities en zelfbeoordeling; geen AI-score.


## HR-vragen

### 01. Vertel over jezelf in relatie tot deze functie.

**Interviewer wil weten:** Relevant profiel kunnen selecteren, geen hele levensloop.

**Sterk / 30 seconden:** Ik verbind mijn echte ervaring met drie rolgebieden: probleemdiagnose, gecontroleerd opleveren en communicatie. Voor ieder gebied noem ik een werk- of labvoorbeeld en mijn eigen bijdrage. Ik benoem welk stackdeel ik nog gericht leer.

**Zwak — vermijden:** Mijn CV volledig voorlezen of claimen de hele stack al te beheersen.

**Vervolgvragen:** Wat was jouw bijdrage, wat deed het team, welk bewijs heb je?

**2 minuten:** Begin met huidige rol/achtergrond in één zin. Bespreek één concreet probleem, jouw acties en toetsbaar resultaat. Koppel dat aan applicatiebeheer, requirements of leverancierscoördinatie. Noem één gerichte gap, de oefening waarmee je haar verkleint en welke begeleiding je eerst nodig hebt. Gebruik uitsluitend echte cijfers en gebeurtenissen.

### 02. Waarom wil je van functie veranderen?

**Interviewer wil weten:** Constructieve motivatie en verwachting.

**Sterk / 30 seconden:** Ik zoek een rol waarin techniek direct aan operationele processen gekoppeld is en waar ik naast bouwen ook analyse, delivery en beheer verantwoordelijkheid kan opnemen. Ik leg uit waarom mijn huidige stap logisch is met mijn echte achtergrond.

**Zwak — vermijden:** Mijn huidige werkgever/team afbreken of zeggen dat ik alleen een wagen wil.

**Vervolgvragen:** Wat ontbreekt nu, wat verwacht je hier anders?

### 03. Hoe kijk je naar wachtdienst?

**Interviewer wil weten:** Praktische beschikbaarheid en realistisch risicobesef.

**Sterk / 30 seconden:** Ik begrijp dat wachtdienst expliciet onderdeel is. Ik wil rooster, responstijd, escalatiedekking, opleiding en compensatie bespreken. Binnen passende afspraken bereid ik me voor met runbooks en toegangschecks; ik beloof geen onbeperkte beschikbaarheid.

**Zwak — vermijden:** Altijd beschikbaar beloven zonder afspraken, of wachtdienst negeren.

**Vervolgvragen:** Hoe handel je een nachtelijke oproep met onbekende oorzaak af?

### 04. Kun je werken in Zeebrugge en korte verplaatsingen doen?

**Interviewer wil weten:** Haalbaarheid van werkcontext.

**Sterk / 30 seconden:** Ik geef eerlijk mijn bereikbaarheid en mobiliteitsmogelijkheden. Ik begrijp dat Kallo/Zeebrugge in scope zijn en één à twee korte verplaatsingen per maand genoemd worden; ik vraag hoe planning en wachtdienst logistiek geregeld zijn.

**Zwak — vermijden:** Een reis-/woonvoorkeur verzwijgen die later niet haalbaar blijkt.

**Vervolgvragen:** Wat is je praktische start-/reisplan?

### 05. Hoe voldoe je aan de opleidingseis?

**Interviewer wil weten:** Theoretische basis en bewijs van equivalentie.

**Sterk / 30 seconden:** Ik noem mijn echte diploma en relevante ervaring. Als het diploma afwijkt, toon ik analyse-/systeemprojecten en professionele verantwoordelijkheden. Ik vraag hoe ICO ervaring tegen de genoemde opleiding afweegt; ik verzin geen gelijkwaardigheid.

**Zwak — vermijden:** Een diploma/certificaat suggereren dat ik niet bezit.

**Vervolgvragen:** Welke onderwerpen uit opleiding pas je praktisch toe?

### 06. Wat zijn je sterke punten en leerpunten?

**Interviewer wil weten:** Zelfkennis zonder ingestudeerde schijnzwakte.

**Sterk / 30 seconden:** Ik kies twee sterke punten met bewijs en één relevante gap met concrete oefening, feedback en doel. Bijvoorbeeld SQL-praktijk sterk, AIX-productkennis nog beperkt; alleen als dat mijn profiel echt beschrijft.

**Zwak — vermijden:** Perfectionisme noemen zonder concreet gedrag of alle gaps verbergen.

**Vervolgvragen:** Hoe weet je dat dit sterk is, wat verbeterde recent?

### 07. Wat verwacht je van onboarding?

**Interviewer wil weten:** Leerbaarheid en zelfstandige voorbereiding.

**Sterk / 30 seconden:** Ik wil eerst proces/architectuur, eigenaren, toegang, changeprocedures en incidentescalatie begrijpen. Daarna shadow ik tickets en lever een kleine change met review op. Ik neem zelf notities en controleer begrip met teach-back.

**Zwak — vermijden:** Een volledige cursus voor alles eisen of zonder begeleiding productie aanpassen.

**Vervolgvragen:** Wat kun je al in week één bijdragen?

## Motivatie-vragen

### 08. Waarom ICO en havenlogistiek?

**Interviewer wil weten:** Onderbouwde interesse in echte businesscontext.

**Sterk / 30 seconden:** De publieke ICO-site beschrijft RoRo en automotive-distributie. De rol spreekt mij aan omdat applicatiedata en integraties de fysieke operatie ondersteunen en omdat beheer naast een nieuw TOS-project staat. Ik wil de precieze projectfase van jullie horen.

**Zwak — vermijden:** Fictieve innovatieprojecten of interne systemen aan ICO toeschrijven.

**Vervolgvragen:** Wat weet je van onze activiteiten en waar komt die kennis vandaan?

### 09. Waarom deze brede rol in plaats van alleen developer?

**Interviewer wil weten:** Fit met support, analysis en coördinatie.

**Sterk / 30 seconden:** Ik wil verantwoordelijkheid voor een bruikbaar resultaat, inclusief requirements, tests, gebruikers en nazorg. Code is één middel. Ik geef een echt voorbeeld waarin diagnose of afstemming meer waarde gaf dan een extra feature.

**Zwak — vermijden:** Support minderwaardig noemen of impliceren alleen te willen programmeren.

**Vervolgvragen:** Hoe verdeel je aandacht tussen incidenten en projectwerk?

### 10. Wat vind je interessant aan legacy/enterpriseplatformen?

**Interviewer wil weten:** Pragmatische houding tegenover bestaande stack.

**Sterk / 30 seconden:** Ik zie bestaande platforms als systemen met waarde, constraints en afhankelijkheden. Ik leer eerst waarom ze er zijn en hoe ze werken. Moderniseren beoordeel ik op risico, kosten, supportbaarheid en businessresultaat.

**Zwak — vermijden:** AIX/JBoss verouderd noemen en onmiddellijk alles herschrijven.

**Vervolgvragen:** Wanneer zou je vervangen in plaats van verbeteren?

### 11. Wat trekt je aan in nieuw TOS implementeren?

**Interviewer wil weten:** Veranderwerk realistisch begrijpen.

**Sterk / 30 seconden:** Het verbindt processen, data, integraties, leveranciers en adoptie. Ik vind gecontroleerde cutover interessant: duidelijke acceptance, sleutelreconciliatie, in-flight berichten en herstelplan. De fase en mijn mandaat wil ik begrijpen.

**Zwak — vermijden:** Alleen enthousiast zijn over een nieuw scherm of technische stack.

**Vervolgvragen:** Wat kan misgaan bij cutover?

### 12. Wat wil je in zes maanden kunnen?

**Interviewer wil weten:** Gerichte ontwikkeling en realistische scope.

**Sterk / 30 seconden:** Binnen lokale afspraken wil ik de kernketen zelfstandig uitleggen, afgebakende tweedelijnstickets afhandelen en één kleine verbetering end-to-end opleveren met businessacceptatie. Exacte doelen stel ik met supervisor vast.

**Zwak — vermijden:** Binnen zes maanden architect van alles willen zijn zonder context.

**Vervolgvragen:** Hoe meet je vooruitgang?

### 13. Welke minder leuke delen accepteer je?

**Interviewer wil weten:** Bewustzijn van administratie, support en herhaling.

**Sterk / 30 seconden:** Rapportage, incidentregistratie en documentatie horen bij betrouwbaarheid. Ik maak ze efficiënt met vaste formats en automatisering waar verantwoord, zodat de volgende collega niet opnieuw moet zoeken.

**Zwak — vermijden:** Zeggen dat documentatie of gebruikersvragen tijdverspilling zijn.

**Vervolgvragen:** Hoe houd je documentatie actueel?

### 14. Waarom ben je interessant als je niet alles kent?

**Interviewer wil weten:** Transferable skills plus eerlijk leerplan.

**Sterk / 30 seconden:** Ik toon bewijs in analyse, delivery en communicatie en benoem precies welke productkennis ontbreekt. Ik oefen met vergelijkbare concepten, zonder die als productervaring te verkopen. Voor lokale TOS/AIX-procedures zoek ik begeleide start.

**Zwak — vermijden:** Ik leer snel zeggen zonder bewijs of geen gaps willen erkennen.

**Vervolgvragen:** Welke gap is het grootste risico?

## Techniek-vragen

### 15. Leg de waarschijnlijke architectuur uit.

**Interviewer wil weten:** Laagbegrip en feiten scheiden.

**Sterk / 30 seconden:** De vacature noemt TOS-componenten met AIX/IBM P-series, Oracle en JBoss, plus iWay, WebFOCUS, portalen en Apex. Ik zou de verbindingen eerst valideren. Een oefenmodel is portal → app → database, met EDI en rapportering ernaast. APEX heeft een eigen databasegerichte route.

**Zwak — vermijden:** Een eigen cloud/microservice-architectuur presenteren als ICO-feit.

**Vervolgvragen:** Waar verwacht je logs en wat is de bron van waarheid?

**2 minuten:** Noem eerst de bevestigde componenten. Leg daarna laag voor laag functies uit. Toon één oefentransactie en mogelijke foutgrenzen. Zeg expliciet dat productvarianten, authenticatie, transport en topology niet in de vacature staan. Vraag welke componenten in het nieuwe TOS blijven. Gebruik geen ORDS/JBoss-relatie als vaststaand bedrijfsfeit.

### 16. Wat is een transactie en waarom is die belangrijk?

**Interviewer wil weten:** Dataconsistentie en recovery.

**Sterk / 30 seconden:** Een transactie bundelt wijzigingen met commit of rollback. Een status en auditrecord moeten consistent blijven. Een timeout na commit kan leiden tot duplicate retry; ik verifieer businessstatus en idempotentie voordat ik opnieuw uitvoer.

**Zwak — vermijden:** Commit zien als hetzelfde als gebruiker ontving succes.

**Vervolgvragen:** Hoe test je een fout tussen commit en ACK?

### 17. Hoe voorkom je dubbele EDI-verwerking?

**Interviewer wil weten:** Idempotentie en concurrerende races.

**Sterk / 30 seconden:** Ik definieer een business-eventkey, niet alleen transport-ID. Atomische unieke verwerking en opgeslagen resultaat beschermen bij retry/concurrency. Ik test dubbel, opnieuw verpakt, timeout na commit en parallel verstuurd. Exact contract afstemmen.

**Zwak — vermijden:** Een voorafgaande SELECT als enige dedupcontrole gebruiken zonder racebescherming.

**Vervolgvragen:** Wat als partner iedere retry een nieuw ID geeft?

### 18. Wat doet JBoss?

**Interviewer wil weten:** Runtime onderscheiden van applicatie.

**Sterk / 30 seconden:** JBoss is een Java application serverfamilie die applicaties en gedeelde services zoals datasources/threads beheert. Variant/versie bepalen details. Ik lees eerste exception, config en poolgedrag en controleer echte businessactie, niet alleen processtatus.

**Zwak — vermijden:** JBoss een database noemen of EAP-versie bij ICO aannemen.

**Vervolgvragen:** Waarom kan healthy process toch falende transacties hebben?

### 19. Wat moet je van AIX weten?

**Interviewer wil weten:** Platformbegrip en veilige grenzen.

**Sterk / 30 seconden:** Processen, rechten, filesystem en resourcegedrag begrijpen. Ik lever tijd, path en foutbewijs aan beheerder en gebruik lokale toegestane read-only checks. Linuxkennis helpt conceptueel, maar AIX-specifieke procedures verifieer ik.

**Zwak — vermijden:** Linuxcommando’s als bewezen AIX-runbook presenteren.

**Vervolgvragen:** Wat doe je bij volle disk?

### 20. Wat is APEX en hoe beveilig je een formulier?

**Interviewer wil weten:** Productinterpretatie en serverregels.

**Sterk / 30 seconden:** In Oracle-context waarschijnlijk Oracle APEX, maar ik bevestig de naam. APEX maakt databasegerichte webapps. Validatie en authorisatie moeten op server/objectscope gelden; UI verbergen is geen security. Ik test onbevoegde request, conflict en audit.

**Zwak — vermijden:** APEX automatisch op JBoss laten draaien of alleen UI-knop blokkeren.

**Vervolgvragen:** Wat is session state en waarom maakt het uit?

### 21. Hoe maak je rapportcijfers betrouwbaar?

**Interviewer wil weten:** Businessdefinitie en datalineage.

**Sterk / 30 seconden:** Definieer businessobject, snapshot/tijdzone, inclusie, unique keys en filters. Vergelijk bron en rapport met een sleutelverschillenlijst, niet alleen totalen. Check join-cardinaliteit en refresh. Laat business de definitie accepteren.

**Zwak — vermijden:** Blind DISTINCT gebruiken om totaal passend te krijgen.

**Vervolgvragen:** Wat is verschil tussen eventtijd en verwerkingstijd?

## Scenario-vragen

### 22. Business vraagt directe productie-UPDATE.

**Interviewer wil weten:** Veiligheid en mandaat onder druk.

**Sterk / 30 seconden:** Ik verduidelijk impact, bron van waarheid en downstreameffect. Alleen een bevoegde, traceerbare correctie met audit/reconciliatie en herstelplan is acceptabel. Ik betrek businessowner als status fysieke vrijgave raakt.

**Zwak — vermijden:** Een UPDATE uitvoeren om gebruiker gerust te stellen.

**Vervolgvragen:** Wat als manager blijft aandringen?

### 23. Leverancier levert laat: wat doe je?

**Interviewer wil weten:** Actiegericht escaleren.

**Sterk / 30 seconden:** Ik verifieer resterend werk en acceptance, maak impact op afhankelijke taken duidelijk en geef opties met capaciteit/scope/tijd. Acties krijgen owner/datum. Escalatie volgt mandaat; ik maskeer vertraging niet in weekrapport.

**Zwak — vermijden:** Alleen zeggen dat leverancier slecht is.

**Vervolgvragen:** Wat meld je business en wat meld je leverancier?

### 24. Release faalt na schemawijziging.

**Interviewer wil weten:** Hersteldenken over data.

**Sterk / 30 seconden:** Ik stop verdere ongecontroleerde changes, inventariseer app/schema/datastatus en vraag bevoegd go/no-go. Rollback hangt van compatibiliteit en nieuwe data af. Ik kies met owners bewezen recovery/forward fix en valideer keten/business.

**Zwak — vermijden:** Meteen oude app terugzetten zonder schemacontrole.

**Vervolgvragen:** Wat als migratie onomkeerbaar is?

**2 minuten:** Beschrijf eerste minuten: owner, scope, stoppen en bewijs. Maak onderscheid tussen deploymentstatus en datastatus. Leg expliciet uit dat een restore nieuw ontstane data kan verliezen en replay duplicaten kan veroorzaken. Benoem beslisrecht, communicatie en stopcriteria. Sluit met businessjourneys, sleutelreconciliatie en monitorperiode.

### 25. Twee locaties hebben verschillende resultaten.

**Interviewer wil weten:** Scope en sitevarianten.

**Sterk / 30 seconden:** Ik vergelijk dezelfde veilige taak, parameters, config en tijd over Kallo/Zeebrugge. Werkende site is een controlegroep, geen bewijs dat gedeelde componenten perfect zijn. Ik probeer de eerste verschilgrens te vinden.

**Zwak — vermijden:** Globale restart uitvoeren omdat één site faalt.

**Vervolgvragen:** Welke site-specifieke data kan oorzaak zijn?

### 26. Nieuwe collega blijft fouten maken.

**Interviewer wil weten:** Coachend en taakgericht handelen.

**Sterk / 30 seconden:** Ik observeer de taak en controleer instructieversie/toegang. Daarna oefent collega zelf happy en foutpad en legt aanpak terug uit. Ik verbeter instructie of proces waar verwarring terugkeert.

**Zwak — vermijden:** Zeggen dat collega gewoon beter moet opletten.

**Vervolgvragen:** Hoe meet je of training werkt?

### 27. Mogelijk klantdata verkeerd zichtbaar.

**Interviewer wil weten:** Securityincident herkennen.

**Sterk / 30 seconden:** Ik escaleer feitelijk naar security/IT-owner, beperk bewijsdeling en laat exposure/containment bepalen. Ik test met veilige accounts, behoud audit en corrigeer server/objectscope via procedure. Externe communicatie door aangewezen owner.

**Zwak — vermijden:** Screenshot breed mailen of logs wissen na fix.

**Vervolgvragen:** Welke minimale gegevens leg je vast?

### 28. Go-live gepland, training niet klaar.

**Interviewer wil weten:** Readiness over techniek heen.

**Sterk / 30 seconden:** Ik maak ontbrekende acceptance/training/support/recovery concreet in readinessmatrix. Ik presenteer risico en opties, bijvoorbeeld beperkte pilot of ander window. Bevoegd owner beslist expliciet; gebouwd is niet hetzelfde als klaar voor gebruik.

**Zwak — vermijden:** Live zetten omdat leverancier klaar zegt.

**Vervolgvragen:** Welke gates zijn blockers?

## Troubleshooting-vragen

### 29. Wat doe je in de eerste vijf minuten van een incident?

**Interviewer wil weten:** Geordend handelen.

**Sterk / 30 seconden:** Ik bepaal businessimpact/veiligheid, scope, starttijd, laatste werkende taak en owner. Ik verzamel één geredigeerd sample/request-ID en recente changes. Ik communiceer volgende update en wijzig niets blind.

**Zwak — vermijden:** Onmiddellijk restarten of tegelijk vijf instellingen wijzigen.

**Vervolgvragen:** Hoe bepaal je prioriteit?

### 30. Welke logregel is het belangrijkst?

**Interviewer wil weten:** Correlatie en eerste oorzaak.

**Sterk / 30 seconden:** De eerste relevante fout in dezelfde keten is vaak waardevoller dan latere gevolgerrors. Ik koppel ID, tijdzone, versie en businessresultaat. Een losse stacktrace zonder context is onvoldoende.

**Zwak — vermijden:** De langste stacktrace kopiëren zonder tijd/ID.

**Vervolgvragen:** Hoe herken je vervolgschade?

### 31. HTTP 200 maar gebruiker meldt fout.

**Interviewer wil weten:** Technisch succes versus businesssucces.

**Sterk / 30 seconden:** Ik lees contract en body, controleer businessresultaat en downstreamcommit. 200 kan alleen geaccepteerde ontvangst betekenen. Ik volg de async-verwerking en laat gebruiker de taakuitkomst bevestigen.

**Zwak — vermijden:** 200 als bewijs dat het systeem volledig goed werkt.

**Vervolgvragen:** Hoe monitor je asynchrone afhandeling?

### 32. Geen errors, toch geen verwerking.

**Interviewer wil weten:** Liveness van businessproces.

**Sterk / 30 seconden:** Ik controleer verwacht volume, laatste succesvolle verwerking, scheduler/consumer en oldest pending. Een stilstaande flow kan geen nieuwe errors geven. Ik vergelijk inputvolume met unieke gecommitteerde events.

**Zwak — vermijden:** Niets doen omdat logs groen zijn.

**Vervolgvragen:** Welke alert zou dit eerder vinden?

### 33. Wanneer escaleer je?

**Interviewer wil weten:** Grenzen en ownership.

**Sterk / 30 seconden:** Bij veiligheids/data/securityrisico, brede impact, ontbrekend recht/kennis, benodigde specialist of afgesproken tijdgrens. Ik stuur evidence pack met impact, tijdlijn, laatste goede grens, tests en benodigde actie/besluit.

**Zwak — vermijden:** Pas na uren zoeken of meteen zonder enige context doorschuiven.

**Vervolgvragen:** Wat is een goede evidence pack?

### 34. Hoe voorkom je tunnelvisie?

**Interviewer wil weten:** Wetenschappelijke probleemaanpak.

**Sterk / 30 seconden:** Ik schrijf minstens twee hypotheses met voorspelling en weerlegging. Ik kies een veilige onderscheidende test en zoek een werkend tegenvoorbeeld. Daarna verander ik één factor en meet resultaat.

**Zwak — vermijden:** De laatste change altijd als oorzaak aannemen.

**Vervolgvragen:** Geef een hypothesematrix voor traag rapport.

### 35. Hoe sluit je een incident correct af?

**Interviewer wil weten:** Resultaat en vervolgwerk.

**Sterk / 30 seconden:** Businesshandeling gevalideerd, backlog/dataconsistentie gecontroleerd, gebruiker bevestigt en acties/tijdlijn vastgelegd. Root cause onzeker? Dan expliciet problem-link en eigenaar, geen verzonnen conclusie. Workaround krijgt einddatum.

**Zwak — vermijden:** Ticket sluiten zodra service start.

**Vervolgvragen:** Wat monitort je na herstel?

## Business-vragen

### 36. Waarom is IT kritisch in een RoRo-terminal?

**Interviewer wil weten:** Sectorbegrip zonder bedrijfsfantasie.

**Sterk / 30 seconden:** Fysieke overdracht en informatie moeten overeenkomen: identiteit, locatie, status en partnercommunicatie. Verkeerde data kan zoekwerk, vertraging of verkeerde planning veroorzaken. Exacte ICO-procesregels wil ik bij operations valideren.

**Zwak — vermijden:** Alle terminals behandelen alsof het containers zijn.

**Vervolgvragen:** Wat betekent RoRo?

### 37. Wat is de bron van waarheid?

**Interviewer wil weten:** Data ownership.

**Sterk / 30 seconden:** Dat is per gegeven de afgesproken gezaghebbende bron, niet noodzakelijk één systeem voor alles. Voor fysieke aanwezigheid, partneropdracht en financiële status kunnen andere owners gelden. Conflicten oplossen vraagt regels en bewijs.

**Zwak — vermijden:** Het nieuwste bericht is altijd waar.

**Vervolgvragen:** Wat doe je bij conflicterende bronnen?

### 38. Hoe prioriteer je een rapportbug en integratie-uitval?

**Interviewer wil weten:** Impactgestuurde beslissingen.

**Sterk / 30 seconden:** Ik vergelijk fysieke/processimpact, gebruikers/partners, deadline, veiligheid en workaround. De categorie alleen bepaalt prioriteit niet. Ik vraag operationele owner om businessconsequenties en documenteer afweging.

**Zwak — vermijden:** Iedere integratie-uitval automatisch hoger zetten.

**Vervolgvragen:** Wanneer is een rapport kritieker?

### 39. Wat betekent efficiënte implementatie?

**Interviewer wil weten:** Businessresultaat plus totale kosten.

**Sterk / 30 seconden:** Niet alleen weinig ontwikkeluren: bruikbaarheid, fouten, beheerlast, opleiding en support tellen mee. Ik leg acceptance en verwachte verbetering vast en meet na release met business, zonder fictieve ROI-cijfers.

**Zwak — vermijden:** Snel live gaan gelijkstellen aan efficiëntie.

**Vervolgvragen:** Welke KPI zou je kiezen?

### 40. Welke datavelden wil je begrijpen?

**Interviewer wil weten:** Procesmodel kunnen afleiden.

**Sterk / 30 seconden:** Identiteit/businesssleutel, statusbetekenis, locatie, event/verwerkingstijd, partnerreferentie, actor/audit en uitzonderingen. Ik vraag welke van deze werkelijk bestaan en wie eigenaar is, niet dat mijn demoschema productieschema is.

**Zwak — vermijden:** Alleen tabellen bekijken zonder statusbetekenis.

**Vervolgvragen:** Waarom twee timestamps?

### 41. Hoe betrek je een gebruiker bij acceptance?

**Interviewer wil weten:** Testbare adoptie.

**Sterk / 30 seconden:** Laat de gebruiker representatieve taken inclusief uitzondering uitvoeren met heldere expected results. Leg bewijs en besluit vast. Demo kijken is geen UAT; de proceseigenaar accepteert functionele regels.

**Zwak — vermijden:** Na één demo aannemen dat iedereen akkoord is.

**Vervolgvragen:** Wie beslist over tegenstrijdige verwachtingen?

### 42. Hoe ondersteunt deze rol kwaliteit/veiligheid/milieu?

**Interviewer wil weten:** Verantwoordelijkheid voor fysieke context.

**Sterk / 30 seconden:** Ik behandel data die fysieke handelingen stuurt zorgvuldig, borg audit/rechten en bespreek veilige workarounds met operations. Efficiëntere/logistieke informatie kan helpen, maar ik verzin geen ICO-emissiesystemen of certificering.

**Zwak — vermijden:** Veiligheid als alleen hardwareteamprobleem afdoen.

**Vervolgvragen:** Geef voorbeeld van gevaarlijke statuscorrectie.

## Gedrag-vragen

### 43. Vertel over een fout die je maakte.

**Interviewer wil weten:** Ownership en leren.

**Sterk / 30 seconden:** Gebruik een echte STAR-case: situatie, jouw verantwoordelijkheid, fout, gevolg, herstel/communicatie en preventie. Benoem eigen aandeel zonder collega’s de schuld te geven. Heb je alleen labvoorbeeld, zeg dat expliciet.

**Zwak — vermijden:** Ik maak geen fouten of een verkapte successtory.

**Vervolgvragen:** Welke controle heb je daarna toegevoegd?

### 44. Hoe werk je onder stress?

**Interviewer wil weten:** Betrouwbaar gedrag onder druk.

**Sterk / 30 seconden:** Ik stabiliseer impact/veiligheid, schrijf acties/tijd op, verdeel eigenaarschap en update vaste momenten. Ik verander één factor tegelijk en vraag hulp waar nodig. Onderbouw dit met echt voorbeeld.

**Zwak — vermijden:** Ik doe alles tegelijk en werk gewoon harder.

**Vervolgvragen:** Wanneer verloor je overzicht en wat deed je?

### 45. Beschrijf een conflict met stakeholder.

**Interviewer wil weten:** Feiten en gezamenlijke uitkomst.

**Sterk / 30 seconden:** Gebruik een echte case met verschillend doel/verwachting. Ik maak de criteria en evidence zichtbaar, stel opties voor en bevestig besluit/actie. Ik beschrijf mijn eigen communicatie en resultaat.

**Zwak — vermijden:** De ander was dom; ik had gelijk.

**Vervolgvragen:** Wat zou je volgende keer anders zeggen?

### 46. Hoe organiseer je veel parallelle taken?

**Interviewer wil weten:** Capaciteit en prioriteit.

**Sterk / 30 seconden:** Ik houd één zichtbaar overzicht met impact, deadline, owner, afhankelijkheid en status. Ik reserveer incidentruimte, beperk werk in uitvoering en escaleer capaciteitsspanning voordat beloften onhaalbaar worden.

**Zwak — vermijden:** Alles in mijn hoofd of altijd meteen nieuwste vraag doen.

**Vervolgvragen:** Wat laat je vallen als productieincident komt?

### 47. Hoe geef je taakgericht leiding zonder hiërarchie?

**Interviewer wil weten:** Coördinatie en invloed.

**Sterk / 30 seconden:** Ik spreek resultaat, acceptance, eigenaar en datum af en vraag bewijs/obstakels. Ik coach op taak en escaleer bij mandaatconflict. Ik behandel een leverancier niet als werknemer als dat niet mijn rol is.

**Zwak — vermijden:** Iedereen bevelen geven of niets durven afspreken.

**Vervolgvragen:** Wat als iemand afspraken niet nakomt?

### 48. Hoe ga je om met onbekende techniek?

**Interviewer wil weten:** Leermethode en eerlijkheid.

**Sterk / 30 seconden:** Ik zoek officiële docs voor gebruikte versie, bouw kleine veilige repro, vraag buddyreview en documenteer wat nog onbekend is. Ik koppel kennis aan concrete taak en test voldoende begrip vóór productieactie.

**Zwak — vermijden:** Online commando kopiëren en in productie proberen.

**Vervolgvragen:** Welke output lever je na één leerdag?

### 49. Wanneer zeg je nee?

**Interviewer wil weten:** Integriteit en risicobeheersing.

**Sterk / 30 seconden:** Ik begrens een actie die onbevoegd, onveilig of zonder herstelbaarheid is. Ik leg het risico concreet uit en bied een uitvoerbaar alternatief of vraag expliciet besluit aan de juiste owner. Ik blokkeer niet uit gemak.

**Zwak — vermijden:** Altijd ja zeggen of alleen “procedure zegt nee”.

**Vervolgvragen:** Hoe behoud je samenwerking?

## Ervaring-vragen

### 50. Welke projectervaring sluit aan?

**Interviewer wil weten:** Eigen bijdrage en transfer.

**Sterk / 30 seconden:** Ik selecteer een echt project met requirement, afhankelijkheid, planning en acceptatie. Ik vertel wat ik zelf deed, hoe ik risico volgde en wat aantoonbaar werkte. Portfolio label ik als portfolio, geen professionele delivery.

**Zwak — vermijden:** Teamresultaat volledig aan mezelf toeschrijven.

**Vervolgvragen:** Hoe rapporteerde je afwijkingen?

### 51. Heb je Oracle/AIX/JBoss-ervaring?

**Interviewer wil weten:** Productniveau exact kunnen plaatsen.

**Sterk / 30 seconden:** Ik benoem per product: theorie, lab, met hulp of zelfstandig professioneel. Transfer vanuit andere SQL/Unix/runtimeomgeving leg ik concreet uit en voeg productverschillen toe. Een ontbrekend AIX-lab is geen AIX-beheerervaring.

**Zwak — vermijden:** Ja zeggen omdat ik Linux of SQL ken.

**Vervolgvragen:** Welke taak deed je zelfstandig en welke met begeleiding?

### 52. Toon je beste troubleshootingcase.

**Interviewer wil weten:** Diagnostiek en bewijs.

**Sterk / 30 seconden:** Echte case: verwacht/werkelijk, impact, hypotheses, test, eerste foutgrens, gecontroleerd herstel en preventie. Laat geanonimiseerde runbook/test/logvoorbeeld zien, zonder vertrouwelijke gegevens.

**Zwak — vermijden:** Ik restartte en het was opgelost zonder verdere controle.

**Vervolgvragen:** Wat bewees de oorzaak en wat was onzeker?

**2 minuten:** Gebruik maximaal twee minuten: 20 seconden context/impact; 40 seconden hypotheses en onderscheidend bewijs; 30 seconden herstel/validatie; 30 seconden oorzaak/preventie en eigen bijdrage. Als root cause niet bewezen was, zeg dat en licht vervolgwerk toe. Noem alleen echte resultaten of duidelijk synthetische labmetingen.

### 53. Welke code/tool heb je gemaakt?

**Interviewer wil weten:** Hands-on delivery en onderhoud.

**Sterk / 30 seconden:** Toon een echte tool met businessprobleem, input/output, validatie, auth indien relevant, logging en tests. Bespreek foutpaden, README en wat je achteraf verbeterde. Leg rolkoppeling uit, niet alleen framework.

**Zwak — vermijden:** Alleen UI-screenshot tonen en geen gedrag uitleggen.

**Vervolgvragen:** Wat gebeurt bij duplicaat of timeout?

### 54. Heb je leveranciers gestuurd?

**Interviewer wil weten:** Communicatie en acceptance.

**Sterk / 30 seconden:** Ik geef echte afstemming met werkpakket, acceptance en acties. Als ik geen professionele vendorervaring heb, toon ik een simulatie/opdracht en leg ik uit wat ik nog niet heb gedaan, zoals contract-/budgetmandaat.

**Zwak — vermijden:** Elke e-mail naar support als volledige leverancierssturing verkopen.

**Vervolgvragen:** Hoe ging je om met incomplete oplevering?

### 55. Hoe heb je kennis overgedragen?

**Interviewer wil weten:** Onboarding en gebruikerstraining.

**Sterk / 30 seconden:** Noem een echte instructie/workshop/pairing. Leg doelgroep, taak, oefening, feedback en versiebeheer uit. Laat gebruiker/collega zelf handelen en pas uitleg aan waar begrip ontbreekt.

**Zwak — vermijden:** Ik stuurde een link dus ze waren opgeleid.

**Vervolgvragen:** Hoe controleerde je begrip?

### 56. Welke gap pak je als eerste aan?

**Interviewer wil weten:** Prioriteit op risico/ROI.

**Sterk / 30 seconden:** Ik kijk naar rolkritiek én mijn bewijs. Ontbrekende SQL/incident/requirements-praktijk heeft hoge prioriteit. Lokale TOS-codes zijn onboardingkennis. Ik kies een oefening met deliverable en stopcriterium en bespreek startbegeleiding.

**Zwak — vermijden:** Alles tegelijk leren of alleen de meest trendy stack.

**Vervolgvragen:** Moet je daarvoor wachten met solliciteren?

<a id="16"></a>

# DEEL 16 — Vragen aan ICO

**Waarschijnlijk / afgeleid uit functiecontext.** ★ markeert de tien meest waardevolle vragen. Verdeel ze over technische en HR-gesprekken; lees niet alle dertig achter elkaar voor. Vraag bij een abstract antwoord een recent concreet voorbeeld.

| Top | Thema | Vraag |
|---|---|---|
| ★ | Team | Hoe groot is het interne/extern ontwikkelingsteam, wie bezit welk component? |
| ★ | Verwachtingen | Welke drie resultaten moet ik na 90 dagen aantoonbaar leveren? |
| ★ | TOS | Welk huidig en nieuw TOS gebruiken jullie, in welke implementatiefase zitten jullie? |
| ★ | Werkmix | Hoe verdeelt de afgelopen maand zich over programmeren, projectwerk en tweede lijn? |
| ★ | Wachtdienst | Hoe vaak word ik ingeroosterd, hoeveel oproepen zijn gebruikelijk, wat zijn dekking/vergoeding/escalatie? |
| ★ | Architectuur | Welke versies/varianten van Oracle, AIX, JBoss, WebFOCUS, iWay en Apex zijn werkelijk in gebruik? |
| ★ | Onboarding | Welke buddy, documentatie, testomgeving en opleidingsdagen zijn beschikbaar? |
| ★ | Autonomie | Welke productiewijzigingen mag deze rol zelfstandig doen en wie autoriseert CRQ/go-live? |
| ★ | Releases | Hoe worden database-, app- en integratiechanges samen getest en hersteld? |
| ★ | Risico | Wat zijn nu de grootste continuïteits- en projectrisico’s waarvoor jullie deze persoon zoeken? |
|  | Legacy | Welke componenten zitten buiten support en welk moderniseringspad is afgesproken? |
|  | Development | Welke programmeertalen, codebases en reviewafspraken gelden voor eigen development? |
|  | EDI | Welke partners, standaarden, transports en ACK-/retrycontracten zijn het belangrijkst? |
|  | Rapportering | Wie bezit businessdefinities, WebFOCUS-rapporten en masterdata? |
|  | Incidents | Hoe verloopt overdracht van Service Desk naar tweede lijn en hoe worden incidenten geprioriteerd? |
|  | Problems | Is er tijd/owner voor structurele fixes na incidenten, en hoe volgen jullie acties? |
|  | Leveranciers | Welke budget-/contract-/acceptatiebevoegdheid heeft deze rol bij externe partners? |
|  | Portefeuille | Hoe kiezen jullie prioriteit bij meerdere businessunits en beperkt budget/capaciteit? |
|  | Locaties | Welke processen/configuraties verschillen tussen Kallo en Zeebrugge? |
|  | Documentatie | Waar staan actuele runbooks, componentcatalogus en releasehistorie, en wie onderhoudt ze? |
|  | Security | Hoe zijn least privilege, vendor access, audit en security-escalatie geregeld? |
|  | Herstel | Wie bezit backup/restore en hoe vaak wordt herstel inclusief integraties gerepeteerd? |
|  | Talen | Welk niveau Nederlands/Engels/Frans is nodig per stakeholder en taak? |
|  | Remote | Wat zijn afspraken over thuiswerk, presence tijdens releases en wachtdienst? |
|  | Cultuur | Hoe reageert het team als iemand een risico of eigen fout vroeg meldt? |
|  | Management | Hoe vaak heb ik feedbackoverleg met Supervisor en Director IT en wat beoordelen zij? |
|  | Carrière | Welke route bestaat naar senior/lead/architect en welk gedrag toont promotiegereedheid? |
|  | Opleiding | Welke producttraining/certificatie wordt gefinancierd en is er werkbare leertijd? |
|  | Arbeidsvoorwaarden | Hoe werken wagen/cafetariaplan, onkosten, verzekeringen en wachtdienstcompensatie praktisch? |
|  | Succes | Hoe meten jullie effectiviteit, efficiënte implementatie en gebruikersadoptie? |

<a id="17"></a>

# DEEL 17 — Portfolio strategie

**Waarschijnlijk / afgeleid uit functiecontext — portfolio-ontwerpen, geen ICO-systemen.** Deze repository bevat het leerinstrument; onderstaande drie projecten zijn afzonderlijke bouwopdrachten, niet reeds gebouwde enterprise-applicaties. Gebruik synthetische data. Bouw liever één geloofwaardige verticale flow met foutpaden dan veel schermen zonder gedrag.


## Project 1 — EDI Reconciliation Lab

**Omvang:** 1–3 dagen bij SQL/programmeerbasis. **Vacaturekoppeling:** R19/R20/R25/R30.

**Probleem:** Partner zegt tien events verstuurd, systeem heeft er acht uniek verwerkt.

**Businesscase:** Snel kunnen verklaren of berichten ontbreken, dubbel zijn of geweigerd zonder gevaarlijke replay.

**Architectuur:** Synthetische JSON/CSV → validatie → SQLite-lab → reconciliatiequery → CLI/klein rapport. SQL-concepten overdraagbaar; dit bewijst geen Oracle-productbeheer.

**Technologie:** Python/SQLite of eigen vertrouwde taal; optioneel Oracle-sandbox. Geen iWay/WebFOCUS-licentie nodig voor conceptbewijs.

**Requirements:** Input bevat message_id, business_event_id, partner, vehicle_id, event_type, event_at. Ontbrekende sleutel afwijzen; duplicaten zichtbaar; bron/target op unieke eventkey vergelijken.

**Features:** Importpreview, rejected reasons, duplicatentelling, ontbrekende keys, last successful en geredigeerde evidence-export.

**Database:** vehicles, messages, processing_results; unique business_event_id; synthetische data en expliciete transacties.

**API/integraties:** Bestandscontract, ACK-simulatie en minimaal drie fixtures: valide, malformed, duplicate. JSON is leerformaat, geen vastgesteld ICO-EDI.

**Authentication:** CLI-local demo heeft geen multi-user auth; documenteer beperking. Als webversie: reader/importerrollen en servercontrole.

**Logging:** ID, tijdzone, mappingversie, stap en resultaat; geen secrets of echte klantgegevens.

**Tests:** Verwacht acht unieke successen, één malformed en één duplicate in vaste fixture; test atomiciteit en opnieuw importeren zonder extra effect.

**Deployment:** Reproduceerbaar lokaal script, vaste dependencies/command, optioneel container. Beperking: geen enterprise productie-SLA.

**Documentatie en README:** Datadictionary, contract, runbook, incidentrapport en README met setup/sample/expected output.

**Screenshots/diagrammen:** Datastroomdiagram plus screenshot van verschilset en duidelijke rejected reason.

**Wat dit bewijst:** SQL, EDI-keten, idempotentie, troubleshooting en Office-achtige reconciliatie. Laat één timeout-after-commit hardop verklaren.

**Definition of done:** clone/setup reproduceerbaar, positieve en negatieve tests draaien, één failure live demonstreren, businessresultaat uitleggen, beperkingen eerlijk labelen en concrete vacancy-IDs in README.


## Project 2 — Vehicle Exception Portal

**Omvang:** Ongeveer één week bij web-/SQLbasis; APEX-productlab kan extra setup vragen. **Vacaturekoppeling:** R11/R12/R14/R21/R22/R31/R09.

**Probleem:** Een gebruiker moet een locatiecorrectie aanvragen zonder audit of validatie te verliezen.

**Businesscase:** Controleerbare taakflow met rolrechten en gebruikersfeedback, geen handmatige ongedocumenteerde data-update.

**Architectuur:** Browser → server-side validatie/autorisatie → relationele DB + audit; optioneel Oracle APEX/ORDS indien sandbox. Moderne equivalent apart labelen.

**Technologie:** Oracle APEX + Oracle-sandbox heeft hoogste productsignalering. Anders vertrouwde webstack met SQL en expliciete beperking “conceptueel equivalent”.

**Requirements:** Bevoegde rol, geldige actieve locatie, versiecheck, redenplicht, oude/nieuwe toestand, actor/tijd; onbevoegde directe request moet falen.

**Features:** Lijst van uitzonderingen, detail, correctie, optimistic concurrency conflict, auditweergave, export en teach-back instructie.

**Database:** vehicles(version,location_id), locations(active), corrections(actor,reason,old,new,at); schema fictief en migraties versioned.

**API/integraties:** Simuleer outbound event na correcte transactie; geen echte partnerverbinding. Demo-API-contract met success/forbidden/conflict/validation response.

**Authentication:** Reader/operator/admin met objectscope; APEX authorisations of echte serverchecks. Browserknop verbergen is niet voldoende.

**Logging:** Correlation-ID, actor, businesskey en foutcategorie; audit en technische logs onderscheiden.

**Tests:** Happy, invalid location, unauthorized, stale version, duplicate submit, error after commit. UAT-taak door andere persoon laten uitvoeren.

**Deployment:** Testomgeving met manifest/config, changelog, smoke test en recoverybeperking; geen echte ICO-config.

**Documentatie en README:** CRQ, functionele/technische analyse, rolmatrix, testbewijs, quick guide en README met bekende beperkingen.

**Screenshots/diagrammen:** Architectuur en state diagram, screenshots van happy path, conflict en audit.

**Wat dit bewijst:** Requirements vertalen, portaal bouwen, rights/validatie, dataconsistentie, gebruikersopleiding en releasebewustzijn.

**Definition of done:** clone/setup reproduceerbaar, positieve en negatieve tests draaien, één failure live demonstreren, businessresultaat uitleggen, beperkingen eerlijk labelen en concrete vacancy-IDs in README.


## Project 3 — Terminal Integration & Cutover Workbench

**Omvang:** Flagship: 3–5 weken afgebakend bij relevante basis; geen gegarandeerde leertijd. **Vacaturekoppeling:** R06/R07/R08/R12/R16/R17/R18/R19/R20/R23/R24/R25/R26/R35.

**Probleem:** Oud/nieuw oefen-TOS, partnerberichten en rapporten moeten bij cutover consistent blijven.

**Businesscase:** Een aantoonbaar beheersbare migratie en incidentrespons met traceerbaarheid, geen alleen mooi dashboard.

**Architectuur:** Partner simulator → integratieflow → old/new SQL schemas → report/reconciliation; app/API + browserworkbench; background processing indien nodig. iWay/JBoss/APEX only if licensed/sandbox available.

**Technologie:** Eigen bekende backend + SQL + testqueue of durable outbox als ontwerpkeuze. Oracle/JBoss-lab optioneel. Geen claim van echte TOS/iWay/WebFOCUS-ervaring zonder die producten.

**Requirements:** Ten minste 100 synthetische events, unieke businesskeys, valide transitions, rejection, retry/backoff, scope per site, fixed snapshot, in-flight delta en go/no-go gates.

**Features:** Message trace, backlog/oldest age, replaypreview, duplicate-safe verwerking, verschillen per key/field, cutover rehearsal en incidenttimeline.

**Database:** vehicles, locations, events, audit, outbox, processing_attempts, migration_runs, reconciliation_diffs; constraints en transacties explicit.

**API/integraties:** Inbound arrival/location/dispatch simulator; ACK na commit, timeoutinjectie, malformed date, reordered events en partnerroutewissel.

**Authentication:** Reader/operator/releaseapprover met server/objectscope; replay en go-livebesluit gescheiden. Audit is lokaal demo-bewijs, geen complianceclaim.

**Logging:** Trace IDs over componenten, first failure, mapping/schema/appversie, timer en businessoutcome; geen fake uptime KPI.

**Tests:** Duplicate/concurrent replay, timeout-after-commit, partial migration, invalid transition, unauthorized site, queue stall en recovery; reconciliatiegate stopt go-live bij verschillen.

**Deployment:** Reproduceerbare dev/test; CI-build/tests als portfoliofeature. Rehearsed release + incompatible migration-case; forward fix/restore verschillen expliciet.

**Documentatie en README:** README als ingang, componentcatalogus, contract, CRQ, zes werkpakketten, risicolog, fictieve budgetforecast, releaseplan, runbooks, post-mortem en wekelijkse businessupdate.

**Screenshots/diagrammen:** Architecture/state diagram, trace screenshot, diff-report en readinessmatrix. Film 3-minuten-demo met één injected failure.

**Wat dit bewijst:** Business/system thinking, SQL/integratie, gecontroleerde delivery, vendor simulation, incidentmanagement en beide-site scope. Begrens enterpriseclaims en laat gaps zien.

**Definition of done:** clone/setup reproduceerbaar, positieve en negatieve tests draaien, één failure live demonstreren, businessresultaat uitleggen, beperkingen eerlijk labelen en concrete vacancy-IDs in README.

<a id="18"></a>

# DEEL 18 — Bewijsmatrix

**Persoonlijk profiel ontbreekt.** Geen CV/GitHub/zelfscore aangeleverd. “Niet beoordeeld” betekent onbekend, niet onbekwaam. Vul in de app bewijslinks en huidig niveau in. Er wordt niets automatisch uit je GitHub geïnterpreteerd. Om later te personaliseren zijn projectlink, eigen bijdrage, gebruikte techniek, context (werk/lab), datum en resultaat nodig.

| Requirement | Mijn bewijs | Wat ontbreekt nog? | Bouwen/leren |
|---|---|---|---|
| R01 — Permanente functie, Zeebrugge, 38 uur | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Praktische afspraak met HR/ICO; geen portfoliobewijs nodig |
| R02 — IT-master of bachelor gelijkgesteld door ervaring | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Praktische afspraak met HR/ICO; geen portfoliobewijs nodig |
| R03 — Dagshift, beperkte verplaatsingen en wachtdienst | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Praktische afspraak met HR/ICO; geen portfoliobewijs nodig |
| R04 — Integriteit, intensiteit, innovatie | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Meld risico’s vroeg; beloof geen onbewezen oplossing. |
| R05 — Arbeidsvoorwaarden en opleidingsmogelijkheden | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Praktische afspraak met HR/ICO; geen portfoliobewijs nodig |
| R06 — Technische projectplannen beheren en rapporteren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Maak mijlpalen, eigenaar, risico’s, planning en wekelijkse status. |
| R07 — Externe bedrijven aansturen | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Specificeer deliverables, acceptatie, deadlines en escalaties. |
| R08 — Core-systemen en nieuw Terminal Systeem | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Leg datastromen vast; plan migratie, test en herstel. |
| R09 — Kwaliteit, veiligheid en milieu ondersteunen | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Bespreek foutieve data, toegang, traceerbaarheid en veilige workarounds. |
| R10 — Specificaties toetsen aan strategie/procedures/standaarden | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Controleer ontwerp, security, lifecycle en changevoorwaarden. |
| R11 — Bijstaan in behoeftenanalyse | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Observeer huidige werkwijze; maak acceptatiecriteria. |
| R12 — Lastenboek, werkpakketten en CRQ | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Beschrijf scope, interfaces, tests, uren, rollout en rollback. |
| R13 — Implementatie begeleiden | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Volg issues en afhankelijkheden; organiseer acceptatie en nazorg. |
| R14 — Gebruikers opleiden | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Maak taakgerichte demo, oefencases en korte werkinstructie. |
| R15 — Outsourcing coördineren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Leg eigenaarschap, toegang, overdracht en exitdocumentatie vast. |
| R16 — Capaciteit en budget bewaken | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Vergelijk forecast/actual, scope en resterend werk; escaleer afwijkingen. |
| R17 — Applicatiecomponenten in kaart brengen/analyseren/evalueren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Maak componentcatalogus met eigenaar, versie en interface. |
| R18 — Releases op servers/systemen met partners coördineren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Gebruik releasekalender, compatibiliteitsmatrix en go/no-go. |
| R19 — TOS met IBM P-series, AIX, Oracle en JBoss | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Traceer gebruiker → applicatie → query; stem platformproblemen af. |
| R20 — EDI-processing en rapportering met WebFOCUS/iWay | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Volg bericht van ontvangst tot businessresultaat; controleer rapportdefinities. |
| R21 — Webportalen opzetten en beheren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Beheer configuratie, permissies, tests, certificaten en releasebewijs. |
| R22 — Nieuwe functionaliteit en koppelingstools ontwikkelen | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Implementeer kleine wijziging met contract, validatie en logging. |
| R23 — Projectportefeuille beheren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Orden op impact, afhankelijkheden, risico en beschikbare mensen. |
| R24 — Afwijkingen proactief vinden en bijsturen | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Vergelijk voortgang met baseline en stel opties met gevolgen voor. |
| R25 — Tweede lijn incident/problem/change tot afronding | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Prioriteer, onderzoek, communiceer, herstel en documenteer oorzaak. |
| R26 — Wekelijks IT en business rapporteren | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Meld resultaat, risico, budget/capaciteit, besluit en volgende stap. |
| R27 — Intern/extern ontwikkelingsteam en training nieuwe collega’s | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Doe review, overdracht en begeleid een collega met echte oefencase. |
| R28 — IT-evoluties volgen; technische kennis en analyse | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Vergelijk lifecycle, kosten en operationele haalbaarheid. |
| R29 — PRINCE2 of andere projectmethode | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Gebruik businesscase, fasering en tolerantie; certificaat niet expliciet vereist. |
| R30 — MS Office en gerelateerde producten | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Gebruik Excel voor reconciliatie, Word voor CRQ, presentatie voor opleiding. |
| R31 — Apex | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Oefen formulieren, SQL-rapporten, validatie en rechten. |
| R32 — Talen N/E/F | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Leg incident uit, lees documentatie en voer leveranciersoverleg. |
| R33 — Communiceren, organiseren, stress en taakgericht leidinggeven | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Prioriteer transparant; benoem eigenaar en updatefrequentie. |
| R34 — Supervisor/Director IT; projectcoördinator/business/klanten/leveranciers | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Maak beslisrechten, escalatie en communicatie per doelgroep duidelijk. |
| R35 — Applicatieomgevingen Kallo én Zeebrugge | Niet beoordeeld; invullen | Bewijs/niveau onbekend | Test locatieconfiguratie en operationele afhankelijkheden per site. |

Bewijssterkte: definitie kunnen uitleggen < oefenresultaat < reproduceerbaar project met negatieve tests < eigen professionele bijdrage met resultaat. Een credential ondersteunt een basis; bewijst geen productievaardigheid. Gebruik geen vertrouwelijke gegevens in een openbaar portfolio. De tracker bewaart bewijs uitsluitend lokaal; een export is door jou te beheren.

<a id="19"></a>

# DEEL 19 — Gap analysis

**Waarschijnlijk / afgeleid uit functiecontext — raamwerk; jouw gaps zijn nog niet vastgesteld.** Vul eerst niveau en bewijs in, dan bepaal je gewicht. Niet iedere onbekende stacknaam is een selectieblocker.

| Gap | Herkenning | Gewicht voor deze vacature | Gerichte oplossing | Wachten met solliciteren? |
|---|---|---|---|---|
| Knowledge gap | Ik kan begrip niet uitleggen | Hoog bij SQL/EDI/incident/release; minder zwaar bij intern TOS-product | Begrip + kleine flow tekenen + één negatieve oefening, 2–8 uur per concept | Bij kernconcepten snel basis leggen; onbekend product niet automatisch blocker |
| Practical gap | Ik begrijp maar deed het weinig | Hoog bij data/troubleshooting/requirements | 1–7 dagen lab met foutinjectie en testbewijs | Solliciteren parallel kan; wees eerlijk over begeleiding |
| Experience gap | Geen professionele productie-/vendorcase | Middel–hoog afhankelijk van gewenst zelfstandigheidsniveau | Transfercase + portfolio + expliciet buddy-/mandaatgesprek | Niet automatisch wachten; ICO moet instapniveau beoordelen |
| Credential gap | Diploma/certificaat ontbreekt | Opleiding expliciet relevant; PRINCE2-certificaat niet verplicht vermeld | Echte opleiding/ervaring tonen en equivalentie bespreken | Diploma-eis kan blocker zijn; HR verifiëren, geen zelfverklaarde gelijkstelling |
| Confidence gap | Ik kan het maar leg het onduidelijk uit | Hoog omdat communicatie essentieel is | STAR/evidence pack, 30s/2min oefenen, collega-feedback | Nee, oefenen tijdens sollicitatie |

## Per gap drie vragen

1. Is het letterlijk vereist, afgeleid of slechts mogelijke tooling?
2. Ontbreekt begrip, uitvoerbaarheid of alleen bedrijfscontext?
3. Welk bewijs toont een veilige start en welke begeleiding blijft nodig?

## Voorbeelden

**Geen iWay-productervaring, wel integratietool gebouwd:** laat mapping, logging, ACK en idempotentie zien. Vraag training op iWay; claim geen productexpertise. **Geen Oracle, wel relationele SQL:** goede transfer maar datatype/tooling/PLSQLverschillen moeten nog geoefend. **Geen incidentervaring:** een sterk failure-lab helpt, maar vervangt geen productie-escalatie; bespreek shadowing vóór wachtdienst. **Slecht Frans:** gewicht hangt af van concrete taak en taalniveau; oefen incidentupdate en vraag verwachting.

Je grootste persoonlijke risico kan pas met profiel/evidence worden bepaald. Deze app geeft een voorbereidingskaart, geen selectiegarantie.

<a id="20"></a>

# DEEL 20 — Gericht leerplan

**Waarschijnlijk / afgeleid uit functiecontext.** Bandbreedte: 2–3 gerichte uren per dag naast werk indien basiskennis aanwezig is; minder basis betekent langer, niet een magische 7-dagenkwalificatie. Dag 1–7 is één crash course; week 1 vat die samen, geen extra leerweek. Solliciteren kan parallel. Learning roadmap is voorbereiding; het 30/60/90-plan in hoofdstuk 23 is voor ná indiensttreding.

Stop zodra je het concrete deliverable met negatieve test en uitleg kunt laten zien; besteed resterende tijd aan volgende kritieke gap. Productlicenties ontbreken? Gebruik een conceptlab en benoem transferbeperking.

| Dag/week | Onderwerp | Theorie | Praktijk | Deliverable | Leerdoel | Goed genoeg |
|---|---|---|---|---|---|---|
| Dag 1 | Rol en keten | V1, componentlagen, RoRo/procesbasis | Teken één fictieve voertuigflow; markeer zeker/onzeker | 1 pagina rolkaart + 10 interviewvragen | Rol zonder jargon uitleggen | Je noemt 5 outputs, 5 onzekerheden en owners. |
| Dag 2 | SQL en datakwaliteit | Keys, joins, nulls, datum, transaction | Maak 20 synthetische records met duplicates/nulls | 5 queries + expected resultaten | Read-only afwijkingen vinden | Je verklaart rijvermenigvuldiging en gebruikt parameters. |
| Dag 3 | EDI en veilige retry | Transport/ACK/commit, mapping, idempotentie | Verwerk valide/duplicate/malformed samples | Message trace en replaytest | Ontvangst van businessresultaat onderscheiden | Replay geeft geen dubbel effect; verschilset klopt. |
| Dag 4 | Troubleshooting | Impact/scope/hypothesen/bewijs | Los login, mapping en traag rapport hardop op | 3 incident/evidence packs | Eerste foutgrens en owner kiezen | Twee hypotheses, veilige test en gebruikersvalidatie per case. |
| Dag 5 | Requirements en CRQ | Businessvraag, acceptance, impact/recovery | Schrijf locatiecorrectie inclusief rechten/conflict | CRQ + 6 work packages + testmatrix | Technische opdracht aan partner geven | Onbevoegde actie en timeout zitten in acceptance. |
| Dag 6 | Portal en runtime | APEX-route/JBoss/database; security | Bouw kleine demo of verifieer auth/validatie in lab | Werkende taakflow of gecontroleerde repro | Laagbegrip aan praktisch bewijs koppelen | Je toont één happy en twee foutpaden, geen fake productclaim. |
| Dag 7 | Interview en bewijs | STAR, bekende/onbekende facts, positioning | Oefen 8 vragen en 2 scenario’s met timer | README, gap-top-3 en 30s/2min verhaal | Solliciteren met eerlijk concreet bewijs | Je rolverhaal, casus en 10 ICO-vragen zijn helder. |
| Week 1 / dagen 1–7 | Crash course afronden | De zeven onderwerpen hierboven | Elke dag 2–3 gefocuste uren, meer indien basis ontbreekt | Project 1 eerste versie + bewijskaart | 80/20-basis zonder rabbit holes | Crash-output compleet, onzekerheden zichtbaar. |
| Week 2 / dagen 8–14 | SQL/EDI verdiepen | Atomiciteit, ordering, ACK en reconciliation | Project 1 test met parallelle duplicates en partial failures | Testlog + runbook + incidentrapport | Zelfstandig kleine flow onderzoeken | Je kunt onverwachte input veilig uitleggen en herhalen. |
| Week 3 / dagen 15–21 | Portaal en gebruikersflow | APEX indien bevestigd, validatie/rollen/audit | Project 2 bouwen; iemand anders doet UAT | Portal + CRQ + quick guide | Businessvraag gecontroleerd opleveren | Unauthorized, stale version en invalid location getest. |
| Week 4 / dagen 22–30 | Release en interview | Manifest, compatibility, recovery, stakeholders | Demo-uitrol/recovery, 16 interviewvragen en 5 scenario’s | Release evidence + CV-projectbeschrijving | Voldoende bewijs voor inhoudelijk gesprek | Je zegt precies wat je wel/niet zelfstandig gedaan hebt. |
| Week 5 / dagen 31–37 | Runtime/platformdiagnose | JBoss pools/exceptions en Unix/AIX-laag | Simuleer permission/datasource/diskprobleem veilig | 3 laag-evidence packs | Gericht specialist inschakelen | Eerste fout en benodigde meting zijn helder. |
| Week 6 / dagen 38–44 | Vendor en capaciteitssturing | Work packages, forecast en acceptance | Simuleer leverancier die extra scope/uren vraagt | Actielog, risk log, budgetforecast | Businessbesluit onderbouwen | Twee opties met consequenties en eigenaar. |
| Week 7 / dagen 45–51 | Flagship verticale flow | Outbox/retry/backlog als ontwerpopties | Project 3 één partner/site end-to-end bouwen | Trace + duplicate-safe verwerking | Keten met foutpaden bewijzen | Timeout na commit levert geen dubbel business-effect. |
| Week 8 / dagen 52–60 | Cutover/reconciliatie | Snapshot, in-flight, key/field differences | Project 3 old/new schema en cutovergate | Rehearsal + go/no-go-matrix | Datamigratie op bewijs beoordelen | Bij ontbrekend record stopt demo go-live met uitlegbare reden. |
| Week 9–10 / dagen 61–74 | Observability en hardere scenario’s | Business health, metrics, first failure, exposure | Queue stall, retry-storm, multi-site en scopeleak lab | 4 post-mortems + monitorregels | Breder risico overzien zonder expertclaim | Je meet businessuitkomst en bewaart bewijs veilig. |
| Week 11–12 / dagen 75–88 | Overdracht en sollicitatieverdieping | Training, rapportdefinities, eigen bewijsverhaal | Demo met key-userrol, 20 vragen/10 scenarios en CVreview | Complete README, teach-back, skillsupdate | Resultaat begrijpelijk aan diverse stakeholders tonen | Iemand kan setup/taak uitvoeren zonder jouw live hulp. |
| Dagen 89–90 | Herijk en beperk scope | Risico-/ROI-afweging | Audit bewijs tegen R01–R35, kies resterende top-3 gaps | Definitieve proof matrix en next steps | Leren richten op echte vacature | Geen open kritiek foutpad; onbekende company facts blijven onbekend. |

<a id="21"></a>

# DEEL 21 — Wat moet ik niet leren?

**Waarschijnlijk / afgeleid uit functiecontext.** Deze afbakening is voor voorbereiding, geen vrijstelling van werkelijk toegewezen werkzaamheden.

| Voorlopig niet diep leren | Voldoende startniveau | Waarom | Wanneer wel verdiepen? |
|---|---|---|---|
| IBM Power firmware/HMC/SAN | Hardware/OS/app onderscheid, capacitysymptomen | Geen volledige hardwarebeheerrol vermeld | Als beheer expliciet aan jou toegewezen wordt |
| AIX kernel-/paging tuning | Processen, disk, rechten, resources herkennen | Specialistische ingrepen met risico | Met runbook, producttraining en beheerowner |
| Oracle RAC/Data Guard/optimizerinternals | SQL/transacties, plan/locks kunnen bespreken | DBA-specialisme niet expliciet gevraagd | Als ownership en doelen bevestigen |
| Volledige Jakarta EE-/Java-specificatie | Runtime/pool/exception/config, kleine codeflow | Programmeertaal/depth onbekend | Concrete codebase vraagt dit |
| Alle EDIFACT/X12-segmenten, AS2-crypto | Contract/mapping/ACK/retry | Standaard/transport onbekend | Werkelijke partnercontract bevestigt |
| Alle WebFOCUS-syntax/plugins | Rapportdefinitie, filters, joins, refresh | Productversie onbekend | Actual reportbeheer met productlab |
| Alle iWay-adapters | Bestaande flow en foutpad begrijpen | Universeel platformexpert niet nodig | Specifieke adapterwerkpakketten |
| PRINCE2-certificatiememorisatie | Businesscase/workpakket/risico/tolerantie gebruiken | Certificaat niet als vereiste genoemd | ICO/careerdoel vraagt credential |
| Cloud/Kubernetes/microservices | Hostingconcepten herkennen | Niet genoemd in vacature | Na architecture validation |
| Geavanceerde frontendanimatie | Bruikbare formulier-/rapportflow | Business/reliability weegt zwaarder | Echte UXvraag met meetbare waarde |
| VBA/complexe Officeautomatisering | Betrouwbare sheet en status/instructie | Basisproductiviteit volstaat vaak | Herhaalde taak levert duidelijke ROI |

**On the job:** lokale statuscodes, TOS-product, servers, credentials, leveranciers-SLA, tickettool, rapportcatalogus, safetyregels en interne CRQ-goedkeuring. Kun je nu niet publiek leren. Niet wachten met solliciteren vanwege ontbrekende interne kennis.

**Rabbit holes:** dagen zoeken naar fictieve ICO-cloudarchitectuur, elk product installeren zonder concrete taak, een perfecte enterpriseclone bouwen, of meer certificaten verzamelen terwijl SQL/incident/requirements-praktijk ontbreekt. Stopregel: leer iets alleen als het een R-ID, kritieke oefencase of bevestigd kennistekort oplost.

<a id="22"></a>

# DEEL 22 — Sollicitatiestrategie

**Persoonlijk oordeel nog niet mogelijk:** CV en projectbewijzen ontbreken. Onderstaand advies is conditioneel, niet “je bent klaar”.

1. **Voor alles kennen solliciteren?** Ja als je kernanalyse, betrouwbaar deliverygedrag, voldoende IT-basis en duidelijke leerbaarheid kunt bewijzen en de praktische context past. Productgaps eerlijk bespreken.
2. **Echte mogelijke blockers:** onhaalbare wachtdienst/verplaatsing, niet passend opleidingsniveau zonder aanvaarde ervaringsequivalentie, onvoldoende essentiële communicatie, geen veilige data-/incidentbasis of behoefte aan veel begeleiding waar ICO volledige zelfstandigheid verwacht. HR/hiring manager beslist.
3. **Normale gaps:** specifieke TOS, productversies, interne processen en één enterpriseproduct niet professioneel gebruikt. Gewicht hangt van onboarding en teamdekking af.
4. **Positionering:** probleemoplosser die data, gebruikers en technische uitvoering verbindt. Niet alleen een lijst frameworknamen.
5. **Benadrukken:** echte analyse-, SQL-, integratie-, support-, project-/stakeholder- en opleverervaring met eigen bijdrage en resultaat.
6. **Minder benadrukken:** niet-gerelateerde UI-trends, losse cursuscertificaten zonder toepassing en algemene “ik ben gemotiveerd”-claims.
7. **CV:** profiel in 3 regels, relevante skills met eerlijke niveaus, 2–3 bullets per passend project (probleem → jouw actie → resultaat), portfolio-ID/koppeling en talen/diploma/mobiliteit feitelijk.
8. **Motivatiebrief:** RoRo-context uit publieke bron, hybride rolfit, één bewijsvoorbeeld, gerichte productgap met aanpak en uitnodiging om startverwachtingen te bespreken.
9. **GitHub:** Project 1 voor data/EDI, Project 2 voor portaal/requirements, Project 3 voor chain/release. Een goede README/testcase telt meer dan aantal repos.
10. **Onbekende onderwerpen:** “Ik heb X nog niet professioneel gebruikt. Ik heb Y gedaan dat dezelfde concepten raakt; hier is bewijs. Voor X heb ik taak Z geoefend en heb ik voor productie nog begeleiding op A/B nodig.”

## Positioning statement — personaliseer feitelijk

“Ik ben interessant voor deze rol omdat ik technische problemen kan structureren, gebruikersvragen naar testbare oplossingen kan vertalen en betrouwbaar kan opleveren met duidelijke communicatie. Dat onderbouw ik met [echt project/casus en mijn bijdrage]. Ik beheers niet elk genoemd enterpriseproduct op professioneel niveau; voor [echte gap] heb ik een gericht oefenplan en benoem ik de benodigde startbegeleiding. Ik combineer praktisch bewijs met de bereidheid de lokale terminalprocessen zorgvuldig te leren.”

## Bestaande ervaring vertalen

Webdevelopment → servervalidatie, rollen, API’s, tests en releases. Datawerk → SQL/reconciliation/rapportdefinities. Support → impact/scope/communicatie. Projectwerk → requirements, planning en acceptance. Ondernemerschap → ownership en klantwaarde, maar geen automatisch bewijs van enterprisebeheer. Alleen gebruiken als de ervaring werkelijk bestaat.

## Voorbeeld-CVbullet als template

“Bouwde [eigen synthetische EDI-lab] met duplicate-safe verwerking en sleutelreconciliatie; testte [eigen negatieve cases] en documenteerde [runbook]. Portfolio, geen productie-ICO-omgeving.” Vervang placeholders met bewijs; schrijf geen verzonnen impactpercentage.

<a id="23"></a>

# DEEL 23 — 30 / 60 / 90 dagen na start

**Waarschijnlijk / afgeleid uit functiecontext — voorstel voor onboarding, geen ICO-beoordelingsnorm.** Stem milestones af op toegang, projectfase, changevensters en team. Productierechten en wachtdienst-readiness komen niet vanzelf met een kalenderdatum.


## Eerste 30 dagen — Begrijpen en veilig bijdragen

**Werk en contacten:** Supervisor/Director, Service Desk, projectcoördinator, key users per site en component-/vendorowners spreken. Toegang, omgeving en escalatie oefenen. Eén belangrijke businessflow en componentkaart valideren. Shadow minstens enkele representatieve tickets, afhankelijk van beschikbaarheid. Kleine documentatiefix of read-only reconciliatie onder review.

**Milestones / bewijs:** Gevalideerde rol/RACI, proces- en componentkaart, toegang/checklist, twee gereviewde evidence packs en top-5 risico’s. Zelfstandig uitleggen wie welke productieactie mag doen. Wachtdienst alleen na afgesproken readiness.

## Dag 31–60 — Afgebakend zelfstandig uitvoeren

**Werk en contacten:** Binnen mandaat enkele tweede-lijncases afhandelen, één CRQ/werkpakket coördineren, partnerfix in test valideren, kleine portal/toolchange opleveren en gebruikersinstructie bijwerken. Weekrapport met risico/capacity/budget.

**Milestones / bewijs:** Een geaccepteerde change met test/release/recoverybewijs, incidentafsluiting met data/gebruikersvalidatie en buddyfeedback. Nog geen onbewezen totale TOS-eigendom.

## Dag 61–90 — Ownership van een duidelijk domein

**Werk en contacten:** Met supervisor afgebakend component/integratie/projectwerkpakket opnemen. Eén herhaald probleem structureel oplossen, monitoring/documentatie verbeteren en een release met partners coördineren.

**Milestones / bewijs:** Domein-eigenaarschap afgesproken, runbook door collega bruikbaar, problemactie met effectbewijs, betrouwbare forecast en gepresenteerde 90-dagenreview. Nieuwe doelen op werkelijke prioriteiten.

## Reviewvragen aan supervisor

Wat kan ik al zelfstandig, welke fouten/risico’s vermijd ik goed, waar is nog review nodig, welke outputs helpen het team en welke verantwoordelijkheid moet de komende maand groeien? Noteer besluiten en opvolging. Geen performancepercentage verzinnen.

<a id="24"></a>

# DEEL 24 — First week survival guide

**Waarschijnlijk / afgeleid uit functiecontext.** Begin als collega die zorgvuldig leert en kleine waarde levert.

| Dag | Vragen en contacten | Toegang / systemen | Documenteren / deliverable |
|---|---|---|---|
| 1 | Supervisor: scope, prioriteiten, mandaat; Service Desk: escalatie/rooster; safetyintro | Werkplek, e-mail, ticketing/docs, trainingsomgeving; echte toolnamen navragen | Contact-/escalatiekaart, begrippenlijst en “wat mag ik al doen?” |
| 2 | Key user: toon één ontvangst/locatie/vertrektaak; vraag fouten en fysieke gevolgen | Read-only demo/businessflow, geredigeerde voorbeelddata | Proceskaart met bron van waarheid en drie open vragen |
| 3 | Componentowner: traceer dezelfde taak; vendor: supportgrens | TOS/app/log/read-only DB indien goedgekeurd; omgeving altijd labelen | Eerste gevalideerde component/dataflowkaart, loglocaties en versies |
| 4 | Buddy: neem een ticket door; changeowner: CRQ en releasevoorbeeld | Testomgeving, releasebewijs, monitoring en herstelprocedures | Evidence pack van geshadowd ticket en recoveryvragen |
| 5 | Supervisor/key user: samenvatting en feedback; kies kleine volgende taak | Toegangscheck/escaleer ontbrekende rechten; geen privilege-omzeiling | Weekrapport: wat geleerd, open risico’s, taak/owner voor week 2 |

## Toegangschecklist — uitsluitend via bevoegde eigenaar

- [ ] Omgevingen, hosts/endpoints en labels duidelijk: test ≠ productie.
- [ ] Ticketing, documentatie, componentcatalogus en releasehistorie.
- [ ] Log/monitoring en read-only databron waar nodig.
- [ ] Ontwikkel-/versieomgeving en sandbox volgens taak.
- [ ] Contact voor Service Desk, infra/DB, vendor en securityincident.
- [ ] Toegangs-/secretprocedure, minimale rol en audit.
- [ ] Wachtdienstrooster, bereikbaarheid en readinesscriteria.
- [ ] Lokale kwaliteit-, veiligheids- en milieuregels.

## Nog niet proberen veranderen

Geen productiestatussen, autorisaties, mappings, database/schema, runtime/platformconfig, vendorroute, logretentie of releasebeleid veranderen zonder context en mandaat. Niet de hele architectuur vervangen na eerste indruk. Wel inconsistente documentatie signaleren, veilige vragen stellen en één kleine gereviewde verbetering voorstellen.

## Eerste-week-notitieformat

Taak → businessdoel → componenten → eigenaar → input/output → foutpad → logbron → procedures → open vraag. Laat buddy het document corrigeren. Een eerlijk “onbekend” is betrouwbaarder dan een onjuiste ingevulde pijl.

<a id="25"></a>

# DEEL 25 — Performance playbook: 6–12 maanden

**Waarschijnlijk / afgeleid uit functiecontext.** “Top 10%” is een gedragsprofiel, geen gemeten ICO-ranking. Groei gaat over effect en betrouwbaarheid, niet overal expert worden.

| Dimensie | Gemiddelde uitvoering | Sterke / top 10%-uitvoering | Concreet bewijs |
|---|---|---|---|
| Ownership | Eigen taak af, vervolg onbekend | Volgt ketenresultaat, overdracht en open acties | Geaccepteerde delivery en gesloten nazorg |
| Betrouwbaarheid | Werkt snel, status soms laat | Realistische belofte, vroeg risico, gecontroleerde changes | Geen verrassingen in forecast/updates |
| Communicatie | Technische details naar iedereen | Impact/besluit voor business, evidence voor techniek | Zelfde incident helder voor twee doelgroepen |
| Documentatie | Notities alleen voor zichzelf | Runbook reproduceerbaar, eigenaar/versie en foutpad | Collega gebruikt zonder live begeleiding |
| Troubleshooting | Bekende fix herhalen | Bewijs, tegenhypothese en veilige validatie | Root cause/test/reconciliatie aantoonbaar |
| Businesskennis | Schermen kennen | Fysieke proces en statusbetekenis begrijpen | Betere acceptance en minder verkeerde aannames |
| Automatisering | Handmatig terugkerend werk | Kleine veilige tools met review/test/audit | Reconciliation/check herhaalbaar, echte tijdwinst gemeten |
| Stakeholders | Reageren op vragen | Verwachtingen/owners proactief organiseren | Besluit-/actielog en minder scopeverwarring |
| Proactiviteit | Wachten op incident | Trends en afwijkingen vroeg signaleren | Herhaald probleem structureel weg, monitor erbij |
| Technische kennis | Losse stacknamen | Afhankelijkheden en recoverygrenzen uitleggen | Impactanalyse voorspelt keteneffect |
| Procesverbetering | Procedure volgen | Ontbrekende controle verbeteren zonder bureaucracy | Checklist/test voorkomt herhaalde fout |

## Maandritme

Kies één herhaald probleem en één handmatige check om verantwoord te verbeteren. Verzamel baseline, scopeer klein, maak test/bewijs en bespreek effect. Review je componentcatalogus bij iedere change. Train elk kwartaal iemand op een echte taak. Volg productlifecycle/IT-evoluties met een korte beslissingnotitie: risico, businesswaarde en beheerlast.

## Vermijd heldengedrag

Altijd persoonlijk brandjes blussen zonder kennisoverdracht creëert afhankelijkheid. Sterke ownership maakt ook collega’s effectief. Geen KPI-gaming: minder tickets kan betere preventie of slechtere melding betekenen; interpreteer samen met businessuitkomst.

<a id="26"></a>

# DEEL 26 — Career path

**Waarschijnlijk / afgeleid uit functiecontext — mogelijke loopbanen, geen toegezegd ICO-carrièrepad.** Titels, salarissen en promoties hangen van organisatie/regio/mandaat af. Geen ongeverifieerde salarisbedragen.

| Richting | Verantwoordelijkheid / benodigde kennis | Kwalitatief potentieel / overstap |
|---|---|---|
| Junior/medior application specialist | Afgebakende tickets/changes, dataflow en procedures | Goede basis; meer zelfstandigheid verhoogt waarde |
| Senior application/integration engineer | Complexe keten, structurele fixes, release-/recoveryontwerp | Technisch schaarse businesskennis; overdraagbaar naar logistiek/enterprise |
| Technical lead | Teamreview, kwaliteit, complex werkpakketten en mentoring | Meer invloed; bewijs van coaching en leverbetrouwbaarheid nodig |
| Solution/integration architect | Grenzen, contracts, data ownership, nonfunctionele eisen en migratierisico | Hoog specialistisch potentieel; architectuurkeuzes met bewijs leren |
| IT project/delivery manager | Portefeuille, budget, risico, leveranciers en adoptie | Managementpotentieel; minder zelf bouwen, sterker bestuurlijk mandaat |
| Application manager / service owner | Continuïteit, lifecycle, SLA/contract en teamcoördinatie | Brede operationele verantwoordelijkheid; people/budgetskills ontwikkelen |
| Business analyst / productowner | Procesvragen, value, requirements en backlog | Relatief logische transfer bij sterk businessbegrip; productmandaat is apart |
| Consultant enterprise/logistics IT | Implementaties, klantdiagnose, training en vendorintegratie | Ondernemerswaarde door domein-/ketenexpertise; verkoop/scope/contract leren |
| Head of IT / manager | Mensen, governance, strategie, budget en leveranciers | Langere route met people-management en meerdere deliverydomeinen |

## Overstapbaarheid

SQL, requirements, integraties, support en delivery zijn breed bruikbaar. Zeer productspecifieke knowledge blijft waardevol maar vraagt vertaalslag. Leg AIX/JBoss/iWay-ervaring uit als runtime/OS/integratievaardigheid met concrete beperkingen. Cloudplatformrol of pure frontendfunctie kan extra specifieke bouwervaring vragen.

## Ondernemerswaarde

Problemen kunnen diagnoseren, klanten begrijpen, werkpakketten begrenzen en gecontroleerd opleveren helpt consultancy/toolontwikkeling. Gebruik nooit interne ICO-gegevens, code of afspraken als eigen publiek product zonder bevoegdheid. CTO is geen automatische volgende stap; daarvoor zijn strategie, people, financiën en bredere engineeringleiding nodig.

<a id="27"></a>

# DEEL 27 — Moeilijkheidsgraad

**Waarschijnlijk / afgeleid uit functiecontext — adviesinschatting, geen gemeten werkomgeving of beoordeling van jou.** Score kan dalen met sterke buddy/support of stijgen bij ongedocumenteerde legacy en drukke wachtdienst.

| Dimensie | Score / 10 | Waarom / te verifiëren |
|---|---:|---|
| Technische moeilijkheid | 8 | Meerdere enterprise-lagen, integratie en nieuw TOS; versies/dekking onbekend |
| Programmeerintensiteit | 5 | Functionaliteit/tools expliciet, maar veel beheer/coördinatie; echte uren navragen |
| Analytisch denken | 9 | Keten/data/requirements over meerdere systemen |
| Stress | 7 | Tweede lijn + wachtdienst + live terminalcontext; oproepvolume onbekend |
| Verantwoordelijkheid | 8 | Beide locaties en applicatiecontinuïteit naast vernieuwing |
| Communicatie | 9 | Business, team, leiding, klanten en externe partners |
| Learning curve | 8 | Producten, proces, lokale regels en migratie tegelijkertijd |
| Zelfstandigheid | 8 | Beheren, prioriteren en finaliseren; instapverwachting toetsen |
| Businesskennis | 7 | Terminalproces en statussemantiek nodig; lokale kennis leerbaar |
| Operations/support | 8 | Incident/problem/change en wachtdienst expliciet |

De rol is breed en vraagt volwassen gedrag. Moeilijkheid komt vooral uit afhankelijkheden, risico en communicatie, niet uit maximale algoritmische programmeercomplexiteit. De vacature noemt geen aantal ervaringsjaren; uit breedte alleen mag je geen formele senioriteitsgrens afleiden.

<a id="28"></a>

# DEEL 28 — Red flags / green flags

**Expliciet uit vacature** versus **te verifiëren interpretatie**. Een signalering is geen conclusie over teamkwaliteit.

| Signaal | Waarom interessant | Wat verifiëren? |
|---|---|---|
| Green: intern én extern ontwikkelingsteam genoemd | Potentiële samenwerking en kennisdekking | Teamgrootte, taakverdeling en beschikbare begeleiding |
| Green: opleidingsmogelijkheden | Productgaps kunnen planbaar zijn | Budget, tijd, buddy en echte recente opleiding |
| Green: concrete stack en rapportagelijnen | Meer houvast dan vage algemene IT-rol | Huidige versies, lifecycle en mandaat |
| Green: nieuw TOS/applicatieve vernieuwing | Leren over businessmigratie en controlled delivery | Projectfase, deadlines, testomgeving en data-eigenaarschap |
| Green: integriteit/kwaliteit/veiligheid genoemd | Zorgvuldigheid expliciet relevant | Hoe wordt vroeg risico melden in praktijk behandeld? |
| Green: onbepaalde duur en voordelen | Duidelijke arbeidscontext | Voorwaarden en totale afspraken, geen salarisclaim |
| Aandacht: veel disciplines in één rol | Brede scope kan groei of overbelasting betekenen | Tijdmix, eigenaren en werk-in-uitvoering |
| Aandacht: wachtdienst | Ondersteuning buiten dagshift mogelijk | Oproepvolume, responstijd, vergoeding en backup |
| Aandacht: enterprise/legacyplatformen | Product-/lifecyclecomplexiteit mogelijk | Supportstatus, upgradepad en documentatie |
| Aandacht: huidige continuïteit + nieuw TOS | Twee sporen strijden om capaciteit | Wie vangt support op tijdens projectpieken? |
| Aandacht: budget/vendormanagement | Verantwoordelijkheid zonder mandaat kan frictie geven | Beslisrechten en escalationroute |
| Aandacht: Kallo en Zeebrugge | Sitevarianten en reiscontext | Shared versus lokale config en bereikbaarheid |

Geen bewijs voor “één persoon doet alles”, “permanente brandjes”, “moderne cloudstack”, “duidelijk carrièrepad” of “onrealistische lijst”. Die hypothesen vragen concrete interviewantwoorden. Een goed antwoord bevat voorbeelden, niet alleen “dat is geregeld”.

<a id="29"></a>

# DEEL 29 — Cheat sheet voor het gesprek

**Compacte herhaling — maximaal enkele pagina’s bij print/export.** Alles hieronder is rolgericht; architectuurdetails blijven hypotheses tot bevestigd.

## Rol in één zin

Technische project-/applicatieschakel die terminalsystemen beheert en verbetert, partners coördineert en complexere incidenten afsluit met businessvalidatie.

## Vijf outputs

Technisch CRQ/werkpakket; component-/datastroomkaart; geaccepteerde release; incident/problem-afsluiting met bewijs; opleiding en wekelijkse status. Kallo én Zeebrugge in scope. Dagshift/38 uur, verplaatsingen en wachtdienst expliciet.

## Stack onthouden

TOS = businessapplicatie. IBM P-series = platform. AIX = OS. JBoss = Java runtime/application server. Oracle = relationele data/transacties. iWay = integratie. EDI = businessdata-uitwisseling. WebFOCUS = rapportering. Apex waarschijnlijk Oracle APEX = databasegerichte webapps; eerst bevestigen. MS Office en N/E/F ook genoemd. PRINCE2 of andere methode.

## Keten en jargon

Input → validatie → mapping → businessregel → commit → ACK → rapport. ACK = bevestiging, betekenis uit contract. Idempotentie = herhalen zonder dubbel business-effect. Reconciliatie = sleutel/veld/meaning vergelijken. CRQ = change request. UAT = gebruikersacceptatietest. Cutover = overgang. Rollback = terugzetten, met data/schema-beperking. Source of truth = gezaghebbende bron per gegeven.

## Incidentstappen

Impact/veiligheid → scope/tijd → sample/ID → laatste goede grens → recente changes → hypotheses/veilige tests → bevoegd herstel → business/data/partnercontrole → monitoren → documenteren/problem-link. Geen blind restart, bulk-replay, DELETE of productie-UPDATE.

## Procesonderscheid

Incident herstelt; problem voorkomt herhaling; change beoordeelt/autoriseert wijziging; release bundelt compatibele versies; deployment voert plaatsing uit. Gebouwd ≠ getest ≠ geaccepteerd ≠ productie gevalideerd.

## Interview vijf ankers

1. Leg architectuur uit en label aannames.
2. Diagnose met twee hypotheses en één onderscheidende test.
3. Timeout na commit kan duplicaat veroorzaken.
4. Requirements omvatten rechten, validatie, conflict, audit en foutpad.
5. Eigen ervaring exact labelen: werk/lab/theorie/met hulp/zelfstandig.

## Zelf vragen

Nieuw/huidig TOS en fase; werkmix/codebase; versies/owners; wachtdienst/backup; onboarding/buddy; productie-/budgetmandaat; release/recovery; grootste risico; 90-dagenoutputs; training/documentatie.

## Niet vergeten

Publieke ICO-context is RoRo/automotive, geen containerterminal aanname. Topology/cloud/EDI-standaard/teamgrootte/salaris onbekend. Kritieke voorbereiding: SQL/data, troubleshooting, requirements, communicatie, vendor/release. Productexpertise overal is geen startvereiste, veilig gedrag wel.

<a id="30"></a>

# DEEL 30 — Final assessment en acties

**Waarschijnlijk / afgeleid uit functiecontext.** Geen persoonlijke geschiktheidsbeoordeling zonder CV/portfolio en geen garantie op sollicitatiesucces.

## Hoe goed begrijp ik de rol als ik dit beheers?

Je begrijpt het functiepatroon, bevestigde verantwoordelijkheden, waarschijnlijke ketenrisico’s en het soort output dat een medewerker levert. Je kunt een inhoudelijk gesprek voeren, oefeningen plannen en een gecontroleerde eerste werkperiode voorstellen. Het interne systeem, lokale regels en productievaardigheid vereisen begeleiding/praktijk. Lezen is kennis; zelfstandig oplossen met bewijs is vaardigheid.

## Tien dingen die ik moet kunnen

1. Roloutputs en de grenzen van mijn mandaat uitleggen.
2. Een businesshandeling door componenten en data volgen.
3. SQL-afwijkingen en sleutelreconciliatie read-only uitvoeren.
4. Incidentimpact/scope en veilige first steps bepalen.
5. Meerdere hypotheses toetsen met relevant bewijs.
6. EDI-commit/ACK/retry/duplicaten correct verklaren.
7. Businessvraag naar requirements/acceptance/werkpakket vertalen.
8. Release, schema/data en herstelrisico coördineren.
9. Business/leverancier/leiding passend informeren en gebruikers trainen.
10. Eigen kennisniveau en resterende gaps eerlijk met bewijs positioneren.

## Vijf grootste mogelijke risico’s — nog niet persoonlijk vastgesteld

Te weinig kernpraktijk ondanks theorie; onderschatte wachtdienst/brede scope; te snel productie-ingrijpen; techfocus zonder terminalproces; product/labervaring sterker voorstellen dan zij is. Mitigatie: failure-labs, concrete teamvragen, mandaat/recovery, processhadowing en eerlijke proof matrix.

## Vijf kansen

Brede enterprisevaardigheid; echte business-impact begrijpen; TOS-vernieuwing als leerschool; integratie/dataexpertise opbouwen; doorgroeien naar lead/architect/delivery of consulting. Geen van deze is een gegarandeerd ICO-traject.

## Deze week — prioriteit

1. Lees bronstatus en hoofdstukken 1/2/5; schrijf rol in eigen woorden en 10 onbekenden.
2. Vul je niveau/bewijs voor SQL, incident, requirements en communicatie in de tracker.
3. Bouw Project 1 met malformed/duplicate/timeouttest en heldere README.
4. Schrijf één CRQ en één evidence pack; laat iemand kritisch doorvragen.
5. Oefen acht interviews en twee scenario’s met timer; noteer drie verbeteringen.
6. Pas CV/motivatie feitelijk aan en selecteer tien vragen aan ICO.
7. Als praktische/diploma/kernbasis passen, solliciteer parallel aan gericht leren; vraag instapverwachting en begeleiding expliciet.

## Beheersingstest

Laat een collega een onbekende payloadfout, statusconflict en releaseprobleem kiezen. Kun je impact, bewijs, hypothesen, veilige aanpak, communicatie en preventie uitleggen zonder modelantwoord? Dan begrijp je de werkwijze. Kun je haar reproduceerbaar uitvoeren in lab en lokaal onder begeleiding? Dan groeit praktische readiness. De dashboardvoortgang meet alleen afgevinkte hoofdstukken, niet bekwaamheid.