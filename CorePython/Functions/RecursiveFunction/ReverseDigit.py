def reverseDigit(num, rev):

    if num == 0:
        return rev

    digit = num % 10
    rev = rev * 10 + digit
    return reverseDigit(num // 10, rev)


    
i = reverseDigit(1234, 0)
print("Reverse Number = ",i)
