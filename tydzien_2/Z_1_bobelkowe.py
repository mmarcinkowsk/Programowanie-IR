def sortowanie_bobelkowe(lista):
    while True:
        liczba_zamian = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                liczba_zamian += 1
        if liczba_zamian == 0:
            break
    return lista

if __name__ == "__main__":
    a = [4, 8, 12, -7, 3.333, 0, 0, 8]
    print(a)
    print(sortowanie_bobelkowe(a))
