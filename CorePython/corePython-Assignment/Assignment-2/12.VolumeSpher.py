# Find the volume of sphere.

import math

radius = float(input("Enter radius: "))

# Formula = ( 4/3 ) * pi r*r*r
volume = (4 / 3) * math.pi * radius ** 3

print("Volume =", volume)