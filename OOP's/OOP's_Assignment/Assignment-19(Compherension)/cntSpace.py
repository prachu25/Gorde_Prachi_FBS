# 3. Count the number of spaces in a string (take input from user)

text = input("Enter String: ")

space = [x for x in text if x == " "]

print(len(space))