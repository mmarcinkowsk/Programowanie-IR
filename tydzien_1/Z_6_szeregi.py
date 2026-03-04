#!/usr/bin/python3

import Z_5_silnia

def szereg_exp(x, n):
    wynik = 0
    for k in range(n+1):
        wynik += (x**k)/(Z_5_silnia.rsilnia(k))
    return wynik

def szereg_cos(x, n):
    wynik = 0
    for k in range(n+1):
        wynik += ((-1)**k)*(x**(2*k))/Z_5_silnia.rsilnia(2*k)
    return wynik

if __name__ == "__main__":
    n = int(input("Podaj n:"))
    x = float(input("Podaj x:"))
    print(f"exp({x}) = {szereg_exp(x, n)}")
    print(f"cos({x}) = {szereg_cos(x, n)}")