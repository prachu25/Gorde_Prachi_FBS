# check the String is Palindrome or not  (Without using inbuilt methods, slicing)


def is_palindrome(str):

    rev = ""

    for ch  in str:
        rev = ch + rev

    if(str == rev):
        return True
    else:
        return False


s = "level"

print(is_palindrome(s))