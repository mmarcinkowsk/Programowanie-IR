#!/usr/bin/python3

class Stos():

    def __init__(self):
        self.__lista = []

    def push(self, x):
        self.__lista.append(x)

    def pop(self):
        return self.__lista.pop()
    
    def czy_pusty(self):
        if len(self.__lista) == 0:
            return True
        else:
            return False
    

stos = Stos()

napis = input('Podaj napis:')

for litera in napis:
    stos.push(litera)

nowy_napis = ''

while not stos.czy_pusty():
    nowy_napis += stos.pop()

print(nowy_napis)
