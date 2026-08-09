# Multiple Parameter
#1. why? To Pass Multiple Values to the function
#2. Mention astrick(*) Symbol befire parameter name in function defination     => *args
#3. Value Stroed in tuple formate
#4. Use for loop to assess values individully.

def mul_sum(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum

res = mul_sum(10,20,30,40)
print('addition =', res)