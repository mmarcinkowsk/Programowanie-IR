#!/usr/bin/python3

import math

class Okrag():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def obwod(self):
        return 2*math.pi*self.r
    
    def przeciecia(self, drugi_okrag):
        odleglosc_srodkow = math.sqrt( (self.x - drugi_okrag.x)**2 + (self.y - drugi_okrag.y)**2 )

        if odleglosc_srodkow == self.r + drugi_okrag.r or odleglosc_srodkow == abs(self.r - drugi_okrag.r):
            if odleglosc_srodkow == 0 and self.r == drugi_okrag.r:
                return math.inf
            else:
                return 1
        elif odleglosc_srodkow > self.r + drugi_okrag.r or odleglosc_srodkow < abs(self.r - drugi_okrag.r):
            return 0
        else:
            return 2
    

o1 = Okrag(0, 0, 1)
o2 = Okrag(0, 2, 1)

print(o1.obwod())
print(o1.przeciecia(o2))
