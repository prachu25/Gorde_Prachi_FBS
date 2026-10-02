# 10. Write a program to remove all occurrences of a given element in the list.

def removeOccurences(lst, element):

    new_list = []

    for i in lst:
        if i != element:
            new_list.append(i)

    return new_list


lst = [1, 2, 3, 2, 4, 2, 5]
target = 2
res = removeOccurences(lst, target)
print(res)
