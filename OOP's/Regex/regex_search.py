import re

# data = "my fav crickter is hitman, jersey number is 45"

# r = re.search(r"\d{2}", data)
# print(r)



s = "I love java programming  than Python"
result = re.search("Python",s)
print(result)



# search()  - anywhere
# match()   - beginning only