#!/usr/bin/python3

import threading
import multiprocessing

import time

import urllib.request

adres_strony = 'https://www.fuw.edu.pl/~mmarcinkowski/dydaktyka/powolna_strona.php'

def wczytaj_strone():
    '''Wczytuje stronę `adres_strony` i printuje jej kod HTML.'''
    print(urllib.request.urlopen(adres_strony).read())

def f():
    print('Ala ma kota.')

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def wypisz_fib(n):
    print(fib(n))

def wykonaj_wielowatkowo(f, args, N):
    '''
    f - funkcja do wykonania przez wątek,
    args - lista/krotka argumentów do podania funkcji f,
    N - liczba wątków do utworzenia.
    '''
    watki = []
    for i in range(N): # Tworzę wątki
        watki.append(threading.Thread(target=f, args=args))

    for watek in watki: # Uruchamiam wątki
        watek.start()

    for watek in watki: # Czekam, aż wątki skończą pracę ("zbieram" wątki)
        watek.join()

def wykonaj_wieloprocesowo(f, args, N):
    '''
    f - funkcja do wykonania przez proces,
    args - lista/krotka argumentów do podania funkcji f,
    N - liczba procesów do utworzenia.
    '''
    procesy = []
    for i in range(N): # Tworzę procesy
        procesy.append(multiprocessing.Process(target=f, args=args))

    for proces in procesy: # Uruchamiam procesy
        proces.start()

    for proces in procesy: # Czekam, aż procesy skończą pracę
        proces.join()

if __name__ == '__main__':
    """Główną część programu umieszczam wewnątrz `if __name__ == '__main__'`
    Na niektórych systemach operacyjnych (nawet różne dystrybucje linuxa porafią
    zachowywać się inaczej) uruchomienie dodatkowych procesów może wywołać
    uruchomienie przez nie fragmentów kodu poza funkcją `f`. Wareunek  na `__name__`
    pozwala wykryć nie tylko, czy skrypt jest ładowany jako biblioteka (`import`),
    ale również, czy jest uruchamiany jako podproces.
    WAŻNE: W takiej sytuacji należu umieścić definicję funkcji wywoływanej przez podproces
    POZA warunkiem `if __name__ == '__main__'`, inaczej może nie zostać zdefiniowana w
    podprocesie.
    (multiprocessing jest dziwny :( )"""


    print('Testy na ciągu Fibonacciego:')
    print('Jednowątkowo:')
    tf0 = time.time()
    for i in range(10):
        wypisz_fib(32)

    tf1 = time.time()

    print('Wielowątkowo:')
    tf2 = time.time()
    wykonaj_wielowatkowo(wypisz_fib, [32], 10)
    tf3 = time.time()

    print('Wieloprocesowo:')
    tf4 = time.time()
    wykonaj_wieloprocesowo(wypisz_fib, [32], 10)
    tf5 = time.time()



    print('Testy z ładowaniem powolnej strony:')
    print('Jednowątkowo:')
    ts0 = time.time()
    for i in range(10):
        wczytaj_strone()

    ts1 = time.time()

    print('Wielowątkowo:')
    ts2 = time.time()
    wykonaj_wielowatkowo(wczytaj_strone, [], 10)
    ts3 = time.time()

    print('Wieloprocesowo:')
    ts4 = time.time()
    wykonaj_wieloprocesowo(wczytaj_strone, [], 10)
    ts5 = time.time()


    print(f'Fibonacci jednowątkowo: {tf1-tf0}s')
    print(f'Fibonacci wielowątkowo: {tf3-tf2}s')
    print(f'Fibonacci wieloprocesowo: {tf5-tf4}s')

    print(f'Ładowanie strony jednowątkowo: {ts1-ts0}s')
    print(f'Ładowanie strony wielowątkowo: {ts3-ts2}s')
    print(f'Ładowanie strony wieloprocesowo: {ts5-ts4}s')
