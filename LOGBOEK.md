# Logboek

Nieuwste sessie bovenaan. Per sessie: wat gedaan, wat lastig was, volgende stap.

---

## 6 oktober 2026: Mini-oefening negatieve index (10 min)

- **Gedaan:** voorspellen wat `bedrijven[0]`, `[-1]`, `[-2]`, `[-5]` en `[-6]` geven bij een list van 5 bedrijven.
- **Uitslag:** 0/5. Er kwamen **letters** uit als antwoord in plaats van hele elementen.
- **Kern van het misverstand:** list en string door elkaar gehaald. Een index op een **list** geeft het hele element (`'IBM'`), een index op een **string** geeft een letter. Letter uit een element: `bedrijven[0][0]` → `'M'`.
- **Ook gemist:** `[-6]` geeft een `IndexError` (buiten de list). Typfout `Äpple"` zou een `SyntaxError` geven.
- **Coach:** goed dat dit nu bovenkomt en niet op het examen. Dit is precies het gat uit de niveautest (vraag 2). Morgen eerst deze oefening opnieuw, echt in de REPL getypt.

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
