#!/usr/bin/python3

import time

def rfib(n):
    if n==1 or n==2:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)
    
def ifib(n):
    if n==1 or n==2:
        return 1
    poprzednia = 1
    jeszcze_poprzednia = 1
    obecna = 0
    for k in range(2, n):
        obecna = poprzednia + jeszcze_poprzednia
        jeszcze_poprzednia = poprzednia
        poprzednia = obecna
    return obecna


    
n = int(input("Podaj n:"))

t0 = time.time()
fib_rekurencyjnie = rfib(n)
t1 = time.time()
print(f"F_{n} = {fib_rekurencyjnie}, czas obliczeń rekurencyjnie {t1-t0}s")

t0 = time.time()
fib_iteracyjnie = ifib(n)
t1 = time.time()
print(f"F_{n} = {fib_iteracyjnie}, czas obliczeń iteracyjnie {t1-t0}s")