def productDigit(num):

    if(num == 0):
        return 1

    digit = num % 10
    return digit * productDigit(num //10)


num = 1234
res = productDigit(num)
print("Product of Digit = ", res)