# Write a program to find sum of digits using recursion.

def sum_digit(num):

    if num == 0:
        return 0

    digit = num % 10
    return digit + sum_digit(num // 10)

n = 123
print(f"Sum of Digit {n} = ",sum_digit(n))