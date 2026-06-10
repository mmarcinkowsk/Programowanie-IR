#!/usr/bin/python3

import threading
import re
import time

from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError

start_URL = 'https://www.fuw.edu.pl/~mmarcinkowski/dydaktyka/powolna_strona.php'
href_pat = r'<a.*href=\"([^\"]*)\".*?>'

def znajdz_linki(url):
    try:
        kod_HTML = urlopen(url).read().decode('utf-8')
        
        linki_wzgledne = re.findall(href_pat, kod_HTML) # szukam linków regexem
        linki_bezwzgledne = [urljoin(start_URL, link) for link in linki_wzgledne] # przerabiam na użyteczne linki
        return linki_bezwzgledne
    except HTTPError:
        return []
    

def szukaj(url, zagniezdzenie=0):
    linki = znajdz_linki(url)
    print(f'{url} :')
    print(linki)
    if zagniezdzenie > 0:
        for link in linki:
            time.sleep(0.1) # opóźnienie, żeby nie obciążać niepotrzebnie strony
            szukaj(link, zagniezdzenie-1)
            
def szukaj_wielowatkowo(url, zagniezdzenie=0):
    time.sleep(0.1) # opóźnienie, żeby nie obciążać niepotrzebnie strony
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