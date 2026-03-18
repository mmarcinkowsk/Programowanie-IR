#!/usr/bin/python3

import random

liczby = set()

while len(liczby) < 6:
    liczby.add(random.randint(1, 49))

print(liczby)