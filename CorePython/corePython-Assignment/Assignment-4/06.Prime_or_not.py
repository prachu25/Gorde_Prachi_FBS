# 6. WAP to check if a given number is prime number or not.

"""
A prime number is a number that has exactly two factors: 1 and itself.
"""


n = int(input('Enter a number to check prime or not: '))

i = 1
count = 0

while i <= n:
    
    if( n % i == 0):
        count = count + 1   
    
    i+=1

if (count == 2):
    print("Prime Number")
else:
    print("Not Prime Number")