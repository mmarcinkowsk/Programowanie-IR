#!/usr/bin/python3

import time

import matplotlib.pyplot as plt

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


    
# n = int(input("Podaj n:"))

lista_n = list(range(1, 30))
lista_czasow_r = []
lista_czasow_i = []

for n in lista_n:

    t0 = time.time()
    fib_rekurencyjnie = rfib(n)
    t1 = time.time()
    lista_czasow_r.append(t1-t0)

    t0 = time.time()
    fib_iteracyjnie = ifib(n)
    t1 = time.time()
    lista_czasow_i.append(t1-t0)

fig, ax = plt.subplots()

ax.plot(lista_n, lista_czasow_r, label='rekurencyjnie')
ax.plot(lista_n, lista_czasow_i, label='iteracyjnie')

ax.legend()
ax.set_xlabel('n')
ax.set_ylabel('czas [s]')
ax.set_yscale('log')

plt.show()
