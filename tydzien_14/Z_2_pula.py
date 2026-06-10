#!/usr/bin/python3

import multiprocessing

import time

import numpy as np


N = 100000
powtorzen = 1000
wyniki = []

def oblicz_MC(N):
    punkty = np.random.rand(N, 2)
    promienie = np.sqrt(np.sum(punkty**2, axis=1))

    return 4*len(punkty[promienie <= 1])/N

if __name__ == '__main__':
    t0 = time.time()
    for powtorzenie in range(powtorzen):
        wyniki.append(oblicz_MC(N))
    t1 = time.time()

    t2 = time.time()    
    with multiprocessing.Pool() as pula:
        '''Tworzę pulę procesów. Jeśli nie sprecyzuję liczby,
        Stworzy ich tyle, ile rdzeni ma procesor (`os.process_cpu_count()`).'''

        wyniki_pula = list(pula.imap_unordered(oblicz_MC, [N]*powtorzen))
        '''Używam puli, by obliczyć wartości funkcji `oblicz_MC` na
        elementach listy `[N]*powtorzen`.
        Metoda `.imap_unordered` zwraca wartości nie koniecznie w tej
        samej kolejności, co zawartość wejściowej listy (tu nam na tym
        nie zależy).
        Podobna metoda `.imap` zwraca wartości zachowują kolejność,
        ale przez to wątki czekają na siebie, zanim zwrócą wynik
        i obliczenia będą (odrobinę) wolniejsze.'''
    t3 = time.time()

    wyniki = np.array(wyniki)
    wyniki_pula = np.array(wyniki_pula)

    print(f'pi = {np.mean(wyniki)} +- {np.std(wyniki)}')
    print(f'pi = {np.mean(wyniki_pula)} +- {np.std(wyniki_pula)}')
    print(f'Pętla for: {t1-t0}s')
    print(f'Pula procesów: {t3-t2}s')