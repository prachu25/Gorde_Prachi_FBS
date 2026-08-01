# Write a program to reverse a number using recursion.

def reverse_num(num,rev):

    if num == 0:
        return rev

    digit = num % 10
    rev = rev * 10 + digit 

    return reverse_num(num // 10, rev)

num = 12345
print(f"Reverse number of {num} is = ", reverse_num(num, 0))