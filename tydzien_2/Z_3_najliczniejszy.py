#!/usr/bin/python3

def najliczniejszy(lista):
    licznosc = 0
    naliczniejsze_elementy = []

    for element in lista:
        if lista.count(element) > licznosc:
            licznosc = lista.count(element)
            naliczniejsze_elementy = [element]
        elif lista.count(element) == licznosc:
            if element not in naliczniejsze_elementy:
                naliczniejsze_elementy.append(element)

    if len(naliczniejsze_elementy) == 1:
        return (naliczniejsze_elementy[0], licznosc)
    else:
        return [(element, licznosc) for element in naliczniejsze_elementy]
    
a = [1, 2, 4, 2, 8, "abc", "abc", -9, 4, 2]

print(a)
print(najliczniejszy(a))
