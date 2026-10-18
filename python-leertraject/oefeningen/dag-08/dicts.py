# Dag 8: Dictionaries (8 en 13 oktober 2026)
# Zelf getypt. Comments en opmaak door de coach.

# ============================================================
# Deel 1: uitlezen
# ============================================================

auto = {
    "merk": "Tesla",
    "jaar": 2022,
    "kleuren": ["wit", "zwart"]
}

print(auto["merk"])          # value ophalen met de key
print(auto["kleuren"][1])    # key → list → index 1 = TWEEDE element → 'zwart'
print(auto.get("prijs"))     # .get() bij een key die niet bestaat → None (geen KeyError)
print("Tesla" in auto)       # `in` zoekt alleen bij de KEYS, niet bij de values → False
auto["jaar"] = 2024          # bestaande key → value overschrijven
print(auto["jaar"])

# ============================================================
# Deel 2: aanpassen
# ============================================================

auto["prijs"] = 4500         # nieuwe key → toevoegen
print(len(auto))             # len() telt het aantal keys
del auto["kleuren"]          # del = key + value verwijderen
print(auto)
print(list(auto.keys()))     # alleen de keys. `auto` zelf is GEEN key, maar de dict
print(auto.get("prijs"))

# ============================================================
# Deel 3: geneste dicts, zo ziet een AI-API-response eruit
# Na een list → getal [0], na een dict → key ["..."]
# ============================================================

response = {
    "model": "gpt-4o",
    "choices": [
        {"index": 0, "message": {"role": "assistant", "content": "Hallo Arrya!"}}
    ],
    "usage": {"total_tokens": 42}
}

print(response["usage"]["total_tokens"])                # dict → dict → 42
print(response["choices"][0]["message"]["content"])     # dict → list → dict → dict → 'Hallo Arrya!'

# Zelf geschreven:
print(response["choices"][0]["message"]["role"])        # → 'assistant'
print(response["model"])                                # → 'gpt-4o'


dog = {"name": "Jeff", "color": "Brown" , "breed": "Caucasian" , "age": 4 }

dog["legs"] = 4 

print(dog)