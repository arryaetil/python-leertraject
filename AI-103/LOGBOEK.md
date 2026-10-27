# AI-103: logboek

Nieuwste sessie bovenaan. Per sessie: wat gedaan, wat lastig was, volgende stap.

---

## 27 oktober 2026: Tutoring op examenniveau (dag voor het controlemoment)

- **Context:** tussen 21 en 26 okt niets gelogd; planning van die dagen staat nog open. Morgen 28 okt practice assessment (doel ≥ 70%).
- **Afspraak:** vragen voortaan in het **Engels** (feedback NL), op echte examenhardheid: geen opmaak of sleutelwoorden die het antwoord verraden, alle opties echte Azure-keuzes.
- **Uitslag: 2/7 gemeten** (Q1 telt niet: vraag verraadde het antwoord).
  - Q2 opinion mining + PII-codefragment (3 slots) ❌: slot 1 `AnalyzeSentimentAction()` i.p.v. `show_opinion_mining=True`. Eis "each individual part" gemist. Slot 2 (categories filter) en 3 (`redacted_text`) goed.
  - Q3 deployment types ✅: Data Zone Batch (nachtjob, EU, goedkoopst, eigen quota) en Data Zone Standard (chat, EU, per token).
  - Q4 document translation ❌: koos text API (A) i.p.v. D. B, C en E goed weggestreept, maar D overgeslagen omdat **glossary** onbekend was.
  - Q5 orchestration workflow (CLU + custom question answering) ✅, vond hem moeilijk, goed geëlimineerd.
  - Q6 MCP-tool met approval (4 slots) ❌: `require_approval="always"` en `mcp_approval_request` goed; Key Vault-secret in code gekozen i.p.v. `project_connection_id`, `tool_choice` i.p.v. `previous_response_id`.
  - Q7 Docker-container ❌: deel 2 goed (tekst blijft lokaal, alleen metering naar Azure), deel 1 (`Eula`, `Billing`, `ApiKey`) **open gelaten**.
  - Q8 SSML choose four ❌: `say-as`, `sub`, `break` goed; vierde (`prosody rate`) niet gegeven.
- **Patroon (hetzelfde als 20 okt, nu scherper):** de fouten zijn leesfouten, geen gebrek aan begrip.
  1. Eén eis gemist (Q2).
  2. Laatste overgebleven optie niet langs de eisen gelegd (Q4).
  3. Eis samengevat in een eigen label ("keyless") dat de betekenis veranderde (Q6).
  4. Delen open gelaten (Q7, Q8).
  Eisen en zeker/twijfel/gok werden bijna nooit opgeschreven, ook niet na herhaald vragen.
- **Gevoel:** codevragen voelen taai, "nog maar 2 weken". Bijgestuurd: het zijn 11 dagen, de practice assessment had weinig codevragen, en bij elke codevraag was minstens de helft van de slots goed. Codevragen = per slot één eis zoeken, wegstrepen wat niet bestaat of een eis breekt.
- **Nieuwe examenregels** toegevoegd (glossary, onbekend ≠ fout bij gelijke opties, E-B-A containers, connections, `previous_response_id`, orchestration workflow, conversation summarization, Data Zone Batch).
- **Volgende stap:** 28 okt 's avonds practice assessment in rust. Bij elke vraag de eisen in de woorden van de vraag opschrijven, niets open laten. Daarna 20 min per dag codefragmenten lezen.

---

## 20 oktober 2026: Toets tekst & spraak op examenniveau + nieuwe routine

- **Gedaan:** 5 vragen op examenniveau (specifieke servicenamen, afleiders die bijna goed zijn). Uitslag: **1/4** gemeten, vraag 5 telt niet (gespiekt in de kaart). Ook bij vraag 4 gespiekt.
  - 1 opinion mining ✅ (zekerheid niet genoemd)
  - 2 conversational PII ❌ (koos gewone PII detection: werkt wel, maar is niet "designed for this input")
  - 3 document translation + glossary ❌ **"heel zeker"** maar fout: eis "originele opmaak behouden" gemist
  - 4 CLU: gespiekt, telt als niet geweten
  - 5 SSML: gespiekt
- **Patroon:** kiest op één signaalwoord en checkt de andere eisen niet. Nieuwe werkwijze: eisen opschrijven → elke optie tegen álle eisen → dan kiezen. Altijd zeker/twijfel/gok noemen.
- **Inzicht van Arrya zelf:** eerst de kaart leren, dan toetsen. Terecht: bij ~13% meet toetsen vooral wat er nog niet is.
- **Coach:** "ik ken alles op hoog niveau, alleen de termen nog" is deels waar (principes kloppen), maar de termen en use cases zíjn het examen. Afspraak: tempo bepaald door toetsscore (8/10 zonder spieken = door).
- **Ook:** kaart vertaald naar het Engels (zoeken op "aspect" vindt opinion mining). Dagnamen in beide planningen rechtgezet: examen is **zaterdag** 7 november.
- **Routine vanaf nu:** 's avonds ~1 uur kaart leren, de dag erna op werk ~1 uur toetsen, plus Python.
- **Volgende stap:** vanavond Text & language + Service picker (tekst, vertalen). Morgen op werk 10 vragen tekstanalyse, kaart dicht.

---

## 19 oktober 2026: Foundry-kaart gebouwd

- **Aanleiding:** na de practice assessment zei ze zelf waar het misging: "veel vragen gingen over kiezen tussen services, maar ik wist niet goed wat ze inhielden en wanneer ik ze moest toepassen". Daarnaast vragen over Azure CLI-commands, Docker-containers en configuratiewaarden. Codevragen waren er minder dan verwacht.
- **Gemaakt:** [`foundry-kaart.html`](foundry-kaart.html) met 85 onderwerpen in 10 groepen, laag voor laag doorklikbaar. Per onderwerp: wat het is, wanneer je het kiest, code, configuratie en examenvalkuilen. Bovenaan een servicekiezer met vergelijkingstabellen. Zoeken, filter per examendomein, licht/donker, en "Snap ik" om je voortgang bij te houden.
- **Bronnen:** officiële studiegids (16 april 2026) en Microsoft Learn (okt 2026). De SDK-code voor modellen, agents en MCP-approvals is gecontroleerd tegen de actuele docs. De overige code is een schets om te leren lezen.
- **Volgende stap:** elke sessie begint met de servicekiezer van het onderwerp van die dag. Markeer "Snap ik" alleen als je het zonder spieken kunt uitleggen.

---

## 19 oktober 2026: Officiële practice assessment

- **Gedaan:** officiële practice assessment van Microsoft. Gepland op 18 okt, een dag later gedaan. Uitslag **63%** (doel 80%). Details in [`niveautests/2026-10-19-practice-assessment.md`](niveautests/2026-10-19-practice-assessment.md).
- **Sterk:** vision (~82%), Plan & manage (~75%), info-extractie (~71%).
- **Zwak:** tekstanalyse (~13%) en GenAI & agents (~59%). Samen het grootste deel van de gemiste punten.
- **Coach:** de coachtest van 17 okt was te makkelijk (tekst 2/2 vs. ~13% officieel). Vanaf nu meet alleen de officiële assessment.
- **Planning herschikt:** eerst tekst & spraak (20–21 okt), dan GenAI & agents (22–26 okt), Plan & manage compact op 27 okt. Controlemoment 28 okt blijft.
- **Volgende stap:** vandaag nog alle foute vragen nalezen. Ma 20 okt: tekstanalyse.

---

## 17 oktober 2026: Niveautest AI-103 + studieplan

- **Gedaan:** coachtest van 15 vragen, verdeeld naar de examengewichten. Uitslag **13/15**, maar maar **8 echt geweten**. 5 goed via eliminatie of gok. Details in [`niveautests/2026-10-17-ai103.md`](niveautests/2026-10-17-ai103.md).
- **Fout van de coach:** bij vraag 3 stond het juiste antwoord vetgedrukt. Zelf eerlijk gemeld ✅. Telt als niet geweten.
- **Sterk:** elimineren en principes (RAG vs. fine-tuning, tools voor live data, "prompt is verzoek, code is garantie"). Stelde goede vervolgvragen (RRF vs. semantic ranker, temperature vs. top_p, seed).
- **Lastig:** Plan & manage (3/5). Provisioned throughput, 429, tracing en Application Insights waren onbekend. Bij vraag 10 Application Insights weggestreept *omdat het onbekend was*: dat is de verkeerde eliminatie.
- **Afspraak:** bij vraag 5 eerst "geen idee". Teruggestuurd → via eliminatie goed. Nooit meer een vraag open laten.
- **Gevoel:** stress over 7 november. Eerlijk beeld: haalbaar met ~50 uur in 21 dagen, alleen zonder gemiste dagen.
- **Volgende stap:** za 18 okt de officiële practice assessment als nulmeting. Planning per dag staat in [`VOORTGANG.md`](VOORTGANG.md), examenregels in [`notities/ai103-examenregels.md`](notities/ai103-examenregels.md).

