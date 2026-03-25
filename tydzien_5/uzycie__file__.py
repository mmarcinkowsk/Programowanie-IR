# Stała __file__ pokazuje położenie skrptu z kodem na dysku.
print(__file__)

# Przydaje się gdy chcemy znaleźć ścieżki do innych plików znajdujących się w tym samy katalogu, co skrypt.
# Dzięki temu nie musimy podawać ścieżki bezwględnej do każdego pliku, który chcemy otworzyć.
# Do tego celu można na przykład użyć funkcji z biblioteki os.

import os

katalog_nadrzedny = os.path.dirname(__file__)

print(f'Skrypt znajduje się w katalogu {katalog_nadrzedny}')

pliki_wym_katalogu = os.listdir(katalog_nadrzedny)

print(f'Lista plików w tym katalogu: {pliki_wym_katalogu}')

scierzka_bezwzgledna_do_pliku_inwokacjatxt = os.path.join(katalog_nadrzedny, 'inwokacja.txt')

print(f'Plik inwokacja.txt znajduje się pod ścieżką {scierzka_bezwzgledna_do_pliku_inwokacjatxt}')

# Funkcje takie, jak os.path.dirname czy os.path.join działają na każdym systemie operacyjnym, więc nie musimy modyfikować kodu, by dział na Windowsie, Linuxie, Macu itp.
# Nazwy funkcji z os bywają dziwaczne, niektóre są pod os.path, a inne nie, dlatego nie polecam zapamiętywać tego wszystkiego, tylko za każdym razem sobie sprawdzać.
