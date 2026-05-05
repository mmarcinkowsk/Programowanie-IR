class Srednia():

    def __init__(self, x):
        self.x = x

    def N(self):
        return len(self.x)
    
    def __call__(self):
        raise NotImplementedError()
    
class SredniaArytmetyczna(Srednia):

    def __init__(self, x):
        super().__init__(x)

    def __call__(self):
        return sum(self.x)/self.N()
    
class SredniaGeometryczna(Srednia):

    def __call__(self):
        product = 1

        for a in self.x:
            product *= a

        return product**(1/self.N())
    
class SredniaHarmoniczna(Srednia):

    def __call__(self):
        return self.N()/sum([1/a for a in self.x])
    

x = [1, 2, 3, 4, 5, 6]

ari = SredniaArytmetyczna(x)
geo = SredniaGeometryczna(x)
har = SredniaHarmoniczna(x)

print(ari.N())
print(ari())
print(geo())
print(har())