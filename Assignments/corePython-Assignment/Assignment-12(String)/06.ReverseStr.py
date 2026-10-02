# Write a Python program to reverse a given string without using any built-in reverse function.

def reverse_str(str):

    rev = ""

    for i in range(len(str)-1, -1,-1):
        rev = rev + str[i]

    return rev

s = "ihcarp"
res = reverse_str(s)
print(f"Reverse String = ", res)