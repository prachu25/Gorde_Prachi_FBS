# 7. Write a program to find sum of digits of a number.

def sum_of_digit():

    num = int(input('Enter a number: '))

    sum = 0

    while(num > 0):
        digit = num % 10
        sum = sum + digit
        num = num // 10

    print("Sum of Digit =", sum)


# Function call
sum_of_digit()
        
