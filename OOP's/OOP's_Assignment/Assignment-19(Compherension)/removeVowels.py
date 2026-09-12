# 4. Remove all of the vowels in a string (take input from user)

text = input("Enter a string: ")

remove_vowel = [x for x in text if x not in "aeiou"]
print(remove_vowel)


