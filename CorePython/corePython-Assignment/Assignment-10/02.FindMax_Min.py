# 2. Write a program to find maximum and minimum element in a list.

def findMaxMin(lst):
    max_ele = lst[0]
    min_ele = lst[0]

    for i in range(len(lst)):
        if(lst[i] > max_ele):
            max_ele = lst[i]

        if(lst[i] < min_ele):
            min_ele = lst[i]

    return max_ele, min_ele


numbers = [22, 33, 45, 90, 81, 76, 120]

maximum , minimum = findMaxMin(numbers)

print("Maximum = ",maximum)
print("Minimim = ", minimum)


