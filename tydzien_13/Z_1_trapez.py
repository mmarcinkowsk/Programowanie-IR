#!/usr/bin/python3

import numpy as np

def trapezy(f, a, b, N):
    delta_x = (b-a)/N
    x_k = np.linspace(a, b, N+1)
    y_k = f(x_k)
    return np.sum(y_k[:-1] + y_k[1:])*delta_x/2

def f(x):
    return 1/x

print(trapezy(f, 1, 10, 10000))
print(np.log(10))
