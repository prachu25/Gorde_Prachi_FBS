# Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive function0s

def fact(num):

    if num == 0:
        return 1

    return num * fact(num-1)


# n = 5
# print(f"factrial of {n} = ", fact(n))

def sumSeries(n):
    if n == 1:
        return 1

    return sumSeries(n-1) + fact(n)



n = int(input("Enter n: "))
print("sum =", sumSeries(n))

