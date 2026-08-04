# 2. Write a program to find maximum and minimum element in a list.

lst = [30,24,56,98,65,77,90,99,30,120]

max_ele = 0 
min_ele = lst[0]

for i in range(len(lst)):
    if(lst[i] > max_ele):
        max_ele = lst[i]

    if(lst[i] < min_ele):
        min_ele = lst[i]

print("Maximum Element = ", max_ele)
print("Minimum Element = ", min_ele)
