from pathlib import Path
import json, textwrap

ROOT=Path(__file__).resolve().parents[1]
chapters=[]
def add(n,title,module,body):
    chapters.append(dict(id=n,title=title,module=module,body=textwrap.dedent(body).strip()))

V='[Vacature ICO](https://www.icoterminals.com/nl/jobs/it-development-officer)'
NOTE=f'**Bronstatus:** expliciete verantwoordelijkheden volgen uit {V}. De aanpak, oefeningen, tijdsverdeling en voorbeelden zijn **Waarschijnlijk / afgeleid uit functiecontext**; geen vastgestelde interne ICO-procedures.'

requirements=[
('R01','Permanente functie, Zeebrugge, 38 uur','Een vaste rol met planning over meerdere projecten.','Plan capaciteit op 38 uur; reserveer interruptieruimte.','Basiskennis','Hoog'),
('R02','IT-master of bachelor gelijkgesteld door ervaring','Toon theoretische basis én toepasbare ervaring; precieze diploma-equivalentie navragen.','Koppel opleiding en projecten aan analyse, systemen en delivery.','Intermediate','Hoog'),
('R03','Dagshift, beperkte verplaatsingen en wachtdienst','Regulier dagwerk met beschikbaarheidsverplichtingen; rooster onbekend.','Vraag oproepfrequentie, compensatie, toegang en escalatiedekking.','Intermediate','Kritiek'),
('R04','Integriteit, intensiteit, innovatie','Eerlijk rapporteren, zorgvuldig afwerken en nuttig verbeteren.','Meld risico’s vroeg; beloof geen onbewezen oplossing.','Intermediate','Hoog'),
('R05','Arbeidsvoorwaarden en opleidingsmogelijkheden','Maaltijd/ecocheques, verzekeringen, GSM/laptop, wagen, vergoeding en cafetariaplan worden genoemd.','Vraag voorwaarden, budget en praktische opleidingstijd.','Beginner','Middel'),
('R06','Technische projectplannen beheren en rapporteren','Jij organiseert technische uitvoering en afhankelijkheden.','Maak mijlpalen, eigenaar, risico’s, planning en wekelijkse status.','Gevorderd','Kritiek'),
('R07','Externe bedrijven aansturen','Uitbesteden verwijdert je verantwoordelijkheid voor resultaat niet.','Specificeer deliverables, acceptatie, deadlines en escalaties.','Gevorderd','Kritiek'),
('R08','Core-systemen en nieuw Terminal Systeem','Continuïteit van huidige applicaties naast verandering.','Leg datastromen vast; plan migratie, test en herstel.','Gevorderd','Kritiek'),
('R09','Kwaliteit, veiligheid en milieu ondersteunen','IT-keuzes hebben operationele gevolgen.','Bespreek foutieve data, toegang, traceerbaarheid en veilige workarounds.','Intermediate','Hoog'),
('R10','Specificaties toetsen aan strategie/procedures/standaarden','Een technisch haalbare wijziging moet ook passen in afspraken.','Controleer ontwerp, security, lifecycle en changevoorwaarden.','Gevorderd','Hoog'),
('R11','Bijstaan in behoeftenanalyse','Vraag door naar probleem en gebruikersdoel.','Observeer huidige werkwijze; maak acceptatiecriteria.','Intermediate','Kritiek'),
('R12','Lastenboek, werkpakketten en CRQ','CRQ is het change request: waarom, wat, risico en goedkeuring.','Beschrijf scope, interfaces, tests, uren, rollout en rollback.','Gevorderd','Kritiek'),
('R13','Implementatie begeleiden','Delivery controleren tot het werkend in gebruik is.','Volg issues en afhankelijkheden; organiseer acceptatie en nazorg.','Gevorderd','Hoog'),
('R14','Gebruikers opleiden','Adoptie is deel van technisch succes.','Maak taakgerichte demo, oefencases en korte werkinstructie.','Intermediate','Hoog'),
('R15','Outsourcing coördineren','Organiseer de grens tussen interne en externe uitvoering.','Leg eigenaarschap, toegang, overdracht en exitdocumentatie vast.','Gevorderd','Hoog'),
('R16','Capaciteit en budget bewaken','Bewaken of inspanning en resultaat nog kloppen.','Vergelijk forecast/actual, scope en resterend werk; escaleer afwijkingen.','Gevorderd','Hoog'),
('R17','Applicatiecomponenten in kaart brengen/analyseren/evalueren','Ken componenten, afhankelijkheden en kwetsbare punten.','Maak componentcatalogus met eigenaar, versie en interface.','Intermediate','Kritiek'),
('R18','Releases op servers/systemen met partners coördineren','Versies moeten samen compatibel live gaan.','Gebruik releasekalender, compatibiliteitsmatrix en go/no-go.','Gevorderd','Kritiek'),
('R19','TOS met IBM P-series, AIX, Oracle en JBoss','Bedrijfskritische applicaties op enterpriseplatformen.','Traceer gebruiker → applicatie → query; stem platformproblemen af.','Gevorderd','Kritiek'),
('R20','EDI-processing en rapportering met WebFOCUS/iWay','EDI is gestructureerde gegevensuitwisseling tussen organisaties.','Volg bericht van ontvangst tot businessresultaat; controleer rapportdefinities.','Gevorderd','Kritiek'),
('R21','Webportalen opzetten en beheren','Gebruikersinterfaces met lifecycle en toegangsbeheer.','Beheer configuratie, permissies, tests, certificaten en releasebewijs.','Intermediate','Hoog'),
('R22','Nieuwe functionaliteit en koppelingstools ontwikkelen','Hands-on bouwen maakt deel uit van de functie.','Implementeer kleine wijziging met contract, validatie en logging.','Intermediate','Hoog'),
('R23','Projectportefeuille beheren','Meerdere projecten concurreren om dezelfde capaciteit.','Orden op impact, afhankelijkheden, risico en beschikbare mensen.','Gevorderd','Hoog'),
('R24','Afwijkingen proactief vinden en bijsturen','Niet wachten op mislukte oplevering.','Vergelijk voortgang met baseline en stel opties met gevolgen voor.','Intermediate','Hoog'),
('R25','Tweede lijn incident/problem/change tot afronding','Service Desk draagt complexere applicatieproblemen over.','Prioriteer, onderzoek, communiceer, herstel en documenteer oorzaak.','Gevorderd','Kritiek'),
('R26','Wekelijks IT en business rapporteren','Vertaal techniek naar voortgang en impact.','Meld resultaat, risico, budget/capaciteit, besluit en volgende stap.','Intermediate','Hoog'),
('R27','Intern/extern ontwikkelingsteam en training nieuwe collega’s','Technische samenwerking en taakgerichte sturing.','Doe review, overdracht en begeleid een collega met echte oefencase.','Intermediate','Hoog'),
('R28','IT-evoluties volgen; technische kennis en analyse','Maak passende verbeterkeuzes, geen technologie om zichzelf.','Vergelijk lifecycle, kosten en operationele haalbaarheid.','Intermediate','Hoog'),
('R29','PRINCE2 of andere projectmethode','Methodisch plannen, beslissen en risico’s beheersen.','Gebruik businesscase, fasering en tolerantie; certificaat niet expliciet vereist.','Intermediate','Hoog'),
('R30','MS Office en gerelateerde producten','Praktische analyse, rapportage en communicatie.','Gebruik Excel voor reconciliatie, Word voor CRQ, presentatie voor opleiding.','Basiskennis','Middel'),
('R31','Apex','Waarschijnlijk Oracle APEX gezien Oracle-stack; verifiëren.','Oefen formulieren, SQL-rapporten, validatie en rechten.','Intermediate','Hoog'),
('R32','Talen N/E/F','Waarschijnlijk Nederlands/Engels/Frans; niveau onbekend.','Leg incident uit, lees documentatie en voer leveranciersoverleg.','Intermediate','Hoog'),
('R33','Communiceren, organiseren, stress en taakgericht leidinggeven','Techniek en mensen onder druk op één resultaat richten.','Prioriteer transparant; benoem eigenaar en updatefrequentie.','Gevorderd','Kritiek'),
('R34','Supervisor/Director IT; projectcoördinator/business/klanten/leveranciers','Beslissen gebeurt in een netwerk van stakeholders.','Maak beslisrechten, escalatie en communicatie per doelgroep duidelijk.','Intermediate','Hoog'),
('R35','Applicatieomgevingen Kallo én Zeebrugge','Wijzigingen kunnen meerdere locaties raken.','Test locatieconfiguratie en operationele afhankelijkheden per site.','Gevorderd','Kritiek')]

add(1,'Executive summary','overview',f'''
{NOTE}

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
''')

add(2,'Vacature regel voor regel','overview',NOTE+'\n\nDe bronvereisten zijn volledig geparafraseerd en geordend; navigatie en algemene websitefooter zijn geen functievereisten. IDs vormen de koppeling met skills, portfolio en bewijs.\n\n| ID / vacaturevereiste (parafrase) | Werkelijke betekenis | Praktijk | Moeilijkheid | Belang |\n|---|---|---|---|---|\n'+'\n'.join(f'| {r[0]} — {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |' for r in requirements))

add(3,'De functie in de praktijk','overview',f'''
{NOTE}

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
''')

resp=[
('Technische projectplanning','R06/R10/R12','Maak probleem, scope en acceptatie concreet voordat je uren plant. Splits in werkpakketten met eigenaar, afhankelijkheid, reviewmoment en opleverbewijs.','Alleen deadlines plannen, zonder afhankelijkheden of businessacceptatie.','Gebruikt risicotoleranties en alternatieven; toont gevolgen van scopewijziging.','CRQ, lastenboek, planning, risicolog','Laat een eigen werkpakket met requirements, testplan en forecast zien.'),
('Behoeftenanalyse','R11','Observeer de echte taak; vraag om drie voorbeelden, een uitzondering en het gevolg van niets doen. Scheid gewenste UI van onderliggende behoefte.','Een voorgesteld scherm verwarren met het probleem.','Valideert proces én uitkomsten bij de gebruiker voordat een leverancier bouwt.','Proceskaart, stakeholderlijst, acceptatiecriteria','Vertel hoe een vraag veranderde na doorvragen en welk resultaat dat gaf.'),
('Leveranciers en outsourcing','R07/R15','Spreek deliverables, toegang, acceptatie, support en documentatie af. Volg acties met eigenaar/datum en bewijs; bespreek afwijking vroeg.','Een technische toezegging accepteren zonder demonstratie of test.','Houdt eigen ketenkennis; laat overdracht en beheerbaarheid meeleveren.','Actielog, contractafspraken, opleverchecklist','Toon een escalatiemail en een acceptatiematrix zonder vertrouwelijke details.'),
('Capaciteit en budget','R16/R23/R24','Vergelijk begroting, werkelijk verbruik, resterend werk en beschikbare mensen. Rapporteer forecast, afhankelijkheden en opties; vraag besluit bij overschrijding.','Urenverbruik rapporteren zonder resterende scope.','Meldt trend voordat budget op is; herprioriteert met businesswaarde.','Excel, projectportefeuille, forecast','Gebruik een voorbeeld waarin je scope, tijd of kwaliteit expliciet afwoog.'),
('Applicatiemodellering en core-beheer','R08/R17/R19/R35','Leg component, omgeving, eigenaar, versie, input/output en herstelafhankelijkheden vast. Loop één transactie door en onderhoud die kaart bij changes.','Een schema met blokjes maken zonder eigenaar of foutpad.','Kan tijdens incidenten exact aanwijzen welke ketengrens nog gezond is.','Componentcatalogus, logs, read-only SQL','Leg een eigen architectuurdiagram uit inclusief onbekende aannames.'),
('EDI en rapportering','R20','Bewaar bericht-ID, partner, ontvangsttijd, mappingversie en businessresultaat. Reconcile aantallen en unieke sleutels; onderscheid technisch ACK van businessverwerking.','Een ontvangen bestand als succesvolle verwerking tellen.','Test duplicaten, order en retries; controleert betekenis van rapportcijfers.','iWay/WebFOCUS indien juiste productvariant, berichtarchief','Demonstreer replay zonder dubbel effect en verklaar een cijferafwijking.'),
('Portalen en nieuwe tools','R21/R22/R31','Ontwikkel klein en afgebakend; valideer input server-side, controleer rechten en log wie wat wijzigde. Test happy path en uitzonderingen.','Een knop verbergen als enige toegangscontrole.','Bouwt taakgericht met audit, onderhoudsplan en testdata.','APEX indien bevestigd, SQL, ontwikkelomgeving','Toon formulier, negatieve autorisatietest en duidelijke README.'),
('Releasecoördinatie','R18/R13','Koppel versies, databasechanges en partnerconfiguratie. Leg window, go/no-go, rollout, recovery en nazorg vast. Verifieer een echte businesshandeling na livegang.','Rollback gelijkstellen aan enkel een oude applicatie terugzetten.','Onderzoekt data-/schema-compatibiliteit en herstelvenster vóór go-live.','Releaseplan, artefactenregister, checklist','Laat een gerepeteerde deployment met testbewijs en recoverybeperking zien.'),
('Tweede lijn en wachtdienst','R03/R25','Neem ticket met impact, tijd en repro over. Vorm hypotheses, verzamel bewijs, voer alleen toegestane changes uit en sluit met gebruikersvalidatie.','Blind restarten; parallel meerdere changes maken; stil blijven.','Beperkt risico, verdeelt taken en communiceert vaste updates.','Ticketing, logs, runbooks, SQL, escalatielijst','Werk hardop een incident uit en onderscheid herstel van root cause.'),
('Rapportage en communicatie','R26/R32/R33/R34','Schrijf wat opgeleverd is, wat risico loopt, welke keuze nodig is, wie eigenaar is en wanneer de volgende update komt. Pas detail aan doelgroep aan.','Een logdump sturen of een onzekere ETA als belofte presenteren.','Zegt wat bekend/onbekend is en vertaalt risico naar operationele gevolgen.','Office, statusformat, overleg','Geef hetzelfde incidentbericht voor business en leverancier.'),
('Opleiden en samenwerken','R14/R27','Laat gebruiker/nieuwe collega zelf een taak uitvoeren, met uitzondering en recovery. Documenteer de stappen en controleer begrip.','Een demo geven zonder de deelnemer zelf te laten oefenen.','Maakt overdracht zelfstandig bruikbaar en laat feedback verbeteren.','Quick guide, sandbox, buddyplan','Toon een werkinstructie en vertel hoe je begrip controleerde.'),
('Kwaliteit, veiligheid, milieu en integriteit','R04/R09','Bespreek of foutieve data onveilige fysieke acties of verkeerde rapportage kan veroorzaken. Gebruik traceerbare goedkeuringen en meld onzekerheid eerlijk.','Een workaround laten leiden tot verlies van fysieke traceerbaarheid.','Betrekt operationele verantwoordelijke en borgt latere reconciliatie.','Risicomatrix, auditlog, changeprocedure','Vertel hoe je onder druk een risicovolle shortcut begrensde.')]
body=NOTE
for title,ids,how,junior,strong,tools,proof in resp:
    body+=f'\n\n## {title} — {ids}\n\n**Betekenis en belang:** {next((r[2] for r in requirements if r[0] in ids),title)} Dit bepaalt of het resultaat bruikbaar, beheersbaar en betrouwbaar is.\n\n**Goed uitvoeren:** {how}\n\n**Juniorfout:** {junior}\n\n**Sterke medewerker:** {strong}\n\n**Tools:** {tools}; concrete interne tooling verifiëren.\n\n**Sollicitatiebewijs:** {proof}'
add(4,'Verantwoordelijkheden','overview',body)

add(5,'Technische architectuur','technical',f'''
{NOTE}

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
''')

add(7,'Businesskennis','overview','''
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
''')

skills=[
('SQL / relationele data','Zelfstandig read-only analyseren','MUST HAVE','R19/R20/R25','Join, null, unieke sleutel, transactie en reconciliatie','Query + uitleg + testdata'),
('Incidentanalyse / ketendiagnose','Zelfstandig, productieacties met mandaat','MUST HAVE','R25/R03','Impact, scope, bewijs, veilige herstelstap','Incidentrapport + hardop casus'),
('Requirements en acceptatiecriteria','Zelfstandig','MUST HAVE','R11/R12','Businessvraag testbaar maken','CRQ + positieve/negatieve tests'),
('Communicatie en prioritering','Zelfstandig','MUST HAVE','R26/R33','Mensen op impact/besluit richten','Businessupdate + STAR-case'),
('Applicatiecomponenten en datastromen','Zelfstandig modelleren','MUST HAVE','R17/R19','Fouten lokaliseren en changes beoordelen','Diagram + transactie walkthrough'),
('Project-/leverancierssturing','Zelfstandig binnen mandaat','MUST HAVE','R06/R07/R16','Scope, capaciteit en acceptatie bewaken','Planning + risicolog + forecast'),
('Release, change en herstel','Uitvoeren met hulp → zelfstandig','SHOULD HAVE','R18/R25','Wijziging veilig en traceerbaar','Gerepeteerd releaseplan'),
('EDI / iWay-concepten','Gebruiken en flow diagnosticeren','SHOULD HAVE','R20','Mapping, ACK, idempotentie en replay','Berichtpipeline met negatieve tests'),
('Oracle praktijk','Gebruiken; DBA-werk met hulp','SHOULD HAVE','R19','SQL-tooling en foutbeelden kennen','Oracle-demo of expliciete simulatorbeperking'),
('JBoss / Java runtime','Begrijpen en logs gebruiken','SHOULD HAVE','R19','Runtime, pool, exceptions en config','Diagnoserapport van testapp'),
('WebFOCUS / rapportdefinities','Gebruiken → beheer leren','SHOULD HAVE','R20','Cijfers en filters verklaren','Rapportreconciliatie'),
('Webportal / Apex','Gebruiken, kleine functie bouwen','SHOULD HAVE','R21/R22/R31','Input, validatie, rollen en audit','Formulier + rechten/validatietests'),
('Nederlands/Engels/Frans','Praktisch communiceren; eisen navragen','SHOULD HAVE','R32','Intern en extern overleg','Zelfde incident uitleggen in drie talen'),
('AIX / IBM P-series','Begrijpen; beheer onder begeleiding','ON THE JOB','R19','Laaggrenzen, resources en rechten','Linux-lab met expliciete AIX-verschillen'),
('ICO-processen / TOS-product','Lokaal leren','ON THE JOB','R08/R35','Siteconfig en migratie-specifieke regels','Buddy-walkthrough, proceskaart'),
('MS Office','Zelfstandig gebruiken','SHOULD HAVE','R30','Rapportage, analyse en opleiding','Budget/reconciliatiesheet + instructie'),
('PRINCE2 / alternatief','Begrijpen en toepassen','SHOULD HAVE','R29','Businesscase, stages, tolerantie','Faseplan; certificaat niet verplicht genoemd'),
('IT-evoluties en lifecycle','Afwegen','SHOULD HAVE','R28','Beheerbaarheid en migratiekeuzes','Technische beslisnotitie'),
('Veiligheid/kwaliteit/milieu','Toepassen, lokale regels leren','MUST HAVE','R09/R04','Fysieke operatie niet schaden','Risicoafweging + traceerbare workaround'),
('Training / taakgericht leidinggeven','Zelfstandig kleine groep','SHOULD HAVE','R14/R27/R33','Adoptie en overdracht','Quick guide + teach-back'),
('Cloud/Kubernetes','Alleen indien bevestigd','NICE TO HAVE','Afgeleid','Niet genoemd; geen leerblocker','Geen prioritair bewijs nodig'),
('Diepe AIX/Oracle tuning','Expert niet aangenomen','NICE TO HAVE','Afgeleid','Specialistische samenwerking; eigenaarschap navragen','Duidelijke escalatiegrens')]
add(8,'Skills matrix en prioriteiten','skills',NOTE+'\n\nNiveaus: **theorie kennen → begrijpen → uitvoeren met hulp → zelfstandig uitvoeren → expert**. Expert zijn betekent specialistische oorzaken/ontwerpkeuzes overzien, geen noodzakelijke startvoorwaarde voor iedere stacknaam.\n\n| Skill | Nodig niveau | Prioriteit | Waarom / vacature | Hoe aantonen? |\n|---|---|---|---|---|\n'+'\n'.join(f'| {s[0]} | {s[1]} | {s[2]} | {s[3]}: {s[4]} | {s[5]} |' for s in skills)+'''

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
''')

add(9,'Mentale modellen','sops','''
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
''')

troubleshooting='''
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
'''

add(11,'Incident, problem, change en release','sops','''
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
''')

add(12,'Requirements naar technische oplossing','sops','''
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
''')

add(13,'Stakeholder management','sops','''
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
''')

# Every technology record answers the same fifteen practical questions, with topic-specific evidence.
tech=[]
def t(name,source,definition,use,why,where,mechanism,can,notneeded,problems,diagnosis,terms,question,answer,exercise,case,hours,level):
    tech.append(dict(name=name,source=source,definition=definition,use=use,why=why,where=where,mechanism=mechanism,can=can,notneeded=notneeded,problems=problems,diagnosis=diagnosis,terms=terms,question=question,answer=answer,exercise=exercise,case=case,hours=hours,level=level))

t('Terminal Operating System (TOS)','V1',
'Software die terminalprocessen en operationele gegevens ondersteunt. Exact ICO-product en modules onbekend.',
'Registratie, status, planning en uitvoering van terminalhandelingen; concrete processen door key users laten tonen.',
'Een gedeeld operationeel beeld vermindert inconsistentie tussen fysieke goederen en informatie.',
'Centraal applicatiedomein; de vacature koppelt TOS-componenten aan AIX/IBM P-series/Oracle/JBoss.',
'Businesshandelingen volgen regels en veranderen toestand. Integraties en rapporten lezen/verwerken die toestand. Modelleer state transitions en bron van waarheid.',
'Eén transactie end-to-end volgen, gebruikersfout versus systeemfout onderscheiden, wijzigingsimpact op beide vestigingen beoordelen en migratietests voorbereiden.',
'Het onbekende product vooraf volledig kennen of ieder logistiek proces zelf beheren.',
'Onjuiste status, ontbrekende opdracht, inconsistentie na timeout, vastgelopen integratie en foutieve locatie.',
'Vergelijk fysieke verwachting, bronrecord, audit, businessregels en partnerstatus op dezelfde sleutel/tijd. Laat operatie bepalen wat echt gebeurd is.',
'state, transition, source of truth, cutover, reconciliation, exception, master data',
'Hoe onderzoek je een voertuig dat fysiek aanwezig is maar niet zichtbaar in het TOS?',
'Ik begrens op voertuig, locatie en tijd. Ik controleer ontvangst en het eerste foutieve ketenpunt, vergelijk registratie met bron van waarheid en laat operations de fysieke toestand bevestigen. Herstel gebeurt traceerbaar en met downstreamcontrole.',
'Modelleer vijf fictieve voertuigen en geldige statusovergangen. Test vertrek zonder aankomst, dubbele aankomst en locatiecorrectie. Lever state diagram en foutmatrix op.',
'Een partner meldt aankomst opnieuw omdat het ACK ontbreekt: controleer eerst of de businesscommit al bestaat voordat je replay toestaat.',
'12–20 uur concept/proceslab; enkele weken lokale proceskennis met buddy. Productexpertise maanden, geen startvereiste.','Begrijpen → zelfstandig ketenanalyse')
t('IBM P-series / IBM Power','V1/T1',
'Genoemde IBM-serverfamilie voor enterprise workloads; huidige Power-benaming en precieze hardware bij ICO verifiëren.',
'Platform waarop AIX-gerelateerde TOS-componenten volgens vacature draaien.',
'Enterpriseplatformen bieden beheermogelijkheden en capaciteit voor langdurige workloads; ICO-keuzehistorie onbekend.',
'Onder OS/applicatielaag. Virtualisatie/LPAR en beheertools kunnen relevant zijn, maar zijn niet genoemd.',
'Hardware levert CPU, geheugen en I/O. Partities, indien aanwezig, verdelen resources; applicatieproblemen kunnen door capaciteit of opslag worden versterkt.',
'Platform versus OS versus applicatie onderscheiden en een gericht resourceprobleem aan platformbeheer melden.',
'Zelf firmware, SAN, HMC of fysieke hardware wijzigen zonder toegewezen rol en opleiding.',
'Resource contention, I/O-latentie, capaciteitsgrens of hardwarealarm; geen vastgestelde ICO-problemen.',
'Correlatie tussen tijd van applicatievertraging en platformmetrics; vraag eigenaar om partitie-/storagegegevens. Controleer of andere workloads meevertragen.',
'Power, partition/LPAR, CPU entitlement, I/O, capacity, HMC (alleen bij relevante setup)',
'Moet je de hardware kunnen beheren om applicaties te ondersteunen?',
'Ik moet de afhankelijkheid en resource-indicatoren begrijpen. Diep platformbeheer vraagt expliciet eigenaarschap. Ik lever tijd, impact en metingen zodat de beheerder gericht kan onderzoeken.',
'Maak een laagdiagram hardware → OS → runtime → database/app. Benoem voor drie symptomen de mogelijke eigenaar en ontbrekende meting.',
'TOS reageert traag bij een batch: sluit query- of poolproblemen niet uit omdat de server-CPU hoog is.',
'3–6 uur voor rolbegrip; productbeheer afzonderlijke opleiding.','Begrijpen; beheer met hulp')
t('AIX','V1/T1',
'IBM Unix-besturingssysteem. Het is geen Linux-distributie; shellconcepten overlappen, specifieke beheertools verschillen.',
'Processen, filesystems, gebruikers, netwerk en resources voor de genoemde TOS-componenten.',
'Stabiele enterprise-OS-functies voor de genoemde omgeving; de reden voor de oorspronkelijke keuze is onbekend.',
'Tussen IBM-platform en applicatie/runtime/database; verdeling hosts onbekend.',
'Processen draaien met rechten en verbruiken geheugen/CPU/I/O. Filesystems kunnen vollopen. Services hebben eigen start- en beheerprocedures.',
'Logpaden vinden, process/resourcebegrip toepassen en disk/rechten als oorzaak herkennen; gebruik toegestane read-only controles en lokale runbooks.',
'Kernel tuning, filesystems resizing, systeempatching en rootbeheer vóór indiensttreding.',
'Vol filesystem, verkeerde bestandsrechten, proces niet actief, te weinig resources, klokverschil.',
'Scopeer fout/tijd; controleer via bevoegde beheerder filesystem en processtatus; vergelijk service- en OS-log. Linuxcommando-output is geen AIX-bewijs.',
'filesystem, process, permission, UID, mount, service, paging, environment',
'Een verwerking faalt met een schrijffout: wat controleer je?',
'Ik controleer doelpad, rechten, beschikbare ruimte en of de applicatie de verwachte gebruiker gebruikt. Ik laat de eigenaar retentie en veilig ruimteherstel bepalen; ik verwijder geen logs of bestanden blind.',
'Maak in een Linux-testdirectory een permission denied en herstel alleen de labrechten. Leg op papier uit welke AIX-check nog door officiële versie/runbook bevestigd moet worden.',
'EDI-output kan niet geschreven worden; procesrestart lost volle opslag niet op en kan bewijs verloren doen gaan.',
'8–16 uur Unixbasis/laagdiagnose, daarna 2–4 weken AIX-begeleiding voor lokale taken.','Begrijpen → gebruiken met hulp')
t('Oracle Database / SQL / PL/SQL','V1; algemene databaseconcepten',
'Relationele database met SQL voor data en PL/SQL voor procedurele logica. Versie/licenties en DBA-eigenaarschap onbekend.',
'Operationele records, constraints, transacties, mogelijk businesslogica en rapportdata.',
'Consistente gedeelde opslag met transactie- en integriteitsregels.',
'Onder applicatielogica en mogelijk rechtstreeks onder APEX; integraties/rapporten kunnen via andere lagen benaderen.',
'Queries lezen tabellen; keys/constraints bewaken relaties. Een transactie bundelt wijzigingen met commit/rollback. Locks voorkomen conflicten maar kunnen wachten veroorzaken.',
'SELECT/join/filter/group begrijpen, null en datumcorrectheid bewaken, duplicaten detecteren en veilige read-only reconciliatie uitvoeren. Een klein PL/SQL-blok begrijpen indien de codebase dat gebruikt.',
'Production DBA, RAC/Data Guard/backupbeheer of optimizerexpert zijn tenzij expliciet toegewezen.',
'Lockwait, traag plan, connectionpool-uitputting, constraint violation, verkeerde join, stale rapport of timezonefout.',
'Vraag query/schema/parameters en timing; beperk scope, vergelijk actual/expected rows, laat DBA locks/plan beoordelen. Meet voor/na; voeg niet blind indexes toe.',
'primary/foreign key, constraint, index, transaction, commit, rollback, lock, execution plan, bind variable',
'Waarom kan een succesvolle update toch een foutmelding opleveren?',
'De databasecommit kan geslaagd zijn terwijl het antwoord of ACK faalt. Daarom zoek ik eerst op businesssleutel en request-ID. Een onbeschermde retry kan dubbel verwerken.',
'Maak synthetische vehicles/locations/edi_messages. Schrijf een query voor voertuigen zonder locatie en één voor dubbele businessreferenties. Test met nulls en duplicaten. Gebruik parameters.',
'Een rapport telt 120 voertuigen waar brondata 100 heeft: een one-to-many join kan rijen vermenigvuldigen; verklaar de relatie voor je DISTINCT toevoegt.',
'20–35 uur SQLbasis plus 8–15 uur transacties/reconciliatie; DBA-expertise is apart.','Zelfstandig read-only; wijzigingen met review')
t('JBoss / Java application server','V1/T2',
'Application server in de Java-ecosysteemfamilie. JBoss EAP en WildFly zijn verwante producten; ICO-variant/versie niet vastgesteld.',
'Host applicaties en configureert gedeelde services zoals datasources, transacties en logging.',
'Enterpriseapplicaties hebben een runtime en centrale resourceconfig nodig.',
'Tussen clients/portalen en database/businesscomponenten. Niet gelijkstellen aan de TOS zelf.',
'Requests gebruiken threads en databaseverbindingen uit pools. Exceptions laten zien waar uitvoering faalt; configuratie/dependency-versies bepalen werking.',
'Deploymentstatus en relevante logs lezen, datasource/pool/JVM/exceptionbegrip toepassen en configvergelijking met eigenaar uitvoeren.',
'De hele Java/Jakarta EE-specificatie of clusterarchitectuur beheersen; geen onbewezen EAP-consolecommando’s kopiëren.',
'Deployment failure, databaseconnectiefout, pool leeg, geheugen-/threadprobleem, incompatibele library of verkeerd configprofiel.',
'Correlatie-ID en exceptionketen; onderscheid eerste fout van vervolgschade. Controleer recente artefact/configchange, databasebereikbaarheid en resource-indicatoren. Restart alleen volgens plan.',
'JVM, datasource, connection pool, thread, WAR/EAR, exception, subsystem, standalone/domain (variantafhankelijk)',
'De health endpoint werkt maar transacties timen uit. Hoe kan dat?',
'Een simpele healthcheck hoeft geen databaseactie te testen. Ik vergelijk echte transacties, poolwachttijd en DB-latentie. Een healthy proces bewijst geen healthy businessdienst.',
'Lees een voorbeeldlog met connection timeout, identificeer de eerste fout en maak een evidence pack met vijf vragen aan runtime/DB-eigenaar.',
'Na apprelease gebruikt de datasource de verkeerde testconfig; het artefact start maar de business-smoke test faalt.',
'10–20 uur runtime/diagnoseconcepten; 1–3 dagen begeleide productlab indien beschikbaar.','Begrijpen → diagnostisch gebruiken')
t('EDI','V1; protocolvariant onbekend',
'Electronic Data Interchange: gestructureerde businessdata tussen organisaties. Een bepaalde standaard of transportvorm is niet bevestigd.',
'Partnerberichten ontvangen, valideren, mappen, verwerken en bevestigen.',
'Vermindert handmatige herinvoer en ondersteunt voorspelbare keteninformatie.',
'Externe partnergrens via middleware naar applicatie/data, met retourstatus of ACK.',
'Transport → syntax → semantiek/mapping → businessregels → commit → ACK. Iedere stap kan slagen/falen onafhankelijk van de rest.',
'Contracten en samples lezen, bericht-ID/businesssleutel volgen, duplicaten/order/ACK/replay verklaren en reconciliëren.',
'Alle EDIFACT-segmenten of AS2-beheer leren voordat de werkelijke standaard bekend is.',
'Fout datumformaat, onbekende locatie, duplicaat, ontbrekend ACK, verkeerde volgorde, encoding of partnercontractwijziging.',
'Volg één ID van transport tot commit; vergelijk mappingversie en sample met afgesproken contract. Test replay in sandbox; bepaal partial commits voordat bulk-replay mag.',
'schema, mapping, ACK/NACK, correlation ID, idempotency, replay, retry, ordering, dead letter (concept)',
'Wat is het verschil tussen een technisch ACK en een businessbevestiging?',
'Technisch ACK kan alleen ontvangst/syntax bevestigen. Businessbevestiging zegt of de bedoelde verwerking geaccepteerd is. Ik lees het contract; ik neem niet aan dat een ontvangen bestand gelijk is aan een verwerkt voertuig.',
'Verwerk tien JSON-oefenberichten met twee duplicaten en één onbekende locatie. Lever per ID ontvangst, validatie, verwerking en resultaat op. JSON is een demoformaat, niet bewezen ICO-EDI.',
'Partner stuurt dezelfde aankomst opnieuw na timeout; unieke businesssleutel plus gecontroleerde transactiestatus voorkomt dubbel effect.',
'12–24 uur concepten/lab, daarna daadwerkelijke partnerformaten tijdens onboarding.','Zelfstandig flowanalyse; productbeheer leren')
t('iWay / middleware','V1; productvariant verifiëren',
'iWay verwijst naar integratiesoftware voor verbinding, transformatie en orchestration. Variant en version zijn onbekend.',
'Koppeling van componenten en EDI-verwerking, zoals genoemd in vacature.',
'Centrale adapter/mappinglogica vermindert koppellogica in losse applicaties.',
'Tussen partnertransport en businessapplicatie/database; werkelijke topology onbekend.',
'Een flow heeft input, parse/transform, route, uitvoer en foutafhandeling. Configuratie en mappingversie zijn deel van de release.',
'Een bestaande flow lezen, foutgrens bepalen, configuratie/retries volgen en wijziging met partner testen.',
'Productplugin ontwikkelen of alle adapters/administratie leren vóór de eerste werkweek.',
'Adapterverbinding, mapping exception, backlog, verkeerd endpoint, onveilige retry en credential/certificaatverval.',
'Input/output en flowlog op ID, configversie en endpoint vergelijken; check backlogleeftijd naast aantallen; afstemmen met externe partner.',
'adapter, listener, channel, process flow, transform, route, error handling (benamingen versieafhankelijk)',
'Hoe vind je een fout in een integratieflow?',
'Ik markeer de laatste bewezen goede output en eerste verkeerde input. Ik vergelijk één sample en versie en controleer downstreamcommit vóór retry. Daarna reproduceer ik de mappingfout met synthetische data.',
'Teken een integratieflow en definieer per stap minimaal logveld, foutpad en eigenaar. Implementeer de concepten in portfolio als productlicentie ontbreekt.',
'Nieuwe locatiecode veroorzaakt mappingfouten voor één partner; de andere stromen blijven werken, dus scopeer de mappingvariant.',
'8–16 uur concepten; 2–5 begeleide productlabdagen voor lokale flows.','Gebruiken met hulp → zelfstandig bestaande flows')
t('WebFOCUS / BI en rapportering','V1; exacte productdocs nog verifiëren',
'Business-intelligence-/rapportageproductfamilie; precieze deployment en versie niet vastgesteld.',
'Rapportering genoemd bij EDI/TOS-portefeuille; exacte rapporten en databronnen onbekend.',
'Businessgebruikers hebben betrouwbare cijfers en gecontroleerde definities nodig.',
'Rapportlaag boven databronnen/adapters; directe Oracleverbinding of tussenlaag niet bewezen.',
'Bronselectie, filters, joins, aggregaties, toegangsregels en refresh bepalen wat het rapport toont.',
'Rapportcijfers terugleiden tot bronrecords en definitie, parameters/refresh/rechten controleren en wijzigingen valideren.',
'Alle rapportsyntax/dashboardfeatures vooraf beheersen of zelf datawarehousearchitect zijn.',
'Verkeerde telling, refreshachterstand, datumfilter, one-to-many join, verborgen rolfilter en exportverschil.',
'Vergelijk gelijke sleutelset, tijdzone en snapshot. Controleer datasource, filter, rechten en laatste refresh. Gebruik één afwijkend record als bewijs.',
'measure, dimension, filter, aggregation, report parameter, refresh, drill-down, row-level security (concept)',
'Twee rapporten tonen verschillende aantallen. Welke vraag stel je eerst?',
'Tellen ze hetzelfde businessobject onder dezelfde definitie, tijd en scope? Pas daarna onderzoek ik join, filter en refresh. Ik maak een verschilset met sleutels in plaats van cijfers passend te maken.',
'Maak twee synthetische rapportqueries met verschillende inclusie van inactieve locaties. Documenteer definitie, refresh en reconciliatie.',
'Weekrapport telt status op verwerkingstijd waar operations op eventtijd telt; beide queries kunnen technisch correct zijn maar andere vragen beantwoorden.',
'8–16 uur rapportanalyse; echte syntax/catalogus on the job.','Begrijpen → gebruiken; beheer met begeleiding')
t('Apex — waarschijnlijk Oracle APEX','V1/T3; interpretatie verifiëren',
'Oracle Application Express is databasegerichte low-code webontwikkeling. “Apex” kan theoretisch iets anders zijn; in Oracle-context waarschijnlijk APEX.',
'Formulieren, rapporten en taakgerichte webportalen op relationele data.',
'Snel gecontroleerde applicaties maken met bestaande database en businessregels.',
'Browser → weblaag/ORDS → APEX-engine in Oracle. ORDS is een productarchitectuurreferentie, niet als ICO-component genoemd.',
'Pagina’s bevatten regions, items, validations en processes; engine bewaakt sessie, page flow, auth en authorisatie. Een browsersessie is niet permanent dezelfde databasesessie.',
'Rapport en formulier maken, servervalidatie/rechten begrijpen, foutpaden testen en export/versieoverdracht documenteren.',
'Iedere plugin of JavaScript-API kennen, platforminstallatie of SYSDBA-beheer doen.',
'Verkeerde session state, autorisatielek, onjuiste processvolgorde, constraintfout en niet-geparameteriseerde query.',
'In test page/process en debuglog volgen; itemwaarden/session state/rollen en DB-resultaat vergelijken. Verberg geheimen en toon niet onnodig interne foutdetails.',
'workspace, application, page, region, item, process, validation, session state, authentication, authorization, ORDS',
'Waarom is een verborgen knop geen voldoende security?',
'Een gebruiker kan een request buiten de UI sturen. Autorisatie hoort op de server en op het relevante object/scope. Ik test een onbevoegde request expliciet en controleer dat data niet wijzigt.',
'Bouw indien sandbox beschikbaar een voertuiglocatieformulier met reden, autorisatie en validatie. Zonder licentie/sandbox maak een equivalent en label het als conceptbewijs.',
'Een correctieformulier overschrijft stale data; gebruik een gecontroleerde versiecheck en laat gebruiker de actuele toestand herladen.',
'15–30 uur gerichte APEX-praktijk bij SQLbasis; installatiebeheer niet inbegrepen.','Gebruiken → kleine functie zelfstandig met review')
t('Webportalen / HTTP / API','V1 voor portalen; overige concepten afgeleid',
'Een webportaal geeft gebruikers toegang tot applicatiefuncties. HTTP is request/response; API is een afgesproken software-interface.',
'Gebruikersacties, rapportinzage en systeemkoppelingen; geen specifieke frontendtaal genoemd.',
'Maakt businessfuncties toegankelijk met gecontroleerde toegang en feedback.',
'Client → web/app-laag → businesslogica/data; identity en TLS zijn dwarsdoorsnijdend.',
'Request bevat actie/data/auth; server controleert regels en antwoord. Clienttimeout kan na servercommit vallen; statuscode alleen is onvoldoende businessbewijs.',
'Repro en browser/netwerkfout onderscheiden, contract/errorcodes begrijpen, rollen/validatie en taakflow testen.',
'Een modern framework of microservices invoeren zonder behoefte; vacature vraagt geen React.',
'401/403, verlopen sessie, 500, TLS-fout, verkeerde scope, timeout en stale cache.',
'Vergelijk één/gehele gebruikersgroep, requesttijd/ID en serverlog. Test toegang en businessresultaat; onderscheid auth, netwerk en applicatie.',
'request/response, HTTP status, timeout, payload, TLS, session, endpoint, contract',
'Wat is het verschil tussen 401 en 403?',
'Doorgaans ontbreekt of faalt bij 401 authenticatie; bij 403 ontbreekt toestemming. Productgedrag kan verschillen, dus ik controleer serverlog en rolconfig zonder rechten blind te verruimen.',
'Schrijf contract voor een synthetische locatiecorrectie: input, allowed roles, validatie, conflict, error en audit. Test direct request buiten de UI.',
'Eén klant ziet niets: scopefilter kan correct blokkeren of verkeerde klantmapping bevatten; bewijs nodig vóór aanpassen.',
'8–16 uur web/API-diagnose, aanvullende bouwpraktijk 1–3 dagen.','Begrijpen → gebruiken')
t('Authenticatie / autorisatie / security','Waarschijnlijk / afgeleid',
'Authenticatie bewijst identiteit; autorisatie beperkt acties en datascope. Least privilege geeft alleen benodigde toegang.',
'Portalen, beheeraccounts, database en partnertransport beschermen.',
'Voorkomt onbedoelde wijziging, gegevenslek en onbevoegde operationele beslissingen.',
'Alle lagen; concrete SSO/AD/LDAP/OIDC-keuze onbekend.',
'Identitycontrole, rol/scopebeleid, secretbeheer, transportbeveiliging en audit versterken elkaar. UI-controls vervangen servercontrole niet.',
'Minimale rechten vragen, secrets uit code/logs houden, role/scope negatieve tests uitvoeren en securityincident gericht escaleren.',
'Cryptografie ontwerpen, pentestexpert zijn of eigen identityprovider bouwen.',
'Te brede rol, hardcoded credential, log met gevoelige data, verlopen certificaat en verkeerde klantfilter.',
'Bepaal blootstelling/scope zonder data onnodig te kopiëren. Bewaar bewijs volgens procedure; betrek securityowner voor containment en credentialrotatie.',
'least privilege, RBAC, scope, secret, TLS, audit, containment, exposure',
'Je ontdekt mogelijk klantdata in de verkeerde portal. Wat doe je?',
'Ik behandel het als mogelijk securityincident, beperk verdere blootstelling via bevoegde eigenaar, bewaar minimaal bewijs en meld feitelijke scope/ onzekerheid. Ik verwijder geen auditsporen en communiceer extern alleen volgens afspraken.',
'Maak een rolmatrix voor reader/operator/admin met twee klant-scopes en test alle verboden combinaties.',
'Een leverancier vraagt permanent adminaccount; bespreek taakgebonden tijdelijke rechten en audit met IT-eigenaar.',
'6–12 uur relevante basis; interne securityprocedure tijdens onboarding.','Zelfstandig toepassen; specialist escaleren')
t('Netwerk / DNS / TCP / TLS','Waarschijnlijk / afgeleid',
'DNS vertaalt namen, TCP draagt verbindingen en TLS beveiligt transport; poorten/routes bepalen bereikbaarheid.',
'Client-server, database en partnerconnectiviteit onderzoeken.',
'Applicaties hebben betrouwbare en beveiligde netwerkgrenzen nodig.',
'Onder iedere remote call; topologie/proxy/firewall bij ICO onbekend.',
'Naamresolutie → connectie → TLS-handshake → protocol → applicatieantwoord. Een geslaagde ping bewijst geen applicatieprotocol.',
'Foutlaag herkennen, timestamp/endpoint geven en gerichte reachability/TLS-check afstemmen.',
'Routingprotocollen/SAN/netwerkarchitectuur diep leren of firewall breed openzetten.',
'DNS-verwijzing fout, connect-timeout, certificaat verlopen, trustchain of proxyconfig verkeerd.',
'Verschil tussen hosts/locaties; check naam, route/poort en certificaat met bevoegde beheerder. Test werkelijk protocol; geen credentials in gedeelde commands.',
'DNS, port, route, firewall, handshake, certificate chain, expiry, proxy, latency',
'Een endpoint is bereikbaar maar de integratie faalt. Waarom?',
'Bereikbaar is een laagbewijs. TLS, credentials, protocolcontract of businessvalidatie kunnen nog falen. Ik volg de eerste foutgrens en vergelijk beide kanten op hetzelfde tijdstip.',
'Teken vier storingen: DNS, connectie, TLS, applicatie. Geef per fout één onderscheidende veilige controle.',
'Alleen Zeebrugge faalt na routewijziging: vergelijk locatiepad en configuratie, niet direct code aanpassen.',
'6–12 uur appgericht netwerkbegrip.','Begrijpen → diagnostisch gebruiken')
t('Logging / monitoring / messaging','Waarschijnlijk / afgeleid',
'Logs tonen gebeurtenissen; metrics tonen trends; alerts vragen actie. Messaging ontkoppelt verzending van verwerking.',
'Ketenproblemen vinden en tijdig zien dat backlog of fouten groeien.',
'Een systeem kan draaien terwijl businessverwerking achterblijft.',
'Bij app, OS, DB, integratie en rapport; concrete tooling onbekend.',
'Correlatie-ID verbindt stappen, timestamps ordenen gebeurtenissen. Queue age is naast queue length nodig. At-least-once delivery vereist duplicate-safe verwerking.',
'Geschikte logvelden ontwerpen, backlog/foutpercentage/interactietijd lezen en op businessuitkomst monitoren.',
'Een observabilityplatform bouwen, exacte brokeradministratie of distributed tracingexpert worden.',
'Geen correlatie, verkeerde tijdzone, alert zonder owner, sensitive logs, consumer stuck en retry-storm.',
'Vergelijk last successful businessevent, oldest pending en foutgroep. Bewaar IDs, mask persoonsgegevens en stem retentie/alertactie af.',
'correlation ID, metric, alert, backlog, oldest age, consumer, retry, dead letter, retention',
'Waarom is “aantal fouten nul” geen voldoende monitoring?',
'Het proces kan niets verwerken. Ik monitor volume, laatste succesvolle verwerking en achterstand naast foutpercentage. Een stilgevallen consumer geeft mogelijk geen nieuwe error.',
'Maak een dashboard met volume/minuut, errors, oldest pending en unieke successful businesskeys. Injecteer stilstand en controleer alert.',
'Een batch start niet: output is leeg en logs tonen geen error. Verwacht volume en schedulerbewijs onthullen het probleem.',
'8–16 uur appgerichte observability-praktijk.','Zelfstandig ontwerpen op kleine schaal')
t('Deployment / CI/CD / versiebeheer / cloud','V1 releases; CI/CD/cloud afgeleid',
'Deployment plaatst een versie; versiebeheer bewaart changes; CI/CD automatiseert checks/uitrol. Cloud is een hostingmodel, niet bevestigd.',
'Herhaalbare tests en releases met compatibele config/schema/artefacten.',
'Reduceert handmatige fouten en geeft herleidbaar releasebewijs.',
'Deliverylaag over omgevingen; concrete Git/CI/CD en cloudprovider onbekend.',
'Change → review → tests → artefact → acceptatie → goedgekeurde uitrol → businessvalidatie. Secrets/config zijn omgevingsgebonden.',
'Release manifest, compatibiliteit, pipeline-uitkomst en recoveryplan begrijpen; demo reproductief bouwen.',
'Kubernetes, multi-cloud, enterprise pipelineplatform of containerstrategie vóór bevestiging.',
'Juiste code verkeerde config, schema niet compatibel, test ontbreekt, half deployment en onomkeerbare migratie.',
'Vergelijk artefactversie, config en schema; laat smoke test echte businessactie doen. Bij datamigratie expliciet beoordelen of restore/forward fix nodig is.',
'artifact, build, pipeline, environment, migration, rollback, forward fix, smoke test, manifest',
'Is een app-rollback altijd voldoende?',
'Nee. Data en schema kunnen gewijzigd zijn. Ik definieer vooraf compatibiliteit en herstelmogelijkheden, inclusief partnerberichten en data die sinds livegang ontstaan zijn.',
'Bouw een demo met één compatibele schemawijziging en één incompatibele. Documenteer wat veilig terug kan en wat niet.',
'Partneradapter verwacht veld uit nieuwe schema maar app wordt teruggezet; recovery moet alle afhankelijke versies behandelen.',
'10–20 uur release/versiepraktijk; cloud alleen gericht leren indien werkelijk nodig.','Zelfstandig demo; productieworkflow met begeleiding')
t('PRINCE2 / projectmanagement / CRQ','V1',
'PRINCE2 is een projectmanagementmethode; vacature laat alternatieven toe. CRQ is change request; lastenboek beschrijft technische opdracht en werkpakketten.',
'Resultaat, fasen, beslissingen, risico’s, budget en leveranciersafspraken organiseren.',
'Voorkomt onduidelijke scope en onzichtbare afwijkingen.',
'Besturingslaag rond businessanalyse, techniek en delivery.',
'Businesscase rechtvaardigt werk; fasen maken review mogelijk; tolerantie bepaalt wanneer escalatie nodig is. Werkpakket maakt output en acceptatie concreet.',
'Kleine businesscase, risico-/actielog, werkpakket, forecast en wijzigingsimpact maken en gebruiken.',
'Certificaat of alle methodeterminologie memoriseren; certificaat niet expliciet vereist.',
'Scope creep, ontbrekende owner, late budgetmelding, leverancier levert zonder acceptatie en onduidelijke beslisrechten.',
'Vergelijk baseline en resterende scope/capaciteit. Benoem beslissing, alternatieven en consequenties; laat change autoriseren.',
'businesscase, stage, tolerance, work package, risk, issue, CRQ, acceptance, forecast',
'Een leverancier vraagt 30% extra tijd. Wat rapporteer je?',
'Ik vraag bewijs van resterend werk/oorzaak, beoordeel impact en presenteer opties: scope beperken, planning aanpassen of capaciteit wijzigen. Ik maak duidelijk wie beslist en welke tolerantie overschreden is.',
'Maak CRQ van locatiecorrectie met 6 werkpakketten, risicolog, acceptance en budgetvoorbeeld met expliciete fictieve bedragen.',
'Nieuwe TOS-integratie blijkt afhankelijk van partnerdata die niet geleverd is; escalatie vóór het releasewindow voorkomt verrassingen.',
'8–16 uur toegepaste methode/CRQ; formele certificatie apart.','Zelfstandig toepassen, mandaat navragen')
t('MS Office / N-E-F / training','V1',
'Office is een productiviteitspakket; N/E/F vermoedelijk Nederlands/Engels/Frans. Vereist taalniveau en gerelateerde producten onbekend.',
'Analyse, rapportage, specificaties, leverancierscontact en gebruikersopleiding.',
'Technische uitvoering vraagt begrijpelijke afspraken en bewijs voor meerdere doelgroepen.',
'Communicatie-/administratielaag; documenten moeten aansluiten op brondata en changes.',
'Excel helpt reconciliëren/forecasten; documenten leggen scope vast; presentaties begeleiden taken. Schrijf acties met eigenaar en datum; houd dezelfde betekenis over talen heen.',
'Een betrouwbare verschillenlijst, wekelijkse status en taakgerichte instructie maken; technisch incident praktisch kunnen uitleggen.',
'VBA/complexe dashboards, professionele vertaler of perfecte business-Frans zijn zonder niveau-eis.',
'Foutieve sheetformule, versieverwarring, jargon, vertaalde term met ander betekenis en training zonder oefening.',
'Controleer formules met kleine handmatige steekproef, versie/eigenaar en definities. Laat ontvanger samenvatten welke actie verwacht wordt.',
'reconciliation, forecast, action log, version, teach-back, key user',
'Hoe leg je een databaseprobleem uit aan operations?',
'Ik beschrijf welke handeling vertraagt, wat wel werkt, welke tijdelijke werkwijze veilig is en wanneer een update volgt. De technische fout geef ik apart aan de uitvoerders.',
'Schrijf hetzelfde incident in 5 zinnen NL/EN/FR. Laat taalhulp fouten verbeteren zonder je competentieniveau te overdrijven.',
'Business leest “test klaar” als “live”; scheid gebouwd, getest, geaccepteerd en productie-gevalideerd.',
'4–8 uur templates/praktijk; taalontwikkeling afhankelijk van uitgangsniveau.','Zelfstandig praktisch gebruiken')

body=NOTE+'''

## Gebruik dit handboek met 80/20-focus

Begin bij TOS/data/SQL, ketendiagnose en delivery. Productversies ontbreken: leer concepten en oefen alleen in een sandbox. Leertijden zijn bandbreedten bij IT-basiskennis, geen garantie van professionele beheersing. Oracle APEX-docs zijn geverifieerd via Context7; een toevallig opgehaald verwijderingscommando is bewust niet opgenomen omdat het irrelevant en destructief is.
'''
for x in tech:
    body+=f'''\n\n## {x['name']}

**Bronstatus:** {'Expliciet uit vacature: product/onderwerp genoemd; diepgang en toepassing afgeleid' if 'V1' in x['source'] else 'Waarschijnlijk / afgeleid uit functiecontext; geen bevestigde ICO-tool'}. Bronreferentie: {x['source']}; links in researchdossier.

1. **Wat is het?** {x['definition']}
2. **Gebruik:** {x['use']}
3. **Waarom:** {x['why']}
4. **Architectuurplek:** {x['where']}
5. **Conceptueel:** {x['mechanism']}
6. **Wat moet je kunnen:** {x['can']} Doelniveau: **{x['level']}**.
7. **Niet vooraf nodig:** {x['notneeded']}
8. **Typische problemen:** {x['problems']}
9. **Troubleshooting:** {x['diagnosis']}
10. **Termen:** {x['terms']}
11. **Interviewvraag:** {x['question']}
12. **Voorbeeldantwoord:** {x['answer']} Zeg erbij of dit labervaring, begrip of professionele ervaring is.
13. **Praktijkoefening:** {x['exercise']}
14. **Werksituatie:** {x['case']}
15. **Leertijd:** {x['hours']}
'''
glossary=[('Datasource','Gedeconfigureerde databaseverbinding voor een applicatie.'),('Connection pool','Herbruikbare databaseverbindingen; verzoeken wachten als alle verbindingen bezet zijn.'),('Thread','Uitvoeringseenheid binnen een proces; teveel werk of wachten kan capaciteit uitputten.'),('JVM','Java Virtual Machine: runtime waarin Java-code draait.'),('WAR/EAR','Verpakkingen voor Java-web-/enterpriseapplicaties; exacte deploymentvorm versieafhankelijk.'),('LPAR','Logical Partition: afgezonderde platformomgeving met toegewezen resources; niet bevestigd bij ICO.'),('HMC','Hardware Management Console voor relevant IBM-platformbeheer; aanwezigheid onbekend.'),('Paging','Geheugenpagina’s naar opslag verplaatsen; hoge activiteit kan symptoom van druk zijn.'),('UID/permission','Gebruikersidentiteit en bestandsrechten die bepalen welk proces mag lezen/schrijven.'),('Bind variable','Queryparameter apart van SQL-tekst; geen onveilige stringconcatenatie.'),('Constraint','Databaseregel die toegestane waarden/relaties afdwingt.'),('Execution plan','De stappen waarmee database een query uitvoert; DBA interpreteert met volume/parameters.'),('Mapping','Bronvelden/codes vertalen naar doelvelden met expliciete regels.'),('ACK/NACK','Positieve/negatieve bevestiging; contract bepaalt of ontvangst of businessuitkomst bedoeld wordt.'),('Idempotentie','Herhaalde verwerking geeft hetzelfde bedoelde businessresultaat zonder dubbel effect.'),('Atomiciteit','Samenhangende wijzigingen slagen samen of worden samen ongedaan gemaakt.'),('Correlation ID','Referentie die dezelfde handeling door meerdere componenten koppelt.'),('Retry/replay','Retry is opnieuw proberen; replay is bestaande input herverwerken. Eerst commit/duplicaatrisico bepalen.'),('Ordering','Volgorde waarin events verwerkt worden; aankomsttijd is niet altijd businessvolgorde.'),('Backlog/oldest age','Onverwerkt werk en leeftijd van het oudste item; beide bepalen of de keten achterloopt.'),('Dead letter','Afzondering van niet verwerkbare berichten voor gecontroleerd onderzoek; product niet bevestigd.'),('Outbox','Ontwerp waarin businesscommit en verzendopdracht samen duurzaam vastgelegd worden; demo-optie.'),('Backoff/jitter','Toenemende wachttijd en spreiding bij retries om een herstelbare fout niet te verergeren.'),('Circuit breaker','Ontwerp dat tijdelijk calls stopt na herhaald falen; geen genoemd ICO-component.'),('Row-level security','Toegang beperken per record/datascope; exacte mechaniek afhankelijk van product.'),('Authentication/authorization','Identiteit controleren versus toestemming voor actie/object bepalen.'),('Session state','Waarden/context van een gebruikerssessie; niet gelijk aan permanente databasesessie.'),('ORDS','Oracle REST Data Services: webintermediair naar Oracle/APEX; niet genoemd in vacature.'),('Workspace/region/item/process','APEX-werkgebied, paginagebied, invoerwaarde en verwerkingsstap; details in officiële docs.'),('DNS/TCP/TLS','Naamresolutie, netwerkverbinding en versleutelde/beveiligde transportlaag.'),('Certificate chain/truststore','Vertrouwensketen van certificaten en verzameling vertrouwde issuers/config; versiebeheer nodig.'),('RBAC/scope','Rechten via rollen en begrenzing tot relevante objecten/klant/site.'),('Retention','Hoe lang logs/data bewaard blijven; verwijderen alleen volgens beleid/eigenaar.'),('Artefact/manifest','Uit te rollen pakket en overzicht van compatibele app/config/schema/mappingversies.'),('CI/CD','Automatische build-/test-/deliverystappen; platform bij ICO onbekend.'),('Smoke test','Kleine controle op kritieke werking na deployment; ook echte businesshandeling testen.'),('Forward fix','Nieuwe herstelwijziging in plaats van terugzetten; nodig als rollback niet veilig is.'),('UAT','User Acceptance Testing: gebruikers controleren afgesproken taakresultaat en uitzonderingen.'),('CRQ/lastenboek','Change request en technische opdracht met scope, werkpakketten, risico en acceptance.'),('Tolerance/forecast','Afgesproken afwijkingsgrens en verwachting van eindresultaat/kosten op actuele informatie.'),('Optimistic concurrency','Wijziging toestaan alleen als record nog dezelfde versie heeft als bij lezen.'),('Reconciliatie','Bron/target vergelijken op sleutel, velden en businessbetekenis, niet alleen totaal.'),('Cutover/in-flight','Overgang naar nieuw systeem en events die rond dat moment nog onderweg/onverwerkt zijn.'),('RACI','Wie uitvoert, eindverantwoordelijk beslist, geraadpleegd en geïnformeerd wordt; lokale matrix verifiëren.')]
body+='\n\n## Jargon en moderne vergelijkingen\n\n| Term | Praktische betekenis |\n|---|---|\n'+'\n'.join(f'| {term} | {meaning} |' for term,meaning in glossary)+'''

**Legacy in moderne concepten:** AIX is dezelfde architectuurlaag als andere Unix/Linux-OS’en, niet dezelfde commandoset. JBoss hoort bij de runtime/application-serverlaag, niet bij databases of frontendframeworks. iWay combineert integratie-/adapter-/mappingconcepten die je ook in moderne middleware aantreft, maar een simulator bewijst geen iWay-administratie. WebFOCUS is BI/rapportering; overdraagbaar zijn joins, filters, definities en lineage, niet automatisch productsyntax. APEX is databasegerichte webontwikkeling; een moderne webdemo kan validatie/rechten/audit tonen maar geen APEX-productexpertise. Vergelijk concepten, benoem productverschillen en respecteer bestaande systeemwaarde.
'''
add(6,'Technologiehandboek','technical',body)

scenarios=[]
def s(title,level,ids,situation,known,unknown,questions,causes,logs,db,network,app,integration,approach,diagnosis,solution,communication,prevention,rubric):
    scenarios.append(dict(id=len(scenarios)+1,title=title,level=level,requirements=ids,situation=situation,known=known,unknown=unknown,questions=questions,causes=causes,logs=logs,database=db,network=network,application=app,integration=integration,approach=approach,diagnosis=diagnosis,solution=solution,communication=communication,prevention=prevention,rubric=rubric.split('|')))

s('Eén gebruiker kan niet inloggen','Basis','R21/R25/R32',
'Om 08:40 meldt een operator dat het portaal toegang weigert; een collega lijkt wel te kunnen werken.',
'Eén melding en een loginfout, niet bewezen sitebrede uitval.','Foutcode, rol, accountstatus, omgeving en of andere accounts hetzelfde probleem hebben.',
'Sinds wanneer, welk scherm/bericht, account of device, recent wachtwoord/rol gewijzigd?',
'Verlopen account/sessie, verkeerde loginroute, rolprobleem, lokale browsercache of identitydienst.',
'Tijd, geredigeerde account-ID, auth-fout en servercorrelatie. Geen wachtwoord loggen.',
'Applicatierol/scope vergelijken met goedgekeurde matrix; geen eigen productie-accounttabel aanpassen.',
'Alleen relevant als endpoint/authdienst niet bereikt wordt; vergelijk dezelfde URL vanaf twee devices.',
'Onderscheid 401/authenticatie van 403/toestemming; niet blind admin geven.',
'SSO is onbekend; als gebruikt, laat identityowner hetzelfde request volgen.',
'Impact bevestigen → vergelijken met werkend account → auth versus rechten isoleren → gericht herstellen.',
'Oefenhypothese: account is juist geauthenticeerd maar ontbreekt in operatorrol; bevestigen in serverlog/rolmatrix.',
'Bevoegde eigenaar corrigeert de goedgekeurde rol; nieuwe sessie en echte taak testen.',
'Zeg welke taak geblokkeerd is, wat nog werkt en volgende update; accountdetails alleen aan bevoegde groep.',
'Onboarding/rolwijziging met acceptatietest en duidelijke identity-escalatie.',
'Impact en scope|Authenticatie versus autorisatie|Least privilege|Functionele hercontrole')
s('Portaal toont oude informatie','Basis','R21/R25',
'Een status lijkt oud in het portaal, maar operations zegt dat de handeling net verwerkt is.',
'Eén weergaveverschil.','Of bronrecord actueel is, refresh/caching en tijdzone.',
'Welke sleutel, verwacht event, eventtijd of verwerkingstijd, andere gebruiker/weergave?',
'Cache, vertraagde verwerking, rapportrefresh of verkeerde scope.',
'Request-ID/tijd en laatste succesvolle verwerking van dezelfde sleutel.',
'Read-only bronstatus en update/eventtijd vergelijken met portaalquery.',
'Geen brede netwerkdiagnose zonder timeout; controleer request/response indien stale cache vermoed.',
'Parameters, cachepolicy en rolfilter vergelijken. Refresh bewijst geen oorzaak.',
'Check of bericht alleen ontvangen of werkelijk gecommit is.',
'Zelfde sleutel en tijd → bron vergelijken → keten of weergave isoleren.',
'Oefenhypothese: bron klopt maar endpoint gebruikt een oude snapshot; test cacheversie en refresh.',
'Cache/refresh via eigenaar corrigeren of verwerking herstellen; gebruiker laat taak opnieuw uitvoeren.',
'Maak duidelijk of fysieke registratie goed is en welk scherm achterloopt.',
'Timestamp/refresh zichtbaar maken en freshnessmonitor toevoegen.',
'Bron van waarheid|Tijd en refresh|Geen onnodige mutatie|Gebruikersvalidatie')
s('Rapportexport bevat verkeerde telling','Basis','R20/R30',
'Een WebFOCUS-rapport en Excel-export tonen een ander voertuigaantal.',
'Twee verschillende uitkomsten, nog geen bewijs van dataverlies.','Definities, filters, tijdzone, refresh en unieke sleutel.',
'Tellen we voertuigen of events? Dezelfde locaties, datumgrenzen en autorisatie?',
'One-to-many join, verkeerde filter, exportlimiet, stale refresh of spreadsheetformule.',
'Rapportparameters, queryversie, refreshmoment en exportmetadata.',
'Verschilset op businesssleutel; join-cardinaliteit en nulls controleren.',
'Pas controleren bij afgebroken export/timeout; geen eerste hypothese.',
'Dezelfde report-versie/parameters en scope testen.',
'Controleer bronrefresh indien rapport op downstreamdataset draait.',
'Definitie aligneren → dezelfde snapshot → verschillen per sleutel → query/export isoleren.',
'Oefenhypothese: rapport telt eventregels in plaats van unieke voertuigen; bevestigen via kardinaliteit.',
'Definitie/query corrigeren via change; verwacht resultaat door business laten bevestigen.',
'Meld cijferimpact zonder direct “database fout” te zeggen; corrigeer eerder verspreid rapport indien nodig.',
'Rapportdatacontract, referentieset en formulecontrole.',
'Definitie en scope|Sleutelreconciliatie|Join-cardinaliteit|Businessacceptatie')
s('Onduidelijke businessvraag','Basis','R11/R12',
'Business vraagt “maak het scherm sneller” en wil een raming morgen.',
'Er is een klacht, geen meetbaar probleem.','Welke taak, baseline, volume, uitzonderingen en deadline.',
'Welke stap kost tijd, wanneer, voor wie, welke vertraging en wat gebeurt bij niets doen?',
'Trage query, onhandige workflow, dubbele invoer of onrealistische verwachting.',
'Taakduur en requesttimings pas verzamelen na concrete repro.',
'Onderzoeken als een query de taak bottleneck blijkt; niet direct index voorstellen.',
'Latentie tussen locatie en server meten indien scope daarnaar wijst.',
'Observeer gebruiker; scheid klikaantal, responstijd en wachttijd.',
'Check of UI op partnerstatus wacht, waardoor snelle frontend niets oplost.',
'Observeer drie taken → probleemzin → doel/constraints → opties → kleine gevalideerde raming.',
'Oefenhypothese: dubbele invoer kost meer tijd dan technische latentie; meet beide.',
'Werkpakket voor taakverbetering met acceptatiecriteria en expliciete aannames.',
'Geef bandbreedte met onbekenden en datum waarop raming verfijnd wordt.',
'Intakeformat en key-useracceptatie voor iedere CRQ.',
'Probleem vóór oplossing|Taakobservatie|Meetbare acceptance|Raming met onzekerheid')
s('Nieuwkomer moet portaal leren','Basis','R14/R27',
'Een nieuwe medewerker kent de taak niet en gebruikt een oude handleiding.',
'Documentatie bestaat maar versie en begrip zijn onzeker.','Rechten, huidige flow, uitzonderingen en aanspreekpunt.',
'Welke echte taak moet zelfstandig lukken, welke fouten komen voor, wie bevestigt de procedure?',
'Oude instructie, te veel jargon, geen oefening of ontbrekende toegang.',
'Geen productielogs nodig voor training; leg labstappen/resultaten vast.',
'Synthetische testdata; geen echte klantgegevens kopiëren.',
'Toegang en juiste omgeving testen vóór sessie.',
'Actuele schermflow en rol aansluiten op instructie.',
'Leg externe afhankelijkheid uit zonder live partneractie uit te voeren.',
'Doel afbakenen → toegang → demo → deelnemer oefent → teach-back → feedback.',
'Oefenhypothese: instructie hoort bij vorige release; verifieer manifest/screens.',
'Quick guide updaten met eigenaar/versie; deelnemer doorloopt happy en foutpad.',
'Noem helpkanaal en wat gebruiker bij fout wel/niet moet herhalen.',
'Training koppelen aan release en terugkerende feedbackreview.',
'Taakgericht doel|Veilige testomgeving|Teach-back|Versiebeheer instructie')
s('API geeft serverfout','Intermediate','R22/R25',
'Een portalactie geeft HTTP 500 voor één type aanvraag; andere acties slagen.',
'Serverantwoord is fout, niet dat het hele platform uitligt.','Payloadvariant, eerste fout, commitstatus en recente changes.',
'Welke actie, welke input, sinds wanneer, request-ID, gebeurt hetzelfde bij alle records?',
'Null/validatiefout, constraint, code-exception of downstreamfout.',
'Request-ID, exceptionketen en laatste change, met secrets gemaskeerd.',
'Zoek businessresultaat en constraintfout read-only; commitstatus vóór retry.',
'500 bewijst bereikbaar applicatiepad; downstreamconnectiviteit kan wel falen.',
'Reproduceer input in test, vergelijk runtime/config en foutafhandeling.',
'Contractversie/downstreamresponse controleren als fout door externe service komt.',
'Scope → first exception → input vergelijken → commitstatus → veilige repro → fix/test.',
'Oefenhypothese: onbekende status wordt onjuist als null verwerkt; bevestig reproduceerbare exception.',
'Validatie/foutpad verbeteren en alleen veilige requests herhalen; geen bulk retry.',
'Meld getroffen actie en veilige workaround, niet een onbewezen gehele uitval.',
'Negatieve contracttests en logging van eerste foutgrens.',
'Scope en correlatie|Eerste exception|Commit vóór retry|Negatieve regressietest')
s('EDI-bericht geweigerd','Intermediate','R20/R25',
'Eén partnerbericht bereikt middleware maar wordt afgewezen; 18 vergelijkbare berichten wachten.',
'Transportreceipt bestaat; businessacceptatie niet.','Foutveld, mappingversie, partnercontract en partial processing.',
'Welke ID’s, nieuwe formaatvariant, laatste goede sample, contractwijziging aangekondigd?',
'Datum/encoding, onbekende code, verplichte waarde ontbreekt of mappingversie verkeerd.',
'Transport-ID, parser/validationlog, mappingversie, foutveld; geredigeerde payload.',
'Check unieke businesssleutel en eventuele gedeeltelijke commit.',
'Transport werkt voor sample; pas verder testen als receipt onvolledig is.',
'Controleer semantische businessvalidatie na syntax.',
'Vergelijk input/output per stap en technisch versus functioneel ACK.',
'Contract vergelijken → foutveld isoleren → representatieve test → correctie → controlled replay.',
'Oefenhypothese: partner levert nieuwe datumvariant; onderscheid fout contract versus mapping.',
'Partner corrigeren of geautoriseerde mappingchange; replay pas na duplicate-check en reconciliatie.',
'Geef partner dezelfde ID/tijd en concreet contractverschil; business krijgt impact/volume.',
'Contractversiebeheer, sampletests en schema-validatie.',
'Transport versus verwerking|Contractbewijs|Partial commit/duplicaten|Veilige replay')
s('Databasequery is traag','Intermediate','R19/R20/R25',
'Een specifieke zoekactie duurt 20 seconden in de demo; de vorige testbaseline was 2 seconden.',
'Taak is trager onder bepaalde input; cijfers zijn fictief.','Queryplan, locks, volume, parameters, concurrency en configchange.',
'Alle zoekacties of één filter, piekmoment, laatste wijziging, hoeveel records?',
'Verkeerd queryplan, meer volume, missing/poor index, lock, poolwait of onbegrensde export.',
'Requesttiming splitsen in poolwait/query/render; query-ID en parameters volgens privacybeleid.',
'DBA plan/locks laten bekijken; row count en selectiviteit vergelijken met baseline.',
'Meet alleen als server/DB-roundtrip afwijkend is; onderscheid querytijd van netwerktijd.',
'Parameter/ORM-query en pagina-limit vergelijken; geen onbewezen tuning.',
'Batchbelasting of partnerburst kan load toevoegen; correleer tijd.',
'Baseline → concrete repro → laag-timings → DBA evidence → meet één wijziging.',
'Oefenhypothese: filter ontbreekt in nieuwe query; bewijs via rows/plan, niet alleen CPU.',
'Gerichte queryfix en review/test; index of capacity alleen met eigenaar/impactanalyse.',
'Meld taak/volume/temporary limit en geen prestatiebelofte zonder meting.',
'Representatieve performancetest, querylimits en trendmonitor.',
'Baseline en parameters|Pool versus querytijd|DBA/plan evidence|Voor/nameting')
s('JBoss kan niet verbinden met database','Intermediate','R19/R25',
'Na configuratiewijziging starten applicaties maar transacties geven datasource-fouten.',
'Runtime start; businesshandeling faalt.','Credentials, endpoint, pool, DB-status en juiste targetomgeving.',
'Alle apps/hosts, sinds welke change, eerste foutcode, welk datasourceprofiel?',
'Verkeerd endpoint/secret, DB niet bereikbaar, auth geweigerd of poolconfig.',
'Datasource/JDBC-fout, configrelease, server/starttijd; credentialwaarden nooit tonen.',
'DB-eigenaar controleert listener/auth/service en geschikte sessies.',
'Resolutie/poort en werkelijke DB-service testen door bevoegd team.',
'Vergelijk config met goedgekeurde omgeving; health endpoint is onvoldoende.',
'Andere DB-afhankelijke flows als impactgrens vergelijken.',
'Recent change → configdiff zonder secrets → netwerk/auth/pool onderscheiden → herstel.',
'Oefenhypothese: testendpoint in productieconfig; bewijs via manifest/configkey.',
'Goedgekeurde config terugzetten of corrigeren; business-smoke en integratiecontrole.',
'Informeer over transacties die wel/niet werken en veilige retryvoorwaarden.',
'Omgevingsvalidatie, secretreferenties en dependency healthcheck.',
'Business-smoke|Secretveilig configbewijs|Netwerk/auth onderscheiden|Gecontroleerde restore')
s('AIX-filesystem vol','Intermediate','R19/R25',
'Verwerking stopt met write-fouten; een beheerder meldt 100% bezetting van een filesystem.',
'Schrijfprobleem en capaciteitssignaal; locatie/data-inhoud nog onbekend.','Welke files, retentie, andere services en veilige opruimoptie.',
'Welk mount/path, groeisnelheid, sinds wanneer, vereist audit/berichtarchief, wie beheert opslag?',
'Loggroei, grote batch, retentiejob faalt of tijdelijke bestanden blijven staan.',
'Write exception, disktrend, retentiescheduler en recente volumenverandering.',
'Controleer of commit al gedaan is en alleen export/ACK faalt; DB-files nooit blind verwijderen.',
'Niet eerste oorzaak; downstreamretries kunnen extra volume opleveren.',
'Welke uitvoer faalt, wat is opnieuw uitvoerbaar en wat moet bewaard?',
'Blokkeer ongecontroleerde replay; check output versus gecommitteerde data.',
'Owner → impact → evidence bewaren → retentie/capaciteitplan → controlled herstel.',
'Oefenhypothese: logging is gegroeid na debugchange; bevestig zonder auditverlies.',
'Bevoegd beheerder archiveert/roteert volgens beleid of breidt capaciteit uit; app/businessflow testen.',
'Zeg dat herstelplan databehoud omvat; geen “we verwijderen alles” shortcut.',
'Diskthreshold, groeitrend, retentietest en debug-einddatum.',
'Geen blind verwijderen|Eigenaarschap opslag|Commit/replay check|Groei en retentie')
s('Dubbel verwerkt partnerbericht','Intermediate','R20/R22/R25',
'Een partner verstuurt dezelfde aankomst twee keer; er verschijnen dubbele events.',
'Dubbele input; dubbele business-effecten vermoed.','Message-ID versus businesssleutel, commit/ACK, impact op rapport en operatie.',
'Zijn IDs gelijk, is hetzelfde business-event opnieuw verpakt, welke verwerking is correct?',
'Retry na ontbrekend ACK, deduplicatie op verkeerde sleutel, niet-atomische check/insert.',
'Ontvangst, dedupbesluit, commit en ACK per ID met timestamps.',
'Unieke keys en audit vergelijken; race/transactionboundary bekijken met developer/DBA.',
'Timeout kan trigger zijn; transportprobleem is niet hele oorzaak.',
'Idempotentie moet ook bij concurrente verzending werken.',
'Bespreek retrycontract en betekenis van IDs met partner.',
'Effect inventariseren → bron-event bepalen → oorzaak retry/dedup → veilige correctie.',
'Oefenhypothese: ieder retry krijgt nieuw transport-ID maar dezelfde eventkey.',
'Unique business-eventkey en atomische verwerking via change; correctie met audit en downstreamreconciliatie.',
'Meld dat ontvangst dubbels normaal kan zijn, dubbel effect niet; correctie-impact afstemmen.',
'Concurrency/duplicate/timeout-regressietests en dedupmonitor.',
'Businesssleutel versus transport-ID|Atomiciteit|Auditcorrectie|Concurrency test')
s('Ontbrekend ACK na succesvolle commit','Intermediate','R20/R25',
'Partner zegt “niet ontvangen”; intern lijkt event wel verwerkt.',
'Intern record bestaat; partnerstatus onduidelijk.','Welke ACK-semantiek, verzendstatus, correlation en retryrisico.',
'Welk event, welk expected ACK, sinds wanneer, partner ontvangt andere confirmations?',
'ACK-export mislukt, transporttimeout, partnerfilter of mismatch referentie.',
'Commit en outbound ACKlog op dezelfde correlation/businesskey.',
'Bewijs unieke commit; geen event opnieuw aanmaken om ACK te forceren.',
'Retourpad/TLS/credential en beide tijdlijnen vergelijken.',
'Controleren of ACK los van businessverwerking veilig opnieuw te sturen is.',
'Partner vraagt bestaande bevestiging/replaycontract, geen volledige re-import.',
'Commitstatus bewijzen → outbound-grens isoleren → bevestiging gecontroleerd herverzenden.',
'Oefenhypothese: ACKsend timeout na commit; check outboundqueue en partnerreceipt.',
'Alleen bevestiging opnieuw sturen volgens contract; event niet opnieuw verwerken.',
'Bevestig intern resultaat met minimale gegevens en test ontvangst samen.',
'Duurzame outboundstatus, ACK-retries en end-to-end reconciliatie.',
'Commitbewijs|ACK-semantiek|Geen dubbel event|Partnerreceipt controleren')
s('Locatiecode onbekend in mapping','Intermediate','R20/R35',
'Berichten uit Kallo slagen, dezelfde nieuwe code uit Zeebrugge faalt.',
'Locatie-/codegebonden scope.','Siteconfig, masterdataowner en officiële code.',
'Welke code, bij wie geldig, mapping per vestiging, wijziging aangekondigd?',
'Masterdata niet gesynchroniseerd, hardcoded mapping, verkeerde siteconfig.',
'Site, code, mappingversie en rejected reason.',
'Locatiemasterdata en geldigheid read-only vergelijken, niet ter plaatse fictieve code maken.',
'Netwerk is minder waarschijnlijk als andere siteberichten langs zelfde pad slagen.',
'Sitevarianten en businessregels beoordelen.',
'Contract/codecatalogus en partnerwijziging afstemmen.',
'Codebron bepalen → siteconfig vergelijken → impact → geautoriseerde mapping/masterdatachange.',
'Oefenhypothese: code geldig, één mappingcatalogus loopt achter; bewijs van owner nodig.',
'Catalogusupdate met beide-site tests en controlled replay.',
'Geef partner/operations concrete affected codes en backlog, zonder verkeerde fysieke locatie toe te kennen.',
'Masterdatagovernance, synchronisatiecheck en site-tests.',
'Site scope|Masterdata-eigenaar|Geen fictieve code|Beide locaties testen')
s('TLS-certificaat verlopen','Intermediate','R21/R25',
'Een partnerendpoint faalt sinds middernacht met handshake error.',
'TLS-fout vóór businessresponse.','Certificaatkant, trustchain, expiry, gewijzigde hostname en andere consumers.',
'Welk endpoint, welke chain, laatste goede verbinding, is renewal geweest?',
'Expiry, incomplete chain, truststore verouderd, hostname mismatch of klokprobleem.',
'TLS-fout/expiry/hostname zonder secrets, requesttijd en deploymentconfig.',
'Geen DB-mutatie nodig; check eventueel reeds gecommitteerde queuevoorraad.',
'Bevoegde eigenaar controleert cert/chain/time en relevante endpointroute.',
'Truststoreconfig kan runtimecomponent zijn; tijdelijke trust-all is onveilig.',
'Partner bevestigt certwisseling en test hetzelfde endpoint.',
'Certkant identificeren → owner → juiste chain/renewal → test → backlog veilig verwerken.',
'Oefenhypothese: partner renewal zonder volledige chain; bewijs via chainvergelijking.',
'Correct certificaat/chain of trustconfig geautoriseerd plaatsen; verificatie nooit uitschakelen.',
'Meld welke stroom blokkeert en plan/volgende update; geen ongefundeerde cyberclaim.',
'Expiry-alert, contactlijst en renewalrepetitie.',
'TLS laag|Chain/hostname/time|Geen trust-all|Renewalmonitor')
s('Release faalt halverwege','Gevorderd','R18/R25',
'App is vernieuwd maar schema-migratie stopt; portaal geeft inconsistent gedrag.',
'Versiemix en gedeeltelijke uitvoering.','Migratiestappen, irreversible data, oude versiecompatibiliteit, impact.',
'Welke stappen geslaagd, transactioneel of niet, huidige schema, herstelbewijs?',
'Migratiefout, ontbrekende permissie, onverwachte data of uitvoervolgorde.',
'Deploymentmanifest, migrationlog, timestamp en first failure.',
'DBA schema/data-status vergelijken met plan; geen blind restore over nieuwe data.',
'Alleen relevant als deployverbinding faalde; eerst state inventory.',
'App/schemaversies en compatibiliteit vaststellen.',
'Partners in-/outbound veilig pauzeren als procedure vereist om mixed states te beperken.',
'Stop verdere changes → state inventariseren → go/no-go owner → rollback/forward fix beoordelen.',
'Oefenhypothese: migration faalt op onverwachte null-data na eerdere schemawijziging.',
'Gerepeteerd recoverypad of goedgekeurde forward fix; daarna business/data/partnerchecks.',
'Meld precies welke versiestappen klaar zijn en wat onzeker is; updates door één incidentowner.',
'Production-like dataset, prereq-check en recoveryrepetitie.',
'Stop en state inventory|Schema/data recovery|Go/no-go owner|End-to-end validatie')
s('Leverancier wijst naar ons','Gevorderd','R07/R25/R33',
'Integratiepartner zegt dat netwerk bij ICO fout is, intern zegt men dat payload fout is.',
'Twee meningen, geen gezamenlijk bewijs.','Exacte foutgrens en gedeelde correlatie/tijdzone.',
'Welk ID, wat verzonden/ontvangen, welke timestamps, contractversie en fout?',
'Echte netwerkfout, payloadreject, timezoneverwarring of ontbreken van grenslogging.',
'Evidence pack met ID, geredigeerd input/output, tijd/zone en eerste error.',
'Businesscommit controleren om retries niet te verdubbelen.',
'Verzend-/ontvangstbewijs naast elkaar; bereikbaarheid test is niet payloadacceptatie.',
'Verwerkingsfout en release/configversie demonstreren.',
'Samen één sample langs beide grenzen volgen.',
'Gezamenlijke grens-test plannen, rollen verdelen, feiten/taken noteren, escaleren op ontbrekend ownership.',
'Oefenhypothese: ontvangst slaagt en validation reject is aantoonbaar; netwerkclaim daarmee voor dit sample weerlegd.',
'Owner op bewijs aanwijzen en testbare fix opleveren; eigen monitoringgat eveneens verbeteren.',
'Neutraal: “bewijs A/B, onbekend C, actie X door Y vóór Z”.',
'Contract, shared correlation en escalatieafspraken.',
'Feiten vóór schuld|Gezamenlijke sample|Ketenbewijs|Owner en deadline')
s('Twee urgente projecten concurreren','Gevorderd','R16/R23/R24',
'Business A wil release deze week, business B heeft verplichte partnerwijziging; dezelfde leverancier doet beide.',
'Capaciteitsconflict.','Deadlinehardheid, risico, minimale scope, afhankelijkheden en beslisrecht.',
'Wat als elk project later komt, welke deadline extern vaststaat, wat is MVP?',
'Overplanning, onzichtbare afhankelijkheid, scopegroei of onvoldoende forecast.',
'Projectactuals/actielog, geen technische logs tenzij incident oorzaak van conflict is.',
'Data-/migratieafhankelijkheden van beide changes onderzoeken.',
'Omgevingsvensters/sitebelasting kunnen releasevolgorde beperken.',
'Compatibiliteit en gezamenlijke componenten bepalen.',
'Partnerdeadlines en testresources bevestigen.',
'Impact/urgentie/scope vergelijken → capacity forecast → opties → bevoegd besluit → nieuwe baseline.',
'Oefenhypothese: extern contractwindow is hard, wensdatum A onderhandelbaar; verifiëren bij owners.',
'Prioriteit en scope geautoriseerd aanpassen met consequenties, geen stille overurenbelofte.',
'Beide businessunits krijgen hetzelfde besluit en onderbouwde timing.',
'Portefeuilleoverzicht, capacitybuffer en vroeg risico-overleg.',
'Impact en hardheid|Capaciteit forecast|Opties met gevolgen|Beslisrecht')
s('Budget dreigt te overschrijden','Gevorderd','R16/R24/R26',
'70% budget is gebruikt maar leverancier meldt 50% scope afgerond.',
'Verbruik en scopepercentage passen niet vanzelf samen.','Definition of done, resterende raming en oorzaak.',
'Gebouwd of geaccepteerd, fixed/variable kosten, scopewijzigingen, wat resteert?',
'Onderschatting, scope creep, rework, overhead of onbetrouwbare voortgangsmeting.',
'Uren/facturen, werkpakketstatus en changebesluiten.',
'Niet van toepassing op financiële diagnose; datawerk kan extra kostenbron zijn.',
'Niet van toepassing tenzij infrastructuurkosten deel van project zijn.',
'Opleveringen demonstreren aan acceptancecriteria.',
'Partnerafhankelijkheden en extra adapterwerk beoordelen.',
'Actuals verifiëren → remaining effort → estimate at completion → opties en escalatie.',
'Oefenhypothese: 50% is gebouwd maar test/nazorg niet geraamd; forecast opnieuw onderbouwen.',
'Scope/tijd/budgetbesluit door bevoegde owner; werkpakketbaseline wijzigen.',
'Geen foutloze eindprijs suggereren: bandbreedte, aannames en besluitdatum.',
'Voortgang op accepted deliverables, frequente forecast en scopecontrol.',
'Actual versus accepted|Remaining forecast|Vroeg escaleren|Scopebesluit vastleggen')
s('Productie ligt gedeeltelijk plat','Gevorderd','R19/R25/R35',
'Zeebrugge meldt dat een kritieke taak faalt; Kallo lijkt nog te werken.',
'Locatiegebonden impact, maar omvang nog te bevestigen.','Veiligheidsimpact, gedeelde componenten, beschikbaar workaround en prioriteit.',
'Welke taak/gebruikers, fysieke gevolgen, starttijd, laatste change, andere locaties echt getest?',
'Siteconfig, netwerkroute, lokaal endpoint, gedeelde app met site-specifieke data of load.',
'Site/time/request correlation, first failure en laatste succesvolle taak.',
'Siteparameters en businesskeys vergelijken; geen systeemwijde datawijziging.',
'Route/DNS/endpointverschil als hypothese; eigenaar laten meten.',
'Zelfde transactie op werkende/ falende site met veilige data vergelijken.',
'Partnerstromen per site checken en veilige backlogbewaring regelen.',
'Incidentowner → operationsveiligheid → impactmatrix → laatste goede grens → gerichte hersteltest.',
'Oefenhypothese: lokale routeconfigwijziging; bewijzen met locatiepad en app-health/data.',
'Geautoriseerde gerichte herstelactie; test beide sites en reconciliatie, voorkom shared component te verstoren.',
'Vaste updates per getroffen businessunit; benoem wat gecontroleerd blijft werken.',
'Sitegerichte synthetic/business checks en configreview.',
'Veiligheid en impact|Werkende site als vergelijking|Gerichte actie|Beide-sites validatie')
s('Database lock blokkeert verwerking','Gevorderd','R19/R25',
'Meerdere transacties wachten; een DBA ziet één langlopende blocking session.',
'Lock-relatie, nog geen mandaat om sessie te stoppen.','Owner, transactie-intentie, rollbackduur en commitstatus.',
'Sinds wanneer, welke tabellen/taak, recent batch, kan gecontroleerd beëindigd worden?',
'Langlopende transactie, vergeten commit, batchoverlap of gewijzigde lockvolgorde.',
'Requesttiming, DB-session/lock evidence van DBA, job-owner en batchlog.',
'DBA identificeert blocking/waiting sessies en gevolgen; kill kan lang rollbacken.',
'Niet primaire oorzaak als DB-lock bewezen is; geen firewallwijziging.',
'Transactiegrenzen en timeout/retrygedrag bekijken.',
'Retryburst vermijden; downstreamstatus pas na commit beoordelen.',
'Owner/impact → lockbewijs → beheerbesluit → veilig beëindigen/herstellen → data check.',
'Oefenhypothese: onderhoudsjob houdt lock; controleer eigenaar en status vóór ingreep.',
'DBA voert goedgekeurde actie uit; code/batchfix via problem/change, met transactie/retrytests.',
'Leg uit dat herstel niet onmiddellijk is als rollback nog loopt.',
'Batchvensters, transactieduurmonitor, korte transacties en concurrencytests.',
'DBA bewijs|Geen blind kill|Rollbackimpact|Structurele transactiecontrole')
s('Veiligheidsgevoelige statuscorrectie','Gevorderd','R09/R21/R25',
'Een gebruiker wil een hold verwijderen om vertrek te versnellen, maar reden is onduidelijk.',
'Voorgestelde datawijziging kan fysieke actie beïnvloeden.','Wie vrijgave mag beslissen en waarom hold bestaat.',
'Welke holdsoort, bron, bevoegdheid, fysieke verificatie en downstreamgebruik?',
'Legitieme achterhaalde status, ontbrekende update of verkeerde interpretatie van hold.',
'Audit/history en bron van beslissing, minimale persoonsgegevens.',
'Read-only status/herkomst; geen UPDATE op verzoek alleen.',
'Niet relevant zonder aanwijzing voor ontbrekend bronbericht.',
'Serverautorisatie en geldige transitions beoordelen.',
'Partner/businesstoestemming en statusbron vergelijken.',
'Operationele eigenaar inschakelen → feitelijke toestand/verantwoordelijkheid → traceerbare change.',
'Oefenhypothese: hold heeft nog geldige grond; IT kan dit niet autonoom opheffen.',
'Alleen bevoegde businessbeslissing uitvoeren via goedgekeurde flow met audit en downstreamcontrole.',
'Erken tijdsdruk maar benoem dat vrijgave een business-/veiligheidsbesluit is.',
'Rolmatrix, redenplicht, audit en training statusbetekenis.',
'Fysieke gevolgen|Bevoegde beslissing|Geen ongeautoriseerde update|Audit/ketencontrole')
s('Mogelijk datalek in portaal','Gevorderd','R21/R25/R09',
'Klant A meldt mogelijk een voertuig van klant B in de portal.',
'Mogelijke scopefout; omvang niet vastgesteld.','Reproduceerbaarheid, data/exposure, betrokken users en ownerprocedure.',
'Welke minimaal nodige sleutel, tijd, view, accountscope, sinds welke release?',
'Row-scopefilter fout, cache gedeeld, verkeerde klantmapping of data-eigenaarschap.',
'Audit/access/request-ID veilig bewaren; geen gevoelige screenshots breed verspreiden.',
'Goedgekeurde owner controleert klantrelaties en effectieve scope.',
'Geen evidence dat firewallprobleem; eerst server/data-access.',
'Object-level autorisatie en caching toetsen met veilige testaccounts.',
'Partner/masterdata kan verkeerd ownership aanleveren, maar server moet scope afdwingen.',
'Securityowner → minimale evidence → containment door bevoegd team → exposure scope → fix/test.',
'Oefenhypothese: ontbrekende serverfilter; alleen na scopebewijs concluderen.',
'Bevoegd team beperkt toegang en corrigeert autorisatie; credential/notificationkeuzes via echte procedure.',
'Intern feitelijk en vertrouwelijk; externe melding door aangewezen verantwoordelijke.',
'Negatieve multi-tenant autorisatietests, cacheisolation en audit.',
'Security-escalatie|Minimale bewijsdeling|Objectscope|Containment en regressietest')
s('TOS-migratie met verschil in aantallen','Specialistisch','R08/R18/R35',
'Tijdens oefencutover telt nieuwe omgeving minder open voertuigen dan oude bron.',
'Telling verschilt; criterium “open” kan verschillend zijn.','Snapshot, filters, rejected records, cutoverwindow en terugkeermogelijkheid.',
'Zelfde snapshot en statusdefinitie, welke sleutelset ontbreekt, berichten tijdens freeze?',
'Mappingfout, ontbrekende historie, uitsluitingsregel, batchreject of events na snapshot.',
'Migratiebatch, mappingversie, rejected IDs en change/cutovertijd.',
'Sleutel-/veld-/statusreconciliatie, niet alleen counts; bron/target audit.',
'Transport-integriteit indien file onvolledig; checksum/recordcount in demo.',
'Businessacceptatie per status en kritieke taak, niet alleen technische import.',
'In-flight messages, dedupkeys en partnerroutewissel mee analyseren.',
'Go-live stoppen volgens criteria → differences by key → classificeer → herstel/afstelbesluit.',
'Oefenhypothese: “hold” status verkeerd uitgesloten; bewijs met mapping en keyset.',
'Mapping corrigeren/rehearsal herhalen of cutover afstellen via owner; herstelpad op data beoordelen.',
'Go/no-go op concrete verschillen en risico, geen cosmetisch aanpassen van rapportcounts.',
'Meerdere rehearsalruns, reconciliation gates en delta/in-flight plan.',
'Key/field reconciliation|Snapshot/in-flight|Go/no-go gate|Herstelbaarheid')
s('Retry-storm veroorzaakt nieuwe uitval','Specialistisch','R20/R25/R18',
'Na partnertimeout stijgen retries en raken runtimepools vol; errors nemen toe.',
'Retries en resourceuitputting correleren, causaliteit nog testen.','Commitstatus, retrybeleid, capaciteit, veilige pauze en backlog.',
'Welke retryfrequentie, hoeveel unieke events, first failure vóór storm, wie mag throttlen?',
'Onbegrensde retries, geen backoff, concurrency te hoog of oorspronkelijk downstreamprobleem.',
'Retrycount, request-ID, poolwait, errortrend, oldest pending en first failure.',
'Commit/dedup en lock/poolimpact door DBA beoordelen.',
'Timeout oorspronkelijke bron mogelijk; connect versus readtimeout onderscheiden.',
'Threads/pool versus business throughput vergelijken; restart kan load terug laten stormen.',
'Veilige rate limit/backoff en duplicate-safe controlled replay met partner.',
'Contain load met bevoegdheid → eerst oorzaak → bewezen healthy baseline → geleidelijk backlog verwerken.',
'Oefenhypothese: retries zonder jitter/backoff versterken tijdelijk DB-probleem; meet in lab.',
'Geautoriseerd pauzeren/throttlen, dependency herstellen, idempotente replay begrenzen en monitoren.',
'Meld herstelvolgorde en dataconsistentie; niet beloven dat alle backlog direct weg is.',
'Bounded retries/backoff, capacitytest, circuit-breaker als ontwerpoptie en businessmonitor.',
'Feedbacklus herkennen|Containment met mandaat|Duplicate-safe backlog|Geleidelijke hervatting')
s('Nieuwe TOS go-live onder tijdsdruk','Specialistisch','R06/R08/R07/R18/R33',
'Leverancier wil live; operationele acceptance, rollbackbewijs en gebruikersopleiding zijn onvolledig.',
'Technische build is klaar, readiness niet.','Welke kritieke criteria ontbreken, mandate, contractdeadline en restimpact.',
'Welke task tests geslaagd, data verschillen, supportcoverage, training, restore en partnerchecks?',
'Planningdruk, definition-of-done te smal, afhankelijkheden of onderschatte adoptie.',
'Test/release manifest, open defects, cutoverrehearsal en goedkeuringslog.',
'Migratiereconciliatie en recoverywindow aantonen.',
'Bereikbaarheid per locatie/partner in go-livebewijs.',
'Kritieke businessjourneys en autorisatiechecks laten accepteren.',
'Inbound/outbound route, ACK en in-flight data met partners testen.',
'Readiness matrix → blockers/rest-risico → opties/pilot/uitstel → bevoegd go/no-go.',
'Oefenhypothese: geen gevalideerd recoverypad voor migratie is een blocker totdat bevoegd risico-besluit bestaat.',
'Niet zelfstandig politiek beslissen: evidence/advies en expliciet mandaat; missing gates afronden of window wijzigen.',
'Zakelijk: welke gate ontbreekt, welke gevolgen, wat is nodig en wie beslist vóór welk tijdstip.',
'Readinesscriteria vanaf projectstart, training/supportworkstream en rehearsalplanning.',
'Build versus readiness|Evidence gates|Recovery en adoptie|Expliciet go/no-go')

def scenario_md(x,incident=False):
    fields=[('Situatie / symptomen','situation'),('Wat weet ik?','known'),('Wat weet ik niet?','unknown'),('Eerste vragen / controles','questions'),('Mogelijke oorzaken','causes'),('Logs / bewijs','logs'),('Database','database'),('Netwerk','network'),('Applicatie','application'),('Integratie','integration'),('Mijn aanpak','approach'),('Diagnose — te bewijzen oefenhypothese','diagnosis'),('Oplossing','solution'),('Communicatie','communication'),('Preventie','prevention')]
    return f"\n\n## {x['id']:02d}. {x['title']} — {x['level']}\n\nVacaturekoppeling: {x['requirements']}. **Waarschijnlijk / afgeleid uit functiecontext; synthetische casus.**\n\n"+'\n\n'.join(f'**{label}:** {x[key]}' for label,key in fields)+ '\n\n**Goed genoeg / rubric:** '+ '; '.join(x['rubric'])+'.'

incident_ids=[1,3,6,7,8,9,10,11,12,14,15,19,20,22]
add(10,'Troubleshooting playbook','sops',troubleshooting+''.join(scenario_md(scenarios[i-1],True) for i in incident_ids))
add(14,'25 praktijkscenario’s','scenarios','''
**Waarschijnlijk / afgeleid uit functiecontext.** Oefencases in toenemende complexiteit. De app laat je eerst zelf antwoorden, daarna een rubric en modelaanpak bekijken. Er is geen AI-beoordeling: je vergelijkt eerlijk je eigen aanpak met vier criteria. Productie-ingrepen vereisen intern mandaat. De genoemde diagnoses zijn hypotheses, geen vastgestelde root causes.

Gebruik: beschrijf eerste vijf minuten, nodige bewijs, herstelrisico en communicatie. Beoordeel vervolgens ieder rubricpunt en noteer één verbeteractie. Alleen lezen is geen praktische beheersing.
'''+''.join(scenario_md(x) for x in scenarios))

interviews=[]
def q(category,question,intent,strong,weak,follow,long=None):
    interviews.append(dict(id=len(interviews)+1,category=category,question=question,intent=intent,strong=strong,weak=weak,follow=follow,long=long,rubric=['Beantwoord de vraag concreet','Onderscheid echte ervaring van lab/kennis','Noem bewijs, risico of resultaat','Leg relatie met deze rol uit']))

q('HR','Vertel over jezelf in relatie tot deze functie.','Relevant profiel kunnen selecteren, geen hele levensloop.',
'Ik verbind mijn echte ervaring met drie rolgebieden: probleemdiagnose, gecontroleerd opleveren en communicatie. Voor ieder gebied noem ik een werk- of labvoorbeeld en mijn eigen bijdrage. Ik benoem welk stackdeel ik nog gericht leer.',
'Mijn CV volledig voorlezen of claimen de hele stack al te beheersen.',
'Wat was jouw bijdrage, wat deed het team, welk bewijs heb je?',
'Begin met huidige rol/achtergrond in één zin. Bespreek één concreet probleem, jouw acties en toetsbaar resultaat. Koppel dat aan applicatiebeheer, requirements of leverancierscoördinatie. Noem één gerichte gap, de oefening waarmee je haar verkleint en welke begeleiding je eerst nodig hebt. Gebruik uitsluitend echte cijfers en gebeurtenissen.')
q('HR','Waarom wil je van functie veranderen?','Constructieve motivatie en verwachting.',
'Ik zoek een rol waarin techniek direct aan operationele processen gekoppeld is en waar ik naast bouwen ook analyse, delivery en beheer verantwoordelijkheid kan opnemen. Ik leg uit waarom mijn huidige stap logisch is met mijn echte achtergrond.',
'Mijn huidige werkgever/team afbreken of zeggen dat ik alleen een wagen wil.',
'Wat ontbreekt nu, wat verwacht je hier anders?')
q('HR','Hoe kijk je naar wachtdienst?','Praktische beschikbaarheid en realistisch risicobesef.',
'Ik begrijp dat wachtdienst expliciet onderdeel is. Ik wil rooster, responstijd, escalatiedekking, opleiding en compensatie bespreken. Binnen passende afspraken bereid ik me voor met runbooks en toegangschecks; ik beloof geen onbeperkte beschikbaarheid.',
'Altijd beschikbaar beloven zonder afspraken, of wachtdienst negeren.',
'Hoe handel je een nachtelijke oproep met onbekende oorzaak af?')
q('HR','Kun je werken in Zeebrugge en korte verplaatsingen doen?','Haalbaarheid van werkcontext.',
'Ik geef eerlijk mijn bereikbaarheid en mobiliteitsmogelijkheden. Ik begrijp dat Kallo/Zeebrugge in scope zijn en één à twee korte verplaatsingen per maand genoemd worden; ik vraag hoe planning en wachtdienst logistiek geregeld zijn.',
'Een reis-/woonvoorkeur verzwijgen die later niet haalbaar blijkt.',
'Wat is je praktische start-/reisplan?')
q('HR','Hoe voldoe je aan de opleidingseis?','Theoretische basis en bewijs van equivalentie.',
'Ik noem mijn echte diploma en relevante ervaring. Als het diploma afwijkt, toon ik analyse-/systeemprojecten en professionele verantwoordelijkheden. Ik vraag hoe ICO ervaring tegen de genoemde opleiding afweegt; ik verzin geen gelijkwaardigheid.',
'Een diploma/certificaat suggereren dat ik niet bezit.',
'Welke onderwerpen uit opleiding pas je praktisch toe?')
q('HR','Wat zijn je sterke punten en leerpunten?','Zelfkennis zonder ingestudeerde schijnzwakte.',
'Ik kies twee sterke punten met bewijs en één relevante gap met concrete oefening, feedback en doel. Bijvoorbeeld SQL-praktijk sterk, AIX-productkennis nog beperkt; alleen als dat mijn profiel echt beschrijft.',
'Perfectionisme noemen zonder concreet gedrag of alle gaps verbergen.',
'Hoe weet je dat dit sterk is, wat verbeterde recent?')
q('HR','Wat verwacht je van onboarding?','Leerbaarheid en zelfstandige voorbereiding.',
'Ik wil eerst proces/architectuur, eigenaren, toegang, changeprocedures en incidentescalatie begrijpen. Daarna shadow ik tickets en lever een kleine change met review op. Ik neem zelf notities en controleer begrip met teach-back.',
'Een volledige cursus voor alles eisen of zonder begeleiding productie aanpassen.',
'Wat kun je al in week één bijdragen?')

q('Motivatie','Waarom ICO en havenlogistiek?','Onderbouwde interesse in echte businesscontext.',
'De publieke ICO-site beschrijft RoRo en automotive-distributie. De rol spreekt mij aan omdat applicatiedata en integraties de fysieke operatie ondersteunen en omdat beheer naast een nieuw TOS-project staat. Ik wil de precieze projectfase van jullie horen.',
'Fictieve innovatieprojecten of interne systemen aan ICO toeschrijven.',
'Wat weet je van onze activiteiten en waar komt die kennis vandaan?')
q('Motivatie','Waarom deze brede rol in plaats van alleen developer?','Fit met support, analysis en coördinatie.',
'Ik wil verantwoordelijkheid voor een bruikbaar resultaat, inclusief requirements, tests, gebruikers en nazorg. Code is één middel. Ik geef een echt voorbeeld waarin diagnose of afstemming meer waarde gaf dan een extra feature.',
'Support minderwaardig noemen of impliceren alleen te willen programmeren.',
'Hoe verdeel je aandacht tussen incidenten en projectwerk?')
q('Motivatie','Wat vind je interessant aan legacy/enterpriseplatformen?','Pragmatische houding tegenover bestaande stack.',
'Ik zie bestaande platforms als systemen met waarde, constraints en afhankelijkheden. Ik leer eerst waarom ze er zijn en hoe ze werken. Moderniseren beoordeel ik op risico, kosten, supportbaarheid en businessresultaat.',
'AIX/JBoss verouderd noemen en onmiddellijk alles herschrijven.',
'Wanneer zou je vervangen in plaats van verbeteren?')
q('Motivatie','Wat trekt je aan in nieuw TOS implementeren?','Veranderwerk realistisch begrijpen.',
'Het verbindt processen, data, integraties, leveranciers en adoptie. Ik vind gecontroleerde cutover interessant: duidelijke acceptance, sleutelreconciliatie, in-flight berichten en herstelplan. De fase en mijn mandaat wil ik begrijpen.',
'Alleen enthousiast zijn over een nieuw scherm of technische stack.',
'Wat kan misgaan bij cutover?')
q('Motivatie','Wat wil je in zes maanden kunnen?','Gerichte ontwikkeling en realistische scope.',
'Binnen lokale afspraken wil ik de kernketen zelfstandig uitleggen, afgebakende tweedelijnstickets afhandelen en één kleine verbetering end-to-end opleveren met businessacceptatie. Exacte doelen stel ik met supervisor vast.',
'Binnen zes maanden architect van alles willen zijn zonder context.',
'Hoe meet je vooruitgang?')
q('Motivatie','Welke minder leuke delen accepteer je?','Bewustzijn van administratie, support en herhaling.',
'Rapportage, incidentregistratie en documentatie horen bij betrouwbaarheid. Ik maak ze efficiënt met vaste formats en automatisering waar verantwoord, zodat de volgende collega niet opnieuw moet zoeken.',
'Zeggen dat documentatie of gebruikersvragen tijdverspilling zijn.',
'Hoe houd je documentatie actueel?')
q('Motivatie','Waarom ben je interessant als je niet alles kent?','Transferable skills plus eerlijk leerplan.',
'Ik toon bewijs in analyse, delivery en communicatie en benoem precies welke productkennis ontbreekt. Ik oefen met vergelijkbare concepten, zonder die als productervaring te verkopen. Voor lokale TOS/AIX-procedures zoek ik begeleide start.',
'Ik leer snel zeggen zonder bewijs of geen gaps willen erkennen.',
'Welke gap is het grootste risico?')

q('Techniek','Leg de waarschijnlijke architectuur uit.','Laagbegrip en feiten scheiden.',
'De vacature noemt TOS-componenten met AIX/IBM P-series, Oracle en JBoss, plus iWay, WebFOCUS, portalen en Apex. Ik zou de verbindingen eerst valideren. Een oefenmodel is portal → app → database, met EDI en rapportering ernaast. APEX heeft een eigen databasegerichte route.',
'Een eigen cloud/microservice-architectuur presenteren als ICO-feit.',
'Waar verwacht je logs en wat is de bron van waarheid?',
'Noem eerst de bevestigde componenten. Leg daarna laag voor laag functies uit. Toon één oefentransactie en mogelijke foutgrenzen. Zeg expliciet dat productvarianten, authenticatie, transport en topology niet in de vacature staan. Vraag welke componenten in het nieuwe TOS blijven. Gebruik geen ORDS/JBoss-relatie als vaststaand bedrijfsfeit.')
q('Techniek','Wat is een transactie en waarom is die belangrijk?','Dataconsistentie en recovery.',
'Een transactie bundelt wijzigingen met commit of rollback. Een status en auditrecord moeten consistent blijven. Een timeout na commit kan leiden tot duplicate retry; ik verifieer businessstatus en idempotentie voordat ik opnieuw uitvoer.',
'Commit zien als hetzelfde als gebruiker ontving succes.',
'Hoe test je een fout tussen commit en ACK?')
q('Techniek','Hoe voorkom je dubbele EDI-verwerking?','Idempotentie en concurrerende races.',
'Ik definieer een business-eventkey, niet alleen transport-ID. Atomische unieke verwerking en opgeslagen resultaat beschermen bij retry/concurrency. Ik test dubbel, opnieuw verpakt, timeout na commit en parallel verstuurd. Exact contract afstemmen.',
'Een voorafgaande SELECT als enige dedupcontrole gebruiken zonder racebescherming.',
'Wat als partner iedere retry een nieuw ID geeft?')
q('Techniek','Wat doet JBoss?','Runtime onderscheiden van applicatie.',
'JBoss is een Java application serverfamilie die applicaties en gedeelde services zoals datasources/threads beheert. Variant/versie bepalen details. Ik lees eerste exception, config en poolgedrag en controleer echte businessactie, niet alleen processtatus.',
'JBoss een database noemen of EAP-versie bij ICO aannemen.',
'Waarom kan healthy process toch falende transacties hebben?')
q('Techniek','Wat moet je van AIX weten?','Platformbegrip en veilige grenzen.',
'Processen, rechten, filesystem en resourcegedrag begrijpen. Ik lever tijd, path en foutbewijs aan beheerder en gebruik lokale toegestane read-only checks. Linuxkennis helpt conceptueel, maar AIX-specifieke procedures verifieer ik.',
'Linuxcommando’s als bewezen AIX-runbook presenteren.',
'Wat doe je bij volle disk?')
q('Techniek','Wat is APEX en hoe beveilig je een formulier?','Productinterpretatie en serverregels.',
'In Oracle-context waarschijnlijk Oracle APEX, maar ik bevestig de naam. APEX maakt databasegerichte webapps. Validatie en authorisatie moeten op server/objectscope gelden; UI verbergen is geen security. Ik test onbevoegde request, conflict en audit.',
'APEX automatisch op JBoss laten draaien of alleen UI-knop blokkeren.',
'Wat is session state en waarom maakt het uit?')
q('Techniek','Hoe maak je rapportcijfers betrouwbaar?','Businessdefinitie en datalineage.',
'Definieer businessobject, snapshot/tijdzone, inclusie, unique keys en filters. Vergelijk bron en rapport met een sleutelverschillenlijst, niet alleen totalen. Check join-cardinaliteit en refresh. Laat business de definitie accepteren.',
'Blind DISTINCT gebruiken om totaal passend te krijgen.',
'Wat is verschil tussen eventtijd en verwerkingstijd?')

q('Scenario','Business vraagt directe productie-UPDATE.','Veiligheid en mandaat onder druk.',
'Ik verduidelijk impact, bron van waarheid en downstreameffect. Alleen een bevoegde, traceerbare correctie met audit/reconciliatie en herstelplan is acceptabel. Ik betrek businessowner als status fysieke vrijgave raakt.',
'Een UPDATE uitvoeren om gebruiker gerust te stellen.',
'Wat als manager blijft aandringen?')
q('Scenario','Leverancier levert laat: wat doe je?','Actiegericht escaleren.',
'Ik verifieer resterend werk en acceptance, maak impact op afhankelijke taken duidelijk en geef opties met capaciteit/scope/tijd. Acties krijgen owner/datum. Escalatie volgt mandaat; ik maskeer vertraging niet in weekrapport.',
'Alleen zeggen dat leverancier slecht is.',
'Wat meld je business en wat meld je leverancier?')
q('Scenario','Release faalt na schemawijziging.','Hersteldenken over data.',
'Ik stop verdere ongecontroleerde changes, inventariseer app/schema/datastatus en vraag bevoegd go/no-go. Rollback hangt van compatibiliteit en nieuwe data af. Ik kies met owners bewezen recovery/forward fix en valideer keten/business.',
'Meteen oude app terugzetten zonder schemacontrole.',
'Wat als migratie onomkeerbaar is?',
'Beschrijf eerste minuten: owner, scope, stoppen en bewijs. Maak onderscheid tussen deploymentstatus en datastatus. Leg expliciet uit dat een restore nieuw ontstane data kan verliezen en replay duplicaten kan veroorzaken. Benoem beslisrecht, communicatie en stopcriteria. Sluit met businessjourneys, sleutelreconciliatie en monitorperiode.')
q('Scenario','Twee locaties hebben verschillende resultaten.','Scope en sitevarianten.',
'Ik vergelijk dezelfde veilige taak, parameters, config en tijd over Kallo/Zeebrugge. Werkende site is een controlegroep, geen bewijs dat gedeelde componenten perfect zijn. Ik probeer de eerste verschilgrens te vinden.',
'Globale restart uitvoeren omdat één site faalt.',
'Welke site-specifieke data kan oorzaak zijn?')
q('Scenario','Nieuwe collega blijft fouten maken.','Coachend en taakgericht handelen.',
'Ik observeer de taak en controleer instructieversie/toegang. Daarna oefent collega zelf happy en foutpad en legt aanpak terug uit. Ik verbeter instructie of proces waar verwarring terugkeert.',
'Zeggen dat collega gewoon beter moet opletten.',
'Hoe meet je of training werkt?')
q('Scenario','Mogelijk klantdata verkeerd zichtbaar.','Securityincident herkennen.',
'Ik escaleer feitelijk naar security/IT-owner, beperk bewijsdeling en laat exposure/containment bepalen. Ik test met veilige accounts, behoud audit en corrigeer server/objectscope via procedure. Externe communicatie door aangewezen owner.',
'Screenshot breed mailen of logs wissen na fix.',
'Welke minimale gegevens leg je vast?')
q('Scenario','Go-live gepland, training niet klaar.','Readiness over techniek heen.',
'Ik maak ontbrekende acceptance/training/support/recovery concreet in readinessmatrix. Ik presenteer risico en opties, bijvoorbeeld beperkte pilot of ander window. Bevoegd owner beslist expliciet; gebouwd is niet hetzelfde als klaar voor gebruik.',
'Live zetten omdat leverancier klaar zegt.',
'Welke gates zijn blockers?')

q('Troubleshooting','Wat doe je in de eerste vijf minuten van een incident?','Geordend handelen.',
'Ik bepaal businessimpact/veiligheid, scope, starttijd, laatste werkende taak en owner. Ik verzamel één geredigeerd sample/request-ID en recente changes. Ik communiceer volgende update en wijzig niets blind.',
'Onmiddellijk restarten of tegelijk vijf instellingen wijzigen.',
'Hoe bepaal je prioriteit?')
q('Troubleshooting','Welke logregel is het belangrijkst?','Correlatie en eerste oorzaak.',
'De eerste relevante fout in dezelfde keten is vaak waardevoller dan latere gevolgerrors. Ik koppel ID, tijdzone, versie en businessresultaat. Een losse stacktrace zonder context is onvoldoende.',
'De langste stacktrace kopiëren zonder tijd/ID.',
'Hoe herken je vervolgschade?')
q('Troubleshooting','HTTP 200 maar gebruiker meldt fout.','Technisch succes versus businesssucces.',
'Ik lees contract en body, controleer businessresultaat en downstreamcommit. 200 kan alleen geaccepteerde ontvangst betekenen. Ik volg de async-verwerking en laat gebruiker de taakuitkomst bevestigen.',
'200 als bewijs dat het systeem volledig goed werkt.',
'Hoe monitor je asynchrone afhandeling?')
q('Troubleshooting','Geen errors, toch geen verwerking.','Liveness van businessproces.',
'Ik controleer verwacht volume, laatste succesvolle verwerking, scheduler/consumer en oldest pending. Een stilstaande flow kan geen nieuwe errors geven. Ik vergelijk inputvolume met unieke gecommitteerde events.',
'Niets doen omdat logs groen zijn.',
'Welke alert zou dit eerder vinden?')
q('Troubleshooting','Wanneer escaleer je?','Grenzen en ownership.',
'Bij veiligheids/data/securityrisico, brede impact, ontbrekend recht/kennis, benodigde specialist of afgesproken tijdgrens. Ik stuur evidence pack met impact, tijdlijn, laatste goede grens, tests en benodigde actie/besluit.',
'Pas na uren zoeken of meteen zonder enige context doorschuiven.',
'Wat is een goede evidence pack?')
q('Troubleshooting','Hoe voorkom je tunnelvisie?','Wetenschappelijke probleemaanpak.',
'Ik schrijf minstens twee hypotheses met voorspelling en weerlegging. Ik kies een veilige onderscheidende test en zoek een werkend tegenvoorbeeld. Daarna verander ik één factor en meet resultaat.',
'De laatste change altijd als oorzaak aannemen.',
'Geef een hypothesematrix voor traag rapport.')
q('Troubleshooting','Hoe sluit je een incident correct af?','Resultaat en vervolgwerk.',
'Businesshandeling gevalideerd, backlog/dataconsistentie gecontroleerd, gebruiker bevestigt en acties/tijdlijn vastgelegd. Root cause onzeker? Dan expliciet problem-link en eigenaar, geen verzonnen conclusie. Workaround krijgt einddatum.',
'Ticket sluiten zodra service start.',
'Wat monitort je na herstel?')

q('Business','Waarom is IT kritisch in een RoRo-terminal?','Sectorbegrip zonder bedrijfsfantasie.',
'Fysieke overdracht en informatie moeten overeenkomen: identiteit, locatie, status en partnercommunicatie. Verkeerde data kan zoekwerk, vertraging of verkeerde planning veroorzaken. Exacte ICO-procesregels wil ik bij operations valideren.',
'Alle terminals behandelen alsof het containers zijn.',
'Wat betekent RoRo?')
q('Business','Wat is de bron van waarheid?','Data ownership.',
'Dat is per gegeven de afgesproken gezaghebbende bron, niet noodzakelijk één systeem voor alles. Voor fysieke aanwezigheid, partneropdracht en financiële status kunnen andere owners gelden. Conflicten oplossen vraagt regels en bewijs.',
'Het nieuwste bericht is altijd waar.',
'Wat doe je bij conflicterende bronnen?')
q('Business','Hoe prioriteer je een rapportbug en integratie-uitval?','Impactgestuurde beslissingen.',
'Ik vergelijk fysieke/processimpact, gebruikers/partners, deadline, veiligheid en workaround. De categorie alleen bepaalt prioriteit niet. Ik vraag operationele owner om businessconsequenties en documenteer afweging.',
'Iedere integratie-uitval automatisch hoger zetten.',
'Wanneer is een rapport kritieker?')
q('Business','Wat betekent efficiënte implementatie?','Businessresultaat plus totale kosten.',
'Niet alleen weinig ontwikkeluren: bruikbaarheid, fouten, beheerlast, opleiding en support tellen mee. Ik leg acceptance en verwachte verbetering vast en meet na release met business, zonder fictieve ROI-cijfers.',
'Snel live gaan gelijkstellen aan efficiëntie.',
'Welke KPI zou je kiezen?')
q('Business','Welke datavelden wil je begrijpen?','Procesmodel kunnen afleiden.',
'Identiteit/businesssleutel, statusbetekenis, locatie, event/verwerkingstijd, partnerreferentie, actor/audit en uitzonderingen. Ik vraag welke van deze werkelijk bestaan en wie eigenaar is, niet dat mijn demoschema productieschema is.',
'Alleen tabellen bekijken zonder statusbetekenis.',
'Waarom twee timestamps?')
q('Business','Hoe betrek je een gebruiker bij acceptance?','Testbare adoptie.',
'Laat de gebruiker representatieve taken inclusief uitzondering uitvoeren met heldere expected results. Leg bewijs en besluit vast. Demo kijken is geen UAT; de proceseigenaar accepteert functionele regels.',
'Na één demo aannemen dat iedereen akkoord is.',
'Wie beslist over tegenstrijdige verwachtingen?')
q('Business','Hoe ondersteunt deze rol kwaliteit/veiligheid/milieu?','Verantwoordelijkheid voor fysieke context.',
'Ik behandel data die fysieke handelingen stuurt zorgvuldig, borg audit/rechten en bespreek veilige workarounds met operations. Efficiëntere/logistieke informatie kan helpen, maar ik verzin geen ICO-emissiesystemen of certificering.',
'Veiligheid als alleen hardwareteamprobleem afdoen.',
'Geef voorbeeld van gevaarlijke statuscorrectie.')

q('Gedrag','Vertel over een fout die je maakte.','Ownership en leren.',
'Gebruik een echte STAR-case: situatie, jouw verantwoordelijkheid, fout, gevolg, herstel/communicatie en preventie. Benoem eigen aandeel zonder collega’s de schuld te geven. Heb je alleen labvoorbeeld, zeg dat expliciet.',
'Ik maak geen fouten of een verkapte successtory.',
'Welke controle heb je daarna toegevoegd?')
q('Gedrag','Hoe werk je onder stress?','Betrouwbaar gedrag onder druk.',
'Ik stabiliseer impact/veiligheid, schrijf acties/tijd op, verdeel eigenaarschap en update vaste momenten. Ik verander één factor tegelijk en vraag hulp waar nodig. Onderbouw dit met echt voorbeeld.',
'Ik doe alles tegelijk en werk gewoon harder.',
'Wanneer verloor je overzicht en wat deed je?')
q('Gedrag','Beschrijf een conflict met stakeholder.','Feiten en gezamenlijke uitkomst.',
'Gebruik een echte case met verschillend doel/verwachting. Ik maak de criteria en evidence zichtbaar, stel opties voor en bevestig besluit/actie. Ik beschrijf mijn eigen communicatie en resultaat.',
'De ander was dom; ik had gelijk.',
'Wat zou je volgende keer anders zeggen?')
q('Gedrag','Hoe organiseer je veel parallelle taken?','Capaciteit en prioriteit.',
'Ik houd één zichtbaar overzicht met impact, deadline, owner, afhankelijkheid en status. Ik reserveer incidentruimte, beperk werk in uitvoering en escaleer capaciteitsspanning voordat beloften onhaalbaar worden.',
'Alles in mijn hoofd of altijd meteen nieuwste vraag doen.',
'Wat laat je vallen als productieincident komt?')
q('Gedrag','Hoe geef je taakgericht leiding zonder hiërarchie?','Coördinatie en invloed.',
'Ik spreek resultaat, acceptance, eigenaar en datum af en vraag bewijs/obstakels. Ik coach op taak en escaleer bij mandaatconflict. Ik behandel een leverancier niet als werknemer als dat niet mijn rol is.',
'Iedereen bevelen geven of niets durven afspreken.',
'Wat als iemand afspraken niet nakomt?')
q('Gedrag','Hoe ga je om met onbekende techniek?','Leermethode en eerlijkheid.',
'Ik zoek officiële docs voor gebruikte versie, bouw kleine veilige repro, vraag buddyreview en documenteer wat nog onbekend is. Ik koppel kennis aan concrete taak en test voldoende begrip vóór productieactie.',
'Online commando kopiëren en in productie proberen.',
'Welke output lever je na één leerdag?')
q('Gedrag','Wanneer zeg je nee?','Integriteit en risicobeheersing.',
'Ik begrens een actie die onbevoegd, onveilig of zonder herstelbaarheid is. Ik leg het risico concreet uit en bied een uitvoerbaar alternatief of vraag expliciet besluit aan de juiste owner. Ik blokkeer niet uit gemak.',
'Altijd ja zeggen of alleen “procedure zegt nee”.',
'Hoe behoud je samenwerking?')

q('Ervaring','Welke projectervaring sluit aan?','Eigen bijdrage en transfer.',
'Ik selecteer een echt project met requirement, afhankelijkheid, planning en acceptatie. Ik vertel wat ik zelf deed, hoe ik risico volgde en wat aantoonbaar werkte. Portfolio label ik als portfolio, geen professionele delivery.',
'Teamresultaat volledig aan mezelf toeschrijven.',
'Hoe rapporteerde je afwijkingen?')
q('Ervaring','Heb je Oracle/AIX/JBoss-ervaring?','Productniveau exact kunnen plaatsen.',
'Ik benoem per product: theorie, lab, met hulp of zelfstandig professioneel. Transfer vanuit andere SQL/Unix/runtimeomgeving leg ik concreet uit en voeg productverschillen toe. Een ontbrekend AIX-lab is geen AIX-beheerervaring.',
'Ja zeggen omdat ik Linux of SQL ken.',
'Welke taak deed je zelfstandig en welke met begeleiding?')
q('Ervaring','Toon je beste troubleshootingcase.','Diagnostiek en bewijs.',
'Echte case: verwacht/werkelijk, impact, hypotheses, test, eerste foutgrens, gecontroleerd herstel en preventie. Laat geanonimiseerde runbook/test/logvoorbeeld zien, zonder vertrouwelijke gegevens.',
'Ik restartte en het was opgelost zonder verdere controle.',
'Wat bewees de oorzaak en wat was onzeker?',
'Gebruik maximaal twee minuten: 20 seconden context/impact; 40 seconden hypotheses en onderscheidend bewijs; 30 seconden herstel/validatie; 30 seconden oorzaak/preventie en eigen bijdrage. Als root cause niet bewezen was, zeg dat en licht vervolgwerk toe. Noem alleen echte resultaten of duidelijk synthetische labmetingen.')
q('Ervaring','Welke code/tool heb je gemaakt?','Hands-on delivery en onderhoud.',
'Toon een echte tool met businessprobleem, input/output, validatie, auth indien relevant, logging en tests. Bespreek foutpaden, README en wat je achteraf verbeterde. Leg rolkoppeling uit, niet alleen framework.',
'Alleen UI-screenshot tonen en geen gedrag uitleggen.',
'Wat gebeurt bij duplicaat of timeout?')
q('Ervaring','Heb je leveranciers gestuurd?','Communicatie en acceptance.',
'Ik geef echte afstemming met werkpakket, acceptance en acties. Als ik geen professionele vendorervaring heb, toon ik een simulatie/opdracht en leg ik uit wat ik nog niet heb gedaan, zoals contract-/budgetmandaat.',
'Elke e-mail naar support als volledige leverancierssturing verkopen.',
'Hoe ging je om met incomplete oplevering?')
q('Ervaring','Hoe heb je kennis overgedragen?','Onboarding en gebruikerstraining.',
'Noem een echte instructie/workshop/pairing. Leg doelgroep, taak, oefening, feedback en versiebeheer uit. Laat gebruiker/collega zelf handelen en pas uitleg aan waar begrip ontbreekt.',
'Ik stuurde een link dus ze waren opgeleid.',
'Hoe controleerde je begrip?')
q('Ervaring','Welke gap pak je als eerste aan?','Prioriteit op risico/ROI.',
'Ik kijk naar rolkritiek én mijn bewijs. Ontbrekende SQL/incident/requirements-praktijk heeft hoge prioriteit. Lokale TOS-codes zijn onboardingkennis. Ik kies een oefening met deliverable en stopcriterium en bespreek startbegeleiding.',
'Alles tegelijk leren of alleen de meest trendy stack.',
'Moet je daarvoor wachten met solliciteren?')

body='''
**Waarschijnlijk / afgeleid uit functiecontext — oefenvragen, geen gelekte ICO-interviewvragen.** 56 vragen, acht categorieën. Gebruik de modelantwoorden als structuur. Geen ervan mag fictieve persoonlijke ervaring worden. Een sterk antwoord noemt feitelijke eigen bijdrage, grenzen, bewijs en relatie met de job.

Een 30-secondenantwoord is het korte antwoord hieronder. Een 2-minutenantwoord gebruikt een echte case: context → jouw taak → acties/bewijs → resultaat → reflectie/rolkoppeling. Bij vijf complexe vragen is een langere invulling toegevoegd. De simulator werkt lokaal met timer, notities en zelfbeoordeling; geen AI-score.
'''
for cat in ['HR','Motivatie','Techniek','Scenario','Troubleshooting','Business','Gedrag','Ervaring']:
    body+=f'\n\n## {cat}-vragen'
    for x in [x for x in interviews if x['category']==cat]:
        body+=f"\n\n### {x['id']:02d}. {x['question']}\n\n**Interviewer wil weten:** {x['intent']}\n\n**Sterk / 30 seconden:** {x['strong']}\n\n**Zwak — vermijden:** {x['weak']}\n\n**Vervolgvragen:** {x['follow']}"
        if x['long']: body+=f"\n\n**2 minuten:** {x['long']}"
add(15,'Interview question bank','interview',body)

company_questions=[
('★','Team','Hoe groot is het interne/extern ontwikkelingsteam, wie bezit welk component?'),
('★','Verwachtingen','Welke drie resultaten moet ik na 90 dagen aantoonbaar leveren?'),
('★','TOS','Welk huidig en nieuw TOS gebruiken jullie, in welke implementatiefase zitten jullie?'),
('★','Werkmix','Hoe verdeelt de afgelopen maand zich over programmeren, projectwerk en tweede lijn?'),
('★','Wachtdienst','Hoe vaak word ik ingeroosterd, hoeveel oproepen zijn gebruikelijk, wat zijn dekking/vergoeding/escalatie?'),
('★','Architectuur','Welke versies/varianten van Oracle, AIX, JBoss, WebFOCUS, iWay en Apex zijn werkelijk in gebruik?'),
('★','Onboarding','Welke buddy, documentatie, testomgeving en opleidingsdagen zijn beschikbaar?'),
('★','Autonomie','Welke productiewijzigingen mag deze rol zelfstandig doen en wie autoriseert CRQ/go-live?'),
('★','Releases','Hoe worden database-, app- en integratiechanges samen getest en hersteld?'),
('★','Risico','Wat zijn nu de grootste continuïteits- en projectrisico’s waarvoor jullie deze persoon zoeken?'),
('','Legacy','Welke componenten zitten buiten support en welk moderniseringspad is afgesproken?'),
('','Development','Welke programmeertalen, codebases en reviewafspraken gelden voor eigen development?'),
('','EDI','Welke partners, standaarden, transports en ACK-/retrycontracten zijn het belangrijkst?'),
('','Rapportering','Wie bezit businessdefinities, WebFOCUS-rapporten en masterdata?'),
('','Incidents','Hoe verloopt overdracht van Service Desk naar tweede lijn en hoe worden incidenten geprioriteerd?'),
('','Problems','Is er tijd/owner voor structurele fixes na incidenten, en hoe volgen jullie acties?'),
('','Leveranciers','Welke budget-/contract-/acceptatiebevoegdheid heeft deze rol bij externe partners?'),
('','Portefeuille','Hoe kiezen jullie prioriteit bij meerdere businessunits en beperkt budget/capaciteit?'),
('','Locaties','Welke processen/configuraties verschillen tussen Kallo en Zeebrugge?'),
('','Documentatie','Waar staan actuele runbooks, componentcatalogus en releasehistorie, en wie onderhoudt ze?'),
('','Security','Hoe zijn least privilege, vendor access, audit en security-escalatie geregeld?'),
('','Herstel','Wie bezit backup/restore en hoe vaak wordt herstel inclusief integraties gerepeteerd?'),
('','Talen','Welk niveau Nederlands/Engels/Frans is nodig per stakeholder en taak?'),
('','Remote','Wat zijn afspraken over thuiswerk, presence tijdens releases en wachtdienst?'),
('','Cultuur','Hoe reageert het team als iemand een risico of eigen fout vroeg meldt?'),
('','Management','Hoe vaak heb ik feedbackoverleg met Supervisor en Director IT en wat beoordelen zij?'),
('','Carrière','Welke route bestaat naar senior/lead/architect en welk gedrag toont promotiegereedheid?'),
('','Opleiding','Welke producttraining/certificatie wordt gefinancierd en is er werkbare leertijd?'),
('','Arbeidsvoorwaarden','Hoe werken wagen/cafetariaplan, onkosten, verzekeringen en wachtdienstcompensatie praktisch?'),
('','Succes','Hoe meten jullie effectiviteit, efficiënte implementatie en gebruikersadoptie?')]
add(16,'Vragen aan ICO','interview','''
**Waarschijnlijk / afgeleid uit functiecontext.** ★ markeert de tien meest waardevolle vragen. Verdeel ze over technische en HR-gesprekken; lees niet alle dertig achter elkaar voor. Vraag bij een abstract antwoord een recent concreet voorbeeld.

| Top | Thema | Vraag |
|---|---|---|
'''+ '\n'.join(f'| {star} | {cat} | {question} |' for star,cat,question in company_questions))

projects=[
dict(id=1,title='EDI Reconciliation Lab',duration='1–3 dagen bij SQL/programmeerbasis',requirements='R19/R20/R25/R30',problem='Partner zegt tien events verstuurd, systeem heeft er acht uniek verwerkt.',business='Snel kunnen verklaren of berichten ontbreken, dubbel zijn of geweigerd zonder gevaarlijke replay.',architecture='Synthetische JSON/CSV → validatie → SQLite-lab → reconciliatiequery → CLI/klein rapport. SQL-concepten overdraagbaar; dit bewijst geen Oracle-productbeheer.',technology='Python/SQLite of eigen vertrouwde taal; optioneel Oracle-sandbox. Geen iWay/WebFOCUS-licentie nodig voor conceptbewijs.',requirementsText='Input bevat message_id, business_event_id, partner, vehicle_id, event_type, event_at. Ontbrekende sleutel afwijzen; duplicaten zichtbaar; bron/target op unieke eventkey vergelijken.',features='Importpreview, rejected reasons, duplicatentelling, ontbrekende keys, last successful en geredigeerde evidence-export.',database='vehicles, messages, processing_results; unique business_event_id; synthetische data en expliciete transacties.',integration='Bestandscontract, ACK-simulatie en minimaal drie fixtures: valide, malformed, duplicate. JSON is leerformaat, geen vastgesteld ICO-EDI.',auth='CLI-local demo heeft geen multi-user auth; documenteer beperking. Als webversie: reader/importerrollen en servercontrole.',logging='ID, tijdzone, mappingversie, stap en resultaat; geen secrets of echte klantgegevens.',tests='Verwacht acht unieke successen, één malformed en één duplicate in vaste fixture; test atomiciteit en opnieuw importeren zonder extra effect.',deployment='Reproduceerbaar lokaal script, vaste dependencies/command, optioneel container. Beperking: geen enterprise productie-SLA.',docs='Datadictionary, contract, runbook, incidentrapport en README met setup/sample/expected output.',visuals='Datastroomdiagram plus screenshot van verschilset en duidelijke rejected reason.',proof='SQL, EDI-keten, idempotentie, troubleshooting en Office-achtige reconciliatie. Laat één timeout-after-commit hardop verklaren.'),
dict(id=2,title='Vehicle Exception Portal',duration='Ongeveer één week bij web-/SQLbasis; APEX-productlab kan extra setup vragen',requirements='R11/R12/R14/R21/R22/R31/R09',problem='Een gebruiker moet een locatiecorrectie aanvragen zonder audit of validatie te verliezen.',business='Controleerbare taakflow met rolrechten en gebruikersfeedback, geen handmatige ongedocumenteerde data-update.',architecture='Browser → server-side validatie/autorisatie → relationele DB + audit; optioneel Oracle APEX/ORDS indien sandbox. Moderne equivalent apart labelen.',technology='Oracle APEX + Oracle-sandbox heeft hoogste productsignalering. Anders vertrouwde webstack met SQL en expliciete beperking “conceptueel equivalent”.',requirementsText='Bevoegde rol, geldige actieve locatie, versiecheck, redenplicht, oude/nieuwe toestand, actor/tijd; onbevoegde directe request moet falen.',features='Lijst van uitzonderingen, detail, correctie, optimistic concurrency conflict, auditweergave, export en teach-back instructie.',database='vehicles(version,location_id), locations(active), corrections(actor,reason,old,new,at); schema fictief en migraties versioned.',integration='Simuleer outbound event na correcte transactie; geen echte partnerverbinding. Demo-API-contract met success/forbidden/conflict/validation response.',auth='Reader/operator/admin met objectscope; APEX authorisations of echte serverchecks. Browserknop verbergen is niet voldoende.',logging='Correlation-ID, actor, businesskey en foutcategorie; audit en technische logs onderscheiden.',tests='Happy, invalid location, unauthorized, stale version, duplicate submit, error after commit. UAT-taak door andere persoon laten uitvoeren.',deployment='Testomgeving met manifest/config, changelog, smoke test en recoverybeperking; geen echte ICO-config.',docs='CRQ, functionele/technische analyse, rolmatrix, testbewijs, quick guide en README met bekende beperkingen.',visuals='Architectuur en state diagram, screenshots van happy path, conflict en audit.',proof='Requirements vertalen, portaal bouwen, rights/validatie, dataconsistentie, gebruikersopleiding en releasebewustzijn.'),
dict(id=3,title='Terminal Integration & Cutover Workbench',duration='Flagship: 3–5 weken afgebakend bij relevante basis; geen gegarandeerde leertijd',requirements='R06/R07/R08/R12/R16/R17/R18/R19/R20/R23/R24/R25/R26/R35',problem='Oud/nieuw oefen-TOS, partnerberichten en rapporten moeten bij cutover consistent blijven.',business='Een aantoonbaar beheersbare migratie en incidentrespons met traceerbaarheid, geen alleen mooi dashboard.',architecture='Partner simulator → integratieflow → old/new SQL schemas → report/reconciliation; app/API + browserworkbench; background processing indien nodig. iWay/JBoss/APEX only if licensed/sandbox available.',technology='Eigen bekende backend + SQL + testqueue of durable outbox als ontwerpkeuze. Oracle/JBoss-lab optioneel. Geen claim van echte TOS/iWay/WebFOCUS-ervaring zonder die producten.',requirementsText='Ten minste 100 synthetische events, unieke businesskeys, valide transitions, rejection, retry/backoff, scope per site, fixed snapshot, in-flight delta en go/no-go gates.',features='Message trace, backlog/oldest age, replaypreview, duplicate-safe verwerking, verschillen per key/field, cutover rehearsal en incidenttimeline.',database='vehicles, locations, events, audit, outbox, processing_attempts, migration_runs, reconciliation_diffs; constraints en transacties explicit.',integration='Inbound arrival/location/dispatch simulator; ACK na commit, timeoutinjectie, malformed date, reordered events en partnerroutewissel.',auth='Reader/operator/releaseapprover met server/objectscope; replay en go-livebesluit gescheiden. Audit is lokaal demo-bewijs, geen complianceclaim.',logging='Trace IDs over componenten, first failure, mapping/schema/appversie, timer en businessoutcome; geen fake uptime KPI.',tests='Duplicate/concurrent replay, timeout-after-commit, partial migration, invalid transition, unauthorized site, queue stall en recovery; reconciliatiegate stopt go-live bij verschillen.',deployment='Reproduceerbare dev/test; CI-build/tests als portfoliofeature. Rehearsed release + incompatible migration-case; forward fix/restore verschillen expliciet.',docs='README als ingang, componentcatalogus, contract, CRQ, zes werkpakketten, risicolog, fictieve budgetforecast, releaseplan, runbooks, post-mortem en wekelijkse businessupdate.',visuals='Architecture/state diagram, trace screenshot, diff-report en readinessmatrix. Film 3-minuten-demo met één injected failure.',proof='Business/system thinking, SQL/integratie, gecontroleerde delivery, vendor simulation, incidentmanagement en beide-site scope. Begrens enterpriseclaims en laat gaps zien.')]
body='''
**Waarschijnlijk / afgeleid uit functiecontext — portfolio-ontwerpen, geen ICO-systemen.** Deze repository bevat het leerinstrument; onderstaande drie projecten zijn afzonderlijke bouwopdrachten, niet reeds gebouwde enterprise-applicaties. Gebruik synthetische data. Bouw liever één geloofwaardige verticale flow met foutpaden dan veel schermen zonder gedrag.
'''
for x in projects:
    body+=f"\n\n## Project {x['id']} — {x['title']}\n\n**Omvang:** {x['duration']}. **Vacaturekoppeling:** {x['requirements']}.\n\n"
    for label,key in [('Probleem','problem'),('Businesscase','business'),('Architectuur','architecture'),('Technologie','technology'),('Requirements','requirementsText'),('Features','features'),('Database','database'),('API/integraties','integration'),('Authentication','auth'),('Logging','logging'),('Tests','tests'),('Deployment','deployment'),('Documentatie en README','docs'),('Screenshots/diagrammen','visuals'),('Wat dit bewijst','proof')]:
        body+=f'**{label}:** {x[key]}\n\n'
    body+='**Definition of done:** clone/setup reproduceerbaar, positieve en negatieve tests draaien, één failure live demonstreren, businessresultaat uitleggen, beperkingen eerlijk labelen en concrete vacancy-IDs in README.\n'
add(17,'Portfolio strategie','portfolio',body)

add(18,'Bewijsmatrix','skills','''
**Persoonlijk profiel ontbreekt.** Geen CV/GitHub/zelfscore aangeleverd. “Niet beoordeeld” betekent onbekend, niet onbekwaam. Vul in de app bewijslinks en huidig niveau in. Er wordt niets automatisch uit je GitHub geïnterpreteerd. Om later te personaliseren zijn projectlink, eigen bijdrage, gebruikte techniek, context (werk/lab), datum en resultaat nodig.

| Requirement | Mijn bewijs | Wat ontbreekt nog? | Bouwen/leren |
|---|---|---|---|
'''+ '\n'.join(f"| {r[0]} — {r[1]} | Niet beoordeeld; invullen | Bewijs/niveau onbekend | {('Praktische afspraak met HR/ICO; geen portfoliobewijs nodig' if r[0] in ['R01','R02','R03','R05'] else r[3])} |" for r in requirements)+'''

Bewijssterkte: definitie kunnen uitleggen < oefenresultaat < reproduceerbaar project met negatieve tests < eigen professionele bijdrage met resultaat. Een credential ondersteunt een basis; bewijst geen productievaardigheid. Gebruik geen vertrouwelijke gegevens in een openbaar portfolio. De tracker bewaart bewijs uitsluitend lokaal; een export is door jou te beheren.
''')

add(19,'Gap analysis','skills','''
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
''')

roadmap=[]
def learn(period,title,theory,practice,deliverable,goal,enough):
    roadmap.append(dict(id=len(roadmap)+1,period=period,title=title,theory=theory,practice=practice,deliverable=deliverable,goal=goal,enough=enough))
learn('Dag 1','Rol en keten','V1, componentlagen, RoRo/procesbasis','Teken één fictieve voertuigflow; markeer zeker/onzeker','1 pagina rolkaart + 10 interviewvragen','Rol zonder jargon uitleggen','Je noemt 5 outputs, 5 onzekerheden en owners.')
learn('Dag 2','SQL en datakwaliteit','Keys, joins, nulls, datum, transaction','Maak 20 synthetische records met duplicates/nulls','5 queries + expected resultaten','Read-only afwijkingen vinden','Je verklaart rijvermenigvuldiging en gebruikt parameters.')
learn('Dag 3','EDI en veilige retry','Transport/ACK/commit, mapping, idempotentie','Verwerk valide/duplicate/malformed samples','Message trace en replaytest','Ontvangst van businessresultaat onderscheiden','Replay geeft geen dubbel effect; verschilset klopt.')
learn('Dag 4','Troubleshooting','Impact/scope/hypothesen/bewijs','Los login, mapping en traag rapport hardop op','3 incident/evidence packs','Eerste foutgrens en owner kiezen','Twee hypotheses, veilige test en gebruikersvalidatie per case.')
learn('Dag 5','Requirements en CRQ','Businessvraag, acceptance, impact/recovery','Schrijf locatiecorrectie inclusief rechten/conflict','CRQ + 6 work packages + testmatrix','Technische opdracht aan partner geven','Onbevoegde actie en timeout zitten in acceptance.')
learn('Dag 6','Portal en runtime','APEX-route/JBoss/database; security','Bouw kleine demo of verifieer auth/validatie in lab','Werkende taakflow of gecontroleerde repro','Laagbegrip aan praktisch bewijs koppelen','Je toont één happy en twee foutpaden, geen fake productclaim.')
learn('Dag 7','Interview en bewijs','STAR, bekende/onbekende facts, positioning','Oefen 8 vragen en 2 scenario’s met timer','README, gap-top-3 en 30s/2min verhaal','Solliciteren met eerlijk concreet bewijs','Je rolverhaal, casus en 10 ICO-vragen zijn helder.')
learn('Week 1 / dagen 1–7','Crash course afronden','De zeven onderwerpen hierboven','Elke dag 2–3 gefocuste uren, meer indien basis ontbreekt','Project 1 eerste versie + bewijskaart','80/20-basis zonder rabbit holes','Crash-output compleet, onzekerheden zichtbaar.')
learn('Week 2 / dagen 8–14','SQL/EDI verdiepen','Atomiciteit, ordering, ACK en reconciliation','Project 1 test met parallelle duplicates en partial failures','Testlog + runbook + incidentrapport','Zelfstandig kleine flow onderzoeken','Je kunt onverwachte input veilig uitleggen en herhalen.')
learn('Week 3 / dagen 15–21','Portaal en gebruikersflow','APEX indien bevestigd, validatie/rollen/audit','Project 2 bouwen; iemand anders doet UAT','Portal + CRQ + quick guide','Businessvraag gecontroleerd opleveren','Unauthorized, stale version en invalid location getest.')
learn('Week 4 / dagen 22–30','Release en interview','Manifest, compatibility, recovery, stakeholders','Demo-uitrol/recovery, 16 interviewvragen en 5 scenario’s','Release evidence + CV-projectbeschrijving','Voldoende bewijs voor inhoudelijk gesprek','Je zegt precies wat je wel/niet zelfstandig gedaan hebt.')
learn('Week 5 / dagen 31–37','Runtime/platformdiagnose','JBoss pools/exceptions en Unix/AIX-laag','Simuleer permission/datasource/diskprobleem veilig','3 laag-evidence packs','Gericht specialist inschakelen','Eerste fout en benodigde meting zijn helder.')
learn('Week 6 / dagen 38–44','Vendor en capaciteitssturing','Work packages, forecast en acceptance','Simuleer leverancier die extra scope/uren vraagt','Actielog, risk log, budgetforecast','Businessbesluit onderbouwen','Twee opties met consequenties en eigenaar.')
learn('Week 7 / dagen 45–51','Flagship verticale flow','Outbox/retry/backlog als ontwerpopties','Project 3 één partner/site end-to-end bouwen','Trace + duplicate-safe verwerking','Keten met foutpaden bewijzen','Timeout na commit levert geen dubbel business-effect.')
learn('Week 8 / dagen 52–60','Cutover/reconciliatie','Snapshot, in-flight, key/field differences','Project 3 old/new schema en cutovergate','Rehearsal + go/no-go-matrix','Datamigratie op bewijs beoordelen','Bij ontbrekend record stopt demo go-live met uitlegbare reden.')
learn('Week 9–10 / dagen 61–74','Observability en hardere scenario’s','Business health, metrics, first failure, exposure','Queue stall, retry-storm, multi-site en scopeleak lab','4 post-mortems + monitorregels','Breder risico overzien zonder expertclaim','Je meet businessuitkomst en bewaart bewijs veilig.')
learn('Week 11–12 / dagen 75–88','Overdracht en sollicitatieverdieping','Training, rapportdefinities, eigen bewijsverhaal','Demo met key-userrol, 20 vragen/10 scenarios en CVreview','Complete README, teach-back, skillsupdate','Resultaat begrijpelijk aan diverse stakeholders tonen','Iemand kan setup/taak uitvoeren zonder jouw live hulp.')
learn('Dagen 89–90','Herijk en beperk scope','Risico-/ROI-afweging','Audit bewijs tegen R01–R35, kies resterende top-3 gaps','Definitieve proof matrix en next steps','Leren richten op echte vacature','Geen open kritiek foutpad; onbekende company facts blijven onbekend.')

add(20,'Gericht leerplan','roadmap','''
**Waarschijnlijk / afgeleid uit functiecontext.** Bandbreedte: 2–3 gerichte uren per dag naast werk indien basiskennis aanwezig is; minder basis betekent langer, niet een magische 7-dagenkwalificatie. Dag 1–7 is één crash course; week 1 vat die samen, geen extra leerweek. Solliciteren kan parallel. Learning roadmap is voorbereiding; het 30/60/90-plan in hoofdstuk 23 is voor ná indiensttreding.

Stop zodra je het concrete deliverable met negatieve test en uitleg kunt laten zien; besteed resterende tijd aan volgende kritieke gap. Productlicenties ontbreken? Gebruik een conceptlab en benoem transferbeperking.

| Dag/week | Onderwerp | Theorie | Praktijk | Deliverable | Leerdoel | Goed genoeg |
|---|---|---|---|---|---|---|
'''+ '\n'.join(f"| {x['period']} | {x['title']} | {x['theory']} | {x['practice']} | {x['deliverable']} | {x['goal']} | {x['enough']} |" for x in roadmap))

add(21,'Wat moet ik niet leren?','roadmap','''
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
''')

add(22,'Sollicitatiestrategie','interview','''
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
''')

onboarding=[
('Eerste 30 dagen','Begrijpen en veilig bijdragen','Supervisor/Director, Service Desk, projectcoördinator, key users per site en component-/vendorowners spreken. Toegang, omgeving en escalatie oefenen. Eén belangrijke businessflow en componentkaart valideren. Shadow minstens enkele representatieve tickets, afhankelijk van beschikbaarheid. Kleine documentatiefix of read-only reconciliatie onder review.','Gevalideerde rol/RACI, proces- en componentkaart, toegang/checklist, twee gereviewde evidence packs en top-5 risico’s. Zelfstandig uitleggen wie welke productieactie mag doen. Wachtdienst alleen na afgesproken readiness.'),
('Dag 31–60','Afgebakend zelfstandig uitvoeren','Binnen mandaat enkele tweede-lijncases afhandelen, één CRQ/werkpakket coördineren, partnerfix in test valideren, kleine portal/toolchange opleveren en gebruikersinstructie bijwerken. Weekrapport met risico/capacity/budget.','Een geaccepteerde change met test/release/recoverybewijs, incidentafsluiting met data/gebruikersvalidatie en buddyfeedback. Nog geen onbewezen totale TOS-eigendom.'),
('Dag 61–90','Ownership van een duidelijk domein','Met supervisor afgebakend component/integratie/projectwerkpakket opnemen. Eén herhaald probleem structureel oplossen, monitoring/documentatie verbeteren en een release met partners coördineren.','Domein-eigenaarschap afgesproken, runbook door collega bruikbaar, problemactie met effectbewijs, betrouwbare forecast en gepresenteerde 90-dagenreview. Nieuwe doelen op werkelijke prioriteiten.')]
add(23,'30 / 60 / 90 dagen na start','roadmap','''
**Waarschijnlijk / afgeleid uit functiecontext — voorstel voor onboarding, geen ICO-beoordelingsnorm.** Stem milestones af op toegang, projectfase, changevensters en team. Productierechten en wachtdienst-readiness komen niet vanzelf met een kalenderdatum.
'''+''.join(f'\n\n## {period} — {goal}\n\n**Werk en contacten:** {work}\n\n**Milestones / bewijs:** {milestone}' for period,goal,work,milestone in onboarding)+'''

## Reviewvragen aan supervisor

Wat kan ik al zelfstandig, welke fouten/risico’s vermijd ik goed, waar is nog review nodig, welke outputs helpen het team en welke verantwoordelijkheid moet de komende maand groeien? Noteer besluiten en opvolging. Geen performancepercentage verzinnen.
''')

add(24,'First week survival guide','roadmap','''
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
''')

add(25,'Performance playbook: 6–12 maanden','career','''
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
''')

add(26,'Career path','career','''
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
''')

add(27,'Moeilijkheidsgraad','career','''
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
''')

add(28,'Red flags / green flags','career','''
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
''')

add(29,'Cheat sheet voor het gesprek','interview','''
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
''')

add(30,'Final assessment en acties','overview','''
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
''')

# Assemble the standalone handbook and the app's structured datasets from one source.
chapters.sort(key=lambda x:x['id'])
summaries=['Taken, outputs, succesfactoren en de rol in gewone taal.','Alle 35 vacaturevereisten vertaald naar praktijk en prioriteit.','Een illustratieve dag, werkweek en realistische tijdverdeling.','Eigenaarschap, sterke uitvoering, juniorfouten en sollicitatiebewijs.','Componenten, datastromen en expliciet gemarkeerde onzekerheden.','16 technische onderwerpen met oefeningen, interviewuitleg en jargon.','RoRo, automotive en de samenhang tussen fysieke operatie en data.','Niveaus, prioriteiten en de tien skills met hoogste leer-ROI.','Impact, hypotheses, systeemgrenzen en veilig beslissen.','Een diagnostisch framework en 14 gedetailleerde incidentrunbooks.','Procesverschillen en interactieve checks voor gecontroleerde delivery.','Van businessprobleem naar CRQ, testbare oplossing en nazorg.','Communicatie met gebruikers, leiding en externe partners.','25 oefencases van loginprobleem tot TOS-cutover.','56 vragen met intentie, sterke/zwakke antwoorden en vervolgvragen.','30 gerichte vragen aan ICO, met de beste tien gemarkeerd.','Drie concrete bouwopdrachten die vacaturevereisten bewijzen.','Bewijs per R-ID; jouw profiel is nog niet persoonlijk beoordeeld.','Kennis, praktijk, ervaring, diploma en vertrouwen apart beoordelen.','Een crash course en leerroadmap met concrete stopcriteria.','Vermijd rabbit holes en leer lokale kennis tijdens onboarding.','Positioneer echte ervaring en bespreek productgaps eerlijk.','Milestones en verantwoordelijkheden na indiensttreding.','De eerste vijf werkdagen: toegang, mensen, processen en mandaat.','Betrouwbare uitvoering en groei naar bovengemiddelde bijdrage.','Technische, project-, business- en managementroutes.','Scores en onzekerheden rond breedte, stress en zelfstandigheid.','Positieve signalen en aandachtspunten die je moet verifiëren.','Compacte herhaling vlak vóór je sollicitatiegesprek.','Tien kernvaardigheden, risico’s, kansen en acties voor deze week.']
for x,summary in zip(chapters,summaries):x['summary']=summary
assert [x['id'] for x in chapters]==list(range(1,31))
assert len(scenarios)==25 and len(interviews)==56 and len(company_questions)>=25
sources= (ROOT/'research/DOSSIER.md').read_text()
data=dict(chapters=chapters,requirements=[dict(id=r[0],text=r[1],meaning=r[2],practice=r[3],difficulty=r[4],importance=r[5]) for r in requirements],skills=[dict(name=x[0],level=x[1],priority=x[2],requirements=x[3],why=x[4],proof=x[5]) for x in skills],tech=tech,scenarios=scenarios,interviews=interviews,projects=projects,roadmap=roadmap,sources=sources)
(ROOT/'src').mkdir(exist_ok=True)
(ROOT/'src/content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
toc='\n'.join(f"{x['id']}. [{x['title']}](#{x['id']:02d})" for x in chapters)
book='# ICO IT Development Officer — Job Blueprint / Role Playbook\n\nOnderzocht 7 oktober 2026. Onafhankelijk leerinstrument; geen intern ICO-handboek. Geen persoonlijke CV-analyse zonder profiel.\n\n'+toc+'\n\n'+ '\n\n'.join(f"<a id=\"{x['id']:02d}\"></a>\n\n# DEEL {x['id']:02d} — {x['title']}\n\n{x['body']}" for x in chapters)
(ROOT/'docs/JOB-BLUEPRINT.md').write_text(book)
(ROOT/'public').mkdir(exist_ok=True)
(ROOT/'public/JOB-BLUEPRINT.md').write_text(book)
print(json.dumps(dict(chapters=len(chapters),requirements=len(requirements),technologies=len(tech),scenarios=len(scenarios),incident_playbooks=len(incident_ids),interview_questions=len(interviews),company_questions=len(company_questions),words=len(book.split())),indent=2))
