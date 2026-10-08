# Logboek

Nieuwste sessie bovenaan. Per sessie: wat gedaan, wat lastig was, volgende stap.

---

## 8 oktober 2026: Oefeningen dag 5 (lists afgerond)

- **Controlevraag slicing:** 1/3. `landen[2:5]` gaf 2 in plaats van 3 elementen ❌, bij `landen[-2:]` gedacht dat slicing rondloopt naar het begin ❌, de lastige `landen[:1][0][-1]` → `d` ✅. Daarna `[1:4]` met stappen goed ✅. Begrip is er, de fouten komen uit haast.
- **Oefeningen** in `oefeningen/dag-05/oefeningen.py`: level 1, gebundeld tot 3 blokken. Level 2 overgeslagen (rekenwerk dat loops nodig heeft).
  - Fouten onderweg: `[1]` voor het eerste element, `[3] =` (vervangen) in plaats van `insert`, `print(lijst.sort)` zonder `()`, `[0:2]` voor 3 elementen, `[-1:-3]` en `[-2:0]` → lege list, `remove(1)` op plek in plaats van naam (ValueError). Twee keer vergeten op te slaan.
  - Alles uiteindelijk zelf opgelost na een hint. Eindresultaat draait en klopt. ✅
  - Spatie in `" Deepseek"` laten staan. Wel gezien wat het doet: hij komt bij het sorteren vooraan.
  - Blok 3 ingekort (14 en 16 geschrapt), op verzoek wegens energie. `pop()` nog niet zelf gebruikt.
  - Comments door de coach toegevoegd op verzoek. De code zelf is niet aangepast.
- **Patroon:** haast. Bijna elke fout was slordigheid, geen onbegrip. Zelf gezegd: "ik heb zo'n haast, ik wil echt naar een hoger niveau." Afspraak: langzaam is soepel, soepel is snel.
- **Geleerd:** functie uitvoeren = `()`, `remove` (naam) tegenover `pop` (plek), vervangen tegenover invoegen, traceback lezen bij een ValueError.
- **Tuples en sets (dag 6–7), toch nog vandaag gedaan,** op eigen initiatief ("ik wil op schema zijn"). Korte uitleg, daarna 6 prints voorspeld in `oefeningen/dag-06/tuples_sets.py`: 6/6 goed (bij één print eerst overgeslagen, op de vraag meteen `5`). Stappen stonden er dit keer bij. ✅
  - Zelf een regel geschreven die een tuple probeert te veranderen. Die gaf de verwachte `TypeError`, in één keer goed. ✅
  - Bewust licht gehouden: voor het examen zijn tuples en sets het minst belangrijk.
- **Coach:** na de haast van vanochtend was dit rustig en precies. Zo wil ik het morgen bij dictionaries zien.
- **Volgende stap (9 okt):** opwarmer `pop(0)`/`pop()`, met stappen. Daarna dictionaries (dag 8). Weer op schema.

---

## 7 oktober 2026: Herhaling geketend indexeren + start dag 5

- **`bedrijven[2][0]`:** `A`, met de juiste uitleg (eerst de list, dan de string). ✅ Gisteren fout, vandaag zonder hulp goed.
- **`bedrijven[-1][-1]`:** antwoord `B` ❌. Juist: `M`. `[-1]` is het laatste element zelf, er bestaat geen `-0`.
- **`bedrijven[-2][-1]`:** `n` ✅, maar zonder de twee stappen uit te schrijven (de tweede keer).
- **Afspraak:** vanaf nu bij elke codevraag de stappen opschrijven. Een antwoord zonder stappen telt niet.
- **Bestand verplaatst:** eerst per ongeluk naar `oefeningen_dag5\` (underscore in plaats van `\`), daarna rechtgezet naar `oefeningen/dag-05/learn.py`. Naam `learn.py` bewust zo gelaten.
- **Les dag 5 doorgewerkt** in `oefeningen/dag-05/list.py`. Werkwijze aangepast: coach geeft korte uitleg, de les is naslag (scheelt tijd). Per onderdeel eerst voorspellen, dan zelf typen en ▶️.
  - Unpacking: goed, maar eerst "de rest" als antwoord. Na doorvragen: `rest` is een list ✅
  - Slicing: 2/3. `[0:2]` gaf 3 elementen ❌ (eind doet niet mee), terwijl het bij `[-3:-1]` wél goed ging. Controle `[1:3]` goed ✅
  - Modifying, `in`, `append`/`insert`/`remove`/`pop`: goed. `in` eerst gezien als "zoeken en tonen" in plaats van `True`/`False` ❌, na uitleg goed.
  - Copy/join/count/index/sort/reverse: goed, maar eerst beschreven *wat* het doet in plaats van *de uitkomst*. Na doorvragen alles concreet goed ✅
  - De laatste twee blokken eerst niet getypt (alleen voorspeld), daarna wel. Alle uitkomsten kloppen met de voorspellingen.
- **Patroon:** begrippen gaan snel, precisie niet. Vage antwoorden, fouten van één plek, en stappen overslaan (3× vandaag). Blijft het aandachtspunt.
- **Doel aangescherpt:** geen apps bouwen zonder AI, wel sterke fundamentals voor samenwerking met AI (lezen, beoordelen, fouten zien, sturen). Zelf typen blijft de regel tijdens het leren. Na het examen komen er review-oefeningen bij ("vind de fout in deze AI-code").
- **Volgende stap (8 okt):** oefeningen dag 5 (level 1–2) in `oefeningen/dag-05/`, daarna tuples en sets snel lezen (dag 6–7).

---

## 6 oktober 2026: Mini-oefening negatieve index (10 min)

- **Gedaan:** voorspellen wat `bedrijven[0]`, `[-1]`, `[-2]`, `[-5]` en `[-6]` geven bij een list van 5 bedrijven.
- **Uitslag:** 0/5. Er kwamen **letters** uit als antwoord in plaats van hele elementen.
- **Kern van het misverstand:** list en string door elkaar gehaald. Een index op een **list** geeft het hele element (`'IBM'`), een index op een **string** geeft een letter. Letter uit een element: `bedrijven[0][0]` → `'M'`.
- **Ook gemist:** `[-6]` geeft een `IndexError` (buiten de list). Typfout `Äpple"` zou een `SyntaxError` geven.
- **Coach:** goed dat dit nu bovenkomt en niet op het examen. Dit is precies het gat uit de niveautest (vraag 2).
- **Daarna zelf getypt** in `oefeningen/learn.py`. Eerst zonder `print()`, waardoor er niets zichtbaar was. Uitgelegd: de REPL toont uitkomsten automatisch, een bestand alleen met `print()`. Daarna alle vier de prints zelf toegevoegd: uitkomst **Microsoft, IBM, Amazon, Microsoft** en daarna de verwachte `IndexError`. ✅
- **Geleerd:** het verschil tussen de REPL en een bestand, een traceback van onder naar boven lezen, en dat Python na een fout stopt.
- **Coach:** de bedoelde error als mislukking gezien ("wat ben ik hier slecht in"). Afspraak: een terminal lees je van boven naar beneden, eerst kijken wat wél werkte. Nieuw zijn is niet slecht zijn.
- **Zelf ingezien:** "ik telde alsof het een string was, maar het is een list, dus je telt per element." ✅
- **Controlevraag `bedrijven[2][0]`:** antwoord "apple microsoft" ❌. Juist: `'A'`. De tweede index werkt op de **uitkomst** van de eerste (`"Apple"[0]`), niet opnieuw op de list. Dit geketend indexeren is hetzelfde patroon als `klant["adressen"][1]` en geneste API-data, en dus examenstof.
- **Morgen:** start met `bedrijven[2][0]` opnieuw (verwacht: `A` zonder twijfel). Daarna `learn.py` verplaatsen naar `oefeningen/dag-05/negatieve_index.py` en dan dag 5.

---

## 6 oktober 2026: Examendatum en planning

- **Besluit:** AI-103-examen staat op **7 november 2026**. Het Python-deel is daarop gericht: ~18 uur, 1 uur per dag van 7 tot en met 24 oktober (planning in `VOORTGANG.md`).
- **Totaal tijdsbudget:** ~2,5 uur per dag tot het examen (Python + AI-103).
- **Coach:** 80 uur in 32 dagen kan, maar alleen zonder gemiste dagen. Controlemoment op 28 oktober.

---

## 6 oktober 2026: Dag 1–4 gelezen en gecontroleerd

- **Gedaan:** dag 1–4 gelezen. Daarna controle met drie vragen uit het hoofd.
- **Uitslag:**
  - Strings en index: 2/3. `taal[0]` en `len()` goed, `taal[-1]` gemist (antwoord: `n`, een negatieve index telt vanaf het einde).
  - Operators: 1/3. `/` goed, `//` (delen en naar beneden afronden → `3`) en `%` (rest → `1`) niet geweten.
  - Datatypes: 5/5, zonder twijfel.
- **Coach:** bij de operators "durf ik niet" gezegd in plaats van te gokken. Afspraak: voortaan altijd gokken en erbij zeggen dat het een gok is. Logboekregel na het lezen eerst niet geschreven. Vanaf nu houdt de coach het logboek bij.
- **Oordeel:** voldoende voor dag 5. Negatieve index en `//`/`%` komen terug bij dag 5 en 9–10 en moeten er dan zitten.
- **Volgende stap:** dag 5 (Lists), alle oefeningen zelf typen in `oefeningen/dag-05/`.

---

## 6 oktober 2026: Niveautest en start

- **Gedaan:** niveautest (6 vragen), zie [`niveautests/2026-10-06.md`](niveautests/2026-10-06.md). Map en traject opgezet.
- **Lastig:** zelf code schrijven met lists en dictionaries (vraag 2 en 5).
- **Goed:** code lezen en begrippen rond API's.
- **Volgende stap:** dag 1–4 snel doorlezen, daarna dag 5 (Lists) met alle oefeningen zelf getypt.
