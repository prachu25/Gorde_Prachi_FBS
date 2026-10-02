# 7. Python Program to Find the Intersection of Two Lists

def intersection_list(lst1, lst2):

    intersection = []

    for i in lst1:
        if i in lst2 and i not in intersection:
            intersection.append(i)

    return intersection

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

res = intersection_list(lst1,lst2)
print(res)