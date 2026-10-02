# Sum of all numbers between 1 to n

def sum_of_odd():

    n = int(input('Enter a  number: '))

    sum = 0
    i = 0
    while( i < n):

        if(i % 2 == 1):
            sum = sum + i
        i+=1


    print("Sum of Odd Number is = ", sum)


# Function Call
sum_of_odd()

        