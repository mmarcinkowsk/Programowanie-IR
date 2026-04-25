#!/usr/bin/python3

def gcd(a, b):
    '''Największy wspólny dzielnik.'''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class LiczbaWymierna():
    
    def __init__(self, p=0, q=1):
        if q == 0:
            raise ZeroDivisionError
        self.p = p // gcd(abs(p), abs(q))
        self.q = q // gcd(abs(p), abs(q))
        if self.q < 0:
            self.p *= -1
            self.q *= -1
        
    def __str__(self):
        if self.q == 1:
            return str(self.p) # p/1 wyświetlam jako p
        else:
            return f'{self.p}/{self.q}'
    
    def __float__(self):
        return self.p/self.q
    
    def __int__(self):
        znak = self.p//abs(self.p)
        return znak*(abs(self.p) // self.q) # zaokrąglam do liczby całkowitej bliżej zera, analogicznie do konwersji float na int
    
    def __bool__(self):
        return bool(self.p)
    
    def licznik(self):
        return self.p
    
    def mianownik(self):
        return self.q
    
    def __neg__(self):
        return LiczbaWymierna(-self.p, self.q)
    
    def __add__(self, other):
        if isinstance(other, LiczbaWymierna):
            return LiczbaWymierna(self.p*other.q + other.p*self.q, self.q*other.q)
        elif isinstance(other, int):
            return LiczbaWymierna(self.p + other*self.q, self.q)
        elif isinstance(other, float):
            return float(self) + other
        
    def __radd__(self, other):
        return self + other
        
    def __mul__(self, other):
        if isinstance(other, LiczbaWymierna):
            return LiczbaWymierna(self.p*other.p, self.q*other.q)
        elif isinstance(other, int):
            return LiczbaWymierna(other*self.p, self.q)
        elif isinstance(other, float):
            return float(self) * other
        
    def __rmul__(self, other):
        return self*other
    
    def __truediv__(self, other):
        if isinstance(other, LiczbaWymierna):
            return LiczbaWymierna(self.p*other.q, self.q*other.p)
        elif isinstance(other, int):
            return LiczbaWymierna(self.p, self.q*other)
        elif isinstance(other, float):
            return float(self) / other
        
    def __rtruediv__(self, other):
        if other == 1:
            return LiczbaWymierna(self.q, self.p)
        else:
            return 1/(self/other)
        
    def __mod__(self, other):
        if isinstance(other, int):
            return LiczbaWymierna(self.p % (other*self.q), self.q)
        else:
            return float(self) % other
        
    def __floordiv__(self, other):
        if isinstance(other, (int, LiczbaWymierna)):
            return self/other
        else:
            return float(self) // other
        
    def __pow__(self, other):
        if isinstance(other, int):
            if other == 0:
                return LiczbaWymierna(1)
            elif other > 0:
                return self* (self**(other-1))
        return float(self)**other
    
    def __sub__(self, other):
        return self + (-other)
    
    def __rsub__(self, other):
        return -(self - other)
            
    def __iadd__(self, other):
        return self + other
    
    def __imul__(self, other):
        return self*other
    
    def __itruediv__(self, other):
        return self/other
    
    def __isub__(self, other):
        return self - other
            
    def __lt__(self, other):
        if isinstance(other, LiczbaWymierna):
            return self.p*other.q < other.p*self.q
        elif isinstance(other, int):
            return self.p < other*self.q
        elif isinstance(other, float):
            return float(self) < other
        
    def __le__(self, other):
        if isinstance(other, LiczbaWymierna):
            return self.p*other.q <= other.p*self.q
        elif isinstance(other, int):
            return self.p <= other*self.q
        elif isinstance(other, float):
            return float(self) <= other
        
    def __gt__(self, other):
        return not (self <= other)
    
    def __ge__(self, other):
        return not (self < other)
    
    def __eq__(self, value):
        return (self <= value) and (self >= value)
    
    def __ne__(self, value):
        return not self == value
    
    def __abs__(self):
        return LiczbaWymierna(abs(self.p), self.q)
    
if __name__ == '__main__':
    a = LiczbaWymierna(12, -27)
    b = LiczbaWymierna(3, 9)

    print(LiczbaWymierna())
    print(LiczbaWymierna(5))
    print(a)
    print(float(a))
    print(-a)
    print(b)
    print(a+b)
    print(b + 1)
    print(1 + b)
    print(2*b)
    print(b*a)
    print(a<b)
    print(a/2)
    print(1/a)
    print(a/b)
    print(a-b)
    print(a<1)
    print(a < 0.1)
    print(a <= 0.1)
    print(a > 0.1)
    print(a == 0.1)
    print(a != 0.1)
    print(a-1)
    print(1-a)
    print(abs(a))
    print(int(LiczbaWymierna(7,2)))
    print(int(-LiczbaWymierna(7,2)))
    print(LiczbaWymierna(1, 0))
