def smallElement(lst):

    n = len(lst)

    for i in range(n-1):

        for j in range(n-1-i):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst[-3:]    # smallest element 

lst = [64,25,5,4,50,30]

ans = smallElement(lst)
print("Smallest Element =", ans)