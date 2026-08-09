def strongNumber():
    num = int(input('Enter a number: '))
    dup = num

    sum = 0

    while(num > 0):
        digit = num % 10

        fact = 1
        i = 1
        while(i <= digit):
            fact = fact * i
            i+=1

        sum = sum + fact
        num = num //10

    if sum == dup:
        print("Strong Number")
    else:
        print("Not strong number")


# function callg
strongNumber()
    

