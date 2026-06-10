#!/usr/bin/python3

import multiprocessing

import numpy as np

# opcjonalna biblioteka do ładnych pasków postępu
from tqdm import tqdm

N = 50000
powtorzen = 5000
wyniki = []

def oblicz_MC(N):
    punkty = np.random.rand(N, 2)
    promienie = np.sqrt(np.sum(punkty**2, axis=1))

    return 4*len(punkty[promienie <= 1])/N

if __name__ == '__main__':
    print('Pętla for:')
    for powtorzenie in tqdm(range(powtorzen)): 
        '''`tqdm` umie odczytać z `range`, ile iteracji wykona pętla,
        więc nie trzeba mu odzielnie podawać tej liczby.'''
        wyniki.append(oblicz_MC(N))
        
    print('Pula procesów:')
    with multiprocessing.Pool() as pula:
        wyniki_pula = list(tqdm(pula.imap_unordered(oblicz_MC, [N]*powtorzen), total=powtorzen))
        '''Przez specyfikę `.imap_unordered` nie da się zgóry odczytać z niego,
        ile wartości zwróci. Żeby `tqdm` wiedziało, ile będzie kroków,
        musimy samodzielnie je policzyć i podać argumentem `total`.'''

    wyniki = np.array(wyniki)
    wyniki_pula = np.array(wyniki_pula)

    print(f'pi = {np.mean(wyniki)} +- {np.std(wyniki)}')
    print(f'pi = {np.mean(wyniki_pula)} +- {np.std(wyniki_pula)}')