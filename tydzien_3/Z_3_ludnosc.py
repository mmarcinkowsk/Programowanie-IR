import json

plik = open("ścieżka/do/pliku/ludnosc.json")
dane = json.load(plik)
plik.close()

# print(dane)
for rok in dane.keys():
    calkowita_ludnosc = 0
    calkowita_powierzchnia = 0
    for wojewodzwto in dane[rok].keys():
        calkowita_ludnosc += dane[rok][wojewodzwto]["ludność"]
        calkowita_powierzchnia += dane[rok][wojewodzwto]["powierzchnia km2"]
    dane[rok]["Polska"] = {"ludność": calkowita_ludnosc, "powierzchnia km2":calkowita_powierzchnia}

for rok in dane.keys():
    for wojewodzwto in dane[rok].keys():
       dane[rok][wojewodzwto]["gęstość zaludnienia"] = dane[rok][wojewodzwto]["ludność"]/dane[rok][wojewodzwto]["powierzchnia km2"]

print(dane["2020"]["Polska"])
# W tym miejscu skończyliśmy