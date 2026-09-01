# 5. Python Program to Count the Number of Vowels in a String

def count_vowels(str):

    cnt = 0

    for i in str:
         if i in "aeiou":
              cnt+=1

    return cnt

string = "code"
res = count_vowels(string)
print("Vowel Cnt = ",res)