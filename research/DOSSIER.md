# Researchdossier — ICO IT Development Officer

Onderzoeksdatum: 7 oktober 2026. Opgesteld als onafhankelijk sollicitatie- en leerinstrument. Geen intern ICO-handboek en geen relatie met ICO. Publieke beschrijvingen kunnen achterlopen op de operationele omgeving. Geen persoonlijk profiel aangeleverd; geschiktheid blijft onbeoordeeld.

## Onderzoeksmethode

De vacature en twee bedrijfscontextpagina’s zijn met Firecrawl opgehaald en gelezen. Officiële IBM-, Red Hat- en TIBCO-documentatie is gebruikt voor productconcepten. Oracle APEX is via Context7 eerst geïdentificeerd en daarna in de officiële 24.2-documentatie opgezocht. Deze documentatieversie is een leerreferentie, geen aanwijzing voor de ICO-versie. Zoekresultaten voor vergelijkbare rollen worden alleen als context gebruikt na inhoudelijke inspectie.

## Bronnenregister

| ID | Bron | Wat deze bron ondersteunt | Beperking |
|---|---|---|---|
| V1 | [Vacature IT Development Officer](https://www.icoterminals.com/nl/jobs/it-development-officer) | Taken, competenties, stacknamen, rapportagelijnen, Kallo/Zeebrugge, arbeidsvoorwaarden | Geen publicatiedatum, productversies, teamomvang of SLA’s |
| B1 | [Toegangspoort tot Europa](https://www.icoterminals.com/nl/over-ico/de-toegangspoort-tot-europa) | RoRo, automobielindustrie, maritieme verbindingen en Europese distributie | Geen intern operationeel procesmodel |
| B2 | [Innovatie en digitalisatie](https://www.icoterminals.com/nl/over-ico/innovatie-en-digitalisatie) | Publieke ambitie in technologie, logistieke efficiëntie en duurzaamheid | Marketingtekst; geen bewijs van bepaalde technische implementaties |
| T1 | [IBM AIX-documentatie](https://www.ibm.com/docs/en/aix/7.3.0) | AIX-platform en systeembeheerconcepten | Geen bewijs van versie 7.3 bij ICO |
| T2 | [Red Hat JBoss EAP](https://docs.redhat.com/en/documentation/red_hat_jboss_enterprise_application_platform/7.4/html/introduction_to_jboss_eap/index) | Application server, subsystemen, standalone/domain en HA als productmogelijkheden | Vacature zegt JBoss; EAP, WildFly en versie onbekend |
| T3 | [Oracle APEX-documentatie 24.2](https://docs.oracle.com/en/database/oracle/apex/24.2/) | Databasegebaseerde applicatieontwikkeling, sessies, authenticatie en autorisatie | Apex in vacature is waarschijnlijk Oracle APEX, niet bevestigd |
| T4 | [ibi WebFOCUS](https://www.ibi.com/products/ibi-webfocus) | BI-/analytics- en rapportageconcepten | Productpagina; versie en exacte inrichting onbekend |
| T5 | [ibi iWay Service Manager](https://www.ibi.com/products/ibi-iway-service-manager) | Integratie- en middlewareconcepten | Productpagina; iWay-productvariant onbekend |
| C1 | [AGL TOS Solution Expert](https://acareerbyagl.talent-soft.com/job/job-terminal-operating-solution-expert-tos-solex-h-f_9597.aspx?LCID=1033) | Requirements, configuratie/development, UAT, EDI en support komen samen in een TOS-rol | Andere werkgever/locatie; Java/Groovy/.NET/SQL Server/EDIFACT-eisen gelden niet voor ICO |
| C2 | [PTP TOS Manager](https://www.careers-page.com/port-of-tanjung-pelepas-sdn-bhd/job/5W949Y73) | Continuïteit, datakwaliteit, UAT, vendor support en gebruikerstraining | Containerterminal, managementniveau en andere regio; geen ICO-selectiecriteria |
| L1 | [LinkedIn ICO](https://www.linkedin.com/company/international-car-operators/) | Officiële verwijzing op bedrijfswebsite | Firecrawl-toegang geblokkeerd door enrichment-instelling; inhoud niet gebruikt |

## Bevestigde feiten en gevolgtrekkingen

**Expliciet uit vacature — V1:** permanente functie in Zeebrugge, 38 uur; dagshift; korte verplaatsingen één à twee keer per maand; Service Desk-wachtdienst. Master of bachelor gelijkgesteld door ervaring in een IT-richting. Technische projectplannen, specificaties, behoeftenanalyse, technisch lastenboek en werkpakketten in een CRQ. Implementatiebegeleiding, gebruikersopleiding, outsourcing, capaciteit en budget. Applicatiecomponenten modelleren, releases coördineren, TOS-gerelateerde omgeving met IBM P-series/AIX/Oracle/JBoss beheren, EDI en rapportering via WebFOCUS/iWay, webportalen, functionaliteiten en koppelingstools ontwikkelen. Projectportefeuille, afwijkingen bijsturen, tweede lijn incident/problem/change, wekelijkse rapportage, samenwerken met intern/extern team en nieuwe medewerkers trainen. MS Office, PRINCE2 of alternatief, analytisch en communicatief handelen, plannen, stressbestendigheid, taakgericht leidinggeven, IT-evoluties volgen, talen N/E/F. Rapporteert aan IT Development Supervisor en Director IT; stuurt ontwikkelingsteam/externe partners aan; contacten met projectcoördinator, business units, leveranciers en klanten; applicatieverantwoordelijkheid voor Kallo en Zeebrugge. Ondersteunt kwaliteits-, veiligheids- en milieumanagement. Waarden integriteit, intensiteit, innovatie. Genoemde voordelen: maaltijd-/ecocheques, groeps- en hospitalisatieverzekering, GSM/laptop, firmawagen, onkostenvergoeding, cafetariaplan en opleiding.

**Bevestigde publieke bedrijfscontext — B1/B2:** ICO beschrijft RoRo-goederenbehandeling in Zeebrugge/Antwerpen, automotive en internationale distributie, met nadruk op digitalisatie en duurzaamheid.

**Waarschijnlijk / afgeleid uit functiecontext:** transacties rond voertuigidentiteit, locatie, ontvangst/vertrek; tijdkritische ketenintegraties; test/acceptatie/productie; SQL, Java-gerelateerde troubleshooting, releasebewijs en migratiereconciliatie. Dit zijn oefenmodellen. VIN-schema’s, scanapparatuur, ticketpakket, incidentprioriteiten, beschikbaarheidseisen en procedures zijn niet vastgesteld.

## Onbekend — tijdens interview toetsen

TOS-leverancier en nieuw TOS, implementatiefase, huidige lifecycle/supportstatus, programmeertalen en hoeveelheid eigen code, APEX-identiteit, Oracle-versie, JBoss-variant, iWay-variant, EDI-standaard (EDIFACT/XML/anders), transport (SFTP/AS2/API/anders), auth/SSO, cloud, back-up/DR, CI/CD, monitoring, netwerk, rechten, teamomvang, wachtdienstfrequentie/vergoeding, budgetmandaat, SLA en thuiswerk. Geen van deze punten mag als ICO-feit worden gelezen.

## Vergelijkbare rollen

Gezocht op terminal application support, TOS, EDI en applicatieanalist. De eerste resultaten waren voornamelijk aggregators, generieke vacatures en een maritieme personeelsorganisatie met een andere betekenis van TOS. Een gerichtere tweede zoekronde vond C1/C2; beide volledige beschrijvingen zijn gelezen. C1 combineert businessrequirements, ontwikkeling/configuratie, UAT, omgevingen, rapportmapping en EDI; C2 combineert stabiele TOS-operatie, datakwaliteit, monitoring, vendor support, acceptatie en training. Dit ondersteunt het hybride karakter als sectorvergelijking, maar geen ICO-werkpercentages, technologieversies, senioriteitseis of salaris. De dagelijkse modellen blijven **Waarschijnlijk / afgeleid uit functiecontext**. Salarisclaims van aggregators zijn niet gebruikt.

De eerste TIBCO-documentatieroutes voor WebFOCUS/iWay kwamen uit op een generieke landingspagina; die inhoud is niet als productspecifieke documentatie gebruikt. Via aanvullende zoekresultaten zijn de juiste ibi-productpagina’s gevonden en gelezen. UI-/syntaxdetails van iWay/WebFOCUS worden bewust niet als geverifieerd versieadvies gegeven.

## Betrouwbaarheidsregels

1. Stacknamen uit V1 zijn bevestigd; verbindingspijlen en eigenaarschap zijn hypotheses.
2. Elke werkdag, incident, portfolio-opdracht en interviewantwoord is een leervoorbeeld.
3. Geen fictieve professionele ervaring. Antwoorden personaliseren met werkelijk eigen bewijs.
4. Geen productiecommando’s blind uitvoeren: eerst autorisatie, scope, herstelplan en validatie.
5. Percentageverdelingen, moeilijkheid en leertijden zijn adviesinschattingen, geen metingen bij ICO.
