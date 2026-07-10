# 11. Find the area and circumference of circle.

import math

radius = float(input("Enter radius: "))

# Formula of Area = pi*r*r
area = math.pi * radius * radius

# Formula of Circumference = 2pi*r
circumference = 2 * math.pi * radius

print("Area =", area)
print("Circumference =", circumference)