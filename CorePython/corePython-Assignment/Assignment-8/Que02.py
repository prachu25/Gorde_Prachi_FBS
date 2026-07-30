import math

def area_circle():

    print("\n calulate the area of cirlce\n")

    radius = float(input('Enter the Radius of Circle: '))
    area = math.pi* radius * radius

    print("Area of Circle = ", round(area,2))


# Function Call
area_circle()