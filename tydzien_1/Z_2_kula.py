#!/usr/bin/python3

import math

r = float(input("Podaj promień:"))

P = 4*math.pi*r*r
V = (4/3)*math.pi*r**3

print(f"Pole powierzchni wynosi {P}")
print(f"Objętość wynosi {V}")
