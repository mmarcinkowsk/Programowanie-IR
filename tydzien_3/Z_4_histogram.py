#!/usr/bin/python3

import json

import matplotlib.pyplot as plt

def przygotuj_histogram(granice, punkty):

    # Przygotowuję strukturę słownika.
    histogram ={f"<{granice[0]}":0}
    for i in range(len(granice)-1):
        histogram[f"{granice[i]}-{granice[i+1]}"] = 0
    histogram[f"{granice[-1]}>="] = 0

    for punkt in punkty: # Zliczam punkty przypadające na każdy przedział.
        if punkt < granice[0]:
            histogram[f"<{granice[0]}"] += 1
        elif punkt >= granice[-1]:
            histogram[f"{granice[-1]}>="] += 1
        else:
            # Dla punktów mieszczących się wewnątrz granic, znajduję odpowiedni
            # przedział algorytmem wyszukiwania binarnego ( tydzien_2/Z_2_binarne.py)
            dolny = 0
            gorny = len(granice)-1

            while dolny < gorny-1:
                srodek = (dolny+gorny)//2

                if punkt < granice[srodek]:
                    gorny = srodek
                else:
                    dolny = srodek
            histogram[f"{granice[dolny]}-{granice[dolny+1]}"] += 1

    return histogram

def narysoj_histogram(histogram):

    fig, ax = plt.subplots()

    ax.bar(histogram.keys(), histogram.values())

    plt.show()

# histogram = przygotuj_histogram([0, 1, 2, 3], [0.5, 1, 1.5, 1.7, 2])

plik = open("tydzien_3/D-42.json")
dane = json.load(plik)
plik.close()

granice = dane["granice"]
liczby = dane["dane"]

histogram = przygotuj_histogram(granice, liczby)

narysoj_histogram(histogram)