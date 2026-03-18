#!/usr/bin/python3

import json

import matplotlib.pyplot as plt

plik = open("tydzien_3/ludnosc.json")
dane = json.load(plik)
plik.close()


for rok in dane.keys():
    calkowita_ludnosc = 0
    calkowita_powierzchnia = 0
    for wojewodzwto in dane[rok].keys():
        calkowita_ludnosc += dane[rok][wojewodzwto]["ludność"]
        calkowita_powierzchnia += dane[rok][wojewodzwto]["powierzchnia km2"]
    dane[rok]["Polska"] = {"ludność": calkowita_ludnosc, # Dodaję "województwo" "Polska".
                           "powierzchnia km2":calkowita_powierzchnia}

for rok in dane.keys(): # Obliczam gęstość zaludnienia w każdym roku dla każdego województwa.
    for wojewodzwto in dane[rok].keys():
       dane[rok][wojewodzwto]["gęstość zaludnienia"] = dane[rok][wojewodzwto]["ludność"]/dane[rok][wojewodzwto]["powierzchnia km2"]

print(dane["2020"]["Polska"])

print("Dostępne obszary:")
for wojewodzwto in dane["2020"].keys():
    print(wojewodzwto)

wybrane_wojewodzwtwo = input("Wybierz obszar:")

statystyki = ["ludność", "powierzchnia km2", "gęstość zaludnienia"]

indeks_statystyki = int(input("Wybierz statystykę: 0-ludność, 1-powierzchnia, 2-gęstość zaludnienia:"))

wybrana_statystyka = statystyki[indeks_statystyki]

lata = dane.keys()
punkty_do_wyswietlenia = [dane[rok][wybrane_wojewodzwtwo][wybrana_statystyka] for rok in lata]

fig, ax = plt.subplots()

ax.plot(lata, punkty_do_wyswietlenia)

plt.show()
