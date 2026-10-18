# AI-103 examenregels

Vuistregels uit de niveautest van 17 oktober 2026. Elke dag 10 minuten doorlezen. Vul aan met wat je leert.

## Werkwijze op het examen
- Nooit een vraag open laten. Een gok heeft 25% kans, een open vraag 0%.
- Streep alleen weg wat je **zeker** weet dat fout is, niet wat je niet kent.
- Zoek het échte argument in de vraag: *actueel*, *keyless*, *minimal effort*, *reliably*, *guaranteed*.

## Plan & manage
- "No keys / keyless" → **managed identity + RBAC-rol**. Key Vault is nog steeds een sleutel (valkuil).
- Hoog en stabiel verkeer + garantie → **provisioned throughput (PTU)**. Wisselend verkeer → **Standard**.
- HTTP 429 = te veel verzoeken (boven quota: TPM/RPM). Af en toe → **retry met exponential backoff**.
- Per request zien welke stappen, tools, tokens en latency → **tracing + Application Insights** (OpenTelemetry).
- Jailbreak / "ignore instructions" → **Prompt Shields** (direct én indirect, ook tekst in afbeeldingen).
- Verzint het model iets t.o.v. de bronnen? → **groundedness**.
- Auteursrechtelijke tekst/code in de output → **protected material detection**.
- Eenvoudige taak, veel volume, te duur → **small language model** (Phi, mini/nano).

## Generatieve AI & agents
- Eigen of actuele data + verzonnen antwoorden → **RAG**. Fine-tuning = stijl/format/gedrag, niet feiten.
- Consistente output → **temperature 0** (of `seed`). Gegarandeerd format → **structured outputs + JSON schema**.
- Pas temperature **óf** top_p aan, niet allebei.
- Agent-tools: vaste documenten → **file search** · veel eigen content → **Azure AI Search** · live data/acties in eigen systeem → **OpenAPI/function tool** · openbaar internet → **Bing grounding**.
- Een prompt is een verzoek, code is een garantie. Geld of risico → **approval flow (human-in-the-loop)**.

## Computer vision
- Nieuw beeld → **generate**. Deel van een beeld veranderen → **edit + mask (inpainting)**.
- Beeld of video begrijpen en gestructureerde velden eruit halen → **multimodaal model** of **Content Understanding**.

## Tekst en spraak
- Persoonsgegevens verwijderen → **PII detection + redaction** (Azure Language).
- Vaktermen verkeerd verstaan → **custom speech** of **phrase list**. Andere stem → **custom neural voice** (TTS).
- STT = spraak → tekst. TTS = tekst → spraak.

## Informatie-extractie
- Exacte codes én betekenis → **hybrid search**. Bovenop: **semantic ranker**.
- RRF = twee ranglijsten samenvoegen (formule). Semantic ranker = herordenen met een taalmodel.
- OCR = alleen tekst. Velden uit documenten met wisselende layouts → **Content Understanding** (of Document Intelligence prebuilt invoice).
