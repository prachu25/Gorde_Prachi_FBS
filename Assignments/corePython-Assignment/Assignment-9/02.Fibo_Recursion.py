#  Write a program to print Fibonacci series using recursion.

def fibo(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num - 2)


n  = 2
print(f"Fibonacci of {n} is = ", fibo(n))