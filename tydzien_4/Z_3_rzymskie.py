#!/usr/bin/python3

def int_do_rzyskiej(x):
    wynik = ''

    tysiace = x//1000
    setki = (x%1000)//100
    dziesatki = (x%100)//10
    jednosci = x%10

    wynik = 'M'*tysiace + 'C'*setki + 'X'*dziesatki + 'I'*jednosci

    wynik = wynik.replace('C'*9, 'CM')
    wynik = wynik.replace('CCCCC', 'D')
    wynik = wynik.replace('CCCC', 'CD')
    wynik = wynik.replace('X'*9, 'XC')
    wynik = wynik.replace('XXXXX', 'L')
    wynik = wynik.replace('XXXX', 'XL')
    wynik = wynik.replace('I'*9, 'IX')
    wynik = wynik.replace('IIIII', 'V')
    wynik = wynik.replace('IIII', 'IV')

    return wynik

def rzymskie_do_int(liczba):
    liczba = liczba.upper()
    wartosci = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    wynik = 0
    for litera in liczba:
        wynik += wartosci[litera]

    if 'CM' in liczba:
        wynik -= 200
    if 'CD' in liczba:
        wynik -= 200
    if 'XC' in liczba:
        wynik -= 20
    if 'XL' in liczba:
        wynik -= 20
    if 'IX' in liczba:
        wynik -= 2
    if 'IV' in liczba:
        wynik -= 2

    return wynik

# rozwiązanie zaproponowane przez jednego ze studentów, moim zdaniem elegantsze

def rzymskie_do_int_poprzednia(liczba):
    liczba = liczba.upper()
    wartosci = {'':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    poprzednia = ''
    wynik = 0

    for znak in liczba:
        wynik += wartosci[znak]
        if wartosci[poprzednia] < wartosci[znak]:
            wynik -= 2*wartosci[poprzednia]
        poprzednia = znak

    return wynik

print(int_do_rzyskiej(49))
print(rzymskie_do_int('XLIX'))
print(rzymskie_do_int_poprzednia('XLIX'))