# Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a string: ")

words = [x for x in text.split() if len(x) < 5]

print(words)