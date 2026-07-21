#  WAP to check if given number Strong Number.
# abc = a! + b! + c!

"""
A Strong Number is a number whose sum of the factorials 
of its digits is equal to the number itself.
"""


num = int(input('Enter a number: '))
orignal = num

sum = 0

while(num > 0):

    last_digit = num % 10

    fact = 1
    i = 1

    while(i <= last_digit):
        fact = fact * i
        i+=1
    
    sum = sum + fact
    num = num //10


if(sum == orignal):
    print('Strong Number')
else:
    print('Not Strong Number')

print()



