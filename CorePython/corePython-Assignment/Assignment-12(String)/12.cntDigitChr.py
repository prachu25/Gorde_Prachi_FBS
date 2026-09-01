# Write a Python program to count the number of digits and letters present in a given string.

def cnt_digit_chr(string):

    d_cnt = 0
    ch_cnt = 0

    for i in string:

        if '0' <= i <= '9':
            d_cnt += 1

        elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            ch_cnt += 1

    print("chr =", ch_cnt)
    print("digit =", d_cnt)




s = "python1234"
cnt_digit_chr(s)

