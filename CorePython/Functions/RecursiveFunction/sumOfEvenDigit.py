def sumEvenDigit(num):

    if num == 0:
        return 0

    digit = num % 10 

    if digit % 2 == 0:
        return digit + sumEvenDigit(num // 10)
    else:
        return sumEvenDigit(num//10)


n = 123456
res = sumEvenDigit(n)
print("Output = ", res)