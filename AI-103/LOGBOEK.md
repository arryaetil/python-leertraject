# AI-103: logboek

Nieuwste sessie bovenaan. Per sessie: wat gedaan, wat lastig was, volgende stap.

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

