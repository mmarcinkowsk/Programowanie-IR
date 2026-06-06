#!/usr/bin/python3

import numpy as np

N = 10000
powtorzen = 1000
wyniki = []

for powtorzenie in range(powtorzen):
    punkty = np.random.rand(N, 2)
    promienie = np.sqrt(np.sum(punkty**2, axis=1))

    wyniki.append(4*len(punkty[promienie <= 1])/N)

wyniki = np.array(wyniki)

print(f'pi = {np.mean(wyniki)} +- {np.std(wyniki)}')
