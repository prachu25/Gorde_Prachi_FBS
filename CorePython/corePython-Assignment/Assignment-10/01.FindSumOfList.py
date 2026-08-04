# 1. Write a program to find sum of all elements of list
n  = int(input('Enter a number of Element: '))

list = []


for i in range(n):
    ele = int(input(f"Enter a Element {i+1}: "))
    list.append(ele)

# print(list)

total = 0

for i in range(n):
    total = total + list[i]

print(f"Sum Of List Element = {total}")