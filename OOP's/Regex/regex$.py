import re

r = re.search(r"Java$", "I am Good in Java")

if r == None:
    print("Not Matched")
else:
    print("Matched")


# $ check -> The pattern must occur at the end of the string.


# "Javaaaa"  if it is something like this in the end then it print not matched





# ^   → beginning of string
# $   → end of string