# Write a program to calculate area of an equilateral triangle.

import math

side = float(input('Enter the side of Equilateral triangle: '))

# Formula - Area = (√3 / 4) × side²
area = (math.sqrt(3) / 4) * side * side

print('The Area is ', area)
