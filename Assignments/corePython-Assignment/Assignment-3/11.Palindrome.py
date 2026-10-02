# 11. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter 3-digit Number: '))

orignal = num
rev = 0

while num > 0:
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num // 10

if(rev == orignal):
    print('Number is Palindrome')
else:
    print('Number is Not Palindrome')
    