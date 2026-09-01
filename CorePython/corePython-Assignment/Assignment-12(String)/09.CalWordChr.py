# Write a Python program to calculate the number of words and the number of characters present in a given string.
def cal_word_chr(str):

    chr_cnt = 0
    word_cnt = 1

    for ch in str:
        if ch != ' ':
            chr_cnt+=1
        else:
            word_cnt+=1

    print("Number of Charaters =", chr_cnt)
    print("Number of Characters =", word_cnt)


s = "Hello World"
re = cal_word_chr(s)






























"""
Input: Hello World

Output:
Number of Words = 2
Number of Characters = 11
"""
