# 7. Write a program to create a new list from existing list which contains cube of each number  of list.

def cubeList(lst):

    new_list = []

    for i in lst:
        new_list.append(i*i*i)

    return new_list

num_list = [1,2,3,4,5,6,7,8,9]
ans = cubeList(num_list)
print("CUBE LIST =", ans)