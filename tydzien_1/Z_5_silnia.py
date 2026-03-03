#!/usr/bin/python3

def kwadrat(x):
    return x**2

def rsilnia(n):
    if n == 0:
        return 1
    else:
        return n*rsilnia(n-1)
    
def isilnia_while(n):
    wynik = 1
    k = 1
    while k<=n:
        #wynik *= k
        wynik = wynik*k
        k += 1
    return wynik

def isilnia_for(n):
    wynik = 1
    for k in range(n):
        wynik = wynik*(k+1)
    return wynik

    
n = int(input("Podaj n:"))
print(f"{n}! = {rsilnia(n)}")
print(f"{n}! = {isilnia_while(n)}")
print(f"{n}! = {isilnia_for(n)}")
