#!/usr/bin/python3

# import cmath

a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

delta = b*b - 4*a*c

# x1 = (-b + cmath.sqrt(delta))/(2*a)
# x2 = (-b - cmath.sqrt(delta))/(2*a)
x1 = (-b + (delta)**(1/2))/(2*a)
x2 = (-b - (delta)**(1/2))/(2*a)
print(x1)
print(x2)

#if delta < 0:
#    sqrt_delta = math.sqrt(-delta)
#    print(f"{-b/(2*a)} + {sqrt_delta/(2*a)}i")
#    print(f"{-b/(2*a)} - {sqrt_delta/(2*a)}i")
#else:
#    sqrt_delta = math.sqrt(delta)
#    x1 = (-b + sqrt_delta)/(2*a)
#    x2 = (-b - sqrt_delta)/(2*a)
#    print(x1)
#    print(x2)
