# Write a program to check if entered number is a palindrome or not.

def palindrome_num():

    n = int(input('Enter a number: '))
    dup = n

    rev = 0
    while(n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if(rev == dup):
        print("Palindrome number")
    else:
        print('Not Palindrome Number')


# Function call
palindrome_num()
