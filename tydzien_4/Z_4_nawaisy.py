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
print(sprawdz('(){[]{([])}}'))

# tutaj skończyliśmy
            