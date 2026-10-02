# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def second_large(lst):

    n = len(lst)

    for i in range(0, n - 1):

        for j in range(0, n - 1 - i):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst[n-2]     # return second last element 


# call function
lst = [64,25,5,4,50,30]

ans = second_large(lst)
print("Second Large =", ans)
