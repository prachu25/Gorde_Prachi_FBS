# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replace_with_hypen(str):

    result = ""

    for ch in str:
        if ch == " ":
            result += "-"
        else:
            result += ch

    return result

str = "I like Java More than Python."
res = replace_with_hypen(str)
print(res)
