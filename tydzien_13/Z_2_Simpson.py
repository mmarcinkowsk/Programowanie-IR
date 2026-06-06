#!/usr/bin/python3

import numpy as np

def Simpson(f, a, b, N):
    delta_x = (b-a)/N
    x_k = np.linspace(a, b, N+1)
    y_k_nieparzyste = f(x_k[1:-1:2])
    y_k_parzyste = f(x_k[2:-1:2])

    return (f(a) + 4*np.sum(y_k_nieparzyste) + 2*np.sum(y_k_parzyste) + f(b))*delta_x/3

def f(x):
    return 1/(1 + x**2)

print(Simpson(f, 0, 1, 6))
print(np.pi/4)

def f(x):
    return 1/x

print(Simpson(f, 1, 10, 1000))
print(np.log(10))
