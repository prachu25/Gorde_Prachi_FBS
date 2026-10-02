# Python Program to Multiply All the Items in a Dictionary

data = {
    "a": 2,
    "b": 3,
    "c": 4
}

result = 1

for key in data:
    result *= data[key]

print(result)