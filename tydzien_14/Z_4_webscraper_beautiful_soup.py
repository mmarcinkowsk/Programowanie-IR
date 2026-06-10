#!/usr/bin/python3

import threading
import time

from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError

# Biblioteka do analizowania kodu HTML
from bs4 import BeautifulSoup

start_URL = 'https://www.fuw.edu.pl/~mmarcinkowski/dydaktyka/powolna_strona.php'

def znajdz_linki(url):
    try:
        kod_HTML = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(kod_HTML, 'html.parser')
        # HTML przechowuje linki w tagach `<a>`, w ich atrybucie `href`.
        linki_wzgledne = [link.get('href') for link in soup.find_all('a')]
        
        linki_bezwzgledne = [urljoin(start_URL, href) for href in linki_wzgledne]
        return linki_bezwzgledne
    except HTTPError:
        return []
    

def szukaj(url, zagniezdzenie=0):
    linki = znajdz_linki(url)
    print(f'{url} :')
    print(linki)
    if zagniezdzenie > 0:
        for link in linki:
            time.sleep(0.1)
            szukaj(link, zagniezdzenie-1)
            
def szukaj_wielowatkowo(url, zagniezdzenie=0):
    time.sleep(0.1)
    linki = znajdz_linki(url)
    print(f'{url} :')
    print(linki)
    if zagniezdzenie > 0:
        watki = []
        for link in linki:
            watek = threading.Thread(target=szukaj_wielowatkowo, args=(link, zagniezdzenie-1))
            watki.append(watek)
        
        for watek in watki:
            watek.start()
        for watek in watki:
            watek.join()
        
            
szukaj_wielowatkowo(start_URL, 2)