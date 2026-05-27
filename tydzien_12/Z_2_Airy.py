#!/usr/bin/python3

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.special

katalog_nadrzedny = os.path.dirname(__file__)
dane = pd.read_csv(os.path.join(katalog_nadrzedny, 'Airy.csv'))

def model(r, I0, alfa):
    x = alfa*r
    return I0*(2*scipy.special.j1(x)/x)**2

p0 = (0.9, 0.45)
popt, pcov = curve_fit(model, dane['r'], dane['I'], p0, dane['I_err'])
print(popt)

odleglosci = np.linspace(min(dane['r']), max(dane['r']), 1000)

fig, ax = plt.subplots()

ax.errorbar(dane['r'], dane['I'], dane['I_err'], fmt='.', linestyle='none')
ax.plot(odleglosci, model(odleglosci, *popt))
ax.plot(odleglosci, model(odleglosci, *p0))

ax.set_xlabel('$r$')
ax.set_ylabel('$I$')

plt.show()
plt.close(fig)
