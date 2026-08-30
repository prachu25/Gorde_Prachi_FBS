# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def dispaly_large_str(str1, str2):

    cnt_1str = 0
    cnt_2str = 0

    for ch in str1:
        cnt_1str += 1

    for ch in str2:
        cnt_2str += 1

    if cnt_1str > cnt_2str:
        return str1
    else:
        return str2



s1 = "Code"
s2 = "Programming"

res = dispaly_large_str(s1,s2)
print("Larger String =", res)
