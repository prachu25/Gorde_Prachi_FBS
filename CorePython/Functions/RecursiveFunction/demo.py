# Recursive Function

def series(n):
    if(n > 0):         # Base condition to stop infinite recursion
        print(n)
        series(n-1)


# function call
series(5)