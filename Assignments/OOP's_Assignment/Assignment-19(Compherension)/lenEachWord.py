# Use a dictionary comprehension to count the length of each word in a sentence (take input from user)


text = input("Enter a sentence: ")

result = {x: len(x) for x in text.split()}

print(result)