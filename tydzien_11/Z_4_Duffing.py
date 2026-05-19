#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def duffing(t, u, a, b, g, d, omega):
    x, v = u

    dx_dt = v
    dv_dt = -d*v - b*x - a*x**3 + g*np.cos(omega*t)

    return dx_dt, dv_dt

t_span = (0, 100)
a = 1
b = -1 
d = 0.2
g = 0.3
omega = 1

u01 = (0.99, 0)
u02 = (1, 0)
u03 = (1.01, 0)

sol1 = solve_ivp(duffing, t_span, u01, args=(a, b, g, d, omega), dense_output=True)
sol2 = solve_ivp(duffing, t_span, u02, args=(a, b, g, d, omega), dense_output=True)
sol3 = solve_ivp(duffing, t_span, u03, args=(a, b, g, d, omega), dense_output=True)

czasy = np.linspace(t_span[0], t_span[1], 10000)
x1, v1 = sol1.sol(czasy)
x2, v2 = sol2.sol(czasy)
x3, v3 = sol3.sol(czasy)

fig, ax = plt.subplots()

ax.plot(czasy, x1)
ax.plot(czasy, x2)
ax.plot(czasy, x3)

plt.show()
plt.close()

fig, ax = plt.subplots()

ax.plot(x1, v1)
ax.plot(x2, v2)
ax.plot(x3, v3)

plt.show()
plt.close()