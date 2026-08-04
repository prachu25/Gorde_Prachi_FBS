# 6. Write a program to remove duplicates from the list.

lst = [10,20,20,30,40,40,50,30,60,70,70]

new_lst = []

for i in range(len(lst)):    # in / not in → checks whether an element exists inside a list.
    if lst[i] not in new_lst:
        new_lst.append(lst[i])

print(new_lst)       

