# Write a program to check if given number is Armstrong or not using recursive function.

# count digit
def countDigits(n):
    if n == 0:
        return 0
    return 1 + countDigits(n // 10)



# Armstong Number
def armstrong_num(num,digits):

    if num == 0:
        return 0

    last_digit = num % 10
    return (last_digit ** digits) + armstrong_num(num //10, digits)


num = int(input('Enter a number: '))

digits = countDigits(num)
result = armstrong_num(num, digits)

if result == num:
    print(num, "is Armstrong Number")
else:
    print(num, "is NOT Armstrong Number")
    
















"""
Dry Run: 

countDigits(153)
= 1 + countDigits(15)

= 1 + (1 + countDigits(1))

= 1 + (1 + (1 + countDigits(0)))

= 1 + (1 + (1 + 0))

= 1 + (1 + 1)

= 1 + 2

= 3


"""