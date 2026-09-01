# Python Program to Remove the Given Key from a Dictionary

data = {
    "name": "John",
    "age": 20,
    "city": "Pune"
}

key = "age"

result = {}

for k in data:
    if k != key:
        result[k] = data[key]

print(result)





# Using Built in Method del

# if key in data:
#     del data[key]

# print(data)
