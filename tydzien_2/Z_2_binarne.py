#!/usr/bin/python3

from Z_1_bobelkowe import sortowanie_bobelkowe

def wyszukiwanie_binarne(lista, x):
    lista = sortowanie_bobelkowe(lista)

    dolny = 0
    gorny = len(lista)-1

    while dolny < gorny:
        srodkowy = (dolny + gorny)//2

        if x > lista[srodkowy]:
            dolny = srodkowy + 1
        else:
            gorny = srodkowy

    if x == lista[dolny]:
        return dolny
    else:
        return -1

def rwyszukiwanie_binarne(lista, x, dolny=0, gorny=None):
    if gorny is None:
        lista = sortowanie_bobelkowe(lista)
        gorny = len(lista)-1
    if dolny < gorny:
        srodkowy = (dolny + gorny)//2
        if x > lista[srodkowy]:
            return rwyszukiwanie_binarne(lista, x, srodkowy+1, gorny)
        else:
            return rwyszukiwanie_binarne(lista, x, dolny, srodkowy)
    else: 
        if x == lista[dolny]:
            return dolny
        else:
            return -1
    
a = [4, 8, 12, -7, 3.333, 0, 0, 8]
print(sortowanie_bobelkowe(a))
print(rwyszukiwanie_binarne(a, 8))
