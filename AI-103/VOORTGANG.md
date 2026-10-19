# AI-103: voortgang

**Examen:** AI-103 *Developing AI Apps and Agents on Azure*, **vrijdag 7 november 2026**. Slagen = 700/1000.
**Huidige stand:** officiële practice assessment 19 okt: **63%** (doel Microsoft: 80%). Zwakst: tekstanalyse (~13%) en GenAI & agents (~59%).
**Volgende stap:** ma 20 okt: tekstanalyse (Azure Language + Translator).

## Uitslagen

| Datum | Test | Score | Plan & manage | GenAI & agents | Vision | Tekst | Info-extractie |
|---|---|---|---|---|---|---|---|
| 17 okt | Coachtest (15 vragen) | 13/15 | 3/5 | 4/4 | 2/2 | 2/2 | 2/2 |
| 19 okt | **Officiële practice assessment** | **63%** | ~75% | ~59% | ~82% | ~13% | ~71% |

Percentages per domein zijn afgelezen uit de staafgrafiek (±5%). Zie [`niveautests/2026-10-19-practice-assessment.md`](niveautests/2026-10-19-practice-assessment.md).

## Planning per dag

**Herschikt op 19 okt** na de practice assessment. Volgorde op verwacht puntenverlies (gewicht × wat je mist): eerst **tekst & spraak** (bijna alles gemist), dan **GenAI & agents** (zwaarste domein, 59%), daarna Plan & manage, info-extractie en vision kort.

Elke sessie: begin met 10 min [`notities/ai103-examenregels.md`](notities/ai103-examenregels.md), eindig met 5 oefenvragen over het onderwerp van die dag. Nieuwe regels aanvullen.

| Datum | Onderwerp | Tijd | Status |
|---|---|---|---|
| vr 17 okt | Niveautest coach (15 vragen) | – | ✅ 13/15 |
| za 18 okt | Officiële practice assessment | – | ❌ verschoven naar 19 okt |
| zo 19 okt | **Officiële practice assessment** + alle foute vragen nalezen (uitleg + Learn-links) | 1,5 u | ✅ 63% |
| ma 20 okt | Tekst 1: Azure Language (PII, sentiment, entiteiten, samenvatten), Translator, extractie met LLM's + structured JSON | 1,5 u | ⬜ |
| di 21 okt | Tekst 2 / spraak: STT/TTS, custom speech, speech translation, spraak in agents, audio-input | 1,5 u | ⬜ |
| wo 22 okt | GenAI 1: Foundry SDK: app koppelen aan project, modellen aanroepen, parameters, structured outputs (code lezen) | 1,5 u | ⬜ |
| do 23 okt | GenAI 2: RAG end-to-end (AI Search, chunking, embeddings, hybrid, semantic ranker) | 1,5 u | ⬜ |
| vr 24 okt | GenAI 3: Agents (Agent Service, tools, memory, threads) | 1,5 u | ⬜ |
| za 25 okt | GenAI 4: multi-agent, approval flows, workflows, reflectie/self-critique | 2,5 u | ⬜ |
| zo 26 okt | GenAI 5: evalueren (fabrications, relevance, safety), tracing, prompt engineering | 2,5 u | ⬜ |
| ma 27 okt | Plan & manage compact: deploymenttypes/quota, security (managed identity, RBAC, private endpoints), content filters | 2,5 u | ⬜ |
| **di 28 okt** | **Controlemoment: practice assessment opnieuw.** Doel ≥ 70%. Onder de 60% → examen verzetten | 2,5 u | ⬜ |
| wo 29 okt | Gaten uit 28 okt (zwakste domein eerst) | 2,5 u | ⬜ |
| do 30 okt | Info-extractie: Content Understanding documenten, OCR, layout, indexers en skills, RAG-ingestie | 2,5 u | ⬜ |
| vr 31 okt | Tekst & spraak herhalen + 30 oefenvragen alleen over tekst | 2,5 u | ⬜ |
| za 1 nov | Vision: beeld/video genereren en bewerken, Content Understanding beeld/video, visuele RAI | 2,5 u | ⬜ |
| zo 2 nov | Plan & manage: monitoring, responsible AI, modelkeuze, CI/CD | 2,5 u | ⬜ |
| ma 3 nov | Gaten + ExamCert (50 vragen) | 2,5 u | ⬜ |
| di 4 nov | Proefexamen: practice assessment + Tutorials Dojo-sampler + A Guide to Cloud | 2,5 u | ⬜ |
| wo 5 nov | Laatste gaten | 2,5 u | ⬜ |
| do 6 nov | Licht: alleen examenregels herhalen, vroeg slapen | 1 u | ⬜ |
| **vr 7 nov** | **Examen** | | ⬜ |

**Grootste risico:** codevragen met de Python SDK. Daarom blijft Python tot 24 okt gericht op Foundry-code lezen.
