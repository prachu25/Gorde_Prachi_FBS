# 6. Write a program to find print the following Fibonacci series using functions: 
# 1 1 2 3 5 8 n terms

def fibonacci_series():

    num = int(input('Enter a number: '))

    first = 0
    second = 1

    i = 0

    while(i <num):
        print(first, end=" ")
        next = first + second
        first = second
        second = next

        i+=1


# Function call
fibonacci_series()

