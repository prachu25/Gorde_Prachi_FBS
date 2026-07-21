# 10. WAP to check if given number is Perfect Number.

"""
A Perfect Number is a number whose sum of its factors (excluding itself) 
is called perfect number.

EX: 6   
factors of 6: 1,2,3,6   
excluding 6
sum = 1 + 2 + 3 = 6    # called perfect number 

"""

num = int(input('Enter a number: '))

sum = 0
i = 1

while(i < num):

    if(num % i == 0):
        sum = sum + i

    i+=1


if(sum == num):
    print("Perfect Number")
else:
    print("Not Perfect Number")
     