# Write a Python program to find elements in a given set that are not in another set.

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

result  = set()

for n in set1:
    if n not in set2:
        result.add(n)

print(result)






# BUILT IN METHODS

# res = set1 - set2
# print(res)

# s = set1.difference(set2)
# print(s)