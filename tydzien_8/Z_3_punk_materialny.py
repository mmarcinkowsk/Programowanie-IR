#!/usr/bin/python3

import matplotlib.pyplot as plt

from Z_2_wektor import Vector2D

class MasaPunktowa():

    def __init__(self, m, r, v):
        self.masa = m
        self.polozenie = r
        self.predkosc = v
        self.trajektoria = []

    def krok(self, F, dt):
        self.trajektoria.append(self.polozenie)
        self.predkosc += F/self.masa * dt
        self.polozenie += self.predkosc * dt

punkt = MasaPunktowa(1, Vector2D(1, 0), Vector2D(0, 2))


dt = 0.001
k=10
czasy = [dt*i for i in range(10000)]
for t in czasy:
    F = -k*punkt.polozenie
    punkt.krok(F, dt)

x = [r.x for r in punkt.trajektoria]
y = [r.y for r in punkt.trajektoria]

fig, ax = plt.subplots()

ax.plot(czasy, x)
ax.plot(czasy, y)

plt.show()
plt.close(fig)