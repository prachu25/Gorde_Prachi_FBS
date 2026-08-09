def palindromeNumber():

    num = int(input('Enter a number: '))
    orignal = num

    rev= 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num //10

    if(rev == orignal):
        print("Palindrome Number")
    else:
        print("Not Palindrome")



palindromeNumber()