#!/usr/bin/python3

import math

class Beta():

    def __init__(self, beta):
        self.beta = beta

    def gamma(self):
        return 1/math.sqrt(1 - self.beta**2)
    
    def __add__(self, other):
        if isinstance(other, Beta):
            nowa_beta = (self.beta + other.beta)/(1+self.beta*other.beta)
            return Beta(nowa_beta)
        else:
            raise TypeError(f'Zły rodzaj argumentu, nie umiem dodać  obiektu typu {type(other)}.')
        
    def __iadd__(self, other):
        return self + other
        
    def __str__(self):
        return f"beta = {self.beta}"
    

b1 = Beta(0.5)
b2 = Beta(0.3)
b3 = b1 + b2
b3 += b1

print(b3)