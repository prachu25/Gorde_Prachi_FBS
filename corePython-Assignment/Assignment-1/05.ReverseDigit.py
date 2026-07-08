# write a program to reverse the three digit number

num = int(input('Enter a number to Reverse: '))

copy = num

rev = 0

# perfrom operation
while num >0:
    digit = num%10
    rev = rev * 10 + digit
    num = num//10

print(f'The Revser Digit {copy} is {rev}')