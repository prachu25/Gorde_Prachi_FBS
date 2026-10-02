# 13 . Write a program to print list after removing even numbers.

def removeEvenElement(lst):

    new_lst = []

    for i in lst:
        if i % 2 != 0 :
            new_lst.append(i)

    return new_lst



lst = [12,3,5,6,19,20,66,77,37,34,25,11,13]
ans = removeEvenElement(lst)
print(ans)
