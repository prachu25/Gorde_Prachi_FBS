# sum of prime numbers between 1 to n

def sum_of_prime():

    n = int(input('Enter a number: '))

    sum = 0
    i = 2

    while( i <=n ):
        count = 0
        j = 1

        while( j <= i):

            if i % j == 0:
                count +=1

            j+=1

        if count == 2:
            print(i)
            sum +=i

        i+=1

    print("Sum of Prime Number = ", sum)


# FUnction call
sum_of_prime()


            