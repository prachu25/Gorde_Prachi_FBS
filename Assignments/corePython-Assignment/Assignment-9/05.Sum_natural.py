# Write a program to find sum of n numbers using recursion.

def sum_of_number(num):

    if num == 0:
        return 0

    return num + sum_of_number(num - 1)

n = 2
print(f"sum of {n} = ", sum_of_number(n))