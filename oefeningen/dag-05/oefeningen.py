# Dag 5: Lists - oefeningen (8 oktober 2026)
# Zelf getypt. Comments toegevoegd door de coach.

# ============================================================
# Blok 1: aanmaken en uitlezen
# ============================================================

# 1. List maken
item_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 2. List printen
print(item_companies)

# 3. Aantal elementen: len()
print(len(item_companies))

# 4. Eerste, laatste en middelste element
#    Het eerste element is ALTIJD index 0 (niet 1!)
print(item_companies[0])
print(item_companies[-1])
print(item_companies[3])    # midden van 7 = index 3 (3 links, 3 rechts)

# 5. Vervangen: index + =  (het oude element verdwijnt)
item_companies[0] = "OpenAI"

# 6. Achteraan toevoegen: append()
item_companies.append("Antropic")

# 7. Invoegen op een plek: insert(plek, waarde)  (de rest schuift op, er verdwijnt niets)
#    Let op: " Deepseek" heeft een spatie vooraan, dus het is een andere string dan "Deepseek"
item_companies.insert(3," Deepseek")

print(item_companies)

# ============================================================
# Blok 2: zoeken, sorteren, slicen
# ============================================================

# 8. Zit het erin? `in` geeft True of False
print("Google" in item_companies)

# 9. Sorteren: sort() verandert de list zelf, dus print daarna apart
#    Zonder () voer je de functie niet uit: .sort  = de knop, .sort() = op de knop drukken
item_companies.sort()
print(item_companies)

# 10. Omdraaien: reverse() verandert ook de list zelf
item_companies.reverse()
print(item_companies)

# 11. Eerste 3: [start:eind], het eind doet NIET mee. Telling: 3 - 0 = 3
print(item_companies[0:3])

# 12. Laatste 3: negatieve start, eind leeg = door tot het einde
print(item_companies[-3:])

# ============================================================
# Blok 3: verwijderen en samenvoegen
# ============================================================

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

# 13. Eerste verwijderen
#     remove("x") werkt op NAAM, pop(i) werkt op PLEK. Hier gedaan met remove.
front_end.remove("HTML")
print(front_end)

# 15. Laatste verwijderen (kan ook met back_end.pop())
back_end.remove("MongoDB")

# 17. Lists samenvoegen met +  (geeft een nieuwe list)
full_stack = front_end + back_end
print(full_stack)
