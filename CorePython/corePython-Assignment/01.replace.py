# Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_occurences(str):

    result = ""

    for ch in str:
        if ch == 'a':
            result += '$'
        else:
            result += ch

    return result


string = "banana"
res = replace_occurences(string)
print(res)

# OutPut = b$n$n$ 