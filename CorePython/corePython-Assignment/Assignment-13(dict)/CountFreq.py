# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = "apple banana apple orange banana apple"

words = text.split()  # split in comma
# print(words)

freq = {}

for word in words:

    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1

print(freq)