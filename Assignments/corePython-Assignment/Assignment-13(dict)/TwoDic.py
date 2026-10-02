# Python Program to Concatenate Two Dictionaries Into One.

dict1 = {"name": "John", "age": 20}
dict2 = {"course": "Python", "city": "Pune"}

result = {}

for key in dict1:
    result[key] = dict1[key]


for key in dict2:
    result[key] = dict2[key]

print(result)