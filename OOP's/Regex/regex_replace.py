import re

data = "Java is most powerful technology"

# re.sub() is used to find a pattern and replace it with something else.


res = re.sub("Java", "Python", data)

print(res)