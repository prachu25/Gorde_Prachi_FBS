def digitSeprateOut(num):

    if(num > 0):
        digit = num % 10
        print(digit)
        digitSeprateOut(num // 10)


n = 1234
res = digitSeprateOut(n)
