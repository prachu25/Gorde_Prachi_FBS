def CountEvenDigit(num):

    if num == 0:
        return 0

    digit = num % 10 

    if digit % 2 == 0:
        return 1 + CountEvenDigit(num // 10)
    else:
        return CountEvenDigit(num//10)


n = 2468
res = CountEvenDigit(n)
print("Output = ", res)