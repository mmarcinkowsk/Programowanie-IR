#!/usr/bin/python3

class Vector2D():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f'{other} nie jest wektorem.')
    
    def __mul__(self, other):
        if isinstance(other, (int, float)): # mnożenie przez liczbę
            return Vector2D(self.x*other, self.y*other)
        elif isinstance(other, Vector2D): # iloczyn skalarny
            return self.x*other.x + self.y*other.y
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            # return Vector2D(self.x/other, self.y/other)
            return self * (1/other)
        else:
            raise TypeError(f'{other} nie jest liczbą.')
        
    def __rmul__(self, other):
        return self*other
    
if __name__ == '__main__':
    v1 = Vector2D(0, 1)
    v2 = Vector2D(3, 4)

    print(v1+v2)
    print(v2*0.5)
    print(v1*v2)
    print(v1 + 'abc')