num = int(input('Enter a number: '))

orignal = num
rev =0

while(num > 0):
    last_digit = num%10
    rev = rev * 10 +last_digit
    num = num // 10

if(rev == orignal):
    print("Palindrome")
else:
    print("Not Palindrome ")

