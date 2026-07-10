# Program to Find the Roots of a Quadratic Equation

import math

a = float(input('Enter a value of a: '))
b = float(input('Enter a value of b: '))
c = float(input('Enter a Value of c: '))

d = b **2 - 4*a*c

root1 = (-b + math.sqrt(d)) / (2 * a)
root2 = (-b - math.sqrt(d)) / (2 * a)

print('Root1 =', root1)
print('Root2 =', root2)

