# 13 . Write a program to print list after removing even numbers.
lst = [12,3,5,6,19,20,66,77,37,34,25,11,13]

new_lst = []

for i in range(len(lst)):
    if(lst[i] % 2 != 0):
        new_lst.append(lst[i])

print("Removing Even Element in list")
print(new_lst)