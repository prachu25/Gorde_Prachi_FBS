# Given two sets of numbers, write a Python program to find the missing numbers 
# in the second set as compared to the first and vice versa. Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

missing_in_set2 = set()
missing_in_set1 = set()

# Numbers present in set1 but missing in set2

for n in set1:
    if n not in set2:
        missing_in_set2.add(n)


# Numbers present in set2 but missing in set1
for n in set2:
    if n not in set1:
        missing_in_set1.add(n)


print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)