#!/usr/bin/python3

from queue import Queue
import threading

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# Uruchamianie okienka matplotliba przez nie główny wątek
# powoduje problemy. Polecenie `matplotlib.use('agg')` powoduje,
# że matplotlib nie będzie próbował otwierać okienek,
# i tym samym nie przeszkadza mu wielowątkowość.
matplotlib.use('agg')

def zrob_wykres(x, y, nazwa_pliku):
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    
    fig.savefig(nazwa_pliku)
    plt.close(fig)


# Kolejka zadań, kompatybilna z wielowątkowością.
zadania = Queue()

def watek_robotnik(nazwa):
    '''Ten wątek będzie wykonywał rysunki.'''
    while True:
        zadanie = zadania.get() # Pobiera zadanie z kolejki zadań do wykonania
        x, y, nazwa_pliku = zadanie
        zrob_wykres(x, y, nazwa_pliku) # wykonuje zadanie
        print(f'Wątek {nazwa} przygotował plik {nazwa_pliku}.')
        zadania.task_done() # Wątek zgłasza wykonanie zadania

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.linspace(0, 10, 1000)

# Kolejkuję zadania do wykonania
zadania.put((x, np.sin(x), 'sin.pdf'))
zadania.put((x, np.cos(x), 'cos.pdf'))
zadania.put((x, np.tan(x), 'tan.pdf'))
zadania.put((x, np.sinh(x), 'sinh.pdf'))
zadania.put((x, np.cosh(x), 'cosh.pdf'))
zadania.put((x, np.tanh(x), 'tanh.pdf'))
zadania.put((x, np.exp(x), 'exp.pdf'))
zadania.put((x, 1/x, 'recp.pdf'))
zadania.put((x, x**2, 'square.pdf'))
zadania.put((y, np.log(y), 'log.pdf'))
zadania.put((y, np.sqrt(y), 'sqrt.pdf'))



watki = [threading.Thread(target=watek_robotnik, args=(name,), daemon=True) for name in ['A', 'B', 'C']]
# W programowaniu słowo "daemon" pojawia się w kilku miejscach z różnymi, ale podobnymi znazceniami.
# Zwykle daemon to "coś co pracuje w tle, możemy z tego korzystać, ale nie musimy tym się martwić".
# W kontekście wątków `daemon=True` oznacza, że nie musimy czekać, aż wątek zakończy pracę (nie
# musimu czekać na `wątek.join()`) przed zakończeniem programu.
# Przydaje się to do tworzenia wątków, które pracują w nieskończonych pętlach, wykonując zadania,
# gdy jakieś się pojawią.

for t in watki: # Urochamiam wątki
    t.start()
    
# Linijka `zadania.join()` oznacza "czekaj, aż wszystkie zadania zostaną wykonane",
# co dokładniej oznacza "czekaj, aż `zadania.task_done()` zostanie wywołane tyle razy,
# ile elementów zakolejkowano w kolejce metodą `.put()`."
zadania.join()
