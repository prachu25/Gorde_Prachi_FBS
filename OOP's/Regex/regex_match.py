import re


# It print the o/p bcz python is at the beginning
s = "Python is future technology"

result = re.match("Python",s)
print(result)


# It print  the None bcz match check only at the beginning 
s1 = "future technology is Python"

result1 = re.match("Python",s1)
print(result1)

# search()  - anywhere
# match()   - beginning only
