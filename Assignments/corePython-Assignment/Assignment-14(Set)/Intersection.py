# Write a Python program to remove the intersection of a second set with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = set()

for n in set1:
    if n not in set2:
        result.add(n)


print(result)