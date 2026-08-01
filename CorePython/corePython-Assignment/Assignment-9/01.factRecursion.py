# Write a program to find factorial using recursion.

def fact_recursion(num):

    if(num == 0):
        return 1

    return num * fact_recursion(num-1)

n = 5
res = fact_recursion(n)
print(f"Fcatorial of {n} = ",res)