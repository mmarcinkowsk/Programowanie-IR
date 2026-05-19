#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lv(t, u, a, b, c, d):
    x, y = u
    dx = (a - b*y)*x
    dy = (c*x - d)*y
    return dx, dy


u0 = (1, 0.1)
a = 1
b = 0.1
c = 1
d = 1
t_span = (0, 20)
sol = solve_ivp(lv, t_span, u0, args=(a, b, c, d), dense_output=True)

# print(sol)
time = np.linspace(*t_span, 1000)
x, y = sol.sol(time)

fig, ax = plt.subplots()

ax.plot(time, x, label='prey')
ax.plot(time, y, label='predator')

ax.legend()

plt.show()
plt.close(fig)

fig, ax = plt.subplots()

ax.plot(x, y)

plt.show()
plt.close(fig)