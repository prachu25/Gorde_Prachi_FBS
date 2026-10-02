# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

def duplicateList(lst):

    new_list = []

    for  i in lst:
        new_list.append(i)

    return new_list

numbers = [10, 20, 30, 40]

copy_list = duplicateList(numbers)

print("Original =", numbers)
print("Duplicate =", copy_list)