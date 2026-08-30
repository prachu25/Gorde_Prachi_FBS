# Python Program to Remove the Characters of Odd Index Values in a String

def removeOddIndex_chr(str):

    new_str = ""

    for i in range(len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]

    return new_str

s = "Python"
res = removeOddIndex_chr(s)
print("By Removing Odd Index Char =",res)
