def policz(lista):
    zbior_elementow = set(lista)

    slownik_krotnosci = {}

    for element in zbior_elementow:
        slownik_krotnosci[element] = lista.count(element)

    return slownik_krotnosci

a = [1, 6, 8, 6, 12, "abc", 1, 0]

print(a)
print(policz(a))
