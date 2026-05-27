#!/usr/bin/python3

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

katalog_nadrzedny = os.path.dirname(__file__)
dane = pd.read_csv(os.path.join(katalog_nadrzedny, 'uklad_RC.csv'))

# print(dane['t'])

def model(t, U0, t0, tau):
    return U0*(1 - np.exp(-(t-t0)/tau))

p0 = (5, 0, 1)
popt, pcov = curve_fit(model, dane['t'], dane['U'], p0, sigma=dane['U_err'])

# print(popt)
# print(pcov)

# model(t, *popt)

czasy = np.linspace(min(dane['t']), max(dane['t']), 1000)

fig, ax = plt.subplots()

ax.errorbar(dane['t'], dane['U'], dane['U_err'], fmt='.', linestyle='none')#, markersize=1)
ax.plot(czasy, model(czasy, *popt))

ax.set_xlabel('$t$ (s)')
ax.set_ylabel('$U$ (V)')

plt.show()
plt.close(fig)
