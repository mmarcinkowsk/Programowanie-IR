#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5*np.pi, 1000)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.plot(x, np.cos(x)**2 - np.sin(x)**2)

plt.show()
plt.close(fig)