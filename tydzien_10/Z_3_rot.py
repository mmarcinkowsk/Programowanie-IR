#!/usr/bin/python3

import numpy as np

def R(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

print(R(np.pi/2)@R(np.pi/3))
print(R(np.pi/2 + np.pi/3))
print(np.allclose(R(np.pi/2)@R(np.pi/3), R(np.pi/2 + np.pi/3)))

v = np.array([[0, 1], [1, 0], [2, 3], [9, -17]])
print(v.T)
print((R(np.pi/2)@v.T))