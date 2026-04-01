import re
from operator import add, sub, mul, truediv, mod, pow

def calc(napis):
    wzor = r'([0-9]+\.?[0-9]*) ([+\-*/%^]) ([0-9]+\.?[0-9]*)'

    # Rozwiązanie zaproponowane przez doktorantkę
    operacje = {'+':add, '-':sub, '*':mul, '/':truediv, '%':mod, '^':pow}

    wynik_wyszukiwania = re.search(wzor, napis)

    if wynik_wyszukiwania:
        x = float(wynik_wyszukiwania.group(1))
        y = float(wynik_wyszukiwania.group(3))
        operacja = operacje[wynik_wyszukiwania.group(2)]

        return operacja(x, y)
        # if operacja == '+':
        #     return x+y
        # elif operacja =='-':
        #     return x-y
        # elif operacja == '*':
        #     return x*y
        # elif operacja == '/':
        #     return x/y
        # elif operacja == '%':
        #     return x%y
        # elif operacja == '^':
        #     return x**y

print(calc('12.358 + 73.14'))

# w tym miejscu skończyliśmy