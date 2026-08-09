def factorial(n):

    if(n > 0):
        return n * factorial(n-1)
    else:
        return 1

num = 7
res = factorial(num)
print(f"factorial of {num} = res ")


# digit seprate out
# sum of digit
# reverse digit
