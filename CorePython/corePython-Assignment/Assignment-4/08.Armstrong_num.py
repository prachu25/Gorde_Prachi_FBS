# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 ,

"""
An Armstrong Number is a number in which the sum of the cubes 
of its digits is equal to the original number.
"""

num = int(input('Enter a number: '))
orignal = num

sum  = 0
cube = 1

while(num > 0):
    last_digit = num % 10
    cube = last_digit * last_digit * last_digit
    sum = sum + cube
    num=num//10


print("OUT_PUT number:", sum)

if(sum == orignal):
    print('Armstrong Number')
else:
    print('Not Armstrong Number')
