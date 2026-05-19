#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def rownanie_wahadla(t, u, g, l):
    theta, omega = u

    dtheta_dt = omega
    domega_dt = -(g/l)*np.sin(theta)

    return np.array([dtheta_dt, domega_dt])

def Euler(t, u, rownanie, delta_t, args):
    du_dt = rownanie(t, u, *args)

    return u + du_dt*delta_t

def Euler_sympl(t, u, rownanie, delta_t, args):
    theta, omega = u
    dtheta_dt, domega_dt = rownanie(t, u, *args)

    nowa_omega = omega + domega_dt*delta_t
    nowa_theta = theta + nowa_omega*delta_t

    return np.array([nowa_theta, nowa_omega])

def RK4(t, u, rownanie, delta_t, args):
    k1 = rownanie(t, u, *args)
    k2 = rownanie(t + delta_t/2, u + k1*delta_t/2, *args)
    k3 = rownanie(t + delta_t/2, u + k2*delta_t/2, *args)
    k4 = rownanie(t + delta_t, u + k3*delta_t, *args)

    return u + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*delta_t


delta_t = 0.01
g = 10
l = 2
theta0 = 0.9*np.pi
omega0 = 0
liczba_krokow = 1000
czasy = np.linspace(0, delta_t*liczba_krokow, liczba_krokow)

u_E = [np.array([theta0, omega0])]
u_Esympl = [np.array([theta0, omega0])]
u_RK = [np.array([theta0, omega0])]

for ti in czasy[:-1]:
    nowe_u_E = Euler(ti, u_E[-1], rownanie_wahadla, delta_t, (g, l))
    nowe_u_Esympl = Euler_sympl(ti, u_Esympl[-1], rownanie_wahadla, delta_t, (g, l))
    nowe_u_RK = RK4(ti, u_RK[-1], rownanie_wahadla, delta_t, (g, l))
    u_E.append(nowe_u_E)
    u_RK.append(nowe_u_RK)
    u_Esympl.append(nowe_u_Esympl)


u_E = np.array(u_E)
u_RK = np.array(u_RK)
u_Esympl = np.array(u_Esympl)
theta_E, omega_E = u_E.T
theta_Esympl, omega_Esympl = u_Esympl.T
theta_RK, omega_RK = u_RK.T


t_span = (czasy[0], czasy[-1])
sol = solve_ivp(rownanie_wahadla, t_span, (theta0, omega0), args=(g, l), dense_output=True)
print(sol)
# sol.sol()

fig, ax = plt.subplots()

# ax.plot(czasy, theta_E, label='Euler')
ax.plot(czasy, theta_RK, label='Runge-Kutta')
# ax.plot(sol.t, sol.y[0], label='solve_ivp')
ax.plot(czasy, sol.sol(czasy)[0], label='solve_ivp')
ax.plot(czasy, theta_Esympl, label='Euler sympl')

fontsize = 20
ax.legend(fontsize=fontsize)

plt.show()
plt.close(fig)


fig, ax = plt.subplots()

# ax.plot(theta_E, omega_E, label='Euler')
ax.plot(theta_RK, omega_RK, label='Runge-Kutta')
ax.plot(sol.sol(czasy)[0], sol.sol(czasy)[1], label='solve_ivp')
ax.plot(theta_Esympl, omega_Esympl, label='Euler sympl')

ax.legend(fontsize=fontsize)

plt.show()
plt.close(fig)
