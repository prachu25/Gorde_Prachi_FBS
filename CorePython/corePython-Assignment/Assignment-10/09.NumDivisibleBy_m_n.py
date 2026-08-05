# 11. Write a program to print all numbers which are divisible by m and n in the list.


def divisible_numbers(lst, m, n):
    result = []

    for i in lst:
        if i % m == 0 and i % n == 0:
            result.append(i)


    return result

numbers = [10, 12, 15, 20, 24, 30, 40, 60]
m = 2
n = 5
print(divisible_numbers(numbers,m,n))