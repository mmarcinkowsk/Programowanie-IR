#!/usr/bin/python3

import numpy as np
from scipy.integrate import quad

def f(x):
    return 1/x

print(quad(f, 1, 10))
print(f' {np.log(10)}')


def f(x):
    return 1/(1 + x**2)

print(quad(f, 0, 1))
print(f' {np.pi/4}')   

def f(x):
    return np.exp(-(x)**2)

print(quad(f, -np.inf, np.inf))
print(f' {np.sqrt(np.pi)}') 
