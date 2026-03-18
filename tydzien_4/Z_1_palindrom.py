#!/usr/bin/python3

def palindrom(napis):
    lewa = 0 # Wskazuje na położenie lewego znaku, który porównuję.
    prawa = len(napis) - 1 # Wskazuje na położenie prawego znaku, który porównuję.
    while lewa < prawa:
        while not napis[lewa].isalpha(): # Przeskakuję po znakach nie będących literami.
            lewa += 1
            if lewa > len(napis): # Na wypadek, gdyby skończyły się już litery i do końca napisu były inne znaki.
                return True

        while not napis[prawa].isalpha(): # Przeskakuję po znakach nie będących literami.
            prawa -= 1
            if prawa < 0:
                return True

        if napis[prawa].lower() != napis[lewa].lower():
            return False
        
        lewa += 1
        prawa -= 1
        
    return True


# Alternatywne rozwiązanie, zainspirowane pomysłami kilku studentów.
from string import punctuation, whitespace

ignorowane_znaki = punctuation + whitespace

def palindrom2(napis):
    napis = napis.lower() # Zamieniam wszystkie litery w napisie na małe.

    for ignowany_znak in ignorowane_znaki:
        napis = napis.replace(ignowany_znak, '') # Usuwam wszystkie niepotrzebne znaki z napisu

    for i in range(len(napis)//2):
        if napis[i] != napis[-1-i]:
            return False
        
    return True

print(palindrom2("Kobyła ma mały bok."))
        
