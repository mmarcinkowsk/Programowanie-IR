#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

N = 1000
M = 1000

X, Y = np.meshgrid(np.linspace(-2, 2, N), np.linspace(-2, 2, M))

c = X + 1j*Y
z = np.zeros(c.shape)
iteracje = np.inf*np.ones(c.shape)

for iteracja in range(20):
    z = z**2 + c
    ktore_wybuchaja = np.abs(z) > 2
    gdzie_nieskonczonosci = np.isinf(iteracje)
    iteracje[ktore_wybuchaja & gdzie_nieskonczonosci] = iteracja

fig, ax = plt.subplots()

ax.imshow(iteracje)

plt.show()
plt.close(fig)