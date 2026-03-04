#!/usr/bin/python3

import math

def arctan(x, n):
    wynik = 0
    for k in range(n+1):
        wynik += ((-1)**k)*(x**(2*k+1))/(2*k+1)
    return wynik

def przybliz_pi(n):
    return 16*arctan(1/5, n) - 4*arctan(1/239, n)

n = int(input("Podaj n:"))
print(f"pi to w przybliżeniu {przybliz_pi(n)}")
print(f" błąd {math.pi - przybliz_pi(n)}")
