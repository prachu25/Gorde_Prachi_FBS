# Write a Python program to find all the anagrams and group them together from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for w in words:

    key = "".join(sorted(w))

    if key not in groups:
        groups[key] = []

    groups[key].append(w)




for grp in groups.values():
    print(grp)