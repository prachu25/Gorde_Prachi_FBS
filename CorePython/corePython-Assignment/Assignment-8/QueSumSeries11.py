"""
Write a program to find sum of following series using functions"""

# a. 1+ 2 + 3 + 4+..... + n
def sumOfDigitSeries():
    print("Welcome to Calculate the sum of digit")
    num = int(input('Enter a number: '))
    sum = 0

    i = 1
    while(i <= num):
        sum = sum + i
        i+=1

    print("SUM =", sum)

# Function call
sumOfDigitSeries()




# b. 1!+ 2! + 3! + 4!+..... + n!
def fact_sum():

    print()
    print("Calculate the sum of Factorial")
    num = int(input('Enter a number: '))
    sum = 0

    i = 1
    while(i <= num):
        fact = 1
        j = 1

        while j <= i:
            fact = fact * i
            j+=1

        print(fact)
        sum = sum + fact
        i+=1

    print("Sum =", sum)


# Function call
fact_sum()



# c. 1¹ + 2² + 3³ + ... + nⁿ
def power_sum():

    print()
    print("POWER SUM")
    num = int(input('Enter a number: '))
    sum = 0

    i = 1
    while(i <=num):
        sum = sum + (i ** i)
        i+=1

    print("sum  =", sum)


# function call
power_sum()




















