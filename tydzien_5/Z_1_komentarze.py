#!/usr/bin/python3

import sys

# print(sys.argv)

znak_komentarza = sys.argv[1]
scierzka_pliku_in = sys.argv[2]
scierzka_pliku_out = sys.argv[3]

plik_in = open(scierzka_pliku_in)
plik_out = open(scierzka_pliku_out, 'w')

for linia in plik_in.readlines():
    if not linia.startswith(znak_komentarza):
        plik_out.write(linia)

plik_in.close()
plik_out.close()