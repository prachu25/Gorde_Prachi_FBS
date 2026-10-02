# Python Program to Check if a Given Key Exists in a Dictionary or Not

student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

key = "city"

found = False

for k in student:

    if k == key:
        found = True
        break

if found:
    print('Key Exists')
else:
    print('Key does not exist')
