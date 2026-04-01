#!/usr/bin/python3

import sys

scierzka_pliku_wejsciowego = sys.argv[1]

with open(scierzka_pliku_wejsciowego) as plik_wejsciowy:
    suma = 0

    for linia in plik_wejsciowy.readlines():
        suma += float(linia.split(' ')[-1])

print(f'Suma = {suma}')
