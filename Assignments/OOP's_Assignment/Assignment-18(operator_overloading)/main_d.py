from distance import Distance

d1 = Distance(2, 30, 50)
d2 = Distance(1, 40, 30)

d3 = d1 + d2
print("Addition:")
d3.display()

d4 = d1 - d2
print("Subtraction:")
d4.display()