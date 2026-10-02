def evenRemove(lst):

    new_list = []

    for i in lst:
        if(i % 2 !=0):
            new_list.append(i)

    return new_list

lst = [1,2,3,4,5,6,7,8,9,10]
ans = evenRemove(lst)
print("After Removing Even =", ans)