# 6. Python Program to Find the Union of two Lists

def unino_list(lst1, lst2):

    union = []

    for i in lst1:
        if i not in union:
            union.append(i)

    for i in lst2:
        if i not in union:
            union.append(i)

    return union


# call function
lst1 = [1,2,3,4]
lst2 = [3,4,5,6,7]

res = unino_list(lst1, lst2)
print(res)

