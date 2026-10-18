modellen = ["gpt-4o", "claude", "llama"]

for model in modellen:
    print(model)

berichten = [
    {"role": "user", "content": "Hoi"},
    {"role": "assistent", "content": "Hallo!"}
]

for bericht in berichten:
    print(bericht["content"])

for bericht in berichten :
    if bericht["role"] == "assistent":
        print(bericht["content"])  

klanten = [
    {"naam": "Sanne", "actief": True},
    {"naam": "Pieter", "actief": False},
    {"naam": "Fatima", "actief": True},
        ] 

for klant in klanten :
    if klant["actief"]:
        print(klant["naam"])