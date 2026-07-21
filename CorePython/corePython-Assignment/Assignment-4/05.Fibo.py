# Q1. WAP to print Fibonacci series upto n.

n = int(input('Enter a number of term: '))

# fibo series is -> 0 1 1 2 3 5 8 13 ......

first = 0
second = 1

i = 0

while(i <= n):

    print(first, end=" ")
    next = first + second
    first = second
    second = next

    i+=1



