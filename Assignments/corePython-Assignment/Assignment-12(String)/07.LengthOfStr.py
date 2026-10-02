# Write a Python program to calculate the length of a given string without using the built-in len() function.

def length_of_String(str):

    cnt = 0

    for i in str:
        cnt+=1


    return cnt

s = "Pri"
res = length_of_String(s)
print("Length of String = ", res)