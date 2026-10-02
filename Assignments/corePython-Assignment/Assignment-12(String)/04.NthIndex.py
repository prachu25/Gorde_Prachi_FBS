# 2. Python Program to Remove the nth Index Character from a Non-Empty
def remove_nth_character(Str, index):

    res = ""

    for i in range(len(Str)):
        if i != index:
            res = res + Str[i]

    return res


s = "Python"
n = 3
result = remove_nth_character(s, n)
print(result)