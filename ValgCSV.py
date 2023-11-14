#1 topp fem høyeste og laveste for hver kommune
"""
with open("valg2023.csv", encoding='utf-8') as file:
    lines = file.readlines()

# Fjerner overskrift og eventuelle tomme linjer
lines = [line.strip() for line in lines if line.strip()]

# Oppretter ordbøker for å lagre data
parti_oppslutning = {}  # Struktur: {kommune: {parti: prosentandel}}

# Behandler hver linje i filen
for line in lines[1:]:  # Starter fra andre linje for å hoppe over overskriften
    elements = line.split(';')
    kommune = elements[3]
    parti = elements[7]
    oppslutning = float(elements[8].replace(',', '.'))  # Konverterer til flyttall

    # Oppdaterer ordboken med data
    if kommune not in parti_oppslutning:
        parti_oppslutning[kommune] = {}
    parti_oppslutning[kommune][parti] = oppslutning

# Finner topp fem partier med høyest og lavest prosentandel i hver kommune
top_5_highest = {}
top_5_lowest = {}

for kommune in parti_oppslutning:
    sorted_parties = sorted(parti_oppslutning[kommune].items(), key=lambda x: x[1], reverse=True)
    top_5_highest[kommune] = sorted_parties[:5]
    top_5_lowest[kommune] = sorted_parties[-5:]

# Viser resultatene
print("Topp fem partier med høyest prosentandel oppslutning i hver kommune:")
for kommune in top_5_highest:
    print(kommune, top_5_highest[kommune])

print("\nTopp fem partier med lavest prosentandel oppslutning i hver kommune:")
for kommune in top_5_lowest:
    print(kommune, top_5_lowest[kommune])
"""
#4 Finn antall kommunestyrerepresentanter for Høyre, Venstre og AP i hvert fylke
"""
# Åpner CSV-filen
with open("valg2023.csv", encoding='utf-8') as file:
    lines = file.readlines()

# Fjerner overskrift og eventuelle tomme linjer
lines = [line.strip() for line in lines if line.strip()]

# Oppretter ordbøker for å lagre data
representanter = {}  # Struktur: {fylke: {parti: antall representanter}}

# Behandler hver linje i filen
for line in lines[1:]:  # Starter fra andre linje for å hoppe over overskriften
    elements = line.split(';')
    fylke = elements[1]
    parti = elements[7]
    mandater = int(elements[15])  # Antall mandater

    # Sjekker om partiet er Høyre, Venstre eller AP
    if parti in ['Høyre', 'Venstre', 'Arbeiderpartiet']:
        if fylke not in representanter:
            representanter[fylke] = {}
        if parti not in representanter[fylke]:
            representanter[fylke][parti] = 0
        representanter[fylke][parti] += mandater

# Viser resultatene
for fylke in representanter:
    print(f"fylke: {fylke}")
    for parti, antall in representanter[fylke].items():
        print(f"  {parti}: {antall} representanter")
    print()  # Tom linje for bedre lesbarhet
"""
#5 Finn hvilket parti som er valgvinneren i de fem kommunene med kortest navn (færrest antall bokstaver) og i de fem kommunene med lengst navn (flest antall bokstaver)
# Åpner CSV-filen

# Åpner CSV-filen
with open("valg2023.csv", encoding='utf-8') as file:
    lines = file.readlines()

# Fjerner overskrift og eventuelle tomme linjer
lines = [line.strip() for line in lines if line.strip()]

# Oppretter en ordbok for å lagre data
kommune_data = {}  # Struktur: {kommunenavn: {parti: prosentandel}}

# Behandler hver linje i filen
for line in lines[1:]:  # Starter fra andre linje for å hoppe over overskriften
    elements = line.split(';')
    kommune = elements[3]
    parti = elements[7]
    oppslutning = float(elements[8].replace(',', '.'))  # Konverterer til flyttall

    # Oppdaterer ordboken med data
    if kommune not in kommune_data:
        kommune_data[kommune] = {}
    if parti not in kommune_data[kommune] or oppslutning > kommune_data[kommune][parti]:
        kommune_data[kommune][parti] = oppslutning

# Sorterer kommunene basert på navnelengde
kommuner_sortert = sorted(kommune_data.keys(), key=len)

# Velger de fem kommunene med kortest og lengst navn
korteste_kommuner = kommuner_sortert[:5]
lengste_kommuner = kommuner_sortert[-5:]

# Finner og skriver ut valgvinneren i de utvalgte kommunene
print("Valgvinnere i kommunene med kortest navn:")
for kommune in korteste_kommuner:
    vinner = max(kommune_data[kommune], key=kommune_data[kommune].get)
    print(f"{kommune}: {vinner}")

print("\nValgvinnere i kommunene med lengst navn:")
for kommune in lengste_kommuner:
    vinner = max(kommune_data[kommune], key=kommune_data[kommune].get)
    print(f"{kommune}: {vinner}")


