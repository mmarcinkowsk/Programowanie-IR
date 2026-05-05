class Wielomian():

    def __init__(self, *args):
        if len(args) == 0:
            self.c = list()
            self.c.append(0)
        else:
            self.c = list(args)
        self.__pozbyj_sie_zer_na_koncu()

    def deg(self):
        return len(self.c) - 1
    
    def __call__(self, x):
        wynik = 0
        for n, wsp in enumerate(self.c):
            wynik += wsp*(x**n)

        return wynik
    
    def __str__(self):
        napis = ''
        for n, wsp in enumerate(self.c):
            napis += f' + {wsp}*x^{n}'

        return napis.strip(' +')
    
    def __getitem__(self, key):
        if key <= self.deg():
            return self.c[key]
        else:
            return 0
        
    def __setitem__(self, key, value):
        if key <= self.deg():
            self.c[key] = value
        else:
            while self.deg() < key:
                self.c.append(0)
            self.c[key] = value
        self.__pozbyj_sie_zer_na_koncu()

    def __pozbyj_sie_zer_na_koncu(self):
        while self.deg()>0 and self.c[-1] == 0:
            self.c.pop()

    def __add__(self, other):
        if isinstance(other, Wielomian):
            deg = max(self.deg(), other.deg())

            wspolczynniki = list()
            for n in range(deg+1):
                wspolczynniki.append(self[n] + other[n])

            return Wielomian(*wspolczynniki)
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            wspolczynniki = [other*wsp for wsp in self.c]
            return Wielomian(*wspolczynniki)
        
    def __rmul__(self, other):
        return self * other

    def D(self, deg=1):
        if deg==1:
            return Poly(*[(i+1)*self[i+1] for i in range(self.deg()+5)])
        else:
            return self.D().D(deg-1)
    
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

class WielomianHermitea(Wielomian):

    def __init__(self, n):
        super().__init__()

        for m in range((n//2)+1):
            self[n - 2*m] = (silnia(n)*(-1)**m * 2**(n-2*m))//(silnia(m)*silnia(n-2*m))

        
def dwumianowy(a, k):
    p = 1
    q = 1
    for h in range(k):
        p *= (a-h)
        q *= (k-h)
    return p/q

def legendre_wsp(n, k):
    if k > n:
        return 0
    xi = (n+k-1)/2
    return (2**n)*dwumianowy(n, k)*dwumianowy(xi, n)

class WielomianLegenrea(Poly):

    def __init__(self, n):
        super().__init__(0)
        for k in range(n+1):
            self[k] = legendre_wsp(n, k)


print(WielomianHermitea(3) + WielomianHermitea(4))

# w = Wielomian(1, 2, 3)
# print(w.c)
# print(w.deg())
# print(w(3))
# print(w)
# print(w[2])
# print(w[5])
# w[7] = 2
# print(w)
# w[7] = 0
# print(w)
# print(w.deg())
# print(w)
# print(w.__str__())
# v = Wielomian(3, 0, 0, 1)
# print(w+v)
# print(w*5)
# print(5*w)