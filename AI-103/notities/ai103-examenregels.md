# AI-103 examenregels

Vuistregels uit de niveautest van 17 oktober 2026. Elke dag 10 minuten doorlezen. Vul aan met wat je leert.

## Werkwijze op het examen
- Nooit een vraag open laten. Een gok heeft 25% kans, een open vraag 0%.
- Streep alleen weg wat je **zeker** weet dat fout is, niet wat je niet kent.
- Zoek het échte argument in de vraag: *actueel*, *keyless*, *minimal effort*, *reliably*, *guaranteed*.
- Schrijf eisen op **in de woorden van de vraag**, niet in een eigen label ("key not in code" ≠ "keyless").
- Ook de laatst overgebleven optie langs **alle** eisen leggen voordat je kiest of afwijst.
- Onbekend woord dat in meerdere opties staat? Dan gaat de vraag daar niet over: beslis op het verschil tussen die opties. Een **bekende fout** weegt zwaarder dan een onbekend woord.
- Codevraag: elke slot hoort bij één eis. Streep weg wat niet bestaat of een eis breekt. "Choose three/four" = alle vakjes invullen.

## Plan & manage
- "No keys / keyless" → **managed identity + RBAC-rol**. Key Vault is nog steeds een sleutel (valkuil).
- Hoog en stabiel verkeer + garantie → **provisioned throughput (PTU)**. Wisselend verkeer → **Standard**.
- `--sku-capacity`: Standard-familie = eenheden van **1.000 TPM** (50 = 50.000 TPM, ~6 RPM per 1.000 TPM). Provisioned = **aantal PTU's** (per uur betaald, ook ongebruikt; vol = ook 429, spillover naar Standard).
- Least privilege in Foundry: bouwen/agents/modellen aanroepen → **Azure AI User** op **project**-scope. Contributor = control plane (deployments verwijderen) én geen data actions. Projecten maken + rollen uitdelen → Azure AI Account Owner.
- Wiens rechten? *"this user is allowed to"* → **on-behalf-of** (identity passthrough). *"this specific agent"* → **agent identity** + RBAC. API kent alleen een key → **key in project connection**. Beide eerste zijn Entra ID: beslis op wíens rechten.
- CLI = zin: `az cognitiveservices account [keys|deployment] <werkwoord> --details`. Geen `account` erin of verzonnen werkwoord (`regenerate-key`, `az openai`) = nep. Rollen altijd `az role assignment create`. azd: `provision` = infra, `deploy` = code, `up` = beide.
- Sleutelrotatie zonder downtime: app naar key2 → key1 regenereren → app naar nieuwe key1 → key2 regenereren. Nooit de sleutel regenereren die de app gebruikt.
- Content filter-drempel = vanaf welk niveau geblokkeerd: **Low = strengst**, High = soepelst, Off = goedkeuring nodig. "Safe" is geen drempel.
- Evaluators: **Retrieval** = opgehaalde chunks · **Relevance** = antwoord beantwoordt vraag · **Groundedness** = antwoord vs chunks · **Similarity** = vs referentieantwoord · **Tool call accuracy** = juiste tool + parameters.
- Activity Log = wie wijzigde een instelling (control plane). Diagnostic settings = requests naar het model (data plane). 429-alarm zonder logs → metric alert.
- HTTP 429 = te veel verzoeken (boven quota: TPM/RPM). Af en toe → **retry met exponential backoff**.
- Per request zien welke stappen, tools, tokens en latency → **tracing + Application Insights** (OpenTelemetry).
- Jailbreak / "ignore instructions" → **Prompt Shields** (direct én indirect, ook tekst in afbeeldingen).
- Verzint het model iets t.o.v. de bronnen? → **groundedness**.
- Auteursrechtelijke tekst/code in de output → **protected material detection**.
- Eenvoudige taak, veel volume, te duur → **small language model** (Phi, mini/nano).
- Data mag de EU niet uit → **Data Zone** (Standard of Batch). Global = overal ter wereld. Grote nachtjob, 24 uur ok, goedkoopst, eigen quota → **Batch**.
- Azure AI-container: verplicht **E-B-A**: `Eula=accept`, `Billing=<endpoint>`, `ApiKey=<key>`. Tekst blijft lokaal, alleen verbruik gaat naar Azure. Zonder internet → **disconnected containers** (aanvragen + commitment plan).

## Generatieve AI & agents
- Eigen of actuele data + verzonnen antwoorden → **RAG**. Fine-tuning = stijl/format/gedrag, niet feiten.
- Consistente output → **temperature 0** (of `seed`). Gegarandeerd format → **structured outputs + JSON schema**.
- Pas temperature **óf** top_p aan, niet allebei.
- Agent-tools: vaste documenten → **file search** · veel eigen content → **Azure AI Search** · live data/acties in eigen systeem → **OpenAPI/function tool** · openbaar internet → **Bing grounding**.
- Een prompt is een verzoek, code is een garantie. Geld of risico → **approval flow (human-in-the-loop)**.
- Structured outputs `strict: true`: alle velden in `required`, `additionalProperties: false`; optioneel = `"type": ["string","null"]`. JSON mode (`json_object`) = alleen geldige JSON, géén schema-garantie.
- Wekelijks veranderende feiten → RAG. Stijl/format, few-shot al geprobeerd + duizenden voorbeelden → fine-tuning. Simpel + veel volume + te duur → klein model. Complexe meerstaps-logica → reasoning model.
- Agent Service **standard setup** = eigen Cosmos DB (gesprekken), Storage (bestanden), AI Search (vector stores); + private netwerk als dat geëist wordt. CMK op basic setup ≠ data in eigen subscription.
- Orchestration: vaste volgorde → sequential · specialist neemt gesprek over → handoff · tegelijk + samenvoegen → concurrent · manager maakt/past plan aan → **Magentic** · agents discussiëren, manager kiest spreker → group chat · model verbetert eigen antwoord → reflection.
- MCP-tool met goedkeuring: `require_approval="always"` → output bevat `mcp_approval_request` → stuur `McpApprovalResponse` terug met `previous_response_id=response.id` (zelfde keten). `tool_choice="required"` dwingt alleen een toolaanroep af.
- Sleutel van een tool niet in code of agent definition → **`project_connection_id`** (connection in het Foundry-project). Key Vault-secret in code ophalen = sleutel in code.

## Computer vision
- Nieuw beeld → **generate**. Deel van een beeld veranderen → **edit + mask (inpainting)**. Masker = PNG met alfakanaal, zelfde afmetingen; **transparant = hier mag het model tekenen**.
- Beeld of video begrijpen en gestructureerde velden eruit halen → **multimodaal model** of **Content Understanding**.

## Tekst en spraak
- Sentiment per onderdeel/aspect van een tekst → **opinion mining** (aspect-based sentiment, `show_opinion_mining=True`). Key phrases + document-sentiment koppelt aspect en sentiment níet.
- PII in een chat/transcript met rollen en beurten → **conversational PII**. PII in gewone tekst → PII detection. Categories filter = alleen bepaalde soorten redigeren.
- Intent + waarden uit korte opdrachten → **CLU** (utterances, intents, entities, train + deploy). Alleen categorie → custom text classification. Alleen waarden → custom NER. FAQ-antwoorden → custom question answering.
- Eén endpoint, de **service** routeert tussen intents (CLU) en FAQ (question answering) → **orchestration workflow**.
- Chat/gesprek samenvatten met probleem en oplossing apart → **conversation summarization** (aspects `issue`, `resolution`), niet document summarization.
- Hele bestanden vertalen + opmaak behouden → **document translation** (Blob source + target container). Managed identity van Translator heeft **Storage Blob Data Contributor** nodig (Reader kan niet schrijven). Text translation API doet geen bestanden en geen Blob.
- **Glossary** = bestand (`.tsv`/`.csv`/`.xlf`) met vaste termvertalingen, per targettaal meegegeven bij document translation. Niet vertalen = term op zichzelf zetten. Vaste termen nooit vertalen → **glossary** (document) of **dynamic dictionary** (text API). Custom Translator alleen mét trainingsdata (parallelle zinnen).
- Uitspraak, pauze, tempo sturen → **SSML**: `say-as`, `break`, `prosody`. Andere stem verandert dat niet.
- SSML per probleem: letter voor letter → `say-as interpret-as="characters"` · afkorting voluit → `sub alias` (zonder fonetiek) · uitspraak via fonetisch alfabet → `phoneme` · stilte → `break time` · sneller/langzamer → `prosody rate` · emotie/stijl → `mstts:express-as`.
- Persoonsgegevens verwijderen → **PII detection + redaction** (Azure Language).
- Vaktermen verkeerd verstaan → **custom speech** of **phrase list**. Andere stem → **custom neural voice** (TTS).
- STT = spraak → tekst. TTS = tekst → spraak.
- Label op een stukje tekst → **custom NER**. Label op het hele document → **custom text classification** (*exactly one* = single label, *one or more* = multi label). Company vs river + Wikipedia-link → **entity linking**.
- Default PII-categorieën bevatten ook **Organization**: bedrijfsnamen zichtbaar houden → categories filter.
- Spraak live vertalen in één object → **`TranslationRecognizer`** + `SpeechTranslationConfig`. Bron = volledige locale (`nl-NL`), doel = taalcode (`"de"`), resultaat = `result.translations["de"]`. `ConversationTranscriber` = wie spreekt (diarization), geen vertaling.

## Informatie-extractie
- Exacte codes én betekenis → **hybrid search**. Bovenop: **semantic ranker**.
- RRF = twee ranglijsten samenvoegen (formule). Semantic ranker = herordenen met een taalmodel.
- `query_type`: `simple` = trefwoorden (standaard) · `full` = Lucene (fuzzy `~1`, regex, `veld:term`, boost) · `semantic` = daarna herordenen met taalmodel (kost extra). **Hybrid** is geen query_type: `search_text` + `vector_queries` samen.
- Vectorizer op de index → `VectorizableTextQuery(text=...)`. Geen vectorizer / app maakt de vector zelf → `VectorizedQuery(vector=...)`. `dimensions` = exact de output van het embeddingmodel (3-small/ada-002 = 1536, 3-large = 3072).
- Index-attributen: sorteren maar niet tonen → `sortable: true, retrievable: false`.
- Complexe meerdelige vraag over meerdere bronnen → **knowledge base met agentic retrieval** (Foundry IQ, agent via MCP-endpoint). Korte zoekterm, veel volume, laagste latency → gewone hybrid (+ semantic).
- Chunks op koppen/secties, tabellen heel → **Document Layout skill** (Markdown). Vectoren in de pipeline zonder code → **Azure OpenAI Embedding skill** (integrated vectorization).
- Container: de **container** krijgt `Billing` + `ApiKey`; je **app** praat met de container (`SpeechConfig(host="ws://localhost:5000")`), niet met de cloud.
- OCR = alleen tekst. Velden uit documenten met wisselende layouts → **Content Understanding** (of Document Intelligence prebuilt invoice).
