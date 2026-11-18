import re

s = "Hello World"

result = re.findall(r'\s', s)

print(result)

# \s -> white space char


# \S -> Non - white Space char

s1 = "Python World"

result = re.findall(r'\S', s1)

print(result)


q = re.findall(r"c.t", "cat cobt cuct dot")

print(q)


d = re.findall(r"\d{2,4}", "12 123 1234 12345")
print(d)

a = re.findall(r"[aeiou]", "I am good at java")
print(a)


b = re.findall(r"[^aeiou]", "I am good at java") # negation
print(b)





# \s   → whitespace
# \S   → non-whitespace

# \d   → digit
# \D   → non-digit

# \w   → word character
# \W   → non-word character