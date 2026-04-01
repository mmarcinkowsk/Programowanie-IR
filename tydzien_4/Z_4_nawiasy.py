#!/usr/bin/python3

def sprawdz(napis):
    otwarte = []

    for znak in napis:
        if znak in '([{':
            otwarte.append(znak)
        elif znak == ')':
            if len(otwarte) == 0:
                return False
            poprzedni = otwarte.pop()

            if poprzedni != '(':
                return False
        elif znak == ']':
            if len(otwarte) == 0:
                return False
            poprzedni = otwarte.pop()

            if poprzedni != '[':
                return False
        elif znak == '}':
            if len(otwarte) == 0:
                return False
            poprzedni = otwarte.pop()

            if poprzedni != '{':
                return False
    
    if len(otwarte) > 0:
        return False
    return True

def sprawdz_i_dopasuj(napis):
    otwarte = []

    for i, znak in enumerate(napis):
        if znak in '([{':
            otwarte.append((i, znak))
        elif znak == ')':
            if len(otwarte) == 0:
                return False
            j, poprzedni = otwarte.pop()

            if poprzedni != '(':
                return False
            print(f'() {j}-{i}')
        elif znak == ']':
            if len(otwarte) == 0:
                return False
            j, poprzedni = otwarte.pop()

            if poprzedni != '[':
                return False
            print(f'[] {j}-{i}')
        elif znak == '}':
            if len(otwarte) == 0:
                return False
            j, poprzedni = otwarte.pop()

            if poprzedni != '{':
                return False
            print(f'{{}} {j}-{i}')
    
    if len(otwarte) > 0:
        return False
    return True


def skonstruuj(napis, liczba_otwierajacych, liczba_zamykajacych, zbior):
    if liczba_zamykajacych > liczba_otwierajacych:
        skonstruuj(napis + ')', liczba_otwierajacych, liczba_zamykajacych-1, zbior)
    if liczba_otwierajacych > 0:
        skonstruuj(napis + '(', liczba_otwierajacych-1, liczba_zamykajacych, zbior)
    
    if liczba_otwierajacych == 0 and liczba_zamykajacych == 0:
        zbior.add(napis)


def wypisz(n):
    zbior = set()
    skonstruuj('', n, n, zbior)
    return zbior

print(wypisz(4))

# print(sprawdz_i_dopasuj('(){[]{([])}}'))
