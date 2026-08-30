# Write a Python program to count the number of lowercase characters present in a given string.
def count_lowercase(str):

    cnt = 0

    # ord() converts a character into its Unicode value
    for ch in str:
        if ord(ch) >=97 and ord(ch) <=122:
            cnt+=1

    return cnt

s = "Hello Word Python!"
res = count_lowercase(s)

print("Number of Lowercase Characters =", res)
