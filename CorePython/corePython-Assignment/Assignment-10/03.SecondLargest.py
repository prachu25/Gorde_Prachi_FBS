# 3. Write a program to find the second largest element in the list.
lst = [30,24,56,98,65,77,90,99,30,120]

max = 0
second_max = 0

for i in range(len(lst)):
    if(lst[i] > max):
        second_max = max
        max = lst[i]
    else:
        if(lst[i] < second_max and second_max != max):
            second_max = lst[i]


print("Second Maximum Element = ", second_max)