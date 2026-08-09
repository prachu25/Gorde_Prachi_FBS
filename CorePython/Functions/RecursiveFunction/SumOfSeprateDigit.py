def sumOfDigit(num):

    if num == 0:
        return 0

    digit = num % 10
    return digit + sumOfDigit(num // 10)

num = 1234
res = sumOfDigit(num)
print("sum = ", res)

        
