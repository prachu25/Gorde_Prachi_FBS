# Python Program to Sum All the Items in a Dictionary

data = {
    "a": 10,
    "b": 20,
    "c": 30
}

total = 0

for key in data:
    total += data[key]


print(total)