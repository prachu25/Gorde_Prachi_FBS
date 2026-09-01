# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_word = set()

# find unique words
for w in words:
    unique_word.add(w)

# Count frequency
for w in unique_word:
    cnt = 0

    for item in words:
        if w == item:
            cnt+=1

    print(w, cnt)


# print(unique_word)


